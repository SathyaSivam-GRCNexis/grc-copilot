# Configuration

# Data sources
RSS_FEEDS = [
    "https://iapp.org/rss/",
    "https://www.privacyaffairs.com/feed/",
    "https://www.csoonline.com/index.rss",
    "https://www.darkreading.com/rss.xml",
    "https://threatpost.com/feed/",
    "https://krebsonsecurity.com/feed/",
    "https://www.schneier.com/feed/atom/",
    "https://www.regulationasia.com/feed/",
    "https://www.jdsupra.com/legalnews/cybersecurity/?format=rss",
    "https://techcrunch.com/category/artificial-intelligence/feed/",
    "https://www.wired.com/feed/tag/ai/latest/rss",
    "https://economictimes.indiatimes.com/tech/technology/rssfeeds/13357270.cms",
    "https://www.moneycontrol.com/rss/technology.xml",
]

DOMAINS = ["GRC", "Privacy", "Security", "DevSecOps", "AI", "Product"]

DOMAIN_MAPPING = {
    "Privacy & Data Protection": "Privacy",
    "Data Protection": "Privacy",
    "GDPR": "Privacy",
    "DPDP": "Privacy",
    "Information Security": "Security",
    "Cybersecurity": "Security",
    "AI Governance & Ethics": "AI",
    "AI Governance": "AI",
    "Machine Learning": "AI",
    "Regulatory Compliance": "GRC",
    "Risk Management": "GRC",
    "GRC Career & Skills": "GRC",
    "Compliance": "GRC",
    "Governance": "GRC",
    "DevOps": "DevSecOps",
    "Cloud Security": "DevSecOps",
    "Product Management": "Product",
    "Product Security": "Product"
}

VOICE_PROFILE = """
Professional but accessible writing style.
Simplify complex topics without losing meaning.
Use simple analogies and real-world examples.
Direct statements, no fluff or filler.
Target audience: professionals and learners.
"""

NEWSLETTER_SERIES = {
    "name": "GRC Insights",
    "current_episode": 6,
    "topics_queue": [
        "API Security Basics",
        "Network Security Fundamentals",
        "Identity and Access Management",
        "Encryption Essentials",
        "Third-Party Risk",
        "Incident Response",
        "Security Monitoring",
        "DevSecOps Integration",
        "Container Security",
        "Zero Trust Architecture"
    ]
}

SCORING_PROMPT = """
Score this article from 1-10 based on relevance:
- 9-10: Critical news
- 7-8: Important topics
- 5-6: Moderately relevant
- 3-4: Tangentially related
- 1-2: Not relevant

Article Title: {title}
Article Summary: {summary}

Respond in JSON format:
{{
    "score": <number>,
    "domains": ["<primary domain>", "<secondary domain if applicable>"],
    "reason": "<one sentence explanation>"
}}

Choose domains from: GRC, Privacy, Security, DevSecOps, AI, Product
"""

LINKEDIN_POST_PROMPT = """
{voice_profile}

Write a professional post based on this topic:

Title: {title}
Summary: {summary}
Reference: {url}

Requirements:
1. 200-300 words
2. Start with a hook
3. Explain in simple terms
4. Give 2-3 key takeaways
5. End with a question
6. Include 4-5 hashtags
7. Use 2-3 emojis maximum

Write the complete post:
"""

CAROUSEL_PROMPT = """
{voice_profile}

Create carousel content for this topic:

Title: {title}
Summary: {summary}

Create 7 slides:
- SLIDE 1: Bold title (max 6-8 words)
- SLIDES 2-5: One key point each with heading and body
- SLIDE 6: Practical takeaway
- SLIDE 7: Call-to-action

Format:
SLIDE 1:
[Title text]

SLIDE 2:
Heading: [heading]
Body: [explanation]

... continue for all 7 slides
"""

NEWSLETTER_PROMPT = """
{voice_profile}

Write the next edition of the newsletter.

Series: {series_name}
Episode: {episode_number}
Topic: {topic}

Context:
{news_context}

Requirements:
1. 1500-2000 words
2. Write for beginners
3. Use analogies and examples
4. Structure with clear sections
5. Include 2-3 resource links
6. Use headers and short paragraphs

Write the complete article:
"""

DASHBOARD_PASSWORD = "GRC2026!Shree"
