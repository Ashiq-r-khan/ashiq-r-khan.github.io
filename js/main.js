const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)],gh=r=>`https://github.com/Ashiq-r-khan/${r}`,mail=SITE.email.join('@');
$('#project-list').innerHTML=PROJECTS.map(p=>`<article class="card project"><a href="project.html?p=${p.slug}" tabindex="-1" aria-hidden="true"><img src="${p.image}" alt="" loading="lazy" width="1200" height="675"></a><h3><a href="project.html?p=${p.slug}">${p.title}</a></h3><p class="project__summary">${p.summary}</p><p class="project__result">${p.result}</p><p class="project__foot"><a href="project.html?p=${p.slug}">View details</a><a href="${gh(p.repo)}"><svg class="icon"><use href="#i-github"/></svg>GitHub</a></p></article>`).join('');
if(POSTS.length){$('#post-list').innerHTML=POSTS.map(p=>`<article class="card post"><time>${p.date}</time><h3>${p.title}</h3><p>${p.excerpt}</p><a href="${p.url}">Read on LinkedIn</a></article>`).join('');$('#blog').hidden=false;$('nav a[href="#blog"]').hidden=false}
$$('.js-mail').forEach(a=>a.href=`mailto:${mail}`);
$('.js-mail-text').textContent=mail;
$('#year').textContent=new Date().getFullYear();
const nav=$('#nav-links'),toggle=$('.nav__toggle'),links=$$('#nav-links a');
toggle.addEventListener('click',()=>toggle.setAttribute('aria-expanded',nav.classList.toggle('open')));
links.forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');toggle.setAttribute('aria-expanded',false)}));
const spy=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)links.forEach(a=>a.getAttribute('href')==='#'+e.target.id?a.setAttribute('aria-current','true'):a.removeAttribute('aria-current'))}),{rootMargin:'-45% 0px -50% 0px'});
$$('main section').forEach(s=>spy.observe(s));
const form=$('#contact-form'),status=$('#form-status'),say=(t,c='')=>{status.textContent=t;status.className=c};
form.addEventListener('submit',async e=>{
  e.preventDefault();
  const d=Object.fromEntries(new FormData(form));
  if(d.botcheck)return;
  if(!SITE.web3formsKey){location.href=`mailto:${mail}?subject=${encodeURIComponent('Portfolio message from '+d.name)}&body=${encodeURIComponent(d.message+'\n\n'+d.name+'\n'+d.email)}`;return say('Your email app should open with the message filled in.')}
  const btn=form.querySelector('button');
  btn.disabled=true;say('Sending message…');
  try{
    const r=await fetch('https://api.web3forms.com/submit',{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify({access_key:SITE.web3formsKey,subject:`Portfolio message from ${d.name}`,from_name:'Portfolio website',name:d.name,email:d.email,message:d.message})});
    if(!(await r.json()).success)throw 0;
    form.reset();say('Message sent. I will reply to your email.','ok');
  }catch{say(`The message did not send. Email me at ${mail} instead.`,'err')}
  btn.disabled=false;
});
