# Infinite Dimensional Wave Theory, Second Edition — Part 2: Mass

## 1. Mass is a count

Part 1 established that a particle is a standing wave in a sector well and that its mass is the eigenvalue of that standing wave. This Part states what the eigenvalue is and confronts it with every measured mass.

The energy of the $n$-th standing wave in a $d$-dimensional well equals the *number of distinct configurations* available to the wave up to that level — the count of ways to distribute the excitation among the $d$ directions, accumulated from the ground state up:

$$m = m_{\mathrm{scale},d} \times S(n,d), \qquad S(n,d) = \binom{n+d-1}{d}.$$

$S(n,d)$ is the cumulative state count of a $d$-dimensional oscillator through level $n-1$. The physical statement is that a mode's resonant frequency — its mass — equals the total number of sector states beneath it. Heavier particles are not "more excited" in some vague sense; they sit atop literally more configurations of their sector's geometry. The mass spectrum is a census.

One identity does most of the work in this Part. The count obeys Pascal's recursion,

$$S(n,d) = S(n,d-1) + S(n-1,d),$$

which says a state count in $d$ dimensions splits exactly into the count one dimension down plus the count one level down. Because the sectors are physically nested (Part 1), this arithmetic identity becomes physical machinery: it relates state counts *between* sectors, and the particle spectrum turns out to be threaded on it.

## 2. Two integers and one mass

The entire spectrum is generated from a remarkably small basement:

- **The ground seed, $n_d = 1$.** Every sector's first mode has exactly one configuration, $S(1,d) = 1$, in every dimension. The down quark is this universal ground state, sitting in the $d=3$ well.
- **The geometric seed, $n_u = 3$.** The up quark's index is the number of independent colour classes of the $d=4$ geometry — the same three-ness that makes three colours (Part 1). Their sum $n_s = 4$ (the strange quark) is independently confirmed by the four-class structure of the lepton sector's geometry.
- **One reference mass, the electron's**, $m_e = 0.511$ MeV, which sets the unit.

From the two seed integers, the wave's self-coupling strength in each sector is fixed — the $d=3$ and $d=4$ couplings by seed algebra, the lepton coupling by the four-class geometry of $\mathbb{CP}^3$ ($g_{66} = 1/n_s$), the electroweak coupling by a state count across the quark sectors, and the neutrino coupling by the Hopf relation tying $S^5$ to $\mathbb{CP}^2$ with nothing left to choose. The six sector frequency units $m_{\mathrm{scale},d}$ then all follow from $m_e$ through those couplings. No quark, boson, or neutrino mass is an input anywhere in the chain.

The neutrino scale deserves its own sentence, because it answers a famous puzzle without new machinery. The $d=5$ sector has no self-coupling of its own (its sphere has no complex structure and no group structure to close on); its scale is fixed by a consistency condition linking it to the quark and lepton sectors, and that condition puts it at $7.4\times10^{-13}$ MeV. Neutrinos are light not because of a see-saw with hidden heavy partners but because their sector's well is shallow — a depth set by the same coupling chain as everything else.

## 3. The spectrum

Fifteen particles, one reference mass, two seed integers. The masses below are the physical predictions (three carry the derived corrections of Section 5); comparisons are against PDG 2024.

| Particle | Sector $d$ | Mode $n$ | Predicted | Measured | Error |
|---|---|---|---|---|---|
| electron | 6 | 13 | 0.51100 MeV | 0.51100 MeV | unit reference |
| muon | 6 | 35 | 105.657 MeV | 105.658 MeV | $-0.001\%$ |
| tau | 10 | 23 | 1776.84 MeV | 1776.93 MeV | $-1.0\sigma$ |
| down | 3 | 1 | 4.702 MeV | $\sim$4.70 MeV | $+0.04\%$ |
| strange | 3 | 4 | 93.96 MeV | 93.5 MeV | $+0.49\%$ |
| bottom | 3 | beat at $k_0{=}16$ | 4181 MeV | 4183 MeV | $-0.05\%$ |
| up | 4 | 3 | 2.175 MeV | 2.16 MeV | $+0.70\%$ |
| charm | 4 | 20 | 1277.3 MeV | 1273.0 MeV | $+0.34\%$ |
| top | 4 | 72 | 172.50 GeV | 172.57 GeV | $-0.04\%$ |
| $\nu_1$ | 5 | 10 | 1.487 meV | — | below current bounds |
| $\nu_2$ | 5 | 15 | 8.639 meV | — | below current bounds |
| $\nu_3$ | 5 | 22 | 50.27 meV | — | below current bounds |
| photon | 2 | 0 | 0 | 0 | exact |
| W | 2 | 76 | 80.379 GeV | 80.369 GeV | $+0.012\%$ |
| Z | 2 | 81 | 91.230 GeV | 91.188 GeV | $+0.05\%$ |
| Higgs | 2 | 95 | 125.27 GeV | 125.20 GeV | $+0.05\%$ |

