# Configuration for GRC Intelligence Copilot

# RSS Feeds for GRC News
RSS_FEEDS = [
    # Privacy & Data Protection
    "https://iapp.org/rss/",
    "https://www.privacyaffairs.com/feed/",
    
    # Security
    "https://www.csoonline.com/index.rss",
    "https://www.darkreading.com/rss.xml",
    "https://threatpost.com/feed/",
    "https://krebsonsecurity.com/feed/",
    "https://www.schneier.com/feed/atom/",
    
    # Compliance & Regulation
    "https://www.regulationasia.com/feed/",
    "https://www.jdsupra.com/legalnews/cybersecurity/?format=rss",
    
    # AI & Technology
    "https://techcrunch.com/category/artificial-intelligence/feed/",
    "https://www.wired.com/feed/tag/ai/latest/rss",
    
    # India Specific
    "https://economictimes.indiatimes.com/tech/technology/rssfeeds/13357270.cms",
    "https://www.moneycontrol.com/rss/technology.xml",
]

# GRC Domains for scoring
DOMAINS = [
    "Privacy & Data Protection",
    "Information Security", 
    "AI Governance & Ethics",
    "Regulatory Compliance",
    "Risk Management",
    "GRC Career & Skills"
]

# Your voice profile for content generation
VOICE_PROFILE = """
You are writing as Shree Sathya, author of "The Unwritten Rules of GRC" newsletter.

Voice characteristics:
- Professional but accessible, never jargon-heavy
- Educational and practical - focus on real-world application
- First person occasionally ("I've seen...", "In my experience...")
- Direct statements, no fluff or filler
- Uses analogies to explain complex concepts
- Provides actionable insights, not just theory
- Targets GRC professionals, especially those transitioning from non-technical backgrounds
- Bridges the gap between technical concepts and GRC practice

Tone: Mix of professional, conversational, and thought-leadership
- Professional: Credible, well-researched points
- Conversational: Engaging, relatable examples
- Thought-leadership: Strong opinions backed by reasoning

DO NOT use excessive emojis. Maximum 2-3 per post if needed.
DO NOT use generic motivational language.
DO write like a practitioner sharing real insights.
"""

# Newsletter series configuration
NEWSLETTER_SERIES = {
    "name": "From Non-Tech to Tech-Aware GRC",
    "current_episode": 6,  # Will increment automatically
    "topics_queue": [
        "Understanding API Security in GRC Context",
        "Network Security Fundamentals for Compliance",
        "Identity and Access Management Essentials",
        "Encryption: What GRC Professionals Must Know",
        "Third-Party Risk in Technical Terms",
        "Incident Response from a GRC Perspective",
        "Security Monitoring and Logging Basics",
        "DevSecOps and Compliance Integration",
        "Container Security for Non-Technical GRC",
        "Zero Trust Architecture Explained Simply"
    ]
}

# Prompts
SCORING_PROMPT = """
You are a GRC (Governance, Risk, Compliance) relevance scorer.

Score this article from 1-10 based on relevance to GRC professionals:
- 9-10: Critical GRC news (new regulations, major breaches, compliance deadlines)
- 7-8: Important GRC topics (framework updates, industry guidance, trends)
- 5-6: Moderately relevant (general security/privacy news with GRC implications)
- 3-4: Tangentially related (tech news that may affect GRC)
- 1-2: Not relevant to GRC

Article Title: {title}
Article Summary: {summary}

Respond in JSON format:
{{
    "score": <number>,
    "domains": ["<relevant domain 1>", "<relevant domain 2>"],
    "reason": "<one sentence explanation>"
}}

Domains to choose from: {domains}
"""

LINKEDIN_POST_PROMPT = """
{voice_profile}

Based on this top GRC news article, write a LinkedIn post:

Article Title: {title}
Article Summary: {summary}
Article URL: {url}

Requirements:
1. 200-400 words
2. Hook in first line (curiosity or bold statement)
3. 3-4 key insights or takeaways
4. End with a question to drive engagement
5. Include 4-5 relevant hashtags at the end
6. Mix of professional insight + practical advice + thought leadership

Write the complete LinkedIn post now:
"""

CAROUSEL_PROMPT = """
{voice_profile}

Based on this GRC news, create LinkedIn carousel content (slide-by-slide text):

Article Title: {title}
Article Summary: {summary}

Create 7 slides:
- Slide 1: Bold title/hook (max 8 words)
- Slides 2-6: One key point each with heading + 2-3 lines explanation
- Slide 7: Call-to-action (follow, share, comment)

Format your response as:
SLIDE 1:
[Title text]

SLIDE 2:
Heading: [heading]
Body: [2-3 lines]

... continue for all 7 slides
"""

NEWSLETTER_PROMPT = """
{voice_profile}

Write the next edition of "The Unwritten Rules of GRC" newsletter.

Series: {series_name}
Episode: {episode_number}
Topic: {topic}

This week's top GRC news for context:
{news_context}

Requirements:
1. 1500-2500 words
2. Educational, teaching-focused content
3. Match the style of previous newsletters (practical, non-jargon, real-world focused)
4. Structure:
   - Opening hook (why this matters now)
   - Main teaching content (3-4 sections with clear headers)
   - Real-world example or analogy
   - Common misconceptions to avoid
   - Practical next steps for readers
   - Teaser for next week
5. Include 2-3 free resource links where relevant

Write the complete newsletter article now:
"""

# Dashboard password
DASHBOARD_PASSWORD = "GRC2026!Shree"
