---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}

<style>
.scholar-summary {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0 2rem;
}

.scholar-summary-card,
.scholar-paper-card {
  border: 1px solid rgba(15, 23, 42, 0.08);
  border-radius: 18px;
  background: linear-gradient(180deg, rgba(255,255,255,0.94), rgba(248,250,252,0.98));
  box-shadow: 0 18px 40px rgba(15, 23, 42, 0.06);
}

.scholar-summary-card {
  padding: 1.1rem 1.2rem;
}

.scholar-summary-card h3,
.scholar-paper-card h3 {
  margin: 0 0 0.4rem;
}

.scholar-summary-label {
  font-size: 0.88rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: rgba(15, 23, 42, 0.56);
  margin-bottom: 0.35rem;
}

.scholar-summary-value {
  font-size: 1.4rem;
  font-weight: 700;
  color: #0f172a;
}

.scholar-summary-copy {
  color: rgba(15, 23, 42, 0.8);
  margin: 0.35rem 0 0;
}

.scholar-pubs-grid {
  display: grid;
  gap: 1rem;
  margin-top: 1rem;
}

.scholar-paper-card {
  padding: 1.1rem 1.2rem;
}

.scholar-paper-title {
  font-size: 1.04rem;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 0.45rem;
}

.scholar-paper-meta {
  font-size: 0.92rem;
  line-height: 1.55;
  color: rgba(15, 23, 42, 0.76);
}

.scholar-paper-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  margin-top: 0.75rem;
  padding: 0.32rem 0.7rem;
  border-radius: 999px;
  background: rgba(14, 165, 233, 0.1);
  color: #0369a1;
  font-size: 0.84rem;
  font-weight: 600;
}

.scholar-status {
  margin-top: 0.85rem;
  color: rgba(15, 23, 42, 0.68);
}

@media (max-width: 640px) {
  .scholar-summary-card,
  .scholar-paper-card {
    border-radius: 14px;
  }
}
</style>

<span class='anchor' id='about-me'></span>

I am <span class="accent-text">MA CHENGJIE</span> (<span>马成洁</span>) at <span class="primary-gradient-text">Yonsei University</span>. My research focus is <span class="primary-gradient-text">efficient deep learning</span>. You can reach me at <a href="mailto:cjma@ramo.yonsei.ac.kr" class="link-accent">cjma@ramo.yonsei.ac.kr</a>.

<div class="quote-accent">
This homepage is wired to sync publication metadata from <span class="primary-gradient-text">Google Scholar</span>.
</div>

<div class="scholar-summary">
  <div class="scholar-summary-card floating-card">
    <div class="scholar-summary-label">Affiliation</div>
    <div class="scholar-summary-value">Yonsei University</div>
    <p class="scholar-summary-copy">Current homepage placeholder until you want to add a fuller bio.</p>
  </div>
  <div class="scholar-summary-card floating-card">
    <div class="scholar-summary-label">Research</div>
    <div class="scholar-summary-value">Efficient deep learning</div>
    <p class="scholar-summary-copy">You can later expand this into topics, projects, and recent news.</p>
  </div>
  <div class="scholar-summary-card floating-card">
    <div class="scholar-summary-label">Scholar Sync</div>
    <div class="scholar-summary-value"><span id="total_cit">loading...</span> citations</div>
    <p class="scholar-summary-copy">Publications will appear automatically after the GitHub Action writes Scholar data.</p>
  </div>
</div>

# <i class="fas fa-file-alt"></i> Publications

<div id="scholar-pubs" class="scholar-pubs-grid"></div>
<p id="scholar-pubs-status" class="scholar-status">Loading publications from Google Scholar...</p>

<script>
(function () {
  const dataUrl = "{{ gsDataBaseUrl }}google-scholar-stats/gs_data.json";
  const pubsEl = document.getElementById('scholar-pubs');
  const statusEl = document.getElementById('scholar-pubs-status');
  const totalCitEl = document.getElementById('total_cit');

  function asText(value) {
    return value === null || value === undefined ? '' : String(value);
  }

  function firstNonEmpty(values) {
    for (const value of values) {
      if (value !== null && value !== undefined && String(value).trim() !== '') {
        return String(value).trim();
      }
    }
    return '';
  }

  function renderPublication(pub) {
    const card = document.createElement('article');
    card.className = 'scholar-paper-card floating-card';

    const title = firstNonEmpty([
      pub && pub.bib && pub.bib.title,
      pub && pub.title,
      'Untitled publication'
    ]);
    const authors = firstNonEmpty([
      pub && pub.bib && pub.bib.author,
      pub && pub.authors
    ]);
    const venue = firstNonEmpty([
      pub && pub.bib && pub.bib.venue,
      pub && pub.bib && pub.bib.journal,
      pub && pub.bib && pub.bib.publisher
    ]);
    const year = firstNonEmpty([
      pub && pub.bib && pub.bib.pub_year,
      pub && pub.year
    ]);
    const citations = pub && pub.num_citations ? pub.num_citations : 0;

    const titleEl = document.createElement('div');
    titleEl.className = 'scholar-paper-title';
    titleEl.textContent = title;

    const metaEl = document.createElement('div');
    metaEl.className = 'scholar-paper-meta';
    const metaParts = [];
    if (authors) metaParts.push(authors);
    if (venue) metaParts.push(venue);
    if (year) metaParts.push(year);
    metaEl.textContent = metaParts.join(' · ');

    const badgeEl = document.createElement('div');
    badgeEl.className = 'scholar-paper-badge';
    badgeEl.textContent = `Citations: ${asText(citations)}`;

    card.appendChild(titleEl);
    if (metaParts.length > 0) {
      card.appendChild(metaEl);
    }
    card.appendChild(badgeEl);
    return card;
  }

  fetch(dataUrl, { cache: 'no-store' })
    .then(response => {
      if (!response.ok) {
        throw new Error(`Failed to load ${dataUrl}: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      if (totalCitEl) {
        totalCitEl.textContent = asText(data && data.citedby ? data.citedby : 0);
      }

      const publications = Object.values((data && data.publications) || {})
        .sort((left, right) => (right.num_citations || 0) - (left.num_citations || 0));

      const visiblePublications = publications.slice(0, 12);
      if (!visiblePublications.length) {
        statusEl.textContent = 'No publications were returned by Google Scholar yet.';
        return;
      }

      visiblePublications.forEach(pub => pubsEl.appendChild(renderPublication(pub)));
      statusEl.remove();
    })
    .catch(() => {
      if (totalCitEl) {
        totalCitEl.textContent = '0';
      }
      statusEl.textContent = 'Google Scholar data is not available yet. Enable the GitHub Action and wait for the first sync.';
    });
})();
</script>
