# brawl

**The economics horse-race — whose doctrine was right, by the P&L?**

Worldview is the deepest axis: it's the prior on whether alpha exists at all. Each school prescribes a
book; run them on the same real data and let the P&L adjudicate. A capstone built on **doctrine**, not
client mandate — the fifth archetype capstone. Liquid proxies, all 2016+, same window for fairness.

## Verdict

**No doctrine wins outright — the winner depends on the objective *and* the decade, which is itself the
lesson.** On raw return, equity wins and Behavioral ≈ Chicago (factors are beta). On risk-adjusted
return, **Austrian/Hayek wins** — but only because gold had a great decade and 2020/2025 rewarded its
convex tail. Keynesian's duration bet was crushed by 2022. The race crowns whoever's asset had the
decade; the only regime-robust statement is **"behavioral = beta."**

| school / book | Sharpe | CAGR | maxDD | worst mo | skew | Calmar |
|---|---|---|---|---|---|---|
| **Austrian / Hayek** (gold + equity + tail) | **+1.16** | +9.7% | **−14%** | −5.6% | −0.05 | **+0.67** |
| MMT (TIP + commodities + equity) | +0.99 | +9.0% | −21% | −9.3% | −0.81 | +0.42 |
| Chicago / EMH (own the index) | +0.88 | **+15.0%** | −34% | −12.6% | −0.35 | +0.44 |
| Behavioral (MTUM/QUAL/VLUE) | +0.85 | **+15.3%** | −35% | −12.8% | −0.19 | +0.44 |
| Libertarian (gold only) | +0.83 | +12.9% | −26% | −11.7% | −0.52 | +0.49 |
| Keynesian (duration-heavy) | +0.79 | +6.5% | −24% | −7.4% | −0.28 | +0.27 |
| Monetarism (rate-regime rules) | +0.70 | +8.9% | −34% | −12.6% | −0.40 | +0.26 |

*Winners: by return → Behavioral · by Sharpe → Austrian · by Calmar → Austrian. 2016-01 … 2026-07 (10.5y).*

## What actually happened

- **Behavioral ≈ Chicago on return (+15.3% vs +15.0%)** — the clearest robust finding: the "markets are
  inefficient, exploit biases" book delivered the *same* return as just owning the index, with the *same*
  −35% drawdown. Behavioral alpha was beta. The family's whole corpus said this; here it is in one row.
- **Austrian won risk-adjusted — for a regime-specific reason.** 40% gold + a 10% long-vol tail gave it
  crisis convexity (COVID **+3.4%**, tariffs **+4.0%**) and half the drawdown. But that win rode gold's
  strong 2016–2026 and two convexity-rewarding crashes; in the 2011–15 gold bear this book is a dog.
- **Keynesian lost.** "Lean on the backstop" (duration-heavy) returned +6.5% and took −7.4% in the 2022
  rate shock — the backstop *was* the risk that year.
- **Monetarism's rule earned its narrow keep in the bad months** (inflation −0.6%, rate shock −1.2% — the
  best of any book) but lagged badly the rest of the time (+0.70 Sharpe). Rules dodge, at a cost.

## The crisis grid (the tell)

| school | COVID 2020-03 | inflation 2022-06 | rate shock 2022-09 | tariffs 2025-04 |
|---|---|---|---|---|
| Chicago / EMH | −12.6% | −8.2% | −9.2% | −0.9% |
| Austrian / Hayek | **+3.4%** | −2.9% | −4.2% | **+4.0%** |
| Keynesian | −1.3% | −3.9% | −7.4% | −0.1% |
| Libertarian (gold) | −0.1% | −1.6% | −2.9% | **+5.4%** |
| Monetarism (rules) | −12.6% | **−0.6%** | **−1.2%** | −4.9% |

The hard-money / fragility books are green when the index bleeds — which is exactly why Austrian topped
the risk-adjusted table, and exactly why that's a statement about *this decade's crises*, not about who's
right.

## The honest meta-point

A doctrine horse-race crowns whoever's asset class had the decade. Gold's run made Austrians look
prescient; 2022 made Keynesians look foolish; the bull made the index hard to beat on return. Change the
sample and you change the winner — which is the real finding: **worldview is regime-dependence wearing a
philosophy.** The one thing that survived regardless was that the behavioral book was market beta.

## `brawl_2`

The only fair trial is **multiple regimes** — Massive's 2003+ history across 2008, and critically the
**2011–2015 gold bear** that would gut the Austrian/Libertarian books. Until then, read the risk-adjusted
"winner" as this decade's, not a verdict on economics.

## Reproduce

```bash
export ALPACA_KEY_ID=... ALPACA_SECRET_KEY=...
python3 research/brawl_1.py
```

---

*Blaque Baux — a Carter Warrens research initiative. Research only; not investment advice. The P&L is the
only economist that doesn't argue — but it only speaks for the decade it was given.*
