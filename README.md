# GRC Intelligence & Content Copilot

A fully automated system that transforms you into a top 1% GRC educator by consuming insights from 5 professional worlds and generating original, copyright-safe content.

## The Vision

**Goal:** Become recognized as a thought leader who connects dots across GRC, Security, Privacy, DevSecOps, and AI/Product - the rare professional who sees the full picture.

**Problem Solved:** Manual news consumption is unsustainable. Reading 100+ sources daily is impossible. Most professionals stay siloed in their domain.

**Solution:** An AI copilot that reads everything, scores what matters, and generates original content that positions you as the bridge between technical and business worlds.

## System Architecture

```
                                    GRC COPILOT ARCHITECTURE
    
    ┌─────────────────────────────────────────────────────────────────────────┐
    │                           100+ RSS SOURCES                               │
    │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐│
    │  │   GRC   │ │ Privacy │ │Security │ │DevSecOps│ │   AI    │ │ Product ││
    │  │  6 feeds│ │ 9 feeds │ │32 feeds │ │11 feeds │ │17 feeds │ │16 feeds ││
    │  └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘│
    └───────┼──────────┼──────────┼──────────┼──────────┼──────────┼─────────┘
            └──────────┴──────────┴────┬─────┴──────────┴──────────┘
                                       ▼
    ┌─────────────────────────────────────────────────────────────────────────┐
    │                         FETCH & PARSE ENGINE                             │
    │  • Parallel RSS fetching with timeout handling                          │
    │  • Deduplication by URL and title similarity                            │
    │  • Extract: title, summary, link, published date, source                │
    └─────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
    ┌─────────────────────────────────────────────────────────────────────────┐
    │                      4-DIMENSION AI SCORING                              │
    │                         (Groq LLaMA 3.1)                                 │
    │  ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐         │
    │  │ Business Impact  │ │  Learning Value  │ │ Content Potential│         │
    │  │     (1-10)       │ │     (1-10)       │ │     (1-10)       │         │
    │  └──────────────────┘ └──────────────────┘ └──────────────────┘         │
    │  ┌──────────────────┐                                                    │
    │  │Compliance Relevance│  Total Score: 0-40 │ Threshold: 24+            │
    │  │     (1-10)       │                                                    │
    │  └──────────────────┘                                                    │
    │  + Domain Classification + "Why It Matters" + Content Angle             │
    └─────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
    ┌─────────────────────────────────────────────────────────────────────────┐
    │                   COPYRIGHT-SAFE CONTENT GENERATION                      │
    │                      (Gemini + Groq Fallback)                            │
    │                                                                          │
    │  INPUT: Topic concept, not article details                              │
    │  OUTPUT: Original perspective, not summary                              │
    │                                                                          │
    │  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐            │
    │  │  LinkedIn Post  │ │    Carousel     │ │   Newsletter    │            │
    │  │  150-250 words  │ │    7 slides     │ │  1500-2000 words│            │
    │  │  Original take  │ │  Teach concept  │ │  Tuesday gen    │            │
    │  │  YOUR voice     │ │  No news refs   │ │  Official refs  │            │
    │  └─────────────────┘ └─────────────────┘ └─────────────────┘            │
    │                                                                          │
    │  Voice Profile: Professional-conversational, analogies,                 │
    │                 first person, banned AI phrases, 70% educational        │
    └─────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
    ┌─────────────────────────────────────────────────────────────────────────┐
    │                        DATA PERSISTENCE                                  │
    │  ┌───────────────┐ ┌───────────────┐ ┌───────────────┐                  │
    │  │  news.json    │ │ content.json  │ │newsletter.json│                  │
    │  │ Scored items  │ │ Posts/Carousel│ │ Weekly edition│                  │
    │  └───────────────┘ └───────────────┘ └───────────────┘                  │
    └─────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
    ┌─────────────────────────────────────────────────────────────────────────┐
    │                      INTERACTIVE DASHBOARD                               │
    │                        (GitHub Pages)                                    │
    │                                                                          │
    │  ┌─────────────────────────────────────────────────────────────────┐    │
    │  │  Navigation: Dashboard │ News │ Bookmarks │ Content │ Newsletter│    │
    │  ├─────────────────────────────────────────────────────────────────┤    │
    │  │  5 Stat Cards: Total │ High-Value │ Posts │ Carousels │ Sources │    │
    │  ├─────────────────────────────────────────────────────────────────┤    │
    │  │  Domain Filters: [GRC] [Privacy] [Security] [DevSecOps] [AI]    │    │
    │  ├─────────────────────────────────────────────────────────────────┤    │
    │  │  3-Column Layout: News Feed │ Content Preview │ Details         │    │
    │  ├─────────────────────────────────────────────────────────────────┤    │
    │  │  Features: Dark Mode (D) │ Search (/) │ Bookmarks │ PDF Export  │    │
    │  │            Copy Post (C) │ Domain Pills │ Toast Notifications   │    │
    │  └─────────────────────────────────────────────────────────────────┘    │
    │                                                                          │
    │  Password Protected: Login required for access                          │
    └─────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
    ┌─────────────────────────────────────────────────────────────────────────┐
    │                        AUTOMATION ENGINE                                 │
    │                        (GitHub Actions)                                  │
    │                                                                          │
    │  Schedule:                                                               │
    │  • 5:00 AM IST  - Morning intelligence run                              │
    │  • 6:00 PM IST  - Evening intelligence run                              │
    │  • Tuesdays     - Newsletter generation (for Wednesday publish)         │
    │                                                                          │
    │  Pipeline:                                                               │
    │  1. git pull --rebase (sync conflicts)                                  │
    │  2. Fetch RSS feeds                                                      │
    │  3. Score articles (Groq)                                               │
    │  4. Generate content (Gemini/Groq)                                      │
    │  5. Update JSON files                                                    │
    │  6. git commit & push                                                    │
    │                                                                          │
    │  Zero manual intervention required                                       │
    └─────────────────────────────────────────────────────────────────────────┘
```

