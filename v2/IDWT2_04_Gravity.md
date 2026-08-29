# Infinite Dimensional Wave Theory, Second Edition — Part 4: Gravity

## 0. What this Part teaches

By the end of this Part you can answer: what gravity is when there is no gravitational field; why a universe with infinitely many macroscopic dimensions shows a perfect inverse-square law with one universal constant — including the actual integral that proves it; why every test of extra dimensions comes up empty here and must; **what matter is actually doing along the axes we don't occupy** — why charged matter is forced to stay evenly spread there while only the neutral sectors could ever gather; why hidden-dimensional matter would pull on us at full strength while remaining invisible; why gravity sets the *size* of elementary particles; and where the honest edges of the gravitational story lie.

## 1. Gravity is what mass does to the manifold

In this framework gravity is not an interaction of the kernel type (Part 3) and not a field of any type. It is the curvature of $M_\infty$ itself, sourced by mass — by the wave's concentrated energy density. Where the wave holds a standing wave, the surrounding geometry is distorted; that distortion, measured by anything else, is gravity — complete. There are no gravitons because there is no gravitational field to have quanta; "quantizing gravity" has no subject here, not because the problem is hard but because one does not quantize a shape.

The direction of explanation matters and is easy to state. What a three-dimensional observer writes down — a metric on their spacetime obeying Einstein-type equations sourced by the masses they see — is the *observer's reconstruction* of the underlying phenomenon, and it works for every practical purpose. But the phenomenon itself is simpler than the reconstruction: a definite curvature assigned to a definite mass distribution, linearly and covariantly, so that the geometry inherits every symmetry of its source *exactly*. Translating the source translates its curvature identically; a source uniform along a direction yields geometry uniform along that direction, with no gradient — a fact we use hard in §4. The pathologies of the field-theoretic reading — singularity theorems as ontology, solution branches, metric non-uniqueness — belong to the reconstruction. Where a mass concentration grows dense enough that the observer's effective description develops a horizon, the underlying wave configuration remains a finite-energy, high-amplitude region; nothing physical becomes singular, and nothing is lost.

**And this reading has been tested from inside.** Since Part 3 derives every other force as wave interference, the honest question was asked of gravity too: could the universal attraction be the waves interacting at a distance — an intensity–intensity interference mediated by the wave's own background — rather than geometry? The computation says no, and the refusal is instructive. The static response of the wave's collective background to a localized pattern comes out *screened*: symbolically, $\chi(k,0) = -4m\,n_0/(k^2+\kappa^2)$, whose spatial form is $e^{-\kappa r}/4\pi r$ — a dented condensate heals itself over its stiffness length ($\sim10^{-3}$ fm here), so a wave-mediated static pull dies exponentially beyond it. Remarkably, the mediated force that *does* exist couples in proportion to $m_1m_2$ — the framework natively contains a short-range, equivalence-respecting attraction through its collective channel — but nothing wave-mediated reaches across a room, let alone a solar system. An infinite-range, unscreenable, all-sector force can only be what P5 says it is: not a pattern in the wave, but the shape of the manifold the wave lives on. Gravity is the one interaction that is *not* interference, and the framework proved that about itself.

The equivalence principle comes out as a two-line theorem rather than a postulate. Inertial mass is the sector eigenvalue $m_{{\rm scale},d}\,S(n,d)$ (Part 2). Gravitational mass is what sources curvature — the wave's energy density, integrated over the sector coordinates, which for a normalized mode is *the same eigenvalue times the same unit normalization*. The two masses are one number read twice, so $m_{\rm grav}/m_{\rm inertial} = 1$ for every species identically: no fifth force, no composition dependence, exactly as measured to parts in $10^{13}$.

## 2. The observed Newton constant, derived

### 2.1 The integral

Here is the computation that makes many-dimensional gravity look exactly like textbook gravity. A mass bound in sector $d$ sources, in its own $d$ dimensions, the $d$-dimensional potential $\sim 1/R_d^{\,d-2}$. A three-dimensional observer — uniform in the source's $k = d-3$ hidden coordinates (Part 1 §4) — does not sample that potential at one hidden point; it samples it *integrated over all of them*. With $r$ the observable separation and $\rho$ the hidden radial coordinate:

$$\Phi_{\rm obs}(r) \;\propto\; \int_{\mathbb{R}^k}\frac{d^k\rho}{\bigl(r^2+\rho^2\bigr)^{(d-2)/2}} \;=\; S_{k-1}\int_0^\infty\frac{\rho^{\,k-1}\,d\rho}{(r^2+\rho^2)^{(d-2)/2}} \;=\; \frac{C_k}{r},$$

because the surviving power of $r$ is $k-(d-2) = (d-3)-(d-2) = -1$ — for *every* $d$. (Same beta-function integral as the Coulomb projection of Part 3 §1.2; gravity and electromagnetism pass through the same funnel.) The falloff a three-dimensional observer measures is Newtonian whatever the dimensionality of the source.

### 2.2 The strength — sector-independence is a cancellation, and $4\pi$ is ours

The prefactor $C_k$ depends on the source's sector — but so does the normalization of the source's own $d$-dimensional Green's function, $(d-2)\,S_{d-1}$ with $S_{d-1}$ the unit-sphere area. Divide them and every trace of the source's dimensionality cancels:

$$\frac{C_k}{(d-2)\,S_{d-1}} = \frac{1}{4\pi} \qquad\text{identically, for } d = 3, 4, 5, 6, 10.$$

So a three-dimensional observer measures, from a source of *any* sector,

$$\Phi_{\rm obs}(r) = \frac{G_\infty\,m}{4\pi\,r}, \qquad \boxed{\,G_N = \frac{G_\infty}{4\pi}\,}$$

where $G_\infty$ is the manifold's one intrinsic stiffness — curvature per unit mass — and the $4\pi$ is the area of the *observer's* unit sphere: the signature of the measurer's three dimensions, not of the source. A six-dimensional electron and a ten-dimensional tau pull on us with exactly the same constant per unit scalar mass as a three-dimensional quark; no volume factors, no per-sector Newton constants, no dilution. One gravity, read through one window.

The dimensions beyond $d=10$ contribute nothing, and for a derived reason: nothing binds there (Part 1 §3.3), an empty dimension carries no mass, and an unsourced direction is flat. Gravity's reach across dimensions is finite because the *sources* are finite-dimensional, not because space is truncated.

## 3. Why every extra-dimension experiment comes up empty — and must

The framework claims macroscopic, infinite, flat hidden dimensions, and experiment has spent decades bounding extra dimensions: torsion-balance tests of the inverse-square law down to fifty microns, collider searches for gravitational missing energy, precision spectroscopy. All null. All consistent — necessarily — because every one of those bounds tests a specific package this framework does not contain:

- **No modified force law at short distance.** The Kaluza–Klein steepening of gravity below a compactification radius requires a compactification radius. There is none; §2's integral holds at every separation, so the measured force law is exactly $1/r^2$ at all scales. The torsion balances are measuring the projection theorem and confirming it.
- **No missing-energy channel.** Escaping gravitons require gravitons. Curvature is not a field; nothing radiates into the sector dimensions as an escaping quantum.
- **No tower of graviton modes.** The KK tower is the Fourier spectrum of a *periodic* compact dimension. The sector coordinates are infinite and flat, and the wave's states there are Gaussian-localized standing waves with a purely discrete spectrum (Part 1 §1.3) — the particle spectrum itself, already accounted for. There are no additional propagating modes to produce, miss, or bound.

And the hidden dimensions are not experimentally idle — they are detected daily, as the mass spectrum (Part 2): every fermion and boson mass *is* a measurement of standing waves in those dimensions. What the sectors do not produce is any further gravitational signature beyond the masses of their tenants, which is precisely what is observed.

## 4. Bound within, gradient-free without

Part 1 §4 established that a particle is uniform in every dimension beyond its own. Apply §1's covariance statement — geometry inherits the symmetries of its source — and the single most consequential gravitational fact follows:

**A mass pulls only in the dimensions it is bound in.** Along any direction where a source is uniform, the sourced geometry is translation-invariant: no gradient, no pull. So the electron sources a gravitational gradient in six dimensions, the tau in ten, a nucleon in exactly three — each object gravitates in its own home.

Three consequences, in ascending order of reach:

**Why our gravity is three-dimensional.** Ordinary matter — nucleons and everything assembled from them, planets, stars, instruments, us — is purely three-dimensionally bound (the colour-singlet theorem, Part 1 §5.1). Two such objects source and feel gradients only in the shared three dimensions: ordinary inverse-square gravity. We measure 3D gravity because our *sources* are 3D, not because gravity is.

**Nothing hides from gravity, and nothing is diluted.** Every massive mode, whatever its sector, is bound in $d=3$ as well (the nesting), so against ordinary matter it pulls through the shared three dimensions with its complete scalar mass — never a projected fraction. Mass is a Lorentz scalar here, never "partly in other dimensions": a higher-sector object is gravitationally an ordinary point mass to us, however much structure it carries in coordinates we cannot see.

**The dark-matter constraint — what dark matter cannot be, and could be.** The same theorem cuts in the other direction: a three-dimensionally bound detector is *uniform* in the hidden coordinates, so it feels exactly zero gradient from anything gravitating only in those dimensions, however massive. Dark matter therefore cannot be "gravity leaking from higher dimensions" — that channel is closed by theorem. What the geometry *does* naturally permit is mass that pulls on us at full strength through the shared three dimensions while staying electromagnetically dark. The framework owns the gap plainly: its fifteen-particle spectrum contains no dark-matter candidate, and it does not currently account for the astrophysical evidence — the structure makes gravitationally-honest, optically-dark matter natural, and has not produced the object.

## 5. Matter along the unseen axes

The extra coordinates are not a different kind of place. They are ordinary space — the same forces act along them, at the same strength, by the same laws. That single statement, taken seriously, answers a question the previous sections raise: *what is matter actually doing out there?* Work it out with a picture.

Take one of the three extra directions the electron lives in — call it axis 4 — and imagine plotting, on that single line, the position of every particle in a lump of iron.

