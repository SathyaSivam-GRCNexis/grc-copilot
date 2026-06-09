"""
Content Generator with Engagement-Optimized Templates
"""

import os
import json
import time
import random
from datetime import datetime
from groq import Groq
from config import (
    VOICE_PROFILE, 
    LINKEDIN_POST_PROMPT,
    INSIGHT_POST_PROMPT,
    CONTRARIAN_POST_PROMPT,
    CAREER_POST_PROMPT,
    MISTAKE_POST_PROMPT,
    FRAMEWORK_POST_PROMPT,
    NEWS_ANALYSIS_POST_PROMPT,
    PERSONAL_STORY_POST_PROMPT,
    CAROUSEL_PROMPT, 
    NEWSLETTER_PROMPT,
    NEWSLETTER_SERIES,
    POST_TEMPLATES,
    DAY_TEMPLATE_ROTATION,
    DOMAIN_HOOKS
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


def get_template_for_today():
    """Get the post template based on day of week"""
    today = datetime.now().weekday()  # 0=Monday, 6=Sunday
    template_key = DAY_TEMPLATE_ROTATION.get(today, "insight")
    return template_key, POST_TEMPLATES.get(template_key, POST_TEMPLATES["insight"])


def get_domain_hooks(domain):
    """Get hook examples for a specific domain"""
    hooks = DOMAIN_HOOKS.get(domain, DOMAIN_HOOKS.get("GRC", []))
    return "\n".join(f"• {hook}" for hook in hooks[:5])


def get_template_prompt(template_key):
    """Get the specific prompt for a template type"""
    prompts = {
        "insight": INSIGHT_POST_PROMPT,
        "contrarian": CONTRARIAN_POST_PROMPT,
        "career": CAREER_POST_PROMPT,
        "mistake": MISTAKE_POST_PROMPT,
        "framework": FRAMEWORK_POST_PROMPT,
        "news_analysis": NEWS_ANALYSIS_POST_PROMPT,
        "personal_story": PERSONAL_STORY_POST_PROMPT
    }
    return prompts.get(template_key, INSIGHT_POST_PROMPT)


def generate_linkedin_post(article, clients):
    """Generate engagement-optimized LinkedIn post using day-appropriate template"""
    
    # Get today's template
    template_key, template_info = get_template_for_today()
    
    # Get primary domain
    domains = article.get('domains', ['GRC'])
    primary_domain = domains[0] if domains else 'GRC'
    
    # Get domain-specific hooks
    hooks = get_domain_hooks(primary_domain)
    
    # Get the template-specific prompt
    template_prompt = get_template_prompt(template_key)
    
    prompt = template_prompt.format(
        voice_profile=VOICE_PROFILE,
        title=article['title'],
        domain=primary_domain,
        why_it_matters=article.get('why_it_matters', article.get('score_reason', 'Important for GRC professionals')),
        domain_hooks=hooks
    )
    
    print(f"    Using {template_info['name']} template for {primary_domain}...")
    print(f"    Generating engagement-optimized LinkedIn post...")
    content = generate_content(clients, prompt, max_tokens=1000)
    
    post_data = {
        "content": content,
        "template_used": template_key,
        "template_name": template_info['name'],
        "inspired_by": {
            "topic": article['title'],
            "concept": article.get('why_it_matters', article.get('score_reason', '')),
            "domains": domains
        },
        "domain": primary_domain,
        "generated_at": datetime.now().isoformat(),
        "day_of_week": datetime.now().strftime("%A"),
        "type": "text_post",
        "copyright_safe": True
    }
    
    return post_data


def generate_all_domain_posts(articles, clients):
    """Generate one post per domain using different templates"""
    
    # Only generate for the 6 defined domains
    VALID_DOMAINS = ["GRC", "Privacy", "Security", "DevSecOps", "AI", "Product"]
    
    # Group articles by domain
    domain_articles = {}
    for article in articles:
        domains = article.get('domains', ['GRC'])
        for domain in domains:
            # Only add if it's a valid domain
            if domain in VALID_DOMAINS:
                if domain not in domain_articles:
                    domain_articles[domain] = []
                domain_articles[domain].append(article)
    
    # Templates to rotate through
    template_keys = list(POST_TEMPLATES.keys())
    
    all_posts = []
    
    for i, (domain, domain_arts) in enumerate(domain_articles.items()):
        if not domain_arts:
            continue
            
        # Pick best article for this domain
        best_article = max(domain_arts, key=lambda x: x.get('total_score', 0))
        
        # Rotate template for variety
        template_key = template_keys[i % len(template_keys)]
        template_info = POST_TEMPLATES[template_key]
        
        # Get domain-specific hooks
        hooks = get_domain_hooks(domain)
        
        # Get the template-specific prompt
        template_prompt = get_template_prompt(template_key)
        
        prompt = template_prompt.format(
            voice_profile=VOICE_PROFILE,
            title=best_article['title'],
            domain=domain,
            why_it_matters=best_article.get('why_it_matters', best_article.get('score_reason', '')),
            domain_hooks=hooks
        )
        
        print(f"    Generating {template_info['name']} for {domain}...")
        
        try:
            content = generate_content(clients, prompt, max_tokens=1000)
            
            post_data = {
                "content": content,
                "template_used": template_key,
                "template_name": template_info['name'],
                "domain": domain,
                "inspired_by": {
                    "topic": best_article['title'],
                    "concept": best_article.get('why_it_matters', ''),
                },
                "generated_at": datetime.now().isoformat(),
                "type": "text_post",
                "copyright_safe": True
            }
            
            all_posts.append(post_data)
            
            # Rate limit protection
            time.sleep(2)
            
        except Exception as e:
            print(f"    Error generating post for {domain}: {e}")
            continue
    
    return all_posts


def generate_carousel(article, clients):
    """Generate original educational carousel (copyright-safe)"""
    
    prompt = CAROUSEL_PROMPT.format(
        voice_profile=VOICE_PROFILE,
        title=article['title'],
        summary=article.get('score_reason', article['summary'])
    )
    
    print("    Generating original carousel...")
    content = generate_content(clients, prompt, max_tokens=1500)
    
    # Parse slides from response
    slides = []
    current_slide = None
    
    for line in content.split('\n'):
        line = line.strip()
        if line.upper().startswith('SLIDE') or line.startswith('**SLIDE'):
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
        "inspired_by": {
            "topic": article['title'],
            "domains": article.get('domains', ['GRC'])
        },
        "generated_at": datetime.now().isoformat(),
        "type": "carousel",
        "copyright_safe": True
    }
    
    return carousel_data


