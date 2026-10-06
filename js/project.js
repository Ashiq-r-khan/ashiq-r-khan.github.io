const $=s=>document.querySelector(s),gh=r=>`https://github.com/Ashiq-r-khan/${r}`,i=PROJECTS.findIndex(x=>x.slug===new URLSearchParams(location.search).get('p')),p=PROJECTS[i],ic=n=>`<svg class="icon"><use href="#i-${n}"/></svg>`;
if(!p)location.replace('index.html#projects');
else{
  const next=PROJECTS[(i+1)%PROJECTS.length];
  document.title=`${p.title} | Md. Ashiqur Rahman Khan`;
  $('#project').innerHTML=`<a class="pp__back" href="index.html#projects">${ic('back')}All projects</a>
<p class="hero__role">${p.field}</p>
<h1>${p.title}</h1>
<p class="pp__intro">${p.intro}</p>
<ul class="pills">${p.tools.map(t=>`<li>${t}</li>`).join('')}</ul>
<p class="pp__actions"><a class="btn btn--solid" href="${gh(p.repo)}">${ic('github')}View code on GitHub</a>${p.links.map(l=>`<a class="btn btn--outline" href="${gh(p.repo)}/blob/main/${l.path}">${ic('file')}${l.label}</a>`).join('')}</p>
<img class="pp__cover" src="${p.image}" alt="" width="1200" height="675">
<section><h2>Overview</h2><dl class="pp__overview"><div><dt>Question</dt><dd>${p.question}</dd></div><div><dt>Data</dt><dd>${p.data}</dd></div></dl></section>
<section><h2>Key findings</h2><div class="pp__findings">${p.findings.map(f=>`<div class="card">${f.stat?`<p class="pp__stat">${f.stat}</p>`:''}<h3>${f.title}</h3><p>${f.text}</p></div>`).join('')}</div></section>
<section><h2>How I did it</h2><ol class="pp__methods">${p.methods.map(m=>`<li>${m}</li>`).join('')}</ol></section>
<section><h2>${p.shotsTitle||'Dashboard'}</h2><div class="pp__shots">${p.shots.map(s=>`<figure><a href="${s.src}" target="_blank" rel="noopener"><img src="${s.src}" alt="${s.caption}" loading="lazy"></a><figcaption>${s.caption}</figcaption></figure>`).join('')}</div></section>
<nav class="pp__pager" aria-label="More projects"><a href="index.html#projects">${ic('back')}All projects</a><a href="project.html?p=${next.slug}">Next: ${next.title}${ic('next')}</a></nav>`;
}
$('#year').textContent=new Date().getFullYear();
const nav=$('#nav-links'),toggle=$('.nav__toggle');
toggle.addEventListener('click',()=>toggle.setAttribute('aria-expanded',nav.classList.toggle('open')));
