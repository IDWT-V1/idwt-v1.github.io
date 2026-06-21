# Infinite Dimensional Wave Theory — Part 11: Chemistry

**Status key:** ⭐ Identity · ✅ Structural consequence · 🔵 Numerically verified · 🔶 Motivated / open · ❓ Conjecture

---

## Overview

Part 11 develops chemistry from the $d=6$ orbit structure established in Part 8. The boundary between the two documents is fixed as follows: the single-electron machinery — the hydrogen Hamiltonian and its exact potential separability (Part 8 §14.2, Lemma 1), the orbit state classification $\mathrm{Sym}^L(\mathbb{C}^4)$ under $SU(4)$ ⊃ $SU(3)$ ⊃ SO(3) with its observable and $\mathbb{CP}^3$-hidden states (Part 8 §14.3), the selection rules (Lemma 2), and the Bohr spectrum — lives in Part 8 and is used here by reference. Part 11 begins where more than one electron, or more than one nucleus, enters.

Three established results are inherited throughout:

- The electron is the ($n=13$, $d=6$) mode of $\Psi_\infty$, executing a 6D orbit on the $\mathbb{CP}^3$ sector; the s, p, d, f orbital shapes are the $d=3$ projections of its orbit angular-momentum eigenstates (Part 1 §3d; Part 8 §14.3).
- A $d=3$ observer sees an exact $1/R$ Coulomb potential from any sector $d \geq 3$ (Part 3 §0.8a, Coulomb projection theorem); the atomic force law carries no correction from the hidden $\mathbb{CP}^3$ coordinates.
- Pauli exclusion is a structural consequence of the fermionic anticommutation of $\Psi_\infty$ (Part 1 §7; Part 8 §14.4): co-present electron resonances are distinct modes.

Part 8 also establishes the multi-electron and molecular setting this Part works in: the two-electron Hamiltonian with the repulsion term as the same Coulomb vertex (Part 8 §16.1), exchange antisymmetry from the spinor anticommutation (§16.2), the Aufbau filling structure (§16.4), and the two-center bond mechanism with Born–Oppenheimer decoupling (§17). What Part 8 leaves open — quantitative bond parameters, bond angles (§17.6), correlation energies — is the business of this Part. Every result here is stated with its premises explicit, and each status label applies to the result *given those premises*; §4 derives the premises of §1 from the Part 8 structure to the extent currently possible.

---

## §1. Hybridisation Angles from Orbit-State Orthogonality

### 1.1 Setting and premises

Hybridisation in IDWT is a basis choice, not a mixing process: the $SU(4)$ isometry of $\mathbb{CP}^3$ rotates exactly between the $d=3$ projections of the electron's orbit angular-momentum eigenstates, and the electron settles into the angular-momentum configuration of its 6D orbit that fits its bonding environment (Part 1 §3d). The states available to a bonding electron at a single center, at lowest angular momentum, are the $L=0$ and $L=1$ observable orbit states of Part 8 §14.3:

$$V = \operatorname{span}\{|s\rangle,|p_x\rangle,|p_y\rangle,|p_z\rangle\} \qquad (\text{four orbit states})$$

Every state in V is a full 6D orbit state of the $d=6$ electron — the labels s, p refer to its observable harmonics, not to a 3D object. The L=1 level also contains one $\mathbb{CP}^3$-hidden state (the $z_4$ direction, Part 8 §14.3); it is excluded from V not by neglect but by Lemma 2: the nuclear potential that shapes the bonding environment is a $d=3$ structure, and no $d=3$ operator connects the hidden state to the observable ones, so it takes no part in selecting bond directions.

A hybrid orbit state along the unit direction $\mathbf{n}_i \in \mathbb{R}^3$ is

$$|h_i\rangle = a_i|s\rangle + b_i(\mathbf{n}_i\cdot|\mathbf{p}\rangle), \qquad a_i^2 + b_i^2 = 1,$$

where $a_i^2$ is the s-share of the state. The premises:

- **P1 (orbit states). ✅ in the degenerate-shell idealization (§4.2).** Each σ-bonding electron at the center occupies a hybrid orbit state $|h_i\rangle \in V$ whose direction $\mathbf{n}_i$ is the internuclear axis of its bond. The state space V is established (Part 8 §14.3); the directed zonal form is derived in §4.2 from the axial symmetry of the companion nucleus's potential, exactly in the degenerate-shell idealization, with the s–p splitting of multi-electron centers as the stated refinement.
- **P2 (orthogonality). ✅ (§4.1).** The n co-present bonding resonances at the center are distinct modes of $\Psi_\infty$ and their orbit states are mutually orthogonal. This is derived in §4.1 from exchange antisymmetry (Part 8 §16.2): the n-electron state depends only on the occupied subspace, so the directed states may always be taken orthonormal.
- **P3 (equivalence). ✅ given identical ligands (§4.3).** The n bonds are equivalent: the n hybrid states are related by a symmetry of the center and have equal s-share. Derived in §4.3 for n identical ligands whose arrangement symmetry acts transitively on the bond axes.

### 1.2 The angle identity

⭐ **Theorem (hybridisation angles).** Let $|h_1\rangle, \ldots, |h_n\rangle$ ($2 \leq n \leq 4$) be orthonormal states of the form above whose span contains $|s\rangle$, with equal s-shares. Then

$$\mathbf{n}_i\cdot\mathbf{n}_j = -\frac{1}{n-1} \qquad \text{for all }i\neq j.$$

*Proof.* Since the $|h_i\rangle$ are an orthonormal basis of a subspace containing $|s\rangle$, completeness gives $\sum_i |\langle s|h_i\rangle|^2 = \sum_i a_i^2 = 1$; equivalence gives $a_i^2 = 1/n$ for each $i$. Orthogonality of a pair then reads

$$\langle h_i|h_j\rangle = \tfrac{1}{n} + \bigl(1-\tfrac{1}{n}\bigr)(\mathbf{n}_i\cdot\mathbf{n}_j) = 0 \;\Longrightarrow\; \mathbf{n}_i\cdot\mathbf{n}_j = -\frac{1}{n-1}. \quad\square$$

