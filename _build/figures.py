"""Inline SVG figures for the statistics posts. Colours and fonts come from the page CSS (.fig ...)."""
import math
import numpy as np
from scipy import stats as st

W = 680


def f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


class Plot:
    """A plot area with linear scales inside one SVG."""

    def __init__(self, x0, y0, w, h, xmin, xmax, ymin, ymax):
        self.x0, self.y0, self.w, self.h = x0, y0, w, h
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax

    def x(self, v):
        return self.x0 + (v - self.xmin) / (self.xmax - self.xmin) * self.w

    def y(self, v):
        return self.y0 + self.h - (v - self.ymin) / (self.ymax - self.ymin) * self.h

    def path(self, xs, ys):
        return "M" + " L".join(f"{f(self.x(a))} {f(self.y(b))}" for a, b in zip(xs, ys))

    def area(self, xs, ys, base=None):
        base = self.ymin if base is None else base
        return (self.path(xs, ys) + f" L{f(self.x(xs[-1]))} {f(self.y(base))} L{f(self.x(xs[0]))} {f(self.y(base))} Z")

    def baseline(self):
        return f'<line class="axis" x1="{f(self.x0)}" x2="{f(self.x0 + self.w)}" y1="{f(self.y(self.ymin))}" y2="{f(self.y(self.ymin))}"/>'

    def xticks(self, ticks, fmt=str, dy=18):
        yb = self.y(self.ymin)
        return "".join(f'<text x="{f(self.x(t))}" y="{f(yb + dy)}" text-anchor="middle">{fmt(t)}</text>' for t in ticks)

    def ygrid(self, ticks, fmt=str):
        out = []
        for t in ticks:
            yy = self.y(t)
            if t != self.ymin:
                out.append(f'<line class="grid" x1="{f(self.x0)}" x2="{f(self.x0 + self.w)}" y1="{f(yy)}" y2="{f(yy)}"/>')
            out.append(f'<text x="{f(self.x0 - 8)}" y="{f(yy + 4)}" text-anchor="end">{fmt(t)}</text>')
        return "".join(out)

    def bar(self, xc, v, bw, cls="s1", title=None):
        """Column with a rounded data end and a square baseline."""
        yb, yt = self.y(self.ymin), self.y(v)
        x1, x2 = self.x(xc) - bw / 2, self.x(xc) + bw / 2
        r = min(4, bw / 2, max(yb - yt, 0))
        if yb - yt < 0.4:
            return ""
        d = f"M{f(x1)} {f(yb)} V{f(yt + r)} Q{f(x1)} {f(yt)} {f(x1 + r)} {f(yt)} H{f(x2 - r)} Q{f(x2)} {f(yt)} {f(x2)} {f(yt + r)} V{f(yb)} Z"
        t = f"<title>{title}</title>" if title else ""
        return f'<path class="{cls}" d="{d}">{t}</path>'


def svg(h, body, label, w=W):
    return f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{label}">{body}</svg>'


def txt(x, y, s, cls="", anchor="start"):
    c = f' class="{cls}"' if cls else ""
    a = "" if anchor == "start" else f' text-anchor="{anchor}"'
    return f'<text x="{f(x)}" y="{f(y)}"{c}{a}>{s}</text>'


def line(x1, y1, x2, y2, cls):
    return f'<line class="{cls}" x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}"/>'


def comma(v):
    return f"{v:,.0f}"


