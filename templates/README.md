# Agathos

A static site for Cloudflare Workers. Everything served lives in `public/`.
SPDX-License-Identifier: AGPL-3.0-only (code). Content: CC BY-NC-SA 4.0.
To add content, read `HOW-TO-ADD-CONTENT.md`.

## Repository layout (important)
`wrangler.jsonc` and `public/` sit directly at the repository root:

    wrangler.jsonc
    public/index.html, style.css, robots.txt, sitemap.xml
    templates/article.html   (not served; copy and fill)

If the project ever sits in a subfolder, set Root directory to it in the Worker's Settings > Build.

## Deploy
The Worker's name in Cloudflare must equal `name` in `wrangler.jsonc` exactly: `metanoia`. Settings > Build: build command empty, deploy command `npx wrangler deploy`. Every push to main redeploys.
"Could not detect a directory containing static files" means wrangler cannot see `wrangler.jsonc` where the build runs.

## Being found
Production `workers.dev` addresses are not blocked from search engines. What helps: `robots.txt` and `sitemap.xml` (keep the sitemap current), links from other places, and Search Console.
1. Sign in to Google Search Console with the alternative Google account, add the site as a URL-prefix property, and verify with the HTML tag method (paste the tag into the `<head>` of `public/index.html`, push, then verify).
2. Submit `sitemap.xml`. Do the same in Bing Webmaster Tools.
3. If you ever move to your own domain, change the address in `canonical`, `og:url`, `robots.txt` and `sitemap.xml`.
Indexing takes days to weeks.

## Licences
Content (writing, descriptions): CC BY-NC-SA 4.0. Code (HTML, CSS, config): AGPL-3.0-only; full text in `LICENSE`. Keep the two in separate files.

## Privacy checklist
Everything on the site is public and findable; only your identity is private. No names, places or phone numbers on any page or in any file. The GitHub profile and commit history are public: check your commit email and GitHub's "Keep my email addresses private" setting.
