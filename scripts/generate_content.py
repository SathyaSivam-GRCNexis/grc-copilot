"""
Content Generator - Uses Gemini to generate LinkedIn posts, carousels, and newsletters
"""

import os
import json
from datetime import datetime
import google.generativeai as genai
from config import (
    VOICE_PROFILE, 
    LINKEDIN_POST_PROMPT, 
    CAROUSEL_PROMPT, 
    NEWSLETTER_PROMPT,
    NEWSLETTER_SERIES
)

def init_gemini():
    """Initialize Gemini API"""
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
    return genai.GenerativeModel('gemini-1.5-flash-latest')


def generate_linkedin_post(article, model):
    """Generate LinkedIn post from top article"""
    
    prompt = LINKEDIN_POST_PROMPT.format(
        voice_profile=VOICE_PROFILE,
        title=article['title'],
        summary=article['summary'],
        url=article['url']
    )
    
    response = model.generate_content(prompt)
    
    post_data = {
        "content": response.text,
        "based_on": {
            "title": article['title'],
            "url": article['url'],
            "source": article['source'],
            "score": article['score']
        },
        "generated_at": datetime.now().isoformat(),
        "type": "text_post"
    }
    
    return post_data


def generate_carousel(article, model):
    """Generate carousel content from top article"""
    
    prompt = CAROUSEL_PROMPT.format(
        voice_profile=VOICE_PROFILE,
        title=article['title'],
        summary=article['summary']
    )
    
    response = model.generate_content(prompt)
    
    # Parse slides from response
    slides = []
    current_slide = None
    
    for line in response.text.split('\n'):
        line = line.strip()
        if line.startswith('SLIDE'):
            if current_slide:
                slides.append(current_slide)
            current_slide = {"slide_number": len(slides) + 1, "content": ""}
        elif current_slide is not None:
            if line:
                current_slide["content"] += line + "\n"
    
    if current_slide:
        slides.append(current_slide)
    
    carousel_data = {
        "slides": slides,
        "raw_content": response.text,
        "based_on": {
            "title": article['title'],
            "url": article['url'],
            "source": article['source']
        },
        "generated_at": datetime.now().isoformat(),
        "type": "carousel"
    }
    
    return carousel_data


def generate_newsletter(top_articles, model, config_path="data/newsletter_config.json"):
    """Generate newsletter content (only on Tuesdays)"""
    
    # Check if today is Tuesday
    today = datetime.now()
    if today.weekday() != 1:  # 1 = Tuesday
        print("Not Tuesday - skipping newsletter generation")
        return None
    
    # Load or initialize newsletter config
    try:
        with open(config_path, 'r') as f:
            newsletter_config = json.load(f)
    except FileNotFoundError:
        newsletter_config = {
            "current_episode": NEWSLETTER_SERIES["current_episode"],
            "topics_used": []
        }
    
    # Get next topic
    current_episode = newsletter_config["current_episode"]
    topics_queue = NEWSLETTER_SERIES["topics_queue"]
    topics_used = newsletter_config.get("topics_used", [])
    
    # Find next unused topic
    topic = None
    for t in topics_queue:
        if t not in topics_used:
            topic = t
            break
    
    if not topic:
        # Reset if all topics used
        topic = topics_queue[0]
        topics_used = []
    
    # Create news context from top articles
    news_context = "\n".join([
        f"- {a['title']} ({a['source']}, Score: {a['score']})"
        for a in top_articles[:5]
    ])
    
    prompt = NEWSLETTER_PROMPT.format(
        voice_profile=VOICE_PROFILE,
        series_name=NEWSLETTER_SERIES["name"],
        episode_number=current_episode,
        topic=topic,
        news_context=news_context
    )
    
    response = model.generate_content(prompt)
    
    newsletter_data = {
        "title": topic,
        "series": NEWSLETTER_SERIES["name"],
        "episode": current_episode,
        "content": response.text,
        "top_news_context": [
            {"title": a['title'], "source": a['source'], "score": a['score']}
            for a in top_articles[:5]
        ],
        "generated_at": datetime.now().isoformat(),
        "publish_on": "Wednesday",
        "type": "newsletter"
    }
    
    # Update config
    newsletter_config["current_episode"] = current_episode + 1
    newsletter_config["topics_used"] = topics_used + [topic]
    newsletter_config["last_generated"] = datetime.now().isoformat()
    
    with open(config_path, 'w') as f:
        json.dump(newsletter_config, f, indent=2)
    
    return newsletter_data


def save_content(content, filepath):
    """Save generated content to JSON file"""
    with open(filepath, 'w') as f:
        json.dump(content, f, indent=2)
    print(f"Saved content to {filepath}")


if __name__ == "__main__":
    # Test with sample data
    model = init_gemini()
    
    with open("data/articles.json", "r") as f:
        articles = json.load(f)
    
    if articles:
        top_article = articles[0]
        
        post = generate_linkedin_post(top_article, model)
        save_content(post, "data/linkedin_post.json")
        
        carousel = generate_carousel(top_article, model)
        save_content(carousel, "data/carousel.json")
        
        newsletter = generate_newsletter(articles[:5], model)
        if newsletter:
            save_content(newsletter, "data/newsletter.json")
