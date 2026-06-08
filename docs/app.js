// Configuration
const PASSWORD = "GRC2026!Shree";
const DATA_PATH = "data/";

// Domain colors and labels
const DOMAINS = {
    "GRC": { color: "grc", label: "GRC" },
    "Privacy": { color: "privacy", label: "Privacy" },
    "Security": { color: "security", label: "Security" },
    "DevSecOps": { color: "devsecops", label: "DevSecOps" },
    "AI": { color: "ai", label: "AI & ML" },
    "Product": { color: "product", label: "Product" },
    "Compliance": { color: "grc", label: "GRC" },
    "Risk": { color: "grc", label: "GRC" },
    "Data Protection": { color: "privacy", label: "Privacy" },
    "Information Security": { color: "security", label: "Security" },
    "AI Governance": { color: "ai", label: "AI & ML" }
};

// State
let allArticles = [];
let currentFilter = "all";

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
        document.getElementById('password-input').focus();
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
    
    setupDomainFilters();
}

// Load LinkedIn Post
async function loadLinkedInPost() {
    try {
        const response = await fetch(DATA_PATH + 'linkedin_post.json');
        const data = await response.json();
        
        document.getElementById('linkedin-post').textContent = data.content;
        
        const metaEl = document.getElementById('linkedin-meta');
        if (data.based_on) {
            metaEl.innerHTML = `
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14">
                    <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/>
                    <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>
                </svg>
                Based on: <strong>${data.based_on.title}</strong> (Score: ${data.based_on.score}/10)
            `;
        }
        
        updateLastUpdated(data.generated_at);
    } catch (error) {
        document.getElementById('linkedin-post').textContent = 'Content will be generated at 5 AM or 6 PM IST.';
    }
}

// Load Carousel
async function loadCarousel() {
    try {
        const response = await fetch(DATA_PATH + 'carousel.json');
        const data = await response.json();
        
        const container = document.getElementById('carousel-content');
        
        if (data.slides && data.slides.length > 0) {
            container.innerHTML = data.slides.map((slide, i) => `
                <div class="slide-card">
                    <div class="slide-number">${i + 1}</div>
                    <div class="slide-content">${formatSlideContent(slide.content)}</div>
                </div>
            `).join('');
        } else if (data.raw_content) {
            // Parse raw content into slides
            const slides = parseRawCarousel(data.raw_content);
            container.innerHTML = slides.map((content, i) => `
                <div class="slide-card">
                    <div class="slide-number">${i + 1}</div>
                    <div class="slide-content">${content}</div>
                </div>
            `).join('');
        }
    } catch (error) {
        document.getElementById('carousel-content').innerHTML = '<p>Carousel content will be generated soon.</p>';
    }
}

function formatSlideContent(content) {
    if (!content) return '';
    return content
        .replace(/Heading:\s*/gi, '<strong>')
        .replace(/Body:\s*/gi, '</strong><br>')
        .replace(/\n/g, '<br>')
        .trim();
}

function parseRawCarousel(raw) {
    const slides = [];
    const parts = raw.split(/SLIDE\s*\d+[:\s]*/i);
    for (const part of parts) {
        const cleaned = part.trim();
        if (cleaned) {
            slides.push(formatSlideContent(cleaned));
        }
    }
    return slides;
}

// Load Newsletter
async function loadNewsletter() {
    try {
        const response = await fetch(DATA_PATH + 'newsletter.json');
        const data = await response.json();
        
        const metaEl = document.getElementById('newsletter-meta');
        metaEl.innerHTML = `
            <div class="newsletter-meta-item">
                <strong>Series:</strong> ${data.series || 'From Non-Tech to Tech-Aware GRC'}
            </div>
            <div class="newsletter-meta-item">
                <strong>Episode:</strong> ${data.episode || '?'}
            </div>
            <div class="newsletter-meta-item">
                <strong>Topic:</strong> ${data.title || 'Loading...'}
            </div>
        `;
        
        document.getElementById('newsletter-content').textContent = data.content;
    } catch (error) {
        document.getElementById('newsletter-meta').innerHTML = '<div class="newsletter-meta-item">Newsletter generates every Tuesday</div>';
        document.getElementById('newsletter-content').textContent = 'Newsletter will be generated on Tuesday for Wednesday publishing.';
    }
}

// Load Top News
async function loadTopNews() {
    try {
        const response = await fetch(DATA_PATH + 'articles.json');
        const articles = await response.json();
        
        allArticles = articles;
        
        // Update stats
        document.getElementById('total-articles').textContent = articles.length;
        if (articles.length > 0) {
            document.getElementById('top-score').textContent = articles[0].score || '?';
        }
        
        renderNews(articles);
        renderDomainDistribution(articles);
    } catch (error) {
        document.getElementById('news-list').innerHTML = '<p style="padding: 2rem; text-align: center; color: var(--text-secondary);">News will be available after the first pipeline run.</p>';
    }
}

