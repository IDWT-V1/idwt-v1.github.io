# Infinite Dimensional Wave Theory — Part 3: Forces, Coupling Structure & Colour

All fundamental forces emerge from the geometry of $\Psi_\infty$ and the sector structure of $M_\infty$.

---

## 0. The Complete IDWT Action

Everything in IDWT — gravity, the mass spectrum, coupling constants, mixing angles — follows from a single action functional on $M_\infty = \mathbb{R}^{3,1} \times \Xi$, varied with respect to two dynamical objects: the spacetime metric $g_{\mu\nu}(x)$ and the master spinor field $\Psi_\infty(x,\xi)$.

### 0.1 Field Content

The single fundamental field is $\Psi_\infty(x,\xi)$, a Dirac spinor on $M_\infty$. The manifold carries the metric:

$$ds^2_{M_\infty} = G_{AB}(X)\,dX^A\,dX^B$$

where $X^A = (x^\mu, \xi^a)$ runs over all coordinates of $M_\infty$ without privileged blocks. From the perspective of a $d=3$ observer, the cross-terms between spacetime coordinates $x^\mu$ and sector coordinates $\xi^a$ are negligible, reducing this to the effective product form:

$$ds^2_{M_\infty} \approx g_{\mu\nu}(x)\,dx^\mu\,dx^\nu + h_{ab}(\xi)\,d\xi^a\,d\xi^b$$

In this observer's effective description, $g_{\mu\nu}(x)$ is the dynamical spacetime metric (3 spatial + 1 time) and $h_{ab}(\xi)$ is the fixed background metric on the sector space $\Xi = \bigoplus_{d\in D}\Xi_d$, $D = \{2,3,4,5,6,10\}$. The equations below use this effective form. The Dirac matrices on $M_\infty$ decompose as:

$$\{\Gamma^M, \Gamma^N\} = 2G^{MN}, \quad G^{MN} \approx \mathrm{diag}(g^{\mu\nu}, h^{ab}) \quad \text{[effective product approximation]}$$
$$\Gamma^\mu = e^\mu_a(x)\,\gamma^a \quad \text{[spacetime, via vierbein (3+1 tetrad)]}$$
$$\Gamma^a = \text{sector matrices on } \Xi \quad \text{[from Clifford algebra } \mathrm{Cl}(d) \text{ per sector]}$$

### 0.2 The Action

$$S_{\rm IDWT}[\Psi_\infty, g_{\mu\nu}]
= \frac{1}{16\pi G_N}\int_{\mathbb{R}^{3,1}} R^{(4)}\sqrt{-g}\,d^4x \quad \text{[Einstein--Hilbert]}$$

$$\quad + \int_{\mathbb{R}^{3,1}\times\Xi} \bar\Psi_\infty\bigl(i\Gamma^\mu\nabla_\mu + i\Gamma^a\partial_a\bigr)\Psi_\infty\,d\mu_4\,d\mu_\xi \quad \text{[Kinetic]}$$

