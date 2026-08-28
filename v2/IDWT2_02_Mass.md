# Infinite Dimensional Wave Theory, Second Edition — Part 2: Mass

## 0. What this Part teaches

By the end of this Part you can compute every fundamental particle mass yourself, from four ingredients:

1. **The counting function** $S(n,d)$ — pure combinatorics (§1).
2. **The six sector couplings** $g_{dd}$ — closed forms derived from the sector geometry (§2).
3. **The sector mass units** $m_{{\rm scale},d}$ — all fixed by the couplings and one reference mass, the electron's (§3).
4. **The occupied levels** $n$ — fifteen measured integers, the framework's quantum-number assignments (§4).

Then three particles carry physically-derived corrections (§5), two quarks have special structure (§6), and the same ingredients price the hadrons (§8). Throughout, the occupied levels themselves are treated as what they are: *observed facts*, like the principal quantum numbers a spectroscopist assigns to atomic lines. They display remarkable arithmetic relationships, which §7 reports as findings. Why nature occupies these levels and not others is a mystery this edition does not pretend to solve.

---

## 1. The counting function

### 1.1 Mass is a count of configurations

Part 1 derived the setting: each particle is a standing wave in a $d$-dimensional harmonic well that the wave's own self-coupling digs, and its mass is the eigenvalue of that standing wave, read by a three-dimensional observer as an inertial constant. The content of the mass law is *what the eigenvalue is*:

$$\boxed{\,m = m_{{\rm scale},d}\times S(n,d), \qquad S(n,d) = \binom{n+d-1}{d}\,}$$

$S(n,d)$ is the total number of states of the $d$-dimensional well below level $n$. To see this, count one level at a time. Level $k$ of a $d$-dimensional harmonic oscillator holds one state for every way to distribute $k$ excitation quanta among $d$ directions — stars and bars: arrange $k$ stars and $d-1$ bars, $\binom{k+d-1}{d-1}$ arrangements. Then sum levels $0$ through $n-1$; the sum telescopes by the hockey-stick identity of Pascal's triangle:

$$\sum_{k=0}^{n-1}\binom{k+d-1}{d-1} = \binom{n+d-1}{d} = S(n,d).$$

So a mode's frequency — its mass — equals the cumulative census of sector configurations beneath it. A heavier particle literally sits atop more ways for its sector to vibrate. That is the whole physical content: **mass is an integrated density of states.**

### 1.2 The counts you will need

For hand computation, the polynomial forms:

$$S(n,2) = \tfrac{n(n+1)}{2}, \quad S(n,3) = \tfrac{n(n+1)(n+2)}{6}, \quad S(n,4) = \tfrac{n(n+1)(n+2)(n+3)}{24},$$

and so on ($d$ ascending factors over $d!$). The values at the occupied levels:

| sector | level $n$ | $S(n,d)$ | particle |
|---|---|---|---|
| $d=3$ | 1 | 1 | down |
| $d=3$ | 4 | 20 | strange |
| $d=4$ | 3 | 15 | up |
| $d=4$ | 20 | 8 855 | charm |
| $d=4$ | 72 | 1 215 450 | top |
| $d=5$ | 10 | 2 002 | $\nu_1$ |
| $d=5$ | 15 | 11 628 | $\nu_2$ |
| $d=5$ | 22 | 65 780 | $\nu_3$ |
| $d=6$ | 13 | 18 564 | electron |
| $d=6$ | 35 | 3 838 380 | muon |
| $d=10$ | 23 | 64 512 240 | tau |
| $d=2$ | 0 | 0 | photon |
| $d=2$ | 76 | 2 926 | W |
| $d=2$ | 81 | 3 321 | Z |
| $d=2$ | 95 | 4 560 | Higgs |

(The bottom quark is the one entry with no single level — it is a *beat* between levels 16 and 17 of $d=3$; §6.1.)

Check one yourself: $S(4,3) = \binom{6}{3} = 20$, or level by level, $1+3+6+10 = 20$. Everything below is this table times a unit.

---

## 2. The six couplings

