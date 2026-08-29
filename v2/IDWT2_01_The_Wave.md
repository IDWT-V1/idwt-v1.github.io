# Infinite Dimensional Wave Theory, Second Edition — Part 1: The Wave

## 0. What this edition is

This is a restatement of Infinite Dimensional Wave Theory organized around a single question asked of every claim: *is this a physical phenomenon that could actually be happening?* Everything in these pages passed that test, and everything is developed far enough to follow on the page — the mechanisms, the formulas, and the key derivations are carried in the text, so that no prior document is required. The first-edition Parts 1–11 remain the archive of full rigor, complete status accounting, and numerical verification; where a derivation here is a sketch, the archive holds the whole proof.

The second edition carries no status symbols. What is included is included because the physics is sound enough to state; where a result rests on an open premise, the prose says so, in place.

---

## 1. One wave on one manifold

### 1.1 The ontology

There is one physical object: a complex Dirac spinor wave $\Psi_\infty$ on a manifold

$$M_\infty = \mathbb{R}_t \times \Xi_\infty,$$

where $\mathbb{R}_t$ is a single time direction and $\Xi_\infty$ is a purely spatial manifold with infinitely many dimensions. The wave interacts with nothing but itself. Every particle, force, quantum number, and observation — including the observer — is a feature of this one wave's geometry and self-interaction.

Three commitments are packed into that sentence, and each is load-bearing.

**The dimensions are ordinary, flat, and infinite in extent.** Nothing is compactified, rolled up, or small. Each spatial direction of $\Xi_\infty$ is as large and as flat as the three we occupy. What distinguishes dimensions from one another is not size but whether the wave can *bind* there — whether its self-interaction supports stable localized standing waves at that dimension count. Where geometry labels like $S^3$ or $\mathbb{CP}^2$ appear below, they describe the local symmetry of a bound standing wave near its center — the way a hydrogen ground state has spherical symmetry although the electron roams all of flat infinite $\mathbb{R}^3$ — never the global topology, which is flat $\mathbb{R}^d$ throughout.

**There is exactly one time.** $M_\infty$ has Lorentzian signature $(1,\infty)$: one negative metric eigenvalue from $\mathbb{R}_t$, countably many positive ones from $\Xi_\infty$. The Dirac operator on $M_\infty$ is

$$D = \gamma^0\partial_t + \sum_i \gamma^i \partial_{\xi^i},$$

with a single timelike Clifford generator $\gamma^0$. Every particle in every sector ages by this one clock. A "six-dimensional electron" means six *spatial* dimensions plus the shared time — never a separate $6{+}1$ spacetime. This is what keeps causality ordinary in a universe of many large spatial dimensions: there are no extra timelike directions to support closed timelike curves or competing causal orders, because the causal structure is everywhere set by the one $\mathbb{R}_t$.

**The wave is a classical field.** $\Psi_\infty$ is a deterministic complex spinor field — not a quantum wavefunction, not an element of Fock space. There is no second quantization and no imported Born-rule postulate; the probabilistic appearance of the quantum world is *derived* in §5 from the wave's own conservation law and self-coupling. "Infinite-dimensional" always means the manifold's spatial dimensions, never a Hilbert space.

### 1.2 The action

Everything below follows from one action functional, varied with respect to the wave. Writing $x$ for the observable coordinates and $\xi$ for the sector coordinates, with $P_d$ the projector onto the $d$-dimensional sector subspace $\Xi_d$:

$$S_{\rm IDWT} = \int \bar\Psi_\infty\bigl(i\Gamma^\mu\nabla_\mu + i\Gamma^a\partial_a\bigr)\Psi_\infty \;+\; \frac{1}{2}\sum_{d,d'} g_{dd'}\!\int (\xi_d\cdot\xi_{d'})^2\,\bigl[\bar\Psi_\infty P_d\Psi_\infty\bigr]\bigl[\bar\Psi_\infty P_{d'}\Psi_\infty\bigr].$$

The first term is free Dirac propagation over all of $M_\infty$. The second — the **kernel** — is the wave's entire interaction content: a quartic, density-against-density self-coupling on the sector coordinates. Two facts about its form matter.

*The angular factor is forced.* $(\xi_d\cdot\xi_{d'})^2$ is the unique leading interaction invariant under independent rotations of the two sectors ($U(d)\times U(d')$): the inner product is the only invariant of a pair of directions, its first power is odd and integrates away against isotropic densities, and the square is the lowest surviving term. The kernel is not a modeling choice among many — it is the first thing symmetry permits.

