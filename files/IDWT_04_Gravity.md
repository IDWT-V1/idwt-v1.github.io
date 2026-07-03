# Infinite Dimensional Wave Theory — Part 4: Gravity

---

## 1. Gravity is Curvature of $M_\infty$ Caused by Mass

Gravity is not a 3D phenomenon, and not a 10D phenomenon. It is a property of the full infinite-dimensional geometry of $M_\infty$. When $\Psi_\infty$ has a stable concentrated feature — a massive particle — the surrounding $M_\infty$ geometry is distorted. That distortion is gravity. What a 3D observer calls gravitational attraction is their restricted view of that ∞D curvature, measured at their $d=3$ coordinate level.

Gravity is not a field. There are no gravitons, no spin-2 boson, no propagating gravitational degree of freedom, and no gravitational action separate from the geometry of $M_\infty$. Gravity is geometry responding to mass.

IDWT's macroscopic sector dimensions are consistent with all known gravitational experiments: the absence of any experimental bound on the sector length scale follows structurally, because the experimental bounds presuppose a Kaluza-Klein tower that IDWT does not contain (§1b).

---

## 1b. Why Macroscopic Sector Dimensions Are Consistent with All Experiment

Every experimental constraint on extra dimensions assumes a KK tower. IDWT has no KK tower. The constraint category does not exist in IDWT.

**The standard argument and why it does not apply.** The Eöt-Wash torsion balance tests Newton's law below 50 microns and sees no deviation. Precision atomic spectroscopy (hydrogen 1S–2S) tests the energy levels of the electron — a $d=6$ sector excitation of $\Psi_\infty$ inhabiting six macroscopic spatial dimensions — to $10^{-15}$. Collider experiments search for missing energy from KK graviton emission. All of these null results are taken to exclude macroscopic extra dimensions.

Every one of these exclusions has the same hidden assumption: gravitons can propagate into the sector space, producing a KK tower of massive graviton modes with masses $m_n = n/R$. At distances $r < R$, Newton's law changes from $1/r^2$ to $1/r^{2+d}$. At colliders, KK gravitons are produced and escape.

IDWT has none of this structure:
- There are no gravitons — gravity is curvature of $M_\infty$ caused by mass, not a field with quanta (§1)
- There is no KK tower — sector modes are exponentially localised bound states, not plane waves (§3.9)
- At any macroscopic distance from the source, the sector mode is already suppressed as $\exp(-r^2/L_d^2)$, where $L_d = \lambda_d^{-1/4}$ is the harmonic oscillator localization length
- The gravitational effect measured by a 3D observer is $G_{\mu\nu} = 8\pi G\, T_{\mu\nu}^{\rm eff}$, with $T_{\mu\nu}^{\rm eff}$ indistinguishable from a point mass (§3.2–3.6)

**The sector dimensions are detected.** They produce the entire observed particle mass spectrum via $m = m_{\rm scale,d} \times S(n,d)$. The sectors are not invisible — they are the origin of all fermion and boson masses. What they do not produce is any additional gravitational signature, because the sector-space geometry contributes to gravity only through the observer's stress-energy of the particles it hosts.

**Why no other signatures appear.** The physical modes are exactly the exponentially localised bound states of each sector potential. Any mode that would propagate through $\Xi$ — a scattering state with $E \geq \lambda_d$ — is non-normalizable, hence not a bound-state eigenmode, and is absent from the physical spectrum. There are no bulk modes, no KK excitations above the particle spectrum already identified, and no missing energy channels at any collider energy.


---

## 2. Newtonian Limit

In the weak-field, static, non-relativistic limit:

$$\nabla^2\Phi = 4\pi G_N \cdot S(n,d) \cdot |\psi_{\rm 3D}(r)|^2$$

This is the Poisson equation of Newtonian gravity with mass $m = S(n,d) \times m_{\rm scale,d}$. It follows directly from $\rho_m = \int|\Psi_\infty|^2 d\xi$ — the Born-rule definition of observable matter density.

---

## 3. Gravity on $M_\infty$: Source, Structure, and the 3D Observer's Measurement 🔶

This section establishes what gravity is in IDWT and describes the effective gravitational equation that a 3D observer at fixed $\xi^0$ in $M_\infty$ would measure.

### 3.1 Gravity as Curvature of $M_\infty$ Sourced by Mass

Gravity in IDWT is curvature of $M_\infty$ caused by mass. The mass of a mode $(n,d)$ is $m(n,d) = S(n,d) \times m_{\rm scale,d}$ — a count of sector microstates, the mode's dimensional complexity (dimensional inertia). A concentration of that dimensional inertia distorts the geometry of $M_\infty$, and that distortion is what gravity is.

There is no postulated gravitational field, no graviton, and no separate gravitational action written by hand. The $M_\infty$ action contains the matter term:

$$S_{\rm matter} = \int_{M_\infty} \bar\Psi_\infty \left(i\Gamma^\mu\nabla_\mu + i\Gamma^a\partial_a\right)\Psi_\infty\,d\mu_{M_\infty}$$

The gravitational coupling on $M_\infty$ is $G_\infty$, the curvature-per-unit-mass of the manifold; a 3D observer measures $G_N = G_\infty/(4\pi)$ (§3.12.2). The absolute value of $G_\infty$ is not derived from the combinatorics — it is a second dimensional input alongside $m_e$ (§3.12.4).

The sector-space geometry $h_{ab}(\xi)$ is a fixed background — not a dynamical field. There is nothing gravitational to vary in $\Xi$, so no wave equation exists in the sector directions and no KK graviton tower appears.

**What a 3D observer perceives.** A 3D observer at fixed $\xi^0$ cannot access the full $M_\infty$ geometry. They measure the effect of ∞D curvature at their $d=3$ coordinates. That measurement takes the effective form of a gravitational equation — something that looks like Newton's law at low energies or Einstein's field equation more generally. This effective description is valid for the observer's practical purposes but is not the underlying phenomenon. The phenomenon is ∞D curvature sourced by mass.

### 3.2 The Observer's Effective Gravitational Equation

A 3D observer who constructs a gravitational equation from their measurements finds it sourced by $T_{\mu\nu}^{\rm eff}$ — the full sector-space integral of the matter stress-energy. Varying $S_{\rm matter}$ with respect to the spacetime metric $g_{\mu\nu}(x)$ that the observer uses to describe their $d=3$ spacetime:

$$\frac{\delta S_{\rm matter}}{\delta g^{\mu\nu}} = \sqrt{-g}\int_\Xi T_{\mu\nu}^{\rm Dirac}(x,\xi)\,d\mu_\xi = \sqrt{-g}\,T_{\mu\nu}^{\rm eff}(x)$$

where $T_{\mu\nu}^{\rm Dirac}(x,\xi)$ is the standard Dirac stress-energy at each sector coordinate $\xi$. The observer's effective gravitational equation is:

$$G_{\mu\nu}(x) = 8\pi G_N\,T_{\mu\nu}^{\rm eff}(x), \qquad T_{\mu\nu}^{\rm eff}(x) \equiv \int_\Xi T_{\mu\nu}^{\rm Dirac}(x,\xi)\,d\mu_\xi$$

where $G_N = G_\infty/(4\pi)$, with $G_\infty$ the curvature-per-unit-mass of $M_\infty$ and the $4\pi$ the ordinary three-dimensional Newtonian coefficient (§3.12.2). This equation correctly describes the observer's measurements. It is the 3D observer's read of ∞D curvature sourced by mass — not a fundamental equation of IDWT.

The gravitational source is the full sector-space integral of the matter energy density. No $R^{(\Xi)}$ curvature enters the right-hand side: the sector geometry is a fixed background, not an independent gravitational source.

The effective stress-energy has three contributions:
1. **Occupied modes** (particles): $T_{\mu\nu}^{\rm matter} = \sum_i m_i u_\mu u_\nu \delta^3(x-x_i)/\sqrt{-g}$
2. **Kernel contribution**: positive for colour non-singlet configurations; zero for singlets (confinement)
3. **Vacuum** from unoccupied modes: $\Lambda_{\rm eff}$ (see §4)

### 3.3 Connecting to the Mass Spectrum

For mode $(n,d)$, separating the sector eigenmode $\chi_{n,d}(\xi)$ from the spacetime field $\psi(x)$ via $\Psi_\infty(x,\xi) = \psi(x) \otimes \chi_{n,d}(\xi)$ with $D_\Xi \chi_{n,d} = m_{\rm eff} \chi_{n,d}$ gives mass $m_{\rm eff} = m_{\rm scale,d} \times S(n,d)$. The effective stress-energy factorises:

$$T_{\mu\nu}^{\rm eff}(x) = T_{\mu\nu}^{\rm obs}[\psi](x)\times\int_\Xi|\chi_{n,d}(\xi)|^2\,d\mu_\xi = T_{\mu\nu}^{\rm obs}[\psi](x)\times\|\chi\|^2_\Xi$$

For $L^2$-normalised modes ($\|\chi\|^2_\Xi = 1$), the observer's effective gravitational equation sources by a massive Dirac field with mass $m_{\rm eff} = m_{\rm scale,d}\times S(n,d)$:

$$G_{\mu\nu}(x) = 8\pi G_N\,T_{\mu\nu}^{\rm obs}[\psi](x)$$

The sector dimensions have contributed their mass to this source and do not appear as an independent gravitational term. Mass is the only channel through which the sector-space geometry enters the observer's gravitational measurement.

### 3.4 Why There Are No Additional Gravitational Degrees of Freedom

Gravity is geometry, not a field. Geometry does not have quanta. There are no gravitons because there is no gravitational field to quantize — there is only $M_\infty$ curvature caused by mass. This is not an additional assumption; it follows from what gravity is in IDWT.

