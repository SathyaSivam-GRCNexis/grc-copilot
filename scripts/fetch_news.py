"""
News Fetcher
"""

import feedparser
import json
from datetime import datetime, timedelta
from dateutil import parser as date_parser
from config import RSS_FEEDS

def fetch_news():
    """Fetch news from all RSS feeds"""
    articles = []
    cutoff_date = datetime.now() - timedelta(hours=24)
    
    for feed_url in RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_url)
            source_name = feed.feed.get('title', feed_url)
            
            for entry in feed.entries[:10]:  # Max 10 per feed
                # Parse publication date
                pub_date = None
                if hasattr(entry, 'published'):
                    try:
                        pub_date = date_parser.parse(entry.published)
                    except:
                        pub_date = datetime.now()
                elif hasattr(entry, 'updated'):
                    try:
                        pub_date = date_parser.parse(entry.updated)
                    except:
                        pub_date = datetime.now()
                else:
                    pub_date = datetime.now()
                
                # Make timezone naive for comparison
                if pub_date.tzinfo is not None:
                    pub_date = pub_date.replace(tzinfo=None)
                
                # Only include recent articles (last 24 hours)
                if pub_date < cutoff_date:
                    continue
                
                # Extract summary
                summary = ""
                if hasattr(entry, 'summary'):
                    summary = entry.summary
                elif hasattr(entry, 'description'):
                    summary = entry.description
                
                # Clean HTML from summary
                import re
                summary = re.sub(r'<[^>]+>', '', summary)
                summary = summary[:500]  # Limit length
                
                article = {
                    "title": entry.get('title', 'No Title'),
                    "url": entry.get('link', ''),
                    "summary": summary,
                    "source": source_name,
                    "published": pub_date.isoformat(),
                    "fetched_at": datetime.now().isoformat()
                }
                
                articles.append(article)
                
        except Exception as e:
            print(f"Error fetching {feed_url}: {e}")
            continue
    
    # Remove duplicates based on title similarity
    seen_titles = set()
    unique_articles = []
    for article in articles:
        title_key = article['title'].lower()[:50]
        if title_key not in seen_titles:
            seen_titles.add(title_key)
            unique_articles.append(article)
    
    print(f"Fetched {len(unique_articles)} unique articles from {len(RSS_FEEDS)} feeds")
    return unique_articles


def save_raw_articles(articles, filepath="data/raw_articles.json"):
    """Save raw articles to JSON file"""
    with open(filepath, 'w') as f:
        json.dump(articles, f, indent=2)
    print(f"Saved {len(articles)} raw articles to {filepath}")


if __name__ == "__main__":
    articles = fetch_news()
    save_raw_articles(articles)
