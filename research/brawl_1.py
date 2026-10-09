#!/usr/bin/python3
# =============================================================================
# brawl_1.py — the economics horse-race: whose doctrine was right, by the P&L?
#
# Worldview is the deepest axis — it's the prior on whether alpha exists at all. Each school prescribes
# a book; run them on the same real data and let the P&L adjudicate. A capstone built on DOCTRINE, not
# client mandate. Books (liquid proxies, all 2016+, same window for fairness):
#   Chicago/EMH   — own the index                         (SPY)
#   Monetarism    — rules over discretion, rate-regime    (SPY when rates falling, else short T-bills)
#   Keynesian     — lean on the backstop, duration-heavy  (40 SPY / 60 govt bonds)
#   Austrian      — sound money + fragility hedge          (40 GLD / 30 SPY / 20 IEF / 10 long-vol)
#   Behavioral    — biases → factor premia                 (50 MTUM / 30 QUAL / 20 VLUE)
#   Libertarian   — hard money, gold only (Ron Paul)       (GLD)
#   MMT           — inflation is the only limit, real assets(40 TIP / 30 DBC / 30 SPY)
# =============================================================================
import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from _brawl_common import panel, rets

def metrics(r, months):
    r = np.asarray(r, float); c = np.cumprod(1+r); dd = (c/np.maximum.accumulate(c)-1).min()
    sh = r.mean()/r.std()*math.sqrt(252) if r.std()>0 else float("nan"); z=(r-r.mean())/r.std()
    cagr = c[-1]**(252/len(r))-1
    mo = {}
    for m,x in zip(months,r): mo[m]=mo.get(m,1.0)*(1+x)
    worst = min(v-1 for v in mo.values())
    return dict(sh=sh, cagr=cagr, dd=float(dd), skew=float(np.mean(z**3)), worst=worst,
                calmar=cagr/abs(dd) if dd<0 else float("nan"))

def main():
    syms = ["SPY","IEF","TLT","SHY","GLD","VIXM","MTUM","QUAL","VLUE","TIP","DBC"]
    P, dates = panel(syms); R = {s: rets(P[s]) for s in P}
    L = min(len(R[s]) for s in R); months=[d[:7] for d in dates[1:]][-L:]
    r = {s: R[s][-L:] for s in R}
    # monetarism: rate-regime rule (causal) — SPY when TLT 63d trend up (rates falling), else SHY
    tltpx = np.cumprod(1+r["TLT"]); up = np.array([tltpx[i] > tltpx[max(0,i-63)] for i in range(L)])
    sig = np.zeros(L); sig[1:] = up[:-1]                      # act on yesterday's regime
    monet = sig*r["SPY"] + (1-sig)*r["SHY"]

    books = {
        "Chicago / EMH":      r["SPY"],
        "Monetarism (rules)": monet,
        "Keynesian":          0.40*r["SPY"] + 0.35*r["IEF"] + 0.25*r["TLT"],
        "Austrian / Hayek":   0.40*r["GLD"] + 0.30*r["SPY"] + 0.20*r["IEF"] + 0.10*r["VIXM"],
        "Behavioral":         0.50*r["MTUM"] + 0.30*r["QUAL"] + 0.20*r["VLUE"],
        "Libertarian (gold)": r["GLD"],
        "MMT (real assets)":  0.40*r["TIP"] + 0.30*r["DBC"] + 0.30*r["SPY"],
    }
    print("="*96); print("BRAWL — the economics horse-race: whose doctrine was right, by the P&L?"); print("="*96)
    print(f"  window {dates[-L]}..{dates[-1]}  ({L/252:.1f}y)")
    M = {k: metrics(v, months) for k, v in books.items()}
    print(f"\n  {'school / book':22}{'Sharpe':>8}{'CAGR':>8}{'maxDD':>8}{'worstMo':>9}{'skew':>7}{'Calmar':>8}")
    for k in sorted(M, key=lambda x: -M[x]["sh"]):
        m = M[k]; print(f"  {k:22}{m['sh']:>+8.2f}{m['cagr']*100:>+7.1f}%{m['dd']*100:>+7.0f}%{m['worst']*100:>+8.1f}%{m['skew']:>+7.2f}{m['calmar']:>+8.2f}")

    # winners
    byret = max(M, key=lambda x: M[x]["cagr"]); bysh = max(M, key=lambda x: M[x]["sh"]); bycal = max(M, key=lambda x: M[x]["calmar"])
    print(f"\n  WINNERS:  by return → {byret}   |   by Sharpe → {bysh}   |   by Calmar → {bycal}")

    # crisis behavior
    print("\n  CRISIS MONTHS (book return)")
    tests = [("2020-03","COVID"),("2022-06","inflation"),("2022-09","rate shock"),("2025-04","tariffs")]
    print(f"    {'school':22}" + "".join(f"{lbl:>12}" for _,lbl in tests))
    for k,v in books.items():
        row=""
        for mm,_ in tests:
            idx=[i for i,m in enumerate(months) if m==mm]
            row += f"{(np.prod([1+v[i] for i in idx])-1)*100 if idx else float('nan'):>+11.1f}%"
        print(f"    {k:22}{row}")

    print("\n  READ: no doctrine wins outright — it depends on the objective, and on the DECADE. On raw")
    print("  return, equity wins and Behavioral ≈ Chicago (factors are beta). On risk-adjusted (Sharpe/")
    print("  Calmar), AUSTRIAN wins — but only because gold had a great decade and 2020/2025 rewarded its")
    print("  convex tail; Keynesian's duration bet was crushed by 2022. The race crowns whoever's asset")
    print("  had the decade — which is itself the lesson: regime-dependence, not a right worldview. The")
    print("  only robust call is 'behavioral = beta.' CAVEAT: one regime; the fair trial is multiple")
    print("  cycles (Massive 2003+ across 2008, the 2011-15 gold bear) — brawl_2.")

if __name__ == "__main__":
    main()