The identity is pure linear algebra — it holds for any states of this form, with or without the IDWT postulates. The bond angles follow:

| Configuration | $n$ | $\cos\theta$ | Angle |
|---|---|---|---|
| sp | 2 | −1 | 180° |
| sp$^2$ | 3 | −1/2 | 120° |
| sp$^3$ | 4 | −1/3 | 109.471° |

The sp$^3$ entry is the tetrahedral angle arccos(−1/3) = 109.47° of Part 1 §3d, obtained here from the orbit state space with no input beyond P1–P3.

⭐ **Capacity remark.** V holds four mutually orthogonal states in all, so a center bonding through $L \leq 1$ orbit states supports at most four σ bonds. Larger coordination requires $L=2$ orbit states (the d-shell), which enlarges the available state set; the six-coordinate case is worked out in §1.6.

### 1.3 Numerical verification

🔵 `files/idwt.py` STEP 42 constructs the hybrid states explicitly for n = 2, 3, 4 (collinear, trigonal planar, tetrahedral direction sets), confirms orthonormality to machine precision, and reproduces 180°, 120°, 109.471°.

### 1.4 Non-equivalent hybrids: water 🔶

Dropping P3 while keeping P1–P2: oxygen in H$_2$O carries four hybrid orbit states — two bond states (each reaching an H nucleus) and two lone-pair states. Parameterise the s-share asymmetry as $a_{\rm bond}^2 = 1/4 - \delta$, $a_{\rm lone}^2 = 1/4 + \delta$ (the completeness sum $\Sigma a_i^2 = 1$ is preserved). Orthogonality of the two bond states gives

$$\cos\theta_{\rm HOH} = -\frac{\tfrac{1}{4}-\delta}{\tfrac{3}{4}+\delta}.$$

The measured H–O–H angle of 104.5° corresponds to $\delta = 0.050$, i.e. lone-pair states with five percentage points more s-share than bond states; the same $\delta$ puts the lone-pair axes at 115.4°. The value of δ is fitted to the measured angle, not predicted; deriving δ from the oxygen nuclear charge and bonding environment is an open calculation. *Cross-framework comparison:* in quantum-chemistry language this s-share asymmetry is Bent's rule; here it is a statement about the s-content of orbit states, and the comparison is not a derivation.

Ammonia fits the same one-parameter family: nitrogen carries three bond states with s-share $1/4 - \delta$ and one lone-pair state with s-share $1/4 + 3\delta$ (the factor 3 preserves the completeness sum $\Sigma a_i^2 = 1$). Bond-state orthogonality gives the same relation $\cos\theta_{\rm HNH} = -(1/4 - \delta)/(3/4 + \delta)$; the measured H–N–H angle of 107.8° corresponds to $\delta = 0.016$. The fitted values order by lone-pair count — $\delta({\rm CH}_4) = 0 < \delta({\rm NH}_3) = 0.016 < \delta({\rm H}_2{\rm O}) = 0.050$ — which is the qualitative content of the family: each value is fitted, the monotone trend is the observation. 🔶 (`files/idwt.py` STEP 43.)

### 1.5 What is open

- The selection mechanism: §4.2 derives the directed zonal form of the bonding states at leading multipole order in the degenerate-shell idealization; the remaining energetics (the promotion-energy crossover and the symmetric ligand arrangement) are listed in §4.5.
- The quantitative two-center orbit: the bond mechanism is established (Part 8 §17), but the bond parameters (D_e, R_eq) and the full 6D character of the two-center orbit are open (Part 8 §17.6).
- δ for non-equivalent centers (§1.4) from first principles.

### 1.6 The general zonal identity and six-coordinate centers

The theorem of §1.2 extends to higher angular momentum. Call a hybrid orbit state *zonal* if it is built from the axially symmetric degree-L components about its own bond axis — true of the σ-bonding hybrids considered here, whose observable harmonics are symmetric about the internuclear axis.

- **P1′ (zonal form). 🔶** Each σ-bonding hybrid at the center is zonal about its bond axis, with angular-momentum shares $c_L^2$ ($\Sigma_L c_L^2 = 1$, $c_0^2$ the s-share).

⭐ **Overlap identity.** For two zonal hybrids along $\mathbf{n}_i$ and $\mathbf{n}_j$, the spherical-harmonic addition theorem gives

$$\langle h_i|h_j\rangle = \sum_L c_L^2\,P_L(\mathbf{n}_i\cdot\mathbf{n}_j),$$

with $P_L$ the Legendre polynomials. §1.2 is the $L \leq 1$ case, where the identity reads $1/n + (1 - 1/n)x = 0$.

⭐ **Six equivalent bonds (sp$^3$d$^2$).** Six equivalent zonal hybrids through $L \leq 2$ span the nine observable states of $L \leq 2$ only partially: the six hybrids exhaust |s⟩, the three |p⟩ states, and two zonal d states, so completeness forces the shares $c_0^2 = 1/6$, $c_1^2 = 1/2$, $c_2^2 = 1/3$ (sum = 1). Orthogonality of any pair then reads

$$\tfrac{1}{6} + \tfrac{x}{2} + \tfrac{1}{3}P_2(x) = 0 \;\Longleftrightarrow\; 3x^2+3x = 0 \;\Longleftrightarrow\; x\in\{0,-1\}.$$

Every pair of bond directions is forced to be perpendicular or antipodal, and six unit directions with pairwise cosines in {0, −1} are three orthogonal axes: the octahedron. The 90° geometry of six-coordinate centers (e.g. SF$_6$) follows from the shares and orthogonality alone, with no angle put in by hand.

