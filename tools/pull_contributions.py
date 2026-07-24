# tools/pull_contributions.py
import json
import httpx
from bs4 import BeautifulSoup

USERNAME = "ubada-devops"

def fetch_contributions():
    url = f"https://github.com/users/{USERNAME}/contributions"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = httpx.get(url, headers=headers)
    if response.status_code != 200:
        raise RuntimeError(f"Failed to fetch contributions: HTTP {response.status_code}")
        
    soup = BeautifulSoup(response.text, "html.parser")
    cells = soup.find_all("td", attrs={"data-date": True})
    
    calendar = []
    for cell in cells:
        date = cell.get("data-date")
        level = int(cell.get("data-level", "0"))
        calendar.append({"date": date, "level": level})
        
    with open("assets/contributions.json", "w") as f:
        json.dump(calendar, f, indent=2)
    print(f"📈 Saved {len(calendar)} contribution days to assets/contributions.json")

if __name__ == "__main__":
    fetch_contributions()