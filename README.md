# GRC Copilot

An AI-powered content assistant for GRC (Governance, Risk, and Compliance) professionals.

## Features

- **AI-Powered Analysis** - Leverages Gemini and Groq for intelligent content generation
- **Automated Workflows** - Scheduled pipelines for consistent output
- **Interactive Dashboard** - Clean, modern interface for content management
- **Multi-Format Support** - Generate posts, carousels, and long-form content

## Tech Stack

- Python 3.11
- GitHub Actions (CI/CD)
- GitHub Pages (Hosting)
- Gemini API / Groq API

## Setup

### Prerequisites

- GitHub account
- Groq API key ([console.groq.com](https://console.groq.com))
- Gemini API key ([aistudio.google.com](https://aistudio.google.com))

### Installation

1. Fork or clone this repository

2. Add repository secrets (Settings → Secrets → Actions):
   ```
   GROQ_API_KEY=your_groq_key
   GEMINI_API_KEY=your_gemini_key
   ```

3. Enable GitHub Pages:
   - Go to Settings → Pages
   - Source: Deploy from branch
   - Branch: `main`, Folder: `/docs`

4. Access your dashboard at `https://[username].github.io/grc-copilot/`

## Project Structure

```
grc-copilot/
├── .github/workflows/    # Automation pipelines
├── scripts/              # Core Python modules
├── data/                 # Generated outputs
└── docs/                 # Dashboard (GitHub Pages)
```

## Usage

The pipeline runs automatically on schedule. You can also trigger it manually:

1. Go to Actions tab
2. Select the workflow
3. Click "Run workflow"

## License

Private use only.