The couplings $g_{dd}$ set the well depths (Part 1 §1.3) and, through them, the mass units. None is fitted to a mass. Each is a closed form in two small integers of the sector geometry — the colour count $N_c = \chi(\mathbb{CP}^2) = 3$ and the lepton class count $\chi(\mathbb{CP}^3) = 4$ — which we abbreviate throughout as $a = 3$ and $b = 4$ (with $a + b = 7$ recurring under square roots).

### 2.1 The quark-sector couplings

The $d=3$ and $d=4$ couplings come from one kernel self-consistency structure evaluated at the two quark geometries. The structure has two pieces:

*A universal coefficient.* The kernel's self-consistency eigenvalue at the two quark sectors is the ratio of the Casimir-type factor to the state count one dimension up, and it is the *same* number for both sectors:

$$g_{\rm coeff} = \sqrt{\frac{b(b+1)}{S(b,4)}} = \sqrt{\frac{20}{35}} = \frac{2}{\sqrt7} \;=\; \sqrt{\frac{a(a+1)}{S(a,5)}} = \sqrt{\frac{12}{21}} = \frac{2}{\sqrt7}.$$

(The equality is the binomial symmetry $\binom{6}{4} = \binom{6}{2}$ — a two-line check.)

*A per-sector gap.* The $d=3$ gap is $b^2 = 16$ (the same site $k_0 = 16$ that is Gegenbauer-critical in Part 1 §3.3 and hosts the bottom beat in §6.1); the $d=4$ gap is the harmonic mean of the two integers, $2ab/(a+b) = 24/7$ — the natural effective gap when two boundary conditions act at once.

Coupling = gap over coefficient:

$$g_{33} = \frac{b^2}{2/\sqrt7} = \frac{b^2\sqrt{a+b}}{2} = 8\sqrt7 \approx 21.17, \qquad g_{44} = \frac{24/7}{2/\sqrt7} = \frac{ab}{\sqrt{a+b}} = \frac{12}{\sqrt7} \approx 4.536.$$

Two consequences worth pausing on. First, the product is clean, $g_{33}\,g_{44} = ab^3/2 = 96$, so the rank-1 cross-coupling (Part 1 §1.2) is $g_{34} = \sqrt{g_{33}g_{44}} = \sqrt{96} = 4\sqrt6$. Second — and this is a genuine physical prediction with *no mass input* — the ratio of the two lightest quarks' masses is fixed by the couplings alone (§3.2 shows why):

$$\frac{m_u}{m_d} = \sqrt{\frac{g_{44}}{g_{33}}} = \sqrt{\frac{12/\sqrt7}{8\sqrt7}} = \sqrt{\frac{3}{14}} = 0.4629 \qquad (\text{PDG: } 0.462).$$

### 2.2 The lepton-sector couplings

The $d=6$ coupling is read off the lepton geometry two independent ways, both giving the same number: the class count, $g_{66} = 1/\chi(\mathbb{CP}^3) = 1/4$; and the minimum sectional curvature of $\mathbb{CP}^3$ with its natural (Fubini–Study) metric, which is exactly $1/4$ — the unique curvature scale invariant under the sector's full isometry group. So

$$g_{66} = \tfrac14.$$

The $d=10$ sector shares it: $g_{10,10} = g_{66} = 1/4$. Both are complex-projective geometries whose coupling is set by the same class-count structure, and the kernel *cannot distinguish them* — a genuine degeneracy with two consequences we will use: the muon–tau mass difference is pure geometry (different $S(n,d)$, identical coupling), and the tau's mass correction (§5.1) resums through its own coupling.

### 2.3 The electroweak coupling

$$g_{22} = \frac{p^2\,q}{2} = \frac{17^2\times 5}{2} = 722.5,$$

