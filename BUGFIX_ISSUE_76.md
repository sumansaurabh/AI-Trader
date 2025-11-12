# Bug Fix: Issue #76 - Future Information Leakage (Lookahead Bias)

## 🐛 Problem Description

During historical backtesting, the trading agent was able to retrieve news articles published on **future dates** (i.e., dates later than the current trading day). This allowed the agent to make decisions based on information that would be impossible to possess in real-time, completely invalidating the backtest results.

### Example from Bug Report

When running a backtest for trading day **2025-10-06**, the agent retrieved an article about AMD-OpenAI partnership that was published on **2025-10-10** (4 days in the future):

```
Publish Time: 2025-10-10T10:00:00.000Z
Title: AMD's Stock Surged 24% on Its OpenAI Partnership...
```

The agent then used this future information to make a buy decision, which is a clear case of lookahead bias.

## 🔍 Root Cause Analysis

The bug was caused by multiple issues in `agent_tools/tool_jina_search.py`:

### 1. **Incomplete Filtering Architecture**
- The `_jina_search` method filtered URLs based on dates during the search phase
- However, the `_jina_scrape` method did NOT validate the `publish_time` of scraped content
- This created a gap where future-dated content could slip through

### 2. **String Comparison Bug**
```python
# OLD CODE (BUGGY):
if today_date > standardized_date:  # String comparison!
    filtered_urls.append(item["url"])
```
This used string comparison instead of proper datetime comparison, which could fail for various date formats.

### 3. **Lenient Fallback (Fail-Open)**
```python
# OLD CODE (BUGGY):
if standardized_date == "unknown" or standardized_date == raw_date:
    filtered_urls.append(item["url"])  # Includes unparseable dates!
    continue
```
When dates couldn't be parsed, the system included the content rather than excluding it.

### 4. **No Post-Scrape Validation**
Even if a URL passed the initial filter, the actual scraped content's publish date was never validated against `TODAY_DATE`.

## ✅ Solution Implemented

### 1. **Proper Date Comparison Functions**

Added two new utility functions:

```python
def compare_dates(date1_str: str, date2_str: str) -> int:
    """
    Compare two date strings using proper datetime parsing.
    Returns: -1 (less), 0 (equal), 1 (greater), None (error)
    """
    # Extracts date part and uses datetime.strptime for accurate comparison
```

```python
def is_date_valid_for_backtest(publish_date_str: str, today_date_str: str) -> bool:
    """
    Check if a publication date is valid for backtesting.
    Returns False if dates cannot be compared (fail-closed for safety)
    """
    # Returns True only if publish_date <= today_date
```

### 2. **Dual-Layer Filtering**

#### Layer 1: Search Phase (`_jina_search`)
```python
# NEW CODE:
if today_date:
    if is_date_valid_for_backtest(standardized_date, today_date):
        filtered_urls.append(url)
        logger.info(f"✅ Accepted: {url} (date: {standardized_date} <= {today_date})")
    else:
        blocked_urls.append(url)
        logger.warning(f"🚫 BLOCKED in search: {url} (date: {standardized_date} > {today_date})")
```

#### Layer 2: Scrape Phase (`_jina_scrape`)
```python
# NEW CODE:
today_date = get_config_value("TODAY_DATE")
if today_date:
    if not is_date_valid_for_backtest(standardized_publish_time, today_date):
        logger.warning(
            f"🚫 FUTURE INFORMATION BLOCKED: Article from {standardized_publish_time} "
            f"(current backtest date: {today_date}) - URL: {url}"
        )
        return {
            "url": url,
            "content": "",
            "error": f"Future information filtered: publish_time={standardized_publish_time}, today={today_date}",
            "filtered": True
        }
```

### 3. **Fail-Closed Approach**

Unknown or unparseable dates are now **excluded** rather than included:

```python
if not publish_date_str or publish_date_str == "unknown":
    logger.warning(f"⚠️ Unknown publication date - excluding for safety")
    return False  # Fail-closed
```

### 4. **Enhanced Logging**

Added comprehensive logging throughout the filtering process:
- Search phase: logs accepted vs blocked URLs
- Scrape phase: logs future information blocks
- Final output: reports how many results were filtered

Example output:
```
📊 Search filtering: 5 total URLs, 3 passed, 2 blocked (future dates)
🚫 FUTURE INFORMATION BLOCKED: Article from 2025-10-10 10:00:00 (current backtest date: 2025-10-06)
📊 Final results: 3 included, 2 blocked (future dates)
```

## 🧪 Testing

Created comprehensive test suite (`test_date_filtering_simple.py`) that validates:

1. **Date Parsing**: Correctly handles ISO 8601, relative dates, etc.
2. **Date Comparison**: Proper datetime comparison (not string comparison)
3. **Backtest Validation**: Correctly identifies future vs past dates
4. **Bug Scenario**: Specifically tests the AMD article scenario from the bug report

### Test Results

```
✅ ALL TESTS PASSED!

The future information leakage bug (Issue #76) is FIXED.

Key improvements:
  1. Proper datetime comparison (not string comparison)
  2. Dual-layer filtering (search + scrape)
  3. Fail-closed approach (unknown dates are blocked)
  4. Comprehensive logging for transparency
```

## 📊 Impact

### Before Fix
- ❌ Agent could access future information during backtesting
- ❌ String comparison could fail for various date formats
- ❌ Unknown dates were included (fail-open)
- ❌ No validation after scraping content
- ❌ Backtest results were invalid due to lookahead bias

### After Fix
- ✅ Future information is strictly blocked at two layers
- ✅ Proper datetime comparison ensures accuracy
- ✅ Unknown dates are excluded (fail-closed for safety)
- ✅ Post-scrape validation catches any missed cases
- ✅ Backtest results are now scientifically valid

## 🔒 Security Considerations

The fix implements a **defense-in-depth** approach:

1. **Primary Defense**: Filter at search phase
2. **Secondary Defense**: Validate at scrape phase
3. **Tertiary Defense**: Filter in final output
4. **Fail-Closed**: When in doubt, exclude the content

This ensures that even if one layer fails, the others will catch future information leakage.

## 📝 Files Modified

1. **`agent_tools/tool_jina_search.py`**
   - Added `compare_dates()` function
   - Added `is_date_valid_for_backtest()` function
   - Modified `_jina_search()` to use proper date comparison
   - Modified `_jina_scrape()` to validate publish_time
   - Modified `get_information()` to filter blocked results
   - Enhanced logging throughout

## 🚀 Usage

No changes required to existing code. The fix is transparent to users:

```python
# Existing code continues to work
result = get_information("AMD OpenAI partnership October 2025")

# But now with proper temporal filtering:
# - If TODAY_DATE = "2025-10-06", articles from 2025-10-10 are blocked
# - Comprehensive logging shows what was filtered and why
```

## 🔮 Future Enhancements

Potential improvements for even more robust filtering:

1. **Configurable Strictness**: Allow users to choose fail-open vs fail-closed
2. **Date Source Priority**: Prefer article metadata over content-extracted dates
3. **Timezone Handling**: More sophisticated timezone normalization
4. **Performance**: Cache parsed dates to avoid repeated parsing
5. **Monitoring**: Add metrics for filtered content percentage

## 📚 References

- **GitHub Issue**: #76 - [Bug] Future Information Leakage (Lookahead Bias) in `get_information` Tool During Backtesting
- **Related PR**: #73 - Improved verbose logging of trading agent
- **Test Suite**: `test_date_filtering_simple.py`

## ✍️ Author

Fix implemented in response to detailed bug report with evidence from backtest logs.

## 📅 Date

November 12, 2025