# ---------------------------------------------------------------- Part 1
DENGUE = [566, 166, 111, 143, 1036, 5956, 43854, 71976, 79598, 67769, 40716, 9288]
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def fig_dengue():
    p = Plot(74, 34, 590, 250, -0.6, 11.6, 0, 80000)
    b = [p.ygrid([0, 20000, 40000, 60000, 80000], comma), p.baseline()]
    for i, v in enumerate(DENGUE):
        b.append(p.bar(i, v, 24, title=f"{MONTHS[i]} 2023: {v:,} cases"))
        if v > 40000:
            b.append(txt(p.x(i), p.y(v) - 8, comma(v), "ann", "middle"))
    b.append(p.xticks(range(12), lambda i: MONTHS[i]))
    mean, med = np.mean(DENGUE), np.median(DENGUE)
    b.append(line(p.x0, p.y(mean), p.x0 + p.w, p.y(mean), "l2"))
    b.append(txt(p.x0 + 6, p.y(mean) - 7, f"Mean {mean:,.0f}", "ann"))
    b.append(line(p.x0, p.y(med), p.x0 + p.w, p.y(med), "l3"))
    b.append(txt(p.x0 + 6, p.y(med) - 7, f"Median {med:,.0f}", "ann"))
    b.append(f'<text transform="translate(16 {f(p.y0 + p.h / 2)}) rotate(-90)" text-anchor="middle">Hospitalised dengue cases</text>')
    return svg(316, "".join(b), "Bar chart of monthly hospitalised dengue cases in Bangladesh in 2023 with the mean and median marked")


def fig_boxplot():
    p = Plot(40, 0, 610, 150, 0, 30, 0, 1)
    yc, bh = 78, 38
    b = [line(p.x(0), 150, p.x(30), 150, "axis")]
    b += [txt(p.x(t), 168, str(t), anchor="middle") for t in range(0, 31, 5)]
    b.append(txt(p.x(15), 192, "Length of hospital stay (days)", anchor="middle"))
    b.append(line(p.x(2), yc, p.x(3), yc, "l1") + line(p.x(5), yc, p.x(6), yc, "l1"))
    b.append(line(p.x(2), yc - 10, p.x(2), yc + 10, "l1") + line(p.x(6), yc - 10, p.x(6), yc + 10, "l1"))
    b.append(f'<rect class="boxr" x="{f(p.x(3))}" y="{yc - bh / 2}" width="{f(p.x(5) - p.x(3))}" height="{bh}" rx="2"/>')
    b.append(line(p.x(3.5), yc - bh / 2, p.x(3.5), yc + bh / 2, "l1"))
    b.append(line(p.x(8), 30, p.x(8), 134, "thr"))
    b.append(txt(p.x(8) + 8, 128, "Upper fence = Q3 + 1.5 × IQR = 8"))
    b.append(f'<circle class="s2 ring" cx="{f(p.x(28))}" cy="{yc}" r="5"><title>Outlier: 28 days</title></circle>')
    b.append(txt(p.x(28), yc - 34, "Outlier: 28 days", "ann", "middle") + line(p.x(28), yc - 28, p.x(28), yc - 10, "lead"))
    # labels with leader lines
    b.append(txt(p.x(3) - 8, 22, "Q1 = 3", "ann", "end") + line(p.x(3) - 20, 28, p.x(3), yc - bh / 2 - 3, "lead"))
    b.append(txt(p.x(3.5) + 14, 22, "Median = 3.5", "ann") + line(p.x(3.5) + 26, 28, p.x(3.5) + 2, yc - bh / 2 - 3, "lead"))
    b.append(txt(p.x(2) - 4, 128, "Min = 2", "ann", "end") + line(p.x(2) - 16, 114, p.x(2) - 2, yc + 14, "lead"))
    b.append(txt(p.x(5) + 2, 128, "Q3 = 5", "ann", "middle") + line(p.x(5) + 2, 114, p.x(5), yc + bh / 2 + 3, "lead"))
    b.append(line(p.x(6) + 6, yc, p.x(8) + 14, yc, "lead") + txt(p.x(8) + 20, yc + 4, "Whisker ends at 6, the largest value inside the fence", "ann"))
    return svg(200, "".join(b), "Box plot of ten hospital stays showing the box, whiskers, upper fence and one outlier at 28 days")


