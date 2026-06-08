# Configuration - Curated Sources for Top 1% GRC Educator
# Based on 5-world consumption: GRC, Security, Privacy, DevSecOps, AI/Product

# =============================================================================
# RSS FEEDS - Organized by Priority
# =============================================================================

# TOP 20 PRIORITY SOURCES (Read Weekly)
RSS_FEEDS_PRIORITY = [
    # GRC & Compliance (6)
    "https://grcpros.com/feed/",  # GRC Pros
    "https://allaboutgrc.com/feed/",  # All About GRC
    "https://www.sprinto.com/blog/feed/",  # Sprinto - Modern compliance
    "https://drata.com/blog/rss.xml",  # Drata
    "https://scrut.io/blog/feed/",  # Scrut
    
    # Privacy (2)
    "https://iapp.org/rss/",  # IAPP
    "https://fpf.org/feed/",  # Future of Privacy Forum
    
    # Security (4)
    "https://krebsonsecurity.com/feed/",  # Krebs on Security
    "https://www.schneier.com/feed/atom/",  # Schneier on Security
    "https://www.sans.org/newsletters/newsbites/rss/",  # SANS NewsBites
    "https://feeds.feedburner.com/TheHackersNews",  # The Hacker News
    
    # Cloud/DevSecOps (2)
    "https://cloudseclist.com/feed/",  # CloudSecList
    "https://tldrsec.com/feed/",  # TLDRSec
    
    # AI Governance (3)
    "https://hai.stanford.edu/news/rss.xml",  # Stanford HAI
    "https://www.nist.gov/topics/artificial-intelligence/rss.xml",  # NIST AI
    "https://www.aisnakeoil.com/feed",  # AI Snake Oil
    
    # Product (2)
    "https://www.lennysnewsletter.com/feed",  # Lenny's Newsletter
    "https://www.svpg.com/articles/feed/",  # SVPG
]

