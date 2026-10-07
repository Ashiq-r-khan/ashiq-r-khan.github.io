"""Turn _build/posts/*.md into the static pages in blog/. Run from anywhere: python3 _build/build.py"""
import html
import re
import sys
from pathlib import Path

import markdown

from figures import FIGS

HERE = Path(__file__).resolve().parent
SITE = HERE.parent
V = "20261007a"
BASE = "https://ashiq-r-khan.github.io"
BOXES = {"simple": "In simple words", "example": "Example", "mistake": "Common mistake", "remember": "Remember", "own": "From my own work", "note": ""}
TAGS = {"real": "Real data", "illus": "Illustrative numbers"}


def md(text):
    return markdown.markdown(text, extensions=["tables", "attr_list", "md_in_html", "sane_lists"])


def inline(text):
    return re.sub(r"^<p>|</p>$", "", md(text).strip())


def convert(src):
    store = []

    def keep(s):
        store.append(s)
        return f"@@K{len(store) - 1}@@"

    src = src.replace("\\$", keep("$"))
    # maths: $$...$$ display, $...$ inline
    src = re.sub(r"\$\$(.+?)\$\$", lambda m: keep("\\[" + html.escape(m[1].strip(), quote=False) + "\\]"), src, flags=re.S)
    src = re.sub(r"\$(.+?)\$", lambda m: keep("\\(" + html.escape(m[1], quote=False) + "\\)"), src)

    # figures: [[fig:name|caption]]
    n = [0]

    def fig(m):
        n[0] += 1
        lead, _, rest = m[2].partition("|")
        cap = f"<strong>Figure {n[0]}. {inline(lead.strip())}</strong> {inline(rest.strip())}"
        return "\n\n" + keep(f'<figure class="fig" id="fig-{n[0]}">\n<div class="fig__scroll">{FIGS[m[1]]()}</div>\n<figcaption>{cap}</figcaption>\n</figure>') + "\n\n"

    src = re.sub(r"\[\[fig:(\w+)\|(.+?)\]\]", fig, src, flags=re.S)

    # check-yourself questions: ??? question / answer / ???
    def qa(m):
        return "\n\n" + keep(f'<details class="qa">\n<summary>{inline(m[1].strip())}</summary>\n<p>{inline(m[2].strip())}</p>\n</details>') + "\n\n"

    src = re.sub(r"^\?\?\? (.+?)\n(.+?)\n\?\?\?$", qa, src, flags=re.S | re.M)

    # boxes: ::: kind [real|illus] [Title] ... :::
    def box(m):
        kind, tag, title = m[1], m[2], (m[3] or "").strip()
        label = title or BOXES[kind]
        if kind == "example" and title:
            label = title
        head = ""
        if label:
            chip = f' <span class="box__tag">{TAGS[tag]}</span>' if tag else ""
            head = f'<p class="box__label">{label}{chip}</p>\n\n'
        return f'\n\n<div class="box box--{kind}" markdown="1">\n{head}{m[4].strip()}\n\n</div>\n\n'

    src = re.sub(r"^::: (\w+)(?: (real|illus))?(?: ([^\n]+))?\n(.+?)\n:::$", box, src, flags=re.S | re.M)

    out = md(src)
    def wrap(m):
        cols = m[0].split("</tr>")[0].count("<th")
        wordy = max(len(re.sub(r"<[^>]+>", "", c)) for c in re.findall(r"<td[^>]*>(.*?)</td>", m[0], flags=re.S)) >= 40
        cls = "" if not wordy else " t-wide" if cols >= 4 else " t-mid" if cols == 3 else ""
        cls += " t-dense" if cols >= 9 else ""
        return f'<div class="table-wrap{cls}">{m[0]}</div>'

    out = re.sub(r"<table>.*?</table>", wrap, out, flags=re.S)
    out = re.sub(r' style="text-align: (\w+);"', r' class="\1"', out)
    out = out.replace("p &lt; 0", "p&nbsp;&lt;&nbsp;0")
    while "@@K" in out:
        out = re.sub(r"<p>@@K(\d+)@@</p>", lambda m: store[int(m[1])] if store[int(m[1])].startswith(("<figure", "<details")) else f"<p>{store[int(m[1])]}</p>", out)
        out = re.sub(r"@@K(\d+)@@", lambda m: store[int(m[1])], out)
    return out


ICONS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <defs>
    <symbol id="i-menu" viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h16"/></symbol>
    <symbol id="i-back" viewBox="0 0 24 24"><path d="m15 18-6-6 6-6"/></symbol>
    <symbol id="i-next" viewBox="0 0 24 24"><path d="m9 18 6-6-6-6"/></symbol>
    <symbol id="i-file" viewBox="0 0 24 24"><path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 13h4M10 17h4"/></symbol>
  </defs>
</svg>"""

NAV = """<header class="nav">
  <div class="wrap nav__row">
    <a class="nav__brand" href="../index.html">ashiqur.khan</a>
    <button class="nav__toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav-links"><svg class="icon"><use href="#i-menu"/></svg></button>
    <nav id="nav-links" aria-label="Sections">
      <a href="../index.html">Home</a>
      <a href="../index.html#about">About</a>
      <a href="../index.html#skills">Skills</a>
      <a href="../index.html#projects">Projects</a>
      <a href="../index.html#services">What I Can Do</a>
      <a href="../index.html#certifications">Certifications</a>
      <a href="index.html" aria-current="true">Blog</a>
      <a href="../index.html#contact">Contact</a>
    </nav>
  </div>
