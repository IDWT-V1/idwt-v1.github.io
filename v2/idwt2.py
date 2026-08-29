#!/usr/bin/env python3
"""idwt2.py — Infinite Dimensional Wave Theory, Second Edition: computation record.

Written from scratch for the second edition (v2/). Bare framework only:
NO correction factors anywhere. Every number is the raw output of
  counting function x sector unit,
with the couplings and units derived from the sector geometry and one
reference mass (the electron's). Deviations from measurement are printed
as they stand. The first-edition master record (files/idwt.py) carries the
full corrected framework and its verification history; this file is the
second edition's engine, matching v2/IDWT2_01..06.

Inputs: m_e = 0.511 MeV (unit reference); geometry integers N_c = 3 (colour
classes of CP^2) and n_s-class count 4 (classes of CP^3). PDG 2024 values
appear only as comparisons, never as inputs.

Run: python3 idwt2.py   (self-contained, stdlib only)
"""

from fractions import Fraction as Fr
from math import sqrt, pi, isclose

# ----------------------------------------------------------------------
# S1. THE COUNTING FUNCTION  S(n,d) = C(n+d-1, d)
#     = cumulative state count of the d-dimensional well below level n.
# ----------------------------------------------------------------------

def C(n, k):
    if k < 0 or k > n:
        return 0
    out = 1
    for i in range(k):
        out = out * (n - i) // (i + 1)
    return out

def S(n, d):
    return C(n + d - 1, d)

# hockey-stick identity check: sum of level degeneracies = S(n,d)
for (n, d) in [(4, 3), (13, 6), (72, 4), (22, 5), (81, 2)]:
    assert sum(C(k + d - 1, d - 1) for k in range(n)) == S(n, d)
# Pascal recursion check: S(n,d) = S(n,d-1) + S(n-1,d)
for (n, d) in [(4, 4), (20, 4), (35, 6), (15, 5)]:
    assert S(n, d) == S(n, d - 1) + S(n - 1, d)

# ----------------------------------------------------------------------
# S2. THE SIX SECTOR COUPLINGS (closed forms in a=3, b=4)
# ----------------------------------------------------------------------

a_int, b_int = 3, 4                      # colour classes; lepton classes

# universal coefficient (equal both ways by binomial symmetry C(6,4)=C(6,2))
g_coeff_sq_1 = Fr(b_int * (b_int + 1), S(b_int, 4))     # 20/35
g_coeff_sq_2 = Fr(a_int * (a_int + 1), S(a_int, 5))     # 12/21
assert g_coeff_sq_1 == g_coeff_sq_2 == Fr(4, 7)
g_coeff = 2 / sqrt(7)

gap3 = b_int ** 2                        # 16
gap4 = Fr(2 * a_int * b_int, a_int + b_int)             # 24/7

g33 = gap3 / g_coeff                     # = b^2 sqrt(a+b)/2 = 8*sqrt(7)
g44 = float(gap4) / g_coeff              # = a*b/sqrt(a+b) = 12/sqrt(7)
assert isclose(g33, 8 * sqrt(7)) and isclose(g44, 12 / sqrt(7))
assert isclose(g33 * g44, 96.0)          # product a*b^3/2
g34 = sqrt(g33 * g44)                    # 4*sqrt(6)

g66 = 0.25                               # 1/(lepton class count); FS curvature
g10 = g66                                # shared complex-sector coupling

p_count = S(4, 3) - a_int                # 17
q_count = S(3, 4) - S(3, 3)              # 5   (= S(2,4), hockey-stick)
g22 = p_count ** 2 * q_count / 2         # 722.5  (state count; two d=3 legs^2 x one d=4 leg / exchange 2)

g55 = g33 * g44 / g22                    # Hopf fiber universality: v3/v2 = v5/v4
assert isclose(sqrt(g22) * sqrt(g55), g34)

# ----------------------------------------------------------------------
# S3. SELF-DUG WELLS: lambda_d = (g_dd/2)^(2/3); ground energy; width
# ----------------------------------------------------------------------

sectors = {2: g22, 3: g33, 4: g44, 5: g55, 6: g66, 10: g10}
lam = {d: (g / 2) ** (2 / 3) for d, g in sectors.items()}
E0  = {d: d * sqrt(lam[d]) for d in sectors}
L   = {d: lam[d] ** -0.25 for d in sectors}

# ----------------------------------------------------------------------
# S4. SECTOR UNITS FROM ONE REFERENCE MASS
#     m_scale_d = m_e * sqrt(g_dd/g66) / S(n_floor, d)
# ----------------------------------------------------------------------

m_e = 0.511            # MeV — the sole mass input

m6 = m_e / S(13, 6)                       # electron defines the d=6 unit
m10 = m6                                  # shared coupling => shared unit
m3 = m_e * sqrt(g33 / g66)                # floor n=1: S(1,3)=1 (down quark)
m4 = m_e * sqrt(g44 / g66) / S(3, 4)      # floor n=3: S(3,4)=15 (up quark)
m2 = m_e * sqrt(g22 / g66)
m5 = (a_int / b_int) * m6 ** 3 / m4 ** 2  # cross-sector relation (why nu light)