The masses span from milli-electronvolts to hundreds of GeV — fourteen orders of magnitude — on one unit and two integers. The famous ratios come out as pure counts: $m_\mu/m_e = S(35,6)/S(13,6) = 206.765$ against the measured $206.768$; $m_Z/m_W = S(81,2)/S(76,2) = 1.13500$ against $1.13461 \pm 0.00019$.

Honesty about the residuals, in both directions. The Z prediction sits $+0.05\%$ (42 MeV) above a measurement good to 2 MeV — a small but genuine overshoot with no scale freedom to absorb it, since the electroweak unit is an exact multiple of $m_e$; the scale-free ratio $m_Z/m_W$ is clean at the $2\sigma$ level. The heavy-quark comparisons are scheme-sensitive: charm, bottom, and top masses differ by several percent between the standard definitions, so their sub-percent residuals should be read against that spread, not against statistical error bars alone — which cuts both ways, softening both the agreement and any tension. The most solid comparisons are the scale-independent ratios, and there the pattern is sharp: boson and lepton in-sector ratios match to a few parts in $10^4$, while quark ratios carry small residuals that grow with level separation — real structure, diagnosed in Section 5.

The neutrino masses are predictions in waiting: $\Sigma m_\nu = 60.4$ meV is within reach of upcoming cosmological surveys, and the ordering is necessarily normal ($m_{\nu_1} < m_{\nu_2} < m_{\nu_3}$), because the count $S(n,5)$ only grows — an inverted ordering is impossible here, and experiments currently prefer normal at $3$–$4\sigma$. One tension is on the books and not explained away: the predicted solar mass-squared splitting sits $3.8\%$ ($1.6\sigma$) below the current central value, with no correction available in the structure — either a mechanism is missing or the measured central value moves.

## 4. Why the spectrum hangs together

The mode indices are not fifteen independent numbers. They are threaded on the counting identity and on a handful of physical joins, and the cross-bracing is the point: the same integers keep arriving from different directions.

**Generation two is a theorem.** Pascal's recursion evaluated at the muon's site reads $S(4,4) = S(4,3) + S(3,4)$, i.e. $35 = 20 + 15$: the muon's index *is* the charm index plus the second neutrino's index, because the counting identity demands it at that node. Given the seeds, no freedom exists there.

**The neutrino family is the seed seen through two sectors.** The first neutrino is the up seed's state count in $d=3$ ($S(3,3)=10$), the second is the same seed's count in $d=4$ ($S(3,4)=15$), and the third combines both images with the shared seed removed once ($10+15-3 = 22$) — inclusion–exclusion, forced because both images grow from the same $n_u$ and their overlap must not be counted twice. Leaving out that subtraction would push the summed neutrino mass to $\approx 98$ meV, which cosmology already excludes.

**The charged leptons ride the quark tower.** Electron $13 = 10 + 3$, muon $35 = 20 + 15$, tau $23 = 22 + 1$: each generation's lepton index is a neutrino index plus a quark index. Only the muon's is a pure Pascal node; the electron's and tau's are additive joins whose full dynamical derivation is open (Section 7).

**The bosons cascade from the top.** $n_W = 76$, $n_Z = 81$, and the W–Z gap of $5$ is the same combinatorial quantity that appears inside the electroweak coupling itself — the mass gap and the coupling constant come from one number. The Higgs closes at $n_H = 95 = 3+20+72$, the sum of the three up-type indices — an exact closure whose mechanism is still open.

## 5. Three physical corrections, none fitted

Three particles' masses carry corrections beyond the bare count, and each correction is a physical mechanism with a derived, parameter-free size.

**The tau feels its own echo ($+1/1680$).** The tau's sector and the electron-muon sector share exactly the same coupling strength — the wave cannot tell them apart by coupling, only by geometry. Because of this, the perturbation the lepton sector exerts on the tau feeds back through the tau's own identical coupling, echo upon echo, a geometric series that sums to a factor $4/3$ on the leading perturbation of $1/2240$. Total: $1/1680$, every factor a seed quantity. It moves the tau from $0.06\%$ low to $-1.0\sigma$ — inside the error bar of one of the most precisely measured masses in physics.

**The third neutrino counts one overlap constructively ($+1/35$).** The third neutrino is the one mode built from both sector images of the seed (Section 4), and the two images interfere constructively where they overlap, raising the count by exactly one part in $35$ — an exact algebraic consequence of independently derived couplings, in which the irrational factors cancel and a pure ratio survives. With it, the predicted atmospheric splitting matches oscillation data within $0.2\sigma$. The deeper operator-level reason the overlap enters with precisely this product is not yet derived, and this correction is the least settled of the three.

