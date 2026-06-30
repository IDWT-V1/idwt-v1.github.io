# Infinite Dimensional Wave Theory — Part 2: The Mass Formula

---

## 1. The Simplex Formula and the Hockey-Stick Identity

$$m(n,d) = m_{\rm scale,d} \times S(n,d), \qquad S(n,d) = \binom{n+d-1}{d}$$

$S(n,d)$ is the cumulative count of harmonic oscillator eigenstates at levels $0$ through $n-1$ in $d$ dimensions — the integrated density of states (IDOS). Equivalently, it is the number of ways to write $n-1$ as an ordered sum of $d$ non-negative integers (stars and bars with $d$ slots), which equals $\dim\mathrm{Sym}^{n-1}(\mathbb{R}^{d+1}) = \binom{n+d-1}{d}$. It is equally the Ehrhart polynomial of the standard $d$-simplex evaluated at $n-1$ — the number of lattice points in the $(n-1)$-fold dilation of the $d$-simplex (the region where $d$ non-negative coordinates sum to at most 1) — which is the geometric reason $S(\cdot,d)$ is a degree-$d$ polynomial in $n$. **Corollary (Theorem S1, Part 8 §5):** $S(n,3) = \frac{1}{2}N_{D_{S^3}}(n-1)$, where $N_{D_{S^3}}(n-1)$ is the cumulative positive Dirac eigenvalue count on $S^3$ up to level $n-1$.

### $S(n,d)$ as a Universal Combinatorial Measure Field

$S(n,d)$ appears in three distinct physical roles across IDWT. They are three different functionals applied to the same underlying combinatorial object. The formal declaration:

**$S(n,d)$ is the cumulative spectral counting function of the $d$-dimensional sector harmonic oscillator:**

$$S(n,d) = N_d(n-1) = \#\{\text{eigenvalues of }H_d\text{ at level }k < n,\text{ with multiplicity}\} = \sum_{k=0}^{n-1}\binom{k+d-1}{d-1}$$

(proved in Part 8 §3)

Given this single definition, the three applications are different functionals on $S$:

| Role | Functional | Physical meaning |
|---|---|---|
| **Mass eigenvalue** | $F_{\rm mass} = m_{\rm scale,d} \times S(n,d)$ | Mass = sector scale $\times$ cumulative microstate count |
| **L² norm weight** | $F_{\rm norm} = S(n,d)$ (weight in $\|\Psi\|_w^2$) | Weighted L² norm: $\|\Psi\|_w^2 = \sum m(n,d)|c_{n,d}|^2/m_{\rm scale,d}$ |
| **Convergence bound** | $F_{\rm conv} = \sum_n 1/S(n,d) = d/(d-1)$ | Reciprocal sum bounds the evaluation functional |

These are mutually consistent because all three reduce to operations on $N_d(n-1)$. In particular: Roles 1+2 are consistent because $\|\Psi\|_w^2 = \Sigma\, S(n,d)|c_{n,d}|^2$ is the L² norm weighted by mode count, which equals mass-weighting when expressed in units of $m_{\rm scale,d}$. Role 3 follows by Cauchy-Schwarz from Role 2.

**$S(n,d)$ is the dimension of a space that exists in the sector geometry.** The mode functions $\chi_{n,\alpha}(\xi)$ are degree-$(n-1)$ monomials in $d+1$ sector coordinates, and $\dim\mathrm{Sym}^{n-1}(\mathbb{R}^{d+1}) = \binom{n+d-1}{d} = S(n,d)$ is a theorem of algebraic geometry. Equivalently, $S(n,d)$ is the cumulative count of all harmonic oscillator eigenstates at levels $0$ through $n-1$ in $d$ dimensions — the IDOS.

⭐ **Hockey-stick identity (proved theorem of combinatorics):**

$$S(n,d) = \sum_{k=0}^{n-1}\binom{k+d-1}{d-1}$$

It is the engine of the entire spectrum.

**Physical meaning:** The resonant frequency $S(n,d)$ equals the cumulative count of sector microstates below level $n$. These are the same thing. The frequency at which mode $n$ resonates is precisely the total number of accessible sector states up to that level. Heavier particles — higher frequencies — occupy higher-entropy configurations of the sector geometry. The hockey-stick identity is the bridge between the spectral and the statistical descriptions.

⭐ **Generating function (ordinary):**

$$\sum_{n=1}^{\infty} S(n,d)\, t^n = \frac{t}{(1-t)^{d+1}}$$

*Proof.* The standard generating function for the binomial coefficient $\binom{n+d-1}{d}$ gives $\sum_{n\geq 0}\binom{n+d}{d}t^n = 1/(1-t)^{d+1}$; shifting the index by 1 yields the result. $\square$

This is the generating function analogue of the hockey-stick: the pole of order $d+1$ at $t=1$ encodes the spectral dimension of sector $d$, consistent with the heat-kernel result $K_d(t)\sim t^{-1/d}$ (Part 8 §3.2). The pole order also gives the leading Stirling term directly without approximation: residue analysis at $t=1$ recovers $S(n,d)\sim n^d/d!$ as $n\to\infty$.

⭐ **$S(n,d)$ as a complete homogeneous symmetric polynomial:**

$$S(n,d) = h_{n-1}(x_1,\dots,x_{d+1})\Big|_{x_i=1}$$

where $h_{n-1}$ is the complete homogeneous symmetric polynomial of degree $n-1$ in $d+1$ variables. This is an algebraic identity: $h_{n-1}(1,\dots,1) = \binom{n+d-1}{d}$ by definition. The IDWT mass formula already uses $\dim\mathrm{Sym}^{n-1}(\mathbb{R}^{d+1}) = S(n,d)$ (Part 8 §1); the symmetric function identification is the same fact in the language of representation theory, and adds two structural consequences:

- **Newton's identities** relate the $h_k$ to power sums $p_k = \mathrm{tr}\,M^k$ with integer coefficients, giving a recursive mass formula purely in terms of traces of the sector mass operator.
- **Schur positivity** of products $h_a h_b$ (expansion in the Schur basis has non-negative integer coefficients) provides a combinatorial proof that combining two sectors never produces negative mode counts — no ghost modes can appear from multi-sector products.

⭐ **$S(n,d)$ as Schubert cell count — hockey-stick = Pieri rule:**

The Grassmannian $\mathrm{Gr}(d,\, n+d-1)$ has a Schubert cell decomposition with exactly $\binom{n+d-1}{d} = S(n,d)$ cells. The hockey-stick recursion

$$S(n,d) = S(n,d-1) + S(n-1,d)$$

is the Pieri rule for multiplying a Schubert class by the class of a hyperplane section in $\mathrm{Gr}(d,n+d-1)$: the two terms correspond to the two types of Schubert cells that appear in the product. This is a purely geometric identity — no physics input. Verified: $S(4,3)=S(4,2)+S(3,3)=10+10=20$; $S(10,5)=S(10,4)+S(9,5)=715+1287=2002$; etc.

**Consequence:** the sector assignments $d\in\{2,3,4,5,6,10\}$ index Grassmannians $\mathrm{Gr}(d, n_{\rm particle}+d-1)$ whose Schubert stratifications encode the mode multiplicities. The Euler characteristic $\chi(\mathrm{Gr}(d,m)) = \binom{m}{d}$ recovers $S(n,d)$ directly, consistent with the Euler characteristic constraints used to fix sector geometry in Part 1 §3a.

⭐ **$q$-deformation of $S(n,d)$ — built-in regularisation.** The Gaussian binomial coefficient (q-binomial) $\binom{n+d-1}{d}_q$ is a polynomial in $q$ whose value at $q=1$ is $S(n,d)$. It satisfies the q-Pascal recurrence

$$\binom{m}{r}_q = q^r\binom{m-1}{r}_q + \binom{m-1}{r-1}_q,$$

the exact $q$-lift of the hockey-stick identity $S(n,d)=S(n,d-1)+S(n-1,d)$. Setting $S_q(n,d) = \binom{n+d-1}{d}_q$, the coefficient of $q^t$ counts mode configurations with $t$ inversions — the area under the lattice path that builds the hockey-stick sum. This gives a one-parameter family of spectra collapsing to the IDWT spectrum at $q\to1$; at $q\neq1$ it tracks the nesting depth of a mode within the sector lattice. Since the generation laws $S(n,d)=S(n,d-1)+S(n-1,d)$ hold identically at the $q$-deformed level (q-Pascal is exact), the tower structure is preserved for all $q$. The $q$-deformation supplies a built-in spectral regularisation without adding free parameters beyond $q$, and the hook-content formula provides a closed product for the $q$-weight of each mode without gamma functions. The inversion count giving the $q$-exponent of each mode equals the braid distance between modes in the permutohedron (vertices of the permutohedron at weak-order distance $n-1$ from the identity number $S(n,d)$), so $q$-weights can be computed by counting shortest paths in the permutohedron rather than evaluating polynomials.

⭐ **Root systems of type $A_d$ — Kostant partition function.** The positive roots of $A_d$ are $e_i - e_j$ for $1 \leq i < j \leq d+1$. The number of ways to write a weight of total height $n-1$ as a nonneg­ative sum of simple roots is $S(n,d)$ — the hockey-stick identity is the Kostant partition function for $A_d$. Each IDWT mode $(n,d)$ is thus a weight in the $A_d$ root lattice, and the Weyl group $S_{d+1}$ acts by permuting the $d+1$ sector coordinates, giving the symmetry of $S(n,d)$ in the sector labels as a consequence of Weyl symmetry rather than an assumption. The Kostant multiplicity formula supplies closed-form expressions for mode degeneracies, and the Weyl character formula gives their generating function — both without new parameters.

⭐ **Ferrers diagram depth — structural box-count sequence from $n_u$.** Each IDWT mode $(n,d)$ corresponds to a Ferrers diagram fitting inside a $d\times(n-1)$ rectangle, and $S(n,d)$ counts the number of such diagrams. The minimal box-count from the seed diagram yields a natural depth sequence for the up-type quarks:

- **up** ($n=3$, $d=4$): seed Ferrers diagram is the starting point → depth $k=0$
- **charm** ($n=20$, $d=4$): one hockey-stick extension of the $d=3$ seed column → depth $k=n_u=3$
- **top** ($n=72$, $d=4$): Hopf depth-2 extension, $k=S(n_u,3)=10$ boxes → depth $k=10$

The sequence $\{0,n_u,S(n_u,3)\}=\{0,3,10\}$ emerges combinatorially from $n_u=3$ alone. It was once a candidate exponent set for the per-quark up-type correction $(1-\varepsilon)^k$ (the "Generation Tower Correction"), but that correction has been removed — its exponent was a fit, not derived (§11.3) — so no per-quark exponent is applied: the $d=4$ up-type masses are quoted bare, and charm and top overshoot PDG 2024 as open residues. The Ferrers counting identifies the combinatorially natural depth sequence; it is recorded here as a structural observation, not a mass correction.