⭐ **Equiangular cap.** $n$ directions in the three observable coordinates with equal pairwise cosine $c$ have Gram matrix $(1-c)I + cJ$, with eigenvalues $1-c$ (multiplicity $n-1$) and $1+(n-1)c$; realizability requires rank $\leq 3$, forcing $c = -1/(n-1)$ and $n \leq 4$. At most four equivalent equiangular σ directions exist. A five-coordinate center therefore cannot carry five equivalent bonds of the §1.2 form — consistent with the axial/equatorial inequivalence observed at five-coordinate centers (PF$_5$), though the trigonal-bipyramidal geometry itself is not derived here. 🔶

🔵 Numerical verification: `files/idwt.py` STEP 43 (explicit octahedral Gram matrix orthonormal to machine precision; orthogonality roots; equiangular Gram rank).

---

## §2. Program

The directions this Part is intended to develop, all currently open:

- **Helium and multi-electron atoms. 🔶** Electron–electron repulsion is the $U(1)$ self-coupling of $\Psi_\infty$ on the shared $d=2$ coordinates of two $d=6$ resonances (Part 8 §14.4). A first variational bound on the helium ground state is in §3. Electron correlation involves the full 6D structure: two electrons in the same $\mathbb{CP}^3$ sector correlate through the sector coordinates as well as the $d=3$ projection, and the product-form deficit of §3 measures what that correlation must supply.
- **Shell filling and the Madelung order. 🔵** The $2(2L+1)$ shell counts are established (Part 8 §14.3). The energy ordering of shells in multi-electron atoms (why 4s fills before 3d) is the Madelung $n+l$ rule: fill the shell with the smallest $n+l$ first, breaking ties by $n$. In IDWT, this ordering is a statement about how the screened central-nucleus potential ranks the $\mathbb{CP}^3$ orbit states: high-L states are excluded from the nucleus by the angular-momentum barrier and see a more screened $Z_{\rm eff}$, while low-n states with the same n+l penetrate more and sit deeper in the well. The screening is computed from Slater's rules, which approximate the full inner-electron screening integral of the Part 8 §14.2 Hamiltonian: $Z_{\rm eff}(n,l) = Z - \sigma(n,l)$ with shielding constants fixed by shell structure alone. The resulting orbital energies $E(n,l) = -Z_{\rm eff}^2/(2n^2)$ verify the Madelung sequence at each noble-gas-to-d-block transition: for K (Z=19) and Ca (Z=20) the Slater $Z_{\rm eff}$ gives $E_{4s} < E_{3d}$, so 4s fills first; from Sc (Z=21) onward the $3d$ $Z_{\rm eff}$ grows faster and 3d sits lower, consistent with d-block filling. The pattern repeats at each period boundary. (`files/idwt.py` STEP 51.) The Slater d/f rule — that d and f electrons see all inner shells at weight 1.00 — is derived from the $d=3$ marginal density (Marginal Exactness, §6.1). The $l\geq2$ centrifugal barrier forces the radial density $\rho_{nl}(r) \propto r^{2l} \to 0$ near the nucleus, so d/f electrons sit outside all filled inner shells and receive full screening: the penetration integral $s({\rm inner}\to{\rm d/f}) \approx 1.000$ for every inner shell regardless of its $Z_{\rm eff}$, while $s({\rm inner}\to{\rm s/p}) < 1$ due to inner-shell penetration. This derives the shape of the Slater σ table from the $d=3$ mode functions with no empirical input; the quantitative ordering is verified in STEP 51. (`files/idwt.py` STEP 101. 🔶) The IDWT-specific content is the $\mathbb{CP}^3$-hidden states (Part 8 §14.3, Lemma 2): four hidden d-states per d-shell, four per f-shell, all inaccessible to $d=3$ probes, following the same Pauli counting and the same energy ordering. Their presence does not change the Madelung sequence or the standard shell structure but changes the interpretation: the ten states of each d-block shell divide into five observable ($2L+1 = 5$ for $L=2$, doubly occupied) and four permanently dark, the four $\mathbb{CP}^3$-hidden d-states of that shell.
- **Crystal field structure.** Two layers of the problem have different status. The $\mathrm{SO}(3) \to O_h$ branching of the $L=2$ d-orbital irrep, and the ratio $\Delta_{\rm tet}/\Delta_{\rm oct} = 4/9$, are ✅ structural consequences: the branching $d(L=2) \to E_g \oplus T_{2g}$ under $O_h$ follows from the SO(3) character formula and the $O_h$ character table (`files/idwt.py` STEP 68); the ratio follows from the angular geometry of the ligand positions, computing the $Y_{40}$ (and $Y_{44}+Y_{4,-4}$) sum over the 6 $O_h$ face-centre ligands (sum = 28) versus the 4 $T_d$ cube-vertex ligands (sum = $-112/9$), giving $\Delta_{\rm tet}/\Delta_{\rm oct} = -4/9$ exactly, confirmed independently by both angular terms. Both results enter via Marginal Exactness (§6.1): the d-electrons are governed by their $d=3$ marginal, and the crystal field potential is a 3D structure. The absolute magnitudes $\Delta_o$ and $\Delta_t$ require the radial integral $\langle r^4\rangle$ over the d-orbital wave function and the ligand-to-metal distance. By Marginal Exactness (§6.1), the d-orbital radial function is the standard STO-3d form $R(r) \propto r^2 e^{-\zeta r}$; the integral evaluates analytically to $\langle r^4\rangle = 315\,a_0^4/\zeta^4$, with $\zeta$ the Clementi–Raimondi (1963) exponent for each transition metal. The point-charge formula is then $\Delta_o = 5Z\langle r^4\rangle/(3R_L^5)$ in atomic units. For first-row TM aqua complexes ($R_L \approx 2.0\ \text{Å}$, $|Z|=1$), this gives $\Delta_o \approx 0.6$–$1.7$ eV across the series (Ti to Cu), compared with observed values of 1–3 eV; the point-charge model underestimates by ~30–50%, as expected. (`files/idwt.py` STEP 68.) Both $R_L$ and the effective ligand charge are external inputs — not derived from IDWT — so the absolute magnitudes carry the status 🔶. The IDWT-specific content is the $\mathbb{CP}^3$-hidden states (four per d-shell, Part 8 §14.3, Lemma 2): four additional inaccessible states at every d-block shell whose presence does not alter the observable $e_g/t_{2g}$ splitting but is falsifiable in principle.
- **Dispersion forces. ❓** A candidate reformulation of London dispersion as overlap of the two atoms' $d=6$ mode structures on their shared $d=2$ coordinates, with polarisability as the susceptibility of the 6D orbit to deformation along the $d=2$ directions.