**Quarks weigh less than their count because confinement keeps part of the energy ($-x_e\langle k\rangle$).** The bare count is the mass a quark would have as a free object — and a quark is never free. Part of the counted energy is locked in the colour field that confines it, and the observed inertial mass is lower by that binding share, which grows linearly with how much of the well the mode occupies. The coefficient is derived from the confinement scale (itself derived — Part 3), applies universally to the two colour-carrying sectors with no per-quark freedom, and touches nothing else. Its effect is decisive exactly where it should be: the bare counts overshoot by an amount that *grows with mode index* (up $+0.8\%$, charm $+0.9\%$, top $+2.2\%$) — a shape no scale error can produce, but exactly the shape of level-dependent binding — and the correction flattens all five quarks to within $1\sigma$. The heaviest quark, where the binding bite is largest, lands at $-0.04\%$.

## 6. The two quarks that break the pattern — and why

Thirteen particles sit on the counting tower. Two do not, and both have physical stories.

**The bottom quark is a beat.** At one site in the $d=3$ sector — $k_0 = 16$, and only there — three independent seed conditions coincide, and the wave cannot settle on a single level: it resonates between adjacent modes $16$ and $17$ with equal weight, the way two nearly matched frequencies produce a beat. The resulting mass is the geometric mean of the two levels, $m_b = \sqrt{S(16,3)\,S(17,3)}\times m_{\mathrm{scale},3} = 4181$ MeV, within $0.05\%$ of measurement. An exhaustive search finds no other site in any sector where the coincidence recurs: the spectrum contains exactly one beat particle, and nature has exactly one quark that fits no clean level.

**The top quark is a seed, not an output.** Its index $72$ is the product of the class counts of the three complex sectors — $3\times4\times6$, the same integers that count colours, generations, and flavours — but this product is a closed form for the value, not yet a mechanism selecting it. The framework is honest here: $72$ enters as a third seed. There is a candidate physical account of why the spectrum tops out where it does — the electroweak sector behaves as a fixed total capacity, $\sum_i (m_i/v)^2 \le 1$, which the four heaviest particles exactly saturate, leaving a small measured deficit that no admissible sixteenth mode could fill — and on that reading the heavy indices sit at a subscription boundary rather than at arbitrary sites. That account is developed with the open problems (Part 6), not claimed as settled physics.

## 7. Composites: hadrons from the same counts

The framework's masses are for the fifteen fundamental standing waves; hadrons are bound composites. But the same derived quantities — quark masses, the confinement scale $\Lambda$, the pion decay constant, $N_c = 3$ — assemble into composite masses with no new inputs.

The cleanest is the nucleon: $m_N = N_c\Lambda + m_s = 940$ MeV ($+0.2\%$), the proton as three colour bonds' worth of confinement energy plus, remarkably, the strange quark mass — forced by an exact seed identity, not inserted. Replacing a light quark by a strange one in a baryon adds the mass difference once per remaining colour bond, which prices the $\Lambda$, $\Xi$ octet members to within about a percent. Light mesons follow the chiral square-root law with a derived condensate parameter (pion $-0.2\%$); heavy mesons add a binding energy that is the geometric mean of the heavy mass and the confinement scale (B mesons and bottomonium all within $0.2\%$). And the $d=3$ well itself supports short-lived resonance levels between the stable modes: the $\rho$ meson lands at level $9$ within $0.1\%$ — confirmed independently by a filter computation using only coupling constants, with no mass input at all.

## 8. Could this be luck?

The mass law invites an obvious objection: with enough integers, something always fits. The framework's answer is quantitative. Take the seven scale-independent mass ratios the theory pins with no adjustable anything, and ask how often random integer assignments in the same combinatorial setting do as well. The answer, computed exactly: the joint agreement has probability about $4\times10^{-10}$ — six standard deviations — and in a million random seed-pair spectra, none reproduces the observed pattern; the best random attempt falls short of the actual spectrum's likelihood by more than thirty log-units. The complete protocol, both null models, and every number are in the first-edition record, reproducible by running `files/idwt.py`. Whatever this spectrum is, it is not the kind of agreement random integers produce.

## 9. What Part 2 leaves open

Stated as physics, not bookkeeping. Why the top's index is $72$ — the capacity-saturation reading would make it the last index the electroweak budget admits, but the saturation mechanism itself is not derived. Why the electron's join fires at $13$ — the addition is exact, the dynamical selection of that edge is not. What mechanism underlies the Higgs closure at the sum of the up-type indices. The deeper operator origin of the third neutrino's $1/35$. The solar-splitting $1.6\sigma$ tension. And beneath all of these, the same foundation question flagged in Part 1: deriving from the equation of motion *why these levels fire* rather than verifying that the closed rule reproducing them has no rival.

What is not open is the shape of the result. One reference mass, two seed integers, and a counting identity reproduce every measured fundamental mass to sub-percent accuracy, predict the neutrino masses and ordering outright, and price the hadrons on the side. If mass is a count of sector configurations, all of this is what it should look like — and nothing in the measured spectrum says otherwise.

---

*Second edition, 2026. Derivations and numerical verification: first-edition Part 2, Part 5, Appendix C, and `files/idwt.py` at https://fedgeno.github.io/.*
