// Configuration
const PASSWORD = "GRC2026!Shree";
const DATA_PATH = "data/";

// Check password
function checkPassword() {
    const input = document.getElementById('password-input').value;
    const errorEl = document.getElementById('password-error');
    
    if (input === PASSWORD) {
        document.getElementById('password-screen').classList.add('hidden');
        document.getElementById('dashboard').classList.remove('hidden');
        loadAllContent();
    } else {
        errorEl.textContent = "Incorrect password. Please try again.";
        document.getElementById('password-input').value = '';
    }
}

// Handle Enter key
function handleKeyPress(event) {
    if (event.key === 'Enter') {
        checkPassword();
    }
}

// Load all content
async function loadAllContent() {
    await Promise.all([
        loadLinkedInPost(),
        loadCarousel(),
        loadNewsletter(),
        loadTopNews()
    ]);
}

// Load LinkedIn Post
async function loadLinkedInPost() {
    try {
        const response = await fetch(DATA_PATH + 'linkedin_post.json');
        const data = await response.json();
        
        document.getElementById('linkedin-post').textContent = data.content;
        document.getElementById('linkedin-meta').innerHTML = `
            Based on: <strong>${data.based_on.title}</strong> (${data.based_on.source}, Score: ${data.based_on.score})
        `;
        
        updateLastUpdated(data.generated_at);
    } catch (error) {
        document.getElementById('linkedin-post').textContent = 'Content not yet generated. Pipeline will run at 5 AM or 6 PM IST.';
    }
}

// Load Carousel
async function loadCarousel() {
    try {
        const response = await fetch(DATA_PATH + 'carousel.json');
        const data = await response.json();
        
        document.getElementById('carousel-content').textContent = data.raw_content;
    } catch (error) {
        document.getElementById('carousel-content').textContent = 'Carousel content not yet generated.';
    }
}

// Load Newsletter
async function loadNewsletter() {
    try {
        const response = await fetch(DATA_PATH + 'newsletter.json');
        const data = await response.json();
        
        document.getElementById('newsletter-meta').innerHTML = `
            <strong>Series:</strong> ${data.series} | 
            <strong>Episode:</strong> ${data.episode} | 
            <strong>Topic:</strong> ${data.title} |
            <strong>Publish on:</strong> ${data.publish_on}
        `;
        document.getElementById('newsletter-content').textContent = data.content;
    } catch (error) {
        document.getElementById('newsletter-meta').innerHTML = '<em>Newsletter generates every Tuesday for Wednesday publishing</em>';
        document.getElementById('newsletter-content').textContent = 'No newsletter available yet. Will be generated on Tuesday.';
    }
}

// Load Top News
async function loadTopNews() {
    try {
        const response = await fetch(DATA_PATH + 'articles.json');
        const articles = await response.json();
        
        const topArticles = articles.slice(0, 5);
        
        const newsHtml = topArticles.map(article => `
            <div class="news-item">
                <span class="news-score">${article.score}</span>
                <div class="news-content">
                    <div class="news-title">${article.title}</div>
                    <div class="news-source">${article.source} | ${article.domains ? article.domains.join(', ') : 'GRC'}</div>
                </div>
            </div>
        `).join('');
        
        document.getElementById('news-list').innerHTML = newsHtml;
    } catch (error) {
        document.getElementById('news-list').innerHTML = '<p>No news articles available yet.</p>';
    }
}

// Update last updated time
function updateLastUpdated(timestamp) {
    if (timestamp) {
        const date = new Date(timestamp);
        const options = { 
            weekday: 'short', 
            month: 'short', 
            day: 'numeric',
            hour: '2-digit', 
            minute: '2-digit',
            timeZoneName: 'short'
        };
        document.getElementById('last-updated').textContent = `Last updated: ${date.toLocaleDateString('en-IN', options)}`;
    }
}

// Copy content to clipboard
async function copyContent(elementId) {
    const element = document.getElementById(elementId);
    const text = element.textContent;
    
    try {
        await navigator.clipboard.writeText(text);
        
        // Find the copy button for this section
        const section = element.closest('.content-section');
        const btn = section.querySelector('.copy-btn');
        
        const originalText = btn.textContent;
        btn.textContent = 'Copied!';
        btn.classList.add('copied');
        
        setTimeout(() => {
            btn.textContent = originalText;
            btn.classList.remove('copied');
        }, 2000);
    } catch (error) {
        alert('Failed to copy. Please select and copy manually.');
    }
}

// Check for stored session
document.addEventListener('DOMContentLoaded', () => {
    // Focus password input
    document.getElementById('password-input').focus();
});