---

## §3. Helium: a First Variational Bound 🔶

### 3.1 The Hamiltonian

The $d=3$ marginal Hamiltonian for two electrons at a Z=2 nucleus is established in Part 8 §16.1:

$$H = \sum_{i=1,2}\!\left[-\frac{\nabla_i^2}{2m_e} - \frac{Z\alpha}{r_i}\right] + \frac{\alpha}{r_{12}}.$$

The single-electron part is exact (Part 8 §14.2, Lemma 1); the repulsion term is the same Coulomb vertex — the $U(1)$ self-coupling of $\Psi_\infty$ on the $d=2$ coordinates the two $d=6$ resonances share — with no new coupling introduced (Part 8 §16.1). What remains open is the two-electron problem in the full 6D coordinates: how the two resonances correlate through the $\mathbb{CP}^3$ sector directions, beyond what the $d=3$ marginal resolves.

### 3.2 The bound

With a product trial state of screened scale η (each electron in a hydrogenic ground state of charge η), the energy functional is $E(\eta) = [\eta^2 - 2Z\eta + (5/8)\eta]\,\alpha^2 m_e$; the stationary point is $\eta = Z - 5/16 = 27/16$ and

$$E_{\rm He} = -\eta^2\,\alpha^2 m_e = -2.84766~\text{hartree} \qquad (\text{hartree} \equiv \alpha^2 m_e).$$

The screening value 5/16 is the output of the repulsion integral, not an empirical input. The measured value (the sum of the two ionisation energies) is −2.90339 hartree; the bound lies 1.9% above it, as a variational bound must. This sharpens the first-order perturbative estimate of Part 8 §16.3 (−2.75 hartree, 5.3% above) using the same Hamiltonian. 🔵 (`files/idwt.py` STEP 44.)

The comparison is made in hartree units, where α and m_e cancel: the IDWT-derived α(0) carries a known −2.87% residual traced to the $\sin^2\theta_W$ structural gap (Part 3 §0.7), which would dominate an absolute-eV comparison, while the dimensionless $-\eta^2$ is the content specific to this section.

### 3.3 What the deficit is

The trial state is an uncorrelated product in the $d=3$ marginal. The 1.9% deficit is the energy the two-electron correlation must supply. Under the established potentials this correlation is fixed by the $d=3$ marginal problem — the repulsion $\alpha/r_{12}$ is supported on the observable coordinates, so the marginal exactness theorem (§6.1) applies and the exact answer is the standard correlated one. The open 6D question is therefore not whether correlation differs under the established potentials (it cannot), but whether the cross-sector kernel contact terms leave any residue at chemical scales (§6.1 scope condition). No claim is made here beyond the bound.

---

## §4. Deriving the Premises of §1

The angle theorem of §1.2 rests on premises P1–P3. This section derives them from the Part 8 structure, in decreasing order of completeness. (`files/idwt.py` STEP 45 verifies the computational content.)

### 4.1 Orthogonality is a property of fermionic occupancy ✅

The n bonding electrons at a center form an antisymmetric n-electron state — exchange antisymmetry is established from the spinor anticommutation of $\Psi_\infty$ (Part 8 §16.2). An antisymmetrised product of single-particle states $|h_1\rangle, \ldots, |h_n\rangle$ has a basis-change property: replacing the $|h_i\rangle$ by any other basis of the same span multiplies the state by the determinant of the basis change — a scalar. The physical $n$-electron state therefore depends only on the occupied *subspace* of $V$, not on which basis describes it. Any set of directed states spanning that subspace may be taken orthonormal without changing the physical state.

P2 is thus not an assumption about dynamics; it is a statement of which descriptions are physically equivalent. The content of the angle theorem shifts accordingly: orthogonality is free, and the physics lies in P1 (the subspace admits a basis of bond-directed zonal states) and P3 (with equal s-shares). ✅

### 4.2 The directed zonal form from axial symmetry ✅ (degenerate-shell idealization)

Consider one bond: the electron at center A, with a companion nucleus B at distance $R$ along the unit direction $\mathbf{n}$. The potential of B is a $d=3$ structure (Part 1 §3i) and enters the electron's $d=3$ marginal exactly as the Part 8 Hamiltonian does — the Lemma 1 separation applies per electron, so the analysis lives in the established $d=3$ effective problem.

The potential of B is axially symmetric about $\mathbf{n}$. Decompose the degenerate $L \leq 1$ shell by angular momentum about the $\mathbf{n}$ axis: $|s\rangle$ and $|p_n\rangle$ carry $m = 0$; the two transverse p states carry $m = \pm 1$ and vanish on the axis. The leading multipole of B's potential across the shell is the dipole term, and its matrix elements respect the axial symmetry: it couples $|s\rangle \leftrightarrow |p_n\rangle$ and nothing else. On the hydrogenic $n_H = 2$ shell the only non-zero element is $\langle 2s|z|2p_0\rangle = -3a_0$ (radial quadrature, STEP 45); the perturbation eigenstates are $(|s\rangle \pm |p_n\rangle)/\sqrt{2}$ with the bound combination directed toward B, while the $m = \pm 1$ states are unshifted at this order.

The bound state of the block is therefore a zonal hybrid directed along the internuclear axis — the form P1 assumes. Within the degenerate-shell idealization this is derived, not chosen. ✅ The stated refinement: in a multi-electron center the s and p levels of the same shell are split by inner-electron screening, so the mixing at finite bonding strength is partial rather than maximal; the bonding regime is the one in which the off-diagonal coupling dominates that splitting. Quantifying the crossover (the promotion-energy threshold of bond formation) is an open calculation. 🔶