# SECONDARY SOURCES - All 100 Sources
RSS_FEEDS = [
    # ===================
    # 1. GRC / COMPLIANCE (1-20)
    # ===================
    "https://grcpros.com/feed/",
    "https://allaboutgrc.com/feed/",
    "https://www.sprinto.com/blog/feed/",
    "https://drata.com/blog/rss.xml",
    "https://scrut.io/blog/feed/",
    "https://www.diligent.com/resources/blog/feed/",
    "https://www.metricstream.com/blog/feed/",
    "https://www.auditboard.com/blog/rss/",
    "https://www.onetrust.com/blog/feed/",
    "https://hyperproof.io/blog/feed/",
    "https://secureframe.com/blog/rss.xml",
    "https://www.vanta.com/blog/rss.xml",
    "https://www.isaca.org/resources/news-and-trends/isaca-now-blog/rss",
    "https://iapp.org/rss/",
    "https://www.rmmagazine.com/feed/",
    "https://www.navex.com/blog/feed/",
    "https://www.rsaconference.com/rss.xml",
    "https://www.complianceweek.com/rss/all.rss",
    
    # ===================
    # 2. PRIVACY & DATA PROTECTION (21-40)
    # ===================
    "https://fpf.org/feed/",
    "https://noyb.eu/en/rss.xml",
    "https://www.edpb.europa.eu/rss_en",
    "https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/rss/",
    "https://www.cnil.fr/en/rss.xml",
    "https://www.dataguidance.com/rss.xml",
    "https://www.privacyaffairs.com/feed/",
    "https://privacyinternational.org/rss.xml",
    "https://gdpr.eu/feed/",
    "https://www.cdt.org/feed/",
    
    # ===================
    # 3. CYBERSECURITY (41-60)
    # ===================
    "https://krebsonsecurity.com/feed/",
    "https://www.schneier.com/feed/atom/",
    "https://www.sans.org/newsletters/newsbites/rss/",
    "https://www.sans.org/newsletters/ouch/rss/",
    "https://www.darkreading.com/rss.xml",
    "https://feeds.feedburner.com/TheHackersNews",
    "https://www.bleepingcomputer.com/feed/",
    "https://www.cisa.gov/news.xml",
    "https://www.microsoft.com/security/blog/feed/",
    "https://cloud.google.com/blog/products/identity-security/rss",
    "https://www.mandiant.com/resources/blog/rss.xml",
    "https://www.crowdstrike.com/blog/feed/",
    "https://unit42.paloaltonetworks.com/feed/",
    "https://blog.rapid7.com/rss/",
    "https://www.wiz.io/blog/rss.xml",
    "https://www.tenable.com/blog/feed",
    "https://www.recordedfuture.com/feed/",
    "https://cyberscoop.com/feed/",
    "https://www.securityweek.com/feed",
    "https://risky.biz/feeds/risky-business/",
    
    # ===================
    # 4. CLOUD SECURITY & DEVSECOPS (61-75)
    # ===================
    "https://cloudseclist.com/feed/",
    "https://tldrsec.com/feed/",
    "https://apisecurity.io/feed/",
    "https://owasp.org/feed.xml",
    "https://snyk.io/blog/feed/",
    "https://about.gitlab.com/blog/categories/security/feed.xml",
    "https://www.hashicorp.com/blog/feed.xml",
    "https://www.chainguard.dev/blog/rss.xml",
    "https://www.docker.com/blog/feed/",
    "https://aws.amazon.com/blogs/security/feed/",
    "https://azure.microsoft.com/en-us/blog/topics/security/feed/",
    "https://cloud.google.com/blog/products/identity-security/rss",
    "https://sysdig.com/blog/feed/",
    "https://www.aquasec.com/feed/",
    
    # ===================
    # 5. AI GOVERNANCE & RESPONSIBLE AI (76-90)
    # ===================
    "https://openai.com/blog/rss/",
    "https://www.anthropic.com/index.xml",
    "https://www.deepmind.com/blog/rss.xml",
    "https://hai.stanford.edu/news/rss.xml",
    "https://news.mit.edu/topic/artificial-intelligence2/rss.xml",
    "https://partnershiponai.org/feed/",
    "https://www.nist.gov/topics/artificial-intelligence/rss.xml",
    "https://oecd.ai/en/feed",
    "https://blog.mozilla.org/en/category/ai/feed/",
    "https://huggingface.co/blog/feed.xml",
    "https://thegradient.pub/rss/",
    "https://jack-clark.net/feed/",  # Import AI
    "https://bensbites.beehiiv.com/feed",
    "https://www.aisnakeoil.com/feed",
    
    # ===================
    # 6. PRODUCT MANAGEMENT (91-100)
    # ===================
    "https://www.lennysnewsletter.com/feed",
    "https://www.mindtheproduct.com/feed/",
    "https://productcoalition.com/feed",
    "https://www.svpg.com/articles/feed/",
    "https://www.producttalk.org/feed/",
    "https://www.departmentofproduct.com/feed/",
    "https://review.firstround.com/feed.xml",
    "https://stratechery.com/feed/",
    "https://a16z.com/feed/",
    
    # ===================
    # ADDITIONAL HIGH-VALUE SOURCES
    # ===================
    "https://www.helpnetsecurity.com/feed/",
    "https://techcrunch.com/category/artificial-intelligence/feed/",
    "https://venturebeat.com/category/ai/feed/",
    "https://www.technologyreview.com/feed/",
    "https://github.blog/category/security/feed/",
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
- Explain WHY controls exist, not just WHAT they say
- Connect technical concepts to business impact

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

# 4-Dimension Scoring
SCORING_PROMPT = """
You are scoring a news article for a GRC (Governance, Risk, Compliance) professional who wants to become a top 1% educator.

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

3. **The insight** (your take): What most people miss. Be specific. Connect to WHY controls exist.

4. **Practical takeaway**: One thing the reader can do or think about.

5. **Genuine question**: Ask something you're actually curious about (not "Thoughts?")

REQUIREMENTS:
- 150-250 words total
- Short paragraphs (1-3 sentences each)
- Maximum 2 emojis (or none)
- 3-4 hashtags at the end
- NO clichés, NO hype words
- Write like you're texting a smart friend

Write the post now:
"""

CAROUSEL_PROMPT = """
{voice_profile}

Create 7 carousel slides for this topic. Each slide must be SIMPLE and SCANNABLE.

Topic: {title}
Context: {summary}

FORMAT EACH SLIDE:

SLIDE 1: (Title slide - hook them)
- Bold statement or question (max 8 words)

SLIDE 2-5: (One key point per slide)
Heading: [3-5 words]
Body: [1-2 short sentences - explain like they're 12]

SLIDE 6: (The "So What")
Heading: What This Means For You
Body: [Practical action or mindset shift]

SLIDE 7: (Call to action)
- Follow for more GRC insights

RULES:
- Each slide stands alone
- No jargon without explanation
- Use numbers, comparisons, or analogies
- Scannable in 3 seconds

Create all 7 slides now:
"""

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

2. **The Basics** (3-4 paragraphs)
   - Define the concept in plain English
   - Use an analogy from everyday life

3. **How It Works** (3-4 paragraphs)
   - The mechanics, simplified
   - Real-world example
   - What happens when it goes wrong

4. **Common Mistakes** (3-4 paragraphs)
   - What organizations get wrong
   - How to avoid them

5. **Getting Started** (3-4 paragraphs)
   - Practical first steps
   - Free resources (include 2-3 real links)

6. **Closing** (2 paragraphs)
   - Key takeaway
   - Tease next episode

Write the complete newsletter:
"""

DASHBOARD_PASSWORD = "GRC2026!Shree"
