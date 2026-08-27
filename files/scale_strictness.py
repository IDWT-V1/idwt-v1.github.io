#!/usr/bin/env python3
"""Sector-scale strictness: the narrow, checkable claim.

This script tests one thing, and deliberately not the framework around it:

    Within a sector d, ONE mass scale reproduces EVERY particle assigned to
    that sector, with residuals far smaller than the spacing between adjacent
    rungs of the combinatorial ladder S(n,d) = C(n+d-1, d).

That conjunction is what a scale cannot fake. A scale multiplies every mass in
its sector by the same factor, so it slides them together; and the rungs are
2%-75% apart, so there is nowhere nearby to slide onto. A sector holding two or
three particles therefore imposes one or two constraints that the single scale
had no freedom to satisfy.

The script reports four things, in order, and the last two are the ones that
can go against the claim:

    A. what scale each particle demands, and how tightly the particles of a
       sector agree on it
    B. how far apart the rungs are, which is what makes A hard to arrange
    C. an exhaustive search: how many OTHER index assignments would have fitted
       as well -- the look-elsewhere factor that a per-quantity significance
       calculation leaves out
    D. an honest ledger naming the sectors where the claim holds unaided and
       the sectors where it needs a correction

The claim under test is about the structure of the fit rather than its
precision: whether one scale per sector can carry several masses at once, not
whether any individual ratio matches to within its measurement error. Those are
separate questions and this script answers only the first.

No dependencies beyond the standard library. Deterministic: no sampling, no
seeds -- section C searches its space exhaustively rather than estimating it.

Every quantity is referenced by NAME rather than by a step number, so inserting
or removing a section here cannot silently invalidate a citation elsewhere.
"""

from math import comb, sqrt

# ---------------------------------------------------------------------------
# The combinatorial ladder
# ---------------------------------------------------------------------------

def S(n, d):
    """The simplex number: cumulative count of oscillator states below level n.

    S(n,d) = C(n+d-1, d), the number of monomials of degree < n in d variables.
    The ladder is steep -- adjacent rungs differ by a large fraction -- which is
    the whole reason a scale cannot tune a mass onto one.
    """
    return comb(n + d - 1, d)


def rung_gap(n, d):
    """Fractional distance from rung n to whichever neighbour is closer.

    This is the target a scale would have to hit by accident. A residual well
    inside this gap is a coincidence; a residual comparable to it is not
    evidence of anything.
    """
    here = S(n, d)
    up = S(n + 1, d) / here - 1.0
    down = 1.0 - S(n - 1, d) / here if n > 1 else float('inf')

    return min(up, down)


# ---------------------------------------------------------------------------
# Measured input
#
# PDG 2024 / CODATA. The uncertainty is carried alongside every value because
# section D needs it: a percentage residual means nothing without knowing how
# well the quantity is actually measured, and these span five orders of
# magnitude in relative precision.
# ---------------------------------------------------------------------------

M_E = 0.51099895000          # MeV, the single dimensional anchor
M_E_SIGMA = 0.00000000015

MEASURED = {
    #  name        MeV          1-sigma      sector  mode index
    'e':        (0.51099895000, 1.5e-10,        6,     13),
    'mu':       (105.6583755,   2.3e-6,         6,     35),
    'tau':      (1776.86,       0.12,          10,     23),
    'W':        (80369.2,       13.3,           2,     76),
    'Z':        (91188.0,       2.0,            2,     81),
    'H':        (125200.0,      110.0,          2,     95),
    'd':        (4.70,          0.07,           3,      1),
    's':        (93.5,          0.8,            3,      4),
    'u':        (2.16,          0.07,           4,      3),
    'c':        (1273.0,        4.6,            4,     20),
    't':        (172570.0,      290.0,          4,     72),
}

# The tau carries a derived multiplicative back-reaction from the d=6 -> d=10
# coupling; it is the only lepton that does. Reported both ways in section A,
# because a correction applied to exactly the particle that needed one is worth
# seeing isolated rather than folded in silently.
TAU_BACKREACTION = 1.0 + 1.0 / 1680.0


# ---------------------------------------------------------------------------
# Sector scales, derived from the seeds and m_e alone
# ---------------------------------------------------------------------------