## Feed Distribution

| Domain | Feed Count | Key Sources |
|--------|------------|-------------|
| GRC | 6 | All About GRC, Compliance Week, Bank Info Security, Gov Info Security |
| Privacy | 9 | Future of Privacy Forum, NOYB, CNIL, EFF, EPIC, Privacy International |
| Security | 32 | Krebs, Schneier, Dark Reading, Hacker News, CrowdStrike, Unit42, Mandiant |
| DevSecOps | 11 | OWASP, Snyk, AWS Security, Docker, Kubernetes, CNCF, GitHub Security |
| AI | 17 | DeepMind, Hugging Face, The Gradient, AI Snake Oil, Fast.ai, NVIDIA |
| Product | 16 | Lenny's Newsletter, SVPG, Pragmatic Engineer, Stratechery, Intercom |

**Total: 91 verified working feeds** (tested June 2026)

## Content Philosophy

### Copyright-Safe by Design

The system does NOT:
- Summarize articles
- Quote specific facts or statistics from sources
- Reference specific company incidents
- Copy any source material

The system DOES:
- Use news as inspiration for original thought
- Teach underlying concepts that are timeless
- Share YOUR perspective and frameworks
- Reference only official docs (NIST, ISO, OWASP)

### Voice Profile

- **70% Educational** - Teach something useful
- **20% Conversational** - Relatable examples, analogies
- **10% Thought Leadership** - Strong opinions backed by reasoning

Banned phrases: "In today's fast-paced world", "Let's dive in", "Game-changer", "Leverage", "Seamless", "Robust", "Delve", "Thoughts?"

## Scoring System

Each article is evaluated on 4 dimensions (1-10 each):

| Dimension | What It Measures | High Score Example |
|-----------|------------------|-------------------|
| **Business Impact** | Organizational/industry effect | Major breach, new regulation |
| **Learning Value** | Foundational, recurring concept | Core GRC principle |
| **Content Potential** | Can become engaging content | Perfect for teaching |
| **Compliance Relevance** | Regulatory/framework impact | Direct regulatory action |

**Threshold: 24+ out of 40** to generate content

## Dashboard Features

| Feature | Shortcut | Description |
|---------|----------|-------------|
| View Switch | 1-5 | Dashboard, News, Bookmarks, Content, Newsletter |
| Dark Mode | D | Toggle dark/light theme (persists) |
| Search | / | Filter news items |
| Copy Post | C | Copy LinkedIn post to clipboard |
| Bookmark | Click | Save items (persists in localStorage) |
| PDF Export | Button | Download content as PDF |

## Newsletter Series

**"From Non-Tech to Tech-Aware GRC"**

Episode queue:
1. API Security Basics
2. Network Security Fundamentals
3. Identity and Access Management
4. Encryption Essentials
5. Third-Party Risk
6. Incident Response
7. Security Monitoring
8. DevSecOps Integration
9. Container Security
10. Zero Trust Architecture

Generated Tuesdays, published Wednesdays.

## Tech Stack

| Layer | Technology |
|-------|------------|
| Automation | GitHub Actions (cron) |
| Hosting | GitHub Pages |
| Scoring AI | Groq (LLaMA 3.1 8B Instant) |
| Content AI | Google Gemini (primary), Groq (fallback) |
| Frontend | Vanilla HTML/CSS/JS, Chart.js |
| Data | JSON files in repo |

**Cost: $0** (all free tiers)

## File Structure

```
grc-copilot/
├── .github/workflows/
│   └── pipeline.yml          # Automation schedule & steps
├── scripts/
│   ├── config.py             # 91 RSS feeds, prompts, voice profile
│   ├── fetch_news.py         # RSS fetching & parsing
│   ├── score_articles.py     # 4-dimension AI scoring
│   ├── generate_content.py   # Copyright-safe content generation
│   └── generate_newsletter.py # Weekly newsletter builder
├── data/
│   ├── news.json             # Scored news items
│   ├── content.json          # Generated posts & carousels
│   └── newsletter.json       # Weekly newsletter editions
└── docs/
    └── index.html            # Interactive dashboard
```

## What This Enables

1. **Daily consumption of 100+ sources** without reading them
2. **Original content ready to publish** in your voice
3. **Cross-domain insights** (GRC + Security + AI + Product)
4. **Zero daily effort** after initial setup
5. **Consistent posting schedule** for audience building
6. **Educational authority** through teaching, not news sharing

---

*Built for the GRC professional who wants to lead, not just follow.*