</header>"""

FOOT = """<footer class="footer">
  <div class="wrap"><p>© <span id="year">2026</span> Md. Ashiqur Rahman Khan</p><p><a href="{href}">{label}</a></p></div>
</footer>"""

POST = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Md. Ashiqur Rahman Khan</title>
<meta name="description" content="{desc}">
<meta name="author" content="Md. Ashiqur Rahman Khan">
<meta name="theme-color" content="#0f1722">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{base}/assets/blog/{slug}.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="article:published_time" content="{iso}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../assets/katex/katex.min.css">
<link rel="stylesheet" href="../css/style.css?v={v}">
</head>
<body>
{icons}
<a class="skip" href="#post">Skip to the post</a>
{nav}
<main class="wrap art" data-slug="{slug}">
  <a class="pp__back" href="index.html"><svg class="icon"><use href="#i-back"/></svg>All posts</a>
  <header class="art__head">
    <p class="hero__role">{series} · Part {part} of {parts}</p>
    <h1>{title}</h1>
    <p class="pp__intro">{standfirst}</p>
    <p class="art__meta"><time datetime="{iso}">{date}</time> · {minutes} min read</p>
  </header>
  <div class="art__grid">
    <details class="toc" open><summary>On this page</summary><nav id="toc" aria-label="On this page"></nav></details>
    <article id="post" class="body">
{body}
    </article>
  </div>
  <nav id="pager" class="pp__pager" aria-label="More posts"></nav>
</main>
{foot}
<script defer src="../assets/katex/katex.min.js"></script>
<script defer src="../assets/katex/auto-render.min.js"></script>
<script defer src="../data/site.js?v={v}"></script>
<script defer src="../js/blog.js?v={v}"></script>
</body>
</html>
"""


INDEX = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Blog | Md. Ashiqur Rahman Khan</title>
<meta name="description" content="Study notes on statistics for public health data by Md. Ashiqur Rahman Khan, with definitions in simple words and worked examples.">
<meta name="theme-color" content="#0f1722">
<link rel="canonical" href="{base}/blog/">
<meta property="og:title" content="Blog | Md. Ashiqur Rahman Khan">
<meta property="og:description" content="Study notes on statistics for public health data, with definitions in simple words and worked examples.">
<meta property="og:type" content="website">
<meta property="og:url" content="{base}/blog/">
<meta property="og:image" content="{base}/assets/blog/blog.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../css/style.css?v={v}">
</head>
<body>
{icons}
{nav}
<main class="wrap blog">
  <a class="pp__back" href="../index.html"><svg class="icon"><use href="#i-back"/></svg>Home</a>
  <h1>Blog</h1>
  <p class="blog__intro">Study notes on statistics for public health data. Each post takes one topic, explains it in simple words and works through the examples by hand.</p>
  <div id="blog-list"></div>
  <noscript><p>The post list needs JavaScript.</p></noscript>
</main>
{foot}
<script src="../data/site.js?v={v}"></script>
<script src="../js/blog.js?v={v}"></script>
</body>
</html>
"""


def front(text):
    head, _, body = text.partition("\n---\n")
    meta = dict(l.split(": ", 1) for l in head.strip().splitlines())
    return meta, body


def build():
    posts = []
    for path in sorted((HERE / "posts").glob("*.md")):
        meta, body = front(path.read_text(encoding="utf-8"))
        body_html = convert(body)
        words = len(re.sub(r"<svg.*?</svg>|<[^>]+>|\\\(.*?\\\)|\\\[.*?\\\]", " ", body_html, flags=re.S).split())
        meta["minutes"] = round(words / 200)
        meta["words"] = words
        page = POST.format(body=body_html, icons=ICONS, nav=NAV, foot=FOOT.format(href="index.html", label="All posts"), v=V, base=BASE, url=f"{BASE}/blog/{meta['slug']}.html", desc=html.escape(meta["excerpt"]), parts=3, **{k: v for k, v in meta.items() if k not in ("excerpt",)})
        (SITE / "blog").mkdir(exist_ok=True)
        (SITE / "blog" / f"{meta['slug']}.html").write_text(page, encoding="utf-8")
        posts.append(meta)
        print(meta["slug"], words, "words,", meta["minutes"], "min,", len(page) // 1024, "KB")
    (SITE / "blog" / "index.html").write_text(INDEX.format(icons=ICONS, nav=NAV, foot=FOOT.format(href="../index.html", label="Home"), v=V, base=BASE), encoding="utf-8")
    data = SITE / "data" / "site.js"
    js = data.read_text(encoding="utf-8")
    for m in posts:
        js = re.sub(r'(slug:"%s",.*?minutes:)\d+' % m["slug"], lambda x: x[1] + str(m["minutes"]), js, flags=re.S)
    data.write_text(js, encoding="utf-8")
    return posts


if __name__ == "__main__":
    build()