N_DOWN, N_UP = 1, 3
N_S = N_DOWN + N_UP                       # 4
N_E = 13                                  # electron mode index, anchors d=6


def couplings():
    """The six sector self-couplings, from the seeds only.

    g_22 is the one built from Dirac multiplicities rather than directly from
    the seeds: alpha is the S^3 multiplicity at the seed level less the up-type
    states, beta the d=4 eigenstate increment at the up threshold.
    """
    alpha = S(N_S, 3) - N_UP               # 20 - 3
    beta = S(N_UP, 4) - S(N_UP, 3)         # 15 - 10

    g33 = N_S ** 2 * sqrt(N_S + N_UP) / 2  # 8*sqrt(7)
    g44 = N_S * N_UP / sqrt(N_S + N_UP)    # 12/sqrt(7)
    g66 = 1.0 / N_S                        # 1/4
    g22 = alpha ** 2 * beta / 2            # 722.5

    return {
        2: g22,
        3: g33,
        4: g44,
        5: 96.0 / g22,                     # Hopf universality
        6: g66,
        10: g66,                           # d=10 shares the d=6 coupling
    }


def sector_scales():
    """Derived mass scale per sector, in MeV.

    d=6 is the anchor: m_e divided by its own rung. Everything else is a
    coupling ratio away. d=10 shares g_66, so its scale equals the d=6 scale --
    which is a prediction, not a fit, and section A tests it against the tau.
    """
    g = couplings()

    m6 = M_E / S(N_E, 6)
    m3 = M_E * sqrt(g[3] / g[6])
    m4 = m3 * sqrt(g[4] / g[3]) / S(N_UP, 4)
    m2 = M_E * sqrt(g[2] / g[6])

    return {2: m2, 3: m3, 4: m4, 6: m6, 10: m6}


# ---------------------------------------------------------------------------
# A. What scale does each particle demand?
# ---------------------------------------------------------------------------

def demanded_scale(name):
    """The scale that would reproduce this particle's measured mass exactly."""
    mass, _, d, n = MEASURED[name]

    if name == 'tau':
        mass = mass / TAU_BACKREACTION

    return mass / S(n, d)


def report_scales():
    print("=" * 74)
    print("A. SCALE DEMANDED BY EACH PARTICLE vs THE ONE SECTOR SCALE")
    print("=" * 74)
    print("   A sector's particles must all agree on one number. They had no")
    print("   freedom to: the scale was fixed before the second particle was")
    print("   placed.\n")

    derived = sector_scales()
    by_sector = {}

    for name, (_, _, d, _) in MEASURED.items():
        by_sector.setdefault(d, []).append(name)

    spreads = {}

    for d in sorted(by_sector):
        print(f"  d={d}   derived scale = {derived[d]:.6e} MeV")
        wanted = []

        for name in by_sector[d]:
            want = demanded_scale(name)
            wanted.append(want)
            note = "  (after back-reaction)" if name == 'tau' else ""
            print(f"     {name:4s} demands {want:.6e}"
                  f"   {(want / derived[d] - 1) * 100:+8.4f}% from derived{note}")

        # Spread across the sector: the sector's own internal disagreement,
        # independent of whether the derived value sits in the middle of it.
        spread = max(wanted) / min(wanted) - 1.0 if len(wanted) > 1 else 0.0
        spreads[d] = spread

        if len(wanted) > 1:
            print(f"     -> internal spread across {len(wanted)} particles:"
                  f" {spread * 100:.4f}%")
        print()

    return spreads


# ---------------------------------------------------------------------------
# B. How far apart are the rungs?
# ---------------------------------------------------------------------------

def report_gaps(spreads):
    print("=" * 74)
    print("B. RUNG SPACING -- WHY A SCALE CANNOT ARRANGE SECTION A")
    print("=" * 74)
    print("   Sliding the scale moves every mass in the sector together. To")
    print("   fix one particle you would have to break the others, and the")
    print("   nearest rung to break onto is this far away:\n")

    print(f"  {'particle':10s}{'d':>3}{'n':>5}{'nearest rung':>15}"
          f"{'sector spread':>16}{'ratio':>10}")
    print("  " + "-" * 57)

    tightness = {}

    for name, (_, _, d, n) in MEASURED.items():
        gap = rung_gap(n, d)
        spread = spreads.get(d, 0.0)
        ratio = spread / gap if gap else 0.0
        tightness.setdefault(d, []).append(ratio)
        print(f"  {name:10s}{d:>3}{n:>5}{gap * 100:>14.2f}%"
              f"{spread * 100:>15.4f}%{ratio:>10.4f}")

    print("\n   ratio << 1 means the sector's particles agree on their scale far")
    print("   more tightly than the ladder could have arranged by accident.")
    print()

    return tightness


