"""
Article Scorer
"""

import os
import json
from groq import Groq
from config import SCORING_PROMPT, DOMAINS

def score_articles(articles):
    """Score articles using 4-dimension scoring"""
    
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    scored_articles = []
    
    for article in articles:
        try:
            prompt = SCORING_PROMPT.format(
                title=article['title'],
                summary=article['summary']
            )
            
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a GRC intelligence analyst. Score articles accurately. Always respond in valid JSON only."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=500
            )
            
            result_text = response.choices[0].message.content.strip()
            
            # Parse JSON response
            if "```json" in result_text:
                result_text = result_text.split("```json")[1].split("```")[0]
            elif "```" in result_text:
                result_text = result_text.split("```")[1].split("```")[0]
            
            result = json.loads(result_text)
            
            # Extract 4-dimension scores
            scores = result.get('scores', {})
            article['score_business'] = scores.get('business_impact', 5)
            article['score_learning'] = scores.get('learning_value', 5)
            article['score_content'] = scores.get('content_potential', 5)
            article['score_compliance'] = scores.get('compliance_relevance', 5)
            
            # Total score (sum of 4, max 40) - convert to 1-10 scale for display
            total = result.get('total_score', 20)
            article['score'] = round(total / 4)  # Average for display
            article['total_score'] = total
            
            article['domains'] = result.get('domains', ['GRC'])
            article['score_reason'] = result.get('why_it_matters', '')
            article['content_angle'] = result.get('content_angle', '')
            
            scored_articles.append(article)
            print(f"Scored: {article['title'][:50]}... -> {article['score']} (total: {total}/40)")
            
        except Exception as e:
            print(f"Error scoring article: {e}")
            # Default scores
            article['score'] = 5
            article['total_score'] = 20
            article['score_business'] = 5
            article['score_learning'] = 5
            article['score_content'] = 5
            article['score_compliance'] = 5
            article['domains'] = ['GRC']
            article['score_reason'] = 'Scoring failed - manual review needed'
            article['content_angle'] = ''
            scored_articles.append(article)
    
    # Sort by total score descending
    scored_articles.sort(key=lambda x: x.get('total_score', 0), reverse=True)
    
    return scored_articles


def get_top_articles(scored_articles, count=5, min_score=24):
    """Get top articles by total score (threshold from blueprint: 24/40)"""
    # Filter by minimum threshold
    high_value = [a for a in scored_articles if a.get('total_score', 0) >= min_score]
    
    # If not enough high-value articles, include top ones anyway
    if len(high_value) < count:
        return scored_articles[:count]
    
    return high_value[:count]


def save_scored_articles(articles, filepath="data/articles.json"):
    """Save scored articles to JSON file"""
    with open(filepath, 'w') as f:
        json.dump(articles, f, indent=2)
    print(f"Saved {len(articles)} scored articles to {filepath}")


if __name__ == "__main__":
    with open("data/raw_articles.json", "r") as f:
        articles = json.load(f)
    
    scored = score_articles(articles)
    save_scored_articles(scored)
