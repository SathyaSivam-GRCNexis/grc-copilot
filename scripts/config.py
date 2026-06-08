# Configuration

# RSS Feeds organized by domain - from Blueprint Appendix A
RSS_FEEDS = [
    # ===================
    # SECURITY
    # ===================
    "https://feeds.feedburner.com/TheHackersNews",  # The Hacker News
    "https://www.bleepingcomputer.com/feed/",  # BleepingComputer
    "https://krebsonsecurity.com/feed/",  # Krebs on Security
    "https://www.schneier.com/feed/atom/",  # Schneier on Security
    "https://www.darkreading.com/rss.xml",  # Dark Reading
    "https://www.csoonline.com/index.rss",  # CSO Online
    "https://threatpost.com/feed/",  # Threatpost
    "https://www.securityweek.com/feed",  # Security Week
    "https://nakedsecurity.sophos.com/feed/",  # Sophos Naked Security
    "https://blog.talosintelligence.com/feeds/posts/default",  # Cisco Talos
    
    # ===================
    # GRC / COMPLIANCE
    # ===================
    "https://www.isaca.org/resources/news-and-trends/isaca-now-blog/rss",  # ISACA
    "https://www.nist.gov/news-events/news/rss.xml",  # NIST News
    "https://www.helpnetsecurity.com/feed/",  # Help Net Security (GRC focus)
    "https://www.complianceweek.com/rss/all.rss",  # Compliance Week
    
    # ===================
    # PRIVACY
    # ===================
    "https://iapp.org/rss/",  # IAPP - International Association of Privacy Professionals
    "https://www.privacyaffairs.com/feed/",  # Privacy Affairs
    "https://gdpr.eu/feed/",  # GDPR EU
    "https://fpf.org/feed/",  # Future of Privacy Forum
    
    # ===================
    # AI & AI GOVERNANCE
    # ===================
    "https://openai.com/blog/rss/",  # OpenAI Blog
    "https://www.anthropic.com/index.xml",  # Anthropic
    "https://blog.google/technology/ai/rss/",  # Google AI Blog
    "https://techcrunch.com/category/artificial-intelligence/feed/",  # TechCrunch AI
    "https://venturebeat.com/category/ai/feed/",  # VentureBeat AI
    "https://www.technologyreview.com/feed/",  # MIT Tech Review
    
    # ===================
    # DEVSECOPS
    # ===================
    "https://snyk.io/blog/feed/",  # Snyk Blog
    "https://github.blog/category/security/feed/",  # GitHub Security
    "https://owasp.org/feed.xml",  # OWASP
    "https://www.aquasec.com/feed/",  # Aqua Security
    "https://sysdig.com/blog/feed/",  # Sysdig
    
    # ===================
    # PRODUCT MANAGEMENT
    # ===================
    "https://www.lennysnewsletter.com/feed",  # Lenny's Newsletter
    "https://www.mindtheproduct.com/feed/",  # Mind the Product
    "https://www.svpg.com/articles/feed/",  # Silicon Valley Product Group
    
    # ===================
    # REGULATORY (GLOBAL)
    # ===================
    "https://www.ftc.gov/feeds/press-release-consumer-protection.xml",  # FTC Consumer Protection
    "https://www.enisa.europa.eu/rss.xml",  # ENISA (EU Cybersecurity Agency)
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
Writing style characteristics:
- Professional but conversational - like explaining to a smart colleague
- Use first person occasionally ("I've noticed...", "In my experience...")
- Short paragraphs (2-3 sentences max)
- One clear takeaway per piece
- End with a specific, genuine question (not "Thoughts?")
- Use analogies to explain complex concepts
- Avoid jargon - if you must use a technical term, explain it

BANNED PHRASES (never use these):
- "In today's fast-paced world"
- "In the ever-evolving landscape"
- "Let's dive in"
- "Game-changer"
- "Revolutionary"
- "Unlock"
- "Leverage"
- "Seamless"
- "Robust"
- "Delve"
- "It's not just X, it's Y"
- "Thoughts? 👇"
- "As an AI"
- "As a language model"

TONE:
- 70% educational (teach something useful)
- 20% conversational (relatable examples)
- 10% thought-leadership (strong opinions backed by reasoning)
"""

NEWSLETTER_SERIES = {
    "name": "From Non-Tech to Tech-Aware GRC",
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

# 4-Dimension Scoring (matching the blueprint)
SCORING_PROMPT = """
You are scoring a news article for a GRC (Governance, Risk, Compliance) professional.

Score this article on FOUR dimensions (each 1-10):

1. **Business Impact**: Does it affect organizations, governance, or whole industries?
   - 9-10: Major breach, new regulation, industry-wide change
   - 5-6: Affects specific sectors or companies
   - 1-3: Limited business relevance

2. **Learning Value**: Is the underlying concept foundational and recurring?
   - 9-10: Core GRC/security concept everyone should understand
   - 5-6: Useful knowledge for professionals
   - 1-3: One-off news with limited learning

3. **Content Potential**: Can this become a post, newsletter, or carousel?
   - 9-10: Perfect for explaining a concept or taking a stance
   - 5-6: Could be part of a roundup or brief mention
   - 1-3: Hard to create engaging content from this

4. **Compliance Relevance**: Is there regulatory or framework impact?
   - 9-10: Direct regulatory action, framework update, compliance deadline
   - 5-6: Indirect compliance implications
   - 1-3: No compliance angle

Article Title: {title}
Article Summary: {summary}

Respond in this exact JSON format:
{{
    "scores": {{
        "business_impact": <1-10>,
        "learning_value": <1-10>,
        "content_potential": <1-10>,
        "compliance_relevance": <1-10>
    }},
    "total_score": <sum of 4 scores, max 40>,
    "domains": ["<primary domain>", "<secondary if relevant>"],
    "why_it_matters": "<One sentence: why a GRC professional should care about this>",
    "content_angle": "<Brief suggestion for how to create content from this>"
}}

Choose domains from: GRC, Privacy, Security, DevSecOps, AI, Product
"""

# Humanized LinkedIn Post Prompt (multi-pass approach from blueprint)
LINKEDIN_POST_PROMPT = """
{voice_profile}

Write a LinkedIn post about this news that sounds genuinely human - NOT like AI wrote it.

SOURCE:
Title: {title}
Summary: {summary}
Why it matters: {why_it_matters}
Link: {url}

STRUCTURE YOUR POST:
1. **Hook** (first line): Make them stop scrolling. Be specific, not generic.
   - Good: "A hospital just paid $1.2M in ransomware. The attack started with a PDF."
   - Bad: "Cybersecurity is more important than ever."

2. **Context** (2-3 sentences): What happened and why it matters. Use simple words.

3. **The insight** (your take): What most people miss. Be specific.

4. **Practical takeaway**: One thing the reader can do or think about.

5. **Genuine question**: Ask something you're actually curious about (not "Thoughts?")

REQUIREMENTS:
- 150-250 words total
- Short paragraphs (1-3 sentences each)
- Maximum 2 emojis (or none - real professionals don't overuse them)
- 3-4 hashtags at the end
- NO clichés, NO hype words, NO "In today's world..."
- Write like you're texting a smart friend, not writing a press release

Write the post now:
"""

# Carousel content for Canva
CAROUSEL_PROMPT = """
{voice_profile}

Create 7 carousel slides for this topic. Each slide must be SIMPLE and SCANNABLE.

Topic: {title}
Context: {summary}

FORMAT EACH SLIDE:

SLIDE 1: (Title slide - hook them)
- Bold statement or question (max 8 words)
- Example: "SOC 2 Audits: What They Don't Tell You"

SLIDE 2-5: (One key point per slide)
Heading: [3-5 words]
Body: [1-2 short sentences - explain like they're 12]

SLIDE 6: (The "So What")
Heading: What This Means For You
Body: [Practical action or mindset shift]

SLIDE 7: (Call to action)
- Follow for more GRC insights
- Or a specific next step

RULES:
- Each slide stands alone - someone should get value from any single slide
- No jargon without explanation
- Use numbers, comparisons, or analogies
- No walls of text - scannable in 3 seconds

Create all 7 slides now:
"""

# Newsletter prompt
NEWSLETTER_PROMPT = """
{voice_profile}

Write newsletter episode {episode_number} of "{series_name}"

TOPIC: {topic}

THIS WEEK'S CONTEXT (top news to reference):
{news_context}

STRUCTURE (1500-2000 words total):

1. **Opening hook** (2-3 paragraphs)
   - Start with a story, question, or surprising fact
   - Connect it to why this topic matters RIGHT NOW
   - Make non-technical readers feel this is FOR them

2. **The Basics** (3-4 paragraphs)
   - Define the concept in plain English
   - Use an analogy from everyday life
   - "Think of it like..."

3. **How It Works** (3-4 paragraphs)
   - The mechanics, simplified
   - Real-world example
   - What happens when it goes wrong

4. **Common Mistakes** (3-4 paragraphs)
   - What organizations get wrong
   - Why these mistakes happen
   - How to avoid them

5. **Getting Started** (3-4 paragraphs)
   - Practical first steps
   - Free resources (include 2-3 real links)
   - What to prioritize

6. **Closing** (2 paragraphs)
   - Key takeaway
   - Tease next episode

STYLE:
- Write like you're teaching a friend over coffee
- Use "you" and "we" liberally
- Short paragraphs (max 4 sentences)
- Headers for each section
- Bold key terms when first introduced

Write the complete newsletter:
"""

DASHBOARD_PASSWORD = "GRC2026!Shree"
