# Reddit Tech Monitor

Personal, non-commercial monitor of technology discussions, initially in r/TopologyAI.

## Status
Early prototype. Reddit API approval is pending; no live collection has been performed. AI summarization is planned, requires approval for that use case, and is not implemented.

## Prototype
Python 3 standard library. monitor.py makes one read-only OAuth request for up to 25 recent threads, printing titles and original Reddit links. It stores no content and performs no posting, voting or private-message access.

Set REDDIT_ACCESS_APPROVED=yes only after Reddit approves access. Supply REDDIT_ACCESS_TOKEN and an identifying REDDIT_USER_AGENT through environment variables, then run python monitor.py. Token issuance and refresh will be configured after approval. Never commit credentials.

## Planned features
- Collection approximately every 30 minutes within approved limits.
- Deduplication and personal digest with original links.
- AI summaries for personal reading, subject to approval and provider selection.
- Deletion checks and retention controls for content and summaries before enabling storage.

Documentation: https://www.reddit.com/dev/api/