**The protons plot as an even fog.** A proton is a colour-singlet composite, purely three-dimensionally bound (Part 1 §5.1). It has no structure along axis 4 — it is not *at* any point of the line but uniformly spread along all of it (§4's "bound within, free without"). The iron's entire positive charge, viewed along this axis, is a featureless smear: every point of the line carries the same amount of it.

**The electrons plot as dots.** An electron is a six-dimensional object; it genuinely has a position along axis 4. So the question with physical content is: what arrangement do those dots settle into?

In our three axes, the answer is "they clump" — into atoms, and atoms into planets. But look at *why* clumping is possible in our axes: each electron sits beside a proton, positive cancels negative locally, the neutral pair no longer repels anything, and neutral matter is then free to gather under gravity. **Along axis 4 that trick is impossible.** A proton has no position on the line, so an electron cannot pair with one there; no neutral lump can be built along that axis at all. Any cluster of electrons that began to form at some point of the line would be a bare ball of negative charge — every member pushing every other apart along the axis with the full Coulomb strength (the same forces act there), against gravity's pull at $10^{-42}$ of that strength. The cluster never forms. The equilibrium is the opposite: the electrons spread themselves as evenly as possible along the line, a charged gas filling a room it can never condense in, held flat by its own repulsion against a background of proton-fog it can never lock onto.

So along the unseen axes, the charged matter of the universe has no lumps, no structure, and no events — an enforced, permanent evenness. Three consequences:

- **Why you cannot make two electrons truly meet.** Genuine contact between two electrons means overlap in all six of their coordinates. But their mutual repulsion is holding them apart along the unseen axes at all times, exactly as strongly as along the seen ones — and no apparatus we can build (being made of proton-fog matter with no structure there) can push against it. The collision experiments of our accelerators are Coulomb deflections through the shared coordinates; six-coordinate contact is not hard to arrange, it is *actively prevented* by the same force that prevents it in plain sight.
- **Why the unseen axes look empty.** Not because nothing is there — every electron in the universe extends through them — but because evenness is invisible. A uniform spread sources no gradients (§4), scatters nothing, and shadows nothing. Structure is what can be seen, and structure is exactly what charge forbids there.
- **The one exception: the neutral sectors.** A neutrino has positions along its extra axes and *no charge* — nothing pushes neutrino from neutrino apart out there. For neutrino positions along the unseen axes, gravity is the only force acting, and gravity gathers. If anything in the universe forms lumps along the axes we do not occupy, it is the neutrino background: falling together in the coordinated, all-axes-at-once way gravity moves everything (a body attracted along several axes moves along all of them in one geodesic motion, not axis by axis). Whether that clustering actually proceeds at cosmological timescales, and whether it bears on the dark-sector questions of §4, is a computation the framework has posed and not completed — a lead, recorded as such, not a result.

The moral of the section is your own three axes read backwards: matter clumps *here* because neutrality is possible here. Where neutrality cannot be built, matter is condemned to smoothness — and smoothness is why the rest of the manifold, though as real and as inhabited as our slice, has nothing in it to see.

## 6. Gravity sizes the particles

An unexpected division of labor between the framework's two dimensional inputs: the electron mass prices the spectrum (Part 2), and gravity sizes the particles. A particle is a stiffness-bound standing wave, and the stiffness of the space it stands in is $1/G_\infty$; balancing the mode's inertia against the well curvature (linear in the mode's mass $M$, with the in-sector gravitational coupling $G_d = G_\infty/[(d-2)S_{d-1}]$ — at $d=3$ exactly $G_N$, anchoring the scale) gives the physical radius

$$R_{n,d} = \sqrt{N + d/2}\;M^{-1/4}\,G_d^{3/8}, \qquad N = n-1.$$

Evaluated for the electron: $R_e \approx 1.0\times10^{-29}$ m. Every elementary mode lands at $10^{-29}$–$10^{-30}$ m — sixteen orders below its Compton wavelength, eleven below the tightest compositeness bounds, with heavier particles *smaller* (the $M^{-1/4}$). Every elementary particle is pointlike far below any resolved scale, clearing all electron-substructure and $g-2$ constraints wholesale. The femtometre sizes of nuclear physics are *composite* extents — three confined quark modes and their colour field — not single-particle widths; a proton is big the way a molecule is big, not the way its constituents are.

## 7. The honest edges

**The strength of gravity is an input.** The framework derives gravity's structure — sourced curvature, the universal $1/r$, sector-independence, $G_N = G_\infty/4\pi$, equivalence as a theorem — but not the magnitude of $G_\infty$. It is the second and last dimensional input, alongside $m_e$. And there is no hierarchy problem lurking between the two, because they are not two entries on one scale: the kernel couplings are the wave's self-interaction, $G_\infty$ is the manifold's stiffness, and the famous "why is gravity so weak" ratio compares quantities of different kind that never meet in a formula. The framework declines to be embarrassed by a ratio it never forms. (The Higgs-mass fine-tuning problem also does not arise: masses are integer state counts, and an integer cannot receive a small continuous correction.)

**The cosmological constant is open.** The unoccupied dimensions contribute exactly zero vacuum energy — no bound modes, no condensate, a derived silence. But the occupied sectors' condensates carry real vacuum energy, and no derived mechanism yet explains the observed smallness of the cosmological term. The problem is *confined* — localized to six sectors instead of infinitely many — but not solved, and this edition says so rather than gestures.

**Cosmology is a program, not a result.** Relic abundances, structure formation, the expansion history: the gravitational picture here is a statement about sources and geometry, not yet a history of the universe. Together with dark matter (§4), these are the framework's largest owned absences.

What is not open: everywhere gravity is actually measured — laboratory to solar system — this picture reproduces the record whole. Newtonian gravity with one universal constant, exact equivalence, no fifth force, no deviation at any tested distance: all from the single statement that mass curves the manifold it is bound in, read by three-dimensional readers.

---

*Second edition, 2026. Full derivations and machine verification: first-edition Part 4 at https://fedgeno.github.io/; the computation record `idwt-v2.py` is distributed with these documents.*