def fig_shapes():
    b = []
    pw, gap, x0, hi = 200, 30, 10, 4.4
    ln = st.lognorm(0.7)
    xs = np.linspace(0, hi, 110)
    sym = st.norm(hi / 2, 0.62)
    specs = [("Symmetric", "Mean = Median", xs, sym.pdf(xs), hi / 2, hi / 2),
             ("Right-skewed (positive)", "Mean &gt; Median", xs, ln.pdf(xs), ln.mean(), ln.median()),
             ("Left-skewed (negative)", "Mean &lt; Median", hi - xs[::-1], ln.pdf(xs[::-1]), hi - ln.mean(), hi - ln.median())]
    for i, (title, rel, px, ys, m, md) in enumerate(specs):
        p = Plot(x0 + i * (pw + gap), 62, pw, 130, 0, hi, 0, ys.max() * 1.02)
        b.append(txt(p.x0, 18, title, "ttl"))
        b.append(txt(p.x0 + pw / 2, 46, rel, anchor="middle"))
        b.append(f'<path class="a1" d="{p.area(px, ys)}"/><path class="l1" d="{p.path(px, ys)}"/>')
        ym, ymd = np.interp(m, px, ys), np.interp(md, px, ys)
        b.append(line(p.x(m), p.y(ym), p.x(m), p.y(0), "l2") + line(p.x(md), p.y(ymd), p.x(md), p.y(0), "l3"))
        b.append(p.baseline())
        if i == 1:
            b.append(txt(p.x0 + pw - 4, 128, "long tail to", anchor="end") + txt(p.x0 + pw - 4, 144, "the right", anchor="end"))
        if i == 2:
            b.append(txt(p.x0 + 4, 128, "long tail to") + txt(p.x0 + 4, 144, "the left"))
    b.append(line(250, 222, 276, 222, "l2") + txt(284, 226, "Mean", "ann") + line(360, 222, 386, 222, "l3") + txt(394, 226, "Median", "ann"))
    return svg(238, "".join(b), "Three density curves: symmetric, right-skewed and left-skewed, each with its mean and median marked")


def fig_zscore():
    mu2 = -2 - st.norm.ppf(0.24)
    p = Plot(20, 40, 640, 220, -5.5, 4.5, 0, 0.42)
    xs = np.linspace(-5.5, 4.5, 140)
    left = xs[xs <= -2]
    b = [f'<path class="a2" d="{p.area(left, st.norm.pdf(left, mu2))}"/>', f'<path class="a1s" d="{p.area(left, st.norm.pdf(left))}"/>']
    b.append(f'<path class="l2" d="{p.path(xs, st.norm.pdf(xs, mu2))}"/><path class="l1" d="{p.path(xs, st.norm.pdf(xs))}"/>')
    b.append(line(p.x(-2), 30, p.x(-2), p.y(0), "mark") + txt(p.x(-2) - 8, 24, "Cut-off: z = −2", "ann", "end"))
    b.append(p.baseline() + p.xticks(range(-5, 5), lambda t: str(t).replace("-", "−")))
    b.append(txt(p.x(-0.5), 300, "Height-for-age z-score", anchor="middle"))
    b.append(txt(p.x(-5.4), 70, "A population where 24% of", "ann") + txt(p.x(-5.4), 87, "children fall below −2", "ann") + txt(p.x(-5.4), 104, "(whole curve shifted left)", "ann"))
    b.append(txt(p.x(1.25), 70, "WHO reference population", "ann") + txt(p.x(1.25), 87, "2.3% below −2", "ann"))
    return svg(308, "".join(b), "Two normal curves of height-for-age z-scores: the WHO reference population and a population shifted left so that 24% fall below minus 2")


def _scatter_data(kind, target, n=60):
    for seed in range(4000):
        rng = np.random.default_rng(seed)
        x = rng.uniform(0, 1, n)
        if kind == "curve":
            y = (x - 0.5) ** 2 * 4 + rng.normal(0, 0.07, n)
        else:
            rho = target
            z = (x - 0.5) / x.std()
            y = rho * z + math.sqrt(1 - rho ** 2) * rng.normal(0, 1, n)
        r = np.corrcoef(x, y)[0, 1]
        if round(r, 2) == target:
            return x, y, r
    raise RuntimeError(kind)