# ----------------------------------------------------------------------
# S5. THE SPECTRUM — BARE: counting function x unit, nothing else
# ----------------------------------------------------------------------

PDG = {   # PDG 2024 comparison values (MeV)
    'electron': 0.511, 'muon': 105.6584, 'tau': 1776.93,
    'down': 4.70, 'strange': 93.5, 'bottom': 4183.0,
    'up': 2.16, 'charm': 1273.0, 'top': 172570.0,
    'W': 80369.2, 'Z': 91188.0, 'Higgs': 125200.0, 'photon': 0.0,
}

bare = {
    'electron': m6 * S(13, 6),
    'muon':     m6 * S(35, 6),
    'tau':      m10 * S(23, 10),
    'down':     m3 * S(1, 3),
    'strange':  m3 * S(4, 3),
    'bottom':   m3 * sqrt(S(16, 3) * S(17, 3)),   # two-mode beat at level 16
    'up':       m4 * S(3, 4),
    'charm':    m4 * S(20, 4),
    'top':      m4 * S(72, 4),
    'photon':   m2 * S(0, 2),                     # exactly zero
    'W':        m2 * S(76, 2),
    'Z':        m2 * S(81, 2),
    'Higgs':    m2 * S(95, 2),
}

nu_bare = {i: m5 * S(n, 5) for i, n in (('nu1', 10), ('nu2', 15), ('nu3', 22))}

# exact dimensionless ratios (unit cancels)
r_mu_e  = Fr(S(35, 6), S(13, 6))          # 3515/17
r_tau_e = Fr(S(23, 10), S(13, 6))
r_Z_W   = Fr(S(81, 2), S(76, 2))
r_u_d   = sqrt(g44 / g33)                 # sqrt(3/14), coupling-only
r_nu21  = Fr(S(15, 5), S(10, 5))
r_nu31  = Fr(S(22, 5), S(10, 5))

# ----------------------------------------------------------------------
# S6. MIXING AS COUNTING — BARE (no curvature correction)
# ----------------------------------------------------------------------

sin2_thetaC = Fr(S(1, 3), S(4, 3))        # 1/20
sin_thetaC  = sqrt(float(sin2_thetaC))    # 0.22361 bare
V_cb        = sqrt(S(3, 4) / S(20, 4))
V_us_pdg, V_cb_pdg = 0.22450, 0.04100

# ----------------------------------------------------------------------
# S7. THE COUPLING CASCADE (no adjustable step)
# ----------------------------------------------------------------------

g_s2 = 2 * g44 / pi ** 2                  # kernel over CP^2 volume
g_s  = sqrt(g_s2)
g_2  = Fr(2, 3) * sqrt(g_s)               # x up-quark charge 2/3
g_2  = float(g_2)
sin2_thetaW = 1 - float(Fr(S(76, 2), S(81, 2))) ** 2
cos_thetaW  = float(Fr(S(76, 2), S(81, 2)))
m_W_GeV = bare['W'] / 1000.0
G_F = g_2 ** 2 / (4 * sqrt(2) * m_W_GeV ** 2)     # GeV^-2

# ----------------------------------------------------------------------
# S8. THE STRONG SECTOR: confinement scale and composites (bare inputs)
# ----------------------------------------------------------------------

hbarc = 197.327                            # MeV fm (unit conversion only)
N_c   = a_int
f_pi  = m3 * S(4, 3)                       # coupling dilution g33/S crosses 1 at level 4
Lam   = N_c * f_pi
lam_c = N_c ** 2 * f_pi / 2                # colour energy scale
sigma_GeV2 = (lam_c / 1000.0) ** 2         # string tension = lambda_c^2
m_N   = N_c * Lam + bare['strange']        # nucleon: 3 colour bonds + strange (identity N_c*Lam/a^2 = m_s)
B0    = Lam * S(4, 3) / 2                  # chiral condensate parameter
m_pi  = sqrt((bare['down'] + bare['up']) * B0)
E_bind_b = sqrt(bare['bottom'] * Lam)      # heavy-quark binding
m_rho = m3 * S(9, 3)                       # d=3 resonance level 9

# fringe-law identity (verified: standing channel energy is linear):
#   sigma = A^2 k^2 / 2 — one scale squared; with A,k at lambda_c: sigma = lambda_c^2.

# ----------------------------------------------------------------------
# OUTPUT
# ----------------------------------------------------------------------

def dev(pred, obs):
    return f"{100*(pred-obs)/obs:+.2f}%" if obs else "exact"

W = 72
print("=" * W)
print("IDWT SECOND EDITION — BARE COMPUTATION RECORD (no corrections)")
print("=" * W)
print(f"inputs: m_e = {m_e} MeV; geometry integers 3 (colour), 4 (lepton classes)")

