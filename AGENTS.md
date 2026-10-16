# Koch Christmas Trees

This is a buildless static site deployed to GitHub Pages from `main`.

- Edit page content in `site/*.html`, styles in `site/styles.css`, and illustrations in `site/assets/`.
- Preserve the compact, traditional style: simple headings, modest spacing, ordinary links, and matter-of-fact copy. Avoid oversized hero sections, marketing slogans, and decorative illustrations.
- Keep the site dependency-free and usable without JavaScript. No framework or CMS is needed.
- Keep all asset and internal page paths relative so repository subpaths work on GitHub Pages.
- Preserve the Square reservation URL unless the owners provide a replacement.
- Do not invent addresses, hours, prices, contact details, opening dates, or availability.
- Seasonal information comes from the owners. When changing the season, review the year, anniversary, booking status, varieties, sizes, wreaths, and booking rules together. Do not automatically declare reservations open based on the date.
- Maintain heading hierarchy, keyboard focus indicators, descriptive links, contrast, and mobile layout.
- Run `python3 scripts/check.py` before finishing. Preview desktop and mobile when changing layout.
- Only `site/` is published. Never add secrets or private owner information there.
- Do not change DNS, add a CNAME, or replace the existing WordPress site without explicit instruction.
- Explain the changes and checks. If asked to publish, push to main only when authorized; otherwise prepare a branch/PR.

- Navigation is shared manually across all seven HTML pages; keep links and current-page markers consistent. Update seasonal hours in `site/dates-and-hours.html` alongside the homepage.
