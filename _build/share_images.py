"""Draw the 1200 x 630 share-preview images in assets/blog/. Needs Playwright with Chromium. Run: python3 _build/share_images.py"""
import asyncio, math
import numpy as np
from scipy import stats as st
from playwright.async_api import async_playwright
from pathlib import Path
SITE=str(Path(__file__).resolve().parent.parent)
def bars():
    d=[566,166,111,143,1036,5956,43854,71976,79598,67769,40716,9288]; m=max(d); out=""
    for i,v in enumerate(d):
        h=max(v/m*300,3); out+=f'<rect x="{i*36}" y="{300-h:.1f}" width="22" height="{h:.1f}" rx="4" fill="#1fa8ab"/>'
    return f'<svg width="430" height="300" viewBox="0 0 430 300">{out}<line x1="0" x2="420" y1="{300-26765/m*300:.1f}" y2="{300-26765/m*300:.1f}" stroke="#d95926" stroke-width="3"/></svg>'
def bell():
    xs=np.linspace(-3.4,3.4,120); ys=st.norm.pdf(xs)
    pt=lambda x,y:f"{(x+3.4)/6.8*430:.1f} {300-y/0.4*290:.1f}"
    path="M"+" L".join(pt(x,y) for x,y in zip(xs,ys))
    seg=xs[(xs>=-1)&(xs<=1)]; area="M"+" L".join(pt(x,st.norm.pdf(x)) for x in seg)+f" L{pt(1,0)} L{pt(-1,0)} Z"
    return f'<svg width="430" height="300" viewBox="0 0 430 300"><path d="{area}" fill="#1fa8ab" fill-opacity=".3"/><path d="{path}" fill="none" stroke="#1fa8ab" stroke-width="4" stroke-linecap="round"/><line x1="0" x2="430" y1="300" y2="300" stroke="#33465e" stroke-width="2"/></svg>'
def cis():
    rng=np.random.default_rng(5); ph=rng.binomial(400,.24,14)/400; se=np.sqrt(ph*(1-ph)/400); out=""
    y=lambda v:300-(v-0.15)/0.18*300
    for i,(p,s) in enumerate(zip(ph,se)):
        miss=(p-1.96*s>.24) or (p+1.96*s<.24); c="#d95926" if miss else "#1fa8ab"; x=14+i*31
        out+=f'<line x1="{x}" x2="{x}" y1="{y(p-1.96*s):.1f}" y2="{y(p+1.96*s):.1f}" stroke="{c}" stroke-width="4" stroke-linecap="round"/><circle cx="{x}" cy="{y(p):.1f}" r="7" fill="{c}" stroke="#0f1722" stroke-width="3"/>'
    return f'<svg width="430" height="300" viewBox="0 0 430 300"><line x1="0" x2="430" y1="{y(.24):.1f}" y2="{y(.24):.1f}" stroke="#e8eef5" stroke-width="2"/>{out}</svg>'
def gap():
    import sys; sys.path.insert(0,str(Path(__file__).resolve().parent)); from figures import NAT23, PUB23
    nat,pub=NAT23[17:],PUB23[17:]; x=lambda i:i/(len(nat)-1)*430; y=lambda v:300-v/21000*290
    top=" L".join(f"{x(i):.1f} {y(v):.1f}" for i,v in enumerate(nat)); bot=" L".join(f"{x(i):.1f} {y(v):.1f}" for i,v in reversed(list(enumerate(pub))))
    return f'<svg width="430" height="300" viewBox="0 0 430 300"><path d="M{top} L{bot} Z" fill="#d95926" fill-opacity=".22"/><path d="M{" L".join(f"{x(i):.1f} {y(v):.1f}" for i,v in enumerate(pub))}" fill="none" stroke="#d95926" stroke-width="4" stroke-linejoin="round"/><path d="M{top}" fill="none" stroke="#1fa8ab" stroke-width="4" stroke-linejoin="round"/><line x1="0" x2="430" y1="300" y2="300" stroke="#33465e" stroke-width="2"/></svg>'
CARDS=[("dengue-missing-admissions","From my projects","105,000 dengue admissions were missing from the 2023 division data",gap()),("descriptive-statistics","Statistics for Public Health · Part 1","Descriptive statistics for public health",bars()),
       ("probability-and-distributions","Statistics for Public Health · Part 2","Probability and distributions for public health",bell()),
       ("inferential-statistics","Statistics for Public Health · Part 3","Inferential statistics for public health",cis()),
       ("blog","Blog","Study notes on statistics for public health data",bell())]
TPL='''<!doctype html><meta charset="utf-8"><style>
@font-face{{font-family:Geologica;font-weight:300;src:url(assets/fonts/geologica-latin-300-normal.woff2)}}
@font-face{{font-family:Geologica;font-weight:400;src:url(assets/fonts/geologica-latin-400-normal.woff2)}}
@font-face{{font-family:"JetBrains Mono";font-weight:400;src:url(assets/fonts/jetbrains-mono-latin-400-normal.woff2)}}
body{{margin:0;width:1200px;height:630px;background:#0f1722;color:#e8eef5;font-family:Geologica;display:grid;grid-template-columns:1fr 430px;gap:56px;padding:72px 80px;box-sizing:border-box;align-items:center}}
.l{{display:flex;flex-direction:column;height:100%}}
.s{{font:400 22px "JetBrains Mono";color:#4cc2c4}}
h1{{font-weight:400;font-size:62px;line-height:1.08;letter-spacing:-.02em;margin:28px 0 0}}
.f{{margin-top:auto;font:300 24px Geologica;color:#a3b3c5}}.f b{{font:400 22px "JetBrains Mono";color:#e8eef5;margin-right:18px}}
</style><div class="l"><div class="s">{series}</div><h1>{title}</h1><div class="f"><b>ASHIQ.KHAN</b>Md. Ashiqur Rahman Khan</div></div><div>{art}</div>'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1200,"height":630})
        for slug,series,title,art in CARDS:
            open(f"{SITE}/_og.html","w").write(TPL.format(series=series,title=title,art=art))
            await pg.goto(f"file://{SITE}/_og.html?{slug}",wait_until="networkidle"); await pg.wait_for_timeout(200)
            await pg.screenshot(path=f"{SITE}/assets/blog/{slug}.jpg",type="jpeg",quality=88)
        await b.close()
    import os; os.remove(f"{SITE}/_og.html")
asyncio.run(main())