# ---------------------------------------------------------------------------
# C. Look-elsewhere: how many other assignments would have worked?
# ---------------------------------------------------------------------------

def report_alternatives(n_max=200):
    print("=" * 74)
    print("C. EXHAUSTIVE ALTERNATIVES (the look-elsewhere factor)")
    print("=" * 74)
    print("   A per-quantity significance says how unlikely a target is to land")
    print("   near ONE chosen rung. It does not ask how many rungs were on")
    print("   offer. This does, by searching every assignment in the window.\n")

    derived = sector_scales()
    by_sector = {}

    for name, (_, _, d, _) in MEASURED.items():
        by_sector.setdefault(d, []).append(name)

    for d in sorted(by_sector):
        names = by_sector[d]

        if len(names) < 2:
            continue

        # The observed internal spread, which any rival assignment must beat.
        actual = max(demanded_scale(x) for x in names) / \
                 min(demanded_scale(x) for x in names) - 1.0

        masses = []
        for name in names:
            mass = MEASURED[name][0]
            if name == 'tau':
                mass /= TAU_BACKREACTION
            masses.append(mass)

        # Search every assignment of distinct indices to this sector's
        # particles, preserving mass order so the comparison is like for like.
        rungs = [(n, S(n, d)) for n in range(1, n_max + 1)]
        order = sorted(range(len(masses)), key=lambda i: masses[i])
        better = 0
        total = 0

        def walk(slot, lo, chosen):
            nonlocal better, total

            if slot == len(order):
                total += 1
                want = [masses[order[i]] / chosen[i] for i in range(len(order))]
                if max(want) / min(want) - 1.0 <= actual:
                    better += 1
                return

            for idx in range(lo, len(rungs)):
                walk(slot + 1, idx + 1, chosen + [rungs[idx][1]])

        walk(0, 0, [])

        idwt = " ".join(f"{x}(n={MEASURED[x][3]})" for x in names)
        print(f"  d={d}   {idwt}")
        print(f"     IDWT internal spread          : {actual * 100:.4f}%")
        print(f"     assignments searched (n<={n_max}) : {total:,}")
        print(f"     assignments fitting as well   : {better:,}"
              f"   ({better / total * 100:.4f}% of the space)")
        print()


# ---------------------------------------------------------------------------
# D. Honest ledger
# ---------------------------------------------------------------------------

def report_ledger(tightness):
    print("=" * 74)
    print("D. LEDGER -- WHERE THE CLAIM HOLDS AND WHERE IT DOES NOT")
    print("=" * 74)

    for d in sorted(tightness):
        worst = max(tightness[d])
        if worst == 0.0:
            verdict = "single particle -- no constraint, carries no weight"
        elif worst < 0.01:
            verdict = "HOLDS -- spread is under 1% of the rung gap"
        elif worst < 0.1:
            verdict = "holds -- spread is a small fraction of the gap"
        else:
            verdict = "FAILS unaided -- needs a correction to close"
        print(f"  d={d:<3} worst spread/gap = {worst:7.4f}   {verdict}")

    print()
    print("   The coloured sectors (d=3, d=4) do not close on one scale. That")
    print("   is why the confinement-binding correction exists, and it is the")
    print("   place a referee should press hardest -- a level-dependent")
    print("   correction fitted where a single scale failed is exactly the")
    print("   freedom this script is otherwise measuring the absence of.")
    print()


def main():
    print()
    print("SECTOR-SCALE STRICTNESS")
    print("one scale per sector, several masses each, rungs far apart")
    print()
    spreads = report_scales()
    tightness = report_gaps(spreads)
    report_alternatives()
    report_ledger(tightness)


if __name__ == '__main__':
    main()
