# How to add content (beginner guide)

## How the site is organised
- One front page, `public/index.html`, with a section for each category: Research, Food, Learning, Writing, Workbench. Each section is a list of entries.
- An entry is a link: to a page in this site (a piece of writing) or to another site (an app on its own Worker).
- Do not make a page per category yet. When a section has about five entries, give it its own page (for example `public/writing/index.html`, copied from the front page) and link to it. Empty pages hurt discoverability.

## Add a piece of writing
1. Copy `templates/article.html` to `public/writing/my-title.html` (lowercase, dashes, no spaces).
2. Open it in a text editor. Change the `<title>`, the description, the `<h1>`, and replace "Text goes here." (cheat sheet below). Double-click the file to preview it in your browser.
3. In `public/index.html`, in the Writing section, delete `<li class="soon">Coming soon.</li>` (first time only) and add:
   `<li><a href="writing/my-title.html">My Title</a><span>One-line description.</span></li>`
4. In `public/sitemap.xml`, add a line: `<url><loc>https://metanoia.agathos.workers.dev/writing/my-title</loc></url>`
5. Publish:
cd /home/gaia/metanoia/
       git add -A
       git commit -m "Add: My Title"
       git push origin main

   The site updates in about a minute.

## Writing text in HTML
- Paragraph: `<p>Your text.</p>`
- Subheading: `<h2>Heading</h2>`
- Italic: `<em>text</em>`. Bold: `<strong>text</strong>`
- Link: `<a href="https://example.org">words</a>`
- Quote: `<blockquote><p>Quoted text.</p></blockquote>`
- List: `<ul><li>One</li><li>Two</li></ul>`
- Poem: one `<p>` per stanza, with `<br>` at the end of each line.
Tip: write in a document first, then ask Claude: "Fit this text into templates/article.html."

## Add a project or app
Deploy it as its own Worker, then add an entry in its section linking to its address. Research, Food and Learning entries work the same way as writing.

## Rules
No names, places or phone numbers. Publish only what you wrote or may license, and cite sources. Everything is public.
