import os
import requests
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# 读取 API Key 和 cx
GOOGLE_API_KEY = os.getenv("GOOGLE_API")
CX = os.getenv("CX")

badwords = ["违禁词1", "违禁词2", "badword"]  # 你可以自行扩展

def contains_badword(text):
    if not text:
        return False
    for word in badwords:
        if word in text:
            return True
    return False

def google_search(query, api_key=GOOGLE_API_KEY, cx=CX):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": cx,
        "q": query
    }
    response = requests.get(url, params=params)
    results = response.json()
    items = results.get("items", [])
    # 过滤违禁词
    filtered = [item for item in items if not (contains_badword(item.get("title")) or contains_badword(item.get("snippet")))]
    print(filtered)
    return filtered

if __name__ == "__main__":
    query = "OpenAI"
    results = google_search(query)
    for item in results:
        print(item["title"], item["link"])