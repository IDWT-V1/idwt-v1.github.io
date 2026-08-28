# Infinite Dimensional Wave Theory, Second Edition — Part 1: The Wave

## What this edition is

This is a restatement of Infinite Dimensional Wave Theory organized around a single question asked of every claim: *is this a physical phenomenon that could actually be happening?* Everything in these pages passed that test. Derivations, numerical checks, and the full working record remain in the first-edition Parts and in `files/idwt.py`; here the physics is presented as physics, with open problems stated plainly in prose where they stand.

---

## 1. One wave

There is one physical object: a complex Dirac spinor wave $\Psi_\infty$ on a manifold $M_\infty$ with one time direction and infinitely many macroscopic spatial dimensions. The wave interacts with nothing but itself. Everything observable — every particle, every force, every quantum number, gravity, chemistry — is a feature of this one wave's geometry and self-interaction.

The spatial dimensions are ordinary, flat, and infinite in extent. None are rolled up, compactified, or small. What distinguishes the dimensions from one another is not their size but whether the wave can bind there: at certain dimension counts, the wave's self-interaction supports stable localized standing waves, and at others it does not. The dimension counts that support binding are

$$D = \{2, 3, 4, 5, 6, 10\},$$

and these six *sectors* carry all of matter. Dimensions $7$, $8$, $9$ and everything beyond $10$ exist as coordinates of $M_\infty$ but hold no matter: nothing binds there, and an empty dimension is inert — it has no energy to gravitate and no amplitude to couple, so it contributes nothing to any observation. The universe has infinitely many dimensions and we notice only the occupied ones.

Each sector is characterized by the local symmetry of the wave near a binding center: the two-dimensional sector behaves like $\mathbb{CP}^1$, the three-dimensional sector like the sphere $S^3$, then $\mathbb{CP}^2$, $S^5$, $\mathbb{CP}^3$, and $\mathbb{CP}^5$ for $d = 4, 5, 6, 10$. These labels describe the shape of the bound wave near its center — the way a hydrogen ground state has spherical symmetry although the electron roams all of infinite space — not the global topology, which is flat $\mathbb{R}^d$ everywhere.

The sectors nest. The two coordinates of the $d=2$ sector are two of the three coordinates of $d=3$; those three are three of the four of $d=4$; and so on:

$$\Xi_2 \subset \Xi_3 \subset \Xi_4 \subset \Xi_5 \subset \Xi_6 \subset \Xi_{10} \subset \Xi_\infty.$$

This nesting is not a technicality. It is the entire mechanism of force, and it is why the forces have the reach they do.

There is exactly one time. Every particle in every sector ages by the same clock; the extra dimensions are all spatial. A six-dimensional electron is six spatial dimensions plus the one shared time — never a separate spacetime. This single time direction is what keeps causality ordinary in a universe with many large spatial dimensions.

---

## 2. Particles are standing waves

A particle is a stable standing wave of $\Psi_\infty$ in one of the six sectors. The wave's self-interaction creates a well in each sector; the well's bound states are the particles. Which sector a particle occupies determines everything qualitative about it — its charges, its chirality, what it can and cannot do — and its excitation level within the sector determines its mass.

The occupied sectors and their tenants:

| $d$ | Local symmetry | Particles |
|---|---|---|
| 2 | $\mathbb{CP}^1$ | photon, W, Z, Higgs |
| 3 | $S^3$ | down, strange, bottom quarks |
| 4 | $\mathbb{CP}^2$ | up, charm, top quarks |
| 5 | $S^5$ | the three neutrinos |
| 6 | $\mathbb{CP}^3$ | electron, muon |
| 10 | $\mathbb{CP}^5$ | tau |

A particle's sector dimension is its actual spatial dimensionality. The electron is a six-dimensional object: it has structure in six spatial directions, of which we occupy three. The tau extends through ten. Down-type quarks live in exactly our three. The photon has only two — fewer than we do.

**Bound within, free without.** A particle is bound by its sector well only in its own $d$ dimensions. In every dimension beyond those, no well exists for it, and a free direction admits exactly one rest configuration: uniform presence. Localizing a particle to a finite width in a free direction would cost kinetic energy, so at rest the particle is spread evenly across every dimension it does not structurally occupy. A lower-dimensional particle is therefore not *absent* from the higher dimensions — it is uniformly present in them, pinned to no point. This single fact does a great deal of work below: it is why particles in different sectors can always touch, and why hidden dimensions can carry an influence around a shield yet offer no shortcut through a wall (a barrier built by three-dimensional sources takes the same value at every hidden coordinate, so there is no detour).

**Mass is the sector eigenvalue.** The wave equation on $M_\infty$ separates into an observable part and a sector part. The sector part acts on the particle's bound mode and returns a number — the eigenvalue of its standing wave. A three-dimensional observer, unable to resolve the sector coordinates, sees that number as an inertial constant in an ordinary Klein–Gordon equation: mass. Mass is not conferred by a field or a condensate; it is the pitch of the standing wave. The photon is the $d=2$ sector's ground state with zero excitation, and its mass is exactly zero for that reason — a wave with nothing excited has nothing to weigh.

The eigenvalue itself is a count. The energy of level $n$ in a $d$-dimensional well equals the number of distinct ways to distribute the excitation quanta across the $d$ directions,

$$m = m_{\mathrm{scale},d} \times S(n,d), \qquad S(n,d) = \binom{n+d-1}{d},$$

with one frequency unit $m_{\mathrm{scale},d}$ per sector, all six of which are fixed by the sector couplings and a single reference mass, the electron's. This counting law is the engine of the mass spectrum, and Part 2 of this edition is devoted to it: fifteen particles, one reference mass, agreement with measurement at the fraction-of-a-percent level across six orders of magnitude.

Why these six sectors and not others is a question with a physical answer, sector by sector. Above $d=10$ the wave's self-coupling falls below the threshold needed to hold a standing wave together — localization becomes impossible, so the sector list terminates. The band $d = 7, 8, 9$ can geometrically support binding but the wave's coupling construction never reaches it: the chain of couplings that builds the sectors — each even sector closing on its complex geometry, each odd sphere riding on the sector below it through the Hopf relation between spheres and projective spaces — terminates at $d=6$, with $d=10$ picked out separately as the exact critical endpoint where the binding threshold is met with equality. The tau's sector is the last dimension in which matter can hold together at all.

---

## 3. We are the three-dimensional part

We are not outside $M_\infty$ looking in; we are inside it, at the $d=3$ level. And our position there is not an accident to be postulated — it follows from what stable matter is.

The lightest stable composite objects are the proton and neutron: colour-neutral packages of $d=3$ and $d=4$ quarks. Colour neutrality is precisely the condition that the composite's $d=4$ structure cancels completely, so a nucleon is a purely three-dimensional object. Every nucleus, every atom, every instrument, and every observer is built from such objects. A measuring device made of three-dimensional matter measures three-dimensional physics by construction: it has no coordinate support anywhere else. The question "why do we experience three dimensions?" has an answer rather than an assumption: because the stable bricks that anything can be built from are three-dimensional, and an observer is something built.

Everything characteristic of the quantum world follows from this vantage point — a three-dimensional being registering a wave that extends further than three dimensions.

**The electron cloud is a shadow.** The electron in an atom is not a probability smear. It is a definite object at a definite point of its six-dimensional space at every instant, executing a definite closed orbit. We detect it only where that orbit intersects our three coordinates, and the intersections of a six-dimensional orbit with a three-dimensional slice fall across the whole slice. The familiar "cloud" — and the s, p, d, f orbital shapes — are the three-dimensional shadow of the definite six-dimensional orbit. A shadow does not inherit the localization of the object casting it. The randomness we ascribe to the electron's position is the information in the three coordinates we cannot see; nothing about the electron itself is indefinite.

**The Born rule is derived, not postulated.** Because $\Psi_\infty$ is a complex wave, its phase symmetry conserves a density, $|\Psi_\infty|^2$ — the physical amount of wave at each point. Every interaction, including a detection, is the wave's self-coupling of density against density, so the rate at which a detector fires at a point is proportional to the wave's intensity there. Probability is nothing more than relative firing rate, and a ratio of intensities is unchanged if the whole wave is rescaled — which is why the absolute amplitude of $\Psi_\infty$ never enters any observation and never needs to be known. The rule "probability equals the squared amplitude" is what wave intensity looks like to an observer who can only count detections. The same argument runs in any measurement basis a detector can physically couple to.