def fig_scatter():
    specs = [("Strong positive", "lin", 0.89), ("Moderate negative", "lin", -0.61), ("No relationship", "lin", 0.02), ("Curved relationship", "curve", 0.05)]
    pw, gap = 152, 20
    b = []
    for i, (title, kind, target) in enumerate(specs):
        x, y, r = _scatter_data(kind, target)
        pad = (y.max() - y.min()) * 0.06
        p = Plot(6 + i * (pw + gap), 30, pw, 140, -0.04, 1.04, y.min() - pad, y.max() + pad)
        b.append(txt(p.x0, 18, title, "ttl"))
        b.append(f'<rect class="panel" x="{p.x0}" y="{p.y0}" width="{pw}" height="{p.h}" rx="6"/>')
        b.append("".join(f'<circle class="s1 ring" cx="{f(p.x(a))}" cy="{f(p.y(c))}" r="3.2"/>' for a, c in zip(x, y)))
        b.append(txt(p.x0 + pw / 2, 192, f"r = {r:.2f}".replace("-", "−"), "ann", "middle"))
    return svg(202, "".join(b), "Four scatter plots with correlations of 0.89, minus 0.61, 0.02 and 0.05; the last is a strong curved relationship")


# ---------------------------------------------------------------- Part 2
def fig_ppv():
    p = Plot(56, 16, 560, 230, 0, 62, 0, 100)
    prev = np.linspace(0.0005, 0.62, 160)
    ppv = 0.9 * prev / (0.9 * prev + 0.05 * (1 - prev)) * 100
    npv = 0.95 * (1 - prev) / (0.95 * (1 - prev) + 0.1 * prev) * 100
    b = [p.ygrid([0, 20, 40, 60, 80, 100]), p.baseline(), p.xticks([0, 10, 20, 30, 40, 50, 60])]
    b.append(f'<path class="l2" d="{p.path(prev * 100, npv)}"/><path class="l1" d="{p.path(prev * 100, ppv)}"/>')
    for pr, dx, dy in [(1, 12, 12), (10, 12, 14), (30, 10, 18)]:
        v = 0.9 * pr / (0.9 * pr + 0.05 * (100 - pr)) * 100
        b.append(f'<circle class="s1 ring" cx="{f(p.x(pr))}" cy="{f(p.y(v))}" r="5"><title>Prevalence {pr}%: PPV {v:.1f}%</title></circle>')
        b.append(txt(p.x(pr) + dx, p.y(v) + dy, f"{v:.0f}% at {pr}% prevalence", "ann"))
    b.append(txt(p.x(62) + 8, p.y(ppv[-1]) - 2, "PPV", "ttl") + txt(p.x(62) + 8, p.y(npv[-1]) + 12, "NPV", "ttl"))
    b.append(txt(p.x(31), 290, "Prevalence of disease in the group tested (%)", anchor="middle"))
    b.append(f'<text transform="translate(14 {f(p.y0 + p.h / 2)}) rotate(-90)" text-anchor="middle">Predictive value (%)</text>')
    return svg(298, "".join(b), "Line chart of positive and negative predictive value against prevalence for a test with 90% sensitivity and 95% specificity")


def _pmf_panel(x0, pw, title, ks, ps, ymax, yticks, xt, note=None, yfmt="{:.2f}", ylabel=False, xlabel=None, bw=None):
    p = Plot(x0, 40, pw, 170, ks[0] - 0.7, ks[-1] + 0.7, 0, ymax)
    bw = bw or min(22, pw / len(ks) - 3)
    b = [txt(x0, 18, title, "ttl"), p.ygrid(yticks, lambda t: yfmt.format(t)), p.baseline()]
    b += [p.bar(k, v, bw, title=f"{k}: {v:.3f}") for k, v in zip(ks, ps)]
    b.append(p.xticks(xt))
    if note:
        b.append(txt(p.x(note[0]), p.y(note[1]) - 8, note[2], "ann", "middle"))
    if xlabel:
        b.append(txt(x0 + pw / 2, 250, xlabel, anchor="middle"))
    if ylabel:
        b.append(f'<text transform="translate({f(x0 - 46)} {f(p.y0 + p.h / 2)}) rotate(-90)" text-anchor="middle">Probability</text>')
    return "".join(b)


