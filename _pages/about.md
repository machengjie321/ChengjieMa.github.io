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

# <i class="fas fa-user"></i> About Me

I am <span class="accent-text">MA CHENGJIE</span>, a Ph.D. student in <span class="primary-gradient-text">Electrical and Electronic Engineering</span> at <span class="primary-gradient-text">Yonsei University</span>, based in <span class="primary-gradient-text">Sinchon, Seoul</span>. My research focuses on <span class="primary-gradient-text">Efficient Machine Learning, Federated Learning, LLM Fine-tuning, and AI-RAN</span>. If you enjoy <span class="primary-gradient-text">badminton, cycling, hiking,</span> or <span class="primary-gradient-text">academic exchange</span>, feel free to reach out. You can contact me at <a href="mailto:cjma@ramo.yonsei.ac.kr" class="link-accent">cjma@ramo.yonsei.ac.kr</a>.

# <i class="fas fa-bullhorn"></i> News

- *New*: My first ICML.

# <i class="fas fa-file-alt"></i> Publications

<div id="scholar-pubs" class="scholar-pubs-grid"></div>
<p id="scholar-pubs-status" class="scholar-status">Loading publications from Google Scholar...</p>

# <i class="fas fa-graduation-cap"></i> Educations

- *2024.09 - Present*: Ph.D. student, Department of Electrical and Electronic Engineering, Yonsei University
  - GPA: 97.3/100
  - Advisor: Professor Seong-Lyun Kim
  - Research focus: Efficient Machine Learning and AI-RAN

- *2021.09 - 2024.06*: M.S. in Computer Science and Technology, Beijing University of Posts and Telecommunications
  - GPA: 92.69/100
  - Advisor: Professor Junping Du
  - Thesis: Communication-efficient Federated Learning with Asynchrony and Pruning

- *2017.09 - 2021.06*: B.S. in Computer Science and Technology, Chongqing University of Posts and Telecommunications
  - GPA: 87.11/100, Top 2%
  - Honorary Bachelor's Degree
  - Minor: Business Administration

# <i class="fas fa-briefcase"></i> Internships

- *2025.09 - Present*: LLM fine-tuning and LoRA structure research, Yonsei University
  - Exploring efficient fine-tuning methods for edge clients with limited compute and memory.
  - Studying adaptive LoRA structures to improve parameter efficiency and training performance.

- *2025.09 - Present*: AI-RAN research, Yonsei University
  - Investigating GPU-accelerated base-station architectures for AI-RAN.
  - Exploring the feasibility of moving selected gNB L1 workloads from CPU to GPU using NVIDIA Aerial.

- *2024.09 - 2025.09*: Heterogeneous client federated learning, Yonsei University
  - Studied federated learning with diverse client devices, asynchronous training, and heterogeneous model capacities.
  - Analyzed how system and model heterogeneity affect update drift and training degradation.

- *2022.09 - 2024.06*: Communication-efficient federated learning, Beijing University of Posts and Telecommunications
  - Participated in a subproject of a National Natural Science Foundation major project.
  - Focused on asynchronous training, model pruning, and federated topic modeling.

- *2022.03 - 2022.09*: Shared mobility review and sentiment analysis, BUPT-Didi joint project
  - Conducted topic analysis of user reviews from a shared mobility platform.
  - Analyzed user feedback and sentiment trends for taxi connection scenarios.

<script>
(function () {
  const dataUrl = "{{ gsDataBaseUrl }}google-scholar-stats/gs_data.json";
  const pubsEl = document.getElementById('scholar-pubs');
  const statusEl = document.getElementById('scholar-pubs-status');
  const totalCitEl = document.getElementById('total_cit');
  const fallbackPublications = [
    {
      title: "Breaking the Capacity Bottleneck in Model-Heterogeneous Federated Learning via Gradual Model Restoration",
      authors: "C Ma, S Oh, J Park, SL Kim",
      venue: "Forty-Third International Conference on Machine Learning",
      year: "2025",
      num_citations: "2*"
    },
    {
      title: "Federated Topic Model and Model Pruning Based on Variational Autoencoder",
      authors: "C Ma, Y Li, M Liang, A Li",
      venue: "Chinese Intelligent Automation Conference, 51-60",
      year: "2023",
      num_citations: "1"
    },
    {
      title: "Topic model based on co-occurrence word networks for unbalanced short text datasets",
      authors: "C Ma, J Du, M Liang, Z Guan",
      venue: "2023 5th International Conference on Data-driven Optimization of Complex Systems and Applications",
      year: "2023",
      num_citations: "1"
    }
  ];

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

  function renderFallback(message) {
    pubsEl.innerHTML = '';
    fallbackPublications.forEach(pub => pubsEl.appendChild(renderPublication(pub)));
    statusEl.textContent = message;
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
        renderFallback('Google Scholar has not returned publication data yet. Showing the current manual list.');
        return;
      }

      visiblePublications.forEach(pub => pubsEl.appendChild(renderPublication(pub)));
      statusEl.remove();
    })
    .catch(() => {
      if (totalCitEl) {
        totalCitEl.textContent = '0';
      }
      renderFallback('Google Scholar sync is temporarily unavailable. Showing the current manual list.');
    });
})();
</script>

# <i class="fas fa-book-open"></i> Blogs

- Visit the [blog page](/blog/) for posts and updates.
