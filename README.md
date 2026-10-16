# Koch Christmas Trees

A small, dependency-free HTML/CSS website. No CMS, package install, build tool, or browser JavaScript. The design intentionally uses a compact, traditional small-business layout with straightforward seasonal information.

## Preview and check

```sh
python3 scripts/check.py
python3 -m http.server 8000 --directory site
```

Open http://localhost:8000. Content lives in `site/index.html`; styles live in `site/styles.css`.

## GitHub Pages setup

1. Create a GitHub repository and push this directory to its `main` branch.
2. In the repository, choose **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. Run **Actions → Check and deploy site → Run workflow** if the first push ran before Pages was enabled.
4. The deployment job publishes only `site/`. Later pushes to `main` automatically check and deploy. Pull requests run checks without deploying.

The workflow uses GitHub's built-in token and requires no personal access token or deployment secret. If your organization restricts Actions or Pages, an administrator may need to enable them. Public repositories can use GitHub Pages on GitHub Free; private repository Pages requires a supported paid plan.

All asset paths are relative, so the site works at `https://OWNER.github.io/REPOSITORY/` as well as at a custom domain.

## Custom domain later

The live WordPress domain has deliberately not been changed. First review the GitHub Pages URL. When ready, configure `kochchristmastrees.com` in GitHub's Pages settings and follow its DNS instructions. Preserve email records, verify HTTPS, and retain a WordPress backup before retiring the old hosting. No CNAME is included yet.

## Updating with ChatGPT / Codex

Use a coding session that can access this repository. A regular chat does not automatically have permission to change GitHub files or publish a site. Connect the repo or supply its files, review the proposed changes, and merge/push to `main` when ready.

Example request:

> Update the seasonal announcement in this repository using the following details: [paste approved details]. Follow AGENTS.md, preserve the design and booking link unless instructed otherwise, run the checks, and prepare a pull request for review.

For direct publishing, explicitly authorize committing and pushing to main. Deployment is automatic after that push.

## Content provenance and launch review

Initial copy is adapted from https://kochchristmastrees.com/ as retrieved on October 16, 2026: 25th season; 2026 reservations open; one slot per family; listed varieties and tree sizes; late-season spruce guidance; Ramsey family wreaths; complimentary hot chocolate; tagged-tree policy. Confirm seasonal details before launch. Address, hours, pricing, and contact information were not provided, so they have not been invented. The existing Square booking URL is preserved, but appointment availability must be verified by an owner.

The check script verifies local assets, anchors, basic HTML nesting, image alt attributes, and relative paths. It is not an external link checker or a full accessibility audit.