def fig_binomial():
    a = st.binom(10, 0.24)
    c = st.binom(50, 0.24)
    k1, k2 = list(range(11)), list(range(0, 27))
    b = _pmf_panel(60, 268, "n = 10, p = 0.24", k1, a.pmf(k1), 0.34, [0, 0.1, 0.2, 0.3], k1, (2, a.pmf(2), "most likely: 2"), ylabel=True, xlabel="Stunted children in the sample")
    b += _pmf_panel(398, 272, "n = 50, p = 0.24", k2, c.pmf(k2), 0.16, [0, 0.05, 0.10, 0.15], range(0, 27, 4), (12, c.pmf(12), "centred on np = 12"), xlabel="Stunted children in the sample")
    return svg(258, b, "Bar charts of the binomial distribution with p = 0.24 for 10 and for 50 children")


def fig_poisson():
    b = ""
    specs = [(1, range(0, 8), 0.4, [0, 0.1, 0.2, 0.3, 0.4], range(0, 8), "{:.1f}"), (3, range(0, 11), 0.25, [0, 0.05, 0.10, 0.15, 0.20, 0.25], range(0, 11, 2), "{:.2f}"), (10, range(0, 23), 0.15, [0, 0.05, 0.10, 0.15], range(0, 23, 4), "{:.2f}")]
    for i, (lam, ks, ymax, yt, xt, yf) in enumerate(specs):
        ks = list(ks)
        b += _pmf_panel(58 + i * 216, 168, f"λ = {lam}", ks, st.poisson(lam).pmf(ks), ymax, yt, xt, yfmt=yf, ylabel=(i == 0), xlabel="Number of events")
    return svg(258, b, "Bar charts of the Poisson distribution for lambda equal to 1, 3 and 10")


def fig_negbin():
    mu, k = 2.5, 0.1
    ks = list(range(13))
    po, nb = st.poisson(mu).pmf(ks), st.nbinom(k, k / (k + mu)).pmf(ks)
    p = Plot(56, 16, 604, 220, -0.6, 12.6, 0, 0.8)
    b = [p.ygrid([0, 0.2, 0.4, 0.6, 0.8], lambda t: f"{t:.1f}"), p.baseline()]
    for i in ks:
        b.append(p.bar(i - 0.2, po[i], 15, "s1", f"Poisson, {i}: {po[i]:.3f}"))
        b.append(p.bar(i + 0.2, nb[i], 15, "s2", f"Negative binomial, {i}: {nb[i]:.3f}"))
    b.append(p.xticks(ks))
    b.append(txt(p.x(0.2) + 16, p.y(nb[0]) + 6, "72% of cases infect nobody", "ann"))
    b.append(f'<rect class="s1" x="300" y="44" width="14" height="10" rx="2"/>' + txt(322, 54, "Poisson, mean 2.5 (variance 2.5)", "ann"))
    b.append(f'<rect class="s2" x="300" y="66" width="14" height="10" rx="2"/>' + txt(322, 76, "Negative binomial, mean 2.5, k = 0.1 (variance 65)", "ann"))
    b.append(txt(p.x(8.1), 146, "long tail: a few cases", "ann") + txt(p.x(8.1), 163, "infect 10 or more (7.7%)", "ann") + line(p.x(10.4), 170, p.x(11.1), p.y(0) - 6, "lead"))
    b.append(txt(p.x(6), 280, "Number of people infected by one case", anchor="middle"))
    b.append(f'<text transform="translate(14 {f(p.y0 + p.h / 2)}) rotate(-90)" text-anchor="middle">Probability</text>')
    return svg(288, "".join(b), "Grouped bar chart comparing a Poisson and a negative binomial distribution that both have a mean of 2.5")


