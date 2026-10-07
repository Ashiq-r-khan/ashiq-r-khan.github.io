# ashiq-r-khan.github.io

Source of my portfolio site: https://ashiq-r-khan.github.io

Plain HTML, CSS and JavaScript. The site needs no build step to run. Only the blog pages are generated from Markdown (see Blog).

## Edit the site

| To change | Edit |
|---|---|
| Projects | `data/site.js`, the `PROJECTS` list. Each entry builds a home card and its own page (`project.html?p=slug`) with findings, methods and screenshots. Put the cover (16:9) in `assets/projects/` and screenshots in `assets/projects/<slug>/`. |
| Blog posts | Text in `_build/posts/*.md`, list in `data/site.js` (`POSTS` and `SERIES`). See "Blog" below. |
| Email, contact form key | `data/site.js`, the `SITE` block |
| Hero, about, skills, certifications | `index.html` |
| Colours and fonts | top of `css/style.css` |
| Photo and CV | replace `assets/profile.jpg` and `assets/CV.pdf` (same file names) |

## Blog

The home page shows the first three entries of `POSTS`, and `blog/index.html` shows all of them grouped by series. Each post is its own page, `blog/<slug>.html`, with formulas drawn by KaTeX (`assets/katex/`) and a share image in `assets/blog/`.

The post pages are not written by hand. They are made from the Markdown files in `_build/posts/` by `python3 _build/build.py`. To change a post, edit its `.md` file and run the build again. `_build/README.md` explains the format.

A post written on LinkedIn can be listed too. Give it a `url` in place of a `slug`:

```js
{date:"October 2026", title:"Post title", excerpt:"First two or three lines of the post.", url:"https://www.linkedin.com/posts/..."}
```

## After changing CSS or JavaScript

Browsers keep old copies of `css/style.css`, `js/*.js` and `data/site.js` for a while. After editing any of them, change the `?v=...` value in `index.html` and `project.html`, and `V` in `_build/build.py` (then run the build), to a new value (today's date works), so visitors get the new files straight away.

## Contact form

The form sends through Web3Forms. Get a free access key at https://web3forms.com, then paste it into `web3formsKey` in `data/site.js`. While the key is empty the form opens the visitor's email app instead.

## Credits

Formulas on the blog are drawn with [KaTeX](https://katex.org) (MIT licence). Project cover photos are from Unsplash, by Jair Lazaro, Towfiqu Barbhuiya, Krzysztof Płocha, Boxed Water Is Better, Leo_Visions and Shutter Speed.
