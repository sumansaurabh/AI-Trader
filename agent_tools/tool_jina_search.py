import logging
import os
from typing import Any, Dict, List, Optional

import requests
from dotenv import load_dotenv
from fastmcp import FastMCP

load_dotenv()
import json
import os
import random
import re
import sys
from datetime import datetime, timedelta

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.general_tools import get_config_value

logger = logging.getLogger(__name__)


def compare_dates(date1_str: str, date2_str: str) -> int:
    """
    Compare two date strings safely.
    
    Args:
        date1_str: First date string in format "YYYY-MM-DD HH:MM:SS" or "YYYY-MM-DD"
        date2_str: Second date string in format "YYYY-MM-DD HH:MM:SS" or "YYYY-MM-DD"
    
    Returns:
        -1 if date1 < date2
         0 if date1 == date2
         1 if date1 > date2
         None if comparison fails (unparseable dates)
    """
    try:
        # Extract just the date part (YYYY-MM-DD) for comparison
        date1_part = date1_str.split()[0] if ' ' in date1_str else date1_str
        date2_part = date2_str.split()[0] if ' ' in date2_str else date2_str
        
        # Parse dates
        dt1 = datetime.strptime(date1_part, "%Y-%m-%d")
        dt2 = datetime.strptime(date2_part, "%Y-%m-%d")
        
        if dt1 < dt2:
            return -1
        elif dt1 > dt2:
            return 1
        else:
            return 0
    except Exception as e:
        logger.warning(f"Failed to compare dates '{date1_str}' and '{date2_str}': {e}")
        return None


def is_date_valid_for_backtest(publish_date_str: str, today_date_str: str) -> bool:
    """
    Check if a publication date is valid for backtesting (not from the future).
    
    Args:
        publish_date_str: Publication date string
        today_date_str: Current simulation date string (TODAY_DATE)
    
    Returns:
        True if the publication date is on or before today_date, False otherwise
        Returns False if dates cannot be compared (fail-closed for safety)
    """
    if not publish_date_str or publish_date_str == "unknown":
        # Fail-closed: if we can't determine the date, exclude it
        logger.warning(f"⚠️ Unknown publication date - excluding for safety")
        return False
    
    if not today_date_str:
        # If TODAY_DATE is not set, we're not in backtest mode - allow all
        return True
    
    comparison = compare_dates(publish_date_str, today_date_str)
    
    if comparison is None:
        # Fail-closed: if we can't compare dates, exclude it
        logger.warning(f"⚠️ Cannot compare dates '{publish_date_str}' vs '{today_date_str}' - excluding for safety")
        return False
    
    # Return True only if publish_date <= today_date (comparison <= 0)
    return comparison <= 0


def parse_date_to_standard(date_str: str) -> str:
    """
    Convert various date formats to standard format (YYYY-MM-DD HH:MM:SS)

    Args:
        date_str: Date string in various formats, such as "2025-10-01T08:19:28+00:00", "4 hours ago", "1 day ago", "May 31, 2025"

    Returns:
        Standard format datetime string, such as "2025-10-01 08:19:28"
    """
    if not date_str or date_str == "unknown":
        return "unknown"

    # Handle relative time formats
    if "ago" in date_str.lower():
        try:
            now = datetime.now()
            if "hour" in date_str.lower():
                hours = int(re.findall(r"\d+", date_str)[0])
                target_date = now - timedelta(hours=hours)
            elif "day" in date_str.lower():
                days = int(re.findall(r"\d+", date_str)[0])
                target_date = now - timedelta(days=days)
            elif "week" in date_str.lower():
                weeks = int(re.findall(r"\d+", date_str)[0])
                target_date = now - timedelta(weeks=weeks)
            elif "month" in date_str.lower():
                months = int(re.findall(r"\d+", date_str)[0])
                target_date = now - timedelta(days=months * 30)  # Approximate handling
            else:
                return "unknown"
            return target_date.strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            pass

    # Handle ISO 8601 format, such as "2025-10-01T08:19:28+00:00"
    try:
        if "T" in date_str and ("+" in date_str or "Z" in date_str or date_str.endswith("00:00")):
            # Remove timezone information, keep only date and time part
            if "+" in date_str:
                date_part = date_str.split("+")[0]
            elif "Z" in date_str:
                date_part = date_str.replace("Z", "")
            else:
                date_part = date_str

            # Parse ISO format
            if "." in date_part:
                # Handle microseconds part, such as "2025-10-01T08:19:28.123456"
                parsed_date = datetime.strptime(date_part.split(".")[0], "%Y-%m-%dT%H:%M:%S")
            else:
                # Standard ISO format "2025-10-01T08:19:28"
                parsed_date = datetime.strptime(date_part, "%Y-%m-%dT%H:%M:%S")
            return parsed_date.strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        pass

    # Handle other common formats
    try:
        # Handle "May 31, 2025" format
        if "," in date_str and len(date_str.split()) >= 3:
            parsed_date = datetime.strptime(date_str, "%b %d, %Y")
            return parsed_date.strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        pass

    try:
        # Handle "2025-10-01" format
        if re.match(r"\d{4}-\d{2}-\d{2}$", date_str):
            parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
            return parsed_date.strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        pass

    # If unable to parse, return original string
    return date_str