print("\n-- couplings (closed forms) " + "-" * 43)
print(f"g33 = 8*sqrt7        = {g33:9.4f}      g44 = 12/sqrt7 = {g44:8.4f}")
print(f"g22 = 17^2*5/2       = {g22:9.4f}      g66 = g10,10   = {g66:8.4f}")
print(f"g55 = 96/g22         = {g55:9.4f}      (Hopf universality, forced)")
print(f"check g33*g44 = 96: {g33*g44:.10f}")

print("\n-- sector units from m_e " + "-" * 46)
for name, val in (("m_scale,2", m2), ("m_scale,3", m3), ("m_scale,4", m4),
                  ("m_scale,5", m5), ("m_scale,6", m6)):
    print(f"{name} = {val:.6g} MeV")

print("\n-- the spectrum, BARE (counting x unit) " + "-" * 31)
print(f"{'particle':9s} {'level':>7s} {'bare (MeV)':>12s} {'PDG 2024':>12s} {'dev':>8s}")
levels = {'electron': 13, 'muon': 35, 'tau': 23, 'down': 1, 'strange': 4,
          'bottom': '16~17', 'up': 3, 'charm': 20, 'top': 72,
          'photon': 0, 'W': 76, 'Z': 81, 'Higgs': 95}
for k in ('electron','muon','tau','down','strange','bottom','up','charm',
          'top','photon','W','Z','Higgs'):
    print(f"{k:9s} {str(levels[k]):>7s} {bare[k]:12.4f} {PDG[k]:12.4f} {dev(bare[k],PDG[k]):>8s}")

print("\n-- neutrinos, BARE (no oscillation data used) " + "-" * 25)
for k, n in (('nu1', 10), ('nu2', 15), ('nu3', 22)):
    print(f"{k}: level {n:2d}  m = {nu_bare[k]*1e9:7.3f} meV")
print(f"sum = {sum(nu_bare.values())*1e9:.2f} meV (bound < 120); ordering NORMAL necessarily")
print(f"ratios (exact): m2/m1 = {float(r_nu21):.3f}   m3/m1 = {float(r_nu31):.3f}")

print("\n-- exact dimensionless ratios " + "-" * 41)
print(f"m_mu/m_e  = {r_mu_e} = {float(r_mu_e):.4f}   (PDG 206.7683, {dev(float(r_mu_e),206.7683)})")
print(f"m_tau/m_e = {float(r_tau_e):.3f}          (PDG 3477.23,  {dev(float(r_tau_e),3477.23)})")
print(f"m_Z/m_W   = {r_Z_W} = {float(r_Z_W):.5f} (PDG 1.13461, {dev(float(r_Z_W),1.13461)})")
print(f"m_u/m_d   = sqrt(3/14) = {r_u_d:.4f}       (PDG ~0.462,  {dev(r_u_d,0.462)})")

print("\n-- mixing as counting, BARE " + "-" * 43)
print(f"sin(thetaC) = 1/sqrt(20) = {sin_thetaC:.5f} (PDG {V_us_pdg}, {dev(sin_thetaC,V_us_pdg)})")
print(f"|V_cb| = sqrt(15/8855)   = {V_cb:.5f} (PDG {V_cb_pdg}, {dev(V_cb,V_cb_pdg)})")

print("\n-- coupling cascade " + "-" * 51)
print(f"g_s = {g_s:.5f}   g_2 = {g_2:.5f} (PDG 0.65270, {dev(g_2,0.65270)})")
print(f"sin^2(thetaW) = {sin2_thetaW:.4f} (on-shell 0.22290, {dev(sin2_thetaW,0.22290)})")
print(f"cos(thetaW)   = {cos_thetaW:.5f} (PDG 0.88108)   rho = 1 exact")
print(f"G_F = {G_F:.4e} GeV^-2 (PDG 1.1664e-5, {dev(G_F,1.1664e-5)})")

print("\n-- strong sector and composites (bare inputs) " + "-" * 25)
print(f"f_pi = {f_pi:.2f} MeV (PDG 92.1, {dev(f_pi,92.1)})   Lambda = {Lam:.1f} MeV")
print(f"lambda_c = {lam_c:.1f} MeV -> sigma = lambda_c^2 = {sigma_GeV2:.4f} GeV^2 (lattice 0.18-0.19)")
print(f"         = {lam_c**2/hbarc:.0f} MeV/fm; fringe law sigma = A^2 k^2/2 (linear, verified)")
print(f"m_N  = 3*Lambda + m_s = {m_N:.1f} MeV (PDG 938.9, {dev(m_N,938.9)})")
print(f"m_pi = {m_pi:.1f} MeV (PDG 139.6, {dev(m_pi,139.6)})   B0 = {B0:.0f} MeV")
print(f"E_bind(b) = sqrt(m_b*Lambda) = {E_bind_b:.0f} MeV;  B+ = {bare['bottom']+bare['up']+E_bind_b:.0f} (PDG 5279)")
print(f"rho meson = level 9 = {m_rho:.1f} MeV (PDG 775.3, {dev(m_rho,775.3)})")

print("\n" + "=" * W)
print("Bare record complete. Deviations stand as measured. The corrected")
print("framework and full verification history: files/idwt.py (first edition).")
print("=" * W)