### 4.3 Equal shares from ligand symmetry ✅ (given identical ligands)

Let the n ligands be identical nuclei whose arrangement is invariant under a symmetry group G acting transitively on the bond axes, and let the occupied bonding subspace be G-invariant (the non-degenerate ground configuration). Then G permutes the bond-directed hybrid states of §4.2 among themselves while fixing $|s\rangle$ (the $L = 0$ state is isotropic), so all $n$ s-shares are equal. ⭐ as linear algebra; the physical input is that n identical ligands bind in a symmetric arrangement, which is the energetics statement that remains open (§4.5).

### 4.4 The completeness loop ⭐

The §1.2 proof needs $\sum_i a_i^2 = 1$ — the occupied bonding subspace must contain $|s\rangle$ entirely. This closes by counting. The perturbations of §4.2 couple $|s\rangle$ only to p components along the bond directions. If the $n$ bond directions span a $(n-1)$-dimensional subspace of the three observable directions, the $n$ bonding states lie in $\mathrm{span}\{|s\rangle, p \text{ along that span}\}$ — $n$ states in a space of $n$ states — so the bonding subspace *is* that span, and it contains $|s\rangle$. Completeness applies, the shares are $1/n$, and the angle theorem delivers $\cos\theta = -1/(n-1)$.

The loop then closes on itself: the derived angles realize exactly the direction-span assumed. $n = 2$ gives 180° — collinear, a 1-dimensional direction span; $n = 3$ gives 120° — coplanar, 2-dimensional; $n = 4$ gives 109.47° — fully 3-dimensional. Each case is self-consistent, and the impossible cases exclude themselves: three collinear bonds would require three orthonormal states in a span of two states. A center whose bond directions span fewer dimensions than $n-1$ cannot bind $n$ equivalent ligands through $L \leq 1$ states at all.

Centers with lone pairs sit outside the loop deliberately: there the full four-state space is occupied (bonds plus lone pairs), completeness holds over all four states, and the share asymmetry δ of §1.4 — not yet derived — sets the geometry.

### 4.5 What remains open after §4

- The energetics: that n identical ligands adopt the symmetric arrangement (the input of §4.3), and the nuclear positions themselves, follow from minimising the total energy over the Born–Oppenheimer surface (Part 8 §17). Not yet computed for any polyatomic case.
- The promotion-energy crossover of §4.2 (degenerate-shell idealization vs the real s–p splitting of carbon, nitrogen, oxygen): worked out in §4.6.
- The lone-pair share asymmetry δ (§1.4): the variational framework is in §4.7.
- The full 6D character of the two-center orbit (Part 8 §17.6).

### 4.6 Promotion-energy crossover 🔶

The §4.2 derivation establishes the directed zonal form of each bonding orbit state in the degenerate-shell idealization. A real multi-electron center (carbon, nitrogen, oxygen) has its $ns$ orbital lower than the $np$ orbital by $\Delta E_{\rm sp}$ (the screened s–p gap). Hybridisation is energetically favourable only when the bond energy gained from forming directed bonds exceeds the promotion cost.

For $n_b$ bonds at the center, each lowering the total energy by $U_b$ from the directed overlap (the two-center bonding energy of Part 8 §17), the crossing condition is:

$$n_b \times U_b > \Delta E_{\rm prom}$$

where $\Delta E_{\rm prom}$ is the energy cost of redistributing one electron from the ground-configuration $s^2$ into the hybridised ${\rm sp}^k$ configuration. For carbon ($2s^22p^2\to2s^12p^3$): $\Delta E_{\rm prom} \approx 4$ eV (the 2s–2p gap reduced by the exchange stabilisation of the half-filled 2p shell); four C–H bonds at ≈4.3 eV each provide 17.2 eV $\gg \Delta E_{\rm prom}$ — hybridisation is strongly favoured. For noble gases, no empty orbit state is available and the effective promotion cost is unlimited; hybridisation does not occur. The crossing places nitrogen and oxygen in the intermediate regime where partial hybridisation is expected, consistent with the angles between 90° and 109.47° observed for NH$_3$ and H$_2$O.

IDWT-specific: $U_b$ is the bonding energy from the two-center orbit integral of Part 8 §17.6. Computing $U_b$ for each center-ligand pair is the open calculation that sets the threshold quantitatively; the crossing itself and its qualitative ordering follow from the known ranges of ΔE_prom and bond energies without requiring U_b explicitly. 🔶

### 4.7 The s-share asymmetry δ: variational framework 🔶

The s-share asymmetry δ of §1.4 parameterises the sp$^3$-family hybrid orbit states on the heavy atom (O for H$_2$O, N for NH$_3$). With $n_b$ bond states and $n_{\rm lp}$ lone-pair states:

$$a_b^2 = \tfrac{1}{4} - \delta, \qquad a_{\rm lp}^2 = \tfrac{1}{4} + \tfrac{n_b}{n_{\rm lp}}\,\delta$$

Completeness ($\sum_i a_i^2 = 1$) is preserved for all δ. The bond angle follows from hybridisation orthogonality: $\cos\theta_{bb} = -a_b^2/(1-a_b^2)$.

**Energy decomposition.** The total energy $E(\delta)$ has two classes of contribution:

*One-centre terms* — Slater–Condon Coulomb integrals $J(h_i, h_j)$ between the hybrid orbit states, the total kinetic energy, and the O-nucleus attraction. A key structural fact: the completeness condition $\sum_i a_i^2 = 1$ holds for all δ, so the total s-character and hence the total kinetic energy and O-nucleus attraction are both constant in δ. The one-centre Coulomb integrals, computed from Clementi–Raimondi STO exponents (O: $\zeta_{2s}=2.246$, $\zeta_{2p}=2.227$; N: $\zeta_{2s}=\zeta_{2p}=1.917$), vary by less than 0.004 a.u. over the full range $\delta \in [0, \tfrac{1}{4}]$ for both H$_2$O and NH$_3$. They are not the mechanism that sets the equilibrium. (`files/idwt.py` STEP 52.)