**Entanglement is closeness in coordinates we do not see.** Two electrons a great distance apart in our three dimensions can be adjacent — or overlapping — in the sector coordinates, because sector-coordinate separation is not three-dimensional distance. A measurement on one reads a shared sector state that the other shares not by signalling but by never having been separated in those coordinates in the first place. Nothing travels; the correlation lives in dimensions our notion of "apart" does not reach.

**Uncertainty is perspective, not ontology.** Every particle is sharp in its own dimensions and smeared to any observer resolving fewer. This is relative, not special to us: from the electron's six-dimensional vantage, the tau's four deeper coordinates are likewise integrated out and the tau appears as exactly the same kind of marginal blur. The smearing is the signature of watching from below an object's dimensionality — a property of the viewpoint, never of the object.

---

## 4. Force is shared coordinates

There are no force carriers in IDWT. Nothing is exchanged. Two particles interact for one reason only: they are features of the same wave, and their sectors share coordinates. Motion in a shared coordinate is motion in every sector that owns it — symmetrically, instantly, because there is only one wave. The kernel of the wave's self-interaction couples density to density wherever sector coordinate spaces overlap, and that coupling *is* what we call force.

Two conditions govern every interaction.

**Containment — whether a coupling exists at all.** A particle can couple to a structure only if that structure's coordinates lie inside the particle's own. Because the sectors nest, this reads directly off the dimension counts. Every sector contains the two coordinates of $d=2$: this is why electromagnetism is universal — every charged particle, whatever its sector, holds the photon's entire two-dimensional world as a subspace of its own. The strong interaction spans $d=3$ and $d=4$, the quark sectors, and reaches nothing outside them. The tau, at $d=10$, contains every other sector; it is the one particle for which contact with anything is guaranteed — and correspondingly the tau decays into everything, with no channel dominant.

**The filter — what form the coupling takes.** The particle's own sector geometry stamps the structure of every coupling it has, and forbids entire classes of interaction outright. Polarization is the $U(1)$ geometry of the photon's $\mathbb{CP}^1$ expressing itself: the photon couples to currents aligned with its plane and to nothing else — perpendicular currents get zero, not suppression. Colour is the three-fold structure of $\mathbb{CP}^2$: three colour charges because that geometry has exactly three independent classes to couple through. The electron's $\mathbb{CP}^3$ cancels colour identically — leptons are not weakly coloured but colour-silent, at every energy. And the neutrino's five-dimensional sphere admits no Majorana structure at all: the mathematics of spinors in five dimensions cannot write a lepton-number-violating mass term, at any order, so neutrinoless double beta decay is forbidden outright. That is not a suppression to be overcome by better experiments; on this framework it will never be seen, and observing it would falsify the theory on the spot.

Containment says whether a coupling is possible; the filter says what it looks like and what is impossible. A particle can satisfy containment and still not couple — neutrinos hold the colour sector's coordinates inside their own five, but their sector geometry projects colour to zero, and so they are neutral.

Some familiar facts fall out of this picture with no further input:

- **Transversality of light.** The photon oscillates in its two dimensions and travels perpendicular to them — travel along its oscillation plane is a contradiction in terms. Whatever direction we see a photon move, its oscillation is transverse, with exactly two independent states: the photon's two dimensions, made directly visible as its two polarizations.
- **Lepton universality.** The electron and muon are two levels of the same six-dimensional well. Their couplings to anything outside the sector depend only on the sector, not the level — so they interact identically, differing only in mass. This is not a measured pattern awaiting explanation; two modes of one geometry could not couple differently if they tried.
- **Chirality of the weak interaction.** The complex (Kähler) sectors possess an intrinsic handedness that the real-sphere sectors lack; the weak coupling threads through the complex structure and therefore engages only the left-handed component. Quarks and neutrinos, living on real spheres, have no handedness of their own — their chiral behaviour is inherited through the complex sectors adjacent to them in the nesting.
- **Confinement as admissibility.** There is no colour flux tube and no propagating colour field. Colour neutrality is a selection rule on what states can exist in isolation: a lone coloured object is not a suppressed configuration but an inadmissible one, like a wave required to be single-valued failing to close on itself. Free quarks are not hard to produce; they are not on the menu of states.

Cross-sector interaction never involves two separate objects reaching across a gap. When the electron interacts with the tau, the electron does not extend itself into the tau's deeper coordinates — it was already there, uniformly present (Section 2), because there is one wave and the electron is a feature of it. "Interaction" is one wave's structure at two sector depths meeting on the coordinates the depths share.

---

