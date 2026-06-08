"""
Content Generator
"""

import os
import json
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


def generate_with_gemini(client, prompt):
    """Generate content using Gemini"""
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text


def generate_with_groq(client, prompt, max_tokens=4000):
    """Generate content using Groq"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a professional content writer. Write naturally, like a human expert sharing insights. Never use AI clichés."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content


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


def humanize_content(clients, draft):
    """Second pass: Remove AI tells and make more human"""
    
    humanize_prompt = f"""
Review this draft and rewrite it to sound MORE HUMAN and LESS like AI:

DRAFT:
{draft}

REMOVE these AI patterns if present:
- "In today's world" or similar openers
- Overuse of "leverage", "robust", "seamless", "delve"
- Perfect parallelism (rule of threes everywhere)
- Em-dash overuse
- Generic engagement questions like "Thoughts?"
- Overly formal or corporate language
- Perfect grammar (add some natural variation)

KEEP:
- The core message and structure
- Any good examples or analogies
- Genuine insights

Rewrite to sound like a real professional sharing their genuine thoughts.
Keep it the same length or slightly shorter.

REWRITTEN VERSION:
"""
    
    return generate_content(clients, humanize_prompt, max_tokens=2000)


def generate_linkedin_post(article, clients):
    """Generate humanized LinkedIn post from top article"""
    
    # First pass: Generate draft
    prompt = LINKEDIN_POST_PROMPT.format(
        voice_profile=VOICE_PROFILE,
        title=article['title'],
        summary=article['summary'],
        why_it_matters=article.get('score_reason', 'Important for GRC professionals'),
        url=article['url']
    )
    
    print("    Pass 1: Generating draft...")
    draft = generate_content(clients, prompt, max_tokens=1000)
    
    # Second pass: Humanize
    print("    Pass 2: Humanizing...")
    final_content = humanize_content(clients, draft)
    
    post_data = {
        "content": final_content,
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
    
    # Humanize the newsletter too
    print("    Humanizing newsletter...")
    content = humanize_content(clients, content)
    
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