*Two-centre terms* — The bond electrons extend toward the H nucleus; their Coulomb and exchange repulsion with other electrons depends on the molecular geometry, not only on the on-O orbital angles. The key geometry-dependent term is the H–H nuclear repulsion:

$$V_{HH}(\delta) = \frac{C(n_b,2)}{2\,R_{MH}\,\sin(\theta_{bb}(\delta)/2)}$$

which increases as the bond angle closes with δ. Computed at the observed δ values: $\partial V_{HH}/\partial\delta|_{\delta_{\rm obs}} \approx 0.22$ a.u./unit (H$_2$O) and 0.63 a.u./unit (NH$_3$). This is the main geometric restoring force. The two-centre orbit integrals ⟨$h_b\,h_{b'}|r_{12}^{-1}|h_b\,h_{b'}$⟩ involving electrons partially localised near the H nuclei are the additional interaction required to set the equilibrium δ; these are two-centre integrals of the Part 8 §16 type. Also computed in STEP 52: the overlap integrals $S(2s, 1s_H) = 0.497$, $S(2p_\sigma, 1s_H) = 0.430$ (O–H) and the nuclear attraction difference $\Delta V_H = \langle 2p_z|r_H^{-1}|2p_z\rangle - \langle 2s|r_H^{-1}|2s\rangle = 0.186$ a.u.

**Qualitative predictions (confirmed).** δ > 0 whenever lone-pair states are present; δ increases monotonically with lone-pair count. Both are consistent with the fitted values $\delta({\rm CH}_4) = 0 < \delta({\rm NH}_3) = 0.016 < \delta({\rm H}_2{\rm O}) = 0.050$. The one-body directing energy and $V_{HH}$ each contribute gradients of order 0.2–0.6 a.u./unit $\delta$ at the equilibrium, with the two-centre integrals providing the balance.

**What remains.** Quantitative prediction of δ without fitting requires minimising E(δ) including the two-centre Coulomb and exchange integrals between bond and lone-pair orbit states, evaluated at the Born–Oppenheimer equilibrium geometry. That computation gives the predicted angles directly. 🔶

---

## §5. Aromatic Ring Current: Closed-Shell Scaling 🔶

Part 8 §17a establishes the benzene π system as one 6D orbit coupling to all six centers, with the 4n+2 closed-shell rule as a structural consequence, and names the ring current as its direct experimental signature. This section adds the leading quantitative scaling, in the rigid-ring model.

⭐ **Within the model.** The angular modes of the ring orbit on a ring of radius R, threaded by applied flux φ, have energies $\varepsilon_m = (m - \varphi/\varphi_0)^2 E_R$ with $E_R = \hbar^2/(2m_e R^2)$; the level current is $I_m = -\partial\varepsilon_m/\partial\varphi$, linear in $(m - \varphi/\varphi_0)$. For a closed shell — $m = -n \ldots n$, doubly occupied — the m-linear parts cancel in the sum and the field-induced parts add over all 2(2n+1) electrons:

$$I_{\rm induced} \propto 2(2n+1) = N_\pi,$$

the π-electron count, independent of R (the flux $\varphi = B\pi R^2$ cancels the $R^2$ in $E_R$). The top filled level is $m_{\rm max} = n = (N_\pi - 2)/4$. The induced dipole field opposes the applied field inside the loop and reinforces it in the outer plane: inner protons shielded, outer protons deshielded — the observed annulene pattern ([18]annulene: outer 9.28 ppm, inner −2.99 ppm). A half-filled top level (4n electron systems) breaks the cancellation and reverses the response, the antiaromatic paramagnetic current. (`files/idwt.py` STEP 46.)

🔶 **Status.** The scaling I ∝ N_π and the sign geometry are exact within the rigid-ring model; the model itself is the approximation. Real annulenes relax geometrically with size, and the proton shifts depend on position relative to the loop, so the testable consequence — inner-proton shielding of large annulenes growing stepwise with N_π — requires the geometric refinement before it is a sharp number. Open.

### 5.1 NMR shift formula and [18]annulene comparison 🔶

The ring current $I_{\rm ring}(B_0) = -(N_\pi e^2/4\pi m_e) B_0$ [diamagnetic, from the closed-shell level sum above] creates a local magnetic field at each proton via the Biot–Savart law. For a proton at in-plane radius $\rho$ from the ring center (ring radius $R$, applied field $B_0$):

$$\sigma_{\rm ring} = -\Delta B_z/B_0 = B_z(R,\rho)\times\frac{N_\pi e^2}{4\pi m_e}$$

where $B_z(R, \rho)$ is the $\hat{z}$-component of the unit-current field from the loop, computed from the elliptic-integral Biot–Savart formula (Part 1 §3e units; `files/idwt.py` STEP 50). The sign is determined by the loop geometry:

- **$\rho > R$ (outer proton):** $B_z < 0 \to \sigma_{\rm ring} < 0$ → deshielded (downfield). ✓
- **$\rho < R$ (inner proton):** $B_z > 0 \to \sigma_{\rm ring} > 0$ → shielded (upfield). ✓

For [18]annulene (N_π = 18, R = 3.98 Å, outer and inner proton each 1.09 Å from the ring edge), the rigid-ring calculation (STEP 50) gives:

$$\begin{aligned}
\sigma_{\rm outer} &= -44~\text{ppm} \quad (\text{observed: }{-}9.3~\text{ppm, deshielded})\\
\sigma_{\rm inner} &= +115~\text{ppm} \quad (\text{observed: }{+}3.0~\text{ppm, shielded})
\end{aligned}$$

The sign is correct in both cases. The rigid-ring model overestimates the magnitude — by a factor of ~5 for the outer proton and ~40 for the inner proton. The overestimate is a consequence of the thin-wire (1D loop) approximation: the Biot–Savart field diverges as $1/d$ near the loop wire, and both protons sit only ~1.09 Å from the ring.