More specifically: the sector-space geometry $h_{ab}(\xi)$ is a fixed classical background. It is not dynamical, has no equation of motion, and does not vary. There are therefore no fluctuations $\delta h_{ab}$, no wave equation in $\Xi$, and no KK graviton tower. The sector space enters the observer's gravitational measurement exactly once — through $T_{\mu\nu}^{\rm eff}(x)$, the integrated matter stress-energy, which encodes the mass of each particle and nothing else.

The question of cross-terms between different sector-space coordinates — $\delta^2 S/\delta g_{\mu\nu}(\xi_a)\,\delta g_{\rho\sigma}(\xi_b)$ for $a\neq b$ — does not arise: the 3D observer constructs a single metric $g_{\mu\nu}(x)$ on their $d=3$ spacetime, not a family parameterised by $\xi$. The coupling $\int_\Xi T_{\mu\nu}\, d\mu_\xi$ is already the $\xi$-integrated source; there is no per-leaf metric.

### 3.5 Boundary Terms on Non-Compact $\Xi$

For macroscopic (non-compact) $\Xi$, the variation of $\int_\Xi \cdots\, d\mu_\xi$ by parts requires boundary conditions as $|\xi| \to \infty$.

Physical modes are bound states of the harmonic sector potential $V(\xi) = \lambda_d r^2$ (Part 4 §3.10). Bound states decay as a Gaussian: $|\chi_{n,d}(\xi)| \sim P(|\xi|)\exp(-\sqrt{\lambda_d}|\xi|^2/2)$ for $|\xi| \to \infty$ (polynomial $\times$ Gaussian). Boundary terms in the integration by parts that yields the field equations therefore vanish. The action integral is well-defined despite the non-compact domain.

Non-normalizable (scattering) modes do not satisfy this condition — they are not bound-state eigenmodes of the sector potential and are absent from the physical spectrum. The bound-state normalizability condition automatically selects precisely the modes for which the sector-space integrals converge.

### 3.6 The Equivalence Principle

Inertial mass enters through the sector eigenvalue: $m_{\rm inertial} = m_{\rm scale,d} \times S(n,d)$.
Gravitational mass enters through $T_{\mu\nu}^{\rm eff}(x) = T_{\mu\nu}^{\rm obs}[\psi] \times \|\chi\|^2_\Xi$.

Both carry the same sector normalisation factor $\|\chi\|^2_\Xi$. For normalised modes:

$$m_{\rm inertial} = m_{\rm grav} = m_{\rm scale,d}\times S(n,d)$$

This holds for all modes with the same $(n,d)$ regardless of $\xi^0$. The sector mode-function normalization $W_S = |\chi(\xi^0)|^2/\|\chi\|^2_\Xi$ cancels from the inertial-to-gravitational mass ratio. All particle species have $m_{\rm grav}/m_{\rm inertial} = 1$. No fifth force. No composition-dependent gravitational coupling.

### 3.7 Status of Formal Items

| Item | Status | Reference |
|---|---|---|
| $L^2(\Xi)$ normalisability of $\chi_{n,d}$ | ✅ proved | §3.13 Part I |
| Bianchi identity: $\nabla^\mu T_{\mu\nu}^{\rm eff} = 0$ | ✅ proved unconditionally | §3.13 Part II |
| Spectral theorem: $S(n,d) = N_d(n-1)$ | ✅ proved | Part 8 §3 |
| $\lambda_d$ from kernel self-consistency | ✅ derived: $\lambda_d = (g_{dd}/2)^{2/3}$ | §3.10 |
| $L_d = \lambda_d^{-1/4}$ as sector length scale (harmonic oscillator length) | ✅ defined and computed | §3.9, §3.10.4 |
| $G_N$ sector-independent; no sector correction | ✅ | §3.11–3.12.2 |
| $G_N = G_\infty/(4\pi)$: the $4\pi$ is the 3D Green's-function constant, sector-independent (§3.12.2); $G_\infty$ is a second dimensional input, absolute scale not derived (open) | ✅/🔶 | §3.12.2 |
| Bound within, gradient-free without: the gravitational gradient lives only in a source's bound dimensions | ✅ (exact — the curvature sourced by mass inherits the source's symmetries by translation-covariance of the Poisson sourcing, §3.8) | §3.8 |

Where a mass concentration is large enough that the $d=3$ observer's effective description develops an apparent horizon, the full $M_\infty$ geometry — the curvature sourced by that mass — stays regular. What the observer reads as a singularity is a finite-energy high-amplitude region in the sector-space coordinates. Information is preserved globally.

---

## 3.8 Bound Within, Gradient-Free Without

A sector-$d$ particle is localized (bound) in the coordinates $x_1,\dots,x_d$ and uniform (free) in every coordinate $x_j$ with $j>d$ (Part 1 §3h–3i). "Uniform" means constant nonzero amplitude: the particle is present everywhere in those higher coordinates, not absent from them.

**The gravitational gradient lives only in the bound coordinates. ✅** Gravity is the curvature of $M_\infty$ sourced by the stress-energy $T$ (P5). If a particle's configuration is translation-invariant along $x_j$ — as it is in every coordinate it is uniform in — then $T$ is translation-invariant along $x_j$, and so is the geometry it sources: $\partial_j g_{\mu\nu} = 0$. A direction of uniformity of the source is a Killing direction of the sourced geometry, so there is no curvature gradient and no geodesic deviation along it. A uniform source exerts no pull along the direction it is uniform in. This is the gravitational counterpart of the kernel no-bath result — the wave is uniform in its outer coordinates, so outer translations are exact symmetries and the coupling width into that continuum is zero (Part 7 §1.2, `files/idwt.py` STEP 64). The argument is exact at the linearized level. There is no separate nonlinear step to promote, because IDWT gravity is not a self-gravitating dynamical field with its own solution space. It is $\infty$D curvature sourced by mass, whose 3D read is the linear Poisson law $\nabla^2\Phi = 4\pi G_N\rho_m$ with $\rho_m = \int|\Psi_\infty|^2\,d\xi$ (§3.1). The sourcing of curvature by mass is translation-covariant by construction: translating the mass distribution translates the curvature it sources identically. A mass density uniform in $x_j$ therefore sources a geometry uniform in $x_j$ — exactly, with no gradient and no pull — and for the linear Poisson law this is immediate and unconditional, since the Newtonian Green's function is translation-invariant and a source independent of $x_j$ has the unique decaying potential independent of $x_j$ (`files/idwt.py` STEP 138). **✅** The general-relativistic worry about strong-field solution branches and non-uniqueness of the metric does not arise: that belongs to the metric treated as an independent self-interacting field, which is the 3D observer's effective reconstruction (§3.1), not the IDWT phenomenon. IDWT assigns a definite curvature to a definite mass distribution, and that assignment carries every symmetry of the source.

> **Bound within, gradient-free without.** Mass-energy is present in every dimension, but the attractive gradient — the part of gravity that pulls — exists only in the dimensions the mass is localized in.

**Each object gravitates in its own bound dimensions.** A sector-$d$ mass sources a curvature gradient in $d$ dimensions, not three: the electron ($d=6$) gravitates in six, the neutrino ($d=5$) in five, the tau ($d=10$) in ten. Gravity is not collapsed to $d=3$; it is bound to each source's own sector.

**Observed 3D gravity is a consequence, not a postulate.** Ordinary matter — colour-singlet baryons and the observers built from them — is pure $d=3$-bound (Part 1 §2.4; confinement projects out the $d=4$ index). Two $d=3$-bound sources therefore source and feel a curvature gradient only in the shared $d=3$, which is ordinary inverse-square gravity. A $d=3$ observer measures 3D gravity because the sources available to it are $d=3$-bound.

**Two-body gravity acts in the shared bound dimensions.** Sources $A$ (sector $d_A$) and $B$ (sector $d_B$) gravitate in their shared bound dimensions $\min(d_A,d_B)$ — the same nesting that governs kernel contact (Part 3 §0.8). In any dimension above $d_A$ the source $A$ is uniform and sources no gradient there, even against a $B$ that is localized in it. By the nesting $\Xi_3\subset\Xi_4\subset\dots\subset\Xi_{10}$, every massive mode is bound in $d=3$ as well, so against a $d=3$ source it sources the full-mass gradient in the shared $d=3$: a hidden-sector mass pulls on ordinary matter with its complete scalar mass, never a reduced part. Mass stays a Lorentz scalar — never projected.

**Strength is the scalar mass, not enhanced in higher dimensions.** The gravitational charge is the Lorentz scalar $m$, identical in every bound dimension; $G_N$ is sector-independent (§3.11). A higher-sector pair has more directions of mutual approach, each carrying the same $m$-strength gradient — more directions, not more attraction.

**Finite reach by source-binding.** Every particle is uniform beyond its own sector and every sector satisfies $d\le 10$, so nothing sources a curvature gradient in the $d>10$ vacuum dimensions. The observed reach of gravity is finite because the gravitating sources are finite-dimensional in their binding — not because curved space is truncated and not because a coupling is diluted over a volume.

---

## 3.9 The Sector Localization Length — No Compactification Needed

**$L_d$ is the sector localization length — not a compactification radius.** IDWT has no compact extra dimensions, no periodic boundary conditions, no Kaluza-Klein tower. The space $\Xi$ is limitless. $L_d$ is the characteristic width of the sector ground-state Gaussian in the sector direction (the harmonic oscillator length), derived from the self-consistency equation for $\lambda_d$ in §3.10.

**What $L_d$ is:**