*The coupling matrix is rank-1.* The coupling strengths factorize, $g_{dd'} = v_d\,v_{d'}$, an outer product of one coupling vector. The physical reason: if the matrix had rank two or more, the mean field would carry two or more independent condensates, entangling the sectors and destroying the sector-by-sector separability that the mass law (§2) requires. Rank-1 is the unique structure for which one common condensate $C(x) = \sum_{d'} v_{d'}\langle\xi_{d'}\rangle$ serves every sector, letting each sector see a clean local well. Two corollaries come free: the coupling matrix has exactly one nonzero eigenvalue — the wave has a *single* collective interaction channel, and every cross-sector coupling is a projection of that one channel (this returns with force in Parts 2 and 6); and the kernel energy is a sum of squares, hence non-negative — self-interaction only ever costs energy, so it penalizes configurations and never destabilizes a mode from below.

The six sector self-couplings $g_{dd}$ are not free parameters; they are closed-form expressions in two small integers of the sector geometry — the colour count $3$ and the lepton class count $4$ — and Part 2 derives them. For orientation, the values that will be built there:

| $d$ | 2 | 3 | 4 | 5 | 6 | 10 |
|---|---|---|---|---|---|---|
| $g_{dd}$ | $722.5$ | $8\sqrt7 \approx 21.2$ | $12/\sqrt7 \approx 4.54$ | $96/722.5 \approx 0.133$ | $1/4$ | $1/4$ |

### 1.3 How the wave digs its own wells

Vary the action and the equation of motion is a nonlinear Dirac equation: the free operator plus the kernel acting back on the wave through the sector density it itself creates. In the mean-field step — replacing the density in the kernel by its expectation — the self-coupling becomes a potential. Watch it become *harmonic*, exactly.

For a mode localized in sector $d$, the self-term of the kernel gives the effective potential

$$V_{\rm self}(\xi_d) = g_{dd}\int |\chi_d(\xi')|^2\,(\xi_d\cdot\xi')^2\,d\mu_{\xi'},$$

the wave's density $|\chi_d|^2$ integrated against the kernel's angular factor. Now use the one identity that drives this whole section: for any direction average over an isotropic density,

$$\bigl\langle(\xi_d\cdot\xi')^2\bigr\rangle_{\rm angles} = \frac{|\xi_d|^2\,|\xi'|^2}{d}.$$

This is not a near-origin approximation — it is the exact $\ell=0$ projection of the quadratic kernel, valid for all $\xi_d$; the traceless $\ell=2$ remainder averages to zero against any isotropic density. Substituting,

$$V_{\rm self}(r) = \lambda_d\,r^2, \qquad \lambda_d = g_{dd}\,\frac{\langle r'^2\rangle_d}{d},$$

with $r = |\xi_d|$: a pure harmonic well, derived, not assumed. And the loop closes on itself. The mode $\chi_d$ that sources the well is the ground state *of* the well, and a $d$-dimensional harmonic ground state with stiffness $\lambda_d$ has mean-square radius $\langle r^2\rangle_d = d/(2\sqrt{\lambda_d})$. Substituting back:

$$\lambda_d = \frac{g_{dd}}{2\sqrt{\lambda_d}} \;\Longrightarrow\; \lambda_d^{3/2} = \frac{g_{dd}}{2} \;\Longrightarrow\; \boxed{\lambda_d = \left(\frac{g_{dd}}{2}\right)^{2/3}}$$

The well depth is fixed by the self-coupling alone — a soap-bubble equilibrium: the wave shapes the well, the well shapes the wave, and the fixed point of that loop is the sector's vacuum structure. The resulting numbers:

| $d$ | $g_{dd}$ | $\lambda_d = (g_{dd}/2)^{2/3}$ | ground energy $E_0 = d\sqrt{\lambda_d}$ | width $L_d = \lambda_d^{-1/4}$ |
|---|---|---|---|---|
| 2 | 722.5 | 50.72 | 14.24 | 0.375 |
| 3 | $8\sqrt7$ | 4.820 | 6.586 | 0.675 |
| 4 | $12/\sqrt7$ | 1.726 | 5.255 | 0.872 |
| 5 | 0.133 | 0.164 | 2.025 | 1.571 |
| 6 | 1/4 | 0.250 | 3.000 | 1.414 |
| 10 | 1/4 | 0.250 | 5.000 | 1.414 |

Three consequences of the harmonic form, each doing real work later:

- **The spectrum is purely discrete.** The potential grows without bound, so there is no continuum: no freely propagating sector modes exist, every physical mode is a normalizable bound state with Gaussian tails $\sim e^{-\sqrt{\lambda_d}\,r^2/2}$. (This is why, in Part 4, no experiment sees anything "leaking" into the sector dimensions — there is nothing plane-wave-like there to leak.)
- **The well travels with the mode.** The self-coupling is evaluated about the mode's own centroid — the well is the mode's self-binding, in the mode's frame. Nothing anchors the centroid to any origin (an anchored reading would pin every particle to a point of space and obliterate atomic physics), so the centroid propagates freely with $E^2 = P^2 + m^2$ while the internal structure stays bound. "Bound" always means *bound about its own center*.
- **The amplitude of one excitation is fixed, not free.** Writing the conserved charge $Q = \int|\Psi|^2$ explicitly, the well condition becomes $\lambda_d(Q) = (g_{dd}Q/2)^{2/3}$; the derivation above is exactly the $Q=1$ case. One quantum of excitation has a definite height. This innocuous-looking fact is the seed of the quantum of action, taken up in Part 5.

### 1.4 Nothing bounds the wave: a particle is a centered ripple pattern

The word "well" above earns a caution, because it suggests a container — and there is no container. The well *is* the wave's own self-coupling evaluated on its own density; it exists because the pattern does, not before it. The honest ontology is this: **a particle is a standing wave with a center, rippling outward from that center like the surface of a lake around a struck point, its intensity thinning with distance — self-sustained by its own interference, bounded by nothing.**

Read the mode functions and that is literally what they say. Every mode extends to infinity — nowhere is its amplitude exactly zero. The ground mode of a sector is the no-ripple case: a single central swell dying off smoothly. The excited modes genuinely ripple: their radial profiles oscillate under the decaying envelope, so a mode at level $n$ is a central peak surrounded by concentric rings of intensity — crests and nodes, a frozen circular wave pattern around the center. (These rings are physical structure, and Part 5 will use them: the "ring with a dot" of the higher s orbitals is this ripple structure showing through.) The particle does not *stop* anywhere; it fades — steeply near its own scale, but never to zero, and in the dimensions beyond its sector it does not fade at all (§4).

Discreteness then needs no walls. An unbounded self-interfering wave still supports only a discrete set of patterns — the ones whose ripples close the self-interference loop, reinforcing rather than canceling — the way a soliton or a whispering-gallery mode is discrete without any box. That is what the eigenvalue condition of §1.3 *is*: a resonance condition on self-sustaining patterns. The count $S(n,d)$ of §2 counts self-consistent ripple patterns, and mass — the pattern's pitch — is quantized because self-reinforcement is a closure condition, not because anything confines the wave. "Bound state" everywhere in this edition is shorthand for *self-sustained interference pattern*; nothing in this universe is in a box.

---

## 2. Mass is the pitch of a standing wave

### 2.1 The separation

Write a single-mode configuration as a product of an observable-space factor and a sector factor, $\Psi_\infty(x,\xi) = \psi(x)\otimes\chi_{n,d}(\xi)$. The wave equation on $M_\infty$ separates. The sector factor solves the well's eigenvalue problem,

$$\bigl(-\Delta_{\Xi_d} + \lambda_d r^2\bigr)\chi_{n,d} = E_{n,d}\,\chi_{n,d},$$

and returns a number. The observable factor is left with

$$\partial_t^2\psi = c^2\bigl(\Delta_3 - m^2\bigr)\psi,$$

the Klein–Gordon equation — with the sector eigenvalue sitting exactly where mass sits. To a three-dimensional observer, who cannot resolve motion in $\Xi_d$, the eigenvalue of the hidden standing wave *is* an inertial constant. Mass is not conferred by a field, a condensate, or a symmetry breaking; it is the pitch of the sector standing wave. (The spinor version separates the same way: the Dirac operator on $M_\infty$ splits as $\gamma^\mu\partial_\mu\otimes\mathbf 1 + \gamma^5\otimes D_\Xi$, giving the massive Dirac equation in $3{+}1$ with $m$ the sector Dirac eigenvalue — this is where spin-½ for all fermions comes from, §3.4.)

### 2.2 The eigenvalue is a count

Here is the fact the entire mass spectrum stands on. The $d$-dimensional harmonic well's level $k$ has degeneracy $\binom{k+d-1}{d-1}$ — the number of ways to distribute $k$ excitation quanta among $d$ directions (stars and bars: $k$ stars, $d-1$ bars). Summing the degeneracies from the ground state up through level $n-1$ gives, by the hockey-stick identity of Pascal's triangle,

$$N_d(n-1) = \sum_{k=0}^{n-1}\binom{k+d-1}{d-1} = \binom{n+d-1}{d} \equiv S(n,d).$$

So $S(n,d)$ is the *cumulative state count* of the sector well below level $n$ — the integrated density of states. The framework's mass law is the statement that the mode's frequency equals that count, in sector units:

$$m = m_{{\rm scale},d}\times S(n,d),$$

with one frequency unit $m_{{\rm scale},d}$ per sector. A worked example, to fix the machinery: in $d=3$, the level degeneracies are $1, 3, 6, 10, \ldots$; through level 3 the count is $1+3+6+10 = 20 = S(4,3) = \binom{6}{3}$; with the $d=3$ unit $m_{{\rm scale},3} = 4.702$ MeV (derived in Part 2 from the electron mass and the couplings above), mode $n=4$ weighs $20 \times 4.702 = 94.0$ MeV — the strange quark, measured at $93.5$ MeV. Heavier particles are not vaguely "more excited"; they sit atop literally more configurations of their sector's geometry, and the mass spectrum is a census. Part 2 runs this law across all fifteen particles.

The photon is the cleanest entry: it is the $d=2$ sector's ground mode with zero excitation, $S(0,2) = 0$, so $m_\gamma = 0$ *exactly* — a wave with nothing excited has nothing to weigh. (Part 3 adds two independent protections that keep it exactly zero at all orders.)

One identity is worth knowing from the start. Pascal's rule for binomial coefficients reads, in the count's variables,

$$S(n,d) = S(n,d-1) + S(n-1,d):$$

a state count in $d$ dimensions splits exactly into the count one dimension down plus the count one level down. Because the sectors are physically nested (§4.4), this arithmetic relates counts *between* sectors — and Part 2 reports a striking empirical fact: the occupied particle indices satisfy a web of such relations, the muon's site for instance sitting exactly at a Pascal node, $S(4,4) = S(4,3) + S(3,4)$, i.e. $35 = 20 + 15$. We report these relationships as found; what selects the occupied levels in the first place is one of the framework's open mysteries, and this edition treats it as such.

---

## 3. Which dimensions bind: the sector set

The active sectors — the dimension counts at which the wave's self-interaction supports stable standing waves — are

$$D = \{2, 3, 4, 5, 6, 10\},$$

and this section derives the list. It is the least obvious structural claim in the framework, so it gets the full argument: the chain that builds the sectors, the two rules that terminate it, and the geometry that stamps each sector's identity.

### 3.1 The Hopf chain builds the ladder

The complex Hopf fibrations are the classical fact that odd-dimensional spheres are circle bundles over complex projective spaces:

$$S^1 \to S^{2k+1} \to \mathbb{CP}^k.$$

Concretely: $S^3$ is a circle's worth of phase over every point of $S^2 = \mathbb{CP}^1$; $S^5$ is a circle over every point of $\mathbb{CP}^2$; $S^7$ over $\mathbb{CP}^3$. In the framework these are not analogies — the wave's binding geometries are built by exactly this chain, each rung's self-coupling constructed from the rung below:

| Fibration | Total space (odd sphere) | Base (projective space) | Sectors it supplies |
|---|---|---|---|
| $S^1 \to S^3 \to \mathbb{CP}^1$ | $d=3$ | $d=2$ | hadronic sector over the electromagnetic plane |
| $S^1 \to S^5 \to \mathbb{CP}^2$ | $d=5$ | $d=4$ | neutrino sector over the colour sector |
| $S^1 \to S^7 \to \mathbb{CP}^3$ | — | $d=6$ | lepton sector as the next base |

The chain starts at $d=2$: $\mathbb{CP}^1$, the $U(1)$ fiber's own base, the electromagnetic reference plane contained in everything. The odd spheres ride on their bases through the shared circle fiber — this is why, in Part 3, the coupling of $d=5$ is not an independent constant but is *forced* by the couplings below it through fiber universality ($v_3/v_2 = v_5/v_4$), and why the weak vertex always couples neutrinos to up-type quarks: the neutrino's coordinate space is literally circles fibred over the quark sector.

The chain also carries its own integers. $\mathbb{CP}^k$ is built from one cell in each even dimension $0, 2, \ldots, 2k$, so

$$\chi(\mathbb{CP}^k) = k+1.$$

These class counts are physical multiplicities: $\chi(\mathbb{CP}^2) = 3$ is the number of colour classes the $d=4$ geometry offers — three colours; $\chi(\mathbb{CP}^3) = 4$ is the lepton geometry's class count (with the vacuum class removed, three generations — Part 3); $\chi(\mathbb{CP}^5) = 6$ counts six flavours. Part 2 will note, among the observed index relationships, that the up quark's level equals the colour count — a fact we report without pretending to derive.

### 3.2 First termination: the coupling chain ends at $d=6$

Each even rung's self-coupling is a kernel fixed point built from the seeds. At $d=6$ the construction changes character: $g_{66} = 1/n_s = 1/4$ is read directly off the class count $\chi(\mathbb{CP}^3) = n_s$, not obtained as a new fixed point — so the coupling-construction chain *terminates* there. The band $d = 7, 8, 9$ acquires no self-coupling:

- $d=8$ ($\mathbb{CP}^4$): its class count $\chi = 5$ matches no seed quantity — it is the gap in the sequence $2, 3, 4, 6$ of active class counts — and the fixed-point equation for $g_{88}$ has no seed-anchored solution.
- $d=9$ ($S^9$): as a circle bundle over $\mathbb{CP}^4$ it inherits exactly the $d=8$ obstruction on its invariant block; no value of $g_{99}$ closes the self-consistency.
- $d=7$ ($S^7$): geometrically accounted for already — it is the total space over the active $d=6$ base — and the mode-deposit structure that sites the physical particles (Part 2) has exactly six slots, saturated by the six members of $D$; a seventh sector would need a slot the structure cannot supply.

A dimension with no self-coupling holds no matter, and — this matters — *a matter-empty dimension is inert*: it has no energy to gravitate, no amplitude for any cross-sector coupling to grab, and contributes nothing to any observable. The universe does not owe an explanation for silent dimensions; $d=7,8,9$ are unoccupied for the same reason $d = 11, 12, \ldots$ are (next subsection), and both are invisible for the same reason the manifold's infinitely many further dimensions are.

### 3.3 Second termination: the binding threshold at $d=10$

The deeper cutoff is a criticality condition, and it is worth seeing whole because it is three lines of algebra with a physical punchline.

When the wave's modes couple along a sector's radial ladder, the strength of the link at rung $k_0$ in $d$ dimensions is the Jacobi/Gegenbauer coefficient

$$b_{k_0}(d) = \frac{\sqrt{k_0(k_0+d-1)}}{2k_0+d-2},$$

and $b = 1/2$ is the classical threshold between a ladder that supports propagating (bindable) structure and one whose excitations are evanescent — the same $1/2$ that separates propagation from decay in any nearest-neighbour chain. The relevant rung is the resonance site $k_0 = 16$ — the same site at which, in Part 2, the bottom quark forms as a beat. Solve for criticality:

$$b_{k_0}(d) = \tfrac12 \;\Longleftrightarrow\; 4k_0(k_0+d-1) = (2k_0+d-2)^2 \;\Longleftrightarrow\; 4k_0 = (d-2)^2,$$

(expand both sides; the $4k_0^2$ cancels, the cross terms leave $4k_0$ against $(d-2)^2$). With $k_0 = 16$:

$$(d-2)^2 = 64 \;\Longrightarrow\; d = 10.$$

And $b_{k_0}(d)$ is strictly decreasing in $d$, so the sector table reads:

| $d$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | **10** | 11 |
|---|---|---|---|---|---|---|---|---|---|---|
| $b_{16}(d)$ | .5154 | .5143 | .5128 | .5111 | .5092 | .5071 | .5050 | .5025 | **.5000** | .4975 |

Everything through $d=10$ sits at or above threshold; $d=10$ is *exactly* critical; everything beyond is subcritical — localization is geometrically impossible there, regardless of any coupling, so the sector list ends. The tau's sector is the last dimension in which matter can hold together at all, and it holds together marginally: the tau sits at the exact edge of binding, which is why (Part 2) its mass carries the one correction that vanishes for every other lepton, and why (Part 3) it decays into everything with no dominant channel — a critical-point particle.

Note the two terminations are different in kind, and the difference is physical. $d \ge 11$ is *subcritical*: binding impossible, unconditionally. $d = 7, 8, 9$ are *supercritical*: binding would be permissible, but the coupling construction never reaches them — they are empty, not forbidden. Empty and forbidden dimensions are equally invisible, by inertness.

So the sector set assembles as

$$D = \underbrace{\{2,3\}}_{\text{first Hopf pair}} \cup \underbrace{\{4,5\}}_{\text{second Hopf pair}} \cup \underbrace{\{6\}}_{\text{chain terminus}} \cup \underbrace{\{10\}}_{\text{critical endpoint}},$$

with two Hopf pairs inside it: $(3,4)$ — the two quark families — and $(5,6)$ — neutrinos and charged leptons. Two quark multiplets and two lepton multiplets are a structural consequence of the chain's pairing, not an input.

### 3.4 What each sector's geometry stamps on its tenants

The wave is a spinor field, and spinor structure depends on dimension with period 8 (the Clifford algebra's Bott periodicity). Which reality/chirality conditions a sector admits is therefore fixed by $d \bmod 8$ — and this single classical fact distributes the particle content's qualitative features:

| $d$ | local geometry | $d\bmod 8$ | spinor type | what it stamps |
|---|---|---|---|---|
| 2 | $\mathbb{CP}^1$ | 2 | Majorana–Weyl | two helicities: the photon's two polarizations |
| 3 | $S^3$ | 3 | Majorana | vector-like quarks (no intrinsic handedness) |
| 4 | $\mathbb{CP}^2$ | 4 | Weyl (spin$^c$) | chirality split $u_L$ vs $u_R$; the forced $U(1)$ of spin$^c$ = hypercharge; three colours |
| 5 | $S^5$ | 5 | **Dirac only** | no Majorana condition exists: neutrinos are Dirac, lepton-number violation unwritable |
| 6 | $\mathbb{CP}^3$ | 6 | Weyl | chiral leptons; colour cancels identically |
| 10 | $\mathbb{CP}^5$ | 2 | Majorana–Weyl | the tau; critical-endpoint coupling |

Two entries deserve their sentences here (Part 3 develops both). The complex sectors — $d = 2, 4, 6, 10$ — are Kähler: they carry an intrinsic handedness operator built from their complex structure, and the weak interaction threads through it, touching only the left-handed half. The real spheres $d=3$ and $d=5$ have no handedness of their own; their chiral behaviour is *inherited* through the complex sectors adjacent to them in the nesting. And $d \bmod 8 = 5$ is the unique Clifford class admitting neither a Majorana nor a Weyl condition: on the neutrino's geometry no charge-conjugation matrix exists at all, so no interaction of the lepton-number-violating form $\psi^T C\psi$ can be written *at any order*. Neutrinoless double beta decay is not suppressed here; it is unwritable, and observing it falsifies the framework outright (Part 6).

Spin-½ itself, for every quark and lepton, comes from $\Psi_\infty$ being a Dirac spinor on $M_\infty$: the sector separation hands each mode the spinor structure of its sector, and Fermi statistics follow from the spinor field's anticommutation — Pauli exclusion as field algebra, not axiom. Antiparticles are the conjugate spinor components, automatic in any complex spinor field.

### 3.5 The tenants

Assembling §§3.1–3.4 with the mode indices Part 2 derives:

| $d$ | geometry | particles | why these |
|---|---|---|---|
| 2 | $\mathbb{CP}^1$ | photon, W, Z, Higgs | the reference plane every sector contains |
| 3 | $S^3$ | down, strange, bottom | the seed sector: observable space, first Hopf total space |
| 4 | $\mathbb{CP}^2$ | up, charm, top | the colour sector: $\chi = 3 = N_c$ |
| 5 | $S^5$ | three neutrinos | Hopf partner of $d=4$; Dirac-only spinors |
| 6 | $\mathbb{CP}^3$ | electron, muon | chain terminus; $\chi = 4$, colour-silent |
| 10 | $\mathbb{CP}^5$ | tau | critical endpoint; shares the lepton coupling $1/n_s$ |

A particle's sector dimension is its actual spatial dimensionality. The electron has structure in six spatial directions, of which we occupy three. The tau extends through ten. Down-type quarks live in exactly our three. The photon has only two — fewer than we do. These are not bookkeeping labels; §4 and §5 are about what that dimensionality physically does.

---

## 4. Bound within, free without

### 4.1 The rest state of a free direction

A particle is bound by its sector well only in its own $d$ dimensions. In every dimension beyond those, no well exists for it — the $d=7,8,9$ band carries no sector structure at all, and a higher sector's well belongs to that sector's own modes. In a free direction the particle is governed by the bare Laplacian, whose spectrum on a line is $[0,\infty)$: no negative eigenvalue, hence no bound state, and exactly three solution types — $e^{iky}$ (carrying momentum, $E>0$), the constant ($E=0$), and growing exponentials (unphysical). The unique rest configuration is *the constant*.

The physics: localizing a particle to width $\Delta$ in a free direction costs kinetic energy $\sim 1/(2m\Delta^2)$, so the rest limit forces $\Delta \to \infty$ — uniformity. A massive particle at rest is therefore *uniformly present* across every dimension it does not structurally occupy: not absent from the higher dimensions, but spread evenly through them, pinned to no point. It does not sit somewhere in the hidden coordinates, and it does not drift (drifting needs momentum, an excited outer state). Uniform co-presence is the only zero-energy option a free direction offers.

Normalizability is untouched: the mode is normalized on its own $\Xi_d$, and the uniform outer factor is precisely the statement "this is a $d$-dimensional object — normalize it in $d$ dimensions." The divergence of an outer-volume norm is the object's dimensionality speaking, not a defect.

One exception, and it is the photon. Masslessness removes the rest state: with $E^2 = p^2 + m^2$ and $m=0$ there is no $p=0$ configuration to sit in, so the photon's state in the directions beyond its two must carry momentum — uniform presence becomes *propagation*. The photon travels perpendicular to its own plane because traveling is the only thing a massless object can do out there. §5.5 turns this into transversality and the two polarizations.

### 4.2 What uniformity does and does not permit

Two consequences pull in opposite directions, and keeping them separate prevents both an underclaim and an overclaim.

**Shields fail; walls hold.** A three-dimensional shield can erase a field on the 3D slice but cannot contain a structure extending beyond the slice: the particle is uniformly present in the dimensions the shield was not built in, and meets the field there. (The Aharonov–Bohm phase — a charged particle responding to a field it never locally touches in 3D — is this containment failure seen in the laboratory.) But the same uniformity gives *no way around a barrier*: a barrier along an observable direction is built by 3D sources, so it takes the same value at every hidden coordinate — the hidden directions are transverse to it, separate off as free directions, and leave the ordinary one-dimensional crossing problem intact. Tunneling times are standard; there are no extra-dimensional shortcuts. Hidden dimensions bypass shields, never walls.

**Contact is guaranteed; containment never is.** Because every particle is uniform outside its own dimensions, two particles always meet on the coordinates they share — the lower of the two dimensionalities. A lower-dimensional structure does not need to *find* a higher-dimensional partner in the hidden coordinates; it is already everywhere in them. Three dimensions are always enough to touch a six-dimensional electron — and never enough to contain it.

### 4.3 Orientation is free

With no structure outside its $d$ dimensions, a particle has nothing out there to fix the orientation of its $d$-plane. Which $d$-plane of $M_\infty$ it occupies is a free kinematic degree of freedom; the count $d$, the sector geometry, and the mass are fixed, but the orientation is set by what the particle lines up with. The photon is the sharpest case: its reorientable 2-plane is directly observable as its polarization. This is also why a 2-plane fits inside every sector — the photon couples to every charged particle because every charged particle presents a 2-plane for it to align with.

### 4.4 The nesting, physically

The sectors nest as literal coordinate containment:

$$\Xi_2 \subset \Xi_3 \subset \Xi_4 \subset \Xi_5 \subset \Xi_6 \subset \Xi_{10} \subset \Xi_\infty.$$

The photon's two coordinates are two of the quark's three, three of which are three of the up-quark's four, and so on. A function of only the $d=2$ coordinates is automatically a function on every larger sector — which is the precise sense in which a lower sector's dynamics *are* dynamics in every sector containing it. Motion in a shared coordinate is motion in every sector that owns that coordinate, symmetrically and simultaneously, because there is one wave. This nesting is the entire mechanism of force (Part 3), and it is why each force has exactly the reach it has: electromagnetism universal (every charged sector contains $d=2$), colour confined to the quark block $\{3,4\}$, and the tau in contact with everything (its ten dimensions contain every other sector — and correspondingly it decays into everything, with no channel dominant).

Cross-sector interaction never involves two separate objects reaching across a gap. When the electron interacts with the tau, the electron does not extend itself into the tau's four deeper coordinates — it was already uniformly present there (§4.1), because there is one wave and the electron is a feature of it. "Interaction" is one wave's structure at two sector depths meeting on the coordinates the depths share.

---

## 5. We are the three-dimensional part

### 5.1 The observer's location is a theorem

That we experience three dimensions is not a postulate here; it follows from what stable matter is.

The lightest stable composites the framework admits are colour-neutral baryons — protons and neutrons, built from $d=3$ and $d=4$ quarks. Colour neutrality is precisely the condition that the composite's $d=4$ colour index cancels *completely* (the three colour classes of $\mathbb{CP}^2$ summing to the singlet), so a nucleon has no residual $d=4$ coordinate dependence: it is a purely three-dimensional object. Every nucleus is such an object; every atom, molecule, instrument, and observer is built of such nuclei. A measuring device made of three-dimensional matter measures three-dimensional physics *by construction* — its instruments have no coordinate support anywhere else, so no protocol built from it can return a coordinate outside $d=3$.

"Why do we see three dimensions?" therefore has a mechanism, not an anthropic shrug: because colour confinement makes the stable building bricks three-dimensional, and an observer is something built. Everything characteristically *quantum* about the world then follows from this vantage — a three-dimensional being registering a wave that extends further. The rest of §5 derives the quantum catalogue from it.

### 5.2 The electron cloud is a shadow

The electron in an atom is not a probability smear. It is a definite object at a definite point of its six-dimensional space at every instant, executing a definite closed orbit in $\mathbb{CP}^3$, bound to the nucleus through the shared electromagnetic plane. A three-dimensional observer detects it only where that orbit intersects our three coordinates — and here §4 does its work: the electron's orbit is confined by its sector well *in the six sector dimensions about its center*, not in our three coordinates, so the orbit sweeps through our slice unconfined and its intersections with the slice fall across all of observable space. The familiar "cloud" — and the s, p, d, f orbital shapes — are the three-dimensional shadow of the definite six-dimensional orbit: the angular-momentum structure of the orbit, projected. A shadow does not inherit the localization of the object casting it.

This is the framework's reading of the standard statement that "the electron can be found anywhere": not irreducible chance, but a 6D trajectory read through a 3D window. The randomness we ascribe to the electron's position is the information carried in the three coordinates we cannot see. Part 5 builds atomic physics and chemistry on this picture — including the results (orbital degeneracies, the tetrahedral bond angle, shell structure) that come out of the orbit geometry with no empirical input.

The nucleus, meanwhile, is geometrically *thin* in the electron's space: a $d=3$ object occupying three of the orbit's six dimensions and absent from the rest. An atom is not a ball with a cloud around it; it is a three-dimensional structure being orbited in six dimensions, coupled through a shared two-dimensional plane.

### 5.3 The Born rule, derived

The quantum world's central postulate — probability equals the squared amplitude — is a three-step derivation here, and each step is physics already on the table.

**Step 1: $|\Psi|^2$ is the amount of wave.** $\Psi_\infty$ is complex, so its global phase symmetry carries a conserved Noether current whose density is $\Psi^\dagger\Psi = |\Psi_\infty|^2$. The squared modulus is the physically conserved *quantity of wave* at each point — fixed by the field's own conservation law, not chosen as the thing to square.

**Step 2: detectors fire at the local intensity.** Every interaction in the framework is the kernel — density against density (§1.2). A detection *is* such an interaction, so the rate at which a detector registers the system at a point is proportional to the wave's intensity $|\Psi|^2$ there. The quantity governing detection frequency is the one the interaction already couples to; nothing of the form "now square the amplitude" is appended.

**Step 3: probability is a ratio, so the amplitude cancels.** Only relative rates across outcomes are observable: $\rho(r) = |\Psi(r)|^2 \big/ \int |\Psi|^2$, invariant under $\Psi \to c\Psi$. The absolute amplitude of the universal wave never enters — which is why it need not, and cannot, be known. (The framework separately proves the global amplitude is inaccessible; the Born ratio's amplitude-independence and that inaccessibility are one fact seen twice.)

The rule extends to any basis a detector can physically realize: a detector resonant on channels $\{\phi_a\}$ registers outcome $a$ at a rate proportional to the wave's intensity in that channel, $|\langle\phi_a|\Psi\rangle|^2$, and probability is again the ratio. One idealization enters — a faithful, unbiased detector, which is the *definition* of measuring in a basis rather than a smuggled postulate — and one genuine scope restriction falls out: only channels the kernel can couple to are measurable. The framework does not grant measurement in arbitrary abstract bases; observables are what the wave's self-coupling can actually touch. Nothing observed is lost to this restriction, and the measurement postulate's excess generality is trimmed.

What a $d=3$ observer samples, finally, is the intensity with the unresolved sector coordinates integrated out, $\int|\Psi_\infty(r,\xi)|^2\,d\xi$ — the marginal. The three-dimensional appearance of everything is this integration, not a projection performed by anyone: there is no external screen, no collapse; we are inside the wave, at the coordinate level our bricks are bound to, sampling what our coordinates can reach.

### 5.4 Entanglement, uncertainty, and relativity of smearing

**Entanglement is proximity in coordinates that distance doesn't measure.** Three-dimensional separation is distance in $\Xi_3$. Two electrons a great distance apart in our coordinates can be adjacent — or overlapping — in the sector coordinates, because sector-coordinate separation is simply a different quantity from 3D distance. A measurement on one reads a jointly held sector state; the other reflects it not because a signal crossed the 3D gap but because, in the coordinates that carry the correlation, there never was a gap. Bell-inequality violations are exactly what this looks like: the correlations live in coordinates the locality assumption never constrained. Signalling remains impossible — each local detection is still governed by local intensity (§5.3).

**Uncertainty is perspective.** Every particle is sharp in its own dimensions and smeared to any observer resolving fewer. And this is relative, not special to us: from the electron's six-dimensional vantage, the tau's four deeper coordinates are integrated out the same way, and the tau appears to the electron as exactly the kind of marginal blur the electron presents to us. Smearing is the signature of watching from below an object's dimensionality — a property of the vantage, never of the object.

**The uncertainty principle itself is wave mechanics, not mystery.** Everything a three-dimensional apparatus handles is a wave marginal, and for *any* wave, position spread and wavenumber spread are Fourier conjugates: a waveform cannot be narrow in both, so $\Delta x\,\Delta p \gtrsim 1$ (in units of the one imported quantum — Part 5) is a theorem about waveforms, inherited automatically because there is nothing here *but* waves. What the framework adds is the reason the bound is *irreducible for the observer* rather than a limitation of technique: the information that would sharpen both at once — where the object actually is along its trajectory — resides in the sector coordinates the three-dimensional marginal has integrated out. Dimensional depth, not nature's dice, is what stands between the observer and simultaneous specification.

### 5.5 Transversality: the photon's dimensions, made visible

The photon oscillates in its two dimensions and — being massless (§4.1) — travels perpendicular to them. "Perpendicular to a 2-plane" in $M_\infty$ is a vast space of directions with none privileged; a three-dimensional observer resolves a single propagation direction because *our* three coordinates meet that orthogonal space in one line. The photon cannot oscillate along its direction of travel, since travel is by construction perpendicular to the plane it oscillates in. So in whichever direction we see a photon move, its oscillation is transverse, with exactly two independent states — the photon's two dimensions, directly observable as its two polarizations. Transversality is usually extracted from gauge invariance plus the Maxwell equations; here it is what a two-dimensional oscillator moving perpendicular to itself looks like through a three-coordinate window.

---

## 6. Force is shared coordinates; gravity is the manifold itself

Two principles govern every interaction, and they answer different questions.

**Containment — whether a coupling exists.** A particle can couple to a structure only if that structure's coordinates lie inside the particle's own (§4.4). This is a necessary condition, read directly off the nesting: electromagnetism reaches everything charged because every sector contains the $d=2$ plane; colour reaches only the quark block; the weak structure reaches every fermion sector; nothing reaches a particle through coordinates it does not have.

**The filter — what form the coupling takes.** The particle's own sector geometry stamps the structure of every coupling it has, and forbids entire classes outright. Polarization is the $U(1)$ geometry of $\mathbb{CP}^1$ expressing itself: perpendicular currents get exactly zero, not suppression. Colour is the three-class structure of $\mathbb{CP}^2$. The neutrino's $S^5$ forbids every lepton-number-violating vertex (§3.4). The lepton geometries cancel colour identically — leptons are colour-*silent*, at every energy, not weakly coloured. The two principles are independent, and both must pass: neutrinos contain the colour sector's coordinates (containment holds) yet their geometry projects colour to the singlet (the filter kills it), so they are neutral.

Part 3 develops the force structures one by one — with the coupling *strengths* derived, not just the shapes — and shows the same counting machinery that prices the masses pricing the mixing angles.

Gravity is not a force in this sense at all and gets Part 4 to itself; the shape of it belongs here. Gravity is the curvature of $M_\infty$ sourced by mass — by the wave's energy density — across all coordinates with no sector boundary. There are no gravitons and nothing to quantize: no gravitational field exists, only geometry responding to mass. Two previews of Part 4's derivations, both direct consequences of §4: a mass curves the manifold *with a gradient* only in the dimensions it is bound in (a uniform source is translation-invariant, and so is the geometry it sources — no gradient, no pull), so ordinary gravity is three-dimensional because ordinary matter is; and a three-dimensional observer integrating any source over its hidden coordinates always recovers exactly Newton's $1/r$ — the inverse-square law is not evidence that space is three-dimensional, it is what higher-dimensional gravity looks like from a three-dimensional vantage.

---

## 7. What the wave picture replaces

| Standard account | What is actually happening |
|---|---|
| Wave–particle duality | Only waves exist; a "particle" event is the density–density coupling firing at a point |
| Born rule (postulated) | Detection rate $\propto$ local intensity; probability is relative rate — derived, §5.3 |
| Probability cloud | 3D shadow of a definite 6D orbit, §5.2 |
| Uncertainty (fundamental) | The marginal's spread — information in unresolved coordinates, §5.4 |
| Force carriers exchanged | One wave self-coupling on shared coordinates; bosons are particles, not messengers |
| Mass from the Higgs mechanism | Mass is the sector standing wave's eigenvalue, §2; the Higgs is the $n=95$ mode of $d=2$ |
| Colour, chirality, hypercharge (inputs) | Stamps of the sector geometries, §3.4 and Part 3 |
| Pauli exclusion (axiom) | Anticommutation of the one spinor field, §3.4 |
| Entanglement as nonlocal influence | Proximity in sector coordinates, §5.4 |
| Compactified extra dimensions | Macroscopic flat dimensions, occupied or empty; nothing curled up, §1.1, §3 |
| Quantum gravity | Nothing to quantize: gravity is sourced curvature, §6 and Part 4 |
| Why three dimensions? (anthropic) | Colour-singlet bricks are 3D; observers are built, §5.1 |

---

## 8. What is open, stated where it belongs

This edition states openness in prose, in place; Part 6 collects the full ledger. The items native to this Part:

**Which levels are occupied is a mystery, and this edition lets it be one.** The sector list of §3 is derived; the mass law of §2, given the occupied levels, performs at the fraction-of-a-percent level (Part 2); and the *emptiness* of the unoccupied levels has real mechanics behind it (odd levels are cut off from the vacuum by an exact parity zero; even non-members radiate away with a strictly positive decay width — nothing between the observed particles can persist). But why the particular fifteen occupied levels are the ones nature chose is not derived. The indices display striking arithmetic relationships — Part 2 reports them as findings — and the framework declines to promote those patterns into a derivation. The occupied levels are, in this edition, measured facts on the same footing as the electron mass.

**The rank-1 coupling is argued, not proved.** The physical argument of §1.2 (higher rank entangles the sectors and breaks mass-law separability) runs at sketch rigor in one step; making the entanglement step rigorous would close it.

**The exactness of the product structure** $M_\infty = \mathbb{R}_t \times \Xi_\infty$ — no metric cross-terms between time, our coordinates, and the sector coordinates — is derived at the vacuum level from the covariance of gravity's sourcing (the vacuum's symmetries are inherited exactly by the geometry it sources; Part 4), and stands on that argument rather than on assumption.

Everything else this Part used — the harmonic well, the counting identity, the sector terminations, the observer theorem, the Born rule — is derived at the level shown or better in the archive.

---

*Second edition, 2026. Full derivations, status accounting, and numerical verification: first-edition Parts 1–11 at https://fedgeno.github.io/; the computation record `idwt.py` is distributed with these documents.*