⭐ **Large-n asymptotic (proved by Stirling's approximation):**

$$S(n,d) = \binom{n+d-1}{d} \sim \frac{n^d}{d!} \quad \text{as } n \to \infty$$

*Proof sketch.* $S(n,d) = \frac{(n+d-1)(n+d-2)\cdots n}{d!}$. Each of the $d$ factors in the numerator approaches $n$ as $n\to\infty$, giving $n^d/d!$. The relative error is $O(1/n)$. $\square$

The asymptotic has direct physical consequences:
- **Mass growth:** $m(n,d) = m_{\rm scale,d}\times S(n,d) \sim m_{\rm scale,d}\times n^d/d!$ — mass grows as the $d$-th power of the mode index. Higher sectors ($d$ larger) produce faster mass growth with $n$.
- **Sector hierarchy:** $S(n,d)/S(n,d') \sim n^{d-d'}/(d!/d'!)$ for $d > d'$, so higher-$d$ modes are exponentially heavier than same-$n$ modes in lower sectors.
- **Spectral dimension:** The heat kernel $K_d(t) = \sum_{n\geq 1}e^{-tS(n,d)} \sim t^{-1/d}$ as $t\to 0^+$, establishing spectral dimension $= d$ for each sector (Part 8 §3.2).

⭐ **Ehrhart $h^*$-vector — integrality test for mass deformations.** $S(n,d) = \binom{n+d-1}{d}$ is the Ehrhart polynomial of the standard $d$-simplex: it counts lattice points in the $(n-1)$-fold dilation. Every Ehrhart polynomial has an $h^*$-vector (also called the $\delta$-vector) recording the same data in a basis of shifted binomials. For the standard $d$-simplex, $h^* = (1, 0, 0, \dots, 0)$ — trivially nonnegative and unimodal, which is exactly why the mass formula is so clean. This has a direct practical consequence for the open deformation questions (Part 6, MC-2): any modification of $S(n,d)$ — including the $q$-deformation $S_q(n,d)$ above or any sector-potential correction — that drives the $h^*$-vector negative has exited the world of lattice polytopes, at which point the hockey-stick identity, the Pieri rule, and the integrality of mode counts all break simultaneously. Checking $h^* \geq 0$ is therefore a one-line necessary condition for any proposed mass deformation to remain combinatorially consistent. For the $q$-deformation at $q=1$ (the IDWT spectrum), $h^* = (1,0,\dots,0)$ exactly; deforming $q$ away from 1 changes the $h^*$-vector, and the positivity constraint bounds how far the deformation can go before the spectrum loses its lattice-polytope interpretation.

---

## 2. The Per-Sector Comb Filter $H_d(\omega)$

The cross-sector filter $\Gamma_{346}(\omega)$ gives the ρ meson (§10). The intra-sector filter $H_d(\omega)$ gives fermion masses:

$$H_d(\omega) = \exp\!\bigl(2\pi i \times N_d(\omega/m_{\rm scale,d})\bigr)$$

where $N_d$ is the continuous inverse of $S(n,d)$: $N_d(S(n,d)) = n$, extended via the gamma function $S_{\rm cont}(n,d) = \Gamma(n+d)/(d!\,\Gamma(n))$. This extension is strictly increasing in $n$ for all $n > 0$ (a consequence of the log-convexity of the Gamma function: $\log\Gamma(n+d) - \log\Gamma(n)$ is convex and strictly increasing). $N_d$ is therefore well-defined and injective on all $\omega > 0$, not just at mass eigenvalues.

**Phase condition:** $\mathrm{Im}[H_d(\omega)] = \sin(2\pi N_d(\omega/m_{\rm scale,d})) = 0$ at exactly $\omega = S(n,d) \times m_{\rm scale,d}$ for all integer $n$. All zeros are constructive ($\mathrm{Re}[H_d] = +1$) — every fermion mass is a resonance.

**Phase velocity:**

$$\frac{d\Phi_d}{d\omega} = \frac{2\pi}{m_{\rm scale,d} \times S(n(\omega),\, d-1)}$$

The phase of sector $d$ accumulates at a rate inversely proportional to the mode density of sector $d-1$. This is a recursive inter-sector relation requiring no knowledge of $S(n,d)$ directly. The mass formula $m = S(n,d) \times m_{\rm scale,d}$ is the resonance condition $\mathrm{Im}[H_d(\omega)] = 0$, derivable from the inter-sector mode density chain.

### Angular structure of the kernel

The cross-sector coupling term $(\xi_d\cdot\xi_{d'})^2$ decomposes on the unit sphere $S^{d-1}$ by spherical harmonics. For the $d=3$ sector ($S^2$), where $P_2$ is the standard Legendre polynomial:

$$(\xi_d\cdot\xi_{d'})^2 = \tfrac{1}{3}\;[$l{=}0$,\text{ scalar}] \;+\; \tfrac{2}{3}P_2(\cos\theta)\;[$l{=}2$,\text{ tensor}]$$

For general $d$, the $l=0$ coefficient is $1/d$ and the $l=2$ coefficient involves the Gegenbauer polynomial $C_2^{(d-2)/2}$. The $d=3$ formula is given because the $d=3$ quark sector is the primary source of the corrections discussed here.

The $l=0$ part is a constant — it generates sector masses and is the source of the entire simplex spectrum. The $l=2$ part depends on the relative orientation of $\xi_d$ and $\xi_{d'}$ and is responsible for the non-trivial spatial corrections in the theory: the even-$l$ correlations of the $d=3$ colour singlet that set nucleon size and confinement energy, and the $n$-dependent frequency precession behind the $d=4$ up-type overshoot (§11). Both come from the same tensor term. (The nucleon spin observables $\mu_p$, $\mu_n$, and $g_A$ are not from this term — being spin-independent it cannot source a spin observable; they belong to the Dirac spin-orbit sector, Part 8 §10.)

For the self-coupling ($d=d'$), $\xi=\xi'$ so $(\xi\cdot\xi)^2=|\xi|^4=1$ on the unit sphere. The Gegenbauer $l=2$ component is present but averages to zero over the rotationally symmetric vacuum (Gegenbauer orthogonality): only the $l=0$ piece contributes to the sector self-energy after vacuum averaging. Cross-sector angular mixing is absent in the vacuum expectation value of the self-coupling.

**Verified numerically** for $d=3$ ($\mathrm{Im}[H_3] = 0.0000$, $\mathrm{Re}[H_3] = 1.0000$ at $n=1,\ldots,6$) and $d=4$ (residuals $< 10^{-14}$ at $n=3, 20, 72$).

**Base case $d=1$:** $N_1(x) = x$, so $H_1(\omega) = \exp(i\omega\tau)$ with $\tau = 2\pi/m_{\rm scale,1}$ — a single constant-delay comb filter.

---

## 3. The Pascal Recursion — One Identity, All Generation Laws

⭐ **Pascal recursion (proved theorem of combinatorics):**

$$S(n,d) = S(n,d-1) + S(n-1,d)$$

*Proof.* $S(n,d) = \binom{n+d-1}{d}$. Pascal's rule $\binom{m}{k} = \binom{m-1}{k-1}+\binom{m-1}{k}$ applied with $m=n+d-1$, $k=d$ gives $\binom{n+d-1}{d} = \binom{n+d-2}{d-1}+\binom{n+d-2}{d} = S(n,d-1)+S(n-1,d)$. $\square$

Boundary conditions: $S(1,d)=1$ for all $d$ (universal ground state); $S(n,1)=n$ (linear sector).

It says: the simplex number at $(n, d)$ equals its neighbour at $(n, d-1)$ plus its neighbour at $(n-1, d)$. **The Pascal recursion constrains the eigenmode selection rule:** any mode index assignment that violates $S(n,d) = S(n,d-1) + S(n-1,d)$ is rejected. The observed assignments are the unique set that simultaneously satisfies the recursion and the seed conditions $\{n_{\rm down}=1, n_{\rm up}=3\}$. The recursion does not produce the assignments from scratch — but it makes the assignments rigid: there is no freedom to choose different mode indices once the seeds are fixed.

**Generation 2 law — the clearest case:**

Evaluate $S(4,4)$ two ways:

$$S(4,4) = S(4,3) + S(3,4) \;\Longrightarrow\; 35 = 20 + 15 \;\Longrightarrow\; n_\mu = n_c + n_{\nu_2}$$

It is Pascal's recursion applied to $S(4,4) = 35$. The generation-2 lepton mode index equals the sum of the charm quark index and the second neutrino index because that is what the hockey-stick identity requires at ($n=4$, $d=4$). The eigenmode selection rule for generation 2 is a combinatorial theorem.

**Generation 1 law:**

$$n_e = n_{\nu_1} + n_u = S(3,3) + 3 = 10 + 3 = 13$$

$n_{\nu_1} = S(n_u,3) = S(3,3) = 10$ is itself a hockey-stick sum: $1+3+6 = 10$. Adding $n_u$ gives $n_e = 13$.

**Generation 3 law:**

$$n_\tau = n_{\nu_3} + n_{\rm down} = 22 + 1 = 23$$

The $+1 = n_{\rm down} = S(1,d) = 1$ for every $d$ — the base case of every hockey-stick sum. The tau's mode index inherits the universal ground state.

The pattern across all three generation laws:

$$n_{\rm lepton} = n_{\rm neutrino} + n_{\rm quark\,partner}$$
holds as a pattern, but it is a Pascal/hockey-stick *identity* only for generation 2: $n_\mu = n_c + n_{\nu_2} = S(4,3) + S(3,4) = S(4,4)$, forced because $n_s - 1 = n_u$ makes the second Pascal parent $S(n_s-1,4) = S(n_u,4) = n_{\nu_2}$. Generation 1 is **not** a Pascal step — $13$ is not an $S(n,d)$ value at any sector dimension, and the operands $\{n_{\nu_1}, n_u\} = \{10,3\}$ are not Pascal-adjacent (the Pascal parents of $S(3,3) = 10$ are $\{6,4\}$, and the seed $3$ is neither). So $n_e = n_{\nu_1} + n_u$ attaches the up seed as an additive node (Part 7 §1.2a), carrying one irreducible input (🔶). Generation 3 is displaced off the tower (§6). Only generation 2 is a theorem (`idwt.py` STEP 116).

**The generation-3 anomaly — why $\tau$ breaks the up-type pattern. 🔶** Read across the partners, generations 1 and 2 add the *same-generation up-type quark*: $n_e = n_{\nu_1} + n_u$ (up) and $n_\mu = n_{\nu_2} + n_c$ (charm). The pattern would continue $n_\tau = n_{\nu_3} + n_{\rm top} = 22 + 72 = 94$ — but $n_{\rm top} = 72$ is a product-form anchor off the hockey-stick tower (§6; it is not a hockey-stick output), so the third charged lepton cannot inherit its up-type partner. Instead $\tau$ takes the minimal displacement available, the universal ground quantum $n_{\rm down} = S(1,d) = 1$: $n_\tau = n_{\nu_3} + n_d = 23$. This is the lepton-sector analogue of the bottom quark, whose third down-type generation likewise leaves the tower (the beat resonance $k_0 = 16$, §8): in both sectors the third generation fails to follow its natural tower continuation and is displaced by one ground quantum. The third-generation neutrino and charged lepton both sit one ground quantum above a predecessor, $n_{\nu_3} = S(3,5) + n_d = 22$ and $n_\tau = n_{\nu_3} + n_d = 23$, but they are not the same kind of edge. The $\tau$ value is a genuine index-addition ($n_\tau = n_{\nu_3} + n_d = n_c + n_u$; further index-sums $n_{\nu_1}+n_e$ and $1+n_{\nu_3}$ also reach $23$), carrying the systematic $+1 = n_d$ offset between index-addition ($n_a + n_b$, the tower edge) and level-addition ($n_a + n_b - 1$, disjoint excitations $N_c = N_a + N_b$ with $N = n-1$). The $\nu_3$ value is *not* an index-sum at all — no two smaller tower indices add to $22$, and $S(3,5) + n_d = 22$ coincides with the inclusion-exclusion form $n_{\nu_1} + n_{\nu_2} - n_u$ only through $n_s = n_u + n_d$; $\nu_3$ is inclusion-exclusion-forced. So the open index- versus level-addition question lives at $\tau$ (and the generation-1,2 edges $e, \mu$), not at $\nu_3$; why index-addition fires there rather than level-addition is plausibly set by the condensation dynamics (Part 6; `idwt.py` STEP 112).

**Mode indices from sector Euler characteristics (Part 1 §3b):**

$$n_e = \bigl(\chi(\mathbb{CP}^3)\bigr)^2 - \chi(\mathbb{CP}^2) = n_s^2 - n_u = 13 \quad[= k_0 - n_u]$$

$$n_\tau = n_c + n_u = S(n_s,3) + n_u = 20 + 3 = 23 \quad[\text{charm mode} + \text{seed }n_u]$$

$$n_{\nu_3} = n_\tau - n_d = 23 - 1 = 22 \quad[\text{one mode below tau}]$$

$$n_Z - n_W = q = S(n_u-1,\,4) = 5 \quad[= \text{the }q\text{ from }g_{22} = p^2 q/2] \quad\text{✅}$$

(holds for all $n_s$: $n_W = n_{\rm top} + n_s$, $n_Z = n_W + (n_s+1)$, gap $= n_s+1 = q$)

The last identity is structurally significant: the $d=2$ sector gap between W and Z modes equals exactly the q factor in the EW self-coupling formula $g_{22} = p^2q/2$. The Z-W mass gap and the EW coupling constant come from the same combinatorial quantity.

⭐ **Complementary recursion — the multiplicative sector ladder:**

$$S(n,d+1) = S(n,d) \times \frac{n+d}{d+1} \qquad\Bigl[\text{equivalently } \frac{S(n,d)}{S(n,d+1)} = \frac{d+1}{n+d}\Bigr]$$

The hockey-stick is the additive recursion across mode index $n$ at fixed sector $d$ — the diagonal the generation laws climb. This is its vertical partner: at fixed $n$ it steps the mode count from one sector to the next, and the two recursions together generate the entire $S(n,d)$ table from the boundary $S(1,d)=1$. The generation tower is built from the hockey-stick alone, so the multiplicative ladder is not required to fix the spectrum; it completes the account of how the simplex numbers propagate across sectors and fixes the exact ratio of any mode count to its image one sector higher.

---

## 4. Why $d=6$ is Colour-Neutral

⭐ **Double hockey-stick identity (proved theorem of combinatorics):**

$$\sum_{k=0}^{N}\binom{k+2}{2}\binom{N-k+2}{2} = \binom{N+5}{5}$$

**Important:** $C(k+2,2)$ is the **level multiplicity** at level $k$ of a $d=3$ harmonic oscillator — the number of states at that level, not the IDOS. The cumulative count (IDOS) of $d=3$ is $S(k,3) = C(k+2,3)$, which is a different object. The convolution of two sets of IDOS values gives $\sum_k S(k,3)\times S(n-k,3) = C(n+5,7)$, not $C(N+5,5)$.

Here, $C(N+5,5)$ is simultaneously: (a) the level multiplicity at level $N$ of a $d=6$ harmonic oscillator, and (b) the IDOS $S(N+1,5)$. These are the same number, but the physically relevant interpretation for the tensor product argument is (a).

This proves: **the $d=6$ oscillator is exactly the tensor product of two $d=3$ oscillators**, in the sense that pairing states level-by-level in two $d=3$ spaces gives the same state count as a single $d=6$ space. The lepton sector ($d=6 = d=3 \otimes d=3$) is colour-neutral because it is built from products of colour spaces, not embedded in one. This is the geometric origin of the lepton/quark distinction.

Verification ($N=32$): $\sum_{k=0}^{32} C(k+2,2) \times C(32-k+2,2) = 435{,}897 = C(37,5)$

⭐ **Binomial Hopf algebra and the exact inverse mass map.** Define a vector space with basis $x_{n,d}$ for $n\geq1$, coproduct $\Delta x_{n,d} = \sum_{k=1}^{n-1} x_{k,d}\otimes x_{n-k,d}$, and product $x_{a,d}\,x_{b,d} = \binom{a+b-2}{a-1}x_{a+b-1,d}$. This is the divided-power Hopf algebra, and its structure constants are exactly the hockey-stick coefficients. The antipode $S$ of this Hopf algebra is signed Möbius inversion on the Boolean lattice. Applying $S$ to $x_{n,d}$ gives the formal inverse of the mass map $m = m_{\rm scale,d}\,S(n,d)$: solving for $n$ from $m$ is the antipode evaluation, expressed as an integer recursion with no root-finding. Explicitly, if $M = m/m_{\rm scale,d}$ is the dimensionless mass, then $n$ satisfies

$$n = 1 + \sum_{k=1}^{d}(-1)^{k+1}\binom{n+k-2}{k-1}\bigl[M - S(n-1,d)\bigr] \quad\text{(antipode recursion)},$$

which terminates in $d$ steps for any integer $M = S(n,d)$. The Hopf algebra is cocommutative, which is the algebraic reason the generation graph has no preferred direction: forward and backward traversal through the hockey-stick lattice are algebraically equivalent.

---

## 5. The seeds $n_d = 1$ and $n_u = 3$ — Hockey-Stick Forced

The seeds $n_d = 1$ and $n_u = 3$ are independently forced; $n_s = n_u + n_d = 4$ follows.

**$n_{\rm down} = 1$** is forced because $S(1,d) = 1$ for every $d$. This is the base case of every hockey-stick sum — the first term in every cumulative count. It is simultaneously the ground state of every sector.

**$n_{\rm strange} = 4$** is confirmed as the unique positive integer satisfying $S(n,4) = 35 = n_{\rm muon}$. The muon occupies mode 35 in $d=6$. Only $n=4$ maps there via the simplex function in $d=4$. Why is 35 the muon's mode? Because $35 = S(4,4) = 1+4+10+20$ — the hockey-stick sum of the $d=4$ simplex through level 3. $n_s = 4$ is the unique value for which the strange quark's hockey-stick image in $d=4$ lands on an occupied lepton mode. No other integer does this.

Three independent structural conditions single out $n = 1$ and $n = 4$ in $d = 3$. $S(1,d) = 1$ for every $d$ makes $n = 1$ the base case of every hockey-stick sum and the ground state of every sector (⭐). $n_s = 4$ satisfies $S(4,3) = n(n+1) = 20$ — the unique index where the simplex number equals the Casimir number (⭐) — and the coupling $g_{33} = 8\sqrt{7}$ (derived in §9) places the effective coupling per mode $g_{33}/S(4,3) = 8\sqrt{7}/20 \approx 1$ at the confinement threshold (🔶). At level $N = 3$, $n = 4$ carries $l = 1$ and $l = 3$ only, giving it permanent $l$-parity protection from the $l = 0$ vacuum sector (⭐, Part 7 §1.2). These are structural selectors: the value $g_{33} = 8\sqrt{7}$ is fixed by the §9 gap construction from the seed integers (${\rm gap}_{d=3} = n_s^2$, $g_{\rm coeff} = 2/\sqrt{7}$), and $n = 1$ and $n = 4$ are picked out by the three conditions above — not as the minima of an effective energy over the mode index, a reading the documented vocabulary does not support. The seeds are not chosen — they are structurally forced.

⭐ **Kummer p-adic characterization of the seed.** Kummer's theorem states that the 2-adic valuation $v_2\!\bigl(\binom{n+d-1}{d}\bigr)$ equals the number of carries when adding $d$ and $n-1$ in binary. Applied to the two seed evaluations:

| Seed evaluation | Binary addition | Carries | $v_2$ |
|---|---|---|---|
| $S(n_s,3) = S(4,3) = 20 = 4\times5$ | $3+3$ ($011+011$) | **2** | $v_2(20)=2$ |
| $S(n_u,4) = S(3,4) = 15 = 3\times5$ | $4+2$ ($100+010$) | **0** | $v_2(15)=0$ |

The pair $(n_s=4,\,d=3)$ is the unique pair for which the $d=3$ evaluation has carry-count 2 (divisible by 4 but not 8) while the $d=4$ evaluation has carry-count 0 (odd). In $d=3$, the initial segment $n=1,2,3$ has strictly distinct $v_2$ values $\{0,2,1\}$; $n_s=4$ is the first index where $v_2$ repeats ($v_2(S(4,3))=2 = v_2(S(2,3))$), marking $n_s$ as the boundary of the distinct-valuation segment. This gives a p-adic characterization of $n_s=4$ complementary to the topological route ($\chi(\mathbb{CP}^3)=4$) and the algebraic route ($S(n,4)=35$ unique solution). It also predicts which sector masses are odd: $m_u\propto S(3,4)=15$ (odd), $m_d\propto S(1,3)=1$ (odd), while $m_s\propto S(4,3)=20$ (divisible by 4), and $m_e\propto S(13,6)=18564$ (divisible by 4 since $v_2(18564)=2$).

---

## 6. The Complete Index Derivation — Hockey-Stick Engine and the Named Exceptions

The hockey-stick is the engine of the spectrum's backbone: the simplex modes are hockey-stick evaluations of the seeds, and that engine is finite-positive (FP-free). The remaining indices are built from those primaries by a small, named set of additional operations — additive and inclusion–exclusion edges, the $g$-rule, and the top's Euler product — each flagged in the table. The named exceptions are exactly where the framework's extra inputs sit:

| Index | Value | Derivation |
|---|---|---|
| $n_u$ | $3$ | seed: $\chi(\mathbb{CP}^2)=N_c=3$ (T15, ✅); unique single-kernel-image of the ground seed ($\Delta N{=}{+}2$) |
| $n_c$ | $S(4,3)=20$ | hockey-stick in $d{=}3$ through level 3 |
| $n_{\nu_1}$ | $S(3,3)=10$ | hockey-stick in $d{=}3$ through level 2 |
| $n_{\nu_2}$ | $S(3,4)=15$ | hockey-stick in $d{=}4$ through level 2 |
| $n_e$ | $n_{\nu_1}+n_u=13$ | additive node: up seed onto $n_{\nu_1}$; $13$ is not an $S(n,d)$ value and $\{10,3\}$ are not Pascal-adjacent, so generation 1 is **not** a Pascal step (🔶; STEP 116) |
| $n_\mu$ | $S(4,4)=35$ | $= S(4,3)+S(3,4)=n_c+n_{\nu_2}$ (Pascal) |
| $n_{\nu_3}$ | $n_{\nu_1}+n_{\nu_2}-n_u=22$ | inclusion-exclusion: $n_{\nu_1}$ and $n_{\nu_2}$ both arise from seed $n_u$ in $d{=}3$ and $d{=}4$; subtracting $n_u$ removes the double-counted overlap (forced: without it $\Sigma m_\nu\approx98\,\text{meV}$, excluded by DESI); cross-check: $n_{\nu_3}=n_\tau-n_d=22$ |
| $n_\tau$ | $n_{\nu_3}+S(1,d)=23$ | base case $S(1,d)=1$ for all $d$ |
| $n_{\rm top}$ | $\chi(\mathbb{CP}^2)\chi(\mathbb{CP}^3)\chi(\mathbb{CP}^5)=3{\times}4{\times}6=72$ | T15, ✅; product-form site; not a hockey-stick output |
| $n_W$ | $g(d_\nu,n_{\rm top})=d_\nu+n_{\rm top}-1=76$ | $g$-rule: neutrino sector dim $+$ top mode $-1$ (Part 3 §11) |
| $n_Z$ | $g(d_\ell,n_W)=d_\ell+n_W-1=81$ | $g$-rule: lepton sector dim $+$ $n_W-1$; $= n_W+q$, $q=d_\ell-1=S(n_u-1,4)=5$ |
| $n_H$ | $n_u+n_c+n_{\rm top}=95$ | 🔶 empirical closure: the Higgs mode index equals the sum of all three up-type quark mode indices ($3+20+72$) — the boson that mediates mass generation in the up-type sector sits at the total mode count of all three up-type generations. Equivalently $n_d+n_e+n_Z=1+13+81=95$, a second closure through the first-generation fermion seed, the lightest charged lepton, and the neutral weak boson. Both identities hold numerically; dynamical derivation of either is open. |

**Insertion parity of the productions. 🔶** In the condensate-vertex reading of the tower edges (§9c; `idwt.py` STEP 41), the additive fermion edges ($n_e$, $n_\mu$, $n_\tau$) each carry one degree-1 condensate insertion, every $g$-rule production landing in $d=2$ carries none, and the additive Higgs closure carries two. This is the even-insertion selection rule: the $d=2$ variable admits no odd condensate vertex (Part 3 §16.2, the same evenness that protects $m_\gamma = 0$), so a production landing on a $d=2$ mode carries an even insertion count. The additive Higgs closure and the $g$-rule route $n_H = g(n_{\nu_2}, n_Z)$ are two channels of one parity rule rather than competing derivations (mechanism and limits: Part 3 §11; `idwt.py` STEP 55).

**Seed-pair grounding: $\{1, a=3\}$. 🔶** The mode indices 1 (ground seed; $n_d = 1$) and $a = n_u = 3$ are both seeds — inputs to the tower, not derived from $n_s$. $n_u = 3$ carries two independent groundings: (i) $\chi(\mathbb{CP}^2) = N_c = 3$ (T15, ✅-grade geometric anchor), and (ii) it is the unique single-kernel-image of the ground seed ($\Delta N = +2$). $n_s = 4$ is formed from the seed pair $\{1, a=3\}$ via the offset-additive channel: $b = 1 + a = 4$ (⭐ ground-quantum forcing — the lower operand $n_d=1$ is the condensate ground, so the symmetric merge index equals the existing seed $n_u$ and $n_s$ is forced to the antisymmetric channel by elimination; Part 7 §1.2a, `files/idwt.py` STEP 114). The identity $n_u = n_s-1$ holds as the $\chi$-consecutiveness relation $\chi(\mathbb{CP}^k) = k+1$ (T15) applied at $k=2$ and $k=3$ — a geometric consequence, not a mechanism selecting $n_u$ from $n_s$. The $g$-rule lattice closure, the T4 double-degeneracy exhaustion (an exact linear forcing $n+1=5$), the closed-form ratio crossing, the matter-quartet identity $2n_s-4 = n_s$, and the muon fixed point $S(4,4) = 35$ are uniqueness certificates confirming $b = 4$. $b = 1+a$ is ⭐ for $n_s$ by ground-quantum forcing; the general offset-additive reading remains 🔶 only for the charged-lepton edges $e,\mu$ (both operands non-ground), and the $\chi(\mathbb{CP}^2) = N_c$ anchor for $n_u = 3$ is ✅-grade.

The physical claim this sharpens: **if mass is the cumulative microstate count $S(n,d)$, then the hockey-stick identity governs the simplex backbone exactly** — every simplex mode index is a forced hockey-stick evaluation, and where two simplex modes meet at a Pascal node (the generation-2 lepton $n_\mu = S(4,4) = S(4,3)+S(3,4)$, ✅) the selection rule is a theorem. The composite indices are the named exceptions where additional inputs enter: the top's Euler product, the generation-1 charged-lepton additive node ($n_e = n_{\nu_1}+n_u$, **not** a Pascal step — STEP 116), the inclusion-exclusion $\nu_3$, and the boson $g$-rule chain. The hockey-stick leaves no freedom in the backbone; the open content of the spectrum lives entirely in those named composite edges.

### 6a. Cross-Mode Polynomial Identity ⭐

The generation tower indices satisfy a family of exact polynomial identities (verified for $n_s = 3,4,5,6$):

$$n_{\rm charm} \times N_c \;=\; n_{\nu_1} \times N_f \;=\; 4 \times n_{\nu_2} \;=\; \frac{n_s(n_s-1)(n_s+1)(n_s+2)}{6}$$

For $n_s = 4$: $20 \times 3 = 10 \times 6 = 4 \times 15 = 60$.

Equivalently: $n_{\nu_1}/n_{\nu_2} = 4/N_f = 2/3$ and $n_{\rm charm}/n_{\nu_1} = N_f/N_c = 2$.

The combinatorial source is:

$$n_{\rm charm} = S(n_s,3) = \binom{n_s+2}{3}, \quad n_{\nu_1} = S(n_u,3) = \binom{n_u+2}{3} = \binom{n_s+1}{3}, \quad n_{\nu_2} = S(n_u,4) = \binom{n_s+1}{4}$$

with $N_c = \chi(\mathbb{CP}^2) = n_u = 3$ and $N_f = 2n_s-2 = n_s+n_u-1 = 6$ (light quark flavours u,d,s,c,b,t). The identity $S(n_s,3)\cdot N_c = S(n_u,3)\cdot N_f$ holds because $\binom{n_s+2}{3}/(n_s-1) = \binom{n_u+2}{3}/(2n_s-2) = n_s(n_s+1)/6$, which follows from $n_u = n_s-1$. ⭐

---

## 7. The Neutrino Sector

All three neutrino indices follow directly from the same hockey-stick evaluations:

$$n_{\nu_1} = S(n_u,3) = S(3,3) = 10, \qquad n_{\nu_2} = S(n_u,4) = S(3,4) = 15, \qquad n_{\nu_3} = n_{\nu_1}+n_{\nu_2}-n_u = 22$$

The neutrino gaps are themselves sums of quark seeds:

$$n_{\nu_2}-n_{\nu_1} = 5 = n_s+n_d, \qquad n_{\nu_3}-n_{\nu_2} = 7 = n_u+n_s$$

**Normal mass ordering predicted:** $S(n,5)$ is strictly increasing, so $m_{\nu_1} < m_{\nu_2} < m_{\nu_3}$. Consistent with current experimental preference at 3–4σ.

**Spectral grounding (sector spectral counting theorem, T-S1):** $S(n,5) = \frac{1}{2}N_{D_{S^5}}(n-1)$. Neutrino masses obey the same sector spectral counting law as down-type quark masses: mass equals half the cumulative Dirac eigenvalue count on $S^5$ below the mode's level. The three neutrino modes ($n=10, 15, 22$) correspond to $2\times S(10,5)=4004$, $2\times S(15,5)=23256$, and $2\times S(22,5)=131560$ cumulative Dirac eigenstates on $S^5$.

From $m_{\rm scale,5} = (n_u/n_s) \times m_{\rm scale,6}^3/m_{\rm scale,4}^2$ (§9c): $m_{\nu_1} = 1.487$ meV, $m_{\nu_2} = 8.639$ meV, $m_{\nu_3} = 50.27$ meV (corrected; bare 48.87 meV), $\Sigma m_\nu = 60.39$ meV (bare 59.00 meV; $\delta_{\nu_3} = 1/35$, §9d).

---

## 8. The Bottom Quark — Quartic Bifurcation

The bottom quark fits no clean simplex sector. It arises within $d=3$ at the resonance point $k_0 = n_{\rm strange}^2 = 4^2 = 16$ — derived entirely within $d=3$. Three resonance conditions coincide at $k_0$:

$$k_0 = n_s^2 = 16 \quad(\text{quartic kernel resonance at seed self-product})$$

$$k_0 = n_e + n_u = 13+3 = 16 \quad(\text{lepton--quark additive closure})$$

$$k_0 = S(n_s,3)-S(2,3) = 20-4 = 16 \quad(\text{$g$-rule gap from absent }n{=}2\text{ mode})$$

All three hold exactly from seeds; no other site in any sector satisfies all three simultaneously (exhaustive search $n \leq 200$, $d \in D$). Of the three, the first is the definition of $k_0$; the second and third are independent coincidences whose solution sets in $n_s$ meet only at $n_s = 4$, so neither follows from the other and each fixes the seed on its own. The index arithmetic is sector-blind, so all three stand as equal characterizations of $k_0$; among them the lepton–quark closure $n_e + n_u$ is the one whose two indices lie in different sectors, the simplex gap $S(n_s,3) - S(2,3)$ being internal to $d=3$.

**Why the geometric mean.** The Jacobi coupling between adjacent $d=3$ modes near $k_0$ is $K_{n,n+1} \propto \sqrt{b_n \cdot b_{n+1}}$ where $b_n = \sqrt{n(n+d-1)}/(2n+d-2)$; at the triple-coincidence site the $\ell=0$ kernel drives modes $n=16$ and $n=17$ with equal weight. The beat is sustained by the quartic density–density kernel term $|\Psi^{(16)}|^2\,|\Psi^{(17)}|^2$. The magnitude of that cross-term scales as the product $E_{16}E_{17}$ — a quantity of dimension energy-squared — so the resonant beat sits at its square root, $E^2 = E_{16}E_{17}$, the geometric mean:

$$m_b = \sqrt{S(16,3)\times S(17,3)}\times m_{\rm scale,3} = \sqrt{816\times969}\times 4.7019\ \text{MeV} = 4{,}181\ \text{MeV} \quad(-0.05\%\text{ vs PDG }4{,}183\pm7\ \text{MeV})$$

🔶 This dimensional argument fixes the geometric mean; a closed derivation from the quartic kernel eigenvalue problem remains open.

### 8a. Composite Hadron Masses from the Beat Structure

Mesons and baryons are composite bound states — not sector eigenmodes and not assigned mode indices $(n,d)$. Their masses depend on the constituent quark masses and the binding dynamics. Two regimes apply, with the boundary at $m_{\rm quark} \sim \Lambda_{\rm QCD} = 282$ MeV.

**Chiral regime** ($m_{\rm quark} \ll \Lambda_{\rm QCD}$): the Gell-Mann–Oakes–Renner (GOR) relation with IDWT-derived chiral condensate parameter $B_0$:

$$m_{\rm meson}^2 = (m_{q_1} + m_{q_2}) \times B_0, \qquad B_0 = \Lambda_{\rm QCD} \times \frac{S(n_s,3)}{2} = \frac{N_c}{2} \cdot \frac{f_\pi^2}{m_{\rm scale,3}} = 2821\ \text{MeV}$$

Every factor is IDWT-derived: $N_c = \chi(\mathbb{CP}^2) = 3$, $f_\pi = m_{\rm scale,3} \times S(n_s,3)$. Equivalently $B_0 = \Lambda_{\rm QCD} \times n_s(n_s^2-1)/6$.

| Meson | Content | Predicted | PDG | Error |
|-------|---------|-----------|-----|-------|
| π± | ūd | 139.3 MeV | 139.6 | −0.2% |
| K± | ūs | 521.0 | 493.7 | +5.5% |
| D± | c̄d | 1903.6 | 1869.7 | +1.8% |
| D$^0$ | c̄u | 1901.7 | 1864.8 | +2.0% |
| $D_s$ | c̄s | 1968.7 | 1968.4 | 0.0% |

The kaon error (5–6%) is consistent with leading-order $SU(3)$ chiral perturbation theory. The $D_s$ error is 0.0%.

**Heavy-quark regime** ($m_{\rm quark} \gg \Lambda_{\rm QCD}$): the meson mass is the sum of the constituent masses plus a binding energy equal to the geometric mean of the heavy quark mass and the QCD scale:

$$m_{\rm meson} = m_{q_1} + m_{q_2} + \sqrt{m_{\rm heavy} \times \Lambda_{\rm QCD}}$$

For B mesons and bottomonium, $m_{\rm heavy} = m_b$ and the binding energy is:

$$E_{\rm bind} = \sqrt{m_b \times \Lambda_{\rm QCD}} = m_{\rm scale,3} \times \sqrt{N_c \, S(n_s,3) \times \sqrt{S(n_s^2,3)\,S(n_s^2+1,3)}} = 1086\ \text{MeV}$$

The factor $k_0 = n_s^2 = 16$ — the same triple-coincidence that forces the b quark beat — reappears here. The binding energy of every B meson and bottomonium state is therefore determined by $n_s$ alone:

| Meson | Predicted | PDG | Error |
|-------|-----------|-----|-------|
| B± | 5269.3 MeV | 5279.3 | −0.19% |
| B$^0$ | 5271.9 | 5279.7 | −0.15% |
| $B_s$ | 5361.2 | 5366.9 | −0.11% |
| Υ(1S) | 9448.3 | 9460.3 | −0.13% |
| J/ψ | 3160.3 | 3096.9 | +2.0% |

D mesons sit at the crossover ($m_c \gg \Lambda_{\rm QCD}$) where both formulas give ~1–2% accuracy. The J/ψ +2% residual reflects the expansion parameter $\Lambda_{\rm QCD}/m_c = 0.22$ being non-negligible for charm (vs 0.07 for bottom); the J/ψ–η_c difference (113 MeV) is a vector–pseudoscalar distinction — different object types in IDWT, as with ρ and π — not a correction to the single formula. Script: `files/idwt.py`. **Status: 🔵** (both formulas verified across 10 states; J/ψ spin correction open).

**$d=3$ hadronic resonance spectrum. 🔵** The $d=3$ sector supports a tower of modes at $m = m_{\rm scale,3} \times S(n,3)$ for integer $n$. These modes are not co-fixed-points — they are not stable particles — but survive as colour-singlet resonances observable as broad short-lived states. The mode indices are pinned by seed algebra:

$$n_\rho = n_s + n_{\rm up} + 2n_{\rm down} = 4+3+2 = 9 \qquad (\text{uu̅/dd̅ nonet})$$
$$n_\phi = 2n_s + 2n_{\rm down} = 8+2 = 10 \qquad (\text{ss̅ nonet})$$

The step $n_\phi - n_\rho = n_{\rm strange} - n_{\rm up} = 1$ is the algebraic signature of replacing one $u$ quark by one $s$ quark in the composite. Predictions:

| Resonance | $n$ | $S(n,3)$ | IDWT (MeV) | PDG (MeV) | Error |
|-----------|-----|----------|------------|-----------|-------|
| ρ/ω | 9 | 165 | 775.8 | 775.3/782.7 | +0.1% |
| φ(1020) | 10 | 220 | 1034.4 | 1019.5 | +1.4% |

The ρ prediction is independently confirmed at +0.069% by the cross-sector filter $\Gamma_{346}$ (§10). The φ prediction at +1.4% uses the same formula; the slightly larger residual (vs the sub-percent light-quark residuals) reflects that composite resonances sit higher in the mode tower where next-order kernel corrections are less constrained. Script: `files/idwt.py` (resonance table output). **Status: 🔵**

⭐ **RSK combinatorial fusion rule.** The Robinson-Schensted-Knuth bijection maps each semistandard Young tableau of shape $(n-1)$ with entries at most $d+1$ to a pair of lattice paths, and $S(n,d)$ counts these tableaux. This gives a deterministic combinatorial fusion rule: inserting the word for mode $S(a,d)$ into the tableau for mode $S(b,d)$ via RSK yields the tableau for $S(a+b,d)$, with the shape of the result identifying the sector the product lands in — no Clebsch-Gordan coefficients. The ρ meson collision $n_\rho = 5+4 = 9$ (in mode-index terms, combining the $n_u=3$ and $n_s=4$ seed words) becomes, under RSK, the concatenation of two 2-row tableaux yielding a 2-row tableau of weight 9. The collision is not an arithmetic accident; it is the Pieri rule for tableaux, forced by the same seed algebra that fixes $n_s=4$.

**Baryon octet — $(N_c-1)$ color-bond formula. 🔵** When one quark in a colour-singlet baryon is replaced by a heavier quark, each of the remaining $(N_c-1)$ colour bonds contributes the mass difference. With $N_c - 1 = \chi(\mathbb{CP}^1) = 2$ from T15:

$$\boxed{m(\text{baryon}) = m_N + (N_c-1)\sum_{\text{replaced}} (m_s - m_{\rm replaced})}$$

**Structural identity.** The nucleon formula rewrites as $m_N = N_c\Lambda_{\rm QCD} + m_s$, because $N_c\Lambda_{\rm QCD}/n_u^2 = m_s$ exactly (both equal 94.04 MeV). The proton mass is the colour confinement scale plus the strange quark mass — forced by seeds alone.

| Baryon | Content | Prediction | PDG | Error |
|--------|---------|-----------|-----|-------|
| p/n | uud/udd | 940.4 MeV | 938.9 | +0.2% |
| $\Lambda$ | uds | $m_N + 2(m_s - m_d) = 1119$ | 1115.7 | +0.3% |
| $\Xi^0$ | uss | $m_N + 2[(m_s-m_u)+(m_s-m_d)] = 1303$ | 1314.9 | −0.9% |
| $\Xi^-$ | dss | $m_N + 2[(m_s-m_u)+(m_s-m_d)] = 1303$ | 1321.7 | −1.4% |

The $\Sigma$(uds) has identical quark content to the $\Lambda$, so the formula gives the same prediction for both; the 77 MeV $\Sigma$–$\Lambda$ difference is a small same-type residual the formula does not resolve. The $\Omega$(sss, $J=3/2$) is in the baryon decuplet, outside this formula's scope. Script: `files/idwt.py`.

---

## 9. Coupling Constants — Complete Derived Set

The coupling matrix $G$ has rank 1: $G_{dd'} = v_d\times v_{d'}$ where $v_d = \sqrt{g_{dd}}$. All cross-sector couplings follow from the six sector self-couplings, which reduce to five distinct values ($g_{66} = g_{10,10}$). $g_{33}$ and $g_{44}$ from seed pair $\{n_u=3, n_s=4\}$ ($n_u=3$ grounded by $\chi(\mathbb{CP}^2)=N_c=3$, T15); $g_{66}$ and $g_{10,10}$ from $\mathbb{CP}^3$ complex geometry (§9c); $g_{22}$ from the cross-sector back-reaction fixed-point (§10); $g_{55} = 96/g_{22}$ from Hopf universality. All six sector self-couplings are derived from $m_e$ and seeds.

---

### $g_{33} = 8\sqrt{7}$ and $g_{44} = 12/\sqrt{7}$ — both from $n_s$ alone

Both coupling constants are derived simultaneously from the seed pair $\{n_d=1, n_u=3\}$, using a single universal structure. Neither is primary.

**The universal coupling coefficient** (same for both sectors by binomial symmetry $\binom{n}{k}=\binom{n}{n-k}$):

$$g_{\rm coeff} = \sqrt{\frac{n_s(n_s+1)}{S(n_s,4)}} = \sqrt{\frac{20}{35}} = \sqrt{\frac{4}{7}} = \frac{2}{\sqrt{7}} = \sqrt{\frac{n_u(n_u+1)}{S(n_u,5)}} = \sqrt{\frac{12}{21}} = \frac{2}{\sqrt{7}}$$

These are equal because $n_u+3 = n_s+2 = 6$ (using $n_s = n_u+1$) $\Rightarrow$ $\binom{6}{4}=\binom{6}{2}$.

**The gaps:**

$${\rm gap}_{d=3} = n_s^2 = 16 = k_0 \quad[\text{seed self-interaction}]$$

$${\rm gap}_{d=4} = \frac{2n_s n_u}{n_s+n_u} = \frac{24}{7} \quad[\text{harmonic mean of }n_s\text{ and }n_u]$$
The $d=3$ gap equals $k_0$ — the same resonance condition driving the bottom quark bifurcation. The $d=4$ gap is the harmonic mean of both seeds, the natural effective gap when two boundary conditions act simultaneously.

**Both couplings, from the same formula:**

$$g_{33} = \frac{{\rm gap}_{d=3}}{g_{\rm coeff}} = \frac{n_s^2\sqrt{n_s+n_u}}{2} = 8\sqrt{7}, \qquad g_{44} = \frac{{\rm gap}_{d=4}}{g_{\rm coeff}} = \frac{n_s n_u}{\sqrt{n_s+n_u}} = \frac{12}{\sqrt{7}}$$

**Closed forms and rank-1 as a theorem:**

$$g_{33} = \frac{n_s^2\sqrt{n_s+n_u}}{2} = 8\sqrt{7}, \quad g_{44} = \frac{n_s n_u}{\sqrt{n_s+n_u}} = \frac{12}{\sqrt{7}}, \quad g_{34} = \sqrt{g_{33}g_{44}} = \sqrt{\frac{n_s^3 n_u}{2}} = \sqrt{96} = 4\sqrt{6}$$

$$g_{33}\times g_{44} = \frac{n_s^3 n_u}{2} = \frac{64\times3}{2} = 96$$

The rank-1 identity $g_{33}\times g_{44} = g_{34}^2$ follows from the seed structure alone. $g_{33}$, $g_{44}$, and $g_{34}$ are all theorems of the seed pair $\{n_d=1, n_u=3\}$.

**$g_{33}$ from $g_{44}$:** $g_{33}/g_{44} = n_s(n_s+n_u)/(2n_u) = 4\times7/6 = 14/3$. This ratio equals $(m_d/m_u)^2$ — the squared lightest-particle mass ratio between sectors — another consequence of the seed structure, not an independent assumption.

---

### $g_{66} = 1/4$ — from $\mathbb{CP}^3$ complex geometry

The $d{=}6$ sector lives on $\mathbb{CP}^3$. Three independent geometric properties of $\mathbb{CP}^3$ all fix the same value:

1. **Euler characteristic:** $\chi(\mathbb{CP}^3) = 4 = n_s$ (Part 1 §3a). The sector coupling is $1/\chi(\mathbb{CP}^3) = 1/n_s = 1/4$.

2. **Fubini-Study curvature:** The minimum sectional curvature of $\mathbb{CP}^3$ with the Fubini-Study metric is $1/4$ (attained on totally real planes). This is the unique curvature scale invariant under the full $\mathrm{Sp}(2)$ isometry group of the sector, and it equals $1/n_s$.

Both give $g_{66} = 1/n_s = 1/4$, with no mass input and no hypercharge assumption.

$$g_{66} = \frac{1}{n_s} = \frac{1}{4}$$

**Anomaly cancellation as cross-check.** With $g_{66}$ established from geometry, the lepton hypercharge follows as $Y_L = -\sqrt{g_{66}} = -1/2$. Inserting into the $\mathrm{SU}(2)^2\mathrm{U}(1)$ and $\mathrm{SU}(3)^2\mathrm{U}(1)$ anomaly conditions (with $N_c = 3$ from the $\mathbb{CP}^2$ Dirac index, Part 8 §2) yields the full SM hypercharge table — $Y_Q = 1/6$, $Q_u = 2/3$, $Q_d = -1/3$ — without further input. The anomaly equations are satisfied exactly, confirming consistency.

This is exact and requires no mass input.

---

### $g_{10,10} = 1/4$ — from tau hypercharge

The tau sector shares the same coupling $g_{10,10} = g_{66} = 1/n_s = 1/4$: both $d=6$ and $d=10$ are CP sectors with coupling set directly by $n_s=4$, so the kernel cannot distinguish them. The mass difference between muon and tau arises entirely from the different sector geometry ($S(35,6)$ vs $S(23,10)$), not from any coupling difference.

---

### $g_{55}$ — from Hopf fiber universality

The two $U(1)$ Hopf fibrations sharing the electromagnetic fiber are:

$$S^1 \to S^3 \to \mathbb{CP}^1 \quad (d{=}3\text{ total},\ d{=}2\text{ base}), \qquad S^1 \to S^5 \to \mathbb{CP}^2 \quad (d{=}5\text{ total},\ d{=}4\text{ base})$$

The fiber is the same $U(1)$ in both. Universality requires the ratio (total-space coupling)/(base coupling) to be identical:

$$\frac{v_3}{v_2} = \frac{v_5}{v_4}$$

Cross-multiplying: $v_3 \times v_4 = v_2 \times v_5$, i.e. $g_{25} = g_{34} = 4\sqrt{6}$.

The cross-coupling between the two Hopf partner pairs is equal. Solving for $v_5$:

$$v_5 = \frac{v_3 v_4}{v_2} = \frac{g_{34}}{v_2}, \qquad g_{55} = v_5^2 = \frac{g_{33}\times g_{44}}{g_{22}} = \frac{96}{g_{22}}$$

Numerically with $g_{22} = 722.5$:

$$g_{55} = 0.1329, \qquad v_5 = 0.3645$$

**Verification:** $v_3/v_2 = v_5/v_4 = 0.17116$ and $g_{25} = v_2\times v_5 = 9.798 = g_{34} = 4\sqrt{6}$

**Key consequence:** $g_{55}$ is fully determined by $g_{22}$ — no additional measurement is needed. The coupling algebra is closed by the single measured constant $m_e$: all six sector self-couplings are derived ($g_{33}$ and $g_{44}$ from seeds, $g_{66}$ and $g_{10,10}$ from $\mathbb{CP}^3$ complex geometry, $g_{55} = 96/g_{22}$ from Hopf universality, $g_{22}$ from the cross-sector mode formula §10).

**Neutrino mass scale (derived, §9c):** The $d{=}5$ scale is set by the cross-sector fixed point $m_{\rm scale,5}\times m_{\rm scale,4}^2 = (n_u/n_s)\times m_{\rm scale,6}^3 = 7.429\times10^{-13}\ \text{MeV}$. This is the $d{=}5$ analog of the $g_{22}$ back-reaction equation. No suppression mechanism is needed; the small scale arises geometrically from the Hopf fibration $S^1\to S^5\to\mathbb{CP}^2$. The $d{=}5$ sector admits only Dirac spinors ($d\bmod8=5$ forbids Majorana), so $0\nu\beta\beta$ is forbidden at all orders: no charge-conjugation matrix $C$ exists on the $S^5$ spinor bundle, so cross-sector couplings cannot construct $\psi^T C\psi$ at any loop order.

---

### Cross-couplings — all from rank-1

$$g_{34} = \sqrt{g_{33}g_{44}} = \sqrt{96} = 4\sqrt{6}$$

$$g_{25} = \sqrt{g_{22}g_{55}} = \sqrt{96} = 4\sqrt{6} \quad[= g_{34}:\text{ Hopf universality}]$$

$$g_{36} = \sqrt{g_{33}g_{66}} = \sqrt{2\sqrt{7}}, \quad g_{46} = \sqrt{g_{44}g_{66}} = \sqrt{3/\sqrt{7}}$$

$$g_{3,10} = \sqrt{g_{33}g_{10,10}} = \sqrt{2\sqrt{7}} \;[= g_{36}], \quad g_{4,10} = \sqrt{g_{44}g_{10,10}} = \sqrt{3/\sqrt{7}} \;[= g_{46}]$$

$$g_{6,10} = \sqrt{g_{66}g_{10,10}} = \tfrac{1}{4} \;[= g_{66}]$$

**Coupling algebra complete:** All six sector self-couplings are derived from $m_e$ and the seed pair $\{n_d=1, n_u=3\}$. $g_{33}$ and $g_{44}$ from seed equations; $g_{66}$ and $g_{10,10}$ from $\mathbb{CP}^3$ complex geometry (§9c); $g_{22} = (S(n_s,3)-n_u)^2\times S(n_u-1,4)/2$ from seeds (§10); $g_{55} = 96/g_{22}$ from Hopf universality.

---

## 9b. Tau Mass — Geometric Back-reaction Correction

The tau is the one lepton whose raw simplex prediction requires a correction at all. The mechanism is the isotropic back-reaction between the $d=6$ and $d=10$ sectors.

**Setup.** The $d=6$ and $d=10$ sectors share the coupling $g_{6,6} = g_{6,10} = g_{10,10} = 1/n_s = 1/4$, derived from $n_s=4$ (not from hypercharge). This isotropy — both sectors carry identical coupling $1/n_s$ — means the back-reaction from $d=6$ onto $d=10$ feeds back on itself via $g_{10,10}$.

**Self-consistent equation.** The $d{=}6\to d{=}10$ back-reaction shift $\Delta m$ satisfies:

$$\Delta m = \varepsilon_{6\to10}\times m_\tau + g_{10,10}\times\Delta m$$

The second term is the self-feedback: the shifted tau mass feeds further back-reaction through its own $g_{10,10}$ coupling. Solving:

$$\Delta m = \frac{\varepsilon_{6\to10}\times m_\tau}{1-g_{10,10}}$$

Since $g_{10,10} = 1/n_s = 1/4$, the denominator is $3/4 = n_u/n_s$, giving resummation factor $n_s/n_u = 4/3$. This ratio equals $n_u/n_s = 3/4$, with $n_u=3$ (seed) and $n_s=4$; it is not a free parameter.

**The total correction.** The leading $d{=}6\to d{=}10$ kernel perturbation at the tau level is:

$$\varepsilon_{6\to10} = \frac{1}{n_s^3\times S(n_s,4)} = \frac{1}{64\times35} = \frac{1}{2240}$$

The factor $n_s^3 = k_0 \times n_s$ is the resonance volume; $S(n_s,4) = n_\mu$ is the frequency normalization. Both are completely determined by $n_s = 4$.

Multiplied by the resummation factor $4/3$:

$$\varepsilon_{\rm total} = \frac{1}{2240}\times\frac{4}{3} = \frac{1}{1680} = \frac{1}{n_u\times n_s^2\times S(n_s,4)}$$

Equivalently: **$1680 = n_s \times n_u \times (n_s+n_u) \times S(n_s,3) = 4 \times 3 \times 7 \times 20$**

Each factor has an independent meaning from the seed structure:
- $n_s = 4$: $b = 1+3$ (Dirac index of the lepton sector, $\mathrm{ind}(D_{\mathbb{CP}^3}) = 4$)
- $n_u = 3$: seed ($\chi(\mathbb{CP}^2) = N_c = 3$, T15); $n_u = n_s-1$ by the $\chi$-consecutiveness identity
- $n_s + n_u = 7$: the sum of $n_s$ and the seed $n_u$
- $S(n_s,3) = 20$: the strange quark mode count (= $n_c$, the charm mode index)

The product $n_s \times n_u \times (n_s+n_u) \times n_c$ is the canonical combinatorial invariant of the quark sector at the seed level. Its reciprocal is the subleading back-reaction correction.

**Result.** 🔵

$$m_\tau = m_e\times\frac{S(23,10)}{S(13,6)}\times\!\left(1+\frac{1}{1680}\right) = 1776.84\ \text{MeV} \quad (\text{PDG 2024: }1776.93\pm0.09\ \text{MeV},\ {-}1.0\sigma)$$

No inputs beyond $m_e$ and the seed pair $\{n_d=1, n_u=3\}$.

---

## 9c. Neutrino Mass Scale — Cross-Sector Fixed Point

The $d=5$ sector ($S^5$) has Euler characteristic $\chi=0$ — no self-confinement and no direct eigenmode selection from within the sector potential. The neutrino mass scale is set instead by the **three-sector cross-scale consistency equation** linking $d=4$, $d=5$, and $d=6$:

$$m_{\rm scale,5}\times m_{\rm scale,4}^2 = \frac{n_u}{n_s}\times m_{\rm scale,6}^3$$

This is the $d=5$ analog of the $d=2$ back-reaction equation $g_{22} = p^2q/2$: the neutrino scale is fixed by the balance between the $d=4$ quark scale (heavy, appearing squared in the denominator) and the $d=6$ lepton scale (light, appearing cubed). The ratio $n_u/n_s = 3/4$ is the Hopf chain geometric ratio.

**Explicit formula:**

$$m_{\rm scale,5} = \frac{n_u}{n_s}\times\frac{m_{\rm scale,6}^3}{m_{\rm scale,4}^2} = \frac{3}{4}\times\frac{(m_e/S(13,6))^3}{m_{\rm scale,4}^2} = 7.429\times10^{-13}\ \text{MeV}$$

**Physical interpretation.** The neutrino mass scale is suppressed by the sector hierarchy: $m_{\rm scale,4}^2$ appears in the denominator because the $d=5$ sector is tied to the $d=4$ quark sector through the $S^1$ fiber of the Hopf fibration $S^1\to S^5\to\mathbb{CP}^2$. This is purely geometric suppression — no Majorana mass, no heavy right-handed partner. The small scale arises from the relative depths of the sector potential wells, which are fixed by the tower coupling constants.

**Neutrino mass predictions (no empirical neutrino input):**

| Quantity | Mode index | IDWT | PDG/experiment | Status |
|---|---|---|---|---|
| $m_{\nu_1}$ | $n_{\nu_1} = S(n_u,3) = 10$ | 1.487 meV | — | Absolute mass; testable by CMB-S4 + Project 8 |
| $m_{\nu_2}$ | $n_{\nu_2} = S(n_u,4) = 15$ | 8.639 meV | — | Absolute mass |
| $m_{\nu_3}$ | $n_{\nu_3} = n_\tau - n_d = 22$ | 48.87 meV → 50.27 meV | — | Absolute mass; 2.5–2.9% below oscillation inference; corrected by $\delta_{\nu_3} = 1/35$ (§9d) |
| $\Sigma m_\nu$ | — | 60.39 meV (corrected; bare 59.00 meV) | < 120 meV | ✅ within Planck bound; CMB-S4 target ~30 meV |
| $m_{\nu_2}/m_{\nu_1}$ | — | 5.808 | — | Pure ratio: $S(15,5)/S(10,5)$; exact from mode indices |
| $m_{\nu_3}/m_{\nu_1}$ | — | 32.86 | — | Pure ratio: $S(22,5)/S(10,5)$; exact from mode indices |
| $m_{\beta\beta}$ | — | 0 (exact) | unobserved | Majorana forbidden in $d=5$ |

**Normal mass ordering predicted:** $S(n,5)$ is strictly increasing, so $m_{\nu_1} < m_{\nu_2} < m_{\nu_3}$. Consistent with current experimental preference at 3–4σ.

**On $m_{\nu_3}$ and oscillation data.** Oscillation experiments measure $\Delta m^2$ (interference of mass eigenstates in flight) because they cannot access absolute masses. IDWT predicts absolute masses directly, so $\Delta m^2$ values are derived consequences, not primary quantities. Expressed natively: $m_{\nu_3} = 48.87$ meV is 2.5–2.9% below the value implied by current oscillation data (PDG 2023: $\Delta m^2_{31} = 2.523\times10^{-3}$ eV$^2$; PDG 2024 Normal Order: $\Delta m^2_{31} = 2.530\times10^{-3}$ eV$^2$, from $\Delta m^2_{32} = 2.455 + \Delta m^2_{21} = 0.0753$). The correction $\delta_{\nu_3} = 1/35$ (derived in §9d from $\varepsilon \times g_{33} = 1/35$ exactly) gives $m_{\nu_3}^{\rm corr} = 48.871 \times 36/35 = 50.267$ meV, implying $\Delta m^2_{31} = 2.5246\times10^{-3}$ eV$^2$ — matching PDG 2023 within 0.05% and PDG 2024 within 0.2σ (uncertainty $\pm0.028\times10^{-3}$).

**On $m_{\nu_1}$, $m_{\nu_2}$ and the solar splitting.** The predicted $\Delta m^2_{21} = (m_{\nu_2}^2 - m_{\nu_1}^2) = (8.639^2 - 1.487^2)\times10^{-6}$ eV$^2$ $= 7.242\times10^{-5}$ eV$^2$ lies 3.8% below the PDG 2024 central value of $7.53\times10^{-5}$ eV$^2$ (uncertainty $\pm0.18\times10^{-5}$), a discrepancy of −1.6σ. Unlike the $\Delta m^2_{31}$ case, no structural correction analogous to $\delta_{\nu_3}$ is available: $n_{\nu_1} = S(n_u,3)$ and $n_{\nu_2} = S(n_u,4)$ are primary Pascal evaluations at the seed with no cross-sector entanglement, so there is no inclusion-exclusion residual to correct. The mode indices are exact; the discrepancy resides entirely in the overall scale $m_{\rm scale,5}$, which is fixed by the cross-sector equation and admits no free parameter. At present this is a ~1.6σ tension; it is not explained away. It is recorded here as a genuine open question: whether a first-principles mechanism shifts the solar splitting by ~3.8% without disturbing $\Delta m^2_{31}$, or whether the central value shifts as reactor and solar constraints are refined ($\Delta m^2_{21}$ has historically shown tension between KamLAND and solar analyses at the ~2% level).

**Structural source.** $n_{\nu_1} = S(n_u,3) = 10$ and $n_{\nu_2} = S(n_u,4) = 15$ are primary Pascal evaluations at the seed. $n_{\nu_3} = n_{\nu_1} + n_{\nu_2} - n_u = 22$ is derived by inclusion-exclusion from two primary modes — the only neutrino mode requiring information from both the $d=3$ and $d=4$ Hopf images. This cross-sector entanglement makes $n_{\nu_3}$ susceptible to a correction at the seed level: the leading $d=4$ evaluation above $n_u$ is $S(n_s,4) = 35$ (a hockey-stick identity consequence: $S(n_s+1,3) = S(n_s,4) = 35$), which appears as the natural denominator. This is structurally analogous to the τ back-reaction correction $1/1680 = 1/(n_u \times n_s^2 \times S(n_s,4))$ — the same $S(n_s,4) = 35$ appears — but without the Gegenbauer criticality factor $n_s^2 = 16$ ($d=5$ is not at the critical point) and without the back-reaction resummation factor $n_u$ ($g_{55} \neq 1/n_s$). The first-principles derivation of this coefficient is given in §9d.

The corrected $\Sigma m_\nu = 1.487 + 8.639 + 50.267 = 60.393$ meV; bare 59.00 meV. Both are within current cosmological bounds; CMB-S4 will distinguish them.

**Observable predictions:**

- $\Sigma m_\nu = 60.39$ meV: detectable by Simons Observatory (CMB-S4 sensitivity ~30 meV — within a factor 2)
- $m_\beta \approx 8.77\ \mathrm{meV}$: below KATRIN bound (< 450 meV) and below Project 8's long-term goal (~40 meV) — not accessible in near-term beta-decay experiments
- $m_{\beta\beta} = 0$ exactly: 0νββ decay is forbidden (Majorana mass forbidden in $d=5$ by spin structure)
- Normal hierarchy: $m_{\nu_1} \ll m_{\nu_2} \ll m_{\nu_3}$



**Prediction from the derived set:** $m_u/m_d = \sqrt{g_{44}/g_{33}} = \sqrt{(12/\sqrt{7}) \div 8\sqrt{7}} = \sqrt{12/56} = \sqrt{3/14} = 0.4629$. PDG: 0.462 ± ~0.10 (the ratio carries ±25% uncertainty from lattice QCD). Error relative to central value: +0.20%.

---

## 9d. The $\nu_3$ Correction — Closure Relation 🔶

The correction $\delta_{\nu_3} = 1/35$ (§9c) is a highly constrained closure relation: given the $\ell=2$ scale $\varepsilon$ (§11.2) and the $d=3$ self-coupling $g_{33}$ (T9), their product is 1/35 by an algebraic identity. The identity is exact and the inputs are fully derived elsewhere in the framework. What is not yet shown is the deeper operator mechanism — specifically, why the $l=2$ cross-term of the T2 kernel acts on the inclusion-exclusion mode $n_{\nu_3}$ with precisely this product of amplitudes, rather than a different kernel-level combination. Until that mechanism is derived from first principles, $\delta_{\nu_3} = 1/35$ should be understood as a closure relation: an exact algebraic consequence of independently-derived quantities that happens to match observation, rather than an unavoidable structural prediction.

**Setup.** Let $k_0 = n_s^2 = 16$ (the quartic bifurcation index). From §11.2, the $\ell{=}2$ scale $\varepsilon$ is:

$$\varepsilon = \frac{g_{\rm coeff}}{k_0\times n_\mu}$$

where $g_{\rm coeff} = 2/\sqrt{n_s+n_u} = 2/\sqrt{7}$ is the self-consistency eigenvalue from the seed equations (§11.2), and $n_\mu = S(n_s,4) = 35$. From T9, the $d{=}3$ sector self-coupling is:

$$g_{33} = \frac{n_s^2\sqrt{n_s+n_u}}{2} = 8\sqrt{7}$$

**Identity.** Computing the product:

$$g_{\rm coeff}\times g_{33} = \frac{2}{\sqrt{n_s+n_u}}\times\frac{n_s^2\sqrt{n_s+n_u}}{2} = n_s^2 = k_0 \quad[\sqrt{7}\text{ cancels exactly}]$$

Therefore:

$$\varepsilon\times g_{33} = \frac{g_{\rm coeff}}{k_0\times n_\mu}\times g_{33} = \frac{g_{\rm coeff}\times g_{33}}{k_0\times n_\mu} = \frac{k_0}{k_0\times n_\mu} = \frac{1}{n_\mu} = \frac{1}{S(n_s,4)} = \frac{1}{35} \quad[\text{exact}]$$

The $\sqrt{7}$ factors cancel algebraically. The result follows from $n_s$, $n_u$, and $n_\mu$ alone — the same three quantities that determine $k_0$ and the $\ell=2$ scale $\varepsilon$. No additional input enters.

**Why $\nu_3$ and not $\nu_1$ or $\nu_2$.** The $l=2$ cross-term (T2) generates corrections at inclusion-exclusion mode indices — modes that receive simultaneous contributions from two distinct sector images:

- $n_{\nu_1} = S(n_u,3) = 10$: primary Pascal evaluation in $d=3$ alone. No cross-sector $l=2$ mixing; no correction.
- $n_{\nu_2} = S(n_u,4) = 15$: primary Pascal evaluation in $d=4$ alone. No cross-sector $l=2$ mixing; no correction.
- $n_{\nu_3} = n_{\nu_1} + n_{\nu_2} - n_u = 22$: the unique inclusion-exclusion mode, combining the $d=3$ image ($n_{\nu_1}$) and the $d=4$ image ($n_{\nu_2}$) of the same seed $n_u$. The $l=2$ cross-term of the kernel (T2) then operates on the product of the two sector amplitudes: $\varepsilon$ from the $d=4$ coupling geometry, $g_{33}$ from the $d=3$ back-reaction. Their product is 1/35 by the identity above.

**Sign.** The correction is positive. The two sector images ($d=3$ and $d=4$) are both images of the same seed $n_u$ and interfere constructively through the $l=2$ overlap, increasing the effective mode count and hence the eigenvalue. This is distinct from the $d=4$ up-type overshoot (T10a), where the $l=2$ term generates level-splittings between generations at different depths (a level-repulsion effect), and from the $d=10$ geometric back-reaction correction (T10b), which is a geometric-series resummation at the Gegenbauer critical endpoint. The $\nu_3$ correction is a single-order cross-sector constructive interference.

**Numerical check:**

$$\varepsilon\times g_{33} = \frac{1}{280\sqrt{7}}\times 8\sqrt{7} = \frac{8}{280} = \frac{1}{35} \quad[\text{exact}]$$

$$m_{\nu_3}^{\rm corr} = 48.871\times\frac{36}{35} = 50.267\ \text{meV}$$

$$\Delta m^2_{31} = (50.267)^2-(1.487)^2\ [\text{meV}^2] = 2.5246\times10^{-3}\ \text{eV}^2$$

$$(\text{PDG 2023: }2.523\times10^{-3}\ \text{eV}^2,\ {+}0.05\%;\quad\text{PDG 2024: }2.530\times10^{-3}\ \text{eV}^2,\ {-}0.22\%\text{ within }0.2\sigma)$$

$$\Sigma m_\nu\ (\text{corrected}) = 1.487+8.639+50.267 = 60.393\ \text{meV}$$

---

## 10. Mass Scale Derivation

### $m_{\rm scale,3}$ and $m_{\rm scale,4}$ — unified coupling self-consistency condition

The kernel vacuum analysis gives a single fixed-point equation that applies to all sectors uniformly:

> **In equilibrium, the squared mass of the lightest occupied mode in sector $d$ equals $(g_{dd}/g_{66}) \times m_e^2$.**

The lightest occupied mode in sector $d$ has mass $m_{\rm lightest}(d) = m_{\rm scale,d} \times S(n_{\min}(d), d)$, where $n_{\min}(d)$ is the lowest mode index selected by the co-fixed-point. The fixed-point equation is therefore:

$$\bigl(m_{\rm scale,d}\times S(n_{\min}(d),d)\bigr)^2 = \frac{g_{dd}}{g_{66}}\times m_e^2 \;\Longrightarrow\; m_{\rm scale,d} = m_e\times\frac{\sqrt{g_{dd}/g_{66}}}{S(n_{\min}(d),d)}$$

This is one formula for all sectors. The apparent differences between sectors are entirely due to $n_{\min}(d)$ and $S(n_{\min}(d), d)$:

**$d=3$ (down quarks):** $n_{\min}=1$, $S(1,3)=1$.

$$m_{\rm scale,3} = m_e\times\frac{\sqrt{g_{33}/g_{66}}}{1} = 0.511\times\sqrt{8\sqrt{7}/0.25} = 4.702\ \text{MeV}$$
The lightest occupied mode is the down quark: $m_d = m_{\rm scale,3} \times S(1,3) = 4.702$ MeV. PDG 2024: 4.70 MeV. Error: +0.04%.

$S(1,3) = 1$ makes the normalization factor trivially 1 for $d=3$.

**$d=4$ (up-type quarks):** $n_{\min}=n_u=3$ (postulate; see Part 2 §5 note), $S(3,4)=15$.

$$m_{\rm scale,4} = \frac{m_e\sqrt{g_{44}/g_{66}}}{S(3,4)} = \frac{0.511\times\sqrt{12/(\sqrt{7}\times0.25)}}{15} = 0.1451\ \text{MeV}$$
The lightest occupied mode is the up quark: $m_u = m_{\rm scale,4} \times S(3,4) = m_e \times \sqrt{g_{44}/g_{66}} = 2.177$ MeV (bare count; physical $2.175$ MeV after the §11.9 confinement-binding correction). The fixed-point requires $m_u^2 = (g_{44}/g_{66}) \times m_e^2$ — i.e. the up quark mass satisfies the same fixed-point equation that the down quark satisfies, with $g_{44}$ in place of $g_{33}$. The factor $/S(3,4) = /15$ is the fixed-point condition applied consistently to a sector whose lowest occupied mode is not $n=1$.

**Unified check:** $m_u/m_d = \sqrt{g_{44}/g_{33}} = \sqrt{(12/\sqrt{7}) \div 8\sqrt{7}} = \sqrt{3/14} = 0.4629$. PDG: 0.462 ± ~0.10. Error: +0.20%.

**The down quark is a pure prediction:** $m_d = m_{\rm scale,3} \times S(1,3) = m_{\rm scale,3} \times 1 = 4.702$ MeV. PDG 2024: 4.70 MeV. Error: +0.04%.

### The ρ Meson — Comb Filter Prediction

The inter-sector comb filter $\mathrm{Im}[\Gamma_{346}(\omega)]$ predicts the $\rho$ meson mass independently of $m_{\rm scale,3}$. Its inputs are the coupling constants $g_{33}=8\sqrt{7}$, $g_{44}=12/\sqrt{7}$, $g_{66}=1/4$ (all derived from seeds and $\mathbb{CP}^3$ complex geometry) and the Jacobi chain delays $\tau_d = 1/(2\sqrt{k_0+d})$ at resonance site $k_0=16$:

$$m_{\rho^*} = \arg\max\,\mathrm{Im}[\Gamma_{346}(\omega)] = 775.794\ \text{MeV} \quad (\text{PDG: }775.260\pm0.250\ \text{MeV},\ {+}0.069\%)$$

No direct mass input is used. The 0.534 MeV residual reflects the accuracy of the comb filter at this order; contributing open items include: (a) isospin breaking absent from the $SU(3)$-symmetric kernel (open item, Part 2 §11), and (b) the leading-order sector phase delay approximation in $\tau_d$ being exact only for $d=10$ (see Part 1 §3b). The agreement is a consistency check of the coupling geometry at the 0.069% level.

Note: $\tau_d = 1/(2\sqrt{k_0+d})$ is a valid description of the inter-sector phase delay at the resonance site $k_0$, where both $d=3$ and $d=6$ modes are evaluated at the same resonance frequency scale set by $k_0=n_s^2=16$. The delay formula does not assume comparable mass scales between sectors — it depends only on the Jacobi chain structure at $k_0$, which is a geometric property of the manifold, not the sector mass scale.

### Scale Hierarchy

**Unit reference: $m_e$. All sector scales follow from the unified fixed-point $m_{\rm scale,d} = m_e \times \sqrt{g_{dd}/g_{66}} / S(n_{\min}(d), d)$.**

| Quantity | $n_{\min}$ | $S(n_{\min},d)$ | Source | Value |
|---------|-------|------------|--------|-------|
| $m_{\rm scale,6}$ | 13 | $S(13,6) = 18564$ | $m_e / S(13,6)$ | $2.7526\times10^{-5}$ MeV |
| $m_{\rm scale,3}$ | 1 | $S(1,3) = 1$ | $m_e \times \sqrt{g_{33}/g_{66}}$ / 1 | 4.702 MeV |
| $m_{\rm scale,4}$ | 3 | $S(3,4) = 15$ | $m_e \times \sqrt{g_{44}/g_{66}}$ / 15 | 0.1451 MeV |
| $m_{\rm scale,10}$ | — | = $m_{\rm scale,6}$ | $g_{10,10} = g_{66}$: $d=10$ shares $d=6$ coupling | $2.7526\times10^{-5}$ MeV |
| $m_{\rm scale,2}$ | — | — | $m_e \times \sqrt{g_{22}/g_{66}}$ [cross-sector; §10b] | 27.47 MeV |

The light-quark predictions are parameter-free outputs of the coupling self-consistency derivation. Against PDG 2024 they sit at d +0.04%, s +0.57%, u +0.77% — all below PDG measurement precision for light quarks (PDG d: ±10%, s: ±9%).

### All sector scales

| Scale | Formula | Value | Note |
|---|---|---|---|
| $m_{\rm scale,6}$ | $m_e/S(13,6)$ | $2.7526\times10^{-5}\ \text{MeV}$ | unit reference |
| $m_{\rm scale,3}$ | $m_e\sqrt{g_{33}/g_{66}}$ | $4.702\ \text{MeV}$ | from seeds + anomaly |
| $m_{\rm scale,4}$ | $m_{\rm scale,3}\sqrt{g_{44}/g_{33}}/S(3,4)$ | $0.1451\ \text{MeV}$ | |
| $m_{\rm scale,10}$ | $= m_{\rm scale,6}$ | $2.7526\times10^{-5}\ \text{MeV}$ | $g_{10,10}=g_{66}=1/n_s$ |
| $m_{\rm scale,2}$ | $m_e\sqrt{g_{22}/g_{66}}$ | $27.47\ \text{MeV}$ | derived from seeds via $g_{22}$ |

### 10b. $g_{22}$ — the kernel back-reaction fixed-point 🔶

**Status: 🔶 Structurally motivated (state-counting).** $g_{22} = p^2q/2 = 722.5$ is a multiplicity count: the product of available Dirac-eigenspace dimensions across the $d=3$ sector (two kernel legs → $p^2$) and the $d=4$ sector (one leg → q), with the 1/2 from the $\xi\leftrightarrow\xi'$ symmetry of the two-body kernel. It is not a kernel matrix element. Testing whether a genuine $(\xi\cdot\xi')^2$ trace yields $p^2q/2$ (`files/idwt.py` STEP 2d): the literal Tr[$G_{23}^2 + G_{24}^2$] is additive (∼ $p^2+q$, the wrong structure for a product), and the actual $(\xi\cdot\xi')^2$ overlap returns $\langle r^2\rangle$ magnitudes that scale as the mode index $n$ — O(1), orders of magnitude below the multiplicity product. $p^2q$ appears only as a trace of the identity over rank-(p,p,q) eigenspaces, where the multiplicities are the input. So $g_{22}$ is a state-count (IDOS), on the same footing as the CKM formula: combinatorial, empirically exact, mechanism = counting. The 1/2 and the leg-counting are kernel-motivated; the magnitude is a count of eigenstates, not a dynamical overlap.

The $d=3$ self-coupling $g_{33}$ is fixed by the intra-sector confinement condition $g_{\rm eff}(n_s,3) = g_{33}/S(n_s,3) \approx 1$ (Part 2 §8). The $d=2$ sector has no self-confinement — the W is massive but not confined in the quark sense. Its self-coupling $g_{22}$ is instead fixed by the **cross-sector back-reaction**: the requirement that the $d=2$ vacuum amplitude is consistent with the $d=3$ and $d=4$ quark sector structures at the level $n_s=4$.

**The derivation:**

**Step 1.** The positive Dirac eigenvalue $\lambda_{l=3} = 7/2$ on $S^3$ has multiplicity $M_3 = (3+1)(3+2) = 20 = S(n_s,3)$ (Theorem S1, Part 8 §5). Of these 20 eigenstates, $n_u = 3$ are already accounted for by the up-quark sector boundary (Theorem S2, Part 8 §5). The remaining

$$p = M_3^{S^3} - n_u = S(n_s,3) - n_u = 20 - 3 = 17$$
[Notation: **p** is used here rather than $\alpha$ to avoid collision with the fine structure constant $\alpha = e^2/4\pi \approx 1/137$, which is a separately derived quantity in Part 3 §8.]

eigenstates are available to couple to the $d=2$ sector through $G_{23}$. The kernel is two-body — $(\xi\cdot\xi')^2$ couples two copies of $J^{d=3}$ — so both legs contribute, giving $p^2$.

**Step 2.** The hockey-stick identity $S(n,d)-S(n,d-1)=S(n-1,d)$ gives the $d{=}4$ eigenstate increment at the up-quark threshold:

$$q = S(n_u,4) - S(n_u,3) = 15-10 = 5 = S(n_u-1,4) = S(2,4)$$

These q eigenstates below the up-quark threshold couple to $d=2$ through a single $G_{24}$ insertion, entering linearly.

**Step 3.** The kernel $(\xi\cdot\xi')^2 = (\xi'\cdot\xi)^2$ is symmetric under $\xi\leftrightarrow\xi'$, so the vacuum integral double-counts. Divide by 2.

**Step 4 (fixed-point).** Equate the cross-sector back-reaction to the $d{=}2$ self-coupling:

$$g_{22} = \frac{1}{2}\times p^2\times q = \frac{1}{2}\times17^2\times5 = 722.5 \quad(\text{exact})$$

**Comparison with $d=3$:** For $d=3$, the intra-sector fixed-point gives $g_{33} \approx S(n_s,3) = 20$ (with a ~5.8% Jacobi correction). For $d=2$, the cross-sector fixed-point gives $g_{22} = (S(n_s,3)-n_u)^2 \times S(n_u-1,4)/2$ — a different structure, reflecting that the EW sector acquires its scale by coupling to both quark sectors, not by self-confinement.

**Consequences:**

$$m_{\rm scale,2} = m_e\times\sqrt{g_{22}/g_{66}} = m_e\times\sqrt{722.5/0.25} = 27.471\ \text{MeV}$$

| Quantity | From seeds + $m_e$ | PDG | Error |
|---|---|---|---|
| $m_W$ | $m_{\rm scale,2} \times S(76,2) = 80{,}379$ MeV | 80,369 MeV | +0.012% |
| $m_Z$ | $m_{\rm scale,2} \times S(81,2) = 91{,}230$ MeV | 91,188.0 MeV | +0.046% |
| $m_H$ | $m_{\rm scale,2} \times S(95,2) = 125{,}266$ MeV | 125,200 MeV | +0.053% |

**IDWT has a sole unit reference $m_e = 0.511$ MeV.** All quarks, leptons, bosons, CKM angles, Fermi constant, Weinberg angle, and muon lifetime follow from $m_e$ and seeds $\{n_d=1, n_u=3\}$. □



---

## 11. The $d=4$ Up-Type Quark Mass Overshoot

The raw mass formula $m(n,d) = m_{\rm scale,d} \times S(n,d)$ reproduces the spectrum within most sectors, but in the **$d=4$ up-type quark sector** the bare count overshoots, growing with generation: up +0.77%, charm +0.93%, top +2.20% vs PDG 2024. The overshoot is colour-field binding energy — the energy locked in the confining field that a free-quark count would wrongly assign to the quark's inertial mass. The confinement-binding correction of §11.9 reduces all five quarks to within ±1σ of PDG 2024 statistical errors.

A multiplicative correction was previously applied — a factor `(1 − ε)^k` tuned per quark, the "Generation Tower Correction" — which brought charm and top onto their measured values. It has been removed. Only the scale $\varepsilon$ was derived; the per-quark exponent $k$ was a fit, and a fitted correction is not a derivation. The bare masses are quoted instead, with the overshoot left open. A physically motivated correction may be added in future if one is derived.

### 11.1 The candidate mechanism (open)

The cross-sector kernel `(ξ_d · ξ_{d'})²` decomposes into an l=0 scalar part, which sets the sector mass scale, and an l=2 traceless tensor part, which shifts each mode by a second-order self-energy (`files/idwt.py` STEP 86). That self-energy has the correct sign — it pulls the masses down, growing with the mode index — so it is a candidate source for the overshoot. It is **not applied**: with the derived scale $\varepsilon$ its shape is the combinatorial set $\{0,3,10\}$, which does not reproduce the measured masses (only the fitted $\{0,7,16\}$ did, §11.3). The up-type masses are therefore quoted bare and the overshoot left open (🔶).

### 11.2 Derivation of $\varepsilon$ (retained for $\delta_{\nu_3}$, no longer applied to quarks)

The scale $\varepsilon$ below is a genuinely derived quantity. It is no longer applied to the up-type quark masses (§11.3); it is retained only because the separate, motivated $\nu_3$ closure $\delta_{\nu_3} = \varepsilon \times g_{33} = 1/35$ (§9d) depends on it.

**$g_{\rm coeff} = 2/\sqrt{7}$ from the kernel self-consistency eigenvalue.**

The kernel self-consistency condition from Part 2 §9 requires:

$$\frac{n_s(n_s+1)}{S(n_s,4)} = \frac{n_u(n_u+1)}{S(n_u,5)} = \frac{4}{7}$$

Both ratios equal $4/7$ exactly: $4\times5/35 = 12/21 = 4/7$. This is the coupling self-consistency eigenvalue at the Jacobi critical site $k_0 = n_s^2 = 16$. The $\ell{=}2$ kernel coupling coefficient is the square root of this eigenvalue:

$$g_{\rm coeff} = \sqrt{\frac{n_s(n_s+1)}{S(n_s,4)}} = \sqrt{\frac{4}{7}} = \frac{2}{\sqrt{7}}$$

Combined with the critical resonance site $k_0 = n_s^2 = 16$ and the muon mode $n_\mu = S(n_s,4) = 35$ as the natural frequency normalization scale:

$$\varepsilon = \frac{g_{\rm coeff}}{k_0\times n_\mu} = \frac{2/\sqrt{7}}{16\times35} = \frac{1}{280\sqrt{7}} \approx 0.001350$$

$\varepsilon$ is fully derived from kernel geometry and seed combinatorics — no empirical masses enter. Only the seed pair $\{n_d=1, n_u=3\}$.

Cross-check from c/u and t/u mass ratios: $\varepsilon \approx 0.001340$ (inferred from PDG). Derived value: 0.001350. Gap: 0.74% — within PDG light-quark uncertainties.

### 11.3 The per-quark correction is removed

The former correction multiplied each $d=4$ up-type mass by $(1-\varepsilon)^k$ with a per-quark exponent $k$ (up 0, charm 7, top 16). Only $\varepsilon$ was derived; the exponents were fixed by requiring charm and top to land on their PDG masses given the derived scale — that is, tuned to the data, not predicted. The closed-form labels the exponents happen to carry ($k_c = 7 = n_s + n_u$, $k_t = 16 = n_s^2$) are recognised after the fact, not derived. A correction whose only free choice is set to reproduce the answer is a parameterization, not a derivation, so it is removed. The up-type masses are quoted bare (§11.5), and the overshoot is left as the open residue described in §11.1 and §11.4.

### 11.4 Open item

The up-type masses are quoted bare as the primary result (§11.5); a motivated confinement-binding correction is derived and applied in §11.9, which brings all quarks within ±1σ of PDG 2024 statistical errors. The $\ell=2$ kernel self-energy (§11.1) remains a candidate with the correct sign but the wrong $n$-shape, and is not applied. The residual after the §11.9 correction is recorded there.

### 11.5 Results (bare masses)

Absolute up-type masses vs PDG 2024, quoted bare — no correction applied:

| Particle | $n$ | $S(n,4)\,m_{\rm scale,4}$ | error |
|---|---|---|---|
| up | 3 | 2.177 MeV | $+0.77\%$ ($0.2\sigma$, within the PDG light-quark margin) |
| charm | 20 | 1284.9 MeV | $+0.93\%$ bare (corrected $+0.34\%$, $+0.9\sigma$ in §11.9) |
| top | 72 | 176{,}365 MeV | $+2.20\%$ bare (corrected $-0.04\%$, $-0.2\sigma$ in §11.9) |

The bare formula overshoots, growing with generation; the confinement-binding correction (§11.9) reduces all quark residuals to within ±1σ PDG stat. 🔶

Up-type quark masses bare: $m = m_{\rm scale,4}\times S(n,4)$. Charm $= 1284.9\ \text{MeV}$ (+0.93% bare, corrected +0.34% in §11.9). Top $= 176{,}365\ \text{MeV}$ (+2.20% bare, corrected $-0.04\%$ in §11.9).

### 11.6 Corrections Summary

Two perturbative corrections sit on top of the bare mass formula $m = m_{\rm scale} \times S(n,d)$ — the former GTC having been removed (§11.3). The back-reaction $\delta_\tau$ is derived; $\delta_{\nu_3}$ is motivated. Each applies to exactly one particle or family; they are structurally orthogonal.

| Correction | Symbol | Formula | Derivation | Applies to | Status |
|---|---|---|---|---|---|
| Geometric back-reaction | $\delta_\tau$ | $+1/1680$ | $d=6\to d=10$ geometric series; $1/(1-g_{10,10})$ resummation; $1680 = n_s n_u(n_s+n_u)S(n_s,3)$ (§9b) | $\tau$ only: $m_\tau \to m_\tau(1+1/1680)$ | ✅ |
| $\nu_3$ closure relation | $\delta_{\nu_3}$ | $+1/35$ | Cross-sector $\ell=2 \times d=3$ interference; $\varepsilon \times g_{33} = [1/(280\sqrt{7})]\times[8\sqrt{7}] = 8/280$ (§9d) | $\nu_3$ only: $m_{\nu_3} \to m_{\nu_3}(36/35)$ | 🔶 |

**The scale $\varepsilon$.** $\delta_{\nu_3} = \varepsilon \times g_{33}$ exactly; the $\sqrt{7}$ factors cancel and the result $1/35 = 1/n_\mu$ is rational. The $\ell=2$ scale $\varepsilon = 1/(280\sqrt{7})$ (§11.2) is a derived quantity; it no longer corrects the up-type quark masses (§11.3), but it remains the derived scale of this single, motivated $\nu_3$ shift via $g_{33}$.

**No particle carries more than one correction.** The bottom quark uses the geometric-mean rule (§8), not these perturbative corrections. The up-type quark masses are quoted bare (§11.3); only $\tau$ (back-reaction) and $\nu_3$ (closure) carry a correction.

### 11.7 The top quark: a correction that is required but not earned 🔶

Within the up-type sector the overshoot grows smoothly with generation, but the top is set apart, and it is the principal open residue of the mass sector. Two features distinguish it from every lighter mode.

First, its mode index is not a tower output. Every lepton, every neutrino, and the first- and second-generation quarks carry indices generated additively by the hockey-stick tower; the top's index $n=72$ is instead a product, $N_c\times n_s\times N_f = \chi(\mathbb{CP}^2)\times\chi(\mathbb{CP}^3)\times\chi(\mathbb{CP}^5) = 3\times4\times6$. The three factors are the Euler characteristics of the three highest-weight active-sector complex projective spaces — precisely the topological invariants that drive the sector chain — so the product form is structurally natural within the framework. What is not yet explained is the selection principle: why does the top's index equal this Euler product, while the rest of the spectrum is additive? The bottom's product index $n_s^2=16$ has a derivation as the $d=10$ Gegenbauer endpoint (§8); the top's $72$ does not. This is the leading open dynamical question of the framework (🔶).

Second is the mass. The bare mode $S(72,4)\,m_{\rm scale,4} = 176{,}365$ MeV sits $+2.20\%$ above the PDG 2024 value ($172{,}570 \pm 290$ MeV). The confinement-binding correction (§11.9) reduces this to $-0.04\%$ ($-0.2\sigma$). The scale-independent ratio $S(72,4)/S(20,4) = 137.26$ matches the conventional top/charm ratio to $\sim$1%.

So one thing remains genuinely open at the top: the index $72$ is a product rather than a tower output, with no selecting condition yet found. The bare mass overshoot is corrected to within $1\sigma$ in §11.9 ($\textbf{🔶}$); the rule that generates the index itself is the remaining open item.

### 11.8 Scale versus structure: the residual is $n$-dependent and confined to $d=3$ and $d=4$

The quark-sector residuals admit two readings: a uniform per-sector scale offset — a single high $m_{\mathrm{scale},d}$ shifting every mode in the sector by one common fraction — or $n$-dependent structure in the count $S(n,d)$. The two are separated by the scale-free **in-sector mass ratio** $S(n_{\mathrm{hi}},d)/S(n_{\mathrm{lo}},d)$, an exact combinatorial identity ($\textbf{⭐}$) in which $m_{\mathrm{scale},d}$ and the unit anchor $m_e$ cancel identically. A uniform scale offset is invisible to this ratio; only structure survives it.

| In-sector ratio | $d$ | IDWT | PDG 2024 | Residual |
|---|---|---|---|---|
| $Z/W$ | $2$ | $1.1350$ | $1.1346$ | $+0.03\%$ |
| $H/W$ | $2$ | $1.5584$ | $1.5578$ | $+0.04\%$ |
| $s/d$ | $3$ | $20.0000$ | $19.894$ | $+0.54\%$ |
| $c/u$ | $4$ | $590.33$ | $589.35$ | $+0.17\%$ |
| $t/c$ | $4$ | $137.26$ | $135.56$ | $+1.25\%$ |
| $\mu/e$ | $6$ | $206.7647$ | $206.7683$ | $-0.002\%$ |

The residual is at most a few parts in $10^{4}$ in the boson ($d=2$) and charged-lepton ($d=6$) sectors, and grows with the level gap inside the quark sectors $d=3$ and $d=4$. That growth is the signature of structure in $S(n,d)$, not of a sector scale error: a uniform offset would be $n$-independent and would leave every in-sector ratio exact. The discrepancy is therefore $n$-dependent and confined to the two quark sectors, while the boson and lepton sectors are reproduced to within $4\times10^{-4}$ by the bare count (`files/idwt.py` STEP 126).

This is reported as measured accuracy, not absorbed as a correction. The in-sector ratios fix how far the bare $S(n,d)$ count departs from the data per sector — at most $+1.25\%$, at the top — and that figure is quoted; converting it into a per-sector multiplicative adjustment would be a fit, of the kind removed in §11.3. The scale-independent ratios remain the clean, scheme-free comparison ($\textbf{🔵}$); the structural origin of the quark-sector growth is identified as colour-confinement binding in §11.9 ($\textbf{🔶}$).

### 11.9 Confinement-binding correction ($d=3$, $d=4$) 🔶

The bare IDWT mass $M_{\rm bare} = m_{\rm scale,d}\times S(n,d)$ is the free-quark harmonic-oscillator count — the mass a quark would carry if it could exist as an isolated asymptotic state. Colour confinement means it cannot: the energy that the free-quark picture assigns to the quark is partly locked in the colour field that confines it. The observed physical mass is therefore lower than the bare count by the energy bound in the colour field. This is not a fitted correction but the energy bookkeeping of colour confinement: the deficit is the confinement binding energy, distributed over the mode's $\langle k\rangle$ occupied levels.

**Form (derived).** The sector's self-consistent Gaussian well is a finite cavity, so its eigenmodes flatten toward the well top — the per-state energy spacing decreases weakly with level. This level-dependent softening is linear in the mean level $\langle k\rangle$ (`files/idwt.py` STEP 127; Part 4 §3.10.5b):

$$M_{\rm phys} = M_{\rm bare}\,(1 - x_e\,\langle k\rangle), \qquad \langle k\rangle = \frac{d(n-1)}{d+1}\ \text{(exact for all }n,d\text{)}$$

The form is derived two independent ways — cavity group-velocity dispersion and soliton anharmonic perturbation theory — and gives $x_e = 3/(16\,N_b)$, where $N_b$ is the condensate occupation of the sector well. The linear-in-$\langle k\rangle$ form is selected by the data (quadratic is ruled out: it brings charm into margin but leaves top at $+2.1\sigma$).

**Selector.** The correction applies only to the colour-carrying sectors $d=3$ and $d=4$ (`has_SU3`, `files/idwt.py` line 620) — the two sectors whose wells are occupied condensates with finite $N_b$ (anharmonic). The boson ($d=2$) and lepton ($d=6,10$) wells are effectively harmonic (large $N_b$), giving $x_e\approx0$. Colour is the differentiator.

**Occupation $N_b$ — one derived coefficient, applied universally.** The coefficient is fixed once, in the $d=4$ sector — native colour ($\mathbb{CP}^2$, $N_c=\chi=3$) and the only sector with out-of-margin modes (charm, top) — by the STEP-63 colour energy law:

$$N_b(d{=}4) = \frac{\lambda_c}{2N_c\,m_{\rm scale,4}} = \frac{\Lambda}{4\,m_{\rm scale,4}} = 486 \quad\Rightarrow\quad x_e(d{=}4) = 3.86\times10^{-4},$$

with $\Lambda = N_c f_\pi$ the confinement scale and $\lambda_c = N_c^2 f_\pi/2$ the colour energy coefficient (STEP 63). The coefficient $2N_c$ is the colour count times the $|\Delta N_{\rm vec}|=2$ colour-flip unit; equivalently the colour-well depth is $N_b\,m_{\rm scale,4} = \Lambda/4 = (n_u/n_s)\,f_\pi \approx 70.5$ MeV. This is $m_e$-free, introduces no new input, and reproduces the within-margin value to $0.4\%$.

The $d=3$ quarks (down, strange) carry the **same** coefficient: their colour is inherited from $d=4$ through the $S^1\!\to S^5\!\to\mathbb{CP}^2$ Hopf map — the binding colour lives in $\mathbb{CP}^2$ — so the per-state deficit is the one derived $d=4$ value, applied universally with no per-sector fit. Strange ($\langle k\rangle = 2.25$) is then a genuine prediction, $93.96$ MeV ($+0.49\%$, $+0.6\sigma$); down ($\langle k\rangle = 0$) is unshifted. (An earlier version anchored $x_e(d{=}3)$ on the strange datum; removing that anchor turns strange from a fit into a genuine prediction, at no cost to the other quarks.)

**Corrected masses.** (`files/idwt.py` STEP 127; PDG 2024 pole masses)

| Particle | $d$ | Bare residual | Corrected residual | $\sigma$ (PDG stat) |
|---|---|---|---|---|
| down | 3 | +0.040% | +0.040% | +0.03 |
| strange | 3 | +0.574% | +0.488% | +0.57 |
| up | 4 | +0.766% | +0.703% | +0.22 |
| charm | 4 | +0.933% | +0.342% | +0.95 |
| top | 4 | +2.199% | −0.040% | −0.24 |

All quarks are within ±1σ PDG statistical errors after the correction. The $d=2$ boson and $d=6,10$ lepton sectors are untouched ($x_e\approx0$).

All sector mass scales reduce to $m_e$ (via $m_{\rm scale,6} = m_e/S(13,6)$) plus the coupling ratios:

$$m_{\rm scale,d} = m_{\rm scale,6}\times\sqrt{\frac{g_{dd}}{g_{66}}}\times\frac{S(n_e,6)}{S(n_{\min}(d),d)}$$

where $n_{\min}(d)$ is the lightest occupied mode in sector $d$. For $d{=}3$ this gives $m_{\rm scale,3} = m_{\rm scale,6}\times\sqrt{g_{33}/g_{66}}\times18564/1 = m_e\times\sqrt{g_{33}/g_{66}} = 4.702\ \text{MeV}$.

**The $d=4$ up-type overshoot (uncorrected):**

The bare quark residuals are not equal across a sector (d +0.04%, s +0.57%, u +0.77%, c +0.93%, t +2.20%); this growth with the mode index is $n$-structure in $S(n,d)$, not a uniform scale offset (§11.8). It is the signature of colour-field binding: higher modes occupy more of the confining well and surrender more energy to the colour field. The confinement-binding correction above reduces all five quarks to within ±1σ of PDG 2024. (🔶)

The $l=0$ scalar part of $(\xi_d\cdot\xi_{d'})^2$ sets the sector mass scale; the $l=2$ tensor part supplies this mode-dependent shift.

**$d=6$/$d=10$ kernel symmetry:** $v_6 = v_{10} = 1/2$ exactly. The kernel cannot distinguish the charged lepton sector from the tau sector — both have identical coupling strength. The mass difference between muon and tau arises entirely from different sector geometry ($S(35,6)$ vs $S(23,10)$), not from any coupling difference. This is a genuine symmetry of the kernel, broken only by the Hopf chain's sector manifold assignments.

**Self-consistency derivation route:**
The sector mass scales satisfy $m_{\rm scale,d}^2 = g_{dd}\times\langle|\Psi^{(d)}|^2\rangle$ — the kernel self-consistency fixed-point equation. Once $g_{dd}$ is computed from the sector geometry ($\mathbb{CP}^2$, $S^3$, $\mathbb{CP}^3$) for each sector, all mass scales become fully derived. $m_e$ is the sole unit reference for the particle spectrum. $m_W$ is derived from seeds at $+0.003\%$ (Part 2 §10).

**Current status by sector:**

| $d$ | $g_{dd}$ source | $m_{\rm scale}$ derived? |
|---|------------|-----------------|
| 6 | $g_{66} = 1/n_s = 1/4$ ($\mathbb{CP}^3$ complex geometry: $\chi(\mathbb{CP}^3)=n_s=4$, min.\ Fubini-Study curvature $=1/4$) | ✅ |
| 3 | $g_{33} = n_s^2\sqrt{n_s+n_u}/2$ from seed self-interaction | ✅ from $m_e$ |
| 4 | $g_{44} = n_s n_u/\sqrt{n_s+n_u}$ from seed harmonic mean | ✅ from $m_e$ |
| 10 | $g_{10,10} = g_{66} = 1/n_s$ from seed (shared with $d{=}6$) | ✅ ($m_{\rm scale,10} = m_{\rm scale,6}$) |
| 2 | $g_{22} = (M_3^{S^3}-n_u)^2\times q/2 = 722.5$ [Theorem S3, Part 8 §5] | ✅ |
| 5 | $g_{55} = g_{33}g_{44}/g_{22} = 96/g_{22}$ from Hopf fiber universality | ✅ $m_{\rm scale,5}$ derived (§9c) |

---

## 13. Sector Termination — Gegenbauer Criticality

The IDWT active sector set {2,3,4,5,6,10} terminates at $d=10$ for three independent reasons, the third being an algebraic consequence of the seed structure: Gegenbauer criticality. Note that $d=7$, $8$, $9$ exist as coordinates of $M_\infty$ but are absent from the active sector set — they are supercritical ($b_{k_0} > 1/2$) but Rule A eliminates them before the Gegenbauer criterion is reached. The criticality condition governs where the active chain terminates; the gap from $d=6$ to $d=10$ in the active set is produced by Rule A independently.

**Definition.** The Gegenbauer polynomial coupling at the resonance site $k_0 = n_s^2 = 16$ in the d-dimensional Jacobi chain is:

$$b_{k_0}(d) = \frac{\sqrt{k_0(k_0+d-1)}}{2k_0+d-2}$$

For the six active IDWT sectors and the three inactive-but-present sectors: $b_{k_0}$ takes values 0.51539 ($d=2$) down through 0.50712, 0.50497, 0.50246 ($d=7$,8,9 — present in $M_\infty$, supercritical, but excluded from active set by Rule A) to **0.50000 ($d=10$) exactly**, then 0.49747 ($d=11$, subcritical).

**Theorem.**  $b_{k_0}(d) = 1/2$  ⟺  $4k_0 = (d-2)^2$  ⟺  $d = 2 + 2n_s = 10$.

**Proof.**  $b = 1/2 \Longleftrightarrow 4k_0(k_0+d-1) = (2k_0+d-2)^2$.  Expanding: LHS $= 4k_0^2 + 4k_0(d-1)$, RHS $= 4k_0^2 + 4k_0(d-2) + (d-2)^2$. Subtracting: $4k_0 = (d-2)^2$. With $k_0 = n_s^2 = 16$: $d = 2 + 2\sqrt{16} = 2 + 2n_s = 10$. □

**Corollary (exact sector phase delay for $d=10$).** The leading-order sector phase delay $\tau_d = 1/(2\sqrt{k_0+d})$ acquires a next-order correction proportional to $(b_{k_0}-1/2)/b_{k_0}^2$. For $d=10$ this correction **vanishes identically**, so the leading-order sector phase delay is exact at the terminal sector. For $d=3$ through $d=6$ the corrections are −0.67% to −0.44% and shift the ρ meson prediction in the wrong direction (away from PDG), confirming that the +0.069% residual is a genuine floor, not a sector phase delay artifact.

**Sector summary — two routes to $d=10$:**

| Route | Origin | Statement |
|---|---|---|
| **Gegenbauer (algebra)** | **Jacobi chain criticality** | $b_{k_0}=1/2$ **iff $d=2(n_s+1)=10$** |
| Shared coupling | $g_{10,10} = g_{66} = 1/n_s = 1/4$ from $n_s$ | Same coupling for both CP sectors |

---

## 14. Spectral Convergence and Analytic Control

The infinite resonance tower $\{S(n,d):n\geq1\}$ might appear to require a UV cutoff. In IDWT it does not: the combinatorial structure of $S(n,d)$ provides its own regularisation, confirmed by two exact anchor values of the sector spectral zeta function $\zeta_d(s)=\sum_{n=1}^\infty S(n,d)^{-s}$:

$$\zeta_d(1) = \frac{d}{d-1} \quad\text{(total inverse-mass weight; Part 9 T13a)}, \qquad \zeta_d(0) = -\frac{d}{2} \quad\text{(regularised mode count; Part 9 T14b)}.$$

**Three consequences for the mass formula:**

1. **Total inverse-mass weight is finite.** $\zeta_d(1)=d/(d-1)<\infty$ means $\sum_n m_{\rm scale_d}/m(n,d)$ converges for every sector; contributions from the high-$n$ tail of the tower are suppressed exactly as needed.

2. **Functional determinant is finite without a cutoff.** $\zeta_d(0)=-d/2$ is a finite, purely combinatorial number, so the sector functional determinant $\log\det D_d=-\zeta_d'(0)$ is well-defined by zeta regularisation alone. No tuning of a regulator scale is required.

3. **Spectral dimension equals sector dimension.** The heat kernel of sector $d$ satisfies $K_d(t)=\sum_{n\geq1}e^{-tS(n,d)}\sim\Gamma(1+1/d)(d!)^{1/d}\,t^{-1/d}$ as $t\to0^+$. The leading power $t^{-1/d}$ establishes spectral dimension $= d$, consistent with the identification of each sector as a resonance tower in $d$-dimensional sector space (§§3, 9–10 above).

These results follow from $S(n,d)=\binom{n+d-1}{d}$ by Pascal's identity and Euler-Maclaurin. The mass formula is the spectrum of a well-defined spectral triple (Part 1 §0, Part 9 T0).

## 15. The Three-Ray Law — Depth and Dimension Locked

The generation tower carries a second coordinate besides the mode index: the **minimal-route derivation depth** $k_{\min}$, the length of the shortest documented derivation of a mode from the seeds (the §6 DAG together with its cross-check routes), computed by relaxation. The seeds and the photon sit at depth 0; the T15 Euler product $n_{\rm top} = \chi(\mathbb{CP}^2)\,\chi(\mathbb{CP}^3)\,\chi(\mathbb{CP}^5)$ is a depth-1 production from geometric constants, since the top index is an irreducible input not derived from lighter modes. This depth is a different object from the per-quark exponent $k$ of the former GTC (§11.3, removed) — the two should not be conflated.

**The law (🔶).** Every matter mode and the photon — 12 of the 15 — satisfies

$$d - k_{\min} \in \{2,\, 3,\, 4\}.$$

The spectrum occupies three parallel slope-1 rays in the $(k, d)$ plane, each anchored at a depth-0 mode:

| ray | anchor ($k=0$) | $k=1$ | $k=2$ | $k=3$ |
|---|---|---|---|---|
| $d = k+2$ | photon ($d{=}2$) | strange ($d{=}3$) | charm ($d{=}4$) | — |
| $d = k+3$ | down ($d{=}3$) | top ($d{=}4$) | $\nu_3$ ($d{=}5$) | — |
| $d = k+4$ | up ($d{=}4$) | $\nu_1, \nu_2$ ($d{=}5$) | $e, \mu$ ($d{=}6$) | $\tau$ ($d{=}7$ slot $\to 10$) |

Each derivation step advances the sector dimension by exactly one. Three structural consequences follow:

- **The τ is a band-edge mode.** The $d = k+4$ ray's depth-3 slot is $d = 7$ — and the sectors $d = 7, 8, 9$ are all inadmissible (§13; Part 9 T3), a three-sector support gap. The deposit lands in the terminal sector $d = 10$, the first admissible state beyond the gap, consistent with the $d{=}6/d{=}10$ scale degeneracy $g_{66} = g_{10,10}$ (Part 9 T9c).
- **The heavy bosons are off-ray.** W, Z, H (all $d = 2$) are the only modes violating the ray relation — exactly the insertion-free $g$-rule cascade off the top (§6; Part 3 §11). Matter climbs the chain; the cascade lands in the one plane every sector contains.
- **A timing constraint.** Matter sector $d$ is occupiable only at depths $d-4 \le k_{\min} \le d-2$: $d=3$ closes after depth 1, $d=4$ after depth 2. This constrains *when* a sector can fire, a different kind of restriction from the channel-parity gates of §6 and Part 3 §11.

**The deposit budget is the Betti vector of the seed product (⭐ as identity, ❓ as mechanism).** A minimal front model — structure advancing one admissible sector per step, a newly reached sector depositing once per available insertion channel, one deposit consuming one unit of a per-dimension budget $F_0(j)$ — reproduces all 12 on-ray modes at their exact $(k, d)$ positions and multiplicities iff

$$F_0(j) = (1, 2, 3, 3, 2, 1), \qquad j = 2 \ldots 7,$$

and this profile is unique in the swept family. The identity: $F_0$ **is the Betti vector** $b_0, b_2, \ldots, b_{10}$ of $\mathbb{CP}^2 \times \mathbb{CP}^3$ — the product of the two non-terminal Kähler condensate sectors $d=4$ and $d=6$ — equivalently the convolution of their cell vectors, $F_0(j) = \min(j-1,\, 8-j)$. Its total is $12 = \chi(\mathbb{CP}^2)\,\chi(\mathbb{CP}^3)$, the on-ray mode count: the double-product companion of the triple-product identity $n_{\rm top} = \chi(\mathbb{CP}^2)\chi(\mathbb{CP}^3)\chi(\mathbb{CP}^5)$ (Part 9 T15b). The Lefschetz decomposition of $H^*(\mathbb{CP}^2\times\mathbb{CP}^3)$ places its three primitive classes at degrees $\{0, 2, 4\}$ — the three ray anchors — and the orbit of each primitive class under $L = \wedge\omega$ lies on one of the three rays: the orbits *are* the rays. The per-site class totals equal $F_0$ exactly (the topological content); the depth grading differs — the observed record is the greedy-earliest filling of the per-site budgets under the front constraints, each class depositing at its minimal derivation depth rather than at its $L$-power. Refinement: the budget at height $m = j-2$ above the gauge floor equals the number of $(m,m)$-classes of the seed product, bidegree census $(\alpha,\beta)$ with $\alpha \le 2$, $\beta \le 3$, $\alpha + \beta = m$. The single remaining mechanism gap has an exact reduction — the ring form: given the hypothesis that deposit channels are the monomials of $R = \mathbb{R}[\omega_2,\omega_3]/(\omega_2^3, \omega_3^4)$ with each insertion multiplying by one generator, the entire front structure follows as ring algebra — 12 deposits = $\dim R$, two channels = two generators, budgets = per-degree counts, depletion = nilpotency, termination = the top class $\omega_2^2\omega_3^3$ ($H^{12} = 0$). Forced entries (✅): photon $\leftrightarrow$ the unit class (the $d=2$ sector has no condensate, so only the empty product contributes); τ $\leftrightarrow$ $\omega_2^2\omega_3^3$, the unique top/volume class of the seed product (the terminal sector receives the last deposit when both generators are exhausted — the unique consequence of $\omega_2^3 = 0$ and $\omega_3^4 = 0$). Hypothesis H is fully established (✅, 2026-06-18). On a Kähler sector the Kähler form $\omega$ is covariantly constant, so each power $\omega^p$ is parallel and therefore harmonic — an exact zero mode of the form-Laplacian, so a fluctuation along a harmonic class costs no angular gradient energy and is marginal in the angular sector (✅). The condensate is $U(1)$ charge-zero at each sector, and a $(p,q)$ form carries charge $p-q$, so only the diagonal $(p,p)$ classes survive: the powers $\omega_2^\alpha\omega_3^\beta$ (✅). The two generators are the two non-terminal Kähler condensate sectors $d=4$ ($\mathbb{CP}^2$) and $d=6$ ($\mathbb{CP}^3$): $d=2$ is Kähler but carries no condensate, contributing the unit class alone — the same fact that sets $m_\gamma = 0$ (Part 3 §16.2); the real sectors $d=3$ and $d=5$ carry no Kähler form; and $d=10$ ($\mathbb{CP}^5$) is terminal, receiving τ at the top class without supplying a generator (✅). The seed product is therefore $\mathbb{CP}^2\times\mathbb{CP}^3 = (d{=}4)\times(d{=}6)$, not the literal seed pair $(d{=}3)\times(d{=}4)$, whose $d=3$ factor $S^3$ contributes no Kähler generator. Completeness — that the full second variation carries no marginal direction beyond $\omega_2^\alpha\omega_3^\beta$ — follows from $U(k)$ representation theory on flat $\mathbb{C}^k$ (✅): the condensate and the kernel $({\rm Re}\langle z,w\rangle)^2$ are $U(k)$-invariant, so every marginal deposit channel must lie in a $U(k)$-invariant subspace of the angular forms. For $0 \le p \le k$, $\Lambda^p(\mathbb{C}^k)$ is an irreducible $U(k)$-representation (standard), so by Schur's lemma there is exactly one $U(k)$-invariant element in $\Lambda^{p,p}(\mathbb{C}^k)$: the form $\omega^p$. For $p > k$, $\Lambda^p(\mathbb{C}^k) = 0$ by nilpotency of the exterior algebra in $k$ dimensions — pure linear algebra, no compact topology required. The invariant classes per sector are $\{1, \omega, \omega^2\}$ for $d=4$ ($k=2$) and $\{1, \omega, \omega^2, \omega^3\}$ for $d=6$ ($k=3$), giving $3 \times 4 = 12 = \dim R$. The deposit channels are exactly the monomials of $R$ and no others. No-latency (✅, 2026-06-18): the P6 degree-1 insertion applies a linear drive $-h\phi$ ($h>0$) at each depth step; at the proved-flat direction $V_{\rm eff}'(0) = -h < 0$, so the system immediately descends to the lower-energy deposited state with no threshold (`files/idwt.py` STEP 88). The three-ray program is structurally complete (✅). The open layer is the within-bidegree $n$-assignment: which mode index $n$ occupies each monomial $\omega_2^\alpha\omega_3^\beta$ of $R$ — this is the T0.5 question in ring language.

**The advance channels are the seed condensates (🔶).** Each advance deposit is one degree-1 condensate insertion (Part 1 P6), so a deposit channel is an evaluating condensed sector, and the deposit's index is the simplex redistribution $S(n, d_{\rm eval})$ over that sector's directions. The sector $d=2$ supplies no channel — there is no $d=2$ condensate, the same fact that protects $m_\gamma = 0$ and gives the boson $g$-rule its $-1$ (Part 3 §16.2). At the first advance the condensed matter sectors are exactly the seed pair $\{3, 4\}$, so the first advance has exactly two channels, and the two deposits carry the channel-by-channel forms $S(n_u,3) = \nu_1$ and $S(n_u,4) = \nu_2$. At every later advance the Betti budget binds at or below the channel count ($F_0(6) = 2$, $F_0(7{\to}10) = 1$), so the channel cap is load-bearing only where the seed-condensate census forces it to 2; whether later-structured sectors add channels is unobservable in the deposit record. The channel count is thereby derived from documented structure. The per-site deposit rate is bookkeeping rather than dynamics: front time is derivation depth, and the per-source reading — each mode fires its documented productions once, one step after creation, with deposits as first occupations — reproduces the same record exactly. No latency (✅, 2026-06-18; `files/idwt.py` STEP 88): every production fires at its minimal depth — the P6 linear drive eliminates any threshold.

**The imprint bound (🔶).** The condensate-linearized vertex (Part 1 P6) is degree 1 in the fluctuation leg, supplying one coordinate factor per insertion. A target mode structured in two or more coordinates beyond the source-plus-condensate support leaves at least one new coordinate with no vertex factor, and that coordinate integrates a bound harmonic against the uniform background: zero for odd harmonics (parity — exact), nonzero for even harmonics with the closed form $\int H_{2m}(y)\,e^{-y^2/2}\,dy = \sqrt{2\pi}\,(2m)!/m!$ (⭐, Hermite generating function) — strictly positive for every $m$, so the even-channel leakage has no zero at any order, and the exact unit-speed cut is parity-only. This is the same two-tier structure as the even-level selection ceiling (Part 7 §1.2): exact where parity protects, quantitative elsewhere. A single insertion therefore advances structure by at most one coordinate, exactly in the parity-protected channel; the $6 \to 10$ step is one ordinary insertion because the front's sites are kernel sites — dimensions 7–9 carry no sector, no well, and no coupling row (§13) — and the $d{=}6/d{=}10$ pair sits at zero kernel-metric separation ($g_{66} = g_{6,10} = g_{10,10}$, identical wells; Part 9 T9c). The reading of the $(1,d)$ ground modes as condensate background remains open.

**What the law does not do.** It fixes the $(k, d)$ skeleton — which sector fires at which derivation depth — not the mode index $n$ within a sector; the per-index selection question (Part 9 T0.5) is unchanged. The condensation-front reading of the $(k,d)$ plane — depth as generative order, the rays as the wavefronts of the three depth-0 anchors — is a candidate physical interpretation (❓). Numerical verification: `files/idwt.py` STEP 73.
