# Blog build

The pages in `blog/` are made from the Markdown files in `_build/posts/`. GitHub Pages ignores this folder, so nothing in it is published.

```
python3 _build/build.py          # writes blog/*.html and the reading times in data/site.js
python3 _build/share_images.py   # writes assets/blog/*.jpg (needs Playwright with Chromium)
```

`build.py` needs the Python packages `markdown`, `numpy` and `scipy`.

## Writing a post

Each file in `posts/` starts with a header (`slug`, `title`, `series`, `part`, `date`, `iso`, `standfirst`, `excerpt`), then a line with `---`, then the text in Markdown. Add the post to the `POSTS` list in `data/site.js` with the same `slug`.

| To write | Use |
|---|---|
| Inline formula | `$x^2$` |
| Formula on its own line | `$$x^2$$` |
| A dollar sign in text | `\$` |
| Box | `::: simple`, `::: example`, `::: mistake`, `::: remember`, `::: own` or `::: note`, then the text, then `:::` on its own line |
| Example with a label | `::: example real Title` or `::: example illus Title` |
| Question with a hidden answer | `??? question`, the answer on the next line, then `???` |
| Figure | `[[fig:name|Bold lead.|Rest of the caption.]]`, where `name` is a function listed in `FIGS` in `figures.py` |
| Section that shows in "On this page" | `## Heading {#short-id}` |

After a change to CSS or JavaScript, set a new value for `V` at the top of `build.py` and rebuild, and change `?v=...` in `index.html` and `project.html` to the same value.
