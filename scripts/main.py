"""
Main Pipeline - Orchestrates the entire GRC Intelligence workflow
"""

import os
import json
from datetime import datetime

from fetch_news import fetch_news, save_raw_articles
from score_articles import score_articles, save_scored_articles, get_top_articles
from generate_content import (
    init_gemini,
    generate_linkedin_post,
    generate_carousel,
    generate_newsletter,
    save_content
)


def ensure_directories():
    """Ensure required directories exist"""
    os.makedirs("data", exist_ok=True)
    os.makedirs("docs/data", exist_ok=True)


def run_pipeline():
    """Run the complete intelligence pipeline"""
    
    print("=" * 60)
    print(f"GRC Intelligence Pipeline - {datetime.now().isoformat()}")
    print("=" * 60)
    
    ensure_directories()
    
    # Step 1: Fetch news
    print("\n[1/4] Fetching news from RSS feeds...")
    articles = fetch_news()
    
    if not articles:
        print("No articles fetched. Using fallback content.")
        # Create fallback content
        fallback_article = {
            "title": "Daily GRC Insights",
            "summary": "Stay updated with the latest in Governance, Risk, and Compliance.",
            "url": "https://linkedin.com/in/sathya-sivam",
            "source": "GRC Copilot",
            "score": 8,
            "domains": ["GRC Career & Skills"],
            "published": datetime.now().isoformat()
        }
        articles = [fallback_article]
    
    save_raw_articles(articles)
    
    # Step 2: Score articles with Groq (fast)
    print("\n[2/4] Scoring articles with Groq AI...")
    scored_articles = score_articles(articles)
    save_scored_articles(scored_articles)
    
    # Step 3: Get top articles
    top_articles = get_top_articles(scored_articles, count=5)
    print(f"\nTop 5 articles:")
    for i, a in enumerate(top_articles, 1):
        print(f"  {i}. [{a['score']}] {a['title'][:60]}...")
    
    # Step 4: Generate content with Gemini (high quality)
    print("\n[3/4] Generating content with Gemini AI...")
    client = init_gemini()
    
    # Generate LinkedIn post
    print("  - Generating LinkedIn post...")
    linkedin_post = generate_linkedin_post(top_articles[0], client)
    save_content(linkedin_post, "data/linkedin_post.json")
    
    # Generate carousel
    print("  - Generating carousel content...")
    carousel = generate_carousel(top_articles[0], client)
    save_content(carousel, "data/carousel.json")
    
    # Generate newsletter (only on Tuesdays)
    print("  - Checking for newsletter generation...")
    newsletter = generate_newsletter(top_articles, client)
    if newsletter:
        save_content(newsletter, "data/newsletter.json")
        print("  - Newsletter generated for Wednesday!")
    else:
        # Keep existing newsletter if not Tuesday
        print("  - Keeping existing newsletter (not Tuesday)")
    
    # Step 5: Create summary
    print("\n[4/4] Creating summary...")
    summary = {
        "last_updated": datetime.now().isoformat(),
        "articles_fetched": len(articles),
        "articles_scored": len(scored_articles),
        "top_article": {
            "title": top_articles[0]['title'],
            "score": top_articles[0]['score'],
            "source": top_articles[0]['source']
        },
        "content_generated": {
            "linkedin_post": True,
            "carousel": True,
            "newsletter": newsletter is not None
        }
    }
    
    save_content(summary, "data/summary.json")
    
    print("\n" + "=" * 60)
    print("Pipeline completed successfully!")
    print("=" * 60)
    
    return summary


if __name__ == "__main__":
    run_pipeline()