class WebScrapingJinaTool:
    def __init__(self):
        self.api_key = os.environ.get("JINA_API_KEY")
        if not self.api_key:
            raise ValueError("Jina API key not provided! Please set JINA_API_KEY environment variable.")

    def __call__(self, query: str) -> List[Dict[str, Any]]:
        print(f"Searching for {query}")
        all_urls = self._jina_search(query)
        return_content = []
        print(f"Found {len(all_urls)} URLs")
        if len(all_urls) > 1:
            # Randomly select three to form new all_urls
            all_urls = random.sample(all_urls, 1)
        for url in all_urls:
            print(f"Scraping {url}")
            return_content.append(self._jina_scrape(url))
            print(f"Scraped {url}")

        return return_content

    def _jina_scrape(self, url: str) -> Dict[str, Any]:
        try:
            jina_url = f"https://r.jina.ai/{url}"
            headers = {
                "Accept": "application/json",
                "Authorization": self.api_key,
                "X-Timeout": "10",
                "X-With-Generated-Alt": "true",
            }
            response = requests.get(jina_url, headers=headers)

            if response.status_code != 200:
                raise Exception(f"Jina AI Reader Failed for {url}: {response.status_code}")

            response_dict = response.json()
            
            # Extract publish time and validate against TODAY_DATE
            raw_publish_time = response_dict["data"].get("publishedTime", "unknown")
            standardized_publish_time = parse_date_to_standard(raw_publish_time)
            
            # CRITICAL: Validate that this content is not from the future
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

            return {
                "url": response_dict["data"]["url"],
                "title": response_dict["data"]["title"],
                "description": response_dict["data"]["description"],
                "content": response_dict["data"]["content"],
                "publish_time": standardized_publish_time,
            }

        except Exception as e:
            logger.error(str(e))
            return {"url": url, "content": "", "error": str(e)}

    def _jina_search(self, query: str) -> List[str]:
        url = f"https://s.jina.ai/?q={query}&n=1"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "X-Respond-With": "no-content",
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # 检查HTTP状态码

            json_data = response.json()

            # Check if response data is valid
            if json_data is None:
                print(f"⚠️ Jina API returned empty data, query: {query}")
                return []

            if "data" not in json_data:
                print(f"⚠️ Jina API response format abnormal, query: {query}, response: {json_data}")
                return []

            all_urls = []
            filtered_urls = []
            blocked_urls = []

            # Get TODAY_DATE for filtering
            today_date = get_config_value("TODAY_DATE")

            # Process search results, filter out content from TODAY_DATE and later
            for item in json_data.get("data", []):
                if "url" not in item:
                    continue

                url = item["url"]
                all_urls.append(url)

                # Get publication date and convert to standard format
                raw_date = item.get("date", "unknown")
                standardized_date = parse_date_to_standard(raw_date)

                # Validate date against TODAY_DATE
                if today_date:
                    if is_date_valid_for_backtest(standardized_date, today_date):
                        filtered_urls.append(url)
                        logger.info(f"✅ Accepted: {url} (date: {standardized_date} <= {today_date})")
                    else:
                        blocked_urls.append(url)
                        logger.warning(
                            f"🚫 BLOCKED in search: {url} "
                            f"(date: {standardized_date} > {today_date})"
                        )
                else:
                    # If TODAY_DATE is not set, we're not in backtest mode - keep all results
                    filtered_urls.append(url)

            if today_date:
                print(
                    f"📊 Search filtering: {len(all_urls)} total URLs, "
                    f"{len(filtered_urls)} passed, {len(blocked_urls)} blocked (future dates)"
                )
            else:
                print(f"Found {len(filtered_urls)} URLs (no date filtering - TODAY_DATE not set)")
            
            return filtered_urls

        except requests.exceptions.RequestException as e:
            print(f"❌ Jina API request failed: {e}")
            return []
        except ValueError as e:
            print(f"❌ Jina API response parsing failed: {e}")
            return []
        except Exception as e:
            print(f"❌ Jina search unknown error: {e}")
            return []


