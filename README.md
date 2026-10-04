# ashiq-r-khan.github.io

Source of my portfolio site: https://ashiq-r-khan.github.io

Plain HTML, CSS and JavaScript. No build step.

## Edit the site

| To change | Edit |
|---|---|
| Projects | `data/site.js`, the `PROJECTS` list. Add a cover image (16:9) to `assets/projects/`. |
| Blog posts | `data/site.js`, the `POSTS` list. The Blog section appears once there is one post. |
| Email, contact form key | `data/site.js`, the `SITE` block |
| Hero, about, skills, certifications | `index.html` |
| Colours and fonts | top of `css/style.css` |
| Photo and CV | replace `assets/profile.jpg` and `assets/CV.pdf` (same file names) |

A blog post entry looks like this:

```js
{date:"October 2026", title:"Post title", excerpt:"First two or three lines of the post.", url:"https://www.linkedin.com/posts/..."}
```

## Contact form

The form sends through Web3Forms. Get a free access key at https://web3forms.com, then paste it into `web3formsKey` in `data/site.js`. While the key is empty the form opens the visitor's email app instead.

## Credits

Project cover photos are from Unsplash, by Jair Lazaro, Towfiqu Barbhuiya, Krzysztof Płocha, Boxed Water Is Better, Leo_Visions and Shutter Speed.