def generate_newsletter(top_articles, clients, config_path="data/newsletter_config.json"):
    """Generate original newsletter content (only on Tuesdays) - copyright-safe"""
    
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
    
    # Create thematic context from top articles (concepts only, not content)
    news_context = "\n".join([
        f"- Theme: {a.get('score_reason', a['title'][:50])}"
        for a in top_articles[:5]
    ])
    
    prompt = NEWSLETTER_PROMPT.format(
        voice_profile=VOICE_PROFILE,
        series_name=NEWSLETTER_SERIES["name"],
        episode_number=current_episode,
        topic=topic,
        news_context=news_context
    )
    
    print("    Generating original newsletter...")
    content = generate_content(clients, prompt, max_tokens=4000)
    
    newsletter_data = {
        "title": topic,
        "series": NEWSLETTER_SERIES["name"],
        "episode": current_episode,
        "content": content,
        "themes_this_week": [
            a.get('score_reason', '')[:100] for a in top_articles[:5]
        ],
        "generated_at": datetime.now().isoformat(),
        "publish_on": "Wednesday",
        "type": "newsletter",
        "copyright_safe": True
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
        # Generate today's main post (template based on day of week)
        top_article = articles[0]
        post = generate_linkedin_post(top_article, clients)
        save_content(post, "data/linkedin_post.json")
        
        # Generate posts for all domains (for content library)
        print("\n  Generating domain-specific posts...")
        all_domain_posts = generate_all_domain_posts(articles[:20], clients)
        save_content(all_domain_posts, "data/domain_posts.json")
        
        # Generate carousel from top article
        carousel = generate_carousel(top_article, clients)
        save_content(carousel, "data/carousel.json")
        
        # Generate newsletter (only on Tuesdays)
        newsletter = generate_newsletter(articles[:5], clients)
        if newsletter:
            save_content(newsletter, "data/newsletter.json")
