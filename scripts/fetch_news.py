"""
News Fetcher
"""

import feedparser
import json
import re
from datetime import datetime, timedelta
from dateutil import parser as date_parser
from config import RSS_FEEDS

# Custom headers to avoid being blocked
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (compatible; GRCBot/1.0; +https://github.com)'
}

def fetch_news():
    """Fetch news from all RSS feeds"""
    articles = []
    cutoff_date = datetime.now() - timedelta(hours=48)  # Extended to 48 hours for more content
    
    successful_feeds = 0
    failed_feeds = 0
    
    for feed_url in RSS_FEEDS:
        try:
            # Parse feed with custom agent
            feed = feedparser.parse(feed_url, agent=HEADERS['User-Agent'])
            
            if feed.bozo and not feed.entries:
                print(f"  [SKIP] {feed_url[:50]}... (parse error)")
                failed_feeds += 1
                continue
            
            source_name = feed.feed.get('title', extract_domain(feed_url))
            entries_added = 0
            
            for entry in feed.entries[:10]:  # Max 10 per feed
                # Parse publication date
                pub_date = parse_date(entry)
                
                # Make timezone naive for comparison
                if pub_date.tzinfo is not None:
                    pub_date = pub_date.replace(tzinfo=None)
                
                # Only include recent articles
                if pub_date < cutoff_date:
                    continue
                
                # Extract and clean summary
                summary = extract_summary(entry)
                
                # Skip if no meaningful content
                if len(summary) < 20:
                    continue
                
                article = {
                    "title": clean_text(entry.get('title', 'No Title')),
                    "url": entry.get('link', ''),
                    "summary": summary,
                    "source": source_name,
                    "published": pub_date.isoformat(),
                    "fetched_at": datetime.now().isoformat()
                }
                
                articles.append(article)
                entries_added += 1
            
            if entries_added > 0:
                print(f"  [OK] {source_name}: {entries_added} articles")
                successful_feeds += 1
            else:
                print(f"  [EMPTY] {source_name}: no recent articles")
                
        except Exception as e:
            print(f"  [ERROR] {feed_url[:40]}...: {str(e)[:50]}")
            failed_feeds += 1
            continue
    
    # Remove duplicates based on title similarity
    unique_articles = deduplicate(articles)
    
    print(f"\nFeed Summary: {successful_feeds} successful, {failed_feeds} failed")
    print(f"Articles: {len(articles)} total, {len(unique_articles)} unique")
    
    return unique_articles


def extract_domain(url):
    """Extract domain name from URL for source naming"""
    try:
        from urllib.parse import urlparse
        domain = urlparse(url).netloc
        # Remove www. and .com/.org etc
        domain = domain.replace('www.', '')
        parts = domain.split('.')
        if len(parts) >= 2:
            return parts[-2].title()
        return domain.title()
    except:
        return "Unknown"


def parse_date(entry):
    """Parse publication date from feed entry"""
    pub_date = None
    
    for date_field in ['published', 'updated', 'created', 'pubDate']:
        if hasattr(entry, date_field) and getattr(entry, date_field):
            try:
                pub_date = date_parser.parse(getattr(entry, date_field))
                break
            except:
                continue
    
    if pub_date is None:
        pub_date = datetime.now()
    
    return pub_date


def extract_summary(entry):
    """Extract and clean summary from feed entry"""
    summary = ""
    
    # Try different fields
    for field in ['summary', 'description', 'content']:
        if hasattr(entry, field):
            content = getattr(entry, field)
            if isinstance(content, list) and len(content) > 0:
                content = content[0].get('value', '')
            if content:
                summary = content
                break
    
    # Clean HTML
    summary = re.sub(r'<[^>]+>', '', summary)
    # Clean extra whitespace
    summary = re.sub(r'\s+', ' ', summary).strip()
    # Limit length
    summary = summary[:600]
    
    return summary


def clean_text(text):
    """Clean text of special characters"""
    if not text:
        return ""
    # Remove zero-width characters
    text = re.sub(r'[\u200b\u200c\u200d\u2060\ufeff]', '', text)
    # Clean extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def deduplicate(articles):
    """Remove duplicate articles based on title similarity"""
    seen_titles = set()
    unique_articles = []
    
    for article in articles:
        # Create a normalized key from title
        title_key = article['title'].lower()
        # Remove common words and punctuation
        title_key = re.sub(r'[^\w\s]', '', title_key)
        title_key = ' '.join(title_key.split()[:8])  # First 8 words
        
        if title_key not in seen_titles and len(title_key) > 10:
            seen_titles.add(title_key)
            unique_articles.append(article)
    
    return unique_articles


def save_raw_articles(articles, filepath="data/raw_articles.json"):
    """Save raw articles to JSON file"""
    with open(filepath, 'w') as f:
        json.dump(articles, f, indent=2)
    print(f"Saved {len(articles)} raw articles to {filepath}")


if __name__ == "__main__":
    print("Fetching news from RSS feeds...")
    articles = fetch_news()
    save_raw_articles(articles)