def fig_normal_rule():
    p = Plot(20, 14, 640, 240, -3.6, 3.6, 0, 0.42)
    xs = np.linspace(-3.6, 3.6, 140)
    b = []
    for lim, cls in [(3, "b1"), (2, "b2"), (1, "b3")]:
        seg = xs[(xs >= -lim) & (xs <= lim)]
        b.append(f'<path class="{cls}" d="{p.area(seg, st.norm.pdf(seg))}"/>')
    b.append(f'<path class="l1" d="{p.path(xs, st.norm.pdf(xs))}"/>' + p.baseline())
    labels = ["μ − 3σ", "μ − 2σ", "μ − σ", "μ", "μ + σ", "μ + 2σ", "μ + 3σ"]
    b += [txt(p.x(i - 3), 276, s, anchor="middle") for i, s in enumerate(labels)]
    for lim, yv, s in [(1, 0.2, "68.3% within 1 SD"), (2, 0.105, "95.4% within 2 SD")]:
        yy = p.y(yv)
        b.append(line(p.x(-lim) + 4, yy, p.x(lim) - 4, yy, "arrow") + txt(p.x(0), yy - 8, s, "ttl", "middle"))
    yy = p.y(0.03)
    b.append(line(p.x(-3) + 4, yy, p.x(3) - 4, yy, "arrow") + txt(p.x(0), yy - 8, "99.7% within 3 SD", "ttl", "middle"))
    defs = '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="ahp" d="M0 1 L9 5 L0 9"/></marker></defs>'
    return svg(286, defs + "".join(b), "Normal curve shaded to show 68.3% of values within 1 SD, 95.4% within 2 SD and 99.7% within 3 SD")


def fig_t():
    p = Plot(20, 14, 640, 220, -4.6, 4.6, 0, 0.42)
    xs = np.linspace(-4.6, 4.6, 140)
    b = [f'<path class="l2" d="{p.path(xs, st.t.pdf(xs, 3))}"/><path class="l3" d="{p.path(xs, st.t.pdf(xs, 15))}"/><path class="l1" d="{p.path(xs, st.norm.pdf(xs))}"/>', p.baseline(), p.xticks([-4, -2, 0, 2, 4], lambda t: str(t).replace("-", "−"))]
    for i, (cls, s) in enumerate([("l1", "Normal"), ("l3", "t with 15 df"), ("l2", "t with 3 df")]):
        b.append(line(30, 28 + i * 22, 56, 28 + i * 22, cls) + txt(64, 32 + i * 22, s, "ann"))
    b.append(txt(p.x(2.6), 150, "t, 3 df: heavier tails", "ann") + line(p.x(3.3), 156, p.x(3.0), p.y(st.t.pdf(3.0, 3)) - 5, "lead"))
    return svg(262, "".join(b), "Density curves of the standard normal distribution and t distributions with 15 and 3 degrees of freedom")


