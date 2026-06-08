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

# GRC Domains for scoring - Updated for better categorization
DOMAINS = [
    "GRC",
    "Privacy",
    "Security", 
    "DevSecOps",
    "AI",
    "Product"
]

# Domain mapping for scoring
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

# Your voice profile for content generation
VOICE_PROFILE = """
You are writing as Shree Sathya, author of "The Unwritten Rules of GRC" newsletter.

Voice characteristics:
- Professional but accessible - AVOID technical jargon
- SIMPLIFY complex topics without losing meaning
- Write for beginners who want to understand GRC
- Use simple analogies and real-world examples
- First person occasionally ("I've seen...", "In my experience...")
- Direct statements, no fluff or filler
- Make it easy to understand in 30 seconds
- Target audience: GRC professionals and learners, especially those from non-technical backgrounds

Tone: Mix of professional, conversational, and thought-leadership
- Professional: Credible, well-researched points
- Conversational: Engaging, relatable examples
- Thought-leadership: Strong opinions backed by reasoning

IMPORTANT RULES:
- DO NOT use excessive jargon - explain everything simply
- DO NOT use more than 2-3 emojis per post
- DO NOT use generic motivational language
- DO write like a teacher explaining to a curious student
- DO make complex topics feel approachable
"""

# Newsletter series configuration
NEWSLETTER_SERIES = {
    "name": "From Non-Tech to Tech-Aware GRC",
    "current_episode": 6,
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

# Prompts - Updated for simpler, clearer content
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
    "domains": ["<primary domain>", "<secondary domain if applicable>"],
    "reason": "<one sentence explanation>"
}}

Choose domains from: GRC, Privacy, Security, DevSecOps, AI, Product
Map these appropriately:
- Privacy/Data Protection topics -> "Privacy"
- Security/Cybersecurity topics -> "Security"
- AI/ML/Governance topics -> "AI"
- Compliance/Risk/Governance topics -> "GRC"
- DevOps/Cloud topics -> "DevSecOps"
- Product/Feature topics -> "Product"
"""

LINKEDIN_POST_PROMPT = """
{voice_profile}

Based on this GRC news article, write a LinkedIn post that ANYONE can understand:

Article Title: {title}
Article Summary: {summary}
Article URL: {url}

Requirements:
1. 200-300 words (keep it digestible)
2. Start with a hook that grabs attention
3. Explain the news in SIMPLE terms - imagine explaining to a smart friend who doesn't work in tech
4. Give 2-3 key takeaways that readers can remember
5. End with a thought-provoking question
6. Include 4-5 relevant hashtags at the end
7. Use maximum 2-3 emojis (professional, not excessive)

AVOID:
- Technical jargon without explanation
- Acronyms without spelling them out first
- Overly complex sentences
- Generic motivational statements

Write the complete LinkedIn post now:
"""

CAROUSEL_PROMPT = """
{voice_profile}

Based on this GRC news, create LinkedIn carousel content that's EASY to understand:

Article Title: {title}
Article Summary: {summary}

Create 7 slides for Canva:
- SLIDE 1: Bold, attention-grabbing title (max 6-8 words)
- SLIDES 2-5: One simple key point each with:
  - Heading: Short phrase (max 5 words)
  - Body: 1-2 simple sentences explaining the point (no jargon)
- SLIDE 6: "What This Means For You" - practical takeaway
- SLIDE 7: Call-to-action (follow for more GRC insights)

RULES:
- Use simple words a beginner would understand
- Each slide should stand alone
- No abbreviations without explanation
- Make it visual and scannable

Format your response as:
SLIDE 1:
[Title text]

SLIDE 2:
Heading: [heading]
Body: [simple explanation]

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
1. 1500-2000 words
2. Write for someone NEW to GRC who wants to learn
3. SIMPLIFY every concept - use analogies and examples
4. Structure:
   - Opening: Why this topic matters (make it relatable)
   - Section 1: The basics explained simply
   - Section 2: How it works in the real world (with examples)
   - Section 3: Common mistakes people make
   - Section 4: Practical steps to get started
   - Closing: Key takeaways and what's next
5. Include 2-3 free resource links
6. Use headers and short paragraphs for easy reading

AVOID:
- Dense paragraphs
- Unexplained technical terms
- Assuming prior knowledge
- Being boring or dry

Write the complete newsletter article now:
"""

# Dashboard password
DASHBOARD_PASSWORD = "GRC2026!Shree"