function renderNews(articles) {
    const container = document.getElementById('news-list');
    
    if (!articles || articles.length === 0) {
        container.innerHTML = '<p style="padding: 2rem; text-align: center; color: var(--text-secondary);">No articles found.</p>';
        return;
    }
    
    const topArticles = articles.slice(0, 10);
    
    container.innerHTML = topArticles.map(article => {
        const score = article.score || 5;
        const scoreClass = score >= 7 ? 'high' : (score >= 4 ? 'medium' : 'low');
        const domain = getPrimaryDomain(article.domains);
        const domainInfo = DOMAINS[domain] || { color: 'grc', label: domain || 'GRC' };
        
        return `
            <a href="${article.url || '#'}" target="_blank" class="news-item" data-domains="${(article.domains || []).join(',')}">
                <div class="news-score ${scoreClass}">${score}</div>
                <div class="news-content">
                    <div class="news-title">${escapeHtml(article.title)}</div>
                    <div class="news-meta">
                        <span class="news-source">${article.source || 'Unknown'}</span>
                        <span class="news-domain ${domainInfo.color}">${domainInfo.label}</span>
                    </div>
                </div>
                <div class="news-arrow">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                </div>
            </a>
        `;
    }).join('');
}

function getPrimaryDomain(domains) {
    if (!domains || domains.length === 0) return 'GRC';
    
    // Map to our simplified domains
    const domainMap = {
        'Privacy & Data Protection': 'Privacy',
        'Data Protection': 'Privacy',
        'Information Security': 'Security',
        'AI Governance & Ethics': 'AI',
        'AI Governance': 'AI',
        'Regulatory Compliance': 'GRC',
        'Risk Management': 'GRC',
        'GRC Career & Skills': 'GRC',
        'GRC General': 'GRC'
    };
    
    for (const d of domains) {
        if (domainMap[d]) return domainMap[d];
        if (DOMAINS[d]) return d;
    }
    
    return domains[0] || 'GRC';
}

function renderDomainDistribution(articles) {
    const counts = {
        'GRC': 0,
        'Privacy': 0,
        'Security': 0,
        'DevSecOps': 0,
        'AI': 0,
        'Product': 0
    };
    
    articles.forEach(article => {
        const domain = getPrimaryDomain(article.domains);
        if (counts.hasOwnProperty(domain)) {
            counts[domain]++;
        } else {
            counts['GRC']++;
        }
    });
    
    const maxCount = Math.max(...Object.values(counts), 1);
    
    const container = document.getElementById('domain-bars');
    container.innerHTML = Object.entries(counts).map(([domain, count]) => {
        const percentage = (count / maxCount) * 100;
        const info = DOMAINS[domain] || { color: 'grc' };
        
        return `
            <div class="domain-bar-item">
                <span class="domain-bar-label">${domain}</span>
                <div class="domain-bar-track">
                    <div class="domain-bar-fill ${info.color}" style="width: ${percentage}%"></div>
                </div>
                <span class="domain-bar-count">${count}</span>
            </div>
        `;
    }).join('');
}

// Domain Filters
function setupDomainFilters() {
    const pills = document.querySelectorAll('.domain-pill');
    
    pills.forEach(pill => {
        pill.addEventListener('click', () => {
            // Update active state
            pills.forEach(p => p.classList.remove('active'));
            pill.classList.add('active');
            
            // Filter news
            const domain = pill.dataset.domain;
            currentFilter = domain;
            filterNews(domain);
        });
    });
}

function filterNews(domain) {
    const newsItems = document.querySelectorAll('.news-item');
    
    newsItems.forEach(item => {
        if (domain === 'all') {
            item.style.display = 'flex';
        } else {
            const itemDomains = item.dataset.domains || '';
            const primaryDomain = getPrimaryDomain(itemDomains.split(','));
            
            if (primaryDomain === domain || itemDomains.toLowerCase().includes(domain.toLowerCase())) {
                item.style.display = 'flex';
            } else {
                item.style.display = 'none';
            }
        }
    });
}

// Update last updated time
function updateLastUpdated(timestamp) {
    const el = document.getElementById('last-updated');
    if (timestamp) {
        const date = new Date(timestamp);
        const options = { 
            month: 'short', 
            day: 'numeric',
            hour: '2-digit', 
            minute: '2-digit'
        };
        el.innerHTML = `<span class="pulse"></span><span>Updated ${date.toLocaleDateString('en-IN', options)}</span>`;
    }
}

// Copy content to clipboard
async function copyContent(elementId) {
    const element = document.getElementById(elementId);
    let text = element.innerText || element.textContent;
    
    try {
        await navigator.clipboard.writeText(text);
        
        // Find the copy button for this section
        const section = element.closest('.content-card') || element.closest('.newsletter-card');
        const btn = section.querySelector('.copy-btn');
        
        const originalHTML = btn.innerHTML;
        btn.innerHTML = `
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="20 6 9 17 4 12"/>
            </svg>
            <span>Copied!</span>
        `;
        btn.classList.add('copied');
        
        setTimeout(() => {
            btn.innerHTML = originalHTML;
            btn.classList.remove('copied');
        }, 2000);
    } catch (error) {
        alert('Failed to copy. Please select and copy manually.');
    }
}

// Escape HTML
function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('password-input').focus();
});
