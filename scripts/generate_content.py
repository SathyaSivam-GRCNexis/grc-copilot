"""
Content Generator with Rate Limit Handling
"""

import os
import json
import time
from datetime import datetime
from groq import Groq
from config import (
    VOICE_PROFILE, 
    LINKEDIN_POST_PROMPT, 
    CAROUSEL_PROMPT, 
    NEWSLETTER_PROMPT,
    NEWSLETTER_SERIES
)

# Try to import Gemini
GEMINI_AVAILABLE = False
try:
    from google import genai
    GEMINI_AVAILABLE = True
except ImportError:
    pass


def init_clients():
    """Initialize AI clients"""
    clients = {
        "groq": Groq(api_key=os.environ.get("GROQ_API_KEY"))
    }
    
    if GEMINI_AVAILABLE and os.environ.get("GEMINI_API_KEY"):
        try:
            clients["gemini"] = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
        except:
            pass
    
    return clients


def generate_with_gemini(client, prompt, retries=3):
    """Generate content using Gemini with retries"""
    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            return response.text
        except Exception as e:
            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                if attempt < retries - 1:
                    wait_time = (attempt + 1) * 30
                    print(f"    Gemini rate limited, waiting {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    raise
            else:
                raise


def generate_with_groq(client, prompt, max_tokens=4000, retries=3):
    """Generate content using Groq with retries"""
    # Use smaller model for better rate limits
    models = ["llama-3.1-8b-instant", "llama-3.3-70b-versatile"]
    
    for model in models:
        for attempt in range(retries):
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": "You are a professional content writer. Write naturally, like a human expert sharing insights. Never use AI clichés."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=max_tokens
                )
                return response.choices[0].message.content
            except Exception as e:
                if "429" in str(e) or "rate_limit" in str(e).lower():
                    if attempt < retries - 1:
                        wait_time = (attempt + 1) * 20
                        print(f"    Groq rate limited on {model}, waiting {wait_time}s...")
                        time.sleep(wait_time)
                    else:
                        print(f"    {model} exhausted, trying next model...")
                        break
                else:
                    raise
    
    raise Exception("All models rate limited")


def generate_content(clients, prompt, max_tokens=4000):
    """Generate content - try Gemini first, fall back to Groq"""
    
    # Try Gemini first
    if "gemini" in clients:
        try:
            print("    Using Gemini...")
            return generate_with_gemini(clients["gemini"], prompt)
        except Exception as e:
            print(f"    Gemini failed ({str(e)[:50]}...), falling back to Groq...")
    
    # Fall back to Groq
    print("    Using Groq...")
    return generate_with_groq(clients["groq"], prompt, max_tokens)


def generate_linkedin_post(article, clients):
    """Generate humanized LinkedIn post from top article"""
    
    prompt = LINKEDIN_POST_PROMPT.format(
        voice_profile=VOICE_PROFILE,
        title=article['title'],
        summary=article['summary'],
        why_it_matters=article.get('score_reason', 'Important for GRC professionals'),
        url=article['url']
    )
    
    print("    Generating LinkedIn post...")
    content = generate_content(clients, prompt, max_tokens=1000)
    
    post_data = {
        "content": content,
        "based_on": {
            "title": article['title'],
            "url": article['url'],
            "source": article['source'],
            "score": article['score'],
            "why_it_matters": article.get('score_reason', '')
        },
        "generated_at": datetime.now().isoformat(),
        "type": "text_post"
    }
    
    return post_data


def generate_carousel(article, clients):
    """Generate carousel content from top article"""
    
    prompt = CAROUSEL_PROMPT.format(
        voice_profile=VOICE_PROFILE,
        title=article['title'],
        summary=article['summary']
    )
    
    print("    Generating carousel...")
    content = generate_content(clients, prompt, max_tokens=1500)
    
    # Parse slides from response
    slides = []
    current_slide = None
    
    for line in content.split('\n'):
        line = line.strip()
        if line.upper().startswith('SLIDE'):
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
        "raw_content": content,
        "based_on": {
            "title": article['title'],
            "url": article['url'],
            "source": article['source']
        },
        "generated_at": datetime.now().isoformat(),
        "type": "carousel"
    }
    
    return carousel_data


def generate_newsletter(top_articles, clients, config_path="data/newsletter_config.json"):
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
        topic = topics_queue[0]
        topics_used = []
    
    # Create news context from top articles
    news_context = "\n".join([
        f"- {a['title']} ({a['source']})\n  Why it matters: {a.get('score_reason', 'N/A')}"
        for a in top_articles[:5]
    ])
    
    prompt = NEWSLETTER_PROMPT.format(
        voice_profile=VOICE_PROFILE,
        series_name=NEWSLETTER_SERIES["name"],
        episode_number=current_episode,
        topic=topic,
        news_context=news_context
    )
    
    print("    Generating newsletter...")
    content = generate_content(clients, prompt, max_tokens=4000)
    
    newsletter_data = {
        "title": topic,
        "series": NEWSLETTER_SERIES["name"],
        "episode": current_episode,
        "content": content,
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
    clients = init_clients()
    
    with open("data/articles.json", "r") as f:
        articles = json.load(f)
    
    if articles:
        top_article = articles[0]
        
        post = generate_linkedin_post(top_article, clients)
        save_content(post, "data/linkedin_post.json")
        
        carousel = generate_carousel(top_article, clients)
        save_content(carousel, "data/carousel.json")
        
        newsletter = generate_newsletter(articles[:5], clients)
        if newsletter:
            save_content(newsletter, "data/newsletter.json")