## 5. Gravity is the shape of the manifold

Gravity is not a force in the sense of Section 4 at all. It is the curvature of $M_\infty$ itself, sourced by mass — by the energy density of the wave — across all coordinates without any sector boundary. There are no gravitons and nothing to quantize: there is no gravitational field, only geometry.

A mass curves the manifold only in the dimensions it is localized in. In directions where a source is uniform, the geometry it sources is translation-invariant — flat along that direction, with no gradient and hence no pull. Ordinary matter is three-dimensionally bound (Section 3), so ordinary gravity is three-dimensional: not because gravity is confined to our slice, but because the sources are. A three-dimensional observer measuring the pull of a three-dimensional source integrates over the hidden coordinates and recovers exactly Newton's law, with the observed constant $G_N$ related to the manifold's own coupling by the geometric factor of the three-dimensional Green's function, $G_N = G_\infty/4\pi$.

Because gravity is sourced curvature rather than a self-interacting field with its own dynamics, the geometry inherits every symmetry of its source exactly. The vacuum — static, uniform, isotropic — sources a geometry with no mixing between time, our directions, and the sector directions: the clean product structure of $M_\infty$ is not an assumption but what an unstructured source produces.

Two honest boundaries of this picture. The strength of gravity, $G_\infty$, is a second dimensional input alongside the electron mass: the framework fixes the *structure* of gravity, not its magnitude. And there is no hierarchy problem to solve, because there is no hierarchy: gravity (curvature sourced by the wave) and the forces of Section 4 (the wave's kernel self-coupling) are different kinds of thing, not two couplings on one scale mysteriously far apart. The famous ratio is a comparison of apples to oranges, and the framework declines to be embarrassed by it.

The full gravitational program — why bound systems see ordinary Newtonian dynamics, what a dark-matter observation could and could not mean here, and the cosmological questions the framework leaves open — is Part 4 of this edition.

---

## 6. What the wave picture replaces

The reader keeping score against the standard account can use this dictionary.

| Standard account | What is actually happening |
|---|---|
| Wave–particle duality | There are only waves; localized detections are the density–density coupling firing at a point |
| The Born rule (postulated) | Detection rate proportional to wave intensity; probability is relative rate (derived) |
| Probability cloud | Three-dimensional shadow of a definite higher-dimensional orbit |
| Force carriers exchanged | One wave coupling to itself on shared coordinates; bosons are particles, not messengers |
| Mass from the Higgs mechanism | Mass is the eigenvalue of the particle's sector standing wave; the Higgs is a particle like any other, the $n=95$ mode of $d=2$ |
| Colour charge (input) | The three-fold coupling structure of the $\mathbb{CP}^2$ geometry |
| Chirality of the weak force (input) | Intrinsic handedness of the complex sectors |
| Entanglement as nonlocal influence | Proximity in sector coordinates that three-dimensional distance does not measure |
| Compactified extra dimensions | Macroscopic flat dimensions, unoccupied or occupied; nothing is curled up |
| Quantum gravity | Nothing to quantize: gravity is sourced curvature, not a field |

---

## 7. What is open, said plainly

This edition states its open problems where they arise, in prose, and collects them in Part 6. The largest single one is stated here because it belongs to the foundation: the framework does not yet derive *from the equation of motion* why the particular fifteen standing waves that exist are the ones that fire. The sector list is physically grounded (Section 2); the mass law, given the modes, performs extraordinarily (Part 2); several of the mode indices are forced by exact relations among the others; and the spectrum's termination has a candidate physical mechanism — the electroweak sector can be read as a fixed total capacity that the four heaviest modes exactly saturate, leaving measurable but unfillable headroom, which would make a sixteenth particle not merely undiscovered but impossible to add. But the selection of the occupied levels as a consequence of the dynamics, rather than as a rule that closes and agrees with nature, remains the outstanding problem of the theory, and the reader should weigh the framework knowing that.

What the framework does claim at foundation level, it claims because the physics is doing the work: one wave, six binding sectors, observers made of the three-dimensional bricks, force as shared coordinates, mass as standing-wave pitch, gravity as sourced shape. Each of the Parts that follow takes one of these and confronts it with measurement.

---

*Second edition, 2026. The complete derivations, status accounting, and numerical verification underlying every claim here are maintained in the first-edition Parts 1–11 and the master computation record `files/idwt.py` at https://fedgeno.github.io/.*