# ---------------------------------------------------------------- Part 3
def fig_clt():
    rng = np.random.default_rng(11)
    shape, mean = 1.2, 7.0
    pop = lambda size: rng.gamma(shape, mean / shape, size)
    panels = [("One patient's stay", pop(40000), 0, 42, 1.0, [0, 20, 40]), ("Sample means, n = 5", pop((40000, 5)).mean(1), 0, 21, 0.5, [0, 5, 10, 15, 20]), ("Sample means, n = 30", pop((40000, 30)).mean(1), 0, 21, 0.5, [0, 5, 10, 15, 20])]
    b = []
    pw, gap = 200, 30
    for i, (title, data, lo, hi, step, xt) in enumerate(panels):
        edges = np.arange(lo, hi + step, step)
        h, _ = np.histogram(data, edges)
        p = Plot(10 + i * (pw + gap), 34, pw, 170, lo, hi, 0, h.max() * 1.02)
        b.append(txt(p.x0, 18, title, "ttl"))
        bw = max(p.x(edges[1]) - p.x(edges[0]) - 1.2, 1.5)
        b += [p.bar(e + step / 2, v, bw) for e, v in zip(edges[:-1], h)]
        b.append(line(p.x(mean), p.y0, p.x(mean), p.y(0), "l2"))
        b.append(p.baseline() + p.xticks(xt) + txt(p.x0 + pw / 2, 246, "Days", anchor="middle"))
        if i == 0:
            b.append(txt(p.x(mean) + 8, 62, "population", "ann") + txt(p.x(mean) + 8, 79, "mean 7.0", "ann"))
    return svg(254, "".join(b), "Three histograms: individual hospital stays, means of samples of 5 and means of samples of 30, with the population mean marked")


def _ci_sim():
    for seed in range(200):
        rng = np.random.default_rng(seed)
        ph = rng.binomial(400, 0.24, 40) / 400
        se = np.sqrt(ph * (1 - ph) / 400)
        lo, hi = ph - 1.96 * se, ph + 1.96 * se
        miss = (lo > 0.24) | (hi < 0.24)
        if miss.sum() == 2 and miss[:4].sum() == 0:
            return ph, lo, hi, miss
    raise RuntimeError


def fig_ci():
    ph, lo, hi, miss = _ci_sim()
    p = Plot(64, 40, 560, 220, 0, 41, 14, 36)
    b = [p.ygrid([15, 20, 25, 30, 35], lambda t: f"{t}"), p.baseline(), p.xticks([1, 10, 20, 30, 40])]
    b.append(line(p.x0, p.y(24), p.x0 + p.w, p.y(24), "mark") + txt(p.x0 + p.w + 6, p.y(24) - 2, "True", "ann") + txt(p.x0 + p.w + 6, p.y(24) + 14, "24%", "ann"))
    for i in range(40):
        cls = "2" if miss[i] else "1"
        xx = p.x(i + 1)
        b.append(line(xx, p.y(lo[i] * 100), xx, p.y(hi[i] * 100), f"l{cls}"))
        b.append(f'<circle class="s{cls} ring" cx="{f(xx)}" cy="{f(p.y(ph[i] * 100))}" r="3.4"><title>Survey {i + 1}: {ph[i] * 100:.1f}% ({lo[i] * 100:.1f}% to {hi[i] * 100:.1f}%)</title></circle>')
    b.append(line(70, 14, 96, 14, "l1") + f'<circle class="s1 ring" cx="83" cy="14" r="3.4"/>' + txt(104, 18, "Interval contains the true value", "ann"))
    b.append(line(340, 14, 366, 14, "l2") + f'<circle class="s2 ring" cx="353" cy="14" r="3.4"/>' + txt(374, 18, f"Interval misses it ({int(miss.sum())} of 40)", "ann"))
    b.append(txt(p.x0 + p.w / 2, 302, "40 random samples of 400 children, each with its own 95% confidence interval", anchor="middle"))
    b.append(f'<text transform="translate(16 {f(p.y0 + p.h / 2)}) rotate(-90)" text-anchor="middle">Estimated stunting (%)</text>')
    return svg(310, "".join(b), "Forty simulated survey estimates with 95% confidence intervals; most contain the true value of 24% and two miss it"), int(miss.sum())


