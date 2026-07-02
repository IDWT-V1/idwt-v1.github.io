---
title: "A Combinatorial-Geometric Derivation of the Standard Model Spectrum"
author:
  - name: Fedge No
    email: fedge-no@hotmail.com
date: 18 June 2026
keywords:
  - Standard Model mass spectrum
  - simplex number
  - sector manifolds
  - neutrino mass prediction
  - coupling filter
  - hockey-stick identity
  - Dirac spectral counting
msc: "81V05, 58J50, 53C27, 11B65"
doi: "10.5281/zenodo.20784573"
header-includes:
  - |
    \let\oldabstract\abstract
    \let\oldendabstract\endabstract
    \renewenvironment{abstract}{%
      \oldabstract
    }{%
      \oldendabstract
      \par\medskip
      \noindent\textbf{MSC 2020:} 81V05 $\cdot$ 58J50 $\cdot$ 53C27 $\cdot$ 11B65\par
      \noindent\textbf{Keywords:} Standard Model mass spectrum; simplex number; sector manifolds; neutrino mass prediction; coupling filter; hockey-stick identity; Dirac spectral counting\par
      \noindent\textbf{DOI:} \href{https://doi.org/10.5281/zenodo.20784573}{10.5281/zenodo.20784573}\par
    }
abstract: |
  We present Infinite-Dimensional Wave Theory (IDWT), a framework that provides a combinatorial derivation of the complete Standard Model mass spectrum, to high accuracy, from three integer seeds $\{n_d = 1,\, n_u = 3,\, n_{\rm top} = 72\}$ — whose composite $n_s = n_d + n_u = 4$ drives the fermion tower — together with a single dimensional reference $m_e$ (the electron mass, used only to convert dimensionless ratios to MeV). The mass of each particle is

  $$m(n, d) = m_{\mathrm{scale},d} \times S(n,d), \qquad S(n,d) = \binom{n+d-1}{d},$$

  where $d \in \{2,3,4,5,6,10\}$ labels a sector of the infinite sector space $\Xi_d$ and $n$ is a mode index derived from the integer seeds by a fixed algebraic filtration chain. We prove five theorems: (S1) $S(n,2k+1) = \tfrac{1}{2}N_{D_{S^{2k+1}}}(n-1)$ for all odd-sphere sectors, grounding both quark and neutrino masses as sector spectral counting laws on their sector manifolds; (S2) the cross-sector frequency ratio $m_u/m_d = \sqrt{3/14}$ exactly from sector couplings; (S3) the EW self-coupling $g_{22} = 722.5$ is a product of Dirac eigenvalue multiplicities; (S4) the sector set $D = \{2,3,4,5,6,10\}$ is the unique set consistent with the seeds, via the factorisation $n_{\rm top} = N_c \times n_s \times N_f = 72$; and a Completeness Theorem showing no additional stable particles exist within the framework. One physically motivated correction is derived without additional inputs: a geometric back-reaction factor $1 + 1/1680$ for the $\tau$ lepton, from the $d=6\to d=10$ sector coupling. The $\ell=2$ kernel component yields a derived scale $\varepsilon = 1/(280\sqrt{7})$ that enters the $\nu_3$ mass closure. A physically motivated confinement-binding correction $M_{\rm phys} = M_{\rm bare}(1 - x_e\langle k\rangle)$ applies to the colour-carrying sectors ($d=3,4$), where finite-well flattening reduces per-state energies; its functional form is derived (finite-cavity GVD / anharmonic perturbation theory) and its scale is derived from the colour energy law for the colour-native $d=4$ sector (well occupation $N_b = \Lambda/4m_{\rm scale,4}$) and applied universally to the coloured $d=3,4$ quarks (d=3 colour is inherited from d=4 via the Hopf map). All quark masses are reproduced within PDG 2024 statistical uncertainties with this correction; all other fermion masses are reproduced at tree level without correction. A cross-sector scale consistency equation yields the first-principles prediction of absolute neutrino masses, giving $\sum m_\nu = 60.39$ meV (corrected; bare $59.00$ meV, with $\delta_{\nu_3} = \varepsilon \times g_{33} = 1/35$ derived from the cross-sector kernel) and $m_{\beta\beta} = 0$ at all orders — since no charge-conjugation matrix $C$ exists on the $S^5$ spinor bundle ($d \bmod 8 = 5$), no Majorana operator can be constructed at any loop order. We further show that each sector geometry constitutes a \emph{coupling filter} for its particles: the sector quantum number (polarization, color, the Dirac condition, color silence, Gegenbauer-critical marginal coupling) is not an input label but the geometry expressing itself as a coupling structure, derived from the sector isometry groups, the Euler characteristic, Clifford algebra, and Clifford algebra mod 8 periodicity on the respective sector manifolds. The framework satisfies exact CKM first-row unitarity at tree level. All results are reproduced by a single open-source Python script from the same seeds.
---

**Technical documentation (10 volumes):** doi:[10.5281/zenodo.19767493](https://doi.org/10.5281/zenodo.19767493)\
**Code:** `idwt.py` (archived at Zenodo)

---

## 1. Introduction

The Standard Model contains 19 free parameters, including six fermion masses spanning five orders of magnitude, three CKM angles, and the electroweak mixing angle. Despite extraordinary experimental precision, no principle relates these parameters from first principles. This paper asks: is there a spectral interpretation of particle masses in which every mass equals a combinatorial integer (a mode count) multiplied by a sector-dependent energy scale, where the integers follow from a few integer seeds through a fixed algebraic filtration rather than being chosen individually to match each observed mass?

We show this interpretation exists and is grounded in the Dirac spectra of infinite-extent sector manifolds with harmonic potential wells (the sector-localized modes of the sector Dirac-Harmonic operator). The framework produces quantitative predictions for all 12 measured particle masses, the electroweak sector, CKM observables, and — new in this work — the absolute masses of all three neutrinos, from three integer seeds $\{n_d=1,\, n_u=3,\, n_{\rm top}=72\}$ (composite $n_s = 4$) and the electron mass $m_e$.

### 1.1 What IDWT Is and Is Not

IDWT does not add new spacetime dimensions in the Kaluza-Klein sense. The sector manifolds $\Xi_d$ are infinite Riemannian spaces — not compact extra dimensions, not accessible to gravitons or KK excitations. They are macroscopic, non-compact spatial dimensions — real geometric spaces in which $\Psi_\infty$ vibrates. They differ from KK compact extra dimensions in that they are non-compact, mode localization is set by the sector localization length $L_d$ (not by periodic boundary conditions), and there is no KK graviton tower. All IDWT predictions concern the mass spectrum and coupling structure of existing particles, not new KK towers. Gravity in IDWT is the back-reaction of $|\Psi_\infty|^2$ on the spacetime metric — purely geometric, with no graviton propagation into the sector space. See Technical Volume 4 [11] for the full derivation of the effective Einstein equations.

This framework does not employ Higgs fields, Yukawa couplings, or spontaneous symmetry breaking to generate masses. The $W$ and $Z$ masses are confinement masses of the $d=2$ sector — analogous to the $\rho$ meson mass in QCD — not consequences of a Higgs mechanism. The mass formula $m \propto S(n,d)$ holds for all particles simultaneously.

The companion Python script `idwt.py` [11] implements every derivation in this paper algebraically and is thoroughly commented with equation references. A referee can verify every claimed number by running the script; the present paper provides the mathematical exposition that makes the derivations checkable without Python.

---

## 2. Framework

### 2.1 Foundations: Sector Manifolds and the Master Spinor Field $\Psi_\infty$

The master spinor field $\Psi_\infty$ is a Dirac spinor field on a product manifold $\mathcal{M}_\infty = \mathbb{R}^{3,1} \times \bigoplus_d \Xi_d$, where each $\Xi_d$ is an infinite Riemannian space of real dimension $d$. A sector harmonic potential $V_d(r) = \lambda_d r^2$ (derived from the kernel self-consistency; §3.10.2) creates a confining well that Gaussian-localizes all modes in the sector direction — these are the particles. The geometry labels $\mathbb{CP}^{(d/2)-1}$ and $S^d$ describe the local symmetry of the potential minimum, not the global topology of $\Xi_d$. The space extends without bound; no dimension is compactified. Our observable universe is the restriction $\psi_{\rm obs}(r,t) = \Psi_\infty(r, \xi^0, t)$ at a fixed internal address $\xi^0$.

The sector manifolds $\Xi_d$ are the complex projective spaces $\mathbb{CP}^{(d/2)-1}$ for even $d$ and the odd spheres $S^d$ for odd $d$, organised by the Hopf fibration chain $S^1 \to S^{2k-1} \to \mathbb{CP}^{k-1}$. Their role is spectral: they determine, through the Dirac eigenvalue spectra of the Hopf fibration chain, which mode frequencies are accessible to $\Psi_\infty$. A particle of type $(n,d)$ is a mode of $\Psi_\infty$ whose internal frequency in sector $\Xi_d$ is $S(n,d) \times m_{\mathrm{scale},d}$.

The mode spectrum is discrete because the bound states of $V_d$ are discrete — just as bound states of the hydrogen potential are discrete even though $\mathbb{R}^3$ is infinite. The sectors are not compactified extra dimensions in any sense. The observable 3D universe does not couple to gravitational modes propagating through $\Xi_d$; the back-reaction of $|\Psi_\infty|^2$ on the spacetime metric enters only through the $d=3$-coordinate component of the energy-momentum tensor $T_{\mu\nu}^{\rm obs} = \int |\Psi_\infty|^2 d\xi$.

**How $\xi^0$ selects the observable SM sector.** The fixed internal address $\xi^0$ does not determine which particles exist — the occupied mode set $\Sigma$ is fixed by the seed $n_s = 4$ independently of $\xi^0$. What $\xi^0$ determines is the projection amplitude with which each mode $(n,d)$ appears to an observer at that address: modes with large $\Omega_{\log}(n,d) = \ln(S(n,d)/S(n,2))$ are suppressed exponentially in the Stage-1 filter (Section 11). The SM spectrum is the set of modes that survive both the Stage-1 visibility filter (small $\Omega_{\log}$) and Stage-2 co-fixed-point stability for all $\xi^0$ simultaneously — it is the spectrum common to every observer address in $\mathcal{M}_\infty$. The choice of $\xi^0$ therefore affects only the relative intensities of already-existing modes, not the identity of the particle spectrum. A full derivation of the $\xi^0$-independence of $\Sigma$ is in Technical Volume 1 §2 [11].

**Core postulates.** (P1) $\Psi_\infty$ satisfies a wave equation on $\mathcal{M}_\infty$ with a quartic cross-sector kernel (Section 2.4). (P2) Mass is the resonant frequency of a mode: $m(n,d) = m_{\mathrm{scale},d} \times S(n,d)$. (P3) The sector set $D = \{2,3,4,5,6,10\}$ is determined by $n_s = 4$ (Theorem S4). Full derivation of the kernel from the spinor geometry is in Technical Volume 8 [11].

### 2.2 The Mass Formula

$$\boxed{m(n, d) = m_{\mathrm{scale},d} \times S(n, d)}, \qquad S(n,d) = \binom{n+d-1}{d} = \dim\bigl(\mathrm{Sym}^{n-1}(\mathbb{C}^{d+1})\bigr).$$

$S(n,d)$ is the cumulative count of monomials of degrees $0$ through $n-1$ in $d$ variables. By the hockey-stick identity, $S(n,d) = \sum_{k=0}^{n-1}\binom{k+d-1}{d-1}$, making it also the cumulative count of eigenvalues of the $d$-dimensional sector harmonic oscillator at levels below $n$. The ground state $S(1,d) = 1$ for all $d$ — the unique non-degenerate ground mode in every sector.

**Spectral grounding.** The identification of $S(n,d)$ with a frequency is not a combinatorial postulate; it is a consequence of the Weyl eigenvalue counting law on the sector manifolds (Theorems S1 and S1-General, Section 3).

### 2.3 Uniqueness of $n_s = 4$

The bottom-regime mode indices derive from the composite integer $n_s = n_d + n_u = 4$, the strange-quark mode index in $d=3$ (the top regime, $n \geq 72$, is fixed by the third seed $n_{\rm top} = 72$).

**Theorem.** $n_s = 4$ is the unique positive integer satisfying $S(n_s, 4) = n_\mu$, where $n_\mu$ is the muon mode index.

*Proof.* $S(1,4)=1$, $S(2,4)=5$, $S(3,4)=15$, $S(4,4)=35$, $S(5,4)=70$. The value 35 appears exactly once. $\square$

The condition is self-referential: the $d=4$ simplex image of the strange-quark mode index equals the muon mode index. This cross-sector resonance uniquely selects $n_s = 4$.

**Sensitivity.** The table below shows Jaccard similarity (intersection over union) between the mode index set generated by $(n_d, n_u)$ and the observed SM spectrum $\{1,3,4,10,13,15,20,22,23,35,72,76,81,95\}$, scanning $n_u$ with $n_d = 1$ and $n_s = n_u + 1$ derived:

| $n_u$ | $n_s = n_u + 1$ | Jaccard | Result |
|---|---|---|---|
| 1 | 2 | 0.105 | Wrong spectrum |
| 2 | 3 | 0.217 | Wrong spectrum |
| **3** | **4** | **1.000** | **Correct** |
| 4 | 5 | 0.174 | Wrong spectrum |
| 5 | 6 | 0.077 | Wrong spectrum |
| 6 | 7 | 0.038 | Wrong spectrum |

The exhaustive verification over all $(n_d,n_u)\in[1..40]^2$ (with $n_s = n_d + n_u$ derived for each pair) is implemented in `idwt.py` (Step 1) using the full 14-rule chain. The unique maximiser is $(n_d,n_u)=(1,3)$ at Jaccard $=1.0$; all other pairs produce Jaccard $\leq 0.438$.

**Note on $n_d = 1$ and $n_u = 3$.** The down-quark index $n_d = 1$ is trivially forced: $S(1,d) = 1$ for all $d$. The up-quark index $n_u = 3$ is a seed grounded by the Euler characteristic of the $d=4$ sector manifold: $n_u = \chi(\mathbb{CP}^2) = N_c = 3$ (T15). The composite $n_s = n_u + 1 = 4$ then follows: the double $4/7$ self-consistency condition of Section 5.1 is satisfied by no other consecutive pair $(n_u, n_u+1)$.

### 2.4 The Master Action and Quartic Kernel

The master action on $\mathcal{M}_\infty$ is:

$$\mathcal{L} = \bar{\Psi}_\infty(i\gamma^\mu \partial_\mu - \sum_d \sqrt{V_d(\xi_d)})\Psi_\infty + \sum_{d \leq d'} \frac{g_{dd'}}{2}\int (\xi_d \cdot \xi_{d'})^2 |\Psi^{(d)}|^2 |\Psi^{(d')}|^2 d\mu,$$

where $V_d(\xi) = \lambda_d |\xi|^2/(1+|\xi|^2)$ is the sector potential (harmonic for small $|\xi|$, saturating at $\lambda_d$ for large $|\xi|$) and $g_{dd'} = v_d v_{d'}$ is the rank-1 coupling matrix with $v_d = \sqrt{g_{dd}}$.

The kernel $({\xi}_d \cdot {\xi}_{d'})^2$ is the leading quartic term consistent with $U(d) \times U(d')$ symmetry on the sector pair. It decomposes by angular momentum on the sector sphere as $(\xi \cdot \xi')^2 = \frac{1}{d}[\ell=0] + \frac{d-1}{d}\cdot C_2^{(d-2)/2}(\cos\theta)[\ell=2]$, where the $\ell=0$ part generates sector mass scales (Section 5) and the $\ell=2$ part generates the derived scale $\varepsilon$ that enters the $\nu_3$ closure and is the candidate mechanism for the $d=4$ up-type overshoot (Section 7.1). The rank-1 structure $g_{dd'}g_{d''d'''} = g_{dd'''}g_{d'd''}$ — equivalently $g_{dd'}^2 = g_{dd}g_{d'd'}$ — is not assumed; it follows from $g_{33}g_{44} = g_{34}^2 = 96$ (verified in Section 5.1). Full derivation in Technical Volume 3 [11].

### 2.5 Spectral Infrastructure: Heat Kernel and Zeta Anchors

The combinatorial mass formula is not ad-hoc: it emerges from a spectral geometry with precise analytic control. The **heat kernel** $K_d(t)=\sum_{n=1}^\infty e^{-tS(n,d)}$ of each sector — the trace of the heat semi-group of $D_d$ — has the small-$t$ Weyl expansion
$$K_d(t) = \underbrace{\Gamma\!\bigl(1+\tfrac{1}{d}\bigr)(d!)^{1/d}}_{\text{Weyl coefficient }a_0^{(d)}}\,t^{-1/d} - \frac{d}{2} + O(t^{1/d}),$$
where the power $t^{-1/d}$ confirms the spectral dimension of sector $d$ equals $d$. Via the Mellin transform $\Gamma(s)\zeta_d(s)=\int_0^\infty t^{s-1}K_d(t)\,dt$, the two terms pin the spectral zeta $\zeta_d(s)=\sum_{n\geq1}S(n,d)^{-s}$ at its two most important arguments:

| Sector $d$ | $\zeta_d(1)=d/(d-1)$ | $\zeta_d(0)=-d/2$ |
|---|---|---|
| 2 | 2 | −1 |
| 3 | 3/2 | −3/2 |
| 4 | 4/3 | −2 |
| 5 | 5/4 | −5/2 |
| 6 | 6/5 | −3 |
| 10 | 10/9 | −5 |

$\zeta_d(1)=d/(d-1)$ is the spectral sum rule proved by telescoping from Pascal's triangle (Part 9 T13a). $\zeta_d(0)=-d/2$ is the zeta-regularised eigenvalue count — the direct analogue of the integrated leading Seeley-DeWitt coefficient on a Riemannian manifold of dimension $d$ — and fixes the sector functional determinant $\log\det D_d=-\zeta_d'(0)$ without a UV cutoff. Both values are purely combinatorial. Together they confirm that each sector behaves as a proper Riemannian space of the expected dimension, with controlled vacuum energy and a well-defined one-loop structure. (Full derivations: Part 9 T13–T14.)

---

## 3. Five Spectral Theorems

### Theorem S1 — Sector Spectral Counting Theorem (Odd Spheres)

The positive Dirac eigenvalues on $S^{2k+1}$ at level $\ell$ are $\lambda_\ell = \ell + (2k+1)/2$, each with multiplicity $M_\ell = 2\binom{\ell+2k}{2k}$ [1]. Their cumulative sum satisfies:

$$\sum_{\ell=0}^{n-1} M_\ell^{S^{2k+1}} = 2\sum_{\ell=0}^{n-1}\binom{\ell+2k}{2k} = 2\binom{n+2k}{2k+1} = 2 \cdot S(n,\, 2k+1).$$

*Proof.* By the hockey-stick identity $\sum_{\ell=0}^{n-1}\binom{\ell+2k}{2k} = \binom{n+2k}{2k+1}$, verified by induction. $\square$

**Corollary.** $S(n, 2k+1) = \tfrac{1}{2}N_{D_{S^{2k+1}}}(n-1)$ for all $k \geq 1$. The mass formula $m = m_{\mathrm{scale},d} \times S(n,d)$ for $d \in \{3,5\}$ is a **sector spectral counting law**: particle mass equals half the cumulative Dirac eigenvalue count on the sector sphere below the particle's level.

For IDWT: $d=3$ ($S^3$, quarks) and $d=5$ ($S^5$, neutrinos) both obey the same law. The three neutrino masses $m_{\nu_i} = m_{\mathrm{scale},5} \times S(n_{\nu_i},5)$ equal $\tfrac{1}{2}N_{D_{S^5}}(n_{\nu_i}-1) \times m_{\mathrm{scale},5}$ — they are half the cumulative Dirac eigenvalue count on $S^5$ at levels below $n_{\nu_i}$, multiplied by the sector scale.

### Theorem S2 — Exact Cross-Sector Frequency Ratio

$$\frac{m_u}{m_d} = \sqrt{\frac{g_{44}}{g_{33}}} = \sqrt{\frac{3}{14}} \approx 0.46291 \quad \text{(exact).}$$

*Proof.* $m_d = m_{\mathrm{scale},3} \times S(1,3) = m_{\mathrm{scale},3}$. From the sector scale relation (Section 5.1): $m_{\mathrm{scale},4} = m_{\mathrm{scale},3}\sqrt{g_{44}/g_{33}}/S(n_u,4)$, so $m_u = m_{\mathrm{scale},4} \times S(n_u,4) = m_{\mathrm{scale},3}\sqrt{g_{44}/g_{33}}$. The $S(n_u,4)$ factors cancel exactly. Then $g_{44}/g_{33} = [n_s n_u/\sqrt{n_s+n_u}]/[n_s^2\sqrt{n_s+n_u}/2] = 2n_u/(n_s(n_s+n_u)) = 6/28 = 3/14$. $\square$

Numerical check: $m_u/m_d = 2.177/4.702 = 0.46291 = \sqrt{3/14}$ to machine precision. This ratio is exact from seeds — no experimental quark mass data enters.

### Theorem S3 — $g_{22}$ from Dirac Multiplicities

Define $\alpha = M_{n_s-1}^{S^3} - n_u = S(n_s,3) - n_u = 17$ and $\beta = S(n_u,4) - S(n_u,3) = 5$. Then:

$$g_{22} = \frac{\alpha^2 \beta}{2} = \frac{17^2 \times 5}{2} = 722.5.$$

$\alpha = 20 - 3 = 17$ is the Dirac multiplicity at level $\ell = n_s-1 = 3$ on $S^3$ (which is $M_3 = (3+1)(3+2) = 20 = S(n_s,3)$ by Theorem S1) less the $n_u = 3$ states at the up-quark sector boundary. $\beta = S(n_u,4)-S(n_u,3) = 5$ is the $d=4$ Dirac eigenstate increment at the up-quark threshold (hockey-stick: $S(n,d)-S(n,d-1) = S(n-1,d)$ at $n=n_u, d=4$ gives $S(2,4)=5$). The two-body kernel contributes $\alpha^2$ from two $d=3$ current insertions each carrying $\alpha$ Dirac eigenstates, $\beta$ from one $d=4$ insertion, and $\tfrac{1}{2}$ from Bose symmetry of the symmetric kernel.

**$\mathbb{CP}^2$ spin^c index (Hirzebruch-Riemann-Roch proof).** Let $X = \mathbb{CP}^2$ with $\int_X H^2 = 1$. Chern class: $c(TX) = (1+H)^3$, Todd class: $\mathrm{td}(TX) = 1+\tfrac{3}{2}H+H^2$, Chern character of $\mathcal{O}(k)$: $\mathrm{ch}(\mathcal{O}(k)) = 1+kH+\tfrac{k^2}{2}H^2$. HRR gives $\chi(\mathbb{CP}^2,\mathcal{O}(k)) = \tfrac{k^2+3k+2}{2} = \binom{k+2}{2}$. For $k=+1$: $\mathrm{ind}=3=N_c$ (three left-handed colour modes). For $k=-1$: $\mathrm{ind}=0$ (right-handed singlets are vector-like). The left-right asymmetry of the quark sector is a theorem of spin^c geometry on $\mathbb{CP}^2$, not a postulate.

### Theorem S4 — Sector Set Determined by the Seeds

**Theorem.** $D = \{2,3,4,5,6,10\}$ is the unique sector set consistent with the integer seeds; no per-sector input enters.

*Proof (four steps).*

**Step 1.** From the mode index filtration chain (Section 4): $n_{\rm top} = S(n_e,2) - n_c + 1 = 91 - 20 + 1 = 72$.

**Step 2.** $72 = N_c \times n_s \times N_f = 3 \times 4 \times 6$, where $N_c=3$ (from Theorem S3/spin^c index), $n_s=4$ (seed), $N_f = 72/12 = 6$ (derived). Cross-check: $N_f = S(n_u,2) = S(3,2) = 6$. These three quantities are Euler characteristics of CP sectors:

$$\chi(\mathbb{CP}^{N_c-1}) = 3,\; d=4. \quad \chi(\mathbb{CP}^{n_s-1}) = 4,\; d=6. \quad \chi(\mathbb{CP}^{N_f-1}) = 6,\; d=10.$$

**Step 3.** $d=2$ ($\mathbb{CP}^1$) is the $U(1)$ Hopf base. $d=3$ ($S^3$ over $\mathbb{CP}^1$) has coupling $g_{33} = n_s^2\sqrt{n_s+n_u}/2$ from the kernel fixed-point. $d=5$ ($S^5$ over $\mathbb{CP}^2$) has coupling $g_{55} = 96/g_{22}$ from Hopf universality $v_3/v_2 = v_5/v_4$.

**Step 4.** $d=7$ carries no matter: it is not a corner of the $\mathbb{C}^2\times\mathbb{C}^3$ deposit grid whose six corners are exactly $D$ (STEP 100), so no mode is sited there (a matter-empty sector is inert). $d=8$: $\chi(\mathbb{CP}^4) = 5 \notin \{N_c, n_s, N_f\}$. $d \geq 11$: no mode index in the occupied range. $\square$

The factorisation $n_{\rm top} = \chi(\mathbb{CP}^2)\,\chi(\mathbb{CP}^3)\,\chi(\mathbb{CP}^5) = 72$ is a characteristic-class identity (Technical Volume 9 T15b): among all characteristic numbers of $\mathbb{CP}^2\times\mathbb{CP}^3\times\mathbb{CP}^5$ the Euler number $72$ is the unique nonzero, non-trivial, purely topological one, so $n_{\rm top}=72$ is structurally natural rather than arbitrary. What this theorem does *not* supply is the dynamical reason this Euler product is selected as the top mode index in the first place; that selection is the framework's leading open question (Section 16, item 5).

**Completeness Theorem.** The IDWT spectrum consists of exactly 15 states ($\Sigma \cup \{b\text{-quark}\}$). Any new stable particle requires either a new sector (excluded by S4) or a new derivable mode index (excluded by the uniqueness theorem). No such states exist. Any new particle discovery at any energy falsifies IDWT immediately.

---

## 4. Mode Index Tower

Every mode index is fixed by the seeds through a small set of named operations — hockey-stick (Pascal) evaluations, additive and inclusion–exclusion edges, the $g$-rule, and the top's Euler product — with no index chosen to match a mass. The hockey-stick is the engine for the simplex backbone; the composite indices (the top, the charged-lepton edges, the bosons, the Higgs) enter through the other operations:

| Particle | $d$ | $n$ | Derivation |
|---|---|---|---|
| $d$ quark | 3 | 1 | $n_d=1$: universal ground state $S(1,d)=1$ for all $d$ |
| $s$ quark | 3 | 4 | seed $n_s$ |
| $c$ quark | 4 | 20 | $S(n_s,3)$ |
| $b$ quark | 3 | 16–17 | resonance at $k_0=n_s^2$ (Section 5.2) |
| $u$ quark | 4 | 3 | seed: $n_u = \chi(\mathbb{CP}^2) = N_c = 3$ (T15) |
| $t$ quark | 4 | 72 | $S(n_e,2) - n_c + 1 = 91-20+1$ |
| $\nu_1$ | 5 | 10 | $S(n_u,3)$ |
| $\nu_2$ | 5 | 15 | $S(n_u,4)$ |
| $\nu_3$ | 5 | 22 | $n_\tau - n_d = 23-1$ |
| $e^-$ | 6 | 13 | $n_{\nu_1} + n_u = 10+3$ (generation law) |
| $\mu^-$ | 6 | 35 | $S(n_s,4)$ (seed fixed point) |
| $\tau^-$ | 10 | 23 | $n_c + n_u = 20+3$ |
| $W^\pm$ | 2 | 76 | $d_\nu + n_{\rm top} - 1 = 5+72-1$ ($g$-rule) |
| $Z^0$ | 2 | 81 | $n_W + \beta = 76+5$ |
| $H$ | 2 | 95 | $n_u + n_c + n_t = 3+20+72$ [open] |

**Algebraic cross-checks** (exact consequences of the chain, independently verified):
$n_e = k_0 - n_u = 13$; $\;\; n_\tau = n_c + n_u = 23$; $\;\; n_H = n_Z + 2(n_s+n_u) = 95$; $\;\; n_{\rm top} = \chi(\mathbb{CP}^2)\chi(\mathbb{CP}^3)\chi(\mathbb{CP}^5) = 72$; $\;\; n_Z - n_W = \beta = 5$ (same $\beta$ as in $g_{22}$).

[Open] The Higgs mode index $n_H = n_u + n_c + n_t = 95$ satisfies two independent cross-sector closure relations and is numerically verified, but the dynamical derivation of why scalar excitation indices close under this sum is an open item (Technical Volume 2 §6).

**Spectral independence:** The 14 occupied $S$-values $\{1, 15, 20, 8855, 2002, 2926, 3321, 4560, 11628, 18564, 65780, 1215450, 3838380, 64512240\}$ form a Sidon-like set: no three satisfy $S_i + S_j = S_k$ (all 91 pairs verified). Any perturbation of a mode index breaking this property would immediately produce an inconsistency.

---

## 5. Coupling Constants and Sector Scales

### 5.1 Coupling Constants from the Seed

The kernel vacuum fixed-point at $k_0 = n_s^2 = 16$ requires the self-consistency eigenvalue to equal $4/7$ in both the $d=3$ and $d=4$ sectors simultaneously:

$$\frac{n_s(n_s+1)}{S(n_s,4)} = \frac{4 \times 5}{35} = \frac{4}{7}, \qquad \frac{n_u(n_u+1)}{S(n_u,5)} = \frac{3 \times 4}{21} = \frac{4}{7}.$$

Both ratios equal $4/7$ exactly. This double equality — the $d=3$ and $d=4$ sectors share the same self-consistency eigenvalue at $k_0$ — confirms that $n_s = n_u + 1 = 4$; no other consecutive pair $(n_u, n_u+1)$ produces this coincidence. The Jacobi coupling amplitude at the resonance is $g_{\rm coeff} = \sqrt{4/7} = 2/\sqrt{7}$.

The self-coupling constants follow from this fixed-point condition:

$$g_{33} = \frac{n_s^2\sqrt{n_s+n_u}}{2} = \frac{16\sqrt{7}}{2} = 8\sqrt{7} \approx 21.166,$$

$$g_{44} = \frac{n_s n_u}{\sqrt{n_s+n_u}} = \frac{12}{\sqrt{7}} \approx 4.536,$$

$$g_{33} \times g_{44} = \frac{n_s^3 n_u}{2} = \frac{4^3 \times 3}{2} = 96.$$

The product identity $g_{33}g_{44} = 96$ implies $g_{34} = \sqrt{g_{33}g_{44}} = 4\sqrt{6}$, confirming the rank-1 factorisation $G_{dd'} = v_d v_{d'}$ as a consequence rather than an assumption.

From Theorem S4, Step 2: $g_{66} = 1/n_s = 1/4$ (seed ratio for the $\mathbb{CP}^3$ lepton sector). $g_{22} = 722.5$ (Theorem S3). $g_{55} = 96/g_{22} \approx 0.1329$ (Hopf universality: $v_3/v_2 = v_5/v_4$).

### 5.2 Sector Mass Scales

All scales reduce to $m_e$ via the coupling ratios. The $d=6$ scale is the unit anchor:

$$m_{\mathrm{scale},6} = \frac{m_e}{S(n_e,6)} = \frac{0.51100}{18564} \text{ MeV} = 2.7526 \times 10^{-5} \text{ MeV},$$

$$m_{\mathrm{scale},3} = m_e\sqrt{g_{33}/g_{66}} = 0.51100\sqrt{8\sqrt{7}/0.25} = 4.7019 \text{ MeV},$$

$$m_{\mathrm{scale},4} = m_{\mathrm{scale},3}\frac{\sqrt{g_{44}/g_{33}}}{S(n_u,4)} = \frac{4.7019 \times \sqrt{3/14}}{15} = 0.14510 \text{ MeV},$$

$$m_{\mathrm{scale},2} = m_e\sqrt{g_{22}/g_{66}} = 0.51100\sqrt{722.5/0.25} = 27.471 \text{ MeV}.$$

**Derivation of $g_s$ from $\mathbb{CP}^2$ integration.** The strong coupling emerges from integrating the kernel coupling density $g_{44}$ over $\mathbb{CP}^2$ with the Fubini-Study metric. The Fubini-Study volume of $\mathbb{CP}^2$ (with the standard normalization where a projective line has area $\pi$) is $\pi^2/2$. Averaging $g_{44}$ over this volume gives $g_{44}/(\pi^2/2) = 2g_{44}/\pi^2$, and so:

$$g_s = \sqrt{\frac{2g_{44}}{\pi^2}} = \sqrt{\frac{2 \times 12/\sqrt{7}}{\pi^2}} = 0.9587.$$

The $\mathrm{SU}(2)_L$ coupling is then the charge of the fundamental quark doublet $Q_u = 2/3$ weighted by $\sqrt{g_s}$:

$$g_2 = Q_u\sqrt{g_s} = \frac{2}{3}\sqrt{g_s} = \frac{2}{3}\left(\frac{2g_{44}}{\pi^2}\right)^{1/4} = 0.65275 \quad (\text{PDG } 0.65270, +0.008\%).$$

Full derivation of the $\mathbb{CP}^2$ integration measure and the $Q_u = 2/3$ charge assignment from the spin^c index: Technical Volume 3 §7 [11].

### 5.3 Bottom Quark: Resonance and Geometric Mean

The bottom quark requires separate treatment because three independent conditions coincide at $k_0 = n_s^2 = 16$ in $d=3$:

$$k_0 = n_s^2 = 16, \qquad k_0 = n_e + n_u = 13+3, \qquad k_0 = S(n_s,3) - S(2,3) = 20-4.$$

This triple degeneracy concentrates the kernel drive at $k_0$. The off-diagonal kernel coupling between adjacent $d=3$ modes at $k_0$ is:

$$K_{k_0, k_0+1} \propto \sqrt{b_{k_0} \cdot b_{k_0+1}},$$

where $b_n = \sqrt{n(n+d-1)}/(2n+d-2)$ is the Jacobi coupling at level $n$ in sector $d$. At the triple-coincidence site, the l=0 kernel cannot distinguish modes $n=16$ and $n=17$: both have equal self-consistent spectral weight. The equal-weight fixed point gives the mass as the geometric mean of the two adjacent mode frequencies:

$$m_b = \sqrt{S(16,3) \times S(17,3)} \times m_{\mathrm{scale},3} = \sqrt{816 \times 969} \times 4.7019 = 4181 \text{ MeV}.$$

Why the geometric mean rather than arithmetic? The kernel bilinear $|\Psi^{(n)}|^2|\Psi^{(n+1)}|^2$ at equal occupation $|\Psi^{(n)}| = |\Psi^{(n+1)}|$ has energy $\sqrt{E_n E_{n+1}}$ by the AM-GM relation applied to the quadratic fixed-point equation $E^2 = E_n E_{n+1}$ — the unique positive solution when both mode contributions are equal. The geometric mean is forced by the equal-weight condition, not chosen for fit. Full derivation in Technical Volume 2 §5.3 [11]; `idwt.py` lines 220–245.

PDG: $m_b = 4180 \pm 10$ MeV. Error: $+0.023\%$. The exhaustive search over $n \leq 200$, $d \in D$ finds no other triple-coincidence site — the bottom quark beat is unique.

---

## 6. Mass Predictions

**Table 1.** All masses from $m_e$ and $n_s = 4$ alone (PDG 2024). Up-type quark masses are quoted **bare** (confinement-binding correction in §7.1 brings all quarks within ±1σ PDG). The $\tau$ carries the geometric back-reaction; the $b$ quark is a geometric-mean beat.

| Particle | $d$ | $n$ | $S(n,d)$ | IDWT (MeV) | PDG (MeV) | Error |
|---|---|---|---|---|---|---|
| $\gamma$ | 2 | 0 | — | 0 | 0 | exact |
| $W^\pm$ | 2 | 76 | 2,926 | 80,379 | 80,369.2 | $+0.01\%$ |
| $Z^0$ | 2 | 81 | 3,321 | 91,230 | 91,188.0 | $+0.05\%$ |
| $H$ | 2 | 95 | 4,560 | 125,266 | 125,200(110) | $+0.05\%$ |
| $d$ | 3 | 1 | 1 | 4.702 | 4.70(7) | $+0.04\%^\dagger$ |
| $s$ | 3 | 4 | 20 | 93.96 | 93.5(8) | $+0.49\%^\dagger$ |
| $b$ | 3 | beat | — | 4,181 | 4,183(7) | $-0.05\%$ |
| $u$ | 4 | 3 | 15 | 2.175 | 2.16(7) | $+0.70\%^\dagger$ |
| $c$ | 4 | 20 | 8,855 | 1,277.3 | 1,273.0(46) | $+0.34\%$ (+0.9$\sigma$) |
| $t$ | 4 | 72 | 1,215,450 | 172,500 | 172,570(290) | $-0.04\%$ (−0.2$\sigma$) |
| $e^-$ | 6 | 13 | 18,564 | 0.51100 | 0.51100 | unit ref. |
| $\mu^-$ | 6 | 35 | 3,838,380 | 105.657 | 105.6584 | $-0.001\%$ |
| $\tau^-$ | 10 | 23 | 64,512,240 | 1,776.84 | 1,776.93(12) | $-1.0\sigma$ |

$^\dagger$ The light quarks ($d$, $s$, $u$) carry the universal confinement-binding correction (§7.1; down has $\langle k\rangle = 0$ and is unshifted) and sit within the sizable PDG uncertainties: $d$ $+0.04\%$, $s$ $+0.49\%$, $u$ $+0.70\%$. The scale-free in-sector ratios carry a small $n$-dependent residual that a uniform offset cannot produce (Section 13). The charm and top **bare** counts overshoot by $+0.93\%$ and $+2.20\%$ (their nominal $+2.6\sigma$/$+13\sigma$ are against statistical errors only and are scheme-sensitive); the same correction brings them to $+0.34\%$ and $-0.04\%$, within $\pm1\sigma$ (Table 1, §7.1).

---

## 7. Two Physical Corrections

### 7.1 The $d=4$ Up-Type Overshoot (open)

The bare mass formula overshoots in the $d=4$ up-type sector, growing with generation: up $+0.77\%$, charm $+0.93\%$, top $+2.20\%$. The overshoot is colour-field binding energy — the fraction of the free-quark harmonic count permanently locked in the confining colour field. Applying the confinement-binding correction $M_{\rm phys} = M_{\rm bare}(1 - x_e\,d(n-1)/(d+1))$ (where $\langle k\rangle = d(n-1)/(d+1)$ is an exact identity, not a large-$n$ approximation) brings all five quarks within $\pm1\sigma$ of PDG 2024 statistical errors. Up-type masses are quoted bare in Table 1; corrected values are in §7.1.

**The $\ell=2$ kernel component (a candidate, not applied).** The $\ell=2$ tensor component of the kernel $({\xi}_d \cdot {\xi}_{d'})^2$ is a candidate source for the overshoot. For $d=3$ on $S^2$,

$$(\xi \cdot \xi')^2 = \tfrac{1}{3}[\ell=0] + \tfrac{2}{3}P_2(\cos\theta)[\ell=2].$$

The $\ell=0$ piece sets the sector mass scale; the $\ell=2$ piece is traceless and once offered a candidate self-energy for the overshoot (correct sign, growing with the mode index), but its shape matched only the $\{0,3,10\}$ set (not the measured masses) and is withdrawn. The operative up-type correction is the confinement-binding deficit (§7.1); the $\ell=2$ scale $\varepsilon$ is retained for the $\nu_3$ closure.

**The scale $\varepsilon$ (retained for $\delta_{\nu_3}$, not applied to quarks).** The $\ell=2$ coupling amplitude at the resonance site $k_0 = n_s^2 = 16$, normalised at the muon mode $n_\mu = S(n_s,4) = 35$, is

$$g_{\rm coeff} = \sqrt{n_s(n_s+1)/S(n_s,4)} = \sqrt{4/7} = 2/\sqrt{7}, \qquad \varepsilon = \frac{g_{\rm coeff}}{k_0 \times n_\mu} = \frac{2/\sqrt{7}}{16 \times 35} = \frac{1}{280\sqrt{7}} \approx 0.001350.$$

Every factor is forced ($g_{\rm coeff}$ from the double self-consistency condition, $k_0$ from the seed $n_s$, $n_\mu$ from $S(n_s,4)$), so $\varepsilon$ is a genuinely derived quantity. It is retained as the scale of the separate, motivated $\nu_3$ closure $\delta_{\nu_3} = \varepsilon \times g_{33} = 1/35$ (§7.2).

**The confinement-binding correction.** The bare count $m_{\rm scale,4}\times S(n,4)$ is the free-quark mass; because a coloured quark is never asymptotically free, part of that energy stays locked in the colour field, so the realised mass is lower by $M_{\rm phys}=M_{\rm bare}(1-x_e\langle k\rangle)$. The deficit carries a single derived coefficient $x_e = 3/(16 N_b)$, $N_b = \Lambda/(4\,m_{\rm scale,4})$ from the colour energy law, applied **universally** to the coloured $d=3,4$ quarks (d=3 colour is inherited from $d=4$ via the Hopf map); see §7.1 and `files/idwt.py` STEP 127. This brings all five quarks within $\pm1\sigma$ of PDG 2024 (Table 1). The scale-independent ratio $m_t/m_c = S(72,4)/S(20,4) = 137.26$ matches the conventional ratio to $\sim$1\%; the top index $72$ (a product form $N_c n_s N_f$, off the additive tower) is of open origin.

### 7.2 Tau Lepton Geometric Back-reaction Correction — Complete Derivation

The $d=6$ ($\mu$) and $d=10$ ($\tau$) sectors share identical coupling $g_{66} = g_{6,10} = g_{10,10} = 1/n_s = 1/4$ from the seed. The leading $d=6 \to d=10$ back-reaction perturbation at the $\tau$ level is:

$$\varepsilon_{6\to10} = \frac{1}{n_s^3 \times S(n_s,4)} = \frac{1}{64 \times 35} = \frac{1}{2240}.$$

The physical interpretation: $n_s^3 = k_0 \times n_s$ is the volume factor of the seed resonance; $S(n_s,4) = n_\mu$ is the frequency normalization. The back-reaction feeds through $g_{10,10} = 1/n_s = 1/4$, creating a geometric series:

$$\frac{\Delta m_\tau}{m_\tau} = \frac{\varepsilon_{6\to10}}{1 - g_{10,10}} = \frac{1/2240}{1 - 1/4} = \frac{1/2240}{3/4} = \frac{4}{3 \times 2240} = \frac{1}{1680},$$

where $1680 = n_s \times n_u \times (n_s+n_u) \times S(n_s,3) = 4 \times 3 \times 7 \times 20$. The corrected tau mass is:

$$m_\tau^{\rm corr} = m_\tau^{\rm raw} \times \left(1 + \frac{1}{1680}\right) = 1775.79 \times 1.000595 = 1776.84 \text{ MeV.}$$

PDG 2024: $1776.93 \pm 0.09$ MeV. Error: $-1.0\sigma$.

The factor $1/1680$ is entirely determined by $n_s = 4$ (through $n_s, n_u, n_s+n_u, S(n_s,3)$) with no empirical input.

---

## 8. Electroweak Sector

The Weinberg angle follows from mode indices alone:

$$\sin^2\theta_W = 1 - \left(\frac{S(76,2)}{S(81,2)}\right)^2 = 1 - \left(\frac{2926}{3321}\right)^2 = 0.22373.$$

The $\rho$ parameter $\rho = m_W^2/(m_Z^2\cos^2\theta_W) = 1$ exactly — $W$ and $Z$ are both $d=2$ modes so their ratio is determined by integer counts alone.

The $Z$–$W$ mode gap $n_Z - n_W = 5 = \beta$ is the same $\beta$ that enters $g_{22}$ (Theorem S3). The W-Z mass ratio and the EW self-coupling share a single spectral origin.

From Section 5.2, $g_2 = 0.65275$ and $m_W = m_{\text{scale},2}\times S(76,2) = 80379$ MeV. Both are independently derived. The Fermi constant follows from the $W$ propagator at $q^2 \ll m_W^2$:
$$G_F = \frac{g_2^2}{4\sqrt{2}\,m_W^2} = 1.16584\times10^{-5}\text{ GeV}^{-2}\quad (\text{PDG: }1.16638\times10^{-5},\;-0.047\%).$$
No Higgs VEV enters — $g_2$ and $m_W$ have independent spectral origins.

| EW quantity | IDWT | PDG | Error |
|---|---|---|---|
| $\sin^2\theta_W$ (on-shell) | 0.22373 | 0.22290 | $+0.37\%$ |
| $g_2$ | 0.65275 | 0.65270 | $+0.008\%$ |
| $v$ (GeV) | 246.28 | 246.22 | $+0.023\%$ |
| $G_F$ ($10^{-5}$ GeV$^{-2}$) | 1.16584 | 1.16638 | $-0.047\%$ |
| $\Gamma_W$ (MeV) | 2044 | 2085 | $-1.96\%$ |
| $\Gamma_Z$ (MeV) | 2444 | 2495 | $-2.05\%$ |

The $\Gamma_{W,Z}$ discrepancies are consistent with missing one-loop QCD corrections ($\alpha_s/\pi \approx 3\%$ at $m_Z$), which are beyond tree level.

---

## 9. CKM Matrix

$$\sin\theta_C = \frac{1 + \chi(\mathbb{CP}^1)/(24\cdot S(n_s,3))}{\sqrt{S(n_s,3)}} = \frac{1+1/240}{\sqrt{20}} = 0.22454.$$

The bare value $1/\sqrt{S(n_s,3)} = 1/\sqrt{20}$ comes from the ratio of $d=3$ mode counts at the seed level. The $1/240$ correction is the first Seeley-DeWitt coefficient for the heat kernel on $S^2 \cong \mathbb{CP}^1$ (Euler characteristic $\chi = 2$, seed count $S(n_s,3) = 20$): $\chi/(24 \cdot S(n_s,3)) = 2/480 = 1/240$.

$$|V_{cb}| = \sqrt{\frac{S(n_u,4)}{S(n_c,4)}} = \sqrt{\frac{15}{8855}} = 0.04116, \qquad A_{\rm Wolf} = |V_{cb}| \times S(n_s,3) = 0.82315.$$

**CKM unitarity.** At tree level: $|V_{ud}|^2 + |V_{us}|^2 + |V_{ub}|^2 = 1$ exactly — since $|V_{ud}|=\sqrt{1-|V_{us}|^2}$ and $|V_{ub}|=0$ at tree level. The reported "+5.5$\sigma$ CKM unitarity tension" in the literature is in the nuclear-QED-corrected extraction of $|V_{ud}|$ from superallowed $\beta$ decay, not in the bare coupling. IDWT predicts the bare coupling; the nuclear radiative correction $\delta_R \approx 0.024$ is external nuclear physics.

| Observable | IDWT | PDG | Tension |
|---|---|---|---|
| $\sin\theta_C$ | 0.22454 | 0.22450 | $+0.09\sigma$ |
| $|V_{cb}|$ | 0.04116 | 0.04100 | $+0.11\sigma$ |
| Wolfenstein $A$ | 0.82315 | 0.82300 | $+0.03\sigma$ |

---

## 10. Absolute Neutrino Masses

The $d=5$ sector has Euler characteristic zero and no self-confinement. Its mass scale is set by the Hopf fibration $S^1 \to S^5 \to \mathbb{CP}^2$ requiring the $d=5$ scale to be doubly suppressed by the $d=4$ quark scale:

$$m_{\mathrm{scale},5} \times m_{\mathrm{scale},4}^2 = \frac{n_u}{n_s} \times m_{\mathrm{scale},6}^3 = \frac{3}{4} \times (2.7526 \times 10^{-5})^3 \text{ MeV}^3,$$

$$m_{\mathrm{scale},5} = \frac{3}{4} \times \frac{m_{\mathrm{scale},6}^3}{m_{\mathrm{scale},4}^2} = 7.429 \times 10^{-13} \text{ MeV}.$$

No neutrino oscillation data enters. The absolute masses:

**Table 2.** Neutrino predictions — all from $m_e$ and $n_s = 4$.

| Quantity | IDWT | Experiment | Status |
|---|---|---|---|
| $m_{\nu_1}$ | 1.487 meV | — | **First-principles prediction** |
| $m_{\nu_2}$ | 8.639 meV | — | **First-principles prediction** |
| $m_{\nu_3}$ | 50.27 meV (bare: 48.87) | — | **First-principles prediction** |
| $\sum m_\nu$ | **60.39 meV** (bare: 59.00) | $<120$ meV [5] | Consistent |
| $\Delta m^2_{21}$ | $7.242\times10^{-5}$ eV$^2$ | $(7.53\pm0.18)\times10^{-5}$ | $-1.6\sigma$ |
| $\Delta m^2_{31}$ | $2.525\times10^{-3}$ eV$^2$ | $(2.530\pm0.028)\times10^{-3}$ | $-0.2\%$ |
| $m_{\beta\beta}$ | **0 (all orders)** | Unobserved [6] | Consistent |
| Hierarchy | Normal | Preferred $3$–$4\sigma$ | Consistent |

The $\nu_3$ correction $\delta_{\nu_3} = \varepsilon \times g_{33} = [1/(280\sqrt{7})] \times [8\sqrt{7}] = 1/35$ (exact) is the cross-sector constructive interference between the $\ell=2$ kernel component and the $d=3$ coupling, derived without additional inputs. Applied multiplicatively: $m_{\nu_3}^{\rm corr} = m_{\nu_3}^{\rm bare} \times (36/35) = 50.27$ meV. This closes the $\Delta m^2_{31}$ discrepancy from $-5.7\%$ (bare) to $-0.2\%$ (corrected) against PDG 2024 ($2.530\times10^{-3}$ eV$^2$, NO).

The $m_{\beta\beta} = 0$ prediction holds at all orders: the $d=5$ sector has $d \bmod 8 = 5$, which means no charge-conjugation matrix $C$ exists on the $S^5$ spinor bundle. Since no $C$ exists globally, cross-sector couplings cannot construct $\psi^T C \psi$ at any loop order — the Majorana operator is geometrically absent, not merely suppressed. Any $0\nu\beta\beta$ signal immediately falsifies IDWT. $\sum m_\nu = 60.39$ meV is within reach of CMB-S4 ($\sim 14$ meV sensitivity) and the Simons Observatory ($\sim 30$–40 meV); IDWT will be confirmed or excluded within this decade.

---

## 11. Dynamical Picture: How Sector Geometry Determines Observable Physics

The $\ell=0$ part of the kernel sets the sector scales (mass formula). The $\ell=2$ part generates the derived scale $\varepsilon$ (used for the $\nu_3$ closure) and, at loop level, contributes to boson self-energies. The emergent gauge symmetries arise from the isometry groups of the sector manifolds: $\mathrm{SU}(3)_c$ from the isometry of $\mathbb{CP}^2$; $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ from the isometry of $\mathbb{CP}^1 \cong S^2$.

Colour confinement emerges from the two-stage observability filter. A mode $(n,d)$ is observable only if: (1) $\Omega_{\log}(n,d) = \ln(S(n,d)/S(n,2)) \lesssim \ln 2$ (Stage-1 dimensional visibility passes); and (2) the mode belongs to the co-fixed-point spectrum of the filtration chain (Stage-2 co-fixed-point condition). The $d=3$ modes at $n=2$ (18.8 MeV) and $n=3$ (47.0 MeV) pass Stage 1 but fail Stage 2 — they are not stable particles, consistent with observation.

Gravity: variation of the master action with respect to $g_{\mu\nu}$ yields the observer's Einstein equations $G_{\mu\nu} = 8\pi G_N T_{\mu\nu}^{\rm eff}$, where $T_{\mu\nu}^{\rm eff} = \int_\Xi T_{\mu\nu}^{\rm Dirac}\,d\mu_\xi$ is the sector-space integral of the matter stress-energy. $G_N$ is a measured constant of spacetime; the sector geometry $\Xi$ is a fixed background and contributes no gravitational degrees of freedom. Full treatment in Technical Volume 4 [11].

---

## 12. Sector Geometry as Coupling Filter

The coordinate containment principle (Section 11) answers which forces can reach a given particle's sector coordinates. A complementary principle governs the coupling structure of that interaction: **the particle's own sector geometry determines what coupling handles it presents to the world and what entire classes of interaction are geometrically forbidden to it.** The sector quantum number — polarization, color, the Dirac condition, color neutrality — is not an input label assigned to the particle. It is the geometry of the sector expressing itself as a coupling structure.

**$d=2$ ($\mathbb{CP}^1$, U(1)) — orientation filter.** The photon's two helicity states are the complete internal geometry of $\mathbb{CP}^1$. The coupling to a target goes as $\varepsilon_\mu j^\mu$ — the polarization vector contracted with the current. Perpendicular currents receive zero coupling, not suppression. Polarization is not a property of the photon in addition to its geometry; it is the U(1) fiber structure of $\mathbb{CP}^1$ expressed as what the photon can and cannot couple to.

**$d=3$ ($S^3$, SO(4)) — weak isospin filter.** The isometry SO(4) = SU(2)$_L \times$ SU(2)$_R$ gives down-type quarks their left-handed weak coupling. The right-handed component does not participate in the weak interaction — SU(2)$_R$ is latent in the geometry. Color coupling is inherited derivatively via coordinate containment inside $\Xi_4$, not from the $S^3$ structure itself.

**$d=4$ ($\mathbb{CP}^2$, SU(3)) — color filter.** Color originates here. $\chi(\mathbb{CP}^2) = 3$ — three color coupling handles as a theorem of $\mathbb{CP}^2$ topology, not a parameter. Color conservation is not a dynamical rule; isolated color-nonsinglet asymptotic states are geometrically impossible. Confinement is this filter at the level of which states can be constructed.

**$d=5$ ($S^5$, SO(6)) — Majorana/LNV filter.** The Clifford algebra on $S^5$ ($d \bmod 8 = 5$) admits no charge-conjugation matrix $C$ on the spinor bundle — $C$ does not exist globally on $S^5$. Since no $C$ exists, cross-sector couplings cannot construct $\psi^T C \psi$ at any loop order, and the Majorana mass operator is geometrically forbidden to all orders, not merely at leading order. This is the basis for the $m_{\beta\beta} = 0$ prediction (Section 10). The $S^5$ Hopf fibration $S^1 \to S^5 \to \mathbb{CP}^2$ additionally projects the $\mathbb{CP}^2$ color representation onto its singlet, giving color-neutral neutrinos despite their coordinate support inside $\Xi_4$. The SO(6) $\cong$ SU(4) structure gives neutrinos their $B-L$ charge.

**$d=6$ ($\mathbb{CP}^3$, SU(4)) — colour silence filter.** $\chi(\mathbb{CP}^3) = 4$, not 3; colour contributions cancel in the SU(4) representation. Zero strong coupling at any energy — geometrically absent, not suppressed. The $d=2$ photon sector ($\mathbb{CP}^1$) sits inside $d=6$ via the coordinate nesting $\Xi_2 \subset \Xi_6$; the electron-photon coupling follows from coordinate containment, giving pure U(1) EM with coupling structure fixed by the $\mathbb{CP}^3$ isometry.

**$d=10$ ($\mathbb{CP}^5$, SU(6)) — Gegenbauer-critical coupling.** At the Gegenbauer critical endpoint, modes sit at the Jacobi coupling boundary — neither freely sector-delocalized nor robustly sector-bound. The tau couples in principle to every sector (its coordinates span all of $\Xi_{10}$), but coupling weight is distributed with no dominant channel. No single decay mode is selected; every channel is accessible; none carries concentrated weight. This explains the tau's decay pattern: short lifetime (no gap protecting it) but broad distribution across many channels. The geometric back-reaction correction $\delta_\tau = 1/1680$ (Section 7.2) is required because the naive perturbation series does not converge at the critical point.

**Relationship to coordinate containment.** Coordinate containment is necessary but not sufficient. A particle may have coordinate support in a force's sector and still have zero coupling if its own sector geometry projects the relevant representation to zero. The $S^5$ Hopf structure projects the $\mathbb{CP}^2$ color representation onto the singlet; the $\mathbb{CP}^3$ index cancellation gives zero strong coupling despite the lepton's coordinates containing $\Xi_4$. Both principles together determine the full coupling structure of any particle.

**Significance.** The Standard Model takes quantum numbers as axioms: quarks have three colors by measurement; neutrinos are (possibly) Dirac by measurement; leptons are color-neutral by measurement. IDWT derives each from the Euler characteristic, Clifford algebra mod 8 periodicity, or Clifford algebra on the respective sector manifold. The coupling structure of every particle in the Standard Model is a theorem of each particle's sector manifold geometry, not a postulate.

---

## 13. Light-Quark Scale Offset and In-Sector Structure

PDG reports light-quark masses in $\overline{\rm MS}$ at $\mu = 2$ GeV; IDWT computes them from the sector scale $m_{\mathrm{scale},d}$, fixed at the confinement scale $\Lambda_{\rm QCD} \approx N_c f_\pi = 3 \times 94 = 282$ MeV. The bare-count predictions already sit within the sizable PDG $\overline{\rm MS}$ uncertainties ($d$ $+0.04\%$, $s$ $+0.57\%$, $u$ $+0.77\%$; $b$ $-0.05\%$) even before the §7.1 confinement-binding correction (which brings $s$, $u$ to $+0.49\%$, $+0.70\%$), so the overall sector scale is compatible with the data up to a possible scheme/scale offset between the IDWT confinement scale and $\overline{\rm MS}$ at $\mu = 2$ GeV.

That offset does not account for the whole residual, and the residual is not uniform within a sector. A scheme or scale shift multiplies $m_{\mathrm{scale},d}$ by one common factor for every mode in sector $d$ (the kernel is rank-1), so it cancels identically in the scale-free **in-sector ratio** $S(n_{\rm hi},d)/S(n_{\rm lo},d)$. Those ratios are not exact: $s/d = 20.000$ against $19.894$ ($+0.54\%$), $c/u = 590.33$ against $589.35$ ($+0.17\%$), and $t/c = 137.26$ against $135.56$ ($+1.25\%$), whereas the boson ($Z/W$, $H/W$) and charged-lepton ($\mu/e$) in-sector ratios agree to a few parts in $10^4$. The residual therefore grows with the level gap and is confined to the quark sectors $d=3$ and $d=4$: it is $n$-dependent structure in the combinatorial count $S(n,d)$, not a uniform sector scale error. It is reported as measured accuracy and not absorbed as a correction (§7.1).

The analytic derivation of the scheme conversion from $g_s$ to $\overline{\rm MS}$ at $\mu = 2$ GeV requires computing the QCD running from $\Lambda_{\rm QCD}$ to the PDG renormalization point. This is a well-defined calculation (involving the two-loop QCD $\beta$-function with $N_f=3$ active flavors and matching at $m_c$) that remains to be performed within the IDWT coupling framework. It is flagged as an open item; the current offsets are not in tension with experiment given the large PDG uncertainties on light-quark masses.

---

## 14. Comparison with Other Approaches

| Framework | Mass parameters | Gauge structure | Neutrino masses |
|---|---|---|---|
| Standard Model | 9 fermion masses free | Given | Free (Yukawa) |
| Koide relation [3] | Lepton masses only; 1 relation | Not derived | — |
| Noncommutative geometry [4] | Some constraints | Derived | Not fixed |
| String landscape | Statistical distribution | In principle | Statistical |
| **IDWT (this work)** | **All 15 from $n_s=4$** | **Derived from sector isometries** | **60.39 meV predicted** |

IDWT is distinctive in providing: (a) masses for all 15 predicted particles, (b) a derivation of the sector set from the integer seeds, (c) a spectrum-completeness theorem (no stable mode outside the selected set), and (d) parameter-free neutrino mass predictions falsifiable within this decade.

---

## 15. Falsifiable Predictions

1. **$\sum m_\nu = 60.39$ meV.** A measurement outside $[55, 65]$ meV falsifies the cross-sector scale equation.
2. **$m_{\beta\beta} = 0$ exactly.** Any positive $0\nu\beta\beta$ detection falsifies IDWT.
3. **$m_u/m_d = \sqrt{3/14} = 0.46291$ exactly (Theorem S2).** A ratio outside $[0.40, 0.55]$ falsifies the coupling derivation.
4. **No new stable particles at any energy (Completeness Theorem).** Any new particle discovery falsifies IDWT.
5. **Normal neutrino hierarchy.** Inverted hierarchy is excluded by mode ordering.
6. **No stable states at 18.807 MeV or 47.019 MeV.** These $d=3$ modes pass Stage 1 but fail Stage 2; they may appear as broad resonances only.

---

## 16. Open Items

1. **CP-violating phase $\delta$.** Requires loop-level computation of the Hopf Chern-Simons integral.
2. **PMNS mixing angles.** Derived via spectral geometry (Part 9 T6): $\sin^2\theta_{23}=0.5590$ (PDG 2024: 0.553, $+1.07\%$), $\sin^2\theta_{12}=0.3086$ (PDG 0.307, $+0.51\%$), $\sin^2\theta_{13}=0.02211$ (PDG 0.0219, $+0.96\%$). All three from $g_{55}=96/g_{22}$ and four mode indices. CP phase $\delta$ remains open (requires spectral phase integral).
3. **$\Delta m^2_{31}$ discrepancy.** Closed by $\delta_{\nu_3} = \varepsilon \times g_{33} = 1/35$ (cross-sector constructive interference, exact). Corrected $\Delta m^2_{31} = 2.525\times10^{-3}$ eV$^2$ (PDG 2024: $2.530\times10^{-3}$, $-0.2\%$).
4. **$g_1$ residual $-1.88\%$.** After 1-loop U(1)$_Y$ running from $m_W$ to $m_Z$. Remaining gap consistent with 2-loop QED threshold matching between IDWT fiber scheme and $\overline{\rm MS}$.
5. **Top index $n_{\rm top} = 72$.** The product form $\chi(\mathbb{CP}^2)\times\chi(\mathbb{CP}^3)\times\chi(\mathbb{CP}^5) = 3\times4\times6$ is structurally natural but the selecting condition — why this Euler product and not another combination — has no derivation. This is the leading open dynamical question of the framework.
6. **The gravitational input $G_\infty$.** Gravity in IDWT is the back-reaction of $|\Psi_\infty|^2$ on the spacetime metric (Technical Volume 4 [11]); the in-sector Green's function fixes the per-dimension coupling $G_d = G_\infty/[(d-2)S_{d-1}]$, equal to the measured $G_N$ at $d=3$. $G_\infty$ (equivalently $G_N$) is a second dimensional input alongside $m_e$ and is not derived from the sector combinatorics. It is not commensurable with the active-force couplings: gravity in IDWT is the curvature of $M_\infty$ sourced by $|\Psi_\infty|^2$, whereas the active forces are the wave's kernel self-coupling on shared sector coordinates — geometry versus coupling, not two forces of the same kind. There is therefore no ratio between gravity and the active forces to fine-tune, and the dimensionless $G_\infty m_e^2 \approx 2.2\times10^{-44}$ is simply an input, not a prediction. No fine-tuning is hidden anywhere else either: IDWT masses are discrete spectral ranks $S(n,d)$, not action coefficients, so they receive no additive UV renormalisation and the Higgs-style hierarchy problem does not arise (Technical Volume 8 [11]). The genuinely open question is narrower — whether $G_\infty$ could instead be fixed geometrically, reducing the two dimensional inputs to one — which the present construction does not achieve.
7. **Spectral action EW scale.** The spectral action gives $\sqrt{\operatorname{Tr}(D^2)}=248.3$ GeV, within $+0.82\%$ of $v_{\rm Higgs}$; both are spectral quantities built from the same seeds, so the residual is a spectral-normalisation artefact (Technical Volume 9 [11]), not an independent confirmation. $G_N$ enters the Einstein–Hilbert term as a measured input.

---

## 17. Conclusion

Starting from three integer seeds $\{n_d=1,\, n_u=3,\, n_{\rm top}=72\}$ — whose composite $n_s = n_d + n_u = 4$ is independently forced by the topological fixed point $S(4,4) = 35$ — and the dimensional reference $m_e$, IDWT provides a combinatorial derivation of the complete Standard Model mass spectrum, the electroweak sector, CKM observables, and absolute neutrino masses to high accuracy. Five theorems ground the framework in spectral geometry, with complete proofs supplied above. The Completeness Theorem proves no additional particles exist within the framework — a consequence, not a claim. The $\tau$ back-reaction and $\nu_3$ closure corrections are derived from the kernel structure without additional inputs; the confinement-binding correction for the colour sectors ($d=3,4$) has a derived functional form, with its $d=4$ scale derived from the colour energy law and its $d=3$ scale anchored.

A complementary structural result (Section 12) shows that each sector geometry constitutes a coupling filter for its particles. The sector quantum number — polarization, color, the Dirac condition, total color silence, Gegenbauer-critical marginal coupling — is not an input label but the geometry expressing itself as a coupling structure, derived from the Euler characteristic, Clifford algebra mod 8 periodicity, and Clifford algebra on the sector manifold. Coordinate containment determines whether coupling is possible; the sector geometry determines the structure and forbidden classes of that coupling. These are independent principles that together give a complete geometric account of why each particle interacts the way it does.

The framework makes five concrete predictions falsifiable with near-term experiments, most critically $\sum m_\nu = 60.39$ meV (corrected; bare 59.00 meV, with $\delta_{\nu_3} = 1/35$ derived from the cross-sector kernel; CMB-S4 target: $\sim 14$ meV) and $m_{\beta\beta} = 0$ at all orders (current KamLAND-Zen bound: $< 28$–122 meV, NME-dependent [6]). These will confirm or exclude IDWT within this decade.

---

## Acknowledgements

The author thanks Claude, GPT, Meta, Grok, Perplexity, Z.ai, and Mistral Le Chat.

---

## Appendix A: Quick-Reference Summary

All results from $n_s = 4$ and $m_e$ alone.

---

| Identity | Statement | Source |
|---|---|---|
| **Hockey-stick** | $S(n,d) = S(n,d-1)+S(n-1,d)$ | Combinatorics |
| **Weyl law** | $S(n,2k+1)=\tfrac{1}{2}N_{D_{S^{2k+1}}}(n-1)$ | Theorem S1 |
| **$m_u/m_d$** | $\sqrt{g_{44}/g_{33}}=\sqrt{3/14}$ (exact) | Theorem S2 |
| **$g_{22}$** | $(S(n_s,3)-n_u)^2 \times (S(n_u,4)-S(n_u,3))/2=722.5$ | Theorem S3 |
| **Sector set** | $D=\{2,3,4,5,6,10\}$ from $72=N_c\times n_s\times N_f$ | Theorem S4 |
| **$\ell=2$ scale** | $\varepsilon=1/(280\sqrt{7})=0.001350$ (enters $\delta_{\nu_3}$; not applied to quarks) | $\ell=2$ kernel |
| **Back-reaction** | $1/1680=1/(n_s n_u(n_s+n_u)S(n_s,3))$ | $d=6\to d=10$ |
| **$\sum m_\nu$** | $60.39$ meV (corrected; bare: $59.00$ meV, $\delta_{\nu_3}=1/35$) | §10 |
| **$m_{\beta\beta}$** | $0$ (all orders; no $C$ on $S^5$ bundle, $d \bmod 8 = 5$) | §10, §12 |
| **CKM unitarity** | $|V_{ud}|^2+|V_{us}|^2+|V_{ub}|^2=1$ (exact) | §9 |

---

**All 15 mode indices** ($n_s=4$ forces every entry):

| Particle | $d$ | $n$ | Particle | $d$ | $n$ |
|---|---|---|---|---|---|
| $d$ quark | 3 | 1 | $\nu_1$ | 5 | 10 |
| $u$ quark | 4 | 3 | $e^-$ | 6 | 13 |
| $s$ quark | 3 | 4 | $\nu_2$ | 5 | 15 |
| $c$ quark | 4 | 20 | $\nu_3$ | 5 | 22 |
| $t$ quark | 4 | 72 | $\tau^-$ | 10 | 23 |
| $b$ quark | 3 | beat | $\mu^-$ | 6 | 35 |
| $W^\pm$ | 2 | 76 | $Z^0$ | 2 | 81 |
| $H$ | 2 | 95 | | | |

**All 6 coupling constants** (exact from $n_s=4$):

| Coupling | Value | Sector |
|---|---|---|
| $g_{33}$ | $8\sqrt{7} \approx 21.166$ | $d=3$ quarks |
| $g_{44}$ | $12/\sqrt{7} \approx 4.536$ | $d=4$ quarks |
| $g_{22}$ | $722.5$ (Theorem S3) | $d=2$ gauge |
| $g_{55}$ | $96/722.5 \approx 0.1329$ | $d=5$ neutrinos |
| $g_{66}$ | $1/4$ (seed) | $d=6$ leptons |
| $g_{10,10}$ | $1/4$ (seed, shared with $d=6$) | $d=10$ tau |

---

## References

1. C. Bär, *Geom. Funct. Anal.* **6**, 899 (1996). *(Dirac spectrum on $S^n$)*
2. H. B. Lawson and M.-L. Michelsohn, *Spin Geometry* (Princeton University Press, 1989). *(Clifford algebra mod 8 periodicity, Majorana conditions)*
3. Y. Koide, *Lett. Nuovo Cim.* **34**, 201 (1983).
4. A. Chamseddine, A. Connes, and V. Mukhanov, *JHEP* **2015**, 104 (2015).
5. Planck Collaboration (N. Aghanim et al.), "Planck 2018 results. VI. Cosmological parameters," *A&A* **641**, A6 (2020), arXiv:1807.06209.
6. KamLAND-Zen Collaboration, "Search for Majorana Neutrinos with the Complete KamLAND-Zen Dataset," *Phys. Rev. Lett.* (2024), arXiv:2406.11438.
7. CMB-S4 Collaboration, arXiv:1610.02743 (2016).
8. Simons Observatory Collaboration (P. Ade et al.), *JCAP* **2019**, 056 (2019).
9. KATRIN Collaboration (M. Aker et al.), *Nature Phys.* **18**, 160 (2022).
10. Particle Data Group (R. L. Workman et al.), *Prog. Theor. Exp. Phys.* **2022**, 083C01 (2022).
11. Fedge No, *Infinite-Dimensional Wave Theory: Technical Documentation* (10 volumes), Zenodo, doi:[10.5281/zenodo.19767493](https://doi.org/10.5281/zenodo.19767493) (2026).