mcp = FastMCP("Search")


@mcp.tool()
def get_information(query: str) -> str:
    """
    Use search tool to scrape and return main content information related to specified query in a structured way.

    Args:
        query: Key information or search terms you want to retrieve, will search for the most matching results on the internet.

    Returns:
        A string containing several retrieved web page contents, structured content includes:
        - URL: Original web page link
        - Title: Web page title
        - Description: Brief description of the web page
        - Publish Time: Content publication date (if available)
        - Content: Main text content of the web page (first 1000 characters)

        If scraping fails, returns corresponding error information.
    """
    try:
        today_date = get_config_value("TODAY_DATE")
        if today_date:
            logger.info(f"🔍 Searching with temporal filter: TODAY_DATE={today_date}, query='{query}'")
        
        tool = WebScrapingJinaTool()
        results = tool(query)

        # Check if results are empty
        if not results:
            return f"⚠️ Search query '{query}' found no results. May be network issue or API limitation."

        # Convert results to string format, filtering out blocked content
        formatted_results = []
        blocked_count = 0
        
        for result in results:
            # Skip results that were filtered due to future dates
            if result.get("filtered", False):
                blocked_count += 1
                logger.warning(f"🚫 Filtered result excluded from output: {result.get('url', 'unknown')}")
                continue
                
            if "error" in result and not result.get("filtered", False):
                formatted_results.append(f"Error: {result['error']}")
            elif "content" in result and result["content"]:
                formatted_results.append(
                    f"""
URL: {result['url']}
Title: {result['title']}
Description: {result['description']}
Publish Time: {result['publish_time']}
Content: {result['content'][:1000]}...
"""
                )

        if not formatted_results:
            if blocked_count > 0:
                return f"⚠️ Search query '{query}' returned {blocked_count} result(s), but all were filtered out due to future publication dates (after {today_date})."
            return f"⚠️ Search query '{query}' returned empty results."
        
        if blocked_count > 0 and today_date:
            logger.info(f"📊 Final results: {len(formatted_results)} included, {blocked_count} blocked (future dates)")

        # log_file = get_config_value("LOG_FILE")     
        # signature = get_config_value("SIGNATURE")
        # log_entry = {
        #     "signature": signature,
        #     "new_messages": [{"role": "tool:jinasearch", "content": "\n".join(formatted_results)}]
        # }
        # with open(log_file, "a", encoding="utf-8") as f:
        #     f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

        return "\n".join(formatted_results)

    except Exception as e:
        return f"❌ Search tool execution failed: {str(e)}"


if __name__ == "__main__":
    # Run with streamable-http, support configuring host and port through environment variables to avoid conflicts
    port = int(os.getenv("SEARCH_HTTP_PORT", "8001"))
    mcp.run(transport="streamable-http", port=port)
