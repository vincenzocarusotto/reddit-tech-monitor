"""Read-only prototype. Approval required. AI summaries not yet implemented."""
import json
import os
import sys
from urllib.request import Request, urlopen

if os.environ.get("REDDIT_ACCESS_APPROVED") != "yes":
    sys.exit("Disabled: obtain Reddit approval before enabling access.")
token = os.environ.get("REDDIT_ACCESS_TOKEN")
agent = os.environ.get("REDDIT_USER_AGENT")
if not token or not agent:
    sys.exit("Set REDDIT_ACCESS_TOKEN and REDDIT_USER_AGENT.")
request = Request("https://oauth.reddit.com/r/TopologyAI/new?limit=25&raw_json=1",
                  headers={"Authorization": f"Bearer {token}", "User-Agent": agent})
with urlopen(request, timeout=30) as response:
    listing = json.load(response)
for item in listing["data"]["children"]:
    post = item["data"]
    print(json.dumps({"id": post["id"], "title": post["title"],
          "url": "https://www.reddit.com" + post["permalink"]}, ensure_ascii=False))
