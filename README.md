# GRC Content Copilot

Automated GRC Intelligence & Content Generation system.

## Features

- **Daily News Fetching**: Aggregates GRC news from 15+ trusted sources
- **AI Scoring**: Scores articles 1-10 for GRC relevance using Groq
- **Content Generation**: Creates LinkedIn posts, carousels, and newsletters using Gemini
- **Automated Schedule**: Runs at 5 AM and 6 PM IST daily
- **Private Dashboard**: Password-protected content dashboard on GitHub Pages

## Setup

1. Add repository secrets:
   - `GROQ_API_KEY`: Your Groq API key
   - `GEMINI_API_KEY`: Your Google Gemini API key

2. Enable GitHub Pages:
   - Go to Settings → Pages
   - Source: Deploy from branch
   - Branch: `main`, Folder: `/docs`

3. Access your dashboard:
   - URL: `https://YOUR-USERNAME.github.io/grc-copilot/`
   - Password: Check `scripts/config.py`

## Directory Structure

```
grc-copilot/
├── .github/workflows/pipeline.yml  # Automated schedule
├── scripts/                         # Python scripts
│   ├── main.py                     # Main pipeline
│   ├── fetch_news.py               # News fetching
│   ├── score_articles.py           # AI scoring
│   ├── generate_content.py         # Content generation
│   └── config.py                   # Configuration
├── data/                           # Generated data
└── docs/                           # GitHub Pages dashboard
```

## Manual Trigger

You can manually trigger the pipeline:
1. Go to Actions tab
2. Select "GRC Intelligence Pipeline"
3. Click "Run workflow"

---

Built for [The Unwritten Rules of GRC](https://www.linkedin.com/newsletters/the-unwritten-rules-of-grc-7419717856528850944) by Shree Sathya