Every physical mode $\chi_{n,d}$ is a bound state of the sector Schrödinger operator $H_d = -\Delta_{\Xi_d} + \lambda_d r^2$ (the harmonic self-binding potential derived in §3.10.2). The ground-state mode is a Gaussian:

$$\chi_0(r) \propto \exp\!\left(-\tfrac{\sqrt{\lambda_d}}{2}r^2\right)$$

with characteristic width set by the **harmonic oscillator length**:

$$L_d \equiv \lambda_d^{-1/4}$$

This is the IDWT analogue of the Bohr radius. Like $a_0 = \hbar^2/m_e e^2$, $L_d$ is not a compactification radius — it is the localization width of the ground-state sector mode in an infinite flat space. At any distance $r \gg L_d$, the mode amplitude falls as a Gaussian $\exp(-r^2/L_d^2)$, making the mode activity in that sector negligible to any observer in the $d=3$ subspace.

**Localization length, ground-state energy, and dimensionless coupling.** The $d$-dimensional harmonic oscillator ground state has energy:

$$E_0 = d\sqrt{\lambda_d}$$

and the harmonic oscillator has no continuum ($\sigma_{\rm ess} = \emptyset$) — the spectrum is purely discrete with no scattering threshold. The natural dimensionless coupling is:

$$\hat\lambda_d \equiv \lambda_d\times L_d^2 = \lambda_d^{1/2} = \sqrt{\lambda_d}$$

Values:

| $d$ | $\lambda_d$ | $E_0 = d\sqrt{\lambda_d}$ | $L_d = \lambda_d^{-1/4}$ | $\hat\lambda_d = \sqrt{\lambda_d}$ |
|---|---|---|---|---|
| 2 | 50.723 | 14.244 | 0.375 | 7.122 |
| 3 | 4.820 | 6.586 | 0.675 | 2.195 |
| 4 | 1.726 | 5.255 | 0.872 | 1.314 |
| 5 | 0.164 | 2.025 | 1.571 | 0.405 |
| 6 | 0.250 | 3.000 | 1.414 | 0.500 |
| 10 | 0.250 | 5.000 | 1.414 | 0.500 |

**Why experimental bounds do not apply.** All experimental constraints on macroscopic extra dimensions — Eöt-Wash torsion balance, precision spectroscopy, ISL tests — assume a Kaluza-Klein tower of modes with masses $m_n = n/R$ and modified gravitational potential at distances $r \sim R$. In IDWT:

- There is no KK tower (no periodic modes, no 1/R quantization)
- The sector modes are exponentially localized bound states, not plane waves
- At any laboratory distance $r \gg L_d$, the mode is already Gaussian-suppressed as $\exp(-r^2/L_d^2)$; with the physical single-mode localization now predicted microscopic ($\sim10^{-29}$ m, §3.9a) the suppression is extreme at every accessible scale
- No deviation from $1/r^2$ gravity occurs at any accessible scale
- The gravitational interaction appears standard to the observer: $G_{\mu\nu} = 8\pi G\, T_{\mu\nu}^{\rm eff}$ with $T_{\mu\nu}^{\rm eff}$ indistinguishable from a standard point mass

The hydrogen spectroscopy bound of 6 mm was computed assuming KK modes modify the hydrogen energy levels. With no KK modes, no such bound exists.

## 3.9a The Physical Size of an Excitation — the Stiffness Well 🔵

The $L_d$ above is the *dimensionless* sector localization length (the kernel shape $\lambda_d^{-1/4}$, in sector-coordinate units). The **absolute physical size** of a single-mode excitation is the first observable that requires *both* IDWT dimensional inputs — $m_e$ (through the mode mass $M$) and $G_\infty$ (the stiffness of space). Treating the mode as a harmonic oscillator in its sector well fixes it:

$$R_{n,d} = \sqrt{N + d/2}\,(\mu\kappa)^{-1/4} = \sqrt{N+d/2}\; M^{-1/4}\, G_d^{3/8}, \qquad N = n-1,$$

with inertia $\mu = 1/\sqrt{G_d}$ (the rigidity *as a mass*, not a frequency) and well curvature $\kappa = M/G_d$ (curvature = mass $\times$ stiffness, linear in $M$). The per-dimension gravitational coupling $G_d$ is **derived, not free**: gravity is the one rigidity $1/G_\infty$ acting through the $d$-dimensional geometry, so the in-sector Newtonian coupling is $G_d = G_\infty/[(d-2)\,S_{d-1}]$ (the §3.12 in-sector Green's function, with $S_{d-1} = 2\pi^{d/2}/\Gamma(d/2)$ the unit $(d-1)$-sphere area). **At $d=3$ this is $G_\infty/4\pi = G_N$ exactly** — our measured 3D gravity is the anchor, so the absolute scale is fixed. The dimensionless kernel shape $\lambda_d$ **cancels** from the physical size, and the sector factor is the derived $s_d = [(d-2)\,S_{d-1}]^{3/2}$. (idwt.py STEP 121.)

Numerically the electron ($d=6$/$\mathbb{CP}^3$) is $R_e \approx 1.0\times10^{-29}$ m, and **every** elementary mode lands at $10^{-29}$–$10^{-30}$ m: sub-Compton by ~16 orders, ~11 orders below the electron compositeness bound ($\sim10^{-18}$ m), heavier $\Rightarrow$ smaller ($M^{-1/4}$). So $G_\infty$ sets the scale — **$G_\infty$ does set elementary-particle size** — and every elementary particle is a pointlike single mode far below any resolved size, clearing all compositeness, $g\!-\!2$, and spectroscopy bounds. (The microscopic localization also *strengthens* §3.9: a mode confined to $10^{-29}$ m is even more invisible to a $d=3$ observer.)

**Status — derived (🔵), modulo one founding premise.** With $G_d$ fixed by the universality of gravity across dimensions ($d=3$ is not special; gravity is the same in every direction, anchored to the measured $G_N$), both the sector-dependence $s_d = [(d-2)S_{d-1}]^{3/2}$ and the overall scale are *derived* — no free coefficient, no wall-blocked constant. What remains is one premise, the framework's own ontology: a particle is a stiffness-bound standing wave whose well curvature is linear in the mode mass, $\kappa = M/G_d$. (A purely scale-covariant action gives an $M$-independent size, so the $M^{-1/4}$ scaling is the physical content of "stiffness-bound standing wave," not a free input.) The competing branches are excluded by data: self-gravity ($\kappa \propto G_\infty M^2$) gives the electron $\sim10^{31}$ m, $\mu = M$ gives the wrong $M^{-1/2}$, and a Compton-scale size violates the compositeness bound.

**Two distinct scales — single mode versus composite.** The $\sim10^{-29}$ m here is the size of a *single* elementary mode. It does not conflict with the $\sim$fm scale that appears for hadrons: the proton's $0.84$ fm charge radius is the *composite* confinement extent of three quark modes (Part 8 §11), not a single-mode width. For a single mode, charge extent and mass extent coincide (both $|\chi|^2$), and for elementary modes both equal the tiny $R_{n,d}$ above. (The reference tables that quote $L_d$ directly in fm for the *leptonic* sectors — Part 1 §3e — predate this result and are pending revision to the dimensionless sector unit; the fm values remain the correct *composite/hadronic* unit only for the confining sectors.)


---

## 3.10 Derivation of $\lambda_d$ from the Kernel Self-Consistency Equation

$V_d$ is not postulated. The sector field on $\Xi_d$ carries the action's quartic self-coupling — the $(\xi_d\cdot\xi')^2$ kernel of §3.10.1 — and the sector potential is the **Euler–Lagrange (self-consistent) reduction** of that coupling: the stationary point of the explicit energy functional written in §3.10.5. The subsections below carry out that reduction — the self-coupling integral gives a *global* harmonic potential $V_d(r) = \lambda_d r^2$ (§3.10.2), and self-consistency fixes $\lambda_d = (g_{dd}/2)^{2/3}$ from the seed-built coupling alone (§3.10.3). The harmonic **form** is therefore a derived consequence of the action, not an independent ansatz.

### 3.10.1 Structure of the Inter-Sector Kernel

The $M_\infty$ action includes a bilinear inter-sector coupling kernel. From Part 2 §1, the kernel acts as:

$$K(\xi,\xi') = \sum_{d,d'} g_{dd'}(\xi_d\cdot\xi_{d'})^2$$

