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


def parse_date_to_datetime(date_str: str) -> Optional[datetime]:
    """
    Convert various date formats to datetime object for proper comparison.
    
    Args:
        date_str: Date string in various formats
        
    Returns:
        datetime object if parsing succeeds, None otherwise
    """
    if not date_str or date_str == "unknown":
        return None
    
    # Handle relative time formats
    if "ago" in date_str.lower():
        try:
            now = datetime.now()
            if "hour" in date_str.lower():
                hours = int(re.findall(r"\d+", date_str)[0])
                return now - timedelta(hours=hours)
            elif "day" in date_str.lower():
                days = int(re.findall(r"\d+", date_str)[0])
                return now - timedelta(days=days)
            elif "week" in date_str.lower():
                weeks = int(re.findall(r"\d+", date_str)[0])
                return now - timedelta(weeks=weeks)
            elif "month" in date_str.lower():
                months = int(re.findall(r"\d+", date_str)[0])
                return now - timedelta(days=months * 30)
        except Exception:
            return None
    
    # Handle ISO 8601 format
    try:
        if "T" in date_str and ("+" in date_str or "Z" in date_str or date_str.endswith("00:00")):
            if "+" in date_str:
                date_part = date_str.split("+")[0]
            elif "Z" in date_str:
                date_part = date_str.replace("Z", "")
            else:
                date_part = date_str
            
            if "." in date_part:
                return datetime.strptime(date_part.split(".")[0], "%Y-%m-%dT%H:%M:%S")
            else:
                return datetime.strptime(date_part, "%Y-%m-%dT%H:%M:%S")
    except Exception:
        pass
    
    # Handle "May 31, 2025" format
    try:
        if "," in date_str and len(date_str.split()) >= 3:
            return datetime.strptime(date_str, "%b %d, %Y")
    except Exception:
        pass
    
    # Handle "2025-10-01" format
    try:
        if re.match(r"\d{4}-\d{2}-\d{2}$", date_str):
            return datetime.strptime(date_str, "%Y-%m-%d")
    except Exception:
        pass
    
    # Handle "2025-10-01 08:19:28" format
    try:
        if re.match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$", date_str):
            return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except Exception:
        pass
    
    return None


def parse_date_to_standard(date_str: str) -> str:
    """
    Convert various date formats to standard format (YYYY-MM-DD HH:MM:SS)
    
    DEPRECATED: Use parse_date_to_datetime for proper date comparisons.
    This function is kept for backward compatibility only.

    Args:
        date_str: Date string in various formats

    Returns:
        Standard format datetime string, such as "2025-10-01 08:19:28"
    """
    dt = parse_date_to_datetime(date_str)
    if dt is None:
        return "unknown"
    return dt.strftime("%Y-%m-%d %H:%M:%S")


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
            
            publish_time = response_dict["data"].get("publishedTime", "unknown")
            
            # CRITICAL: Validate publish_time against TODAY_DATE to prevent lookahead bias
            today_date_str = get_config_value("TODAY_DATE")
            if today_date_str and publish_time != "unknown":
                publish_dt = parse_date_to_datetime(publish_time)
                today_dt = parse_date_to_datetime(today_date_str)
                
                if publish_dt and today_dt:
                    if publish_dt > today_dt:
                        logger.warning(
                            f"🚫 LOOKAHEAD BIAS DETECTED: Article published on {publish_time} "
                            f"is AFTER current trading date {today_date_str}. URL: {url}"
                        )
                        print(
                            f"🚫 LOOKAHEAD BIAS BLOCKED: Rejecting future article from {publish_time} "
                            f"(current date: {today_date_str})"
                        )
                        return {
                            "url": url,
                            "content": "",
                            "error": f"Future information blocked: Article published on {publish_time}, after trading date {today_date_str}",
                            "blocked_by_lookahead_filter": True
                        }

            return {
                "url": response_dict["data"]["url"],
                "title": response_dict["data"]["title"],
                "description": response_dict["data"]["description"],
                "content": response_dict["data"]["content"],
                "publish_time": publish_time,
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
            today_date_str = get_config_value("TODAY_DATE")
            today_dt = parse_date_to_datetime(today_date_str) if today_date_str else None

            # Process search results, filter out content from TODAY_DATE and later
            for item in json_data.get("data", []):
                if "url" not in item:
                    continue

                url = item["url"]
                raw_date = item.get("date", "unknown")
                
                # Parse the date to datetime object for proper comparison
                article_dt = parse_date_to_datetime(raw_date)

                # If TODAY_DATE is not set (not in backtest mode), keep all results
                if not today_dt:
                    filtered_urls.append(url)
                    continue

                # If we can't parse the article date, be conservative during backtesting
                if article_dt is None:
                    # During backtesting, exclude unparseable dates to be safe
                    logger.warning(
                        f"⚠️ Unable to parse date '{raw_date}' for URL {url}. "
                        f"Excluding from results during backtesting (TODAY_DATE={today_date_str})"
                    )
                    blocked_urls.append((url, raw_date, "unparseable"))
                    continue

                # Check if article is published BEFORE or ON the current trading date
                if article_dt <= today_dt:
                    filtered_urls.append(url)
                else:
                    # Block future information
                    logger.warning(
                        f"🚫 LOOKAHEAD BIAS: Blocking URL {url} with publish date {raw_date} "
                        f"(parsed: {article_dt.strftime('%Y-%m-%d %H:%M:%S')}) "
                        f"which is AFTER trading date {today_date_str}"
                    )
                    blocked_urls.append((url, raw_date, "future"))

            # Log filtering statistics
            total_results = len(json_data.get("data", []))
            print(f"📊 Search filtering results: {len(filtered_urls)}/{total_results} URLs passed filter")
            if blocked_urls:
                print(f"🚫 Blocked {len(blocked_urls)} URLs due to lookahead bias:")
                for url, date, reason in blocked_urls[:3]:  # Show first 3
                    print(f"   - {url[:80]}... (date: {date}, reason: {reason})")
                if len(blocked_urls) > 3:
                    print(f"   ... and {len(blocked_urls) - 3} more")

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
        tool = WebScrapingJinaTool()
        results = tool(query)

        # Check if results are empty
        if not results:
            return f"⚠️ Search query '{query}' found no results. May be network issue or API limitation."

        # Convert results to string format
        formatted_results = []
        for result in results:
            if "error" in result:
                formatted_results.append(f"Error: {result['error']}")
            else:
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
            return f"⚠️ Search query '{query}' returned empty results."
        

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