def fig_pvalue():
    p = Plot(20, 36, 640, 210, -4.2, 4.2, 0, 0.42)
    xs = np.linspace(-4.2, 4.2, 140)
    d = st.t(78)
    tv = 2.16
    b = []
    for seg in (xs[xs <= -tv], xs[xs >= tv]):
        b.append(f'<path class="s2" d="{p.area(seg, d.pdf(seg))}"/>')
    b.append(f'<path class="l1" d="{p.path(xs, d.pdf(xs))}"/>' + p.baseline() + p.xticks(range(-4, 5), lambda t: str(t).replace("-", "−")))
    b.append(line(p.x(-tv), p.y(0.2), p.x(-tv), p.y(0), "mark") + line(p.x(tv), p.y(0.2), p.x(tv), p.y(0), "mark"))
    b.append(txt(p.x(-tv) - 6, p.y(0.2) + 4, "−2.16", "ann", "end") + txt(p.x(tv) + 6, p.y(0.2) + 4, "Observed t = 2.16", "ann"))
    b.append(txt(p.x(-2.6), p.y(0.045), "area 0.017", "ann", "end") + txt(p.x(2.6), p.y(0.045), "area 0.017", "ann"))
    b.append(txt(p.x(0), p.y(0.2), "Results we would", anchor="middle") + txt(p.x(0), p.y(0.2) + 17, "expect if the null", anchor="middle") + txt(p.x(0), p.y(0.2) + 34, "hypothesis were true", anchor="middle"))
    b.append(txt(p.x(0), 20, "p-value = both shaded tails = 0.034", "ttl", "middle") + txt(p.x(0), 288, "Test statistic", anchor="middle"))
    return svg(296, "".join(b), "A t distribution with both tails beyond plus and minus 2.16 shaded; the two tails together are the p-value of 0.034")


def fig_power():
    crit, delta = 1.96, 2.8
    p = Plot(20, 44, 640, 200, -3.6, 6.4, 0, 0.42)
    xs = np.linspace(-3.6, 6.4, 160)
    l, r = xs[xs <= crit], xs[xs >= crit]
    b = [f'<path class="a2s" d="{p.area(l, st.norm.pdf(l, delta))}"/>', f'<path class="a2" d="{p.area(r, st.norm.pdf(r, delta))}"/>', f'<path class="s1" d="{p.area(r, st.norm.pdf(r))}"/>']
    b.append(f'<path class="l1" d="{p.path(xs, st.norm.pdf(xs))}"/><path class="l2" d="{p.path(xs, st.norm.pdf(xs, delta))}"/>' + p.baseline())
    b.append(line(p.x(crit), 26, p.x(crit), p.y(0), "mark") + txt(p.x(crit) + 6, 20, "Critical value: reject H₀ to the right", "ann"))
    b.append(txt(p.x(-1.2), 64, "If H₀ is true", "ttl", "end") + txt(p.x(4.0), 64, "If H₁ is true", "ttl"))
    b.append(txt(p.x(3.0), p.y(0.2), "Power = 1 − β", "ann", "middle") + txt(p.x(3.0), p.y(0.2) + 17, "(effect detected)", "ann", "middle"))
    b.append(txt(p.x(-3.5), 122, "β: Type II error", "ann") + txt(p.x(-3.5), 139, "(real effect missed)", "ann") + line(p.x(-1.3), 140, p.x(1.35), p.y(0.06), "lead"))
    b.append(txt(p.x(4.7), 172, "α: Type I error", "ann") + txt(p.x(4.7), 189, "(false alarm)", "ann") + line(p.x(4.6), 180, p.x(2.25), p.y(0.012), "lead"))
    b.append(txt(p.x(1.4), 268, "Value of the test statistic", anchor="middle"))
    return svg(276, "".join(b), "Two overlapping curves for the null and alternative hypotheses with the critical value, showing alpha, beta and power as areas")


FIGS = {"dengue": fig_dengue, "boxplot": fig_boxplot, "shapes": fig_shapes, "zscore": fig_zscore, "scatter": fig_scatter, "ppv": fig_ppv, "binomial": fig_binomial, "poisson": fig_poisson, "negbin": fig_negbin, "normal": fig_normal_rule, "t": fig_t, "clt": fig_clt, "ci": lambda: fig_ci()[0], "pvalue": fig_pvalue, "power": fig_power}

if __name__ == "__main__":
    for k, fn in FIGS.items():
        print(k, len(fn()))
    print("CI misses:", fig_ci()[1])