where $p = S(4,3) - 3 = 17$ and $q = S(3,4) - S(3,3) = 15 - 10 = 5$ are state counts: $p$ is the number of $d=3$ eigenstates at the strange level not already spoken for by the up-quark boundary, $q$ is the $d=4$ state increment at the up level (an instance of the hockey-stick identity: $S(n,4) - S(n,3) = S(n-1,4)$, here $S(2,4) = 5$). The kernel is a two-body coupling, so the two $d=3$ legs enter squared and the single $d=4$ leg linearly; the $1/2$ is the exchange symmetry of the two-body kernel. Honesty about status: this is a *state count* — the same counting currency as the mass law itself, and empirically exact through everything it feeds (the W, Z, Higgs masses of §4) — but unlike §2.1 it is not yet derived from an operator; it is counting that works, reported as such.

The number $q = 5$ makes a second, independent appearance below ($n_Z - n_W = 5$, §7), one of the cross-bracings that make the structure hard to dismiss as arbitrary.

### 2.4 The neutrino coupling is forced, not chosen

The two $U(1)$ Hopf fibrations of Part 1 §3.1 share the *same* circle fiber: $S^1\to S^3\to\mathbb{CP}^1$ and $S^1\to S^5\to\mathbb{CP}^2$. Universality of that shared fiber demands the ratio of total-space coupling to base coupling be the same on both:

$$\frac{v_3}{v_2} = \frac{v_5}{v_4} \;\Longrightarrow\; g_{25} = g_{34} \;\Longrightarrow\; g_{55} = \frac{g_{33}\,g_{44}}{g_{22}} = \frac{96}{722.5} = 0.1329.$$

No freedom remains: the neutrino sector's coupling is an output of the three couplings already built. (Check: $v_3/v_2 = v_5/v_4 = 0.1712$, and $g_{25} = g_{34} = 4\sqrt6$ both ways.)

