"""
Article Scorer - Uses Groq to score articles for GRC relevance
"""

import os
import json
from groq import Groq
from config import SCORING_PROMPT, DOMAINS

def score_articles(articles):
    """Score articles using Groq API"""
    
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    scored_articles = []
    
    for article in articles:
        try:
            prompt = SCORING_PROMPT.format(
                title=article['title'],
                summary=article['summary'],
                domains=", ".join(DOMAINS)
            )
            
            response = client.chat.completions.create(
                model="llama-3.1-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a GRC relevance scoring assistant. Always respond in valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=200
            )
            
            result_text = response.choices[0].message.content.strip()
            
            # Parse JSON response
            # Handle potential markdown code blocks
            if "```json" in result_text:
                result_text = result_text.split("```json")[1].split("```")[0]
            elif "```" in result_text:
                result_text = result_text.split("```")[1].split("```")[0]
            
            result = json.loads(result_text)
            
            article['score'] = result.get('score', 5)
            article['domains'] = result.get('domains', [])
            article['score_reason'] = result.get('reason', '')
            
            scored_articles.append(article)
            print(f"Scored: {article['title'][:50]}... -> {article['score']}")
            
        except Exception as e:
            print(f"Error scoring article: {e}")
            # Default score for failed articles
            article['score'] = 5
            article['domains'] = []
            article['score_reason'] = 'Scoring failed'
            scored_articles.append(article)
    
    # Sort by score descending
    scored_articles.sort(key=lambda x: x['score'], reverse=True)
    
    return scored_articles


def get_top_articles(scored_articles, count=5):
    """Get top N articles by score"""
    return scored_articles[:count]


def save_scored_articles(articles, filepath="data/articles.json"):
    """Save scored articles to JSON file"""
    with open(filepath, 'w') as f:
        json.dump(articles, f, indent=2)
    print(f"Saved {len(articles)} scored articles to {filepath}")


if __name__ == "__main__":
    # Test with sample data
    with open("data/raw_articles.json", "r") as f:
        articles = json.load(f)
    
    scored = score_articles(articles)
    save_scored_articles(scored)