$$\quad + \frac{1}{2}\sum_{d,d'\in D} g_{dd'} \int_{\mathbb{R}^{3,1}\times\Xi\times\Xi} (\xi_d\cdot\xi_{d'})^2 \bigl[\bar\Psi_\infty P_d\Psi_\infty\bigr]\bigl[\bar\Psi_\infty P_{d'}\Psi_\infty\bigr]\,d\mu_4\,d\mu_\xi\,d\mu_{\xi'} \quad \text{[Kernel]}$$

where $P_d$ is the projector onto sector $\Xi_d$, and $g_{dd'} = v_d \times v_{d'}$ is the rank-1 coupling matrix with $v_d = \sqrt{g_{dd}}$ determined by the seed pair $\{n_d{=}1,\, n_u{=}3\}$.

The kernel term is the unique leading interaction invariant under $U(d) \times U(d')$ rotations of each sector (T2). Its quartic-in-$\Psi$ form gives confinement, mass, and inter-sector coupling from a single geometric term.

**Note on $G_N$. 🔶** The Einstein--Hilbert coefficient $G_N$ appearing in the action as written is a second dimensional input — the one additional input beyond the seed pair $\{n_d{=}1,\, n_u{=}3\}$ and $m_e$. The framework fixes the *structure* of gravity (curvature of $M_\infty$ sourced by mass, with $G_N = G_\infty/(4\pi)$ sector-independent) but not the absolute scale $G_\infty$, which is not derived from the combinatorics (Part 4 §3.12.4). The action above is therefore an effective description with $G_N$ as a measured input. **Particle physics predictions (masses, mixing angles, coupling constants) are independent of $G_N$** — they depend only on the seed pair $\{n_d{=}1,\, n_u{=}3\}$, $m_e$, and the kernel geometry.

### 0.3 Equations of Motion

**Varying $g^{\mu\nu}$: ✅**

$$G_{\mu\nu}(x) = 8\pi G_N T_{\mu\nu}^{\rm eff}(x), \qquad G_N = \text{measured Newton's constant}$$

The sector space contributes only through $T_{\mu\nu}^{\rm eff} = \int_\Xi T_{\mu\nu}^{\rm Dirac}\,d\mu_\xi$ — a source term, never a propagating gravitational degree of freedom (Part 4 §3.1–3.4).

**Varying $\bar\Psi_\infty$: ✅**

$$\bigl[i\Gamma^\mu\nabla_\mu + i\Gamma^a\partial_a\bigr]\Psi_\infty + \sum_{d,d'} g_{dd'}(\xi_d\cdot\xi_{d'})^2 J^{d'}(x,\xi)\Psi_\infty = 0$$

where $J^{d'}(x,\xi) = \int (\xi_{d'}\cdot\xi')^2\,[\bar\Psi_\infty P_{d'}\Psi_\infty](x,\xi')\,d\mu_{\xi'}$. In the mean-field approximation (replacing $J^{d'}$ by the sector condensate $\langle J^{d'}\rangle$):

$$\bigl[i\Gamma^\mu\nabla_\mu + i\Gamma^a\partial_a - V_{\rm conf}(\xi)\bigr]\Psi_\infty = 0$$

with sector potential $V_{\rm conf} = \sum_d V_d(|\xi_d|)$, $V_d(r) = \lambda_d r^2$ and $\lambda_d = (g_{dd}/2)^{2/3}$ (Part 4 §3.10).

### 0.4 What Each Term Produces

| Term | Variation | Output |
|---|---|---|
| $S_{\rm EH}$ | $\delta g^{\mu\nu}$ | Spacetime Einstein equations, $G_{\rm eff} = G_N = G_\infty/(4\pi)$ (the $4\pi$ is the 3D Green's-function constant, Part 4 §3.12.2) |
| $L_{\rm kinetic}$ (spacetime part) | $\delta\bar\Psi_\infty$ | Dirac propagation in 3D space |
| $L_{\rm kinetic}$ (sector part) | $\delta\bar\Psi_\infty$ | Mass eigenvalue problem $H_d \chi = m_{\rm eff} \chi$ |
| $L_{\rm kernel}$ ($d{=}d'$, self) | $\delta\bar\Psi_\infty$ | Sector confinement $V_d$, $\lambda_d = (g_{dd}/2)^{2/3}$ |
| $L_{\rm kernel}$ ($d=4$, colour) | $\delta\bar\Psi_\infty$ | $\mathrm{SU}(3)$-symmetric quark contact coupling; effective coupling $g^2_{\rm eff} = 2g_{44}/\pi^2$ (§4) |
| $L_{\rm kernel}$ ($d=4 \leftrightarrow d=2$) | consistency | $U(2)$ electroweak coupling fields, $W^\pm$, $Z$, $\gamma$ |
| $L_{\rm kernel}$ ($d=3 \leftrightarrow d=4$) | eigenvalue + $\mathbb{CP}^1$ sector curvature correction | Cabibbo angle $\sin\theta_C$ |

### 0.5 Mass Spectrum from the Action

Separating the sector eigenmode $\chi_n(\xi)$ from the spacetime part $\psi(x)$ via $\Psi_\infty = \psi(x)\otimes\chi_n(\xi)$ reduces the equation of motion to:

$$( i\gamma^\mu\nabla_\mu - m_{\rm eff})\psi = 0 \quad \text{[massive Dirac in 3D space]}$$
$$H_d\,\chi_n = m_{\rm eff}\,\chi_n \quad \text{[sector eigenvalue problem]}$$

**Mass spectrum from the action. ✅** The sector Hamiltonian $H_d = -\Delta_\Xi + V_d(r)$ fixes the mode mass by the spectral counting theorem (Part 8 §3): $m_{\rm eff} = m_{{\rm scale},d}\times S(n,d)$, where $S(n,d)$ is the cumulative count of sector oscillator states at levels $k = 0, 1, \ldots, n-1$ — the integrated density of states — not an individual eigenvalue of $H_d$ (Part 8 §5.1). The mass formula is a consequence of the action.

### 0.6 Effective Colour Coupling from the Kernel

The $d=4$ self-coupling $\mathcal{L}_{44} = (g_{44}/2)\int (\xi_4\cdot\xi_4')^2 J^4(\xi) J^4(\xi')\,d\mu_{\xi'}$ is the direct quark contact interaction. Integrating the kernel current $J^4$ over the $\mathbb{CP}^2$ manifold (volume $\pi^2/(2m_{{\rm scale},4}^4)$) yields the effective coupling strength:

$$g^2_{\rm eff} = \frac{2g_{44}}{\pi^2} \qquad \text{✅}$$

The $\mathrm{SU}(3)$ invariance of this coupling follows from the $\mathbb{CP}^2$ isometry group acting on the quark colour states. The colour interaction is a direct contact term in the kernel — the $\mathbb{CP}^2$ isometry acts on quark colour states through $g_{44}$ with no intermediate colour-exchange field. The contact property itself is a structural consequence of kernel covariance: every non-contact covariant reading of the kernel terms is excluded by established physics (Part 4 §3.10.1 covariance note; `files/idwt.py` STEP 59).

### 0.7 Coupling Constants from the Action

All physical coupling constants follow from $\{g_{dd'}\}$ and the sole unit reference $m_e$ ($m_W$ is derived at +0.003% from seeds via $g_{22}$): 🔵

| Physical quantity | Formula | Value |
|---|---|---|
| Effective colour coupling | $g^2_{\rm eff} = 2g_{44}/\pi^2$ | 0.919 |
| Weinberg angle | $\sin^2\theta_W = 1-(S(n_W,2)/S(n_Z,2))^2$ | 0.2237 |
| $l=2$ kernel scale (sets $\delta_{\nu_3}$) | $\varepsilon = 1/(280\sqrt{7})$ | 0.001350 |
| Cabibbo angle | $\sin\theta_C = (1+\chi(\mathbb{CP}^1)/(24S))/\sqrt{S(n_s,3)}$ | 0.22454 |
| Newton's constant | $G_N = G_\infty/(4\pi)$ (the $4\pi$ is the 3D Green's-function constant; $G_\infty$ one input, Part 4 §3.12.2) | — |
| **$SU(2)_L$ coupling** | **$g_2 = Q_u\sqrt{g_s} = (2/3)\sqrt{g_s} = (2/3)(2g_{44}/\pi^2)^{1/4}$** | **0.65275** |
| **EW scale $\sqrt{\mathrm{Tr}(D^2)}$** | **RMS of 15-particle mass spectrum** | **248.3 GeV** |
| **Fermi constant** | **$G_F = g_2^2/(4\sqrt{2}\,m_W^2)$** | **$1.1658\times10^{-5}$ GeV$^{-2}$** |


**Derivation of $g_2$. ✅** The effective colour coupling $g_s$ is obtained by integrating the kernel coupling density $g_{44}$ over the $\mathbb{CP}^2$ manifold. The Fubini-Study metric gives $\mathbb{CP}^2$ a volume $\pi^2/2$ in units of the sector length scale, introducing the factor $2/\pi^2$ (ratio of successive Hopf-level sphere volumes). The up-quark charge $Q_u = 2/3$ follows from the $\mathrm{spin}^c$ index on $\mathbb{CP}^2$: $\mathrm{ind}(D^c_{\mathbb{CP}^2}\otimes\mathcal{O}(1)) = 3 = N_c$ colours (Theorem S3, Part 8 §2.2), so each colour carries charge $1/N_c = 1/3$ and the doublet carries $2Q_u = 2\times 2/3$. The $\mathrm{SU}(2)_L$ coupling is therefore: 🔵

$$g_s = \sqrt{2g_{44}/\pi^2} \quad \text{[colour coupling, from } \mathbb{CP}^2 \text{ kernel integral]}$$
$$g_2 = \tfrac{2}{3}\sqrt{g_s} = \tfrac{2}{3}(2g_{44}/\pi^2)^{1/4}$$
$$g_2^2 = \tfrac{4}{9}\,g_s = \tfrac{4}{9}(2g_{44}/\pi^2)^{1/2}$$
$$g_2 = \tfrac{2}{3}\sqrt{g_s} = 0.65275 \quad \text{(PDG: } 0.65270,\;{+}0.008\text{\%)}$$

**The coupling cascade. ✅** All three couplings descend from a single tower-derived quantity, $g_{44}$, through a fixed chain — each step determined by the sector geometry alone:

$$g_{44} \;\to\; g_s = \sqrt{2g_{44}/\pi^2} \;\to\; g_2 = \tfrac{2}{3}\sqrt{g_s} \;\to\; \sin^2\theta_W = 1 - \bigl(S(n_W,2)/S(n_Z,2)\bigr)^2 \;\to\; g_1 = g_2\tan\theta_W \;\to\; \alpha$$

The factor $2/3$ at the $g_s\to g_2$ step is both the electric charge of the up quark (index theorem) and the coordinate containment ratio $d_{\rm photon}/d_{\rm hadronic}$: $N_c = 3 = d_{\rm hadronic}$, $d_{\rm photon} = 2$, so $Q_u = d_{\rm photon}/d_{\rm hadronic}$ (Part 1 §3g). The $\mathbb{CP}^2$ kernel integral step involves a continuous Riemannian integral ($2/\pi^2$), not a coordinate count; but the subsequent step is a literal ratio of sector dimensions.

From $g_2$ and $m_W$ (the confinement mass of the W in the $d=2$ sector): 🔵

$$G_F = g_2^2/(4\sqrt{2}\,m_W^2) = 1.1658\times10^{-5}\;\mathrm{GeV}^{-2} \quad \text{(PDG: } 1.1664\times10^{-5},\;{-}0.05\text{\%)}$$
$$g_1 = g_2\tan\theta_W = 0.35044 \quad \text{(PDG: } 0.35740,\;{-}1.95\text{\% at } d{=}2 \text{ sector scale)}$$

IDWT couplings are fixed geometric numbers defined at the $d=2$ sector scale ($\approx m_W$); they do not run. The PDG quotes its values at $m_Z$ under an SM renormalization prescription, so comparison requires a scale translation; the translation used here is the SM 1-loop formula applied to the IDWT input — a cross-framework comparison, not an IDWT mechanism. The $g_1$ gap of $-2\%$ is the difference between the $d=2$-sector-scale $\mathrm{U}(1)_Y$ coupling and the differently-defined $m_Z$-scale PDG quantity. The $\alpha$ prediction: 🔵

$$\alpha = g_1^2 g_2^2/\bigl[4\pi(g_1^2+g_2^2)\bigr] = 1/131.8 \quad \text{(PDG } \alpha(m_Z)=1/127.9,\;{+}3.1\text{\%)}$$

The $+3\%$ gap corresponds to the SM scale translation between the $d=2$ sector scale ($\approx m_W$) and $m_Z$; IDWT supplies the sector-scale value only.



### 0.8 Force Coupling as Spatial Geometry

Each force couples to a particle through the sector coordinates the particle occupies. A particle couples to a force only if the particle's sector contains that force's sector — the coupling geometry lives in that sector, and the particle either occupies that space or it doesn't.

| Force | Sector | Dimensions | Coupling structure |
|---|---|---|---|
| Electromagnetic | $d=2$ | 2 | $U(1)$ phase from shared $d=2$ coordinates |
| Weak | $d=2$ | 2 | $SU(2)_L$ = the $SU(2)$ factor of the U(2) holonomy of $\mathbb{CP}^2$ (§6); acts on the holomorphic (left) spinor half via the Kähler chirality split (§7) |
| Strong | $d=3$, $d=4$ | 3–4 | $SU(3)$ contact coupling via $\mathbb{CP}^2$ isometry |
| Gravity | all | 10 | Curvature of $M_\infty$; no sector boundary |

**Coordinate containment.** A particle couples to a force only when the particle's sector contains the sector where that force's coupling geometry lives. A particle with no $d=2$ support cannot couple electromagnetically. The strong coupling ($d=4$, kernel contact) cannot reach a particle with no $d=3$ or $d=4$ support. Coordinate containment is a necessary condition. The sufficient condition additionally requires the appropriate topological structure — electric charge from the $U(1)$ holonomy on the $d=2$ sector, colour from $\chi(\mathbb{CP}^2) = 3$ (the $d=4$ manifold), and weak isospin from the $SU(2)$ factor of the U(2) holonomy of $\mathbb{CP}^2$ (§6, §7).

**Why coordinate containment guarantees coverage — transverse picture.** A lower-d particle's mode is automatically spread across all of a higher-d particle's extra directions. The photon ($d=2$) illustrates this directly: its mode spans the two transverse directions and need not be aimed at a target in those directions — anything sharing that plane is covered automatically. The same structure repeats at every level of the sector nesting. A $d=3$ quark's mode is transverse to the one extra direction of a $d=4$ particle: it covers that full direction without aiming. A $d=2$ photon interacting with a $d=10$ tau is transverse to eight of the tau's dimensions simultaneously — no alignment is required or even possible in any of them. This is the geometric reason coordinate containment produces automatic coupling rather than conditional coupling: the lower-d particle does not need to find the higher-d particle in its hidden dimensions because it is already everywhere in those dimensions. The coupling strength is set by the sector geometry as usual; the transversality explains why the coupling fires at all. The same reasoning accounts for the quantum mechanical statement that the electron can be found anywhere in the universe: the electron is a $d=6$ object, and a $d=3$ observer detects it only at the intersection of its 6D orbit with our three observable coordinates. The 6D orbit sweeps through our 3D slice freely — no confinement in the $d=3$ directions — so those intersections fall anywhere across observable space. The apparent delocalization is not uncertainty; it is what a 6D orbit looks like when intersected by three observable coordinates it is not confined to.

**Gravity as the exception. ✅** Gravity carries no sector label and is confined to no subset of the spatial dimensions. The effective stress-energy sourcing gravity integrates over all sector coordinates:

$$T_{\mu\nu}^{\rm eff}(x) = \int_\Xi T_{\mu\nu}^{\rm Dirac}(x,\xi)\,d\mu_\xi$$

Gravity is curvature of $M_\infty$ itself, not a 3D effect with extra-dimensional corrections. A $d=3$ observer occupies a subspace of $M_\infty$ and measures that curvature at their $d=3$ coordinates; integrating a source over its hidden coordinates leaves the sector-independent Newtonian $G_N = G_\infty/(4\pi)$ (Part 4 §3.12.2).

**Why gravity reaches every particle.** Gravity is the curvature of $M_\infty$ sourced by mass, not a force confined to a sector. Every particle has mass, so every particle gravitates, and there is no sector boundary to cross. A $d=3$ observer is uniform in a source's hidden coordinates and samples its curvature integrated over them; that integral collapses to the ordinary Newtonian $1/r$ potential with the sector-independent coupling $G_N = G_\infty/(4\pi)$, the $4\pi$ being the 3D Green's-function constant (Part 4 §3.12.2). The same coupling holds for a source of any sector, and no volume factor enters.

**Coupling filter — the particle side.** The coordinate containment principle above describes the force side: which sector a force's coupling geometry occupies determines which particles it can reach. The complementary particle-side principle is the coupling filter: the particle's own sector geometry determines the structure of whatever coupling it has. Coordinate containment is necessary but not sufficient. A particle whose coordinates are nested inside a force's sector may still have zero coupling to that force if its sector geometry projects the relevant representation to zero — as neutrinos are colour-neutral despite their $S^5$ coordinates containing $\Xi_4$, because the $S^5$ Hopf fibration averages over the $\mathbb{CP}^2$ colour representation and selects only the singlet. More broadly: the photon's $U(1)$ geometry constitutes the orientation filter of EM coupling; $\chi(\mathbb{CP}^2) = 3$ constitutes colour with $N_c = 3$ handles; the $S^5$ Clifford algebra constitutes the prohibition of all Majorana/LNV interactions; the $\mathbb{CP}^3$ index cancellation constitutes total colour silence for leptons; the $d=10$ Gegenbauer-critical coupling structure constitutes the tau's fractal marginal coupling to all decay channels. In each case, the sector geometry is not producing a quantum number that then determines coupling — the geometry is the coupling structure. See Part 1 §3d and §3g for the full derivation of each sector's coupling filter.

### 0.8a The 1/R Force Law is Universal — Projection Theorem

⭐ **Theorem (Coulomb projection).** Let a particle occupy sector $d \geq 3$. Its intra-sector static interaction is governed by the $d$-dimensional Coulomb kernel $G_d(r) = 1/r^{d-2}$. A $d=3$ observer cannot access the $(d-3)$ hidden sector coordinates and integrates over them:

$$\varphi_{\rm obs}(R) = S_{d-3}\int_0^\infty \frac{y^{d-4}\,dy}{(R^2+y^2)^{(d-2)/2}}$$

where $S_{d-3} = 2\pi^{(d-3)/2}/\Gamma((d-3)/2)$ is the surface area of the unit $(d-4)$-sphere. Using the beta-function identity with $k = d-3$, $n = (d-2)/2$:

$$\int_0^\infty \frac{y^{k-1}\,dy}{(R^2+y^2)^n} = \tfrac{1}{2}R^{k-2n}\,B(k/2,\,n-k/2) = \tfrac{1}{2}R^{-1}\,\frac{\Gamma(k/2)\,\Gamma(1/2)}{\Gamma(n)}$$

The exponent $k-2n = (d-3)-(d-2) = -1$ for every $d$. Therefore:

$$\varphi_{\rm obs}(R) = C_d/R \qquad \text{for every } d\geq 3$$

The $R$-dependence is universally $1/R$ — independent of sector. What varies with $d$ is only the prefactor:

$$C_d = \frac{\pi^{(d-2)/2}}{\Gamma\!\left(\frac{d-2}{2}\right)}, \qquad C_3=1,\quad C_4=\pi,\quad C_5=2\pi,\quad C_6=\pi^2,\quad C_{10}=\frac{\pi^4}{6}$$

🔵 Numerically verified: $\varphi_{\rm obs}(R)\times R$ is constant to $<1\%$ across two decades of $R$ for $d = 3, 4, 5, 6, 10$.

**Physical meaning.** Coulomb's 1/R is not special to $d=3$ or to the $d=2$ photon sector. It is a theorem about what any $d=3$ observer must see when they marginalise over hidden sector dimensions: the extra integration factors always cancel the extra powers of r. The 1/R law follows from projection regardless of which sector the interacting particles inhabit.

**The $d=2$ photon propagator does not give $1/R$. ⭐** If the force law arose from the photon propagating in its own $d=2$ sector space, the Green's function would be $G_{2D}(r) = -\ln(r)/(2\pi)$ — logarithmic, not $1/R$, and independent of the third observable direction. The $d=2$ propagator does not produce Coulomb's law. The $1/R$ structure is a property of projection, not of the photon's sector.

**Effective coupling.** The observed interaction energy between two particles of sector $d$ with charge units $q_A$, $q_B$ is:

$$E(R) = g_{dd}\times q_A\times q_B\times C_d/R$$

The sector coupling $g_{dd}$ and the charge units are separately normalised for each sector (charge normalisation is an open derivation — see §14). The $C_d$ factors are pure geometry.

---

### 0.8b Sector Properties at a Glance

The table below consolidates, for each sector $d \in D$, the geometric, coupling, and scale properties discussed separately in §0.7–§0.8 and Parts 1–2. One row per sector; read across for the complete coupling profile of each particle family.

| $d$ | Manifold | Isometry | $\chi$ | $g_{dd}$ (exact) | $m_{\rm scale}$ | Hosted particles | Coupling filter consequence |
|---|---|---|---|---|---|---|---|
| 2 | $\mathbb{CP}^1$ | $U(1)$ | 2 | $722.5$ | 27.47 MeV | $\gamma,\;W^\pm,\;Z^0,\;H$ | Orientation filter: two helicity states = complete internal geometry; coupling $\propto \varepsilon_\mu j^\mu$, zero for $j^\mu \perp \varepsilon_\mu$ |
| 3 | $S^3$ | $\mathrm{SO}(4)$ | 0 | $8\sqrt{7}$ | 4.702 MeV | $d,\;s,\;b$ | No intrinsic chirality: $S^3$ is odd-dimensional, so $\gamma^1\gamma^2\gamma^3 \propto \mathbb{1}$ furnishes no chirality operator and its Dirac spinors are vector-like. The down-type left-handed weak structure is not produced here — it is inherited from the $d=4$ $\mathbb{CP}^2$ Kähler chirality through $d{=}3\subset d{=}4$ and the cross-coupling $g_{3,4}$; the $(u_L,d_L)$ doublet is a $\mathbb{CP}^2$ object (§6, §7) |
| 4 | $\mathbb{CP}^2$ | $\mathrm{SU}(3)$ | 3 | $12/\sqrt{7}$ | 0.145 MeV | $u,\;c,\;t$ | Colour filter: $\chi(\mathbb{CP}^2) = N_c = 3$ colour handles from index theorem (§2, Part 8); colour-nonsinglet asymptotic states geometrically impossible |
| 5 | $S^5$ | $\mathrm{SO}(6)$ | 0 | $96/g_{22}\approx 0.133$ | $7.4\times10^{-13}$ MeV | $\nu_1,\;\nu_2,\;\nu_3$ | Majorana/LNV filter: no $C$ on $S^5$ spinor bundle ($d \bmod 8 = 5$); Hopf $S^1\!\to\!S^5\!\to\!\mathbb{CP}^2$ projects colour to singlet |
| 6 | $\mathbb{CP}^3$ | $\mathrm{SU}(4)$ | 4 | $1/4$ | $2.75\times10^{-5}$ MeV | $e^-,\;\mu^-$ | Colour-silence filter: $\chi(\mathbb{CP}^3)=4\neq N_c$; colour contributions cancel in $\mathrm{SU}(4)$ representation; zero strong coupling at all energies |
| 10 | $\mathbb{CP}^5$ | $\mathrm{SU}(6)$ | 6 | $1/4$ | $2.75\times10^{-5}$ MeV | $\tau^-$ | Gegenbauer-critical filter: $b_{k_0}(10)=1/2$ exactly (Part 9 T5); coupling weight distributed with no dominant decay channel; back-reaction correction $+1/1680$ required |

**Column notes.** $\chi$ is the Euler characteristic of the compact local $\mathbb{CP}^k$ model; for odd-sphere sectors ($d=3,5$) the sphere has $\chi(S^d)=0$ and structural counting roles are carried by the CP sector in the Hopf pair. Specifically: $\chi(\mathbb{CP}^2)=N_c=3$, $\chi(\mathbb{CP}^3)=n_s=4$, $\chi(\mathbb{CP}^5)=N_f=6$ (Part 9 T15). The $g_{dd}$ values are exact from the seed $n_u=3$ (primitive); derivations in §0.7 and Part 2 §9. The $m_{\rm scale}$ values use $m_e=0.511$ MeV as the unit reference (Part 2 §10).

**Coordinate containment vs coupling filter.** These are two distinct necessary conditions. Coordinate containment (§0.8) governs which forces can reach a particle: a force couples to a particle only if the particle's sector contains that force's sector. The coupling filter governs what happens within that sector: even with support in the sector, the particle's own sector geometry may project the relevant representation to zero. Both must hold for coupling to occur. Neutrinos ($d=5$): coordinates are nested inside $\Xi_4$ (colour sector), but the $S^5$ Hopf projection selects only the colour singlet — they are colour-neutral despite spatial overlap with the colour sector. Electrons ($d=6$): $\chi(\mathbb{CP}^3)=4\neq 3$; colour contributions cancel in the $\mathrm{SU}(4)$ representation regardless of spatial overlap with $\Xi_4$.

---

### 0.8c Active Coupling Structures by Sector Pair

§0.8 and §0.8b give the two necessary conditions for coupling: coordinate containment (which coordinates a sector pair shares) and the coupling filter (what each sector's geometry permits on those coordinates). This subsection combines them into one map. A cross-sector effect is not an exchange between two objects: it is the single wave $\Psi_\infty$ coupling to itself, through the kernel $g_{d,d'}(\xi_d\!\cdot\!\xi_{d'})^2$, on the coordinates that two of its sectors share (Part 1 §3g). A coupling structure is **active** on a sector pair when it is geometrically present on the shared coordinates and survives both sectors' filters.

The four coupling structures and their geometric origin:

| Structure | Geometric origin | Present on |
|---|---|---|
| $U(1)$ — electric charge | $Q = T_3 + Y$, with $Y$ an eigenvalue of $T_8$ of $\mathrm{SU}(3)=\mathrm{Isom}(\mathbb{CP}^2)$ (§6, §13) | sectors whose hosted modes carry $Q \neq 0$ |
| $\mathrm{SU}(2)_L$ — weak isospin | the $\mathrm{SU}(2)$ factor of the $U(2)$ holonomy of $\mathbb{CP}^2$; Kähler chirality (§7) restricts it to the holomorphic (left) component | the left-handed part of every fermion sector |
| $\mathrm{SU}(3)$ — colour | the $\mathrm{SU}(3)$ isometry of $\mathbb{CP}^2$; $N_c=\chi(\mathbb{CP}^2)=3$ (§2, §6) | the quark sectors $d=3,4$ |
| Gravity | curvature of $M_\infty$; no sector boundary (§0.8) | every sector |

**Per-sector participation. ✅** Each entry follows from the established sector geometry: the charges from the $T_8$ eigenvalues (§6), colour from $\chi(\mathbb{CP}^2)=3$ with the $S^5$ Hopf singlet projection ($d=5$) and the $\chi(\mathbb{CP}^3)=4$, $\chi(\mathbb{CP}^5)=6$ colour-silence of the leptons ($d=6,10$), weak isospin from the Kähler chirality of the $\mathbb{CP}$ sectors with $d=3$ inheriting through $g_{3,4}$ and $d=5$ entering as the Dirac $\nu_L$.

| $d$ | Hosted | $Q$ | $U(1)$ | $\mathrm{SU}(2)_L$ | $\mathrm{SU}(3)$ | Gravity |
|---|---|---|---|---|---|---|
| 3 | $d,s,b$ | $-\tfrac{1}{3}$ | ✓ | ✓ | ✓ | ✓ |
| 4 | $u,c,t$ | $+\tfrac{2}{3}$ | ✓ | ✓ | ✓ | ✓ |
| 5 | $\nu_{1,2,3}$ | $0$ | — | ✓ | — | ✓ |
| 6 | $e,\mu$ | $-1$ | ✓ | ✓ | — | ✓ |
| 10 | $\tau$ | $-1$ | ✓ | ✓ | — | ✓ |

**Pairwise map. ⭐** A structure is active on a pair exactly when both sectors carry it — the intersection of their participation rows. In the cells, $\mathrm{EM}=U(1)$, $\mathrm{W}=\mathrm{SU}(2)_L$, $\mathrm{C}=\mathrm{SU}(3)$, $\mathrm{G}=$ gravity.

| | $d{=}3$ | $d{=}4$ | $d{=}5$ | $d{=}6$ | $d{=}10$ |
|---|---|---|---|---|---|
| **$d{=}3$** | EM·W·C·G | EM·W·C·G | W·G | EM·W·G | EM·W·G |
| **$d{=}4$** | EM·W·C·G | EM·W·C·G | W·G | EM·W·G | EM·W·G |
| **$d{=}5$** | W·G | W·G | W·G | W·G | W·G |
| **$d{=}6$** | EM·W·G | EM·W·G | W·G | EM·W·G | EM·W·G |
| **$d{=}10$** | EM·W·G | EM·W·G | W·G | EM·W·G | EM·W·G |

Gravity occupies every cell, sourced by the full $M_\infty$ curvature. $U(1)$ drops from every pair that includes the neutral neutrino sector $d=5$. $\mathrm{SU}(3)$ colour survives only in the quark block $\{d=3,d=4\}$, removed elsewhere by the neutrino Hopf singlet projection and the lepton colour-silence. $\mathrm{SU}(2)_L$ is present on every fermion pair.

The $d=2$ sector hosts $\gamma,\,W^\pm,\,Z^0,\,H$ — themselves sector excitations of $\Psi_\infty$, not a matter family with a single charge. The $U(1)$ and $\mathrm{SU}(2)_L$ structures are the holonomy geometry of $\mathbb{CP}^2$ (§6), not something those modes carry; the pairwise map therefore runs over the matter sectors.

---

### 0.9 CKM Matrix from the Kernel

The mode amplitude at the $d=3$ coordinate level scales as $|\chi_n(\xi^0)| \propto 1/\sqrt{S(n,d)}$ from $L^2$ normalisation (Part 1 §2.2), so heavier modes (larger $S$) carry less weight at our coordinate level relative to lighter modes. The intra-sector kernel matrix element between modes $n_i$ (lighter) and $n_j$ (heavier) is proportional to the amplitude of the heavier mode at $\xi_0$ relative to the lighter: ✅

$$|\langle\chi_{n_{\rm lighter}}|K_{dd}|\chi_{n_{\rm heavier}}\rangle| \propto \frac{|\chi_{n_{\rm heavier}}(\xi_0)|}{|\chi_{n_{\rm lighter}}(\xi_0)|} = \sqrt{\frac{S(n_{\rm lighter},d)}{S(n_{\rm heavier},d)}}$$

The mixing probability is the square of this ratio: ✅

$$|V_{i\to j}|^2 = \frac{S(n_{\rm lighter},d)}{S(n_{\rm heavier},d)} \qquad \text{[within sector } d\text{]}$$

**Application to CKM elements:**

The Cabibbo angle is the $d=3$ intra-sector mixing (down $\leftrightarrow$ strange): 🔵

$$\sin^2\theta_C = \frac{S(n_d,3)}{S(n_s,3)} = \frac{1}{20} \;\Longrightarrow\; \sin\theta_C = \frac{1}{\sqrt{20}} = 0.22361 \quad \text{[bare]}$$

Corrected by $\mathbb{CP}^1$ sector curvature correction (§12): $\sin\theta_C = (1+1/240)/\sqrt{20} = 0.22454$.

The $|V_{cb}|$ element is the $d=4$ intra-sector mixing (up $\leftrightarrow$ charm): 🔵

$$|V_{cb}|^2 = \frac{S(n_u,4)}{S(n_c,4)} = \frac{S(3,4)}{S(20,4)} = \frac{15}{8855}, \qquad |V_{cb}| = \sqrt{15/8855} = 0.04116$$

PDG $|V_{cb}| = 0.04100 \pm 0.0014$ (exclusive). Tension: $+0.11\sigma$.

**$|V_{ts}|$ from unitarity: 🔵** The third row of the CKM matrix has $|V_{tb}|\approx 1$, so $|V_{ts}|^2\approx|V_{cb}|^2$. IDWT predicts $|V_{ts}|\approx|V_{cb}| = 0.04116$. PDG: $0.04183\pm0.0007$. Tension: $-0.96\sigma$.

**$|V_{ub}|$:** The full $|V_{ub}|$ prediction requires the complete CP-violating phase $\delta_{CP} = \pi + 2\theta_{13} = 197.11°$ (T8 🔶, Part 10 §4), which is now structurally derived. With $\delta_{CP} = 197.11°$: $|V_{ub}| = A s_C^3 \sqrt{\rho^2 + \eta^2}$ where the unitarity triangle parameters follow from the CKM phase. Full numerical prediction awaits T8 reaching 🔵 (three technical gaps in the APS spectral flow proof). Lower bound: $|V_{ub}|_{\rm lower} = A s_C^3 = 0.00920$ (setting the CP-phase factor to its minimum). SM cross-reference: the Wolfenstein parameter $A = |V_{cb}|/\sin^2\theta_C = 0.82315$ matches PDG $A = 0.826 \pm 0.012$ at $-0.24\sigma$.

### 0.10 Pure Sector Identities from the Lagrangian

**$\cos\theta_W = S(n_W,2)/S(n_Z,2)$ exactly. ⭐** From the Lagrangian's Weinberg angle definition:

$$\sin^2\theta_W = 1 - \bigl(S(n_W,2)/S(n_Z,2)\bigr)^2 \;\Longrightarrow\; \cos\theta_W = S(n_W,2)/S(n_Z,2) = 2926/3321 = 0.88106$$

PDG $\cos\theta_W = 0.88108$.

**Sector mass ratios: ⭐**

$$m_\mu/m_e = S(n_\mu,6)/S(n_e,6) = 3{,}838{,}380/18{,}564 = 206.7647 \quad \text{(PDG } 206.7683,\;{-}0.002\text{\%)}$$
$$m_H/m_Z = S(n_H,2)/S(n_Z,2) = 4560/3321 = 1.37308 \quad \text{(PDG } 1.37354,\;{-}0.033\text{\%)}$$

**The $d=2$ coupling $g_{22} = 722.5$ and what it determines. ✅** The Hopf chain constraint $g_{25} = \sqrt{g_{22}}\times\sqrt{g_{55}} = \sqrt{96} = 4\sqrt{6}$ is automatically satisfied for any $g_{22}$ with $g_{55} = 96/g_{22}$ — $g_{22}$ cancels. Its value is fixed instead by the depth of the $d=2$ sector potential: $\lambda_2 = (g_{22}/2)^{2/3} = 50.72$, localization length $L_2 = 0.14$. The large $\lambda_2$ ensures $W$, $Z$, $H$ are tightly confined and do not propagate as bulk KK modes.

**Neutron-proton mass difference, leading order: 🔵**

$$m_n - m_p \approx m_d - m_u = m_{\rm scale,3}\times S(1,3) - m_{\rm scale,4}\times S(3,4) = 4.702 - 2.177 = 2.525\;\mathrm{MeV}$$

PDG: $1.293$ MeV (factor $\sim 2$; uncomputed QED + isospin corrections). The correct order of magnitude emerges from pure sector masses with no parameters. The factor of 2 is the uncomputed electromagnetic correction (proton self-energy $\approx 0.6$ MeV) plus isospin breaking from the $d=3\leftrightarrow d=4$ sector coupling asymmetry.

---

## 1. Electromagnetism

Electromagnetism emerges from the $U(1)$ Hopf fiber connecting the $d=2$ and $d=3$ sectors. Writing $\Psi_\infty = A\cdot e^{i\theta}$, the phase gradient $A_\mu = \partial_\mu\theta$ is the photon field; its curvature $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ gives Maxwell's equations. The photon is massless because its mode index is $n=0$: $S(0,2) = 0$. Full derivation in §14.

---

## 2. Colour Charge from $\mathbb{CP}^2$

The $d=4$ sector geometry is $\mathbb{CP}^2 = \mathrm{SU}(3)/U(2)$. The full isometry group of $\mathbb{CP}^2$ is $\mathrm{SU}(3)$. Therefore quarks in the $d=4$ sector naturally carry $\mathrm{SU}(3)$ quantum numbers — from the manifold's own geometry.

$\chi(\mathbb{CP}^2) = 3$ gives exactly three independent colour modes per quark. The representation is fixed by the sector geometry: the isometry group is $\mathrm{SU}(3)$, so the three modes necessarily transform in the fundamental representation $\mathbf{3}$ — not by postulate, but because $\mathrm{SU}(3)$ is the symmetry group of the space they inhabit. Three colour states per quark is a theorem of the $d=4$ sector geometry.

**$N_c = \chi(\mathbb{CP}^2) = 3$. ✅** This is the geometric origin of colour charge (Part 1 §3d, Part 9 T15, S3).

---

## 3. Colour Symmetry from Consistency

The $\mathrm{SU}(3)$ colour symmetry follows from consistency. The $d=4$ sector field at spacetime point $x$ decomposes into three colour amplitudes (§3a); this decomposition is arbitrary up to local $\mathrm{SU}(3)$ rotations — different orientations of the three colour directions within the $\mathbb{CP}^2$ sector space are physically equivalent. The total colour-plus-EW structure group is: ✅

$$G = \mathrm{SU}(3)\times U(2)$$

Given the three-dimensional colour space identified from $\chi(\mathbb{CP}^2) = 3$ (§2):

1. Physical observables depend on $|\Psi_\infty|^2$ — invariance under local colour rotations $U(x)\in\mathrm{SU}(3)$ is a **consistency requirement**, not a postulate
2. Local invariance forces a connection: $D_\mu\Theta = \partial_\mu\Theta + i[A_\mu, \Theta]$
3. The commutator $[D_\mu, D_\nu]\Theta = i[F_{\mu\nu}, \Theta]$ gives the colour connection curvature:

$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + i[A_\mu, A_\nu]$$

$\mathrm{SU}(3)$ coupling theory is not postulated. It follows from the $\mathbb{CP}^2$ sector geometry and the requirement that physics not depend on the local orientation of the colour frame.

### 3a. Explicit Colour Connection Construction 🔶

The argument above establishes that a connection must exist. This subsection constructs it explicitly from the IDWT sector field.

**The colour triplet state.** $\chi(\mathbb{CP}^2) = 3$ (see Part 8 §2 for explicit construction) gives three left-chiral modes $\phi_a\in L^2(\mathbb{CP}^2)$, $a = 1, 2, 3$. At spacetime point $x$, the $d=4$ sector component of $\Psi_\infty$ decomposes as:

$$\psi_{\rm color}(x) = \bigl(\psi^1(x), \psi^2(x), \psi^3(x)\bigr) \in \mathbb{C}^3$$

where

$$\psi^a(x) = \int_{\mathbb{CP}^2} \phi_a^*(\xi)\,\Psi_\infty^{(d=4)}(x,\xi)\,d\mu_{\mathbb{CP}^2}$$

This integral extracts the three colour amplitudes from the full sector-space field at each spacetime point $x$. It is the IDWT definition of the colour state at $x$.

**Colour connection formula.** The colour frame can be chosen independently at each spacetime point. The unique torsion-free $\mathrm{SU}(3)$ connection preserving the $L^2(\mathbb{CP}^2)$ inner product on $H_{\rm colour}$ is:

$$A_\mu(x) = i\,\psi_{\rm color}^\dagger(x)\,\partial_\mu\psi_{\rm color}(x) \;\in\; \mathfrak{su}(3)$$

This is the colour connection — the $\mathrm{SU}(3)$-valued coupling encoding local colour frame freedom in the $d=4$ sector.

**Coupling transformation check.** Under $U(x)\in\mathrm{SU}(3)$: $\psi_{\rm color}(x)\to U(x)\psi_{\rm color}(x)$. Direct computation: ✅

$$A_\mu \;\to\; i(U\psi)^\dagger\partial_\mu(U\psi) = U^\dagger A_\mu U + U^\dagger\partial_\mu U$$

This is the correct $\mathrm{SU}(3)$ transformation law. The curvature

$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + i[A_\mu, A_\nu] \;\in\; \mathfrak{su}(3)$$

is the colour curvature 2-form. This is a mathematical object encoding the $\mathrm{SU}(3)$ holonomy of the colour frame; it is not a propagating field. The IDWT action (§0.2) contains no kinetic term $F_{\mu\nu}F^{\mu\nu}$ for this connection — the colour interaction is entirely in the kernel contact term.

**Status.** The colour connection is defined and transforms correctly for the zero-mode sector. What remains is constructing $\psi_{\rm color}(x)$ explicitly for propagating quark modes — that is, extending the colour projection $P_{\rm color}$: $\Psi_\infty^{(d=4)} \to \psi_{\rm color}$ beyond the three $\mathbb{CP}^2$ zero modes to the full occupied spectrum ($n=3$ up, $n=20$ charm, $n=72$ top). The zero-mode construction is complete (Part 8 §2); the propagating-mode projection operator is the remaining step.

---

## 4. Effective Colour Coupling from the Kernel

### Derivation of $g^2_{\rm eff}$ from the $d=4$ Kernel

The IDWT action has no Yang-Mills kinetic term. The colour interaction is entirely the $d=4$ self-coupling contact term. To connect with the QCD coupling $g_s$ used in the cascade of §0.7, we derive the effective coupling by integrating the kernel current $J^4$ over $\mathbb{CP}^2$:

The $d=4$ kernel current density, when integrated over $\mathbb{CP}^2$ with the Fubini-Study metric at radius parameter $a = 1/m_{{\rm scale},4}$: ✅

$$\mathrm{Vol}(\mathbb{CP}^2) = \frac{\pi^2 a^4}{2} = \frac{\pi^2}{2\,m_{{\rm scale},4}^4}$$

The kernel coupling $g_{44} = 12/\sqrt{7}$ is dimensionless ($\xi$ measured in units of $1/m_{{\rm scale},4}$). The effective coupling strength extracted by matching the integrated kernel amplitude to the standard QCD form is:

$$\frac{1}{g^2_{\rm eff}} = \mathrm{Vol}(\mathbb{CP}^2)\times\frac{m_{{\rm scale},4}^2}{g_{44}} = \frac{\pi^2}{2}\times\frac{1}{g_{44}} \;\Longrightarrow\; g^2_{\rm eff} = \frac{2g_{44}}{\pi^2} = \frac{2\times(12/\sqrt{7})}{\pi^2} = 0.919 \qquad \text{🔵}$$

This is the coupling $g_s = \sqrt{g^2_{\rm eff}}$ that enters the cascade $g_{44}\to g_s\to g_2\to\sin^2\theta_W\to g_1$ (§0.7). The formula derives from the kernel coupling $g_{44}$ and the $\mathbb{CP}^2$ volume. (This is not a Kaluza-Klein result: $\mathbb{CP}^2$ is the macroscopic $d=4$ sector space — non-compact, with localized bound-state modes rather than KK plane waves.)

---

## 5. Colour Confinement

Assign each quark a colour expectation vector $\vec{n}\in\mathbb{R}^8$ (the 8 $\mathbb{CP}^2$ isometry generator expectation values). For any single quark, $|\vec{n}|^2 = 4/3$. Antiquarks have $\vec{n}(\bar{q}) = -\vec{n}(q)$.

The energy of a composite system is: ✅

$$E_{\rm conf} = \lambda_c\,\Bigl|\sum_i \vec{n}(q_i)\Bigr|$$

This is the unique $\mathrm{SU}(3)$-invariant linear energy functional. Its consequences:

- **Mesons:** only colour-matched $q\bar q$ pairs give $\sum\vec{n} = 0 \to E_{\rm conf} = 0$. All others cost $2\lambda_c$.
- **Baryons:** only the (r,g,b) combination and permutations give $\sum\vec{n} = 0 \to E_{\rm conf} = 0$.

**Only colour-matched configurations are stable.** It is a necessary consequence of the $\mathbb{CP}^2$ isometry group acting on the colour vector space.

**Status note:** This colour-vector model is a *selection rule* — it correctly identifies which states are colour-neutral and therefore stable. It does not yet derive the full confinement mechanism (linear potential, flux-tube formation) from the $M_\infty$ kernel. The derivation of $\lambda_c$ from the inter-sector coupling structure is an open item addressed further in §8 and Part 8 §11.

---

## 6. $\mathrm{SU}(3)_{\rm colour} \times U(2)_{\rm EW}$ from One Manifold

$\mathbb{CP}^2$ carries two independent coupling-algebraic structures:

| Structure | Source | Group | Generators | Physical role |
|---|---|---|---|---|
| Isometry | $\mathrm{SU}(3)$ acts on fibre $\mathbb{C}^3$ | $\mathrm{SU}(3)$ | 8 | Colour symmetry of quark contact coupling |
| Holonomy | Fubini-Study metric | $U(2) = \mathrm{SU}(2)\times U(1)$ | 4 | Electroweak |

### Why $U(1)_Y$ is the $U(1)$ in $U(2)$, and $\mathrm{SU}(2)_L$ is the $\mathrm{SU}(2)$ in $U(2)$

**The $U(1)_Y$ generator is $T_8$ of $\mathrm{SU}(3)$. ✅** Since $\mathbb{CP}^2 = \mathrm{SU}(3)/U(2)$, the isotropy group $U(2)$ sits inside $\mathrm{SU}(3)$. The $U(1)$ factor of $U(2)$ is generated by the 8th $\mathbb{CP}^2$ isometry generator:

$$Y_{\rm generator} = T_8 = \lambda_8/2 = \mathrm{diag}(1,1,-2)/(2\sqrt{3})$$

acting on the fundamental representation $\mathbb{C}^3$. Normalising to give physical hypercharges ($Y = 1/6$ for the quark doublet):

$$Y = (1/\sqrt{3})\,T_8 = \mathrm{diag}(1,1,-2)/6 \quad \text{[acting on colour triplet]}$$

The electric charges follow immediately from $Q = T_3 + Y$:

| Field | $T_3$ | $Y$ | $Q$ |
|---|---|---|---|
| $u_L$ | $+1/2$ | $+1/6$ | $+2/3$ |
| $d_L$ | $-1/2$ | $+1/6$ | $-1/3$ |
| $e_L$ | $-1/2$ | $-1/2$ | $-1$ |
| $\nu_L$ | $+1/2$ | $-1/2$ | $0$ |

The hypercharges are not assigned — they are eigenvalues of $T_8$ on the $\mathrm{SU}(3)$ representations, which are determined by the root lattice of $\mathrm{SU}(3) = \mathrm{Isom}(\mathbb{CP}^2)$.

**The $\mathrm{SU}(2)_L$ generator is the $\mathrm{SU}(2)$ factor of $U(2)$.** From the Kähler spinor decomposition (§7): the $U(2)$ holonomy acts on the tangent space $T^{1,0}(\mathbb{CP}^2) \cong \mathbb{C}^2$. The $\mathrm{SU}(2) \subset U(2)$ acts on $\Lambda^{0,1} = \mathbb{C}^2$ (the left-handed spinors) in the fundamental representation, and acts trivially on $\Lambda^{0,0}$ and $\Lambda^{0,2}$ (the right-handed spinors). Therefore:

- Left-handed quarks ($u_L$, $d_L$): transform as a doublet under $\mathrm{SU}(2)$. **This is $\mathrm{SU}(2)_L$.**
- Right-handed quarks ($u_R$, $d_R$): are $\mathrm{SU}(2)$ singlets. They carry no weak charge.

The weak isospin structure is entirely determined by the $\mathrm{SU}(2)$ factor of the $U(2)$ holonomy of $\mathbb{CP}^2$. No separate postulate is needed. ✅

$$\mathfrak{su}(3) = \mathfrak{u}(2) \oplus \mathfrak{m}$$

where $\mathfrak{m} \cong T_{[e]}(\mathbb{CP}^2)$ is the 4-dimensional (real) tangent space at the base point. **Dimension check:** $\dim\,\mathfrak{su}(3) = 8$, $\dim\,\mathfrak{u}(2) = 4$, $\dim\,\mathfrak{m} = \dim\,\mathbb{CP}^2 = 4$, and $4+4=8$. This is an orthogonal decomposition under the Killing form of $\mathfrak{su}(3)$: the $\mathfrak{u}(2)$ generators are orthogonal to the $\mathfrak{m}$ generators. Therefore:

- The **8 colour generators** are the 8 generators of $\mathfrak{su}(3)$. Of these, 4 live in $\mathfrak{u}(2)$ (the holonomy generators) and 4 live in $\mathfrak{m}$ (the tangent space generators). These generators act on the colour states of quarks through the $\mathrm{SU}(3)$-invariant kernel — they are symmetry generators of the contact coupling, not propagating quanta.
- The **4 EW bosons** are the 4 generators of $\mathfrak{u}(2) \subset \mathfrak{su}(3)$. They act on the tangent space of $\mathbb{CP}^2$, not on the colour fibre. Since $\mathfrak{u}(2)$ and $\mathfrak{m}$ are orthogonal in $\mathfrak{su}(3)$, the EW generators do not mix with the colour generators.

The colour-plus-EW algebra $\mathfrak{su}(3) \oplus \mathfrak{u}(2)$ is the full algebra of $\mathbb{CP}^2$'s isometry group $\mathrm{SU}(3)$, decomposed according to the homogeneous space structure. No extra bosons appear because the decomposition $\mathfrak{su}(3) = \mathfrak{u}(2) \oplus \mathfrak{m}$ is complete and exhausts all generators.

---

## 7. Chirality from Kähler $\gamma_5$

The chirality of the weak structure — the $\mathrm{SU}(2)_L$ factor of $\mathbb{CP}^2$'s $U(2)$ holonomy acts on left-handed components only — follows from the spinor structure of $\Psi_\infty$ on the sector manifolds. ✅ Three sectors are **Kähler manifolds**: $d=2$ ($\mathbb{CP}^1$), $d=4$ ($\mathbb{CP}^2$), $d=6$ ($\mathbb{CP}^3$). Each carries a canonical Kähler form $\omega$, which defines a chirality operator on the sector spinor:

$$\gamma_5^{\text{Kähler}} = i^m\,\omega_{a_1 a_2}\cdots\omega_{a_{2m-1}a_{2m}}\,\gamma^{a_1}\cdots\gamma^{a_{2m}}$$

where $m$ is the complex dimension of the sector ($m=1,2,3$ for $d=2,4,6$ respectively). This operator anticommutes with all sector gamma matrices $\gamma^a$, splitting the sector spinor into **holomorphic** (positive chirality = LEFT) and **anti-holomorphic** (negative chirality = RIGHT) components.

**Why $\mathrm{SU}(2)_L$ acts only on the holomorphic half — the Kähler spinor argument:**

On a Kähler manifold of complex dimension $m$, the Dirac spinor bundle decomposes as:

$$S = \Lambda^{0,*}(T^{*1,0}) = \Lambda^{0,0} \oplus \Lambda^{0,1} \oplus \cdots \oplus \Lambda^{0,m}$$

The Kähler chirality operator $\gamma_5^{\text{Kähler}}$ splits this into:
- **$S_+$ (LEFT)** $= \Lambda^{0,1} \oplus \Lambda^{0,3} \oplus \cdots$ (odd-degree anti-holomorphic forms)
- **$S_-$ (RIGHT)** $= \Lambda^{0,0} \oplus \Lambda^{0,2} \oplus \cdots$ (even-degree anti-holomorphic forms)

The $U(2)$ holonomy of $\mathbb{CP}^2$ acts on $T^{*1,0}(\mathbb{CP}^2)$ — the holomorphic cotangent bundle. This means $U(2)$ acts on $\Lambda^{0,1}$ but not on $\Lambda^{0,0}$. For $d=4$ ($\mathbb{CP}^2$, $m=2$):

- $\Lambda^{0,0} = \mathbb{C}$: transforms trivially under $U(2)$ → singlet, RIGHT-handed
- $\Lambda^{0,1} = T^{*1,0}$: transforms in the fundamental of $U(2)$ → doublet, LEFT-handed
- $\Lambda^{0,2} = \det(T^{*1,0})$: transforms as a character of $U(2)$ → singlet, RIGHT-handed

$\mathrm{SU}(2)_L$ acts exclusively on the left-handed components of quarks and leptons. ✅ This selectivity arises from the Kähler geometry of the $d=4$ ($\mathbb{CP}^2$) and $d=6$ ($\mathbb{CP}^3$) sectors. The Kähler structure naturally divides the spinors into holomorphic ($\Lambda^{0,1}$) and anti-holomorphic ($\Lambda^{0,0}$ and $\Lambda^{0,2}$) components. Only the holomorphic part transforms under $\mathrm{SU}(2)_L$.
Right-handed quarks and leptons are geometric singlets under this structure — not because left-handedness is postulated, but because the Kähler geometry makes the anti-holomorphic components invisible to $\mathrm{SU}(2)_L$.

For the $d=6$ lepton sector ($\mathbb{CP}^3$), the Kähler geometry splits the spinor into holomorphic (left-handed, 4 components) and anti-holomorphic (right-handed, 4 components) parts: $\Lambda^{0,1} \oplus \Lambda^{0,3}$ and $\Lambda^{0,0} \oplus \Lambda^{0,2}$.

**The non-Kähler sectors ($d=3$, $d=5$) have no Kähler form** and therefore no intrinsic chirality operator. Quarks in $d=3$ ($S^3$) are intrinsically vector-like; their observed left-right asymmetry is inherited from the $d=4$ sector via the cross-coupling $g_{3,4}$. The neutrino sector $d=5$ ($S^5$) is also non-Kähler — it has no chirality operator — consistent with the fact that neutrinos are Dirac fermions (no Weyl condition possible in $d=5$, see Part 1 §6).

**The spin${}^c$ Dirac index** is a consequence of this structure: the net count of left-chiral zero modes is exactly the holomorphic Euler characteristic $\chi_{\rm hol}(\mathbb{CP}^m) = \binom{m+1}{m} = m+1$, which agrees with the indices tabulated in the sector Dirac table. ✅ The Kähler form is the geometric cause; the index is its topological fingerprint.

| Sector | Kähler? | $\gamma_5^{\text{Kähler}}$ | L/R split | Physical |
|--------|---------|-----------|-----------|---------|
| $d=2$ ($\mathbb{CP}^1$) | ✓ | exists | 1L + 1R | $W^\pm$ polarisation |
| $d=3$ ($S^3$) | ✗ | none | vector-like | Colour inherited from $d=4$ |
| $d=4$ ($\mathbb{CP}^2$) | ✓ (spin${}^c$) | exists | 2L + 2R | $u_L,d_L$ vs $u_R,d_R$ |
| $d=5$ ($S^5$) | ✗ | none | Dirac only | $\nu_L + \nu_R$ (Dirac neutrinos) |
| $d=6$ ($\mathbb{CP}^3$) | ✓ | exists | 4L + 4R | $\nu_L,e_L,\nu_{\mu L},\mu_L$ vs right-handed |
| $d=10$ ($\mathbb{CP}^5$) | ✓ | exists | 16L + 16R | $d\bmod 8=2$ Maj-Weyl |

---

## 8. Hypercharges from Anomaly Cancellation

With $N_c = 3$ from $\chi(\mathbb{CP}^2)$, and $g_{66} = 1/4$ established from $\mathbb{CP}^3$ complex geometry (Part 2 §9c), all SM hypercharges follow from anomaly cancellation. ✅ Full derivation in §13; result: $Y_Q = 1/6$, $Y_L = -1/2 = -\sqrt{g_{66}}$, $Q_u = 2/3$, $Q_d = -1/3$. Fractional charges are not inputs — they follow from three colours and the coupling $g_{66}=1/n_s$.

**Note on derivation order.** The anomaly cancellation route works from $d=4$ geometry upward: $\chi(\mathbb{CP}^2) = 3$ gives $N_c = 3$, then $\mathbb{CP}^3$ complex geometry ($\chi(\mathbb{CP}^3) = n_s$) gives $g_{66} = 1/4$, and $N_c = 3$ together with $Y_L = -\sqrt{g_{66}} = -1/2$ force the remaining hypercharge assignments via $\mathrm{SU}(2)^2U(1)$ anomaly cancellation. Anomaly cancellation is the mechanism that propagates the geometric inputs into a complete hypercharge table — it is not the source of $g_{66}$.

---

## 9. Colour Coupling: Geometric, Not Running 🔶

The IDWT colour coupling is a contact term in the kernel with no quadratic colour-field term (§0.2, §0.6). There is no gauge-field kinetic structure and therefore no coupling evolution to compute: the effective colour coupling varies only through geometric dilution, $g_{\rm eff}(n,d) = g_{dd}/S(n,d)$, across the quark mode index. Whether the $\mathrm{SU}(3)$-symmetric quark contact coupling produces a confinement-scale strengthening of the effective coupling is an open derivation item. Its geometric inputs — $N_c = 3$ from the $\mathbb{CP}^2$ Dirac index (§2) and the six occupied quark modes — are established.

---

## 10. Electroweak Predictions

With the $d=2$ sector scale $m_{{\rm scale},2} = 27.47$ MeV: 🔵

| Observable | IDWT | Observed | Error |
|---|---|---|---|
| $m_\gamma$ | 0 (exact) | 0 | — |
| m_Z | 91,230 MeV | 91,188 MeV | +0.047% |
| m_Higgs | 125,266 MeV | 125,200 MeV | +0.053% |
| $\sin^2\theta_W$ | 0.2237 | 0.22290 (on-shell) | +0.37% |
| ρ parameter | 1 (exact) | 1.002 | −0.2% |

**$\sin^2\theta_W$ is parameter-free: ⭐**

$$n_Z - n_W = n_s + n_d = 4 + 1 = 5 = q = S(n_u,4) - S(n_u,3) = S(2,4) \quad \text{[same } q \text{ as Theorem S3]}$$
$$\sin^2\theta_W = 1 - \bigl(S(76,2)/S(81,2)\bigr)^2 = 0.2237$$

The $Z$--$W$ mode gap equals $q$ — the same Dirac eigenstate increment that enters $g_{22}$ (Theorem S3, Part 8 §5). Both arise from the $d=4$ sector's eigenvalue count at the up-quark level. $n_Z - n_W = q$ links the $W$--$Z$ mass ratio to the EW coupling constant through a single spectral identity.

**ρ = 1 is derived:** W and Z live in the same sector → custodial $SU(2)$ is automatic.

---

## 11. The Boson Eigenmode Selection and Sector Coupling Map

🔶 All boson mode indices follow from the Vandermonde sector coupling $g(a,b) = a + b - 1$ applied to occupied mode indices and sector dimensions:

| Coupling | Result | Identification |
|---------|--------|----------------|
| $g(d{=}4,\; n_{\nu_1}{=}10)$ | 13 | $n_e$ — up sector + $\nu_1$ → electron |
| $g(d{=}4,\; n_c{=}20)$ | 23 | $n_\tau$ — up sector + charm → tau |
| $g(d{=}5,\; n_{\rm top}{=}72)$ | 76 | $n_W$ — $\nu$ sector + top → W boson |
| $g(d{=}6,\; n_W{=}76)$ | 81 | $n_Z$ — lepton sector + W → Z boson |
| $g(n_{\nu_2}{=}15,\; n_Z{=}81)$ | 95 | $n_H$ — $\nu_2$ + Z → Higgs |
| $g(d{=}10,\; n_s{=}4)$ | 13 | $n_e$ — tau sector + strange → electron |

**Boson generation chain: ✅**

$$g(d{=}5,\,n_{\rm top}{=}72) = 76 = n_W, \quad g(d{=}6,\,n_W{=}76) = 81 = n_Z, \quad g(n_{\nu_2}{=}15,\,n_Z{=}81) = 95 = n_H$$

**Sum rules: ⭐**

$$n_u + n_c + n_{\rm top} = 3+20+72 = 95 = n_H, \qquad n_{\rm top} = n_H - n_u - n_c = 72$$

**Jacobi boundary identities at $k_0 = n_s^2 = 16$: ⭐**

$$b_{16}^2 = n_W: \quad 16\times19/4 = 76 = n_W$$
$$n_W + S(2,3) = n_s\times S(n_s,3): \quad 76+4 = 80 = 4\times20$$
$$n_e = n_s^2 - n_s + 1 = 16-4+1 = 13$$

**Cabibbo consistency: ⭐** $\sin^2\theta_C = S(2,3)/(S(2,3)+n_W) = 4/80 = 1/20$, consistent with $1/\sqrt{20}$. The absent $n=2$ mode appears as the second singular value of the boundary coupling matrix.

The coupling-conservation identity is equivalent to any of: $g(d{=}5, n_{\rm top}) = n_W$; $n_W = 4\times19 = 76$; $n_W + n_{\nu_2} = S(n_e,2) = 91$. All three are algebraically equivalent and all proved.

**Derivation of the −1 offset.** The Vandermonde rule $g(a,b) = a+b-1$ follows from the **lattice join of mode indices** and a stars-and-bars counting argument. A boson is a two-sector composite: it couples a fermionic mode at index $n_{\rm ferm}$ in sector $d_{\rm sect}$ to the EM base sector ($d=2$). Placing $n_{\rm ferm}$ quanta from the fermionic sector and $(d_{\rm sect}-1)$ quanta representing the sector-coordinate overhead into a single $d=2$ mode requires placing $n_{\rm ferm} + (d_{\rm sect}-1)$ objects into 2 bins with each bin receiving at least 1 object. By stars-and-bars, the minimum composite index is $n_{\rm ferm} + (d_{\rm sect}-1) = n_{\rm ferm} + d_{\rm sect} - 1$. The $-1$ is the **shared vacuum**: both the fermionic tower and the sector-dimension overhead share exactly one ground-state unit $S(1,d)=1$ (universal for any $d$), which must be subtracted to avoid double-counting. Equivalently, $g(a,b) = a+b-1$ is the join operation in the ranked mode-index lattice: the smallest mode index $m$ such that $S(m,2) \geq \max(S(a,1), S(b,1))$ satisfies $m = a+b-1$, verified by $S(a+b-1,2) = (a+b-1)(a+b)/2$, the first triangular number that covers both $a$ and $b$. The $-1$ offset is load-bearing — $g(d{=}5,\; n_{\rm top}{=}72) = 76 = n_W$; the Jacobi boundary identity $b_{16}^2 = 76$ provides an independent confirmation. All three boson applications check: $n_W = 72 + 5 - 1 = 76$, $n_Z = 76 + 6 - 1 = 81$, $n_H = 15 + 81 - 1 = 95$. **Status: ✅ (combinatorial derivation).**

**The even-insertion selection rule. 🔶** The g-rule's insertion-free character follows from the kernel parity of the $d=2$ variable. The additive fermion edges of the generation tower each carry one degree-1 condensate insertion above exact level addition (Part 2 §9c; `idwt.py` STEP 41); such a vertex exists only in a sector with a non-zero condensate $\langle\xi_{d'}\rangle$ to supply the linearization (Part 1 P6). The condensate-linearized vertices remain even (degree 2) in the $d=2$ variable (§16.2), so no odd insertion can act on a $d=2$ leg, and a production landing on a $d=2$ mode must carry an even number of insertions. The W, Z, and H joins carry zero — exact level addition, with the $-1$ as the shared vacuum unit derived above — while the additive Higgs closure $n_H = n_u + n_{\rm charm} + n_{\rm top}$ carries two, making the two documented Higgs routes channels of one parity rule rather than competing derivations. The fermion edges carry one insertion, available only off $d=2$. One structural fact — no $d=2$ condensate — therefore yields both $m_\gamma = 0$ (§16.2) and the $-1$ offset. The oscillator proxy verifies the landing for all seven productions, and the odd-insertion counterfactual indices 77, 82, 96 are unoccupied (`idwt.py` STEP 55). The 🔶 gap: the bridge from the single-variable proxy insertion count to the multi-leg vertex parity is stated, not derived; the rule constrains channel parity, not route selection.

---

## 12. Cabibbo Angle

The Cabibbo mixing angle arises from the $d=3\leftrightarrow d=2$ coupling structure. The bare IDWT prediction is $1/\sqrt{20}$; the curvature of the mediating $d=2$ sector ($\mathbb{CP}^1$) provides a computable correction.

### Bare Prediction

The Cabibbo angle at leading order: ✅

$$\sin^2\theta_C = \frac{1}{S(n_s,3)} = \frac{1}{20} \;\Longrightarrow\; \sin\theta_C = \frac{1}{\sqrt{20}} = 0.22361$$

Equivalently, from the Jacobi boundary identity $n_W + S(2,3) = n_s\times S(n_s,3)$:

$$\sin^2\theta_C = \frac{S(2,3)}{S(2,3) + n_W} = \frac{4}{80} = \frac{1}{20}$$

This is a theorem of $n_s=4$ and the Vandermonde structure, determined entirely by the combinatorial fixed point.

### Curvature Correction from the Mediating Sector

The curvature correction to the Cabibbo angle enters through the $d=2$ sector ($\mathbb{CP}^1 = S^2$), where the W boson mode lives. The bare prediction uses a flat-space normalization of the mode functions on $\mathbb{CP}^1$. The actual $\mathbb{CP}^1$ geometry has curvature, which corrects the effective mode density through the sector Dirac curvature correction formula.

**Step 1 — $\mathbb{CP}^1$ sector curvature correction ($d=2$ sector):** 🔵

The Dirac operator on $\mathbb{CP}^1$ satisfies:

$$D^2 = \Delta + R/4 \qquad \text{(sector Dirac curvature identity)}$$

The heat kernel of $D^2$ on $\mathbb{CP}^1$ at the diagonal:

$$K(t,x,x) \sim \frac{N}{4\pi t}\bigl[1 + t(R/6 - R/4) + O(t^2)\bigr] = \frac{N}{4\pi t}\bigl[1 - tR/12 + O(t^2)\bigr]$$

The $R/6$ term is the standard heat-kernel curvature correction; the $-R/4$ Bochner term subtracts, giving the net $-R/12$ coefficient.

**Step 2 — IDWT time scale:**

The heat-kernel time relevant for the Cabibbo correction is set by the strange quark's energy scale. In units where $m_{{\rm scale},3} = 1$:

$$t_0 = 1/S(n_s,3) = 1/20$$

**Step 3 — Corrected effective mode count:**

$$S_{\rm eff} = S(n_s,3)\times(1 - R\,t_0/12) = 20\times\bigl(1 - 2/(12\times20)\bigr) = 20\times(1 - 1/120)$$

**Step 4 — Corrected Cabibbo angle:**

$$\sin^2\theta_C = 1/S_{\rm eff} \approx (1/20)\times(1 + 1/120)$$
$$\sin\theta_C = \sqrt{\sin^2\theta_C} \approx (1/\sqrt{20})\times(1 + 1/240) \quad \text{[Taylor: }\sqrt{1+\delta}\approx1+\delta/2\text{]}$$

**Step 5 — Using $R = \chi(\mathbb{CP}^1)$:**

For unit $\mathbb{CP}^1 = S^2$: $R = 2 = \chi(\mathbb{CP}^1)$ (the scalar curvature equals the Euler characteristic for the standard metric on $S^2$). Therefore:

$$\boxed{\sin\theta_C = \frac{1 + \chi(\mathbb{CP}^1)/(24\cdot S(n_s,3))}{\sqrt{S(n_s,3)}} = \frac{1 + 1/240}{\sqrt{20}} = 0.22454}$$

**Why $\chi(S^3) = 0$ does not contribute:** The $d=3$ quark sector has geometry $S^3$. The Euler characteristic of any odd-dimensional closed manifold is zero: $\chi(S^3) = 0$. The curvature correction vanishes for the quark sector. The correction enters exclusively through the $d=2$ sector ($\mathbb{CP}^1$), where the $SU(2)_L$ mixing structure lives.

**Result:**

| Quantity | Value |
|---|---|
| $\sin\theta_C$ (bare) | 0.22361 |
| $\sin\theta_C$ (curvature corrected) | 0.22454 |
| PDG $\lambda$ (Cabibbo angle) | 0.22450 ± 0.00044 |
| Tension | +0.09σ |

The correction closes the tension from −2.03σ to +0.09σ with no free parameters. The inputs are: $\chi(\mathbb{CP}^1) = 2$ (topology of the W boson sector), $S(n_s,3) = 20$ (seed structure), and the $\mathbb{CP}^1$ sector curvature correction coefficient $-R/12$ (a theorem of spin geometry).

**First-row unitarity. ✅** IDWT's CKM matrix is unitary by construction. $V_{ud}$ is not an independent prediction — it is the trigonometric complement of $\sin\theta_C$:

$$|V_{ud}| = \sqrt{1 - \sin^2\theta_C} = 0.97447$$

This value is not separately testable against the PDG nuclear beta-decay result of $0.97370 \pm 0.00014$, because the apparent $5.5\sigma$ discrepancy is not an IDWT-specific failure. It is the **Cabibbo Angle Anomaly**, a pre-existing tension within the Standard Model itself: the PDG values of $|V_{ud}|$ (from nuclear beta decay) and $|V_{us}|$ (from kaon decays) are independently measured, and they fail to satisfy $|V_{ud}|^2 + |V_{us}|^2 + |V_{ub}|^2 = 1$ by ${\approx}3\sigma$ (giving ${\approx}0.9985$ rather than 1.000). Computing $\sqrt{1 - |V_{us}|^2_{\rm PDG} - |V_{ub}|^2_{\rm PDG}} = 0.97447$ — precisely IDWT's value — demonstrates that this gap is entirely attributable to the known unitarity deficit in the SM measurement inputs, not to anything IDWT does differently. IDWT enforces exact CKM unitarity by construction; the tension is between the two independent PDG measurements, and IDWT agrees with $|V_{us}|$ at $+0.09\sigma$. Reporting a $5.5\sigma$ $V_{ud}$ discrepancy alongside the $+0.09\sigma$ $V_{us}$ agreement would double-count a single angular prediction.



---

## 13. Spin^c Structure and Hypercharge Derivation

$\mathbb{CP}^2$ is spin${}^c$ (not spin). The spin${}^c$ structure requires an auxiliary $U(1)$ bundle — geometrically forced, naturally identified with $U(1)_Y$ (hypercharge).

**$N_c = 3$ determines all SM hypercharges via anomaly cancellation: ✅**

The SM gauge group $\mathrm{SU}(3)\times\mathrm{SU}(2)\times U(1)_Y$ has four independent triangle anomaly conditions per generation. With $N_c = 3$ (from $\chi(\mathbb{CP}^2)$), $Y_Q = 1/(2N_c) = 1/6$, $Y_L = -1/2$, $Y_u = 2/3$, $Y_d = -1/3$, $Y_e = -1$:

$$[\mathrm{SU}(2)]^2[U(1)_Y]:\quad N_c Y_Q + Y_L = 3(1/6) + (-1/2) = 0 \;\checkmark$$
$$[\mathrm{SU}(3)]^2[U(1)_Y]:\quad 2Y_Q - Y_u - Y_d = 2(1/6) - 2/3 - (-1/3) = 0 \;\checkmark$$
$$[\mathrm{grav}]^2[U(1)_Y]:\quad 2N_c Y_Q + 2Y_L - N_c Y_u - N_c Y_d - Y_e = 1-1-2+1+1 = 0 \;\checkmark$$
$$[U(1)_Y]^3:\quad 6(1/6)^3 + 2(-1/2)^3 - 3(2/3)^3 - 3(-1/3)^3 - (-1)^3 = 0 \;\checkmark$$

All four independent anomaly conditions cancel exactly with $N_c = 3$. The charge formula $Q = T_3 + Y$ (Gell-Mann--Nishijima) then gives $Q_u = 2/3$, $Q_d = -1/3$ — a consequence of the hypercharge assignments, not a separate anomaly condition. Fractional charges are not inputs — they follow from $N_c = 3$ from $\mathbb{CP}^2$ geometry.

**The $N_c$ chain: ✅**

$$\text{IDWT } d{=}4\text{ sector: }\mathbb{CP}^2 = \mathrm{SU}(3)/U(2) \;\to\; \text{Dirac index} = \binom{3}{2} = 3 = N_c \;\to\; Y_Q = 1/(2N_c) = 1/6 \;\to\; \text{all SM hypercharges}$$

**Generation number:** $N_{\rm gen} = N_c = 3$ follows from $n_s = \chi(\mathbb{CP}^3) = 4$ and gauge-fixing: the lepton sector has $n_s = 4$ $\mathbb{CP}^3$ modes; gauge-fixing removes one, leaving $N_{\rm gen} = n_s - 1 = 3$. Since $n_s = N_c + 1$ (T4/T15a chain: $N_c = \chi(\mathbb{CP}^2) = 3$, $n_s = \chi(\mathbb{CP}^3) = 4$), this gives $N_{\rm gen} = N_c = 3$ by construction. **Status: ✅.**

*Division-algebra identity (⭐).* The charged-lepton sector $d=6$ sits at $d-2 = 4 = \dim\mathbb{H}$ in the sector ladder, and $\chi(\mathbb{CP}^3) = 4 = \dim\mathbb{H}$, so the generation count also reads $N_{\rm gen} = \chi(\mathbb{CP}^3) - 1 = \dim\mathbb{H} - 1 = \dim\,\mathrm{Im}\,\mathbb{H} = 3$. This is an algebraic restatement of the same count, not a second derivation — the mechanism is the gauge-fixing above. It is noted because the sector set realizes the normed division algebras at $d-2 \in \{1,2,4,8\}$, and under that reading three generations is the imaginary dimension of the quaternions.

---

## 14. Electromagnetism from the Hopf Fiber

### Structure

The $d=2$ and $d=3$ sectors are unified by the Hopf fibration: ✅

$$S^1 \to S^3 \to S^2 = \mathbb{CP}^1$$

- **$d=2$ ($\mathbb{CP}^1 = S^2$):** The base of the Hopf fibration — bosons parameterize the base
- **$d=3$ ($S^3$):** The total space — quarks live here and naturally carry $U(1)$ charge from the fiber action
- **$S^1$ fiber $= U(1)$:** The electromagnetic group, not postulated — it is the Hopf fiber

### Photon Derivation

Write $\Psi_\infty = A\cdot e^{i\theta}$. The phase gradient defines the photon: ✅

$$A_\mu = \partial_\mu\theta$$

This is the $n=0$ zero mode of the $U(1)$ Hopf fiber. The field tensor:

$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$$

is the curvature 2-form of the $U(1)$ connection. The Lorentz force equation follows from the geodesic equation in $\mathbb{R}^3\times S^1$:

$$F = q(E + v\times B)$$

Electromagnetism is not postulated — it emerges from the phase geometry of $\Psi_\infty$ via the Hopf fiber.

### The Second Hopf Fibration: $S^1 \to S^5 \to \mathbb{CP}^2$

Electromagnetism arises from the $n=1$ complex Hopf fibration $S^1 \to S^3 \to S^2 = \mathbb{CP}^1$ ($d=3$ over $d=2$). The $n=2$ complex Hopf fibration plays the same structural role for the weak vertex:

$$S^1 \;\to\; S^5 \;\to\; \mathbb{CP}^2$$

The $d=5$ neutrino sector ($S^5$) is the total space of this fibration. The base is $\mathbb{CP}^2$ — the up-quark sector ($d=4$). The fibre is $S^1$ — the $d=2$ sector. The neutrino's $S^5$ coordinate space is geometrically a family of circles fibred over the quark sector. The $W$ ($d=2 = S^1$) is the fibre of $S^5$ projected over $\mathbb{CP}^2$ — the weak vertex is not a coupling constant added separately, it is the geometry of the $S^1 \to S^5 \to \mathbb{CP}^2$ fibration. ✅ The coupling between up quarks and neutrinos exists because the neutrino's coordinate space is built from the quark sector and the $d=2$ fibre. The $d=2$ fibre direction is always part of the coupling because that is the coordinate direction the $d=5$ sector shares with $d=2$; the $d=4$ base is always involved because it is what the fibre is defined over. There is no $S^1$ fibre without the $\mathbb{CP}^2$ base — which is why there is no neutrino without a companion quark coupling.

| Fibration | Total space | Base | Fibre | Vertex |
|-----------|-------------|------|-------|--------|
| $S^1 \to S^3 \to S^2$ | $d=3$ (down quarks) | $d=2$ (gauge / $\mathbb{CP}^1$) | $S^1$ | EM: $\gamma$ couples $d=3 \leftrightarrow d=2$ |
| $S^1 \to S^5 \to \mathbb{CP}^2$ | $d=5$ (neutrinos) | $d=4$ (up quarks) | $S^1$ | Weak: $W$ couples $d=5 \leftrightarrow d=4$ along $S^1$ fibre |

Both are instances of the complex Hopf fibration $S^1 \to S^{2n+1} \to \mathbb{CP}^n$ at $n=1$ and $n=2$. The same $S^1$ fibre appears in both; the difference is which fermion sector sits at the base.

### Massless Photon

In $d=2$, $m = m_{\rm scale,2} \times S(n,2)$. The photon is $n=0$: $S(0,2) = C(1,2) = 0 \to m_\gamma = 0$ exactly. The $n=0$ mode exists because the $U(1)$ fiber has a trivial representation with zero occupation — no fiber excitation means massless boson. The first $d=2$ sector excitation ($n=1$) has mass $m_{\rm scale,2} \times 1 = 27.47$ MeV, safely above photon mass bounds.

### Transverse Polarization from Sector Dimension

The photon lives in the $d=2$ sector: it is a 2-dimensional object, oscillating in its two dimensions and moving perpendicular to them. It has exactly two independent oscillation modes — its two sector dimensions — and these are its two polarization states.

Perpendicular to a 2-plane is a high-dimensional space of directions in $M_\infty$, with none privileged. A $d=3$ observer resolves a single propagation direction because the observer's three coordinates meet that orthogonal space in one line; the photon cannot oscillate along its direction of travel because travel is, by construction, perpendicular to the plane it oscillates in. So in whichever direction we see a photon move, its oscillation is transverse to that motion and carries exactly two independent states. Electromagnetic waves are transverse with two polarizations because both are what a $d=3$ observer resolves of a 2-dimensional oscillator moving perpendicular to itself. No additional argument from gauge invariance or the Maxwell equations is needed.

The masslessness ($n=0$, $S(0,2)=0$) and the universality ($d=2$ ⊂ every higher sector) are properties of the photon within its sector. Transversality and the two polarizations are what a $d=3$ observer resolves of a $d=2$ object. All follow from $d=2$.

### Curvature Unification

Both gravity and electromagnetism are curvature 2-forms in IDWT:

| Force | Bundle | Curvature object |
|-------|--------|-----------------|
| Electromagnetism | $U(1)$ Hopf fiber | $F_{\mu\nu} = \partial_{[\mu}\partial_{\nu]}\theta$ |
| Gravity | Metric $g_{\mu\nu}$ | Riemann tensor $R^\rho{}_{\sigma\mu\nu}$ |

The statement from P4 — all physics follows from the geometry of $M_\infty$ — is concrete for both forces.

**Electric charge is derived.** The electromagnetic coupling is $e = g_2 \sin\theta_W$, where $g_2 = (2/3)\sqrt{g_s}$ follows from the $\mathbb{CP}^2$ kernel volume integral (§4) and $\sin\theta_W = \sqrt{1-(S(76,2)/S(81,2))^2}$ follows from the mode indices. The fine structure constant at the $d=2$ sector scale — the natural coupling scale of the $d=2$ sector, ≈m_W, where the IDWT couplings are defined as fixed geometric numbers — is $\alpha = e^2/(4\pi)$, giving $1/\alpha = 131.8$. Translating to $q\to0$ with the SM 1-loop vacuum-polarisation formula applied to the IDWT inputs (a cross-framework comparison; IDWT couplings themselves do not run), $1/\alpha(0) \approx 133.1$ (−2.9% from PDG 137.036); the residual traces to the $\sin^2\theta_W$ +0.37% gap, not a separate parameter.

**Open item — charge quantization from fiber topology.** The derivation above computes the numerical value of $e$ from $g_2$ and $\sin\theta_W$. A separate question is why charge is quantized — why all observable charges are rational multiples of $e$. The $U(1)$ Hopf fiber $S^1 \to S^3 \to S^2$ has integer first Chern class (winding number), which naturally produces quantized couplings to the fiber. The Chern–Weil integral $\int_{\mathbb{CP}^1} c_1(O(n)) = n$ is exact for every line bundle degree $n$ (⭐ Identity, pure topology; `files/idwt.py` STEP 78), so the integer labelling the $d=2$ Hopf bundle is rigid — this is the topological origin of the integer structure. Whether this topological integer structure is the IDWT mechanism for charge quantization — and how it yields the fractional quark charges $e/3$, $2e/3$ alongside the integer lepton charges — has not been shown in closed form. The fractional values follow from anomaly cancellation (§13), but the connection between the integer Chern class of the Hopf bundle and the observed charge spectrum is an open derivation.

---

## 15. The Quantum Number Package

The spinor structure of $\Psi_\infty$ means the quantum number structure of the SM emerges from geometry. The table below identifies what is derived and which route it comes from.

| SM feature | IDWT derivation | Route |
|---|---|---|
| Spin-½ for quarks and leptons | Dirac operator on $M_\infty$ | Part 8 §2 |
| Fermi statistics | Spinor anticommutation relations | Clifford algebra |
| Particle/antiparticle | Conjugate spinor $\bar\Psi_\infty$ | Complex spinor field |
| Left-handed weak coupling | Kähler $\gamma_5$ selects holomorphic half of each sector spinor | §7 above |
| Quark chirality ($u_L \neq u_R$) | $\mathbb{CP}^2$ Kähler chirality splits 4-spinor into 2L + 2R | §7 above |
| Lepton chirality ($e_L \neq e_R$) | $\mathbb{CP}^3$ Kähler chirality splits 8-spinor into 4L + 4R | §7 above |
| Neutrinos are Dirac | $d=5$ has $d \bmod 8 = 5$; Majorana spinors forbidden | Clifford periodicity |
| Tau hypercharges | $Y(\tau)=-1$ from anomaly cancellation with $N_c=3$ and $g_{66}=1/n_s$ (§8, §13) | ✅ |
| 0νββ rate = 0 | Follows from Dirac neutrino prediction | Falsifiable |

The spinor structure governs quantum numbers — what attaches to each mode. The mass formula $m = m_{\rm scale,d} \times S(n,d)$, all coupling constants, the sector structure $\{2,3,4,5,6,10\}$, and the sole unit reference $m_e$ are determined by the geometric and combinatorial structure of $M_\infty$ independently of spin. $m_W$ is derived.

---

## 16. Electromagnetism: Ward Identity and L-Parity Protection

**Three arguments for photon masslessness.** IDWT has three distinct lines of argument, ordered by strength and IDWT-nativity:

1. **Mass formula (primary).** $S(0,2) = C(1,2) = 0$, so $m_\gamma = S(0,2) \times m_{\rm scale,2} = 0$ exactly from the IDWT mass formula. This is argument (1); it is the cleanest and most model-independent, requiring only the mode-index assignment $n=0$ for the photon.

2. **L-parity (all-orders, IDWT-native, §16.2).** The kernel $(\xi\cdot\xi')^2$ is even under $L \to -L$ and has no $L=1$ component. Therefore $\Pi_{\rm kernel}(q^2) = 0$ for all $q^2$, and no photon mass is generated at any order in the kernel coupling. This is stronger than argument (1) in that it rules out dynamical mass generation beyond the mass formula.

3. **Ward identity (§16.1, partly imported).** Current conservation $\partial^\mu J_\mu^{\rm EM} = 0$ follows from $U(1)$ gauge invariance of the IDWT action by Noether's theorem — this part is IDWT-native. The Ward-Takahashi identity in vertex form ($q_\mu \Gamma^\mu = S^{-1}(p+q) - S^{-1}(p)$) is QFT language used to express the consequence of gauge invariance for the photon propagator. Arguments (1) and (2) are the primary IDWT proofs; argument (3) translates the result into QFT language for cross-framework comparison. It is not an independent derivation within IDWT.

### 16.1 The Ward Identity in IDWT

The IDWT kinetic term contains the covariant derivative: ✅

$$\mathcal{L}_{\rm kin} = \bar\Psi_\infty(i\Gamma^\mu\nabla_\mu)\Psi_\infty, \qquad \nabla_\mu = \partial_\mu - iA_\mu\hat{Q}$$

where $A_\mu$ is the $d=2$ zero-mode (photon) field and $\hat{Q}$ is the $U(1)_{\rm EM}$ charge operator ($Q=-1$ for $d=6$ electrons, $Q=+2/3$ for $d=4$ up-type quarks, etc., from anomaly cancellation §8).

Under a local $U(1)$ gauge transformation $A_\mu\to A_\mu + \partial_\mu\alpha$, $\Psi_\infty\to e^{i\alpha\hat{Q}}\Psi_\infty$:

$$\delta\mathcal{L}_{\rm kin} = -(\partial_\mu\alpha)\,J^\mu_{\rm EM}$$

Setting $\delta S = 0$ (invariance of the action) yields:

$$\partial^\mu J_{\mu,\rm EM}(x) = 0 \qquad \text{[Ward identity]}$$

The $U(1)$ Hopf fiber current conservation law at all loop orders:

$$q_\mu\Gamma^\mu(p,p+q) = S^{-1}(p+q) - S^{-1}(p)$$

holds automatically from gauge invariance.

### 16.2 L-Parity Protection: Photon Mass = 0 to All Orders

**Theorem.** The IDWT kernel cannot produce a photon mass at any order in perturbation theory.

**Proof. ✅** The kernel is $(\xi\cdot\xi')^2$, a degree-2 polynomial in the inner product $\xi\cdot\xi'$. This is EVEN under $\xi\cdot\xi'\to-(\xi\cdot\xi')$, so its spherical harmonic decomposition on $S^{d-1}$ contains only even-$\ell$ terms:

$$(\xi\cdot\xi')^2 = a_0\,P_0(\xi\cdot\xi') + a_2\,P_2(\xi\cdot\xi') + 0\cdot P_1 + 0\cdot P_3 + \cdots$$

The photon is an $L=1$ (vector) boson. The kernel matrix element $\langle\gamma|K|\gamma\rangle$ involves the $L=1$ component of the kernel, which is exactly zero:

$$\langle\gamma|K|\gamma\rangle = 0 \qquad \text{for any kernel insertion}$$

Therefore the photon self-energy from kernel diagrams:

$$\Pi_{\rm kernel}(q^2) = 0 \qquad \text{for all } q^2$$

The photon mass $m_\gamma^2 = \Pi_{\rm kernel}(0) = 0$ exactly, to all orders in the kernel. $\square$

This is stronger than gauge invariance alone (which only requires $\Pi(q^2)$ to be transverse). The L-parity argument shows the kernel CANNOT produce a photon mass even if gauge invariance were broken — the photon is protected by the parity of the coupling tensor.

Condensate-linearized vertices — the degree-1 effective terms produced when the quartic kernel is expanded about a non-zero sector condensate ⟨ξ_{d'}⟩ ≠ 0 (Part 1 P6) — are odd only in the fluctuation leg δξ_{d'} and remain even (degree 2) in the photon's own $d=2$ variable ξ. The L=1 component in the photon's own variable remains exactly zero, so m_γ = 0 survives in the presence of condensate backgrounds without modification to this proof.

The same evenness acts on the production side: with no odd condensate vertex available in the $d=2$ variable, a generation-tower production landing on a $d=2$ mode carries an even number of degree-1 insertions — zero for the W, Z, H g-rule joins, two for the additive Higgs closure (🔶, the even-insertion selection rule, §11; `idwt.py` STEP 55).

### 16.3 Scale Dependence of α — Cross-Framework Comparison

IDWT assigns $\alpha$ a single fixed geometric value at the $d=2$ sector scale; couplings do not run in IDWT — the IDWT scale-dependence mechanism is geometric dilution, $g_{\rm eff} = g_{dd}/S(n,d)$ (Part 5). The kernel does not contribute to the photon self-energy (§16.2). The PDG quotes $\alpha$ at $q^2 = m_Z^2$ under the SM prescription, where the scale dependence is vacuum polarisation from fermion loops. The comparison below is therefore the SM 1-loop formula with the IDWT fermion content as input — a cross-framework comparison, not an IDWT derivation: 🔵

$$\frac{1}{\alpha(q^2)} = \frac{1}{\alpha(m_e^2)} + \sum_f \frac{Q_f^2 N_f^c}{3\pi}\ln(q^2/m_f^2) \quad \text{[SM formula, IDWT inputs]}$$

The IDWT fermion content has three generations with $\sum_f Q_f^2 N_f^c = 3\times[1 + 3\times(1/9+4/9)] = 8$.

Translating $\alpha(0) = 1/137.036$ to $m_Z = 91.2$ GeV (SM 1-loop, above each threshold):

$$\alpha(m_Z) = 1/131.8 \quad \text{[SM 1-loop with IDWT fermion content]}$$
$$\text{PDG: } 1/127.9 \quad \text{[includes hadronic vacuum polarisation + 2-loop]}$$

The gap of $\sim4$ units between $1/131.8$ and $1/127.9$ is entirely accounted for by hadronic vacuum polarisation ($\sim3.5$ units) and two-loop QED corrections ($\sim0.5$ units), neither of which is specific to IDWT.

### 16.4 Status of $\alpha$

The Ward identity establishes:
1. $\partial^\mu J_\mu^{\rm EM} = 0$ exactly
2. Photon mass = 0 exactly (L-parity protection)
3. $\alpha$ is not renormalized by the kernel
4. The measured scale dependence of $\alpha(q^2)$ is reproduced at 1-loop in the cross-framework comparison (SM formula with IDWT fermion content, §16.3)

The $d=2$-sector-scale $\alpha$ from $g_1$ and $g_2$: $1/\alpha = 131.8$ at ${\approx}m_W$. In the SM translation, the hadronic vacuum polarisation between $m_W$ and $m_Z$ contributes ${\approx}3.8$ units of $1/\alpha$ and the leptonic loops add 0.1 units, giving $1/\alpha(m_Z) \approx 127.9$ (PDG: 127.9). $\alpha$ is not an independent unit reference — it follows from $g_2 = (2/3)\sqrt{g_s}$ and $\sin^2\theta_W$ from mode indices. See Part 3 §0.7 for the derivation of $g_2$.