**The coupling algebra is now closed.** Six couplings, five distinct values, every one a closed form in $a=3$ and $b=4$ — and every cross-coupling follows from rank-1 as $g_{dd'} = \sqrt{g_{dd}\,g_{d'd'}}$.

---

## 3. The mass units: one reference, one rule

### 3.1 The fixed-point rule

The kernel vacuum gives one equilibrium condition that applies to every sector uniformly: *the squared mass of the lightest occupied mode in sector $d$ equals $(g_{dd}/g_{66})\times m_e^2$.* Physically — the lightest tenant of each well sits at the depth its coupling ratio to the reference (lepton) sector dictates. Since the lightest occupied mode has mass $m_{{\rm scale},d}\times S(n_{\min},d)$:

$$m_{{\rm scale},d} = \frac{m_e\,\sqrt{g_{dd}/g_{66}}}{S(n_{\min}(d),\,d)}.$$

One measured mass enters the entire framework here: $m_e = 0.511$ MeV. (Any of the fifteen could serve as the unit; the electron is chosen because it is measured to $3\times10^{-10}$.)

### 3.2 Working the units

**$d=6$:** the electron *is* the reference: $m_{{\rm scale},6} = m_e/S(13,6) = 0.511/18\,564 = 2.7526\times10^{-5}$ MeV.

**$d=10$:** shares the $d=6$ coupling (§2.2), hence the same unit: $m_{{\rm scale},10} = m_{{\rm scale},6}$.

**$d=3$:** lightest occupant is the down quark at $n=1$, $S(1,3)=1$:

$$m_{{\rm scale},3} = m_e\sqrt{\frac{8\sqrt7}{1/4}} = 0.511\times\sqrt{84.66} = 4.702 \text{ MeV}.$$

And because $S(1,3) = 1$, this *is* the down quark's mass: $m_d = 4.702$ MeV (PDG $\approx 4.70$; $+0.04\%$) — a parameter-free output, the first mass the machinery produces.

**$d=4$:** lightest occupant is the up quark at $n=3$, $S(3,4)=15$:

$$m_{{\rm scale},4} = \frac{m_e\sqrt{g_{44}/g_{66}}}{15} = \frac{0.511\times\sqrt{18.14}}{15} = 0.1451 \text{ MeV}.$$

(Dividing the up-quark fixed-point mass by 15 rather than 1 is the same rule applied to a sector whose floor is not $n=1$; and the ratio of the two floors is the coupling-only prediction $m_u/m_d = \sqrt{g_{44}/g_{33}}$ quoted in §2.1.)

**$d=2$:** $m_{{\rm scale},2} = m_e\sqrt{g_{22}/g_{66}} = 0.511\times\sqrt{2890} = 27.47$ MeV.

**$d=5$ — why neutrinos are so light.** The neutrino sector has no self-closure of its own — $S^5$ is neither a complex geometry nor a group, so there is no internal structure for its coupling to close on (this is the same geometric loneliness that makes neutrinos Dirac and nearly non-interacting; Part 3). Its scale is fixed instead by a three-sector consistency condition along the Hopf chain that ties it to the quark sector above it and the lepton sector beside it:

$$m_{{\rm scale},5}\times m_{{\rm scale},4}^2 = \frac{a}{b}\,m_{{\rm scale},6}^3 \;\Longrightarrow\; m_{{\rm scale},5} = \frac{3}{4}\times\frac{(2.7526\times10^{-5})^3}{(0.1451)^2} = 7.43\times10^{-13}\text{ MeV}.$$

Read the structure of that fraction: the *heavy* quark unit appears squared in the denominator, the *tiny* lepton unit cubed in the numerator, so the neutrino unit comes out thirteen orders below the electron's — with no see-saw, no heavy partner, no suppression mechanism invented for the purpose. Neutrinos are light because their well is shallow, and their well is shallow because their sector borrows its scale through the fibration rather than owning one.

---

## 4. Computing the spectrum

Now everything is a multiplication. The recipe: look up $S(n,d)$ (§1.2), multiply by the sector unit (§3.2), apply a correction if the particle is one of the three that carry one (§5).

Worked examples across the range:

- **Muon:** $m_\mu = m_e\times S(35,6)/S(13,6) = 0.511\times 3\,838\,380/18\,564$. The ratio reduces exactly: $206.7647$. Measured: $206.7683$ — agreement to $2\times10^{-5}$.
- **W boson:** $m_W = 27.47\times S(76,2) = 27.47\times 2926 = 80\,379$ MeV. Measured: $80\,369\pm13$ ($+0.012\%$).
- **$\nu_2$:** $m_{\nu_2} = 7.43\times10^{-13}\times 11\,628 = 8.64$ meV.
- **Tau (with its §5 correction):** $m_\tau = m_e\times\frac{S(23,10)}{S(13,6)}\times\bigl(1+\tfrac{1}{1680}\bigr) = 1776.84$ MeV. Measured: $1776.93\pm0.09$ ($-1.0\sigma$).

The complete table, with the §5 corrections applied where marked:

| particle | computation | predicted | measured (PDG 2024) | error |
|---|---|---|---|---|
| electron | reference | 0.51100 MeV | 0.51100 MeV | — |
| muon | $m_e\,S(35,6)/S(13,6)$ | 105.657 MeV | 105.658 MeV | $-0.001\%$ |
| tau | ratio $\times(1+1/1680)$ ★ | 1776.84 MeV | 1776.93 MeV | $-1.0\sigma$ |
| down | $4.702\times1$ | 4.702 MeV | $\sim$4.70 MeV | $+0.04\%$ |
| strange | $4.702\times20$, confinement ★ | 93.96 MeV | 93.5 MeV | $+0.49\%$ |
| bottom | beat, §6.1 | 4181 MeV | 4183 MeV | $-0.05\%$ |
| up | $0.1451\times15$, confinement ★ | 2.175 MeV | 2.16 MeV | $+0.70\%$ |
| charm | $0.1451\times8855$, confinement ★ | 1277.3 MeV | 1273.0 MeV | $+0.34\%$ |
| top | $0.1451\times1\,215\,450$, confinement ★ | 172.50 GeV | 172.57 GeV | $-0.04\%$ |
| $\nu_1$ | $7.43\times10^{-13}\times2002$ | 1.487 meV | — | below bounds |
| $\nu_2$ | $\times\,11\,628$ | 8.639 meV | — | below bounds |
| $\nu_3$ | $\times\,65\,780\times(36/35)$ ★ | 50.27 meV | — | below bounds |
| photon | $27.47\times0$ | 0 | 0 | exact |
| W | $27.47\times2926$ | 80.379 GeV | 80.369 GeV | $+0.012\%$ |
| Z | $27.47\times3321$ | 91.230 GeV | 91.188 GeV | $+0.05\%$ |
| Higgs | $27.47\times4560$ | 125.27 GeV | 125.20 GeV | $+0.05\%$ |

Fourteen orders of magnitude, one reference mass, two geometric integers. The neutrino entries are outright predictions: $\Sigma m_\nu = 60.4$ meV awaits the next generation of cosmological surveys, and the ordering is *necessarily* normal, because $S(n,5)$ only grows — an inverted hierarchy cannot be written in this framework at all.

**Honesty in both directions.** The Z sits $+0.05\%$ (42 MeV) above a measurement good to 2 MeV — a genuine overshoot with no scale freedom to hide in, since the unit is an exact multiple of $m_e$; the scale-free ratio $m_Z/m_W = 3321/2926 = 1.13500$ against the measured $1.13461\pm0.00019$ is the cleaner comparison ($\approx2\sigma$). Heavy-quark masses are scheme-dependent at the several-percent level (pole vs $\overline{\rm MS}$), so charm/bottom/top residuals should be read against that spread, not statistical bars — which softens both the agreements and the tensions. The sharpest tests are the scale-free in-sector ratios, and they carry a diagnostic: boson and lepton ratios match to a few parts in $10^4$, while quark ratios show small residuals *growing with level separation* — not a scale error (a scale error cancels in ratios), but real level-dependent structure. §5.3 identifies it: confinement.

---

## 5. Three corrections, three mechanisms

Exactly three particles deviate from the bare count, each for a stated physical reason with a derived, parameter-free size. No other particle is corrected, and no correction has a knob.

### 5.1 The tau hears its own echo: $+1/1680$

The tau's sector and the electron–muon sector carry *identical* coupling $1/4$ (§2.2) — the kernel cannot tell them apart. So when the lepton sector perturbs the tau, the shift feeds back through the tau's own equal coupling, and that echo echoes. The leading perturbation of the $d{=}6\to d{=}10$ coupling at the tau's site is

$$\varepsilon = \frac{1}{b^3\times S(b,4)} = \frac{1}{64\times35} = \frac{1}{2240},$$

($b^3 = 64$ the resonance volume at the critical site, $S(4,4)=35$ the frequency normalization — the muon's own count). The self-feedback is a geometric series in $g_{10,10} = 1/4$:

$$\Delta m = \varepsilon\,m_\tau + g_{10,10}\Delta m \;\Longrightarrow\; \Delta m = \frac{\varepsilon\,m_\tau}{1-\tfrac14} = \varepsilon\,m_\tau\times\frac{4}{3}.$$

Total: $\frac{1}{2240}\times\frac43 = \frac{1}{1680}$. Every factor is one of the two geometry integers or a count built from them. Applied, the tau moves from $0.06\%$ low to $-1.0\sigma$ — inside the error bar of one of the most precisely measured masses in physics. This correction exists *only* for the tau because only the tau sits at the critical endpoint sharing its perturber's coupling; for the electron and muon there is no second sector to echo through.

### 5.2 The third neutrino's overlap: $+1/35$

The three neutrino levels are not structurally alike, and the difference is physical. §7 records the observed relations: $\nu_1$ and $\nu_2$ sit at levels that are single-sector counts, while $\nu_3$'s level combines *both* — it is the one neutrino whose structure draws on the $d=3$ and $d=4$ images simultaneously. Where the two images overlap they interfere constructively, raising the effective count by one part in

$$\frac{1}{S(4,4)} = \frac{1}{35}:$$

$m_{\nu_3} \to m_{\nu_3}\times\frac{36}{35} = 50.27$ meV. The size is an exact algebraic consequence of quantities derived above — the interference amplitude is the product $\varepsilon_{\ell=2}\times g_{33}$, where $\varepsilon_{\ell=2} = g_{\rm coeff}/(16\times35) = 1/(280\sqrt7)$ is the kernel's tensor-channel scale, and the irrationals cancel exactly: $\frac{1}{280\sqrt7}\times 8\sqrt7 = \frac{8}{280} = \frac{1}{35}$. With it, the implied atmospheric splitting $\Delta m^2_{31} = 2.525\times10^{-3}$ eV$^2$ matches oscillation data within $0.2\sigma$. Candor: of the three corrections this one's mechanism is the least deeply derived — the algebra is exact and the inputs independent, but *why* the overlap enters with precisely this product awaits a deeper account, and we say so rather than paper over it.

### 5.3 Quarks weigh less than their count: confinement binding

The bare count prices a *free* quark — and a quark is never free. Part of the counted energy is locked in the colour field that confines it; the observed inertial mass is lower by that locked share. The deficit per state grows linearly with how much of the well the mode occupies, measured by the mean occupied level

$$\langle k\rangle = \frac{d\,(n-1)}{d+1} \quad(\text{exact for the harmonic well}),$$

so

$$M_{\rm phys} = M_{\rm bare}\,\bigl(1 - x_e\,\langle k\rangle\bigr).$$

The coefficient is derived, not fitted, from the confinement scale itself. With $\Lambda = N_c f_\pi = 282$ MeV (both factors derived in §8.1), the condensate occupation of the colour well is $N_b = \Lambda/(4\,m_{{\rm scale},4}) = 486$, and

$$x_e = \frac{3}{16\,N_b} = 3.86\times10^{-4},$$

applied *universally* to the two colour-carrying sectors $d=3,4$ — the $d=3$ quarks inherit their colour from $d=4$ through the fibration, so the per-state deficit is the same one number. Lepton and boson wells are effectively harmonic (no colour condensate) and are untouched.

The shape is the diagnostic that convicts. The bare overshoots grow with level — up $+0.77\%$, charm $+0.93\%$, top $+2.20\%$ — exactly the signature of level-dependent binding and impossible for any scale error. Worked for the top: $\langle k\rangle = 4\times71/5 = 56.8$, deficit $= 3.86\times10^{-4}\times56.8 = 2.19\%$, so $172{,}500$ MeV from a bare $176{,}365$ — landing at $-0.04\%$ of the measured value. All five singly-counted quarks come within $1\sigma$:

| quark | bare error | corrected error |
|---|---|---|
| down | $+0.04\%$ | $+0.04\%$ ($\langle k\rangle = 0$: the ground state pays nothing) |
| strange | $+0.57\%$ | $+0.49\%$ |
| up | $+0.77\%$ | $+0.70\%$ |
| charm | $+0.93\%$ | $+0.34\%$ |
| top | $+2.20\%$ | $-0.04\%$ |

The physics in one sentence: a confined quark's missing percent is not an error in the count — it is the energy the colour field keeps.

---

## 6. The two quarks that break the pattern

### 6.1 The bottom quark is a beat

At exactly one site in the $d=3$ well — level 16 — the wave cannot settle on a single level. Three independent conditions coincide there (§7 lists them among the found relationships: $16 = 4^2 = 13+3 = 20-4$), and at the coincidence the kernel drives levels 16 and 17 with equal weight. Two equally driven adjacent modes do what two nearly matched frequencies always do: they beat. The sustained object is the two-mode resonance, and its mass is the *geometric* mean of the two levels — the kernel's cross-term is a product of the two energies (dimension energy-squared), so the resonance sits at its square root:

$$m_b = \sqrt{S(16,3)\times S(17,3)}\times m_{{\rm scale},3} = \sqrt{816\times969}\times4.702 = 4181 \text{ MeV},$$

against the measured $4183\pm7$ ($-0.05\%$). An exhaustive search finds no second site in any sector where the triple coincidence recurs: the framework contains exactly one beat particle, and nature has exactly one quark that fits no clean level. The remaining openness is stated plainly: the *site* is exact arithmetic and the geometric mean has the dimensional argument above, but a full dynamical account of the two-mode beat is not in hand.

### 6.2 The top quark's level is measured, and remarkable

The top sits at level 72 of the colour sector. We do not derive that integer. What we found, and report as a finding: $72 = 3\times4\times6$ — the product of the class counts of the three complex matter geometries, the same integers that count colours, lepton classes, and flavours ($\chi(\mathbb{CP}^2)\,\chi(\mathbb{CP}^3)\,\chi(\mathbb{CP}^5)$). It is a beautiful identity and it may well be a clue; it is not a derivation, and this edition declines to dress it as one. Given the level, the mass follows from the ordinary recipe with the §5.3 correction — and lands at $-0.04\%$.

---

## 7. The index relationships — reported, not built on

The fifteen occupied levels satisfy a web of exact arithmetic relations. We record them because they are true, verified, and striking; we build nothing on them, and the selection of the levels remains, in this edition, an open mystery.

- $n_\mu = 35 = 20 + 15 = n_c + n_{\nu_2}$ — and this one is a Pascal node of the counting function itself: $S(4,4) = S(4,3) + S(3,4)$.
- $n_e = 13 = 10 + 3 = n_{\nu_1} + n_u$.
- $n_\tau = 23 = 22 + 1 = n_{\nu_3} + n_d$; also $23 = n_c + n_u$.
- $n_{\nu_3} = 22 = 10 + 15 - 3 = n_{\nu_1} + n_{\nu_2} - n_u$ (an inclusion–exclusion shape; without the $-3$, the summed neutrino mass would be $\approx98$ meV, which cosmology excludes — the shape, at least, is doing physical work in §5.2).
- $n_{\nu_1} = 10 = S(3,3)$ and $n_{\nu_2} = 15 = S(3,4)$: the two lighter neutrino levels are themselves counting-function values at the up level.
- $n_H = 95 = 3 + 20 + 72$: the Higgs level is the sum of the three up-type levels. Equivalently $95 = 1 + 13 + 81 = n_d + n_e + n_Z$.
- $n_Z - n_W = 81 - 76 = 5 = q$ — the same state-count $q$ inside $g_{22} = p^2q/2$ (§2.3): the W–Z gap and the electroweak coupling share one integer.
- The beat site three ways: $16 = 4^2 = n_e + n_u = S(4,3) - S(2,3)$.
- $n_{\rm top} = 72 = \chi(\mathbb{CP}^2)\,\chi(\mathbb{CP}^3)\,\chi(\mathbb{CP}^5)$ (§6.2); and $n_u = 3 = \chi(\mathbb{CP}^2)$: the up level equals the colour count.

Some of these may be numerology; some may be the visible edge of the real selection mechanism. The framework's own history includes elaborate attempts to promote this web into a generative derivation of the spectrum, and this edition deliberately omits them: a pattern among numbers we do not understand is a finding, not a foundation. What can be said with statistical force is only that the *masses* built on these levels are not a lucky fit — §9.

---

## 8. The same ingredients price the hadrons

Hadrons are composites — bound assemblies of quark modes, with no levels of their own — but the quantities derived above assemble into their masses with no new inputs.

### 8.1 The confinement scale

The effective coupling felt by a $d=3$ mode is the sector coupling diluted over its states, $g_{\rm eff}(n) = g_{33}/S(n,3)$ — this is the framework's substitute for running couplings (nothing runs; couplings dilute over configurations). It crosses unity between levels: $g_{\rm eff}(4) = 21.17/20 = 1.06$ (confined), $g_{\rm eff}(5) = 0.60$ (free). The confinement scale is the mass at the crossing level:

$$f_\pi = m_{{\rm scale},3}\times S(4,3) = 4.702\times20 = 94.0 \text{ MeV} \quad(\text{measured } 92.1,\ +2.1\%),$$

$$\Lambda = N_c\times f_\pi = 282 \text{ MeV}.$$

### 8.2 The nucleon

$$m_N = N_c\,\Lambda + m_s = 3\times282.1 + 94.0 = 940.4 \text{ MeV} \quad(\text{measured } 938.9,\ +0.2\%).$$

Three colour bonds' worth of confinement energy — plus, remarkably, one strange-quark mass, which enters through an exact identity of the derived quantities ($N_c\Lambda/n_u^2 = m_s$, both sides $94.0$ MeV), not by insertion. Replacing a light quark by a strange one in a baryon adds the mass difference once per remaining colour bond ($N_c - 1 = 2$): the $\Lambda$ baryon at $m_N + 2(m_s - m_d) = 1119$ MeV ($+0.3\%$), the $\Xi$ at $1303$ MeV ($-1\%$).

### 8.3 Mesons, light and heavy

Light pseudoscalars follow the chiral square-root law with a condensate parameter built entirely from §8.1: $m^2 = (m_{q_1}+m_{q_2})\,B_0$, $B_0 = \Lambda\,S(4,3)/2 = 2821$ MeV. The pion: $\sqrt{(4.702+2.175)\times2821} = 139.3$ MeV (measured $139.6$, $-0.2\%$); the $D_s$ lands at $0.0\%$; the kaon's $+5.5\%$ is the expected leading-order chiral error. Heavy mesons bind by the geometric mean of the heavy mass and the confinement scale: $E_{\rm bind} = \sqrt{m_b\Lambda} = 1086$ MeV puts every B meson and the $\Upsilon(1S)$ within $0.2\%$. And the $d=3$ well's own resonance levels between the stable quarks show up as the short-lived vector mesons: level 9 gives the $\rho$ at $S(9,3)\times m_{{\rm scale},3} = 165\times4.702 = 776$ MeV (measured $775.3$) — confirmed independently by an interference computation using only the couplings, with no mass input at all.

---

## 9. Could this be luck?

A mass formula built from integers invites the objection that integers are flexible. The answer is quantitative, and the reader should know its shape.

First, the structure has no continuous dial: the sector units are chained to $m_e$ (§3), so predicting a mass means choosing an integer on a *fixed* ladder whose rungs are far apart — adjacent levels differ by $\sim17\%$ at the muon and $\sim43\%$ at the tau. Landing within $2\times10^{-5}$ of a measured ratio on a $17\%$ grid is not generic; it is one chance in several thousand, per quantity.

Second, the joint test. Take the seven dimensionless, parameter-free ratios whose measurements resolve the grid (a selection rule fixed in advance, not by closeness): $m_\mu/m_e$, $m_\tau/m_e$, $m_Z/m_W$, $m_H/m_W$, $\sin\theta_C$, $m_t/m_c$, and the neutrino splitting ratio. Score each by how lucky a random placement would need to be, and combine. The joint probability that random level assignments do this well: $4\times10^{-10}$ — six standard deviations — by exact computation, $2\times10^{-7}$ under the most conservative treatment. Third, the brute-force version: draw entire random spectra (every level random in its allowed window) a million times and score them against the same data. None matches; the best random spectrum falls short of the actual one by more than thirty log-likelihood units. The complete protocol is in the archive and reruns from a fixed seed in `files/idwt.py`.

Whatever the fifteen integers mean, the masses hanging on them are not the kind of agreement random integers produce.

---

## 10. What this Part leaves open

Stated as mysteries, without scaffolding. *Why these fifteen levels* — the central one; this edition treats the levels as measured. *Why the top's level is $72$* — the triple-product identity is a finding, not an answer. *The bottom beat's dynamics* — site exact, mechanism sketched, full derivation open. *The deeper origin of the $1/35$* (§5.2). *The Higgs level's sum rule* — found, unexplained. *The solar splitting* — the predicted $\Delta m^2_{21}$ sits $1.6\sigma$ low with no correction available in the structure; either something is missing or the measured central value moves. *The Z's $+0.05\%$* — a real residual, stated. None of these gaps touches the calculational content of this Part: every number above follows from the recipe as shown, and the reader now owns the recipe.

---

*Second edition, 2026. Full derivations and machine verification: first-edition Parts 2, 5, 8 and `files/idwt.py` at https://fedgeno.github.io/.*