Two geometric corrections have been computed (STEP 54). Replacing the thin-wire current with a spatially distributed Slater $2p_z$ orbital density (Clementi–Raimondi exponent ζ = 1.625 a.u. for sp$^2$ carbon, with the $z^2$ angular factor that places zero density in the ring plane) reduces the outer field by 33% and the inner field by 21%, giving −29.8 ppm (outer) and +90.8 ppm (inner). Adding the London correction — $\cos(\pi/N) = \cos(\pi/18) = 0.985$ for the discrete hexagonal geometry — reduces each by a further 1.5%, giving −29.3 ppm and +89.4 ppm respectively. These two corrections account for ~35% of the thin-wire values and narrow the discrepancy only modestly.

| | outer proton | inner proton |
|---|---|---|
| thin-wire | $-44.4$ ppm | $+114.7$ ppm |
| $p_z$ + London | $-29.3$ ppm | $+89.4$ ppm |
| observed | $-9.28$ ppm | $+2.99$ ppm |
| residual | $3.2\times$ | $30\times$ |

The remaining factors — 3.2× (outer) and 30× (inner) — require the full discrete-atom GIAO (gauge-including atomic orbitals) calculation, summing over all 18 individual p_z orbital contributions rather than treating the current as a continuous ring. The inner proton residual is larger because the continuous-ring approximation is least valid there: each inner proton sits closest to its bonded carbon, and the divergence of the thin-wire Biot–Savart kernel is most severe at that distance. The N_π scaling holds across the correction: benzene:annulene susceptibility = 6:18 = 1:3, and the observed outer-shift ratio is approximately 1:2 (benzene outer ~1.7 ppm, [18]annulene outer ~3.8 ppm above sp$^2$ reference), qualitatively consistent. Full GIAO is the open quantitative step. (`files/idwt.py` STEP 50, STEP 54.)

---

## §6. Marginal Exactness: What 6D Chemistry Is

### 6.1 The theorem ✅

✅ **Theorem (marginal exactness of chemistry).** Let a system of bound electrons be governed by potentials that separate per Part 8 Lemma 1 — nuclear Coulomb terms supported on the observable coordinates **r**, sector confinement supported on the $\mathbb{CP}^3$ coordinates ξ — and let O be any observable supported on the observable coordinates. This covers every chemical probe: energies, geometries, spectra, electric and magnetic response, including the electron–photon vertex (Part 8 §15), since the $d=2$ coupling acts on shared observable coordinates. Then for product eigenstates ψ ⊗ χ,

$$\langle\psi\otimes\chi_a|O|\psi'\otimes\chi_b\rangle = \langle\psi|O|\psi'\rangle\,\delta_{ab},$$

so every expectation value and transition amplitude is fixed by the $d=3$ marginal dynamics alone; the sector factor drops out, and $\mathbb{CP}^3$-hidden components contribute nothing (Lemma 2). Since the $d=3$ marginal Hamiltonian is the standard molecular Hamiltonian with IDWT-derived inputs (Part 8 §14.2, §16.1, §17.1), IDWT reproduces standard molecular structure and response theory for every chemistry observable measured by a $d=3$ apparatus — vibrational and isotopic effects included, since nuclear motion is likewise a $d=3$ structure. (`files/idwt.py` STEP 47.)

This is the chemistry-wide form of the Coulomb projection consistency of Part 3 §0.8a: the framework does not disturb tested chemistry. A corollary cuts in the other direction: no chirality, spectroscopy, or kinetics experiment performed with 3D apparatus can deviate from the standard-theory result within the established structure. Proposals of such deviations are not open items — they are excluded.

🔶 **Scope condition.** The theorem covers the established potentials. Whether the cross-sector kernel contact terms contribute any residue at chemical energy scales is the one stated caveat. §6.3 bounds it.

### 6.2 What 6D chemistry consists of

Given §6.1, the content of 6D chemistry is three things, none of which is a deviating lab number:

- **Foundation.** What standard chemistry postulates, IDWT derives: Pauli exclusion from spinor anticommutation (Part 8 §16.2); the 2L+1 degeneracies, shell counts, and selection rules from the $SU(4)$ ⊃ $SU(3)$ ⊃ SO(3) chain and ξ-orthogonality (Part 8 §14.3); the bond mechanism (Part 8 §17); the bond angles from orbit-state orthogonality with the premises derived (§1, §4); the Hückel rule and ring-current scaling (Part 8 §17a, §5). The observed numbers are unchanged; their status changes from axiom to theorem of the sector geometry.
- **Ontology and falsifier.** The $\mathbb{CP}^3$-hidden orbit states exist at every shell L ≥ 1 and are strictly inaccessible to 3D apparatus at any order (Part 8 §14.3, Lemma 2). Standard QM has no counterpart states. Any measured coupling to one falsifies the $d=6$ sector identification — a standing, permanent discriminator.
- **Frontier.** The one place a quantitative residue could appear is the cross-sector kernel contact contribution at chemical scales (§6.1 scope condition); §6.3 bounds it at the $10^{-10}$ level — nil for all chemistry. Independent of observables, the orbit trajectory geometry in the $\mathbb{CP}^3$ coordinates (Part 8 §14.4) remains the structural frontier. 6D chemistry is the foundation and the ontology.

### 6.3 The kernel residue bound 🔶

The scope condition of §6.1 closes in two steps.

✅ **Cancellation lemma.** Any kernel component supported on the sector factor alone shifts every atomic and molecular state by the same amount: by Lemma 1, all chemistry states of an electron share one sector eigenstate, so the component's expectation is state-independent and cancels in every measurable difference — spectra, bond energies, barriers are all energy differences. Only kernel components with observable-coordinate support can leave a residue.

