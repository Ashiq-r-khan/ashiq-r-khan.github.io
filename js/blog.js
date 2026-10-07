const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)],ic=n=>`<svg class="icon"><use href="#i-${n}"/></svg>`,small=matchMedia('(max-width:900px)');
$('#year').textContent=new Date().getFullYear();
const nav=$('#nav-links'),toggle=$('.nav__toggle'),list=$('#blog-list'),art=$('.art');
toggle.addEventListener('click',()=>toggle.setAttribute('aria-expanded',nav.classList.toggle('open')));
if(list)list.innerHTML=[...new Set(POSTS.map(p=>p.series||''))].map(n=>{const s=SERIES[n]||{};return `<section class="series"><div class="series__head"><div><h2>${n||'More posts'}</h2>${s.text?`<p>${s.text}</p>`:''}</div>${s.pdf?`<a class="btn btn--outline" href="../${s.pdf}">${ic('file')}Full notes as PDF</a>`:''}</div><div class="posts">${POSTS.filter(p=>(p.series||'')===n).map(p=>postCard(p,'../')).join('')}</div></section>`}).join('');
if(art){
  renderMathInElement($('.body'),{delimiters:[{left:'\\[',right:'\\]',display:true},{left:'\\(',right:'\\)',display:false}],throwOnError:false});
  const hs=$$('.body h2'),toc=$('.toc');
  $('#toc').innerHTML=hs.map(h=>`<a href="#${h.id}">${h.textContent}</a>`).join('');
  const links=$$('#toc a'),mark=()=>{let c=hs[0];hs.forEach(h=>{if(h.getBoundingClientRect().top<=120)c=h});links.forEach(a=>a.toggleAttribute('aria-current',a.hash==='#'+c.id))};
  toc.open=!small.matches;
  links.forEach(a=>a.addEventListener('click',()=>{if(small.matches)toc.open=false}));
  addEventListener('scroll',mark,{passive:true});mark();
  const me=POSTS.find(p=>p.slug===art.dataset.slug),s=POSTS.filter(p=>p.series===me.series),k=s.indexOf(me),prev=s[k-1],next=s[k+1],pdf=(SERIES[me.series]||{}).pdf;
  $('#pager').innerHTML=`<a href="${prev?prev.slug+'.html':'index.html'}">${ic('back')}${prev?`Part ${prev.part}: ${prev.title}`:'All posts'}</a>${pdf?`<a href="../${pdf}">${ic('file')}Full notes as PDF</a>`:''}<a href="${next?next.slug+'.html':'index.html'}">${next?`Part ${next.part}: ${next.title}`:'All posts'}${ic('next')}</a>`;
}