where $\xi_d$ is the $d$-dimensional component of the sector coordinate $\xi$, and $g_{dd'}$ is the coupling matrix (rank-1 in IDWT: $g_{dd'} = v_d v_{d'}$ with $v_d = \sqrt{g_{dd}}$).

For a mode localised in sector $d$, the effective potential arises from averaging the kernel over the background field configuration:

$$V_{\rm eff}(\xi_d) = \int|\Psi_\infty(x,\xi')|^2 K(\xi_d,\xi')\,d\mu_{\xi'}$$

The self-coupling term ($d' = d$) dominates for modes that are well-localised in sector $d$:

$$V_{\rm self}(\xi_d) = g_{dd}\int_{\Xi_d}|\chi_d(\xi')|^2(\xi_d\cdot\xi')^2\,d\mu_{\xi'}$$

**Covariance note — the cross-sector terms are contact terms.** The covariance question settled for the self-term in §3.10.2 applies equally to the cross terms $g_{dd'}(\xi_d\cdot\xi_{d'})^2$, and here the answer is forced rather than chosen. For two modes A (sector $d$, centroid $X_A$, per-component shared-subspace variance $a^2$) and B (sector $d'$, centroid $X_B$, variance $b^2$, separation $R = X_A - X_B$, shared subspace dimension $d_{\rm sh}$), every two-point covariant reading of the cross term fails on established physics ✅:

*Absolute frame:*
$$U_0/g = (X_A\cdot X_B)^2 + b^2|X_A|^2 + a^2|X_B|^2 + d_{\rm sh}a^2b^2 \quad\text{[changes under global translation]}$$

*Pair-centroid frame:*
$$U_1/g = |R/2|^4 + (a^2+b^2)|R/2|^2 + d_{\rm sh}a^2b^2 \quad\text{[mutual quartic confinement of every pair]}$$

*Each-own frame:*
$$U_2/g = d_{\rm sh}a^2b^2 \quad\text{[R-independent: clustering fails]}$$

The absolute reading is not a function of the separation at all; the pair-centroid reading would give the electron–proton pair a kernel energy $\sim10^{18}$ in sector units at $R = a_0$, against the observed Coulomb-only interaction; the each-own-frame reading leaves every pair in the universe coupled at full contact strength at any distance. The only covariant reading that survives is contact-gated:

$$U(R) = g_{dd'}\times\Omega(R)\times d_{\rm sh}\,a^2b^2, \qquad \Omega(0)=1,\quad\Omega\ \text{decaying on the mode-width scale}$$

The $(\xi_d\cdot\xi_{d'})^2$ factor is the local geometry of the coupling at a contact event, evaluated in the contact frame — which is exactly how every coupling computation in these documents uses it, so all established values are $\Omega(0) = 1$ evaluations and unchanged. The contact structure of the kernel (Part 3 §0.6; Part 11 §6.3) is therefore a structural consequence of covariance, not an assertion.

The gate profile follows from the established structure as well ✅. Three inputs fix it uniquely: the kernel term is bilinear in the kernel currents ($L_{dd'} = (g_{dd'}/2)\int(\xi_d\cdot\xi_{d'})^2 J^d J^{d'}$, Part 3 §0.6) — linear in each mode's intensity — so the pair energy is a bilinear functional $U = \iint\rho_A(x)\rho_B(y)F(x-y)$; covariance and the exclusions above force $F$ to decay; and the action supplies no length constant of its own — the $g_{dd'}$ are dimensionless seed-built numbers — so $F$ has zero intrinsic range, the scale-free point contact. The gate is therefore the normalized density overlap:

$$\Omega(R) = \frac{[\rho_A\star\tilde\rho_B](R)}{[\rho_A\star\tilde\rho_B](0)}$$

For Gaussian sector ground modes, $\Omega(R) = \exp(-R^2/(2(a^2+b^2)))$, contact range $\sqrt{a^2+b^2}$. Corollary, exact: a same-sector pair has contact range $\sqrt{2\sigma_d^2} = \lambda_d^{-1/4} = L_d$ — the sector localization length is the same-sector contact range (e–e: $L_6$, the range of Part 11 §6.3; nucleon–nucleon at $d=3$: $L_3 = 0.675$, taken up quantitatively in Part 8 §11). The $d=3$–$d=4$ quark pair has range 0.78 in sector units, the sub-femtometre strong-force scale. Long-range physics is untouched: electromagnetism is carried by the massless, non-compact $d=2$ zero mode (Part 3 §16, §0.8a), to which no width gate applies, and gravity is $M_\infty$ curvature (§1). At $A = B$, $R = 0$ the gated form reduces to the §3.10.2 self-term. (`files/idwt.py` STEP 59, STEP 60.)

### 3.10.2 Evaluating the Self-Coupling

By rotational symmetry in $\Xi_d$, the angular average of the dot product satisfies:

$$\langle(\xi_d\cdot\xi')^2\rangle_{\rm angles} = |\xi_d|^2\,|\xi'|^2/d$$

Therefore:

$$V_{\rm self}(r) = g_{dd}\times\frac{\langle r'^2\rangle_d}{d}\times r^2$$

where $r = |\xi_d|$ and $\langle r'^2\rangle_d = \int_{\Xi_d} r'^2|\chi_d(\xi')|^2\,d\mu_{\xi'}$ is the mean-square sector radius of the ground-state mode. This gives a harmonic potential $V_{\rm self}\propto r^2$ — which is the confining potential itself, $V_d = \lambda_d r^2$ (the saturating form once posited here is dropped; see the note below), with:

**Note on the potential functional form (the harmonic form is derived; MC-2 potential piece resolved).** This is global and exact, not a near-origin fit. For any isotropic localised density $|\chi_d|^2$, the angular identity $\langle(\xi_d\cdot\xi')^2\rangle_{\rm angles} = |\xi_d|^2|\xi'|^2/d$ holds for **all** $\xi_d$ — it is the $\ell=0$ projection of the quadratic kernel, the traceless $\ell=2$ part averaging to zero against an isotropic density (Part 9 T2). So $V_{\rm self}(\xi_d) = \lambda_d|\xi_d|^2$ identically, and the pure harmonic $V_d(r) = \lambda_d r^2$ is the **Euler–Lagrange (self-consistent) solution** of the sector action's quartic self-coupling (§3.10.5), not a separately adopted shape. It is confining (purely discrete spectrum, $\sigma_{\rm ess} = \emptyset$), reproduces the IDOS $S(n,d)$ exactly in every sector, and makes the §3.10.3 self-consistency exact. (The earlier saturating form $\lambda_d r^2/(1+r^2)$ is dropped — it supports no localized bound state in $d=5$, $6$, $10$, the neutrino/charged-lepton/tau sectors, so it cannot host the spectrum.) The one standing assumption is the isotropy of the self-consistent ground state — which closes, since the ground state of $\lambda_d r^2$ is itself isotropic; the $\ell=2$ anisotropy enters only for non-spherical excited modes. This settles the **potential-form** piece of MC-2. The remaining MC-2 action items reduce to **one** question: the Dirac-operator form ($D = D_t + D_\Xi$ vs mixed) is equivalent to the product metric being exact (a clean split holds iff there are no cross-terms; Part 1 §1.1, Appendix A §9), so what stays open is the exactness of $M_\infty = \mathbb{R}_t \times \Xi_\infty$ — settled only by the coupled $(\Psi_\infty,\{M_d\})$ fixed point (🔶, Part 6).

$$\lambda_d = g_{dd}\times\frac{\langle r'^2\rangle_d}{d}$$

**Covariance note — the well rides with the mode.** The self-coupling integral above is written in absolute sector coordinates. Read literally — the well anchored at the origin of $\Xi_d$ — it assigns a mode of internal spread $s$ whose centroid sits at $X$ the displacement energy

$$\frac{U_A(X)}{g_{dd}} = |X|^4 + \frac{2s^2}{d}|X|^2 + \frac{s^4}{d}$$

(exact for an isotropic mode density), a quartic pinning to the sector origin. That reading is excluded by the framework's own established results ✅: it forbids macroscopic motion outright, and at hydrogen's Bohr radius the pinning term ($\sim10^{18}$ in sector units, against $E_0 = 3$) would obliterate the Bohr spectrum of Part 8 §14.2. The physical evaluation is in the mode's frame: displacements in the self-term are taken relative to the mode centroid,

$$V_{\rm self}(\xi) = g_{dd}\int|\chi_d(\xi')|^2\bigl((\xi-X)\cdot(\xi'-X)\bigr)^2\,d\mu_{\xi'}, \qquad X = \text{mode centroid}$$

This is the minimal covariant completion of the kernel's written form 🔶. It leaves the derivation above and every number in §3.10.3–§3.10.4 unchanged — the computation in this section is carried out at X = 0, in the mode frame, so all published values are frame-local — while restoring translation covariance on the flat sector space. The well then travels with the excitation: the displacement energy is $U_B = g_{dd} s^4/d$, independent of X, the centroid propagates freely with $E^2 = P^2 + m^2$ (Part 1 §3i), and a boosted self-bound mode translates rigidly with the well co-moving (verified dynamically; the absolute-kernel counterpart oscillates pinned about the origin). Bound within, free without (Part 1 §3i) accordingly reads: bound about its center in all $d$ sector dimensions; the center free in all of them. The compact internal structure corrects the point-center hydrogen Hamiltonian only through its smearing, $\Delta E/|E_{1s}| = 4(L_6/a_0)^2 \approx 2.9\times10^{-9}$ — the order of the proton-finite-size items of Part 8 §14.4. (`files/idwt.py` STEP 58.)

### 3.10.3 The Self-Consistency Equation

The mode $\chi_d$ is itself the ground state of $H_d = -\Delta_\Xi + V_{\rm conf}$, so $\langle r'^2\rangle_d$ is determined by $\chi_d$. For the $d$-dimensional harmonic oscillator ground state with scale parameter $l = \lambda_d^{-1/4}$:

$$\langle r^2\rangle_d = \frac{d}{2\sqrt{\lambda_d}}$$

Substituting into $\lambda_d = g_{dd}\langle r'^2\rangle_d/d$:

$$\lambda_d = \frac{g_{dd}}{2\sqrt{\lambda_d}} \implies \lambda_d^{3/2} = \frac{g_{dd}}{2} \implies \lambda_d = \left(\frac{g_{dd}}{2}\right)^{2/3}$$

This is the self-consistency condition: the sector potential depth is determined by the sector self-coupling constant alone, which is itself determined by the Euler characteristic and seed structure.

### 3.10.4 Results for All Sectors

| $d$ | $g_{dd}$ | $\lambda_d = (g_{dd}/2)^{2/3}$ | $E_0 = d\sqrt{\lambda_d}$ | $L_d = \lambda_d^{-1/4}$ | $\hat\lambda_d = \sqrt{\lambda_d}$ |
|---|---|---|---|---|---|
| 2 | 722.5 | 50.723 | 14.244 | 0.375 | 7.122 |
| 3 | $8\sqrt{7} \approx 21.17$ | 4.820 | 6.586 | 0.675 | 2.195 |
| 4 | $12/\sqrt{7} \approx 4.54$ | 1.726 | 5.255 | 0.872 | 1.314 |
| 5 | $96/722.5 \approx 0.133$ | 0.164 | 2.025 | 1.571 | 0.405 |
| 6 | 1/4 | 0.250 | 3.000 | 1.414 | 0.500 |
| 10 | 1/4 | 0.250 | 5.000 | 1.414 | 0.500 |

$E_0 = d\sqrt{\lambda_d}$ is the exact ground-state energy of the $d$-dimensional isotropic harmonic oscillator. $L_d = \lambda_d^{-1/4}$ is the oscillator length (Gaussian width of the ground state). $\hat\lambda_d = \sqrt{\lambda_d}$ varies across sectors; the previous claim $\hat\lambda_d \approx 1$ was an artifact of the saturating-potential ansatz (MC-2) and does not hold for the harmonic self-binding operator derived in §3.10.2.

### 3.10.5 The vacuum functional whose stationary point is $\lambda_d$

The §3.10.1–§3.10.3 derivation is the stationarity condition of a single explicit energy functional on the sector field. Writing $\Psi$ for the sector amplitude on $\Xi_d$,

$$E[\Psi] = \int_{\Xi_d}|\nabla\Psi|^2\,d\mu + \frac{g_{dd}}{2}\iint(\xi\cdot\xi')^2|\Psi(\xi)|^2|\Psi(\xi')|^2\,d\mu\,d\mu' \tag{1}$$

Variation $\delta E/\delta\Psi^* = \mu\Psi$ gives the Gross–Pitaevskii form $-\Delta\Psi + V_{\rm self}[\Psi]\Psi = \mu\Psi$ with $V_{\rm self}$ the §3.10.2 mean field; the isotropic average reproduces $V_{\rm self} = \lambda_d r^2$ and the self-consistency $\lambda_d = (g_{dd}/2)^{2/3}$. **The functional (1) exhibits the sector closure as its stationary point — the soap-bubble fixed point of the wave–well loop. ✅** (= §3.10.3.)

Expanding $\Psi = \sum_n A_n\chi_n$ in the well's own modes (ground state $n=1$, level $N=n-1$, $\varepsilon_n = (2(n-1)+d)\sqrt{\lambda_d}$) puts the functional in coupled-mode form,

$$E[\{A_n\}] = \sum_n\varepsilon_n|A_n|^2 + \frac{g_{dd}}{2}\sum_{N_1+N_2=N_3+N_4}K_{n_1n_2n_3n_4}\,A^*_{n_1}A^*_{n_2}A_{n_3}A_{n_4} \tag{2}$$

with K the $(\xi\cdot\xi')^2$ overlap, nonzero only on the $l = 0 \oplus l = 2$ channel. Two features of (2) are exact and structural. The quartic term enforces the index resonance N1+N2 = N3+N4: the generation-tower production edges are four-wave-resonant in the mode index (⭐) — the spectrum is an index-locked four-wave comb on the condensate. Its $l=0 \oplus l=2$ content is the l-parity rule: the ground mode connects only to even levels, so the conservative flow of (2) populates the even-level ladder and excludes the odd levels exactly (⭐, Part 7 §1.2).

What the functional does **not** do is select the occupancy. Its stationary point fixes the well ($\lambda_d$); its quartic term fixes the four-wave comb structure; but the choice of which modes occupy the comb — the co-fixed-point selection (Part 9 T0.5) — is not a minimum of (1)/(2). The conservative Gross–Pitaevskii flow of (2) from the condensate reproduces the l-parity cut and the first injection (ground → up) and then spreads amplitude across the whole even ladder without isolating the tower (🔶/🔵). The even-level selection is therefore not a property of this vacuum functional; it is the radiative-stability statement of Part 7 §1.2 — which even modes are protected against decay through the downward kernel links. The functional (1) is the well closure and the comb kinematics; the occupancy selection is a separate, radiative question — the positive firing-set (Part 9 T0.5 / MC-4), which reduces to the coupled ($\Psi_\infty$, $\{M_d\}$) fixed point. Sector membership itself (Rule A) is fixed by the deposit grid (Part 1 §3a; `idwt.py` STEP 100), not by this functional; it is settled and distinct from the firing-set, and distinct again from Open Theorem A (the operator-theoretic recovery of the sector set from $\hat C$, Part 6).

The condensate structure does settle one of those radiative channels directly. Linearizing the functional about the $n=1$ ground state gives a real Hessian $\mathrm{diag}(4(\mu-\varepsilon_1),\,0)$: the amplitude fluctuation is gapped and the phase fluctuation is the exact $U(1)$ Goldstone of the condensate. The $n=1$ mode is the symmetry-broken vacuum — its only zero-energy fluctuation is the gauge phase, so it carries no populatable positive-energy excitation and cannot serve as a radiation final state. The up quark is the unique tower member whose downward link $(3,4)\to(1,4)$ terminates on a ground mode, so its stability follows from the condensate alone, independent of the occupancy selection (`files/idwt.py` STEP 92). ✅

### 3.10.5a The excitation amplitude is fixed, not free 🔵

The functional (1) determines not only the well depth but the amplitude of a single excitation. Writing the conserved $U(1)$ charge $Q = \int_{\Xi_d}|\Psi|^2$ explicitly, the stationary well depth is $\lambda_d(Q) = (g_{dd}Q/2)^{2/3}$; the published self-consistency $\lambda_d = (g_{dd}/2)^{2/3}$ (§3.10.3) is exactly the $Q=1$ case — the $L^2$-normalised mode it was derived from already fixed the charge to one quantum. The amplitude was therefore settled the moment the well was, and is not an additional free parameter. For a Gaussian sector mode at unit charge the field amplitude is finite in every sector,

$$A = \lambda_d^{d/8}/\pi^{d/4}, \qquad |\Psi(0)|^2 = A^2,$$

with $A = 0.0635$ in the electron sector ($d=6$). The excitation thus has a definite, finite height. The *absolute* physical amplitude still carries the one-quantum normalisation — the quantum of action, §3.10.5c — so only the dimensionless shape amplitude is fixed here. (`files/idwt.py` STEP 122.)

### 3.10.5b The mass is the integrated density of states ✅

The mode mass $M = m_{\rm scale,d}\,S(n,d)$ is a *cumulative state count*, not a single eigenvalue. The combinatorial degeneracy $S(n,d) = \binom{n+d-1}{d} = \sum_{k=0}^{n-1}\binom{k+d-1}{d-1}$ is exactly the cumulative number of $d$-dimensional isotropic harmonic-oscillator states up to level $N=n-1$, since $\binom{k+d-1}{d-1}$ is the level-$k$ degeneracy. The sector well is therefore harmonic with no anharmonic correction: the apparently anharmonic $d=3$ tower $1,10,35,84,165$ (gaps the odd squares) is the parity-selected odd-$n$ subsequence, while the full sequence $1,4,10,20,35,\dots$ has smooth triangular gaps. The mass — a count growing as $N^d$ — and the size-law radial factor $\sqrt{N+d/2}$ — a single-level rms radius (§3.9a) — are two consistent readings of the same harmonic well at the same level $N$; there is no harmonic-versus-anharmonic seam. The absolute energy scale is the single input $m_e$ ($m_{\rm scale,6} = m_e/S(n_e,6)$). (`files/idwt.py` STEP 123; Theorem S1, Part 8 §5.1.) The count $S(n,d)$ remains exactly harmonic in every sector; in the colour-carrying sectors ($d=3,4$) the per-state energy softens weakly with level due to confinement binding — a physically distinct effect that leaves $S(n,d)$ untouched (`files/idwt.py` STEP 127; Part 2 §11.9).

### 3.10.5c The amplitude normalisation is the quantum of action 🔵

A spontaneous decay produces one daughter quantum, and the rate is set by the seed occupation $a_f^2$ of that final mode (Part 6; `files/idwt.py` STEP 105). This is the one quantum of §3.10.5a, fixed by the unit conserved charge $Q=1$, which is invariant under a global rescaling $\Psi\to c\Psi$ (the charge transforms as $Q\to c^2 Q$, so unit charge is $c$-independent). It is therefore not a free per-decay amplitude but the single universal quantum of action — the role $\hbar$ plays in a quantised theory, here supplied as the definition of one excitation. A purely classical field does not produce this normalisation on its own; it is the one genuine physical import beyond the dimensionless sector structure (`files/idwt.py` STEP 125). The contentful inputs of the framework are dimensionless — the gravitational coupling $G_\infty m_e^2 \approx 2.2\times10^{-44}$ and the integer seeds — and a single Compton-scale anchor with $c$ converts them to physical times and lengths; $\hbar$ enters only inside that anchor (as the Compton frequency $m_e/\hbar$ and length $\hbar/m_e c$), never alone.

### 3.10.6 The sector self-consistency hierarchy

The structure of §3.10 reflects a three-level self-consistency in the particle spectrum, each level a distinct fixed-point condition on a different aspect of the field.

**Level 1 — Potential depth (✅, §3.10.3).** The sector potential well is self-sourced: $\lambda_d = (g_{dd}/2)^{2/3}$ is the fixed point of the kernel mean-field on the mode's own density. The mass scale $m_{\rm scale,d}$ and localization length $L_d$ of each sector are outputs of this self-consistency, not inputs. The functional (1) above is the explicit variational statement of this fixed point. The mass scale $m_{\rm scale,d}$ and localization length $L_d$ of each sector are outputs of this self-consistency, not inputs. The functional (1) above is the explicit variational statement of this fixed point.

**Level 2 — Active sector set (✅, Part 1 §3a T3).** Which values of $d$ carry matter is governed by the Sector Set Theorem. Gegenbauer criticality (Rule B, ✅), Euler-characteristic seeding (✅), and Hopf consistency (T9a–c, ✅) together give the conditions for sector activation. Their mechanisms are not uniform: $d=8$ and $d=9$ carry no matter through seed-unmatched Euler characteristics, and $d=7$ carries none because it is not a corner of the deposit grid (Rule A, 🔵; `idwt.py` STEP 100). A matter-empty sector is inert and needs no further arbiter — exactly as $d=11,12,\ldots$ need none. The active sectors $D = \{2,3,4,5,6,10\}$ are the set at which matter resides.

**Level 3 — Physical mode indices (🔶, Part 9 T0.5, MC-4).** Within the active sectors, odd-level modes are excluded by an exact l-parity zero (⭐), and even-level non-members are excluded by a strictly positive irreversible radiative width into the spacetime-momentum continuum (✅, idwt.py STEP 118). Which even-level modes survive as the 15 physical particles is the co-fixed-point condition T0.5. As §3.10.5 makes explicit, this selection is not a stationary point of the Level-1 functional, nor a consequence of Level-2 criticality; it is a radiative stability question whose sufficient derivation is the framework's principal open problem (MC-4).

Each level determines a distinct piece of the spectrum — potential depth, active dimensions, particle indices — and the three together constitute the full sector self-consistency of $\Psi_\infty$ on $M_\infty$.

---

## 3.11 Newton's Constant: Sector-Independence

### 3.11.1 $G_{\rm eff}$ from Sector Mode Normalisation

From the variational derivation (§3.2), the effective stress-energy factorises as:

$$T_{\mu\nu}^{\rm eff}(x) = T_{\mu\nu}^{\rm obs}[\psi](x)\times\|\chi_d\|^2_{\Xi_d} = T_{\mu\nu}^{\rm obs}[\psi](x)$$

for $L^2$-normalised modes. The normalisation condition $\|\chi_d\|^2 = 1$ absorbs the sector volume into the mode function. The value of the mode at the observer address $\xi^0$ is:

$$|\chi_0^d(\xi^0)|^2 \equiv |\chi_0^d(0)|^2$$

(setting $\xi^0 = 0$ by translational freedom). For a $d$-dimensional ground-state sector mode with localization length $L_d$:

$$|\chi_0^d(0)|^2 \propto L_d^{-d}$$

This is exact for the Gaussian ground state; corrections for the actual sector potential are $O(1)$ numerical factors.

### 3.11.2 The Effective Newton's Constant

After sector mode normalisation ($\|\chi_{n,d}\|^2_\Xi = 1$), the effective stress-energy reduces to the standard observer form (§3.3). A 3D observer who constructs a gravitational equation from their measurements obtains:

$$G_{\mu\nu}(x) = 8\pi G_N\,T_{\mu\nu}^{\rm obs}[\psi](x)$$

$G_N$ is the same for all sectors — sector-independent by the $L^2$ normalisation argument. All particles, regardless of which sector they inhabit, source the observer's effective curvature with the same $G_N$. This is the equivalence principle (§3.6) as a theorem.

**Status of $G_N$.** $G_N$ is not a coupling constant in a fundamental gravitational action — there is no such action written by hand in IDWT. $G_N$ is what a 3D observer measures of $\infty$D curvature: $G_N = G_\infty/(4\pi)$, with $G_\infty$ the curvature-per-unit-mass of $M_\infty$ and the $4\pi$ the ordinary three-dimensional Green's-function constant, sector-independent (§3.12.2). Gravity is not quantized; there are no gravitons; there is no quantum gravitational threshold in this framework. The $d>10$ vacuum dimensions do not enter $G_N$ — confirmed by Ricci-flat vacuum in $d > 10$ (no particle sources, so $R_{ab}=0$) and by T5. The absolute value of $G_\infty$ is a second dimensional input, not derived (open, §3.12.4).

---

## 3.12 Newton's Constant — No Sector Correction

### 3.12.1 Why Sector Fluctuations Do Not Correct $G_N$

A legitimate concern with any multi-sector theory is whether integrating out sector-space degrees of freedom produces corrections to the Einstein-Hilbert term. In standard Kaluza-Klein theories this always occurs: the compact space volume multiplies $M_{\rm Pl}$ and becomes a dynamical modulus. The induced correction is:

$$M_{\rm Pl}^{\rm obs,eff} = M_{\rm Pl}^{\rm 6D}\times\sqrt{\mathrm{Vol}(\text{compact space})}$$

**IDWT has a different structure that forbids this correction.**

The functional determinant of the sector operator $O_\Xi$ contributes a term:

$$\Gamma_\Xi = \tfrac{1}{2}\,\mathrm{Tr}_\Xi[\log O_\Xi], \qquad O_\Xi = -D_\Xi^2 + V_d(\xi)$$

Via the Seeley-DeWitt heat kernel expansion, this yields terms of the form:

$$\Gamma_\Xi \sim \int_\Xi\!\left[a_0 + a_2 R_\Xi + a_4 R_\Xi^2 + \cdots\right]d\mu_\xi$$

**Note (non-compact caveat).** The standard Seeley-DeWitt expansion and the coefficient formulas $a_0, a_2, a_4$ are derived for compact Riemannian manifolds. IDWT's sector spaces $\Xi_d$ are non-compact (confinement is from $V_d(r)$, not compactness). The no-correction argument below relies only on the decoupling $\delta\Gamma_\Xi/\delta g_{\mu\nu}=0$, which follows from the product metric structure and is independent of whether the Seeley-DeWitt coefficients retain their standard compact-manifold form. The argument is therefore valid as stated.

The $a_2$ term, proportional to the Ricci scalar $R_\Xi$ of the sector manifold, is the one that would correct the observed Planck mass in a KK theory.

**The key: $O_\Xi$ is independent of $g_{\mu\nu}$.**

$O_\Xi = -D_\Xi^2 + V_d(\xi)$ acts on functions of $\xi$ only. It depends on the sector metric $h_{ab}(\xi)$ and the sector potential $V_d$, but has no dependence on the spacetime metric $g_{\mu\nu}(x)$. This follows from the effective product structure in the $d=3$ observer's description of $M_\infty$, where cross-terms between spacetime and sector coordinates are negligible:

$$ds^2_{M_\infty} \approx g_{\mu\nu}(x)\,dx^\mu\,dx^\nu + h_{ab}(\xi)\,d\xi^a\,d\xi^b$$

In the full metric $G_{AB}dX^A dX^B$ on $M_\infty$, off-diagonal terms $G_{\mu a}$ would in principle couple the spacetime and sector blocks. Their absence in the observer's effective description is what makes $O_\Xi$ independent of $g_{\mu\nu}$ — and therefore what ensures $G_N$ receives no sector correction. The product structure is derived at vacuum level from the action's own symmetries (MC-2, `files/idwt.py` STEP 133, weak-field rigor): the vacuum's spatial isotropy and time-reversal invariance force the cross-blocks of its stress tensor to vanish, and the stationary metric inherits this by the §3.8 uniqueness argument. The no-graviton and no-KK-tower statements rest on that vacuum structure; the sourced curvature inherits the vacuum's symmetries exactly, by translation-covariance of the mass-sourcing (§3.8, `files/idwt.py` STEP 138) — this is not a nonlinear-metric uniqueness question, since IDWT gravity is $\infty$D curvature sourced by mass, not a self-interacting field with a solution space of its own. Therefore:

$$\frac{\delta}{\delta g_{\mu\nu}}\mathrm{Tr}_\Xi[\log O_\Xi] = 0 \quad\text{[exactly]}$$

$\Gamma_\Xi$ is a constant with respect to $g_{\mu\nu}$ — it contributes a fixed cosmological term (already absorbed into $\Lambda_{\rm eff}$) but no correction to $G_N$.

**Why IDWT differs from Kaluza-Klein.** In KK theories, the higher-dimensional metric $G_{MN}$ is a single dynamical object. Its spacetime and extra-dimensional components mix through moduli fields — the compact space fluctuates and gravitons propagate into the sector space. Integrating out these fluctuations produces the observed Planck mass, and the resulting KK excitation tower is excluded by Eöt-Wash and LHC searches.

In IDWT, there is no graviton propagating anywhere. Gravity is curvature of $M_\infty$ caused by mass — not a field with quanta. The sector manifolds $\Xi_d$ are macroscopic spatial dimensions in which $\Psi_\infty$ vibrates; $h_{ab}(\xi)$ is a fixed classical background metric, has no equation of motion, and does not mix with the 3D observer's metric. There are no moduli, no metric fluctuations in $\Xi_d$, and no KK graviton tower. All KK-exclusion bounds presuppose graviton propagation into the sector space; they do not apply to IDWT.

**Conclusion.** $G_N$ as measured by a 3D observer receives no correction from sector fluctuations. The decoupling of $\Gamma_\Xi$ from $g_{\mu\nu}$ follows from the fixed-background structure of $\Xi$, which is a consequence of gravity being $\infty$D curvature sourced by mass rather than a dynamical field in $\Xi$.

---

### 3.12.2 $G_N$ as the 3D Measurement of Infinite-Dimensional Gravity

The previous subsections show that $G_N$ is sector-independent (§3.11) and not corrected by sector fluctuations (§3.12.1). Neither addresses the causal origin of $G_N$. This section establishes the correct logical direction: gravity is a phenomenon of the full $M_\infty$, not a 3D or 10D field appended to the particle physics. $G_N$ is what a 3D observer at $\xi^0$ measures of it.

**Gravity has no sector boundary.** Every other force acts within a specific sector (EM and weak in $d=2$, strong in $d=4$). Gravity is the unique exception — it has no sector confinement because it is curvature of $M_\infty$ itself, the space in which all sectors live. A force confined to $d=4$ cannot reach a $d=2$ particle. Gravity reaches everything because everything lives in $M_\infty$.

**Mass encodes dimensional complexity; gravity couples through it.** The mass formula $m(n,d)=S(n,d)\times m_{\rm scale,d}$ assigns mass proportional to the count of sector microstates in sector $d$. More dimensions means exponentially more microstates: the photon ($d=2$, ground-state massless — two transverse polarisations, no excited microstates) barely couples to gravity; the tau ($d=10$, $S(23,10)=64\,512\,240$) couples strongly. Gravity couples to each particle through that particle's dimensional complexity, which is encoded in its mass. There is no separate gravitational rule per sector — the mass formula already carries the dimensional structure, and gravity couples to mass.

**$G_N$ as a measurement.** A 3D observer measures the $M_\infty$ curvature sourced by a particle of sector $d$. By bound-within, free-without (Part 1 §3h–3i), the observer is uniform in the $k=d-3$ hidden coordinates of that source, so it does not sample the source's field at a single hidden point — it samples the field integrated over all of them. For the $d$-dimensional potential $\sim 1/R^{d-2}$ of a localized mass (with $R^2 = r^2 + \rho^2$, $r$ the observable distance and $\rho$ the hidden distance), the integral over the $k$ hidden coordinates is

$$\int_{\mathbb{R}^k}\frac{d^k\rho}{(r^2+\rho^2)^{(d-2)/2}} = \frac{C_k}{r}, \qquad C_k = \frac{\pi^{(d-2)/2}}{\Gamma\!\left(\tfrac{d-2}{2}\right)}.$$

The hidden coordinates integrate away and leave a $1/r$ potential for every sector: the falloff a 3D observer measures is Newtonian, whatever the dimension of the source. ⭐

**The strength is sector-independent.** The prefactor $C_k$ depends on the sector, but it cancels the $d$-dimensional Green's-function normalization $(d-2)\,S_{d-1}$ exactly, where $S_{d-1} = 2\pi^{d/2}/\Gamma(d/2)$ is the area of the unit $(d-1)$-sphere:

$$\frac{C_k}{(d-2)\,S_{d-1}} = \frac{1}{4\pi}\qquad\text{identically for every } d\in\{3,4,5,6,10\}.$$

A 3D observer therefore measures, for a source of any sector, the Newtonian potential

$$\Phi_{3D}(r) = \frac{G_\infty\,m}{4\pi\,r}, \qquad G_N = \frac{G_\infty}{4\pi}.$$

The $4\pi$ is the area of the observer's own unit 2-sphere — the ordinary 3D Green's-function constant. It is the signature of the observer's three dimensions, not the source's $d$: the source's extra dimensions integrate away, and a 3D observer always lands on $S_2 = 4\pi$. The gravitational coupling is the scalar mass $m$, $G_N$ is sector-independent (§3.11), and no volume factor appears. The source's hidden structure — set by its localization lengths $L_d$ (§3.9) — fixes the shape of the source in the hidden coordinates, but integrates out to the full mass by Gauss's law, leaving only the universal $4\pi$. A $d=6$ electron and a $d=10$ tau each pull on a 3D observer as a plain Newtonian mass. ✅

**The $d>10$ vacuum dimensions do not enter.** Every particle is uniform beyond its own sector, and all sectors satisfy $d\le 10$, so nothing sources a curvature gradient in the $d>10$ vacuum dimensions: a uniform source is translation-invariant and exerts no pull along the directions it is uniform in (§3.8) — the same translation symmetry that closes the $d>10$ bath (Part 7 §1.2). The observed $G_N$ is finite not because curved space is truncated but because the gravitating sources are finite-dimensional in their binding: a vacuum dimension carries no mass and is Ricci-flat ($R_{ab}=0$), so it sources no curvature.

**Status.** The $d>10$ vacuum dimensions do not enter — confirmed by both the Ricci-flat vacuum argument and T5. Gravity is structurally complete: it is curvature of $M_\infty$ sourced by mass, with $G_N = G_\infty/(4\pi)$ sector-independent. The one quantity not derived is the absolute scale $G_\infty$ (equivalently $G_N$), which is a **second dimensional input** alongside $m_e$ (§3.12.4); reducing this to one input would require an independent geometric determination of $G_\infty$, not available in the present construction.

---

### 3.12.3 Gravitational Coupling Ratios

The sector localization lengths $L_d$ (from §3.9, §3.10) fix the shape of each source in its hidden coordinates; that shape integrates out of the observed coupling, leaving the sector-independent Newtonian $G_N = G_\infty/(4\pi)$ (§3.12.2). Mass itself is the resonant frequency $m = m_{\rm scale,d} \times S(n,d)$, fixed entirely by the sector coupling constants and mode index; the $d=5$ neutrino sector has the smallest sector mass scale $m_{\rm scale,5}$ because the $d=5$ sector has no self-confinement ($\chi(S^5)=0$) and its frequency scale is set by the cross-sector Hopf consistency equation $m_{\rm scale,5} \times m_{\rm scale,4}^2 = (n_u/n_s) \times m_{\rm scale,6}^3$ — a frequency-domain relation among sector couplings.

Once $G$ is fixed by one measurement, all gravitational forces $F = G m_1 m_2/r^2$ between any two IDWT particles are predicted by the mass formula $m = m_{\rm scale,d} \times S(n,d)$. No additional parameter is needed.

**Summary of the gravity programme status:**

| Result | Status |
|---|---|
| Spacetime Einstein equations from $M_\infty$ action | ✅ §3.1–3.4 |
| No additional gravitational propagating modes | ✅ §3.4 |
| Equivalence principle: $m_{\rm grav} = m_{\rm inertial}$ | ✅ §3.6 |
| Boundary terms vanish on non-compact $\Xi$ | ✅ §3.5 |
| $L^2(\Xi)$ normalisability via sector mode localization theorem | ✅ §3.13 Part I |
| Bianchi identity $\nabla^\mu T_{\mu\nu}^{\rm eff} = 0$ | ✅ §3.13 Part II |
| Spectral counting $S(n,d) = N_d(n-1)$ | ✅ Part 8 §3 |
| Sector length $L_d$ = sector localization | ✅ §3.9 |
| $\lambda_d = (g_{dd}/2)^{2/3}$ from kernel | ✅ §3.10 |
| $G_N$ sector-independent; no sector correction | ✅ §3.11–3.12.1 |
| $G_N = G_\infty/(4\pi)$; sector-independent (the $4\pi$ is the 3D Green's-function constant, §3.12.2); $G_\infty$ a second dimensional input, absolute scale not derived (open) | ✅/🔶 §3.12.2 |

---

### 3.12.4 $G_\infty$ Numerically and the Second Dimensional Input

**The numerical value of $G_\infty$.** The relation $G_N = G_\infty/(4\pi)$ (§3.12.2) immediately gives $G_\infty$ once $G_N$ is known. Using the measured Newton's constant $G_N = 6.674 \times 10^{-11}$ m$^3$ kg$^{-1}$ s$^{-2}$:

$$G_\infty = G_N \times 4\pi = 8.43 \times 10^{-44}\ \mathrm{MeV}^{-2}.$$

This is not a prediction — it is what $G_\infty$ must equal, given the current input of one measured gravitational coupling. It becomes a prediction only if $G_\infty$ is derived independently from the geometry.

**$G_\infty$ is a second dimensional input. ✅** What §3.12.1–3 establish is the *structure* of gravity: it is curvature of $M_\infty$ sourced by mass; a 3D observer measures the sector-independent Newtonian law $\Phi_{3D} = G_\infty m/(4\pi r)$; the sector functional determinant does not correct it; and no sector volume enters. What they do **not** provide is the absolute value of $G_\infty$. The framework's dimensional inputs are therefore exactly **two** — $m_e$, which sets every particle mass through the sector scales, and $G_\infty$ (equivalently $G_N$), which sets the gravitational scale — with all dimensionless structure following from $N_c=3$. The two scales are different kinds of quantity and are never compared: there is no hierarchy to explain between them, and IDWT does not derive the magnitude of $G_\infty$ from the combinatorics. Reducing the count to one input would require an independent geometric determination of $G_\infty$ — for instance from beyond-product cross-sector metric mixing ($G_{\mu a}\neq 0$) — which is not available in the present construction.

**What does not belong here.** The Kaluza-Klein formula $M_{\rm Pl}^2 = M_*^9 V_7^{\rm phys}$ (which would define an "11D fundamental scale" $M_*$) is not IDWT. It requires compact extra dimensions, graviton propagation through those dimensions, and a Kaluza-Klein tower of massive graviton modes — all of which are explicitly excluded by Part 4 §1b. IDWT has no compact dimensions ($\Xi$ is non-compact), no graviton quanta (gravity is geometry, not a field), and no KK tower. The formula does not apply, and $M_*$ is not a quantity that appears in this framework.

---

## 3.13 Covariant Conservation of $T_{\mu\nu}^{\rm eff}$

**Theorem (Bianchi, unconditional).** Let $\Psi_\infty$ be a physical IDWT mode — any normalizable bound-state eigenmode — with sector-factorized form $\Psi_\infty(x,\xi) = \psi(x)\otimes\chi_{n,d}(\xi)$. Then:

$$\nabla^\mu T_{\mu\nu}^{\rm eff}(x) = 0$$

The proof proceeds in two parts: first establishing that all physical modes are $L^2(\Xi)$, then using that to close the Bianchi identity.

---

### Part I — $L^2(\Xi)$ Normalisability of Physical Modes

**Lemma (harmonic spectrum is purely discrete).** For the sector Schrödinger operator $H_d^{\rm harm} = -\Delta_{\mathbb{R}^d} + \lambda_d r^2$:

$$\sigma_{\rm ess}(H_d^{\rm harm}) = \emptyset$$

The spectrum is purely discrete: $\sigma(H_d^{\rm harm}) = \{(2N + d)\sqrt{\lambda_d} : N = 0, 1, 2, \ldots\}$ with finite multiplicity $C(N+d-1, d-1)$ at each level $N$.

**Proof.** The potential $\lambda_d r^2 \to \infty$ as $r \to \infty$. By Rellich's criterion, the resolvent $(H_d^{\rm harm} - z)^{-1}$ is compact for all $z \notin \sigma(H_d^{\rm harm})$, which implies $\sigma_{\rm ess} = \emptyset$. The eigenvalues follow from separation into radial and angular parts: the radial equation reduces to the $d$-dimensional isotropic harmonic oscillator, whose eigenvalues are $(2n_r + l + d/2)\cdot 2\sqrt{\lambda_d}$ with $n_r = 0,1,\ldots$ and $l = 0,1,\ldots$; the principal level $N = 2n_r + l$ has cumulative degeneracy $C(N+d-1,d-1)$, giving infinitely many discrete eigenvalues. □

**Theorem (sector mode Gaussian decay).** Every eigenfunction $\chi_{n,d}$ of $H_d^{\rm harm}$ satisfies:

$$|\chi_{n,d}(r)| \leq P_n(r)\times\exp\!\left(-\tfrac{\sqrt{\lambda_d}}{2}r^2\right)$$

where $P_n$ is a polynomial of degree $n-1$ (the generalised Laguerre $\times$ angular-harmonic factor).

**Proof.** Eigenfunctions of the d-dimensional harmonic oscillator are products of generalised Laguerre polynomials and solid harmonics times the Gaussian $\exp(-\sqrt{\lambda_d}\,r^2/2)$. Since $P_n$ is a polynomial, it grows at most as a power, and the Gaussian dominates for all r. □

**Corollary ($L^2$ normalisability).** Every eigenfunction $\chi_{n,d}$ is square-integrable on $\mathbb{R}^d$:

$$\|\chi_{n,d}\|^2_{\mathbb{R}^d} = \int_{\mathbb{R}^d}|\chi_{n,d}(\xi)|^2\,d\xi \leq C_n\int_0^\infty r^{d-1+2(n-1)}e^{-\sqrt{\lambda_d}\,r^2}\,dr < \infty$$

for all $d\geq 1$ and all $n\geq 1$. Compactness of $\Xi_d$ is not required — confinement follows from the harmonic potential growing without bound. $\square$

Numerical verification ($d=3$, $n=1$, $l=0$): $\chi_0 \propto \exp(-\sqrt{\lambda_3} r^2/2)$; $\int_0^\infty r^2 e^{-2\sqrt{\lambda_3} r^2/2} dr = \int_0^\infty r^2 e^{-\sqrt{4.82}\, r^2} dr = (\sqrt{\pi}/4)(\sqrt{4.82})^{-3/2} < \infty$. ✓

**Theorem (Physical mode $\leftrightarrow L^2$).** For macroscopic non-compact $\Xi_d$, a mode $\chi$ is a physical mode — a normalised eigenfunction of $H_d^{\rm harm}$ (i.e. $\chi \in L^2(\mathbb{R}^d)$) — if and only if it is an exponentially localised bound state of the sector potential. Existence as a physical mode is a normalizability condition, independent of whether the mode is visible to a $d=3$ observer.

**Proof.**

*(→) Non-eigenfunction modes are non-normalizable.* Any mode that is not a discrete eigenfunction of $H_d^{\rm harm}$ either oscillates (plane-wave-like in the sector directions) or grows. For any such state, $\int|\chi|^2 d\xi$ diverges, so $\chi \notin L^2(\mathbb{R}^d)$ and it is not a bound state.

*(←) Harmonic eigenstates are normalizable.* Every $\chi_{n,d} \in L^2(\mathbb{R}^d)$ by the corollary above, with a Gaussian envelope that decays exponentially — a genuine bound state. □

These $L^2$ bound states are the physical modes: each exists, carries mass $m = m_{\rm scale,d} \times S(n,d)$, and gravitates. Among them, the co-fixed-point condition (the generation tower) selects the stable spectrum. What a $d=3$ observer can or cannot detect is a separate question that does not affect existence or gravitation.

---

### Part II — The Bianchi Identity

With $L^2$ normalisability established, the Bianchi proof in Part II below holds unconditionally.

**Step 1 — Factorisation.**

$$T_{\mu\nu}^{\rm Dirac}(x,\xi) = |\chi_{n,d}(\xi)|^2\times T_{\mu\nu}^{\rm obs}[\psi](x)$$

**Step 2 — Spacetime conservation.** From the spacetime Dirac equation $(i\gamma^\mu\nabla_\mu - m_{\rm eff})\psi = 0$:

$$\nabla^\mu T_{\mu\nu}^{\rm obs}[\psi](x) = 0$$

**Step 3 — Commutation.** Since (a) $\nabla^\mu$ acts on $x$ only, (b) $\partial_\mu(d\mu_\xi) = 0$, and (c) $|\chi|^2\in L^2(\Xi_d)$ by Part I, the dominated convergence theorem applies:

$$\nabla^\mu\int_\Xi|\chi(\xi)|^2 T_{\mu\nu}^{\rm obs}[\psi](x)\,d\mu_\xi = \int_\Xi|\chi(\xi)|^2\nabla^\mu T_{\mu\nu}^{\rm obs}[\psi](x)\,d\mu_\xi$$

**Step 4.**

$$\nabla^\mu T_{\mu\nu}^{\rm eff}(x) = \int_\Xi|\chi_{n,d}(\xi)|^2\times 0\,d\mu_\xi = 0 \qquad\square$$

**Multi-mode.** For $\Psi_\infty = \sum_i \psi_i \otimes \chi_i$, cross terms contribute $\langle\chi_i|\chi_j\rangle_\Xi T_{\mu\nu}^{ij}$. Since $D_\Xi$ is self-adjoint and the $\chi_i$ are eigenfunctions with distinct eigenvalues $m_i \neq m_j$, they are orthogonal: $\langle\chi_i|\chi_j\rangle_\Xi = 0$. Cross terms vanish identically. $\nabla^\mu T_{\mu\nu}^{\rm eff} = 0$ holds for any superposition of physical modes. □

**Status.** The Bianchi identity $\nabla^\mu T_{\mu\nu}^{\rm eff} = 0$ is proved unconditionally for all IDWT physical modes (the normalizable bound states). No remaining open conditions.

---

## 4. Cosmological Constant

The vacuum energy that sources $\Lambda_{\rm eff}$ would come from the sector mode tower. Its observed smallness is not currently derived: an existing mode gravitates whether or not a $d=3$ observer can resolve it, so the relevant question is which modes are persistent physical excitations — only the co-fixed-point modes are stable resonances of $M_\infty$, while the rest are not persistent states. Whether that distinction, together with the sector radii and coupling strengths that fix particle masses, yields a naturally small $\Lambda_{\rm eff}$ is an open problem. ❓

The contribution of the dimensions beyond $d=10$ is fixed: it is zero. ✅ The cosmological term is the $a_0$ Seeley–DeWitt coefficient of the spectral action ${\rm Tr}(f(D/\Lambda))$, and by T5 every $d > 10$ mode lies in the essential spectrum — an extended scattering state, not $L^2$-normalisable, contributing no discrete eigenvalue to the trace. This is the same trace-exclusion established for Newton's constant in §3.12.2; it is coefficient-blind, so it removes the $d > 10$ vacuum dimensions from $a_0$ (the cosmological term) exactly as it removes them from $a_2$ (the Einstein–Hilbert term). Extending the sector self-coupling $g_{dd}$ naively into $d > 10$ instead gives an exponentially divergent vacuum volume (§3.12.2) — the divergence T5 excludes. The same conclusion follows from the mass-scale condition $m_{\rm scale,d}^2 = g_{dd}\langle|\Psi^{(d)}|^2\rangle$ (Part 2 §11.9): the $d > 10$ scattering states support no localised condensate, so the vacuum dimensions carry no sector scale and source no vacuum energy density. The open problem is thereby confined to the finite occupied tower $d ≤ 10$, whose condensed modes carry real vacuum energy. ❓

---

## 5. Generation Tower Mode Selection

The framework treats every admissible integer pair $(n,d)$ with $d \in \{2,3,4,5,6,10\}$ as a candidate resonance of $\Psi_\infty$. The physical particles are those selected by the co-fixed-point condition: the mode index $n$ must be a co-fixed-point of the sector comb filtration from $n_s=4$ — the generation tower. Modes not in the co-fixed-point set are not stable resonances of $M_\infty$, regardless of sector.

In $d=3$, the co-fixed-point spectrum selects exactly $n=1$ (down) and $n=4$ (strange). The intermediate modes $n=2$, $3$ are not co-fixed-points — they are unoccupied resonances of $M_\infty$, predicted absent as stable distinct states (their $d=3$ masses would be 18.8 and 47 MeV). Modes $n\geq5$ in $d=3$ are likewise not selected.