🔶 **Bound on the remainder.** The kernel is a contact structure (the colour coupling is its clearest case, Part 3 §0.6; the contact property and the range below are derived from kernel covariance, Part 4 §3.10.1 covariance note and `files/idwt.py` STEP 59–60), with observable-coordinate range set by the sector length scale: $L_6 = 1.414$ fm (Part 1 §3e). A contact term of range $L$ and depth $V_0$ shifts an s-state by $\Delta E \approx V_0 |\psi(0)|^2 (4\pi/3)L^3$ with $|\psi(0)|^2 = 1/(\pi a_0^3)$, and shifts non-s states only at higher order in $L/a_0$ (their orbit-state density vanishes at contact). The depth premise: the kernel's entire l=0 output in the $d=6$ sector is the sector eigenvalue $m_e$, so a residual contact piece is bounded by the scale it generates, $V_0 \leq m_e$ — a deliberately generous bound. Then

$$\frac{\Delta E}{\alpha^2 m_e} \leq \frac{4}{3}\!\left(\frac{L_6}{a_0}\right)^3\!\times\frac{m_e}{\alpha^2 m_e} = 4.8\times10^{-10}.$$

The kernel residue on any chemistry observable is at most a few parts in $10^{10}$ — the same order as the proton-finite-size correction already catalogued in Part 8 §14.4, three orders below Lamb-scale effects, and far below any chemical measurement. (`files/idwt.py` STEP 48.)

**Consequence.** With the cancellation lemma exact and the remainder bounded at $10^{-10}$, the §6.1 caveat closes: within the established framework, 6D chemistry has no measurable quantitative residue. Its content is the foundation and the ontology of §6.2. The premise that carries the 🔶 is the depth bound $V_0 \leq m_e$; deriving the actual contact amplitude from the kernel normalization would convert the bound into a value, and is the remaining refinement.

### 6.4 Kernel contact amplitude: bounded residue, protected fine structure 🔶 / ✅

The §6.3 bound $V_0 \leq m_e$ is generous by design. Sharpening it requires the angular content of the ($n=13$, $d=6$) electron mode together with the channel structure of the hidden-state self-energy.

**Angular content of the electron mode.** The mode index counts levels from the ground state: $S(1,d) = 1$ is the single level-0 state, so mode $n$ sits at oscillator level $N = n-1$ (the convention of Part 7 §1.2 and the Dirac spectral count of Part 8 Theorem S1). The free $d=6$ mode carries no intrinsic angular momentum: a flat $\mathbb{R}^6$ sector has rotation group $\mathrm{SO}(6) \cong \mathrm{Spin}(6) \cong SU(4)$, and the mode's content is the harmonic tower $H_m = (0,m,0)$ over the occupied levels (`files/idwt.py` STEP 82). The rotation-invariant contact component is the $\mathrm{SO}(6)$ singlet $H_0$, present exactly when $N = n-1$ is even, that is when $n$ is odd. The electron, $n = 13$, is odd, so the contact harmonic is present: the kernel's contact piece has a nonzero matrix element with the electron mode, and the contact amplitude is not removed by parity. The residue stays at the §6.3 value, $\Delta E \leq 4.8\times10^{-10}$ hartree — far below any chemical measurement, so the §6.1 scope condition closes at the bounded level: 6D chemistry carries no measurable quantitative residue. The precise contact value reduces to a bound-state perturbation sum: an SO(3) angular momentum is defined only once the nucleus anchors the observable rotation SO(3)_obs ⊂ SO(6) in the bound problem (`files/idwt.py` STEP 81), where the contact piece couples through the s-channel.

**Angular selection on the higher multipoles (✅).** The l ≠ 0 components of the electron mode do not shift a spherically symmetric (s-type) atomic orbital: $\int |\psi_s(\mathbf{r})|^2 Y_l^m(\theta,\varphi)\,d\Omega = 0$ for l ≠ 0. The even multipoles l = 2, 4, … act only through orbital anisotropy; the l = 0 piece is the one carrying the §6.3-bounded contact shift.

**Fine structure is protected by a selection rule, not only by smallness (✅).** The second-order self-energy of an observable state through the $\mathbb{CP}^3$ hidden states decomposes by which coordinates the kernel touches, and only one of the three channels can affect fine structure. The pure-sector channel (kernel identity on the $d=3$ marginal) has an orbital-independent energy denominator by the Lemma 1 separability, so it produces a shift identical for every orbital — an exact common shift that cancels in every measurable difference by the §6.3 cancellation lemma. The $d=3$-only channel is diagonal in the sector index and has zero observable↔hidden matrix element (Lemma 2), contributing nothing. The mixed observable×sector channel is the only orbital-dependent one; it carries the contact factor $L_6/a_0$ at each of two vertices and is therefore $(L_6/a_0)^2 \approx 7.1\times10^{-10}$, an estimate of order $10^{-19}$ hartree — nine orders below the Lamb shift. Fine structure is protected by the selection rule — the pure-sector self-energy cancels, the $d=3$-only channel cannot reach the hidden states — and not only by the smallness of the contact factor (`files/idwt.py` STEP 77). The relevant SO(3) for this channel is the nucleus-anchored observable rotation SO(3)_obs ⊂ SO(6) ≅ $SU(4)$ of the bound problem (`files/idwt.py` STEP 81) — so the explicit value of the mixed channel reduces to the perturbation sum over its multiplicities.

**The electron's sector content and its chemistry orbitals are different objects.** The electron mode index $n_e = 13$ arises from the seed decomposition $n_e = n_{\nu_1} + n_{\rm up} = 10 + 3 = 13$ (Part 2 §2, §6), placing the mode at level $N = 12$, whose content includes the $\mathrm{SO}(6)$-singlet contact component ($n$ odd); S(13,6) = 18564 sets the $d=6$ mass quantum $m_{\rm scale,6} = m_e/18564$. The periodic-table orbitals (s, p, d, f) are bound states of the $d=3$ marginal Coulomb problem (Marginal Exactness, §6.1), not the harmonic content of this single sector mode; the two are not to be identified.
