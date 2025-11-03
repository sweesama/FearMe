# Fear Me Game Landing Site

_Last updated: 2025-10-30_

## Overview
This repository hosts the promotional landing page for **Fear Me: Jeff The Killer Dating Sim**. The site targets organic Google search traffic for the "Fear Me" keyword and introduces players to the browser-based horror visual novel, while curating guides, updates, and safety information.

The page is a single static HTML document (`index.html`) with inline styles and scripts. Supporting files provide SEO metadata, crawler directives, and deployment settings for static hosting platforms (e.g., Vercel).

## Key Files
- `index.html` – Complete landing page with embedded game iframe, walkthrough, character dossier, news timeline, and FAQ.
- `404.html` – Custom not-found page mirroring the horror branding.
- `favicon.png` – Site icon referenced from the HTML head.
- `robots.txt` – Allows all crawlers and points to the sitemap.
- `sitemap.xml` – Lists anchors for major sections (Home, Walkthrough, Characters, News, FAQ) with current timestamps.
- `llms.txt` – Quick reference metadata for large-language-model prompts or SEO assistants.
- `vercel.json` – Deployment headers; enforces security-oriented response headers.

## Current Site Sections (anchor IDs)
1. `#game` – Play Fear Me directly via itch.io iframe, plus survival overview and quick tips.
2. `#walkthrough` – Chapter-by-chapter guidance, decision advice, ending conditions, and speedrun checklist.
3. `#characters` – Jeff the Killer profile with motivations, interaction tactics, and survival reminders.
4. `#news` – Timeline of official devlog updates, community discoveries, localization milestones, and platform releases.
5. `#faq` – Answers covering platforms, content warnings, pricing, playtime, offline availability, feedback channels, and roadmap expectations.

## Recent Updates (2025-10-30)
- Added detailed **News** timeline covering 2025 release milestones, localization beta, community theories, and APK availability.
- Introduced a dedicated **FAQ** tab with seven high-signal questions for search intent coverage.
- Refreshed **meta tags** (title/description, Open Graph, Twitter Card) for improved SERP snippets and social sharing.
- Expanded **structured data** (VideoGame schema) with platform, author, publisher, and keyword fields.
- Updated `sitemap.xml`, `llms.txt`, and ensured `robots.txt` references the latest sitemap.
- Linked the new `favicon.png` and verified consistent English copy across all public text.

## Quick Start
1. Open `index.html` in a modern browser to preview the page locally.
2. Deploy to a static host (e.g., Vercel). Ensure `vercel.json` is honored for security headers.
3. Confirm the sitemap (`/sitemap.xml`) and robots instructions (`/robots.txt`) are accessible after deployment.

## SEO & Content Notes
- Primary keyword targets: `fear me game`, `Jeff the Killer dating sim`, `fear me walkthrough`, `fear me endings`, `fear me faq`.
- Headings follow a strict hierarchy: single `<h1>` in the game tab, with supporting `<h2>`/`<h3>`/`<h4>` for subsections.
- JSON-LD schema describes the game, platforms (Web/Windows/Android), and upcoming roadmap elements.
- FAQ responses align with E-E-A-T guidelines by citing official itch.io touchpoints and safety warnings.

## Next Steps
1. **Deepen Walkthrough Coverage** – Add Chapters 3+ with exact choice trees, affection thresholds, and screenshots (optional).
2. **Player Testimonials & Media** – Embed curated quotes or video reviews to increase trust and dwell time.
3. **Performance Enhancements** – Consider extracting CSS into an external file, enabling iframe lazy loading, and compressing assets.
4. **Localized Content Strategy** – Prepare bilingual sections or separate guides (e.g., Mandarin) once translations stabilize.
5. **Monitor Devlog Feed** – Schedule periodic updates to News/FAQ after each official itch.io announcement.

For future revisions, append change summaries here and adjust the "Last updated" stamp to match deployment dates.
