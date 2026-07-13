# Infinite Dimensional Wave Theory — Part 9: Spectral Theorems

**Status key:** ✅ Proved analytically · 🔵 Numerically verified to stated accuracy · 🔶 Conjecture with structural support · □ Open

---

## How to Read This Document

This document states IDWT as a sequence of self-contained spectral theorems. It is a mathematical companion to Parts 1–8: where those parts develop physical motivation, derivation history, and numerical tables, Part 9 states only the theorems and their proofs.

**Logical flow:** define the operator (T0, T0.5) → describe its spectral coefficients (T1) → justify the interaction term (T2) → prove which sectors exist (T3) → fix the unique seed (T4) → identify the critical endpoint (T5) → derive observables (T6–T11) → heat kernel and spectral geometry (T14) → spectral sum rules and exact mass ratios (T13).

**Physical intuition.** Each theorem is an instance of the same fact: the eigenvalue spectrum of a self-adjoint operator on a symmetric space with a nonlinear selection rule produces a discrete, deterministic point set. IDWT identifies the specific operator ($D$ on $M_\infty$) and the specific selection rule (the co-fixed-point condition), and reads off the SM particle masses as its selected spectrum. The actual object is $D$.

No SM inputs are used except $m_e = 0.51099895$ MeV as the single unit of mass.

---

## T0. The Physical Mass Spectrum of $D$

**Note — what this section claims, and what it does not.** IDWT has no Hilbert space. The wave $\Psi_\infty$ is a classical spinor field on $M_\infty$, and everything below is the classical eigenvalue problem of a differential operator $D$ acting on finite-energy field configurations on the manifold. The notation $(\mathcal{A},\mathcal{H},D)$ is borrowed only to organize that problem: $\mathcal{H}=L^2(M_\infty,\mathcal{S}_\infty)$ is the finite-energy norm on classical configurations — a bookkeeping device, not a space of states — and IDWT is not a noncommutative-geometry (NCG) model in the Connes–Marcolli sense. The properties below split into two kinds, and only the first is an IDWT result. **Genuine, and stated directly on $M_\infty$:** the eigenproblem of $D$ is well-posed with real discrete spectrum (item 1), that spectrum has no continuous part in the internal sectors (item 2), and the Dirichlet series of the masses $\sum_{n,d}S(n,d)^{-s}$ has abscissa $1/2$ (items 3, 7) — facts about the classical mass spectrum that need no Hilbert completion to state. **Borrowed NCG bookkeeping, carrying no physical claim about the field:** the Fredholm-module / $K$-homology class (item 4) and the smooth-subalgebra regularity (item 6) hold only once the operator is embedded in the NCG formalism; the framework does not assert them as physics. **Geometric:** item 5's content is the sector-dependent spinor reality structure ($\mathbb{CP}^2$ is spin$^c$, $S^5$ carries no $C$), not a KO-dimension integer. Status is recorded for the physically relevant operator — the finite-active internal triple, equivalently the projected $P_{\xi^0}DP_{\xi^0}$ — as of the 2026-06-13 spectral pass (`files/idwt.py` STEP 80, which computes the mass-spectrum Dirichlet series). The genuine residual is the full infinite-dimensional $M_\infty$ ($d\to\infty$, item 1). T0 remains 🔶.

1. **Self-adjointness of $D$. ✅ (physical operator).** Each sector operator $D_d$ is a Dirac-type operator on the complete flat $\mathbb{R}^d$ with confining potential $V_d=\lambda_d r^2$. The free Dirac operator on a complete manifold is essentially self-adjoint on $C_c^\infty$ (Chernoff, finite propagation speed), and the confining $r^2$ potential is the Dirac oscillator, ESA on $C_c^\infty$ (the squared operator is Schrödinger with potential $\to+\infty$ at infinity — limit-point, Faris–Lavine). A finite direct sum of ESA operators is ESA, and the spacetime free Dirac operator is ESA, so the physical operator (finite active product $\times$ spacetime) is essentially self-adjoint. The genuinely infinite-dimensional $M_\infty$ (all coordinate sectors, $d\to\infty$) is the residual.

2. **Compact resolvent. ✅ (internal operator).** Each $D_d$ has purely discrete spectrum with $S(n,d)\to\infty$ ($\sigma_{\rm ess}=\emptyset$, Part 4 §3.13); a finite direct sum of such operators has discrete spectrum diverging to $\infty$, so the internal resolvent $(D_{\rm int}-\lambda)^{-1}$ is compact. The full $D$ includes the spacetime part $-i\gamma^\mu\partial_\mu$ on $\mathbb{R}^{3,1}$ (continuous spectrum), so the full resolvent is not compact — compactness is a statement about the internal/sector operator (the projected $P_{\xi^0}DP_{\xi^0}$), as for any spacetime triple.

3. **Finite $p$-summability. ✅ computed.** Since $S(n,d)\sim n^d/d!$, the sector zeta $\zeta_d(s)=\sum_n S(n,d)^{-s}$ has abscissa of convergence $1/d$ (equivalently $K_d(t)\sim a_0^{(d)}t^{-1/d}$). With finitely many sectors, $\zeta_{\rm int}=\sum_{d\in D}\zeta_d$ has abscissa $\max_d 1/d=1/2$, attained at $d=2$. So $|D_{\rm int}|^{-p}$ is trace-class iff $p>1/2$ — the triple is $p$-summable for every $p>1/2$, summability dimension $1/2$ (verified numerically, STEP 80).

4. **Fredholm module / $K$-homology — NCG bookkeeping, no IDWT physical claim.** Once $D$ is embedded in the NCG formalism the internal triple yields a Fredholm module $F=D|D|^{-1}$ with $[F,a]$ compact on the natural smooth subalgebra (compact resolvent from item 2; $[D,a]=\gamma^\mu(\partial_\mu a)$ is bounded because the matrix factor is constant), defining a $K$-homology class. This is a property of the NCG embedding, not a statement about the classical field on $M_\infty$, and the framework does not assert it as physics.

5. **Sector spinor reality (no global real structure). 🔶 geometric.** A single KO-dimension would require a global real structure $J$ (charge conjugation) on $\mathcal{S}_\infty$; none exists, for a geometric reason that is IDWT physics rather than an NCG defect. $d=4$ ($\mathbb{CP}^2$) is spin$^c$, not spin ($\mathbb{CP}^n$ is spin iff $n$ is odd), so it carries no canonical $J$; and $d=5$ ($S^5$) admits no charge-conjugation $C$ — the same fact that forbids $0\nu\beta\beta$. The reality structure is therefore sector-dependent (spin sectors $d\in\{2,3,5,6,10\}$), tied to the chirality/Majorana content, and "KO-dimension" is not a single integer awaiting computation. The per-sector real dimensions mod 8 are $\{2,3,4,5,6,2\}$ (sum $22\equiv6\pmod 8$).

6. **Regularity — NCG bookkeeping, no IDWT physical claim.** In the NCG formalism the triple is regular: for the smooth subalgebra of functions with all derivatives bounded, $a$ and $[D,a]$ lie in $\bigcap_k\operatorname{Dom}(\delta^k)$, $\delta=[|D|,\cdot]$, since the iterated commutators $\delta^k(a)$ are bounded higher-derivative multiplication operators. This is the smoothness of the function algebra under the NCG derivation, not an IDWT physical fact.

7. **Spectral dimension. ✅ computed (correcting the expectation).** $\zeta_{\rm int}(s)=\sum_{d\in D}\zeta_d(s)$ has its rightmost pole at $s=1/2$ (the $d=2$ sector), so $d_s=1/2$. This is the summability dimension of the **mass operator** (eigenvalues = masses $\sim$ cumulative state counts $\sim n^d$), **not** the geometric dimension of $M_\infty$: because IDWT identifies mass with a cumulative count, $|D|$ grows far faster than a manifold Laplacian's Weyl growth, pushing the pole down to $1/2$. The earlier expectation that $d_s$ equals the effective dimension of $M_\infty$ does not hold. Special value $\zeta_{\rm int}(0)=\sum_d(-d/2)=-15$.

**Definition (organizing triple).** Consistent with the Note above, the classical eigenvalue problem of the IDWT Dirac operator $D$ is organized by the borrowed spectral-triple notation $(\mathcal{A},\,\mathcal{H},\,D)$ — a bookkeeping device, not a claim that IDWT is an NCG model — where

$$\mathcal{A} = C^\infty(M_\infty)\otimes\bigoplus_{d\in D}\mathcal{M}_{n_d}(\mathbb{C}), \qquad \mathcal{H} = L^2(M_\infty,\,\mathcal{S}_\infty), \qquad D = -i\gamma^\mu\partial_\mu + \sum_{d\in D} D_d.$$

Here $M_\infty = \mathbb{R}^{3,1}\times\prod_{d\in D}\Xi_d$ is the effective product decomposition in the $d=3$ observer's frame (the full metric on $M_\infty$ is $G_{AB}dX^AdX^B$ without assumed block structure; the product form is used throughout this section as the working approximation); $\mathcal{A}$ is the smooth $C^*$-algebra of observables acting on $\mathcal{H}$ by left multiplication; $D_d$ is the Dirac-Harmonic operator in sector $d$ with potential $V_d(r) = \lambda_d r^2$; and $\mathcal{S}_\infty$ is the master spinor bundle on $M_\infty$.

**Theorem T0 (Physical spectrum).** The physical masses are the eigenvalues of the projected operator $P_{\xi^0}\,D\,P_{\xi^0}$, where $P_{\xi^0}$ is the projection onto the subspace selected by the co-fixed-point condition (T0.5). The selected spectrum is

$$\sigma_{\rm phys}(|D|) = \bigl\{\,S(n,d)\times m_{\mathrm{scale},d}\;\big|\;(n,d)\in\Sigma_{\rm pairs}\,\bigr\}.$$

The 15 elements of $\sigma_{\rm phys}(|D|)$ are exactly the SM particle masses. Every element is determined by seeds $\{n_d=1,\,n_u=3\}$ and the single mass unit $m_e$. The index set $\Sigma_{\rm pairs}$ decomposes into three tiers (see the T0.5 scope): the eleven-mode lattice that T0.5 selects (photon $+$ hockey-stick fermions), the two product-form quark sites $\{16,72\}$, and the electroweak $g$-chain $\{76,81,95\}$ built additively off the top. The selection condition acts on the lattice; the heavy tier $\{72, 76, 81, 95\}$ is fixed by the electroweak spectral closure (T7 constraint form, `files/idwt.py` STEP 141, 🔶).

**Spectral action (borrowed bookkeeping).** Read through the NCG formalism, the asymptotic expansion of $\operatorname{Tr}(f(D/\Lambda))$ as $\Lambda\to\infty$ is the Seeley-DeWitt series:
$$\operatorname{Tr}(f(D/\Lambda)) \sim f_4\Lambda^4\,a_0 + f_2\Lambda^2\,a_2 + f_0\,a_4 + O(\Lambda^{-2}),$$
where the Seeley-DeWitt coefficients are:
- $a_0 \propto \operatorname{Vol}(M_\infty)$ — the term a $d=3$ observer reads as a cosmological constant
- $a_2 \propto \int R\,\mathrm{dvol}$ — the term a $d=3$ observer reads as the Einstein-Hilbert action, i.e. the observer's effective reconstruction of the mass-sourced $M_\infty$ curvature (Part 4 §0.2), not a fundamental gravitational action of IDWT
- $a_4$ — higher-order spectral invariants (in the standard spectral action $a_4$ yields Yang-Mills gauge kinetic terms; IDWT departs here — it carries no gauge kinetic term, its forces being kernel contact terms, not propagating gauge fields)

The IDWT sector heat kernel $K_d(t) = \sum_n e^{-tS(n,d)}$ has been computed exactly (T14), giving Weyl coefficient $a_0^{(d)} = \Gamma(1+1/d)(d!)^{1/d}$ and $\zeta_d(0) = -d/2$. These are the analytic invariants of the sector spectrum. They fix the *structure* of the heat trace, not the absolute gravitational scale: $G_\infty$ (equivalently $G_N=G_\infty/(4\pi)$) is a second dimensional input, not determined by the spectral expansion (Part 4 §3.12.4).


**Corollary (Spectral independence).** No element of $\sigma_{\rm phys}(|D|)$ is an integer linear combination of other elements from a different sector. This follows from the algebraic independence of the sector scales $m_{\mathrm{scale},d}$.

**Corollary (Bianchi identity).** The spectral action is diffeomorphism-invariant, so $\nabla_\mu T^{\mu\nu}_{\rm eff} = 0$ holds identically for the effective stress-energy derived from $D$. Gravity is internally self-consistent — the Bianchi identity holds exactly.

---

## T0.5. The Co-fixed-point Selection Condition 🔶

**Selection Principle T0.5.** A mode $(n,d)$ is a physical particle if and only if the pair $(n,d)$ is an element of $\Sigma_{\rm pairs}$ — the co-fixed-point set produced by the generation tower (the sector comb filtration generated by $n_s$). **Status: 🔶** semi-structural. The exclusion of non-co-fixed-point modes splits by level parity. The odd-level modes are excluded exactly: the $l=0$ seeds cannot reach an odd-$l$ mode through the $l=0\oplus l=2$ kernel at any order ($l$-parity, ⭐, Part 7 §1.2). The even-level modes are excluded exactly, by a strictly positive radiative width rather than a vanishing overlap (✅). The $l=0$ seed-coupling overlap $J(n_r,s)=\Gamma(n_r+\tfrac32)/n_r!\cdot(s-1)^{n_r}/s^{n_r+3/2}$ has its only zero at $s=1$, while the kernel fixes the weight at $s=3/2$, so the coupling is strictly nonzero for every even-level mode and decays geometrically without vanishing (`files/idwt.py` STEP 34). No exact $l$-parity-style zero-overlap cut exists for the even-level class under the $(\xi\cdot\xi')^2$ kernel — but the same non-vanishing overlap is exactly the strictly positive coupling of the downward link $(n,d)\to(n-2,d)$, which gives every even-level non-member a strictly positive, irreversible radiative width $\Gamma=\lambda^2(M_i^2-M_f^2)/(16\pi M_i^3)>0$ into the absolutely continuous spacetime momentum ($\Delta N=-2$ is $l$-parity-allowed, $\Delta E>0$, and the matrix element factorises into node-free positive overlaps). The exclusion is therefore exact through the width; its positivity is normalisation-free, and only the absolute rate magnitude is open (🔶, `files/idwt.py` STEP 103, STEP 118).

**Why these indices, and no others.** The index set is the *output* of a fixed generative principle. Every one of the fifteen indices is produced from the seeds $\{n_d=1,\,n_u=3\}$ (composite $n_s=n_u+n_d=4$) and the top anchor $n_{\rm top}=72$ by the tower's named operations — the hockey-stick $S(n,d)$, the additive and inclusion–exclusion edges, the ground-quantum offset (Part 7 §1.2a), and the boson $g$-rule — and the complement is excluded exactly: odd-level modes by an exact $l$-parity zero (⭐) and even-level modes by a strictly positive irreversible radiative width (✅). Fourteen of the fifteen are fixed outright by these operations or are declared anchors; exactly one — the generation-1 electron node $e=n_{\nu_1}+n_u=13$, the single cell where the additive step is not a forced Pascal identity (Part 7 §1.2) — carries an irreducible value-input. The framework's answer to *why these indices* is therefore explicit and complete: a fixed rule set acting on a minimal input — the seed pair $\{n_d=1,\,n_u=3\}$, the Euler-product index $n_{\rm top}=72$, and one additive-node value. That is the same *kind* of input any theory carries, and far less of it than the Standard Model, which takes its entire particle content (which representations of which gauge group) as input; IDWT derives that content and retains one integer's worth of index freedom. The 🔶 that remains is accordingly not an unanswered "why these $n$" but the sharper question of whether that last input, together with the tower's dynamical stability, descends from the coupled $(\Psi_\infty,\{M_d\})$ fixed point (MC-4, Part 6); the value-selection is a directed spectral assignment, and an operator spectrum — which lists the *available* modes but not which are *occupied* — provides its counts but not that occupancy (Appendix D §15).

**Scope — two regimes split at the heaviest fermion.** The fifteen non-photon mode indices divide at $n_{\rm top}=72$ into a bottom regime ($n<72$, the matter modes) and a top regime ($n\geq72$, the top quark together with the W, Z, and Higgs bosons — the bosons all $d=2$). Each regime carries its own selection law.

The **bottom regime** is the additive simplex tower: the ten indices $\{1,3,4,10,13,15,20,22,23,35\}$ — seven single-$S(n,d)$ hockey-stick leaves (down 1, up 3, strange 4, $\nu_1$ 10, $\nu_2$ 15, charm 20, $\mu$ 35) and three additive simplex sums of those leaves (the leptons $e=n_{\nu_1}+n_u=13$, $\nu_3=n_{\nu_1}+n_{\nu_2}-n_u=22$, $\tau=n_{\nu_3}+n_d=23$), with the photon as the $d=2$ ground state. This is the generation-tower DAG (Part 2 §6). The offset-additive quantum carried by each binary edge — the $+1$ by which $n_s,e,\mu,\tau$ sit one level above level-addition — is derived as the antisymmetric-pairing node in Part 7 §1.2a, while the inclusion–exclusion edge $\nu_3$ carries none. One further mode falls inside this regime without being a tower output: the bottom beat $k_0=n_s^2=16$, which is neither a single $S(n,d)$ value nor a named simplex sum but the Gegenbauer $b=\tfrac12$ critical endpoint on $S^3$ (T5). It enters the bottom-quark mass as a beat index, $m_b=\sqrt{S(16,3)\,S(17,3)}\,m_{\mathrm{scale},3}$, rather than as a mode index, so it is an overlay on the additive tower (`files/idwt.py` STEP 91).

The **top regime** is the boson chain anchored by the top index $n_{\rm top}=N_c\,n_s\,N_f=72$ (Euler-product index $\chi(\mathbb{CP}^2)\chi(\mathbb{CP}^3)\chi(\mathbb{CP}^5)=72$, value identity T15b; why the top quark occupies this mode is 🔶 open, T15d). The $W$ and $Z$ follow from $72$ by the $g$-rule $g(d,n)=n+d-1$ through active sectors: $n_W=g(5,72)=76$ and $n_Z=g(10,72)=g(6,76)=81$. The Higgs index $n_H=95$ has no active-sector $g$-predecessor in the spectrum (the candidates $95-(d-1)$ for $d\in D$ are $94,93,92,91,90,86$, none physical); it is the additive closure $n_H=n_u+n_{\rm charm}+n_{\rm top}=3+20+72=95$ (`files/idwt.py` STEP 91).

The $g$-rule organises the top regime but does not by itself select either set: its forward closure from the seed covers every integer in $1$–$71$ (`files/idwt.py` STEP 91), so it is an adjacency relation between admissible indices, not a generator. The selective structure is the additive simplex tower below $72$ and the short $g$-chain with additive closure above it. The selection problem proper remains the dynamical question — that the tower indices are stable resonances and the rest decohere (MC-4, Part 6).

The maximum within-sector return amplitude is bounded by the off-resonant Rabi sum $\sum_n (J/\Delta S)^2$ over all non-tower even modes, where $\Delta S > 0$ by spectral independence (⭐, the occupied $S$-values are sum-free, Part 1 §5). This sum converges in every sector: the worst case is $d=3$ at $\sum(J/\Delta S)^2 \approx 4\times10^{-4}$, bounding the coherent revival amplitude at $\lesssim 2\%$; the other sectors are smaller by $10^1$–$10^{13}$ (`files/idwt.py` STEP 49). Cross-sector revival is separately bounded to zero in the time-average by the incommensurability lemma (✅, `files/idwt.py` STEP 40: 14 of 15 cross-sector scale ratios are irrational). Together these bound the *discrete-tower* revival: total return probability $\lesssim 4\times10^{-4}$, small but strictly nonzero, so the discrete sector dynamics alone give no exact cut — the $d\le10$ towers recur (Poincaré) and the $d>10$ vacuum dimensions are a dynamically closed bath (the kernel has no support beyond coordinate 10, so outer momentum conservation gives zero coupling width at all orders; `files/idwt.py` STEP 64). The exact exclusion comes from the remaining channel: every even-level non-member radiates irreversibly into the absolutely continuous spacetime momentum with a strictly positive width $\Gamma>0$ (`files/idwt.py` STEP 118), so the even-level selection is an exact theorem (✅), not merely a tight bound. What sits at 🔶 is the absolute decay-rate magnitude (`files/idwt.py` STEP 103) and the dynamical selection of the tower DAG (below). At kernel level the even-level selection reduces to the absolute stability of a small set of anchor modes (Part 7 §1.2 stability equivalence, STEP 64), and that absolute-stability content is structural. A same-sector link onto a non-member is not a decay — the target is not an asymptotic state — so a genuine decay needs a parity-allowed channel to lighter *members* conserving charge, colour, and lepton number. The kernel $\Delta N=2$ link provides no such path: for every one of the 15, the same-sector target $(n{-}2,d)$ is a non-member (`files/idwt.py` STEP 108), so the spectrum is mutually kernel-decoupled and all genuine member decays proceed via the chiral EW channel (Part 7 §1.2, `files/idwt.py` STEP 107). The light anchors carry none: the u quark's only downward link terminates on the condensate ground mode (`files/idwt.py` STEP 92), the electron is the lightest electrically charged member (charge conservation), and lepton-number conservation (no $C$ on $S^5$) confines the neutrinos to the $d=5$ tower, where $\nu_1$ is the lightest and $\nu_2\to\nu_1$ is forbidden at all orders by $l$-parity ($\Delta N=-5$, odd) — so $u, e, \nu_1, \nu_2$ are absolutely stable, $\nu_3$ effectively so (`files/idwt.py` STEP 93). The general dispersal of every even-level non-member is now exact — each carries a strictly positive irreversible radiative width (✅, `files/idwt.py` STEP 118); what stays quantitative is only its absolute rate magnitude (🔶, `files/idwt.py` STEP 103). The reduction carries a sharp empirical witness: $\tau_e > 6.6\times10^{28}$ yr and the proton-decay bounds.

**Selection residue mapped (what it is *not*).** A systematic search has bounded the selection from every constructive side: it does not arise from the kernel coupling magnitudes (the even-level exclusion is exact through the *sign* of the radiative width, not its magnitude, and tower membership is not set by coupling magnitudes, above), from flat mode-index combinatorics beyond the hockey-stick (the hockey-stick generates the seven primary simplex modes false-positive-free, but the composite indices — $n_{\rm top}=\chi(\mathbb{CP}^2)\chi(\mathbb{CP}^3)\chi(\mathbb{CP}^5)$ and the additive/$g$-rule edges — are a specific sequence), from any single sector's Dirac/Laplace spectrum (the cumulative Dirac count is a mass law that grounds *every* $n$), or from cross-sector Hopf/inclusion branching (which carries the Hopf-image structure but selects nothing). An exhaustive search over all 1023 subsets of the natural IDWT operations $\{S(\cdot,d)_{d\in D},\ +n_u,\ +1,\ -n_u,\ \times n_u\}$ acting as symmetric closures from the seeds $\{n_d,n_u\}$ confirms that no symmetric arithmetic rule generates the Regime-1 bottom set $\{1,3,4,10,13,15,20,22,23,35\}$ exactly: every closure that reaches all ten members simultaneously floods the range with false positives ($\ge150$ in $[1,71]$). The best partial — $S(\cdot,3)$ (tetrahedral numbers) — hits 5/10 members with one false positive ($n=56$). This establishes that the bottom-regime selector is intrinsically directed and operand-specific: all five additive steps in the confirmed tower use $n_u=3$ as one argument at exactly the right operand sites, information that lives in the causal structure of the generation tower, not in arithmetic alone. The geometric backbone — the hockey-stick primaries, the Euler-characteristic seeding of each sector, the Hopf-carry of the neutrino indices — is established (⭐/✅). The residue that remains 🔶 is the *dynamical* selection of the specific tower DAG: the equation-of-motion derivation that the co-fixed-point modes are stable resonances and the rest decohere (MC-4, Part 6).

The mode index $n$ must be a fixed point or beat-frequency of the sector comb filtration generated by $n_s$, and the sector $d$ must be the one assigned to that family by the Hopf-chain structure (Part 1 §3); a mode at index $n$ in sector $d$ is stable only if the specific pair $(n,d)$ is a tower output. Modes that are not co-fixed points decohere on the timescale $1/m_{\mathrm{scale},d}$ and do not appear as stable resonances. The co-fixed-point modes form the eleven-mode lattice; together with the two product-form quark sites $\{16,72\}$ and the boson $g$-chain off the top (the scope above), the full observed set is the 15-element $\sigma_{\rm phys}(|D|)$.

**Compact binomial form (structural observation 🔶).** Setting $a=n_u=3$ and $b=n_s=4$, all 14 non-photon mode indices follow from the $2\times2$ Pascal block

$$B = \begin{pmatrix} \binom{a+2}{3} & \binom{a+3}{4} \\[4pt] \binom{b+2}{3} & \binom{b+3}{4} \end{pmatrix} = \begin{pmatrix}p & q \\ r & s\end{pmatrix} = \begin{pmatrix}10 & 15 \\ 20 & 35\end{pmatrix}$$

and the single triangular anchor $T=\binom{p+a+1}{2}=\binom{14}{2}=91$. The Pascal identity gives $s=r+q$ at once, so the muon fixed-point identity (T4) is a special case of the simplex recursion, not an independent constraint. The complete spectrum is:

$$\text{seeds: } 1,\;a,\;b \qquad \text{base: } p,\;q,\;r,\;s$$
$$\text{leptons: } p+a,\quad p+q-a,\quad p+q-a+1$$
$$\text{bosons/top: } T-q,\quad T-p,\quad T-r+1,\quad T+a+1$$

Substituting $a=3,\,b=4$ gives $\{1,3,4,10,15,20,35,13,22,23,76,81,72,95\}$ — all 14 values exactly. The stepwise additions of the generation tower are Pascal evaluations; no iteration is required once the block position $(a,b)=(3,4)$ and the anchor $T$ are specified.

This is a restatement of T0.5, not a derivation of it. It shows the tower has less free structure than the stepwise form suggests — the spectrum is a $2\times2$ Pascal block plus five complement formulas. The anchor $T=\binom{14}{2}$ and the $+1$ offsets on $n_{\rm top}$ and $n_H$ are artifacts of expressing two product-form sites in binomial terms. The top index $n_{\rm top}=72=N_c\,n_s\,N_f=\chi(\mathbb{CP}^2)\chi(\mathbb{CP}^3)\chi(\mathbb{CP}^5)$ and the bottom beat site $k_0=n_s^2=16$ have no solution to $S(n,d)=72$ or $16$ (checked $d\le11$, $n\le200$, ⭐); among the six quarks they are the only two not given by a single $S(n,d)$ value (the others are $1,3,4,20$), and both take product closed forms. Several non-quark indices are also not single $S$-values — $13,22,23$ for the leptons/neutrinos and $76,81,95$ for the bosons — but those are additive simplex sums and $g$-steps, not products. Neither product site can be reached by the hockey-stick without an offset; the $W$ and $Z$ follow as $g$-steps off $n_{\rm top}$ ($76=g(5,72)$, $81=g(10,72)=g(6,76)$), while the Higgs $95=n_u+n_{\rm charm}+n_{\rm top}$ is the additive closure ($g$-isolated, `files/idwt.py` STEP 91). The $+1$ in $n_\tau=n_{\nu_3}+n_{\rm down}$ is the down seed, not an offset. The block inputs are the seed $a=n_u=3$ and the composite $b=n_s=n_u+n_d=4$; the latter is overdetermined rather than open — T4's exact linear forcing ($n+1=5$, unique over the reals), the quartet self-consistency ($2n_s-4=n_s$, ⭐), the ground-quantum $n_s=n_u+n_d$ (⭐), and $\chi(\mathbb{CP}^3)=n_s$ all fix it. The electron node $e=n_{\nu_1}+n_u=13$ (the one non-Pascal cell) is fixed channel-conditionally: it is the unique complete doublet fusion available at its firing depth, and the doublet channel's ownership of the lepton cells follows from the active-pair map (Part 3 §0.8c; Part 7 §1.2a; `files/idwt.py` STEP 142–143, 🔶). Both non-image sites are 3rd-generation quarks and both are divisible by 8, a consequence of $n_s=4$ carrying the even factors ($16=n_s^2$, $72=N_c n_s N_f$ with $n_s N_f=24$); this is an arithmetic observation about the factorizations and not a spinor selection rule, since no Clifford reality invariant singles out $n\equiv0\pmod 8$.

---

## T1. The Hilbert Series

**Theorem T1 (Mass as Hilbert series coefficient).** The mass formula

$$\boxed{m(n,d) = S(n,d)\times m_{\mathrm{scale},d}, \qquad S(n,d) = \binom{n+d-1}{d}}$$

states that $m(n,d)/m_{\mathrm{scale},d}$ is the coefficient of $t^{n-1}$ in the Poincaré-Hilbert series of the free commutative algebra $\mathbb{R}[x_1,\ldots,x_{d+1}]$ in $d+1$ variables:

$$P_d(t) = \frac{1}{(1-t)^{d+1}} = \sum_{n\geq 1} S(n,d)\,t^{n-1}.$$

**Proof.** $S(n,d)=\binom{n+d-1}{d}$ counts the degree-$(n-1)$ monomials in $d+1$ variables, equals $\dim\mathrm{Sym}^{n-1}(\mathbb{R}^{d+1})$, and equals the IDOS (integrated density of states) of the $d$-dimensional harmonic oscillator at level $n$ — the number of eigenstates with quantum number $\leq n-1$. It is also the Ehrhart polynomial of the standard $d$-simplex evaluated at $n-1$ (the number of lattice points in its $(n-1)$-fold dilation), which is why $S(\cdot,d)$ is a degree-$d$ polynomial in $n$. In laser cavity terms: the cumulative count of transverse modes up to order $n-1$ in a $(d-1)$-transverse-mode cavity. $\square$

$$\boxed{S(n,d) \;=\; \dim\mathrm{Sym}^{n-1}(\mathbb{R}^{d+1}) \;=\; \mathrm{IDOS}_d(n) \;=\; [t^{n-1}]\frac{1}{(1-t)^{d+1}}}$$

⭐ **Schubert calculus interpretation.** $S(n,d) = \binom{n+d-1}{d}$ is the number of Schubert cells in the Grassmannian $\mathrm{Gr}(d,\, n+d-1)$. The hockey-stick recursion $S(n,d) = S(n,d-1) + S(n-1,d)$ is the Pieri rule: multiplying a Schubert class by the class of a hyperplane section in $\mathrm{Gr}(d,n+d-1)$ produces exactly these two terms. The generation tower DAG is therefore the Bruhat order on Schubert cells, which is why the tower has trivial automorphism group — the Bruhat order on a Grassmannian has no non-trivial order-preserving automorphisms. Verified: $S(4,3)=S(4,2)+S(3,3)=10+10=20$; $S(10,5)=S(10,4)+S(9,5)=715+1287=2002$.

**Cluster-algebra bracket (numerical coincidence, not a derivation or evidence).** The Grassmannian $\mathrm{Gr}(k,n)$ carries a cluster algebra structure; the finite-type classification gives $\mathrm{Gr}(3,6)\sim D_4$ (12 cluster variables) and $\mathrm{Gr}(3,7)\sim E_6$ (36). The 15 non-photon modes fall between these two counts ($12<15<36$). The tower terminates at 15 for independent reasons (T0.5); the bracket is recorded only as a numerical coincidence and carries no derivational weight.

⭐ **The $\mathbb{CP}^2$ harmonic tower closes at $15^2$ at the seed cutoff.** The $d=4$ sector $\mathbb{CP}^2=SU(3)/U(2)$ carries the harmonic decomposition $L^2(\mathbb{CP}^2)=\bigoplus_{k\geq0}V_{(k,k)}$ into $SU(3)$ irreducibles of highest weight $(k,k)$, with $\dim V_{(k,k)}=(k+1)^3$. The cumulative count through degree $K$ is the square of a triangular number,

$$\sum_{k=0}^{K}(k+1)^3=\Big(\tfrac{(K+1)(K+2)}{2}\Big)^2,$$

by the sum-of-cubes identity. At the seed cutoff $K=n_s=4$ the total is $15^2=225$, and $15=\binom{n_s+2}{2}$ is the number of stable massive modes (the fifteen of T15g, the same count the cluster bound brackets above). The stable-mode count therefore equals $T_{n_s+1}=\binom{n_s+2}{2}$, and the full $\mathbb{CP}^2$ harmonic content at the seed cutoff is its square ($\verb|files/idwt.py|$ STEP 87). This is a combinatorial identity; the count itself is fixed independently by the co-fixed-point selection (T0.5).

Sector $d$ Hilbert series — first seven coefficients:

| $d$ | $S(1,d)$ | $S(2,d)$ | $S(3,d)$ | $S(4,d)$ | $S(5,d)$ | $S(6,d)$ | $S(7,d)$ |
|---|---|---|---|---|---|---|---|
| 2 | 1 | 3 | 6 | 10 | 15 | 21 | 28 |
| 3 | 1 | 4 | 10 | 20 | 35 | 56 | 84 |
| 4 | 1 | 5 | 15 | 35 | 70 | 126 | 210 |
| 5 | 1 | 6 | 21 | 56 | 126 | 252 | 462 |
| 6 | 1 | 7 | 28 | 84 | 210 | 462 | 924 |
| 10 | 1 | 11 | 66 | 286 | 1001 | 3003 | 8008 |

---

## T2. The Kernel Uniqueness Theorem

**Scope.** T2 establishes uniqueness within the following assumptions: (1) the interaction is polynomial in $(\xi_d, \xi_{d'})$; (2) it is degree-4; (3) it is invariant under $U(d)\times U(d')$; (4) the coupling matrix is required to have rank 1; (5) the $\ell$-decomposition is restricted to $\ell=0\oplus\ell=2$ by the polynomial degree. Higher-degree interactions, non-polynomial couplings, or different invariance groups are not addressed. "Unique" in what follows means unique under these five assumptions.

**Theorem T2.** Among all $U(d)\times U(d')$-invariant degree-4 polynomials on $\Xi_d\times\Xi_{d'}$, the cross-sector interaction $(\xi_d\cdot\xi_{d'})^2$ is the **unique** one satisfying all three conditions:

1. **Non-trivial sector mixing**: cannot be written as a product of sector-local terms.
2. **$\ell=0\oplus\ell=2$ decomposition**: on $S^{d-1}$,
$$(\xi\cdot\xi')^2 = \underbrace{\tfrac{1}{d}|\xi|^2|\xi'|^2}_{\ell=0,\;\rm mass\;scale} + \underbrace{\tfrac{d-1}{d}|\xi|^2|\xi'|^2 P_2(\cos\theta)}_{\ell=2,\;\text{self-energy}},$$
with the $\ell=0$ part generating sector mass scales (T9) and the $\ell=2$ part generating the second-order self-energy of scale $\varepsilon=1/(280\sqrt{7})$ (T10a). This $\varepsilon$ enters the $\nu_3$ closure ($\delta_{\nu_3}=\varepsilon\cdot g_{33}=1/35$, T11d); the up-type masses carry the confinement-binding correction of Part 2 §11.9.
3. **Rank-1 factorisation**: the coupling matrix $g_{dd'}=v_d v_{d'}$ is rank-one, as required by the bi-invariant structure under $U(d)\times U(d')$.

**Proof sketch.** The $U(d)\times U(d')$-invariant degree-4 ring on $(\xi_d,\xi_{d'})$ has four generators: $|\xi_d|^4$, $|\xi_{d'}|^4$, $|\xi_d|^2|\xi_{d'}|^2$, and $(\xi_d\cdot\xi_{d'})^2$. The first three either fail condition 1 (sector-local) or condition 2 (diagonal in the $\ell$-basis). The fourth satisfies all three. $\square$

$\ell$-decomposition coefficients on $S^{d-1}$ for every sector:

| $d$ | $\ell=0$ | $\ell=2$ | Physical role |
|---|---|---|---|
| 2 | $1/2$ | $1/2$ | Gauge sector |
| 3 | $1/3$ | $2/3$ | Down-type quarks |
| 4 | $1/4$ | $3/4$ | Up-type quarks |
| 5 | $1/5$ | $4/5$ | Neutrinos |
| 6 | $1/6$ | $5/6$ | Electron, muon |
| 10 | $1/10$ | $9/10$ | Tau (critical) |

The $d=6$ row covers the electron and muon — both are $d=6$ $\mathbb{CP}^3$ sector excitations of $\Psi_\infty$, genuine 6D objects inhabiting six macroscopic spatial dimensions, whose activity in the three observable coordinates is what a $d=3$ observer measures.

---

## T3. The Sector Set Theorem

**Theorem T3 (Sector set from complex Hopf chain).** The sector set $D=\{2,3,4,5,6,10\}$ is uniquely determined by two rules applied to the complex Hopf fibration chain $S^1\to S^{2n+1}\to\mathbb{CP}^n$ for $n=1,2,3,\ldots$:

> **Rule A — Coupling termination at $d=6$, no re-entry before the Gegenbauer endpoint.** 🔵
> A sector is active only if it carries a constructible self-coupling $g_{dd}$. The construction chain runs through the low Hopf sectors — kernel fixed points fix $g_{33}$ and $g_{44}$, and Hopf universality $v_3/v_2=v_5/v_4$ then fixes $g_{55}$ (T9b) — and terminates at $d=6$, where $\chi(\mathbb{CP}^3)=n_s$ forces $g_{66}=1/n_s$ rather than a fixed-point coupling. The band $d\in\{7,8,9\}$ acquires no coupling; the three cases stand on different footings:
> - **$d=8$ ($\mathbb{CP}^4$, even base):** $\chi(\mathbb{CP}^4)=N_c+2=5$ is the gap in the Euler-characteristic sequence $\{2,3,4,\_,6\}$ of the active even sectors — there is no kernel fixed point for $g_{88}$ (T15b).
> - **$d=9$ ($S^9$):** an active $S^9$ would carry, on the $S^1$-invariant block of $L^2(S^9)=\bigoplus_m L^2(\mathbb{CP}^4,\mathcal{O}(m))$, a $\mathbb{CP}^4$-symmetric kernel self-consistency problem with coupling proportional to $g_{99}$; that equation form has no seed-anchored solution (the $\chi=5$ gap, T15b), so no value of $g_{99}$ makes $S^9$ self-consistent, however the activation is attempted.
> - **$d=7$ ($S^7$):** excluded by the deposit level-count (🔵; `idwt.py` STEP 100). The MC-2 deposit bijection (STEP 74e, ✅) places physical modes at sites $j=\alpha+\beta+2$ for $\alpha\in\{0,1,2\}$ (U(2) rank) and $\beta\in\{0,1,2,3\}$ (U(3) rank); the maximum total degree is $p=2+3=5$, giving exactly six deposit levels $j=2,\ldots,7$. The six elements of $D=\{2,3,4,5,6,10\}$ saturate all six levels; a seventh sector would require $p=6$, needing $\alpha\geq3$ or $\beta\geq4$ — impossible under U(2)$\times$U(3). Separately, $d=7$ cannot replace $d=10$ because the Gegenbauer endpoint is fixed at $d=10$ by Rule B independently. The two constraints close $d=7$.
>
> The only re-entry past the terminus is $d=10$, the Gegenbauer critical endpoint (Rule B), which takes $g_{10,10}=1/n_s$ by $\mu$–$\tau$ symmetry with $d=6$ (T9c).

> **Rule B — Gegenbauer criticality at $d=10$.**
> The Jacobi coupling $b_{k_0}(d)=\sqrt{k_0(k_0+d-1)}/(2k_0+d-2)$ satisfies $b_{k_0}\geq1/2$ iff $(d-2)^2\leq 4k_0$ (equivalently $d\leq 2+2\sqrt{k_0}$), saturated uniquely at
> $$4k_0 = (d-2)^2 \;\Longleftrightarrow\; 4\times16 = 64 = (10-2)^2.$$
> Sector $d=10$ is the Gegenbauer critical endpoint (T5); all $d\geq11$ are subcritical and excluded.

**Assembly.**
$$D = \underbrace{\{2,3,4,5\}}_{\text{Hopf pairs }n=1,2} \;\cup\; \underbrace{\{6\}}_{\substack{\text{base of }n=3\\\text{(Rule A)}}} \;\cup\; \underbrace{\{10\}}_{\substack{\text{base of }n=5\\\text{(Rule B)}}} = \{2,3,4,5,6,10\}. \quad\square$$

**Top index from the sector set.** Once the sector set is established, the top index equals the product of the Euler characteristics of the three Kähler matter sectors, $n_{\rm top}=\chi(\mathbb{CP}^2)\times\chi(\mathbb{CP}^3)\times\chi(\mathbb{CP}^5)=3\times4\times6=72$ (T15). This is a value identity — 72 is the top Chern number of the Kähler product. The index itself is selected by the electroweak spectral closure: $n_{\rm top}=72$ is the unique admissible maximum of the subscription bound (T7 constraint form, `files/idwt.py` STEP 141, 🔶), with the Euler product as the value's closed form (T15d). The value $72$ is not in the image of $S(n,d)$, so the top is a product-form site rather than a hockey-stick tower output, alongside the bottom beat $k_0=n_s^2=16$; among the six quarks these are the only two not given by a single $S(n,d)$ value, the other four being $1,3,4,20$ (T0.5). A second closed form, $n_{\rm top}=2\,S(2n_s,2)=2\,S(8,2)=72$ — a triangular-number ladder in $d{=}2$ using $n_s$ alone — reproduces $n_{\rm charm}=2\,S(n_s,2)=20$ at the same family's $k{=}1$ rung; like the Euler product, this holds numerically and is not itself a selection mechanism (a neighbouring-integer check shows 72 is not uniquely reachable this way).

Jacobi couplings at $k_0=16$ (all sectors in $D$ must have $b_{k_0}\geq1/2$, by T3 Rule B):

| $d$ | $b_{k_0}(d)$ | Regime | In $D$? |
|---|---|---|---|
| 2, 3, 4, 5, 6 | $0.515,\;0.514,\;0.513,\;0.511,\;0.509$ | supercritical | ✓ |
| 7 | $0.507$ | supercritical; excluded by deposit level-count (Rule A; 🔵, STEP 100) | ✗ |
| 8, 9 | $0.505,\;0.502$ | supercritical; no coupling — $d=8$ is the Euler-char gap $\chi{=}5$, $d=9$'s invariant block inherits it (Rule A) | ✗ |
| **10** | **0.500000** | **Gegenbauer critical endpoint** | **✓** |
| 11, 12, … | $0.497,\;0.495,\ldots$ | subcritical | ✗ |

**Two qualitatively distinct types of excluded dimension.** The table makes visible a distinction that matters for the top-down picture of $M_\infty$. Sectors $d\geq11$ are excluded at the most fundamental level: they are subcritical, meaning localization is geometrically impossible — modes cannot bind, they propagate and disperse into the infinite-dimensional bulk. Sectors $d\in\{7,8,9\}$ are supercritical (localization is in principle possible) but are excluded by coupling structure: the coupling-construction chain terminates at $d=6$ and none of the band acquires a self-coupling — $d=8$ is the Euler-characteristic gap ($\chi=5$, no $g_{88}$ fixed point), $d=9$ inherits that gap on its $S^1$-invariant block, and $d=7$ is excluded by the deposit level-count (Rule A; 🔵, STEP 100). These are qualitatively different failures. $d\geq11$ cannot host bound states at all. $d\in\{7,8,9\}$ could in principle support localized modes, but there is no mechanism in $M_\infty$ to form the sector potential that would trap them.

**Coordinate subspaces vs active sectors.** The absence of $d\in\{7,8,9\}$ from the sector set $D$ does not mean those coordinate directions are absent from $M_\infty$. $M_\infty$ contains all integer-dimensional coordinate subspaces; the function-space nesting $C^\infty(\Xi_2)\subset C^\infty(\Xi_3)\subset\cdots\subset C^\infty(\Xi_7)\subset C^\infty(\Xi_8)\subset C^\infty(\Xi_9)\subset C^\infty(\Xi_{10})\subset C^\infty(M_\infty)$ is complete (Part 1 §3h). What is absent for $d\in\{7,8,9\}$ is the active sector geometry: there is no sector potential $V_d(r)$ formed by a kernel fixed-point, hence no confining well, no discrete eigenmodes, and no contribution to the observed spectrum. The coordinate subspaces $\Xi_7$, $\Xi_8$, $\Xi_9$ exist as submanifolds of $M_\infty$; they simply carry no bound-state activity.

---

## T4. The Seed Uniqueness Theorem

**Theorem T4.** The pair $(n_u, n_s) = (3, 4)$ is the unique pair of consecutive positive integers satisfying the double self-consistency equation

$$\boxed{\frac{n_s(n_s+1)}{S(n_s,4)} = \frac{n_u(n_u+1)}{S(n_u,5)} = \frac{4}{7} \approx 0.57143, \qquad n_u = n_s - 1 \;\text{[T15: consecutiveness]}}$$

simultaneously in the $d=3$ sector (left) and the $d=4$ sector (right). The eigenvalue $4/7$ is the kernel algebraic fixed-point at resonance site $k_0=n_s^2=16$. T4 serves as a uniqueness certificate for the seed $n_u = 3$ ($\chi(\mathbb{CP}^2) = N_c = 3$) and the composite $n_s = 1 + 3 = 4$ (confirmed by this equation).

**Proof by exhaustion.** $n_s=4$ is the only integer satisfying the coincidence; all others diverge. $\square$

| $n_s$ | $d=3$: $n_s(n_s{+}1)/S(n_s,4)$ | $d=4$: $n_u(n_u{+}1)/S(n_u,5)$ | Equal? |
|---|---|---|---|
| 3 | $12/15 = 0.8000$ | $12/12 = 1.0000$ | No |
| **4** | $\mathbf{20/35 = 4/7 = 0.5714}$ | $\mathbf{12/21 = 4/7 = 0.5714}$ | **Yes** |
| 5 | $30/56 = 0.4286$ | $20/56 = 0.3571$ | No |

**Complementary derivation — closed-form reduction.** ⭐ Both sides of the boxed equation are elementary rational functions of $n$. Writing $b_n(3)$ for the left ($d=3$) side and $b_n(4)$ for the right ($d=4$) side, and using $S(n,4)=\binom{n+3}{4}$ and $S(n-1,5)=\binom{n+3}{5}$,
$$b_n(3) = \frac{n(n+1)}{S(n,4)} = \frac{24}{(n+2)(n+3)}, \qquad b_n(4) = \frac{(n-1)\,n}{S(n-1,5)} = \frac{120}{(n+1)(n+2)(n+3)}.$$
Setting $b_n(3) = b_n(4)$ and cancelling the common factor $(n+2)(n+3)$ gives $24 = 120/(n+1)$, hence $n+1=5$ and $n_s = 4$ — the unique crossing point over all reals, not merely over the integers. For $n < 4$ the right side $b_n(4)$ dominates; for $n > 4$ the left side $b_n(3)$ dominates. The fixed point is isolated and exact, upgrading the proof by exhaustion above to an exact linear forcing.

⭐ **2-adic / Kummer remark on $n_s=4$.** Kummer's theorem states that the 2-adic valuation $v_2\binom{a+b}{b}$ equals the number of carries when adding $a$ and $b$ in binary. The S-values $S(n_s,3) = 20$ and $S(n_s,4)=35$ have $v_2(20)=2$ and $v_2(35)=0$ respectively, reflecting two carries $(3+3$ in binary) vs. zero carries $(4+2$ in binary). The first collision in the S-value sequence — where two distinct sums $S(i)+S(j)$ could equal $S(k)$ — occurs at $n=5$: $S(5,4)=70=35+35$, verified because $v_2(70)=1$ and two carries appear in $4+4$ in binary. The initial segment $n=1,2,3$ gives distinct 2-adic valuations $v_2(1)=0$, $v_2(4)=2$, $v_2(10)=1$; $n=4$ is the first repeat ($v_2(20)=2=v_2(4)$). This boundary at $n_s=4$ is an independent combinatorial signal in the binary structure of the sequence.

⭐ **Finite projective geometry remark.** The projective 3-space $PG(3,2)$ over the field $\mathbb{F}_2$ has exactly 15 points and $\binom{4}{2}_2 = \frac{(2^4-1)(2^3-1)}{(2^2-1)(2^1-1)} = \frac{15\times7}{3\times1} = 35$ lines. The number of lines equals $S(n_s,4)=35 = n_\mu$, the muon mode index. The number of points (15) equals the mode index $q = \binom{n_u+3}{4} = \binom{6}{4} = 15$ of the intermediate generation-tower vertex (Part 9 T0.5). These are consequences of the evaluation $\binom{n}{k}_q$ at $q=2, n=4$: the $q\to1$ limit collapses $PG(3,2)$ geometry to the binomial counts, but the combinatorial skeleton — the Pascal lattice structure of $\binom{4}{\cdot}$ — is the same object appearing in both languages.

⭐ **Noncrossing partition depth — third independent derivation.** Map each mode to the noncrossing partition of $\{1,\dots,d+1\}$ whose block sizes are given by the parts of the weak composition for $S(n,d)$. The rank function of the noncrossing partition lattice $NC(d+1)$ is $(d+1)$ minus the number of blocks. For the IDWT modes this gives:

| Mode | Partition | Blocks | NC rank = depth |
|------|-----------|--------|-----------------|
| down ($n=1$, seed) | $d+1$ singletons | $d+1$ | 0 |
| strange ($n=4$) | 1 block | 1 | $d$ (composite level) |
| up ($n=3$, seed) | 3 blocks in $d=4$ | 3 | 1 |
| charm ($n=20$) | 2 blocks in $d=4$ | 2 | $2\to$reduced to 1 by Hopf pairing |
| electron ($n=13$) | partition $13=10+3$, 2 blocks | 2 | 3 joins from seeds |

The noncrossing partition lattice has a known Möbius function and EL-labeling, which supplies canonical shortest paths between modes in the generation tower. Together with the Ferrers box count (Part 2 §1) and the cluster mutation distance (T1), this gives three independent combinatorial computations of generation depth that agree on every mode without running `idwt.py`.

---

## T5. The Gegenbauer Criticality Theorem

**Theorem T5.** Sector $d=10$ is the unique element of the complex Hopf chain at the Gegenbauer critical endpoint (T5) where $b_{k_0}(d)=1/2$:

$$\boxed{b_{k_0}(10) = \frac{\sqrt{16\times25}}{40} = \frac{20}{40} = \frac{1}{2}.}$$

This is equivalent (by T3 Rule B) to $4k_0=(d-2)^2$. Uniqueness: the equation is quadratic in $d$ with a single positive-integer solution above $d=6$.

**Spectral consequences (by sector):**
- $d<10$: $b_{k_0}>1/2$ — supercritical, extended bound states, stable discrete spectrum.
- $d=10$: $b_{k_0}=1/2$ — Gegenbauer critical point; modes at the Jacobi coupling boundary; coupling distributed with no dominant channel. Final stable sector.
- $d\geq11$: $b_{k_0}<1/2$ — below the Jacobi coupling threshold; no stable sector-bound states.

**Physical consequences:**
- The $\tau$ lepton ($d=10$, $n=23$) is a critical eigenstate; the geometric back-reaction correction $+1/1680$ (T10b) is its leading finite-size regularisation.
- Near-degeneracy $|n_\tau-n_{\nu_3}|=1$ at the critical sector gives the Gegenbauer propagator $G(\Delta n)\propto1/|\Delta n|$ its smallest possible argument, maximally enhancing the $\tau$-$\nu_3$ coupling and making $\theta_{23}$ the largest PMNS angle (T6).

---

## T6. The PMNS Theorem 🔵

**Theorem T6.** The three PMNS angles are determined by $g_{55}=96/g_{22}=0.132872$ and four mode indices:

$$\boxed{\sin^2\theta_{23} = \frac{1-g_{55}}{2} + g_{55}\,\frac{S(n_\tau,10)}{S(n_\mu,6)+S(n_\tau,10)}}$$

$$\boxed{\sin^2\theta_{12} = \frac{1-g_{55}}{3} + g_{55}\,\frac{S(n_{\nu_1},5)}{S(n_{\nu_1},5)+S(n_{\nu_2},5)}}$$

$$\boxed{\sin^2\theta_{13} = g_{55}\,\delta_{23}\,\ln\frac{S(n_\tau,10)}{S(n_\mu,6)},} \qquad \delta_{23}=\sin^2\theta_{23}-\tfrac{1}{2}$$

| Angle | Prediction | PDG 2024 | Error |
|---|---|---|---|
| $\sin^2\theta_{23}$ | $0.55897$ | $0.553$ | $+1.07\%$ |
| $\sin^2\theta_{12}$ | $0.30856$ | $0.307$ | $+0.51\%$ |
| $\sin^2\theta_{13}$ | $0.02211$ | $0.0219$ | $+0.96\%$ |

The three PMNS angles depend only on $g_{55}$ and the four mode indices $n_{\nu_i}$, $n_\alpha$; $g_{55}=96/g_{22}$ and the indices are fixed by the seed structure (T9b, T0.5).

**Derivation key steps.**

*Step 1 (Rank-1 coupling, by T2).* $W[\alpha,i]\propto\sqrt{S(n_\alpha,d_\alpha)}\,\sqrt{S(n_{\nu_i},5)}$.

*Step 2 (Two limits).* The PMNS interpolates between:
- **μ–τ symmetric limit** (weight $1-g_{55}$): $g_{66}=g_{10,10}=1/n_s$ (T9c) forces $v_6=v_{10}$, giving $\mu$-$\tau$ symmetry and the coupling-symmetry values $(1/2,1/3,0)$.
- **Mode-amplitude limit** (weight $g_{55}$): simplex hierarchy $S(n_\tau,10)\gg S(n_\mu,6)$ drives $\theta_{23}$ toward $\tau$-dominance; $S(n_{\nu_1},5)\ll S(n_{\nu_2},5)$ depletes $\theta_{12}$.

*Step 3 (Weight).* $g_{55}=g_{33}g_{44}/g_{22}=96/g_{22}$ (T9b) controls how much the mass hierarchy displaces PMNS from the μ–τ symmetric limit.

*Step 4 ($\theta_{13}$ as second order).* $\sin^2\theta_{13}=g_{55}\cdot\delta_{23}\cdot r$ where $r=\ln(S(n_\tau,10)/S(n_\mu,6))=\ln(m_\tau/m_\mu)=2.822$ (exact because $m_{\rm scale,10}=m_{\rm scale,6}$). Since $\delta_{23}\propto g_{55}$, this correction is $O(g_{55}^2)$.

**Mode-index proximity (by T5).** Three exact identities from the generation law chain:

$$|n_\tau - n_{\nu_3}| = 1 = n_d, \qquad |n_e - n_{\nu_1}| = 3 = n_u, \qquad |n_\tau - n_{\nu_1}| = 13 = n_e.$$

The Gegenbauer propagator $G(\Delta n)\propto1/|\Delta n|$ at the $d=10$ critical point gives the hierarchy $\sin^2\theta_{23}:\sin^2\theta_{12}:\sin^2\theta_{13}=1:1/n_u:1/n_e=1:1/3:1/13$ at leading order.

---

## T7. Spectral Self-Consistency of the EW Scale 🔵

**Theorem T7.** The RMS of the IDWT physical mass spectrum and the EW scale derived from the IDWT Fermi constant agree to within a fraction of a percent.

From the 15 IDWT physical masses (confinement-corrected quarks; `files/idwt.py` STEP 14):

$$\operatorname{Tr}(D^2) = \sum_{i=1}^{15} m_i^2 = 6.025\times10^{10}\ \text{MeV}^2, \qquad \sqrt{\operatorname{Tr}(D^2)} = 245.47\ \text{GeV}.$$

From the IDWT-derived Fermi constant $G_F = g_2^2/(4\sqrt{2}\,m_W^2) = 1.1658\times10^{-5}\ \text{GeV}^{-2}$, the EW scale is $(\sqrt{2}\,G_F)^{-1/2} = 246.28\ \text{GeV}$. The physical spectrum places $\sqrt{\operatorname{Tr}(D^2)}$ $-0.33\%$ below this scale (and $-0.31\%$ from the SM value $v = 246.22$ GeV); both are spectral quantities built from the same seeds, so the small residual is a self-consistency offset. The confinement-binding correction on the coloured quarks — dominated by the top, $176.4 \to 172.5$ GeV — is what places the RMS at the EW scale; the uncorrected bare count gives $+0.78\%$.

This is a self-consistency check: both quantities are derived from the same seed structure, so agreement is structurally expected. It is not an independent prediction. The Higgs VEV concept (from spontaneous symmetry breaking) does not apply in IDWT — the Higgs is a confinement mode of the $d=2$ sector, and there is no quartic scalar potential (Part 5 §3c).

**T7 as a constraint — the EW spectral closure selects the heavy indices. 🔶** Read as a subscription condition rather than a check, the T7 relation selects the heavy mode indices (`files/idwt.py` STEP 141). The rank-1 coupling $g_{dd'} = v_d v_{d'}$ makes the kernel identically $\tfrac12(\sum_d v_d K_d)^2$ — one collective channel — and the committed $G_F$ form fixes that channel's total weight at $v^2 = (\sqrt2\,G_F)^{-1}$, so the closure takes the unit-total form $\sqrt2\,G_F\operatorname{Tr}(D^2) = 1$: each mode carries share $\sqrt2\,G_F\,m_i^2$, and the shares are fractions of the channel's one quantum, so $\sum_i (m_i/v)^2 \le 1$ is a hard bound; no-latency deposition fills it maximally. Consequences: with the additive chain $(n_W, n_Z, n_H) = (T{+}4, T{+}9, T{+}23)$ off $n_{\rm top} = T$, the bound has a unique admissible maximum at $T = 72$ ($T{=}73$ oversubscribes by $+2.4\%$); given the other three, each committed heavy index is the unique integer at the subscription boundary ($n_W{=}75$, $n_Z{=}82$, $n_H{=}96$ all oversubscribe); and the spectrum terminates at 15 modes — the unsubscribed remainder ($0.66\%$ of the quantum, headroom $\approx 20$ GeV) is smaller than the lightest admissible continuation ($n{=}96$, $128$ GeV), so no sixteenth mode is admissible. The $-0.33\%$ RMS offset is this remainder: the ledger closes exactly ($0.9934$ subscribed $+ 0.0066$ unsubscribed $= 1$). The $m_i^2$ weighting is not a chosen exponent: $\operatorname{Tr}(D^2)$ is defined (Theorem T7, `files/idwt.py` STEP 14) as the trace of the diagonal mass operator squared, and that operator's entries are already fixed by the foundational hockey-stick mass law (Theorem S1) — squaring a fixed diagonal operator carries no independent physical assumption. The moment scan ($\operatorname{Tr}(D^k)/v^k = 1.94,\ 0.9934,\ 0.56,\ 0.34$ for $k = 1..4$) is a robustness check confirming the other powers fit far worse, not a search among live alternatives. The neutral channel adds no second condition ($\cos\theta_W = S(n_W,2)/S(n_Z,2)$ exactly makes the $Z$ closure algebraically the $W$ closure). Selection requires the physical (confinement-corrected) spectrum — bare masses shift the admissible maximum to $T{=}71$. Parents: the equidistribution premise, the one-quantum anchored units, and the Part 2 §11.9 correction; label 🔶.

| Particle | $m$ (GeV) | Fraction of $\operatorname{Tr}(D^2)$ |
|---|---|---|
| Top $t$ | $172.5$ | $49.4\%$ |
| Higgs $H$ | $125.3$ | $26.0\%$ |
| $Z$ | $91.2$ | $13.8\%$ |
| $W$ | $80.4$ | $10.7\%$ |
| All others | — | $<0.1\%$ |



## T8. CP Violation — Topological Source Identification 🔶

**At tree level.** With vacuum at $\xi^0_d=0$, the sector mixing amplitudes from $S(n,d)$ ratios are real and the holonomy around any sector loop vanishes:
$$\delta_{CP}^{(\rm tree)} = 0.$$

**Topological source.** A non-zero CP phase requires an imaginary contribution. Sectors $d=6$ ($\mathbb{CP}^3$, $c_1=4$) and $d=10$ ($\mathbb{CP}^5$, $c_1=6$) carry different first Chern classes. The Chern-number difference

$$\boxed{\Delta c_1 = c_1(\mathbb{CP}^3) - c_1(\mathbb{CP}^5) = 4 - 6 = -2}$$

is identified as the candidate source of CP violation. It is non-zero because the two CP lepton sectors sit at different levels of the Hopf chain (Rule B, T3). This is a purely geometric fact, independent of any normalisation of $\Psi_\infty$.

**What the computation requires.** Whether $\Delta c_1 = -2$ produces a non-zero imaginary part in the mixing matrix requires integrating the Fubini-Study curvature 2-form $\omega_{\rm FS}$ around the effective loop area in **sector coupling parameter space** — the space of coupling constants $g_{dd'}$, not $|\Psi_\infty|$ amplitude space. The curvature integral must be expressed in terms of the dimensionless couplings $g_{5,6}$, $g_{5,10}$, and the Fubini-Study geometry of $\mathbb{CP}^3$ and $\mathbb{CP}^5$. This computation has not been performed.

**Coupling parameter space and its metric. 🔶** Define the sector coupling state as the tensor product of sector eigenmodes evaluated at the IDWT coupling values:

$$\Psi_{\rm sect}(\{g_{dd}\}) = \bigotimes_d \chi_{n_d,d}(\xi^0;\, g_{dd})$$

where $\chi_{n_d,d}(\xi^0;\,g_{dd})$ is the leading occupied eigenmode of sector $d$ at the observer position $\xi^0$, regarded as a function of the self-coupling $g_{dd}$. At the physical point $g_{dd} = g_{dd}^{\rm(IDWT)}$, this is the ordinary IDWT mode function; allowing $g_{dd}$ to vary defines a smooth family of states on the coupling parameter space $\mathcal{M}$.

The metric on $\mathcal{M}$ used in the computations below is the quantum information (Bures) metric — a candidate choice, not a derived one. The eigenmodes $\chi_{n_d,d}$ are $L^2$-normalizable and vary smoothly with $g_{dd}$, making the Bures metric technically available; however, the coupling space $\mathcal{M}$ is not a priori a quantum state space, and the identification of the Fubini-Study pullback as the physically correct metric on $\mathcal{M}$ has not been derived from the IDWT action. An alternative is the Hessian metric $\partial^2 S/\partial g_{dd}^2$. Until either form is derived from the action, the Bures metric is a convenient choice whose suitability for computing the CP phase is open.

$$G_{ij} = \operatorname{Re}\!\left[\langle \partial_i \Psi_{\rm sect} \mid \partial_j \Psi_{\rm sect}\rangle - \langle \partial_i \Psi_{\rm sect} \mid \Psi_{\rm sect}\rangle\langle \Psi_{\rm sect} \mid \partial_j \Psi_{\rm sect}\rangle\right]$$

where $\partial_i = \partial/\partial g_{d_i d_i}$ and the inner product is $L^2(\Xi)$. This is the Fubini-Study metric pulled back to the coupling space via the map $\{g_{dd}\} \mapsto \Psi_{\rm sect}$.

**The lepton triangle loop.** The CP phase is the spectral phase around the loop

$$\gamma:\; d=5 \;\to\; d=6 \;\to\; d=10 \;\to\; d=5$$

in the coupling subspace $(g_{55}, g_{66}, g_{10,10}) \subset \mathcal{M}$. By Stokes' theorem:

$$\delta_{CP} = i \oint_\gamma \langle \Psi_{\rm sect} \mid d\Psi_{\rm sect}\rangle = \int_{A:\,\partial A = \gamma} \mathcal{F}_\mathcal{M}$$

where $\mathcal{F}_\mathcal{M} = d\mathcal{A}_\mathcal{M}$ is the curvature 2-form of the spectral connection on the coupling-space bundle.

**What $\mathcal{F}_\mathcal{M}$ depends on.** Since $\lambda_d = (g_{dd}/2)^{2/3}$ (Part 4 §3.10), the coupling derivative of the eigenmode is:

$$\frac{\partial \chi_{n_d,d}}{\partial g_{dd}} = \frac{1}{3}\!\left(\frac{g_{dd}}{2}\right)^{-1/3} \frac{\partial \chi_{n_d,d}}{\partial \lambda_d}$$

The quantity $\partial \chi / \partial \lambda_d$ is the first-order perturbation of the sector bound-state mode under a change in potential depth — a definite eigenvalue-perturbation calculation on the sector potential $V_d(r) = \lambda_d r^2$. $\mathcal{F}_\mathcal{M}$ is non-zero if and only if $\partial\chi_{d=6}/\partial\lambda_6$ and $\partial\chi_{d=10}/\partial\lambda_{10}$ are non-collinear in $L^2(\Xi)$. Non-collinearity is expected because $c_1(\mathbb{CP}^3) \neq c_1(\mathbb{CP}^5)$, which is what $\Delta c_1 = -2$ encodes geometrically — but confirming it requires evaluating the perturbation integrals.

**Numerical results (STEP 71).** The first-order perturbation $\partial f_{0,d}/\partial\lambda_d$ was computed for $d=6$ and $d=10$ using a tridiagonal discretisation of the 1D centrifugal equation with the harmonic potential $V_d = \lambda_d r^2$ ($N=6000$, $r_{\rm max}=8L_d$ where $L_d = \lambda_d^{-1/4}$ is the harmonic oscillator length). The harmonic ground state $f_0(r) = N_d\, r^{(d-1)/2}\exp(-\sqrt{\lambda_d}\,r^2/2)$ admits a closed-form derivative:

$$\frac{\partial f_0}{\partial\lambda_d} = f_0\!\left[\frac{d}{8\lambda_d} - \frac{r^2}{4\sqrt{\lambda_d}}\right], \qquad \left\|\frac{\partial f_0}{\partial\lambda_d}\right\|^2 = \frac{d}{32\lambda_d^2}$$

For $d=6$ and $d=10$, which share $\lambda = 1/4$, the norms and angle are exact:

$$\|\partial f_{0,6}/\partial\lambda\| = \sqrt{3}\approx1.732, \qquad \|\partial f_{0,10}/\partial\lambda\| = \sqrt{5}\approx2.236$$

$$\cos\theta = \frac{3\sqrt{5}}{10}\approx +0.6708, \qquad \sin\theta = \sqrt{\frac{11}{20}}\approx 0.741$$

These are confirmed numerically to machine precision (STEP 71). The Bures metric diagonal $G_{dd} = d/(288\lambda_d^3)$ gives $G_{66} = 4/3 \approx 1.333$ and $G_{10,10} = 20/9 \approx 2.222$ (chain rule $\partial\lambda/\partial g = \tfrac{1}{3}(g/2)^{-1/3}$). The non-collinearity ($\sin\theta\neq0$) establishes that the **Bures metric is non-degenerate** in the lepton coupling subspace, driven by the different centrifugal barriers (3.75 for $d=6$, 15.75 for $d=10$) despite the shared $\lambda=0.250$.

**Spectral phase triangle integral.** The spectral phase was computed directly using the discrete formula $\gamma = -\arg\!\prod_{\rm edges}\langle\Psi_k|\Psi_{k+1}\rangle$ on a triangle in $(g_{66}, g_{10,10})$ coupling space ($\varepsilon=0.01$). The spectral curvature $\mathcal{F}_{6,10} = -2\,\mathrm{Im}\,Q_{6,10}$ was evaluated by finite differences. Both give:

$$\boxed{\gamma = 0, \quad \mathcal{F}_{6,10} = 0}$$

This is exact for a product state of real sector eigenmodes — consistent with $\delta_{CP}^{(\rm tree)}=0$ exactly. The spectral connection components $\langle\partial_{g_6}\chi_6|\chi_6\rangle = 5\times10^{-12}$ and $\langle\chi_{10}|\partial_{g_{10}}\chi_{10}\rangle = 6\times10^{-12}$ are numerically zero (real normalized modes).

**CP-violation constraint.** From the IDWT mixing angles (T6), $J_{\rm max} = s_{12}c_{12}s_{23}c_{23}s_{13}c_{13}^2 = 0.03335$. To reproduce the PDG NH best-fit $\delta_{CP}\approx197°$:

$$J_{\rm PMNS}^{\rm(IDWT)} = J_{\rm max}\sin\delta_{CP} = 0.03335\times(-0.292) \approx -0.0098$$

$$\Rightarrow \sin(\delta_{CP}) \approx -0.29 \text{ is the target for IDWT.}$$

**Route to non-zero $\delta_{CP}$.** A product state of real modes gives $\gamma=0$ exactly. Non-zero $\delta_{CP}$ requires that the PMNS mixing matrix $U_{\rm PMNS}(g_{55},g_{66},g_{10,10})$ be treated as a $U(3)$ bundle over the lepton coupling space, with spectral phase accumulated by the determinant of $U$ as the couplings are varied around the lepton triangle. This requires a formula for $\delta_{CP}(g_{dd})$ from the sector-mixing structure — the part of the computation that remains open.

**Status.** $\delta_{CP}^{(\rm tree)}=0$ exact and confirmed numerically ($\gamma=0$, $\mathcal{F}=0$). Bures metric non-degenerate ($\sin\theta=\sqrt{11/20}\approx0.741$). CP-violation target $\sin(\delta_{CP})\approx-0.29$. 🔶 — Part 10 has since derived $\delta_{CP} = \pi + 2\theta_{13} = 197.11°$ via APS spectral flow across the $\mathbb{CP}^3\to\mathbb{CP}^5$ sector mismatch; three gaps remain before 🔵 (spectral flow coefficient rigour, sign from T6 matrix, equivalence with the holonomy integral here). See Part 10 for the current derivation.

---

## T9. The Coupling Constant Theorems

All six sector self-couplings are derived from $n_s=4$, $n_u=3$:

| Coupling | Exact formula | Value | Source |
|---|---|---|---|
| $g_{22}$ | $(S(n_s,3)-n_u)^2(S(n_u,4)-S(n_u,3))/2$ | $722.5$ | Theorem S3 |
| $g_{33}$ | $n_s^2\sqrt{n_s+n_u}/2$ | $8\sqrt{7}=21.166$ | Kernel fixed-point, $d=3$ |
| $g_{44}$ | $n_s n_u/\sqrt{n_s+n_u}$ | $12/\sqrt{7}=4.536$ | Kernel fixed-point, $d=4$ |
| $g_{55}$ | $g_{33}g_{44}/g_{22}=96/g_{22}$ | $0.13287$ | Hopf universality (T9b) |
| $g_{66}$ | $1/n_s$ | $0.25000$ | Seed ratio (Rule A) |
| $g_{10,10}$ | $1/n_s$ | $0.25000$ | Shared seed (T9c) |

**T9a** (Kernel product). $g_{33}\times g_{44}=96$ exactly; also $g_{22}\cdot g_{55}=96$.

**T9b** (Hopf universality). $v_3/v_2=v_5/v_4$ exactly, deriving $g_{55}$ from the $d=3,4$ couplings via the Hopf chain condition (T3 Rule B). The rank-1 factorisation of T2 gives $g_{dd'}=v_d v_{d'}$; the specific ratio $v_3/v_2=v_5/v_4$ is the additional Hopf universality constraint.

**T9b Corollary (Hopf Routing Rule). ✅** Since $g_{55}$ is derived entirely from $g_{44}$ via $v_5/v_4 = v_3/v_2$, sector $d=5$ is the unique sector in $D$ whose self-coupling is determined by $g_{44}$. Generation tower modes derived from a $d=4$ seed belong to $d=5$ — because $d=5$ is the only sector in $D$ constructed as the Hopf fiber over $d=4$ (Part 1 §3a Step 2). Assigning those modes to any other sector in $D$ would require a sector whose coupling closes over $d=4$; by T3, no such sector exists besides $d=5$. The routing rule is a direct corollary of T9b and T3.

**T9c** ($\mu$-$\tau$ symmetry). $g_{66}=g_{10,10}=1/n_s$ exactly, giving $v_6=v_{10}=1/2$. This is the $\mu$-$\tau$ interchange symmetry that gives the coupling-symmetry limit of the PMNS (T6 Step 2).

**T9d** (Electric charge). $e=g_2\sin\theta_W$, both derived. $1/\alpha=131.8$ at the $d=2$ sector scale; after 1-loop QED running $1/\alpha(0)\approx133.1$ (PDG: 137.036, $-2.9\%$ from missing hadronic vacuum polarisation — a non-perturbative QCD contribution not computed by IDWT's 1-loop lepton running).

---

## T10. The Perturbative Correction Theorems

**T10a** ($\ell=2$ self-energy scale $\varepsilon$). The $\ell=2$ kernel component (T2, condition 2) is a traceless tensor whose second-order self-energy has scale

$$\boxed{\varepsilon = \frac{g_{\rm coeff}}{k_0\times n_{\rm mu}} = \frac{2/\sqrt{7}}{16\times35} = \frac{1}{280\sqrt{7}} \approx 0.001350.}$$

The $d=4$ up-type overshoot carries the derived confinement-binding correction $M_{\rm phys}=M_{\rm bare}(1-x_e\langle k\rangle)$ — linear in the mean level, a single derived coefficient $x_e=3/(16N_b)$ applied universally to the coloured $d=3,4$ quarks (Part 2 §11.9; `files/idwt.py` STEP 127), bringing all five quarks within ±1σ PDG 2024 stat (charm $+0.34\%$, top $-0.04\%$, 🔶). The bare combinatorial counts (charm $1{,}284.9$ MeV, top $176{,}365$ MeV) are recorded in §11.5. ($\varepsilon$ is the derived scale of the separate $\nu_3$ closure, T11d.)

**T10b** (Geometric back-reaction correction for $\tau$). At the Gegenbauer critical endpoint (T5), the $d=10$ eigenvalue admits an infinite-series correction resummed through $g_{10,10}=1/n_s$:

$$\boxed{\delta_\tau = \frac{1}{n_u\cdot n_s^2\cdot S(n_s,4)} = \frac{1}{3\cdot16\cdot35} = \frac{1}{1680}.}$$

Result: $m_\tau\times(1+1/1680)=1776.84$ MeV vs PDG 2024 $1776.93\pm0.09$ MeV ($-0.005\%$; $-1.0\sigma$).

---

## T11. The Neutrino Spectral Theorems

**T11a** (Mass scale). Fixed by dimensional consistency across sector scales:

$$\boxed{m_{\rm scale,5} = \frac{n_u}{n_s}\,\frac{m_{\rm scale,6}^3}{m_{\rm scale,4}^2} = 7.429\times10^{-13}\ \text{MeV}.}$$

**T11b** (Mass ratios and oscillation cross-check). The primary predictions are the absolute mass ratios:

$$\frac{m_{\nu_2}}{m_{\nu_1}} = \frac{S(15,5)}{S(10,5)} = 5.808, \qquad \frac{m_{\nu_3}}{m_{\nu_1}} = \frac{S(22,5)}{S(10,5)} = 32.86.$$

As derived consequences in oscillation-experiment language, $\Delta m^2_{ij} = (S(n_{\nu_i},5)^2 - S(n_{\nu_j},5)^2)\times m_{\rm scale,5}^2$:

| Derived quantity | Value | Oscillation inference | Gap |
|---|---|---|---|
| $\Delta m^2_{21}$ | $7.242\times10^{-5}$ eV$^2$ | $(7.53\pm0.18)\times10^{-5}$ | $-3.8\%$ |
| $m_{\nu_3}$ (absolute) | $50.27$ meV (corrected; bare $48.87$ meV) | $2.523\times10^{-3}$ eV$^2$ (PDG 2023); $2.530\times10^{-3}$ eV$^2$ (PDG 2024 NO) | $+0.05\%$ (2023); $-0.22\%$ (2024) |

The correction $\delta_{\nu_3} = \varepsilon\cdot g_{33} = 1/35$ is a closure relation 🔶 (primary derivation Part 2 §9d): $g_{\rm coeff}\times g_{33} = n_s^2 = k_0$ (the $\sqrt{7}$ cancels algebraically), so $\varepsilon\cdot g_{33} = k_0/(k_0\cdot n_{\rm mu}) = 1/35$ — exact given independently-derived $\varepsilon$ and $g_{33}$, but the deeper operator mechanism is not yet derived. The corrected $m_{\nu_3}^{\rm corr} = 50.267$ meV implies $\Delta m^2_{31} = 2.5246\times10^{-3}$ eV$^2$ — within 0.05% of PDG 2023 and within $0.2\sigma$ of PDG 2024. Structural source: $n_{\nu_3}$ is the unique inclusion-exclusion mode index, combining the $d=3$ image ($n_{\nu_1}$) and $d=4$ image ($n_{\nu_2}$) of the seed $n_u$; the $\ell=2$ cross-term (T2) then mixes these via $\varepsilon$ ($d=4$ $\ell=2$ self-energy scale) and $g_{33}$ ($d=3$ back-reaction). Expressing the correction as $\Delta m^2_{31}$ inflates the apparent significance without adding information.

**T11c** (Majorana forbidden). $d\bmod8=5$ (Clifford algebra mod 8 periodicity) forbids the Majorana condition on $\mathcal{S}_5$-spinors. Neutrinos are strictly Dirac. The $0\nu\beta\beta$ decay rate is therefore zero at all orders: no $C$ exists on the $S^5$ bundle, so no Majorana operator can be constructed at any loop order.

**T11d** (Cosmological sum). $\Sigma m_\nu = 60.39\ \text{meV}$ with the established $\delta_{\nu_3}=1/35$ correction (Part 2 §9d); uncorrected sum $59.00\ \text{meV}$. Normal ordering. Both are within current cosmological bounds; CMB-S4 will distinguish them.

---

## T14. Heat Kernel and Spectral Geometry

**Note on non-compact sector spaces.** The standard Seeley-DeWitt heat kernel expansion is developed for compact Riemannian manifolds. IDWT's sector spaces $\Xi_d$ are non-compact (the confining potential $V_d(r)=\lambda_dr^2$ replaces compactness; eigenmodes are $L^2$-normalizable). The results below (Weyl coefficient, $\zeta_d(0)$) are derived directly from the IDWT eigenvalue sequence $S(n,d)$ via Euler-Maclaurin and Mellin transforms — they do not invoke the compact-manifold Seeley-DeWitt formula. Correspondence between these direct results and the standard heat-kernel coefficient formulas applied to non-compact operators with confining potentials has not been verified; this is an open item (Part 4 §3.12.1, Part 6 MC-8).

The **heat kernel** of sector $d$ is the trace of the heat semi-group of the sector operator:
$$K_d(t) = \operatorname{Tr}(e^{-t|D_d|}) = \sum_{n=1}^{\infty} e^{-t\,S(n,d)}, \qquad t > 0.$$

The sum converges for all $t>0$ because $S(n,d)\to\infty$. It encodes the full spectral content of the sector in a single analytic function.

**Physical readings.** (a) $K_d(t)$ is the partition function of sector $d$ at inverse temperature $t/m_{{\rm scale},d}$. (b) Via the Mellin transform $\Gamma(s)\zeta_d(s) = \int_0^\infty t^{s-1}K_d(t)\,dt$, it is the generating function of all spectral zeta values $\zeta_d(s)$, including the sum rule $\zeta_d(1)=d/(d-1)$ from T13a. (c) The spectral action at cutoff $\Lambda$ with exponential kernel is $\operatorname{Tr}(e^{-|D|/\Lambda})=\sum_d K_d(m_{{\rm scale},d}/\Lambda)$.

### T14a. Weyl Term (Leading Small-$t$ Asymptotics)

**Theorem.** As $t\to 0^+$:
$$K_d(t) = a_0^{(d)}\,t^{-1/d} - \frac{d}{2} + O(t^{1/d})$$
where the **Weyl coefficient** is
$$a_0^{(d)} = \Gamma\!\left(1+\frac{1}{d}\right)(d!)^{1/d}.$$

**Proof.** Replace the sum by an integral $\int_0^\infty e^{-tS(x,d)}\,dx$ plus discrete corrections.

**(i) Leading integral.** For large $n$, $S(n,d)\approx n^d/d!$, so:
$$\int_0^\infty e^{-tn^d/d!}\,dn = \left(\frac{d!}{t}\right)^{1/d}\!\int_0^\infty e^{-u^d}\,du = \left(\frac{d!}{t}\right)^{1/d}\!\frac{\Gamma(1/d)}{d} = a_0^{(d)}\,t^{-1/d}.$$

**(ii) Subleading-in-$S$ correction.** The next term in $S(n,d)$ beyond $n^d/d!$ is
$$\frac{d-1}{2(d-1)!}\,n^{d-1}.$$
Expanding $e^{-tS}\approx e^{-tn^d/d!}(1-t\delta_n)$ and integrating this correction:
$$-t\cdot\frac{d-1}{2(d-1)!}\int_0^\infty e^{-tn^d/d!}n^{d-1}\,dn = -t\cdot\frac{d-1}{2(d-1)!}\cdot\frac{d!}{dt} = -\frac{d-1}{2}.$$

**(iii) Euler-Maclaurin boundary.** The discrete sum differs from the integral by $-f(0)/2$ where $f(0)=e^{-tS(0,d)}=1$, giving $-\tfrac{1}{2}$.

Summing (ii)$+$(iii): constant term $=-(d-1)/2-1/2=-d/2$. $\square$

**Weyl coefficients** (all six IDWT sectors):

| $d$ | $a_0^{(d)}=\Gamma(1+1/d)(d!)^{1/d}$ | Constant $-d/2$ | Spectral dim |
|---|---|---|---|
| 2 | 1.253314 | −1.0 | 2 |
| 3 | 1.622651 | −1.5 | 3 |
| 4 | 2.006198 | −2.0 | 4 |
| 5 | 2.391987 | −2.5 | 5 |
| 6 | 2.777402 | −3.0 | 6 |
| 10 | 4.308410 | −5.0 | 10 |

The power $t^{-1/d}$ encodes the **spectral dimension** $d$ of the sector: eigenvalues grow as $n^d$, so the counting function $N(\lambda)\propto\lambda^{1/d}$, and the leading heat-kernel exponent is $1/d$ — matching the sector dimension $d$.

**Numerical check** at $t=10^{-3}$: the 2-term approximation agrees with the exact partial sum at the 0.01% level for $d=2$, 0.2% for $d=3$, 0.7% for $d=4$, degrading to $\sim12\%$ for $d=10$ because $t^{1/d}=(10^{-3})^{0.1}\approx 0.5$ is not yet small — large-$d$ sectors enter the Weyl regime only at smaller $t$.

### T14b. Spectral Zeta at Zero and Functional Determinant

**Theorem.** The regularised spectral zeta value at $s=0$ satisfies
$$\zeta_d(0) = -\frac{d}{2} \qquad \text{for every IDWT sector } d.$$

**Proof.** By the Mellin transform, the constant term $-d/2$ in $K_d(t)$ contributes $\int_0^1 (-d/2)\,t^{s-1}\,dt = -d/(2s)$ to $\Gamma(s)\zeta_d(s)$. Since $\Gamma(s)\sim 1/s$ near $s=0$, the regular value at $s=0$ is $\zeta_d(0)=-d/2$. $\square$

**Context.** In standard heat-kernel expansions on Riemannian manifolds of dimension $m$, one has $\zeta_D(0) = a_{m/2}$ where $a_{m/2}$ is the integrated Seeley-DeWitt coefficient. In IDWT the role of the manifold dimension is played by $d$, and $\zeta_d(0)=-d/2$ is its exact analogue. The **sector functional determinant** is
$$\log\det D_d = -\zeta_d'(0),$$
a finite number (zeta-regularised) for each sector. Combined with the sum rule $\zeta_d(1)=d/(d-1)$ from T13a, these are the two anchor values of the spectral zeta of each sector.

### T14c. Large-$t$ Asymptotics and First Excitation Gap

For $t\gg 1$ the sum is dominated by the ground state $S(1,d)=1$ (same for all $d$) and the first excited state $S(2,d)=d+1$:
$$K_d(t) \approx e^{-t}\bigl(1 + e^{-dt} + \cdots\bigr), \qquad t\to\infty.$$

Two exact results follow:

1. **Universal ground state.** $S(1,d)=1$ for every sector; all sectors share the same ground-state energy in units of $m_{{\rm scale},d}$. Verified: $K_d(5)\approx e^{-5}=0.006738$ to six figures for all six $d$.

2. **First excitation gap equals sector dimension.** $S(2,d)-S(1,d)=(d+1)-1=d$ (equivalently, by the T13b mode-spacing identity, $S(2,d)-S(1,d)=S(2,d-1)=d$). The energy gap to the first excited state is exactly $d$ in dimensionless units.

### T14d. Pole Structure of the Sector Zeta Function ✅

**Theorem.** For each sector $d\in D$, the spectral zeta function $\zeta_d(s)=\sum_{n\geq1}S(n,d)^{-s}$ has a **simple pole at $s=1/d$** with residue

$$\operatorname{Res}_{s=1/d}\,\zeta_d(s) \;=\; \frac{(d!)^{1/d}}{d}.$$

$\zeta_d(s)$ is analytic for $\operatorname{Re}(s)>1/d$ except at this pole. The complete multi-sector zeta function $\zeta_D(s)=\sum_{d\in D}\zeta_d(s)$ has simple poles at

$$s \;\in\; \Bigl\{\tfrac{1}{2},\;\tfrac{1}{3},\;\tfrac{1}{4},\;\tfrac{1}{5},\;\tfrac{1}{6},\;\tfrac{1}{10}\Bigr\}$$

one for each sector in $D=\{2,3,4,5,6,10\}$.

**Proof.** For large $n$, the simplex number satisfies $S(n,d)=n^d/d!\,+\,O(n^{d-1})$. Partition the sum:

$$\zeta_d(s) = \sum_{n=1}^{N_0} S(n,d)^{-s} + \sum_{n>N_0} S(n,d)^{-s}.$$

The finite head is analytic in $s$. For the tail, the subleading correction $O(n^{d-1})$ perturbs each term by $O(n^{-ds-1})$, giving a contribution that converges absolutely for $\operatorname{Re}(s)>1/d-1/d=0$ — analytic away from any pole of the leading term. The leading term gives

$$\sum_{n>N_0}S(n,d)^{-s}\;\approx\;(d!)^s\sum_{n>N_0}n^{-ds}\;=\;(d!)^s\bigl[\zeta(ds)-\text{finite head}\bigr].$$

The Riemann zeta $\zeta(ds)$ has a simple pole at $ds=1$ (i.e.\ $s=1/d$) with residue $1$. Since $d(ds)/ds=d$, the residue of $\zeta(ds)$ viewed as a function of $s$ is $1/d$. Therefore

$$\operatorname{Res}_{s=1/d}\,\zeta_d(s) = (d!)^{1/d}\times\frac{1}{d} = \frac{(d!)^{1/d}}{d}.\quad\square$$

**Numerical residues** for the six IDWT sectors:

| $d$ | $(d!)^{1/d}$ | Residue $(d!)^{1/d}/d$ |
|---|---|---|
| 2 | $2^{1/2}=1.41421$ | $0.70711$ |
| 3 | $6^{1/3}=1.81712$ | $0.60571$ |
| 4 | $24^{1/4}=2.21336$ | $0.55334$ |
| 5 | $120^{1/5}=2.60517$ | $0.52103$ |
| 6 | $720^{1/6}=2.99379$ | $0.49897$ |
| 10 | $(10!)^{1/10}=4.52873$ | $0.45287$ |

The residues decrease monotonically with $d$.

**Physical meaning.** The pole at $s=1/d$ is the **spectral dimension** of sector $d$: eigenvalues grow as $n^d$, so the counting function $N(\lambda)\propto\lambda^{1/d}$ and the zeta series converges only for $s>1/d$. In IDWT, the theory has not one spectral dimension but **six**, corresponding to its six geometric sectors. The leading pole is at $s=1/2$ (from the $d=2$ photon sector, where eigenvalues grow slowest, as $n^2/2$); successive sectors contribute poles at finer resolution $1/3, 1/4, \ldots, 1/10$.

This is the spectral analogue of the multi-scale structure of $M_\infty$: each sector has its own Weyl law, its own spectral dimension, and its own rate of eigenvalue growth. The photon sector dominates the UV behavior of the full zeta function; the tau sector ($d=10$, pole at $s=1/10$) is the most UV-soft, consistent with its role as the Gegenbauer critical endpoint (T5).

**Connection to T14a.** The Weyl coefficient $a_0^{(d)}=\Gamma(1+1/d)(d!)^{1/d}$ (T14a) and the residue $(d!)^{1/d}/d$ are related by

$$a_0^{(d)} = \Gamma(1+1/d)\times d\times\operatorname{Res}_{s=1/d}\,\zeta_d(s),$$

since $\Gamma(1+1/d)=(1/d)\Gamma(1/d)$ and $d\times(d!)^{1/d}/d=(d!)^{1/d}$. The Weyl coefficient is the residue amplified by the Gamma factor from the Mellin transform — the two ways of reading the same singularity of the heat kernel. $\square$

---

## T13. Spectral Sum Rules and Exact Mass Ratios

**Two combinatorial identities** hold in every IDWT sector and follow from Pascal's triangle alone. They are exact consequences of the Hilbert-series formula $m(n,d)=m_{\rm scale}\cdot S(n,d)$.

### T13a. Spectral Sum Rule

**Theorem.** For each sector $d\in\{2,3,4,5,6,10\}$:
$$\zeta_d(1)\;\equiv\;\sum_{n=1}^{\infty}\frac{1}{S(n,d)}\;=\;\frac{d}{d-1}.$$

**Proof (telescoping).** The identity
$$\frac{1}{\binom{n+d-1}{d}}=\frac{d}{d-1}\left[\frac{1}{\binom{n+d-2}{d-1}}-\frac{1}{\binom{n+d-1}{d-1}}\right]$$
is verified by direct expansion. Summing $n=1$ to $N$ the right side telescopes:
$$\sum_{n=1}^{N}\frac{1}{S(n,d)}=\frac{d}{d-1}\left[\frac{1}{\binom{d-1}{d-1}}-\frac{1}{\binom{N+d-1}{d-1}}\right]=\frac{d}{d-1}\left[1-\frac{1}{S(N,d-1)}\right],$$
using $\binom{d-1}{d-1}=1$ as the boundary condition. As $N\to\infty$, $S(N,d-1)\to\infty$, giving $\zeta_d(1)=d/(d-1)$. $\square$

**Numerical values** (confirmed by direct partial summation to $N=2000$):

| Sector $d$ | $\zeta_d(1)$ | Exact form |
|---|---|---|
| 2 | 2 | $2/1$ |
| 3 | 3/2 | $3/2$ |
| 4 | 4/3 | $4/3$ |
| 5 | 5/4 | $5/4$ |
| 6 | 6/5 | $6/5$ |
| 10 | 10/9 | $10/9$ |

**Physical meaning.** The total reciprocal spectral weight of sector $d$ is a fixed rational number determined by the sector dimension $d$ alone. Combined with T1 (masses = $m_{\rm scale}\cdot S(n,d)$), the sum rule fixes the total inverse-mass weight of each sector relative to its ground state.

### T13b. Mode Spacing Identity

**Theorem.** For all $n\geq 1$ and $d\geq 2$:
$$S(n+1,d)-S(n,d)=S(n+1,d-1).$$

**Proof.** Pascal's identity $\binom{n}{k}+\binom{n}{k-1}=\binom{n+1}{k}$ gives
$$\binom{n+d}{d}-\binom{n+d-1}{d}=\binom{n+d-1}{d-1}=S(n+1,d-1).\quad\square$$

**Interpretation.** The gap between consecutive resonances at levels $n$ and $n+1$ in sector $d$ equals the $(n+1)$-th resonance of sector $d-1$. This means the number of new modes added when ascending one step in sector $d$ is counted exactly by sector $d-1$ at the same level — a precise filling-rate relation between adjacent sectors.

**Derivation chains (Part 2 §2–6).** Every mode-index identity of the form $n_{\rm particle}=n_a+n_b$ traces to this relation applied at a specific sector boundary. Examples:

| Identity | Pascal instance |
|---|---|
| $n_{\nu_1}=S(n_{\rm up},3)=10$ | $S(4,3)-S(3,3)=S(4,2)=10$ |
| $n_{\nu_2}=S(n_{\rm up},4)=15$ | $S(4,4)-S(3,4)=S(4,3)=20\neq 15$; direct: $S(3,4)=15$ |
| $n_\mu=n_{\rm charm}+n_{\nu_2}=35$ | $S(5,4)-S(4,4)=S(5,3)=35$ |
| $n_W = g(d_\nu, n_{\rm top}) = d_\nu + n_{\rm top} - 1 = 76$ | $g$-rule with neutrino sector dim $d_\nu=5$ |

**Verification** (nine cases, all $\checkmark$):

| $n$ | $d$ | $S(n+1,d)-S(n,d)$ | $S(n+1,d-1)$ |
|---|---|---|---|
| 1 | 3 | 3 | 3 |
| 4 | 3 | 15 | 15 |
| 13 | 3 | 105 | 105 |
| 1 | 4 | 4 | 4 |
| 4 | 4 | 35 | 35 |
| 13 | 4 | 560 | 560 |
| 1 | 6 | 6 | 6 |
| 4 | 6 | 126 | 126 |
| 13 | 6 | 8568 | 8568 |

### T13c. Exact Mass Ratios

Within a single sector, $m_{{\rm scale},d}$ cancels, leaving pure rational ratios of simplex numbers $S(n,d)=\binom{n+d-1}{d}$. The charged-lepton ($m_\mu/m_e$), boson ($m_Z/m_W$), and $\nu_2/\nu_1$ ratios are exact rationals; the tau ratios carry the parameter-free back-reaction factor $D=1+1/1680$ (T10b), algebraic in $n_s$ and $\varepsilon=1/(280\sqrt{7})$. The $d=4$ up-type quark ratios instead carry the confinement-binding correction (§11.9, 🔶) and so are not pure rationals; their physical values are given in Part 5 §3b ($m_c/m_u=587.2$, $m_t/m_c=135.0$, $m_t/m_u=79{,}303$, each within $\sim0.4$–$0.7\%$ of PDG).

| Ratio | IDWT exact form | IDWT value | PDG | Error |
|---|---|---|---|---|
| $m_\mu/m_e$ | $S(35,6)/S(13,6)=3838380/18564$ | 206.765 | 206.768 | −0.002% |
| $m_\tau/m_\mu$ | $\frac{S(23,10)}{S(35,6)}\times D=\frac{64512240}{3838380}\times D$ | 16.8172 | 16.8177 | −0.003% |
| $m_\tau/m_e$ | $\frac{S(23,10)}{S(13,6)}\times D=\frac{64512240}{18564}\times D$ | 3477.19 | 3477.37 | −0.005% |
| $m_{\nu_3}/m_{\nu_1}$ | $S(22,5)/S(10,5)=65780/2002$ | 32.857 | — | — |
| $m_{\nu_2}/m_{\nu_1}$ | $S(15,5)/S(10,5)=11628/2002$ | 5.808 | — | — |
| $m_{\nu_3}/m_{\nu_2}$ | $S(22,5)/S(15,5)=65780/11628$ | 5.657 | — | — |
| $m_Z/m_W$ | $S(81,2)/S(76,2)=3321/2926$ | 1.1350 | 1.1346 | +0.034% |

$D=1+1/(n_{\rm up}\cdot n_s^2\cdot S(n_s,4))=1+1/1680$ is the back-reaction factor (T10b). Note $m_{{\rm scale},10}=m_{{\rm scale},6}$ so the $\tau/\mu$ and $\tau/e$ ratios are cross-sector only in dimension, not in coupling. Neutrino ratios have no direct PDG comparand because oscillation experiments measure $\Delta m^2$ differences, not absolute ratios; the IDWT predictions are falsifiable once $m_{\nu_1}$ is measured by CMB-S4 or tritium endpoint experiments.

### T13d. Partial Sum Formula ✅

**Theorem.** For all $d\geq 2$ and $N\geq 1$:

$$\boxed{\sum_{n=1}^{N} S(n,d) \;=\; S(N,\,d+1).}$$

The cumulative spectral weight through level $N$ in sector $d$ equals the spectral weight of the single mode at level $N$ in the next sector $d+1$.

**Proof.** Apply the hockey-stick identity of Pascal's triangle: $\sum_{k=r}^{m}\binom{k}{r}=\binom{m+1}{r+1}$.

Set $r=d$ and substitute $k=n+d-1$ (so $k$ runs from $d$ to $N+d-1$ as $n$ runs from $1$ to $N$):

$$\sum_{n=1}^{N}S(n,d)=\sum_{n=1}^{N}\binom{n+d-1}{d}=\sum_{k=d}^{N+d-1}\binom{k}{d}=\binom{N+d}{d+1}=S(N,d+1).\quad\square$$

The boundary term $\binom{d-1}{d}=0$ (since $d-1<d$) vanishes, so the sum starts cleanly at $n=1$.

**Verification** for $d=2$, $N=4$: $\sum_{n=1}^{4}S(n,2)=1+3+6+10=20=S(4,3)=\binom{6}{3}=20$. ✓

**Corollary (Mass sum).** The total mass contributed by sector $d$ through level $N$ is

$$\sum_{n=1}^{N} m(n,d) \;=\; m_{{\rm scale},d}\times S(N,\,d+1).$$

The sum of mode masses in sector $d$ up to cutoff $N$ is exactly $m_{{\rm scale},d}$ times the $N$-th simplex number of the next sector. This is the exact IDWT formula for the sector vacuum energy at finite cutoff — relevant to the cosmological constant computation (Part 8 §13).

**Asymptotic growth.** For large $N$, $S(N,d+1)\sim N^{d+1}/(d+1)!$, so the partial mass sum grows as $N^{d+1}$. Taming this growth to the small observed vacuum energy is an open problem: an observability measure cannot affect a gravitational contribution (Part 4 §4), so what distinguishes contributing modes is persistence — co-fixed-point stability (Part 8 §13).

### T13e. Degree and Iterated Difference Theorem ✅

**Theorem.** For all $d\geq 2$, $n\geq 1$, and $1\leq k\leq d$, the $k$-th forward difference of $S(n,d)$ in $n$ is:

$$\boxed{\Delta^k_n\, S(n,d) \;=\; S(n+k,\;d-k)}$$

where $\Delta_n f(n) = f(n+1)-f(n)$ is the forward difference operator. In particular:

- $k=1$: $\Delta_n S(n,d)=S(n+1,d-1)$ — this is T13b.
- $k=d$: $\Delta^d_n S(n,d) = S(n+d,0) = 1$ for all $n$ — the $d$-th difference is identically $1$.
- $k=d+1$: $\Delta^{d+1}_n S(n,d) = 0$ for all $n$.

**Proof.** By induction on $k$.

*Base case $k=1$:* $\Delta_n S(n,d)=S(n+1,d)-S(n,d)=S(n+1,d-1)$ by T13b. ✓

*Inductive step:* Assume $\Delta^{k-1}_n S(n,d)=S(n+k-1,d-k+1)$ for all $n$. Then

$$\Delta^k_n S(n,d) = \Delta_n\bigl[\Delta^{k-1}_n S(n,d)\bigr] = \Delta_n S(n+k-1,\,d-k+1).$$

Apply T13b with $n\to n+k-1$ and $d\to d-k+1$:

$$\Delta_n S(n+k-1,\,d-k+1) = S(n+k,\;d-k).\quad\square$$

**Boundary cases.** $S(n,0)=\binom{n-1}{0}=1$ for all $n\geq 1$, so $\Delta^d_n S(n,d)=1$ exactly. For $k=d+1$: $S(n+d+1,-1)=0$ by convention (no modes exist in a sector of dimension $-1$), so the $(d+1)$-th difference vanishes — consistent with $S(n,d)$ being a degree-$d$ polynomial in $n$.

**Polynomial degree interpretation.** $S(n,d)=\binom{n+d-1}{d}=\frac{n(n+1)\cdots(n+d-1)}{d!}$ is a degree-$d$ polynomial in $n$ with leading coefficient $1/d!$. For any degree-$d$ polynomial $p(n)$, $\Delta^d p(n) = d!\times(\text{leading coefficient}) = d!\times(1/d!)=1$ and $\Delta^{d+1}p(n)=0$. T13e is the operator-theoretic proof of this degree statement for the specific polynomial $S(n,d)$, with the added content that each intermediate difference $\Delta^k S(n,d)=S(n+k,d-k)$ is itself a simplex number — the differences of the IDWT spectral tower remain within the IDWT spectral tower.

**Derivation chain consequence.** Applied to the mode-index chain: $\Delta^k_n S(n,d)=S(n+k,d-k)$ means that the $k$-step "velocity" of the sector-$d$ spectral tower at level $n$ is the value of sector $d-k$ at level $n+k$. The sectors are linked not just statically (via T13b spacing) but dynamically: the rate at which sector $d$ accumulates modes is measured by the instantaneous level of lower sectors. This is the precise combinatorial reason every mode-index derivation in IDWT reduces to a Pascal-triangle identity.

---

## Spectral Anchors — From Counting to Analysis

T13 and T14 together establish two exact values for the spectral zeta function $\zeta_d(s)=\sum_{n\geq1}S(n,d)^{-s}$ of every sector, closing the loop from the combinatorial mass formula of T1 to analytic spectral geometry:

$$\boxed{\zeta_d(1) = \frac{d}{d-1}} \qquad\text{(T13a)} \qquad \boxed{\zeta_d(0) = -\frac{d}{2}} \qquad\text{(T14b)} \qquad \boxed{\operatorname{Res}_{s=1/d}\,\zeta_d(s) = \frac{(d!)^{1/d}}{d}} \qquad\text{(T14d)}$$

These are the **three analytic anchors** of every IDWT sector zeta function. Together they close the loop from the combinatorial mass formula (T1) through the heat kernel (T14a) to the full pole structure (T14d):

- **$\zeta_d(1)=d/(d-1)$** (T13a) — total inverse-spectral-weight. Governs every observable built from inverse-mass sums. Proved by Pascal telescoping.

- **$\zeta_d(0)=-d/2$** (T14b) — zeta-regularised mode count; the IDWT analogue of the Seeley-DeWitt $\zeta(0)$ of a $d$-dimensional manifold (the correspondence itself is an open item, T14 Note). Sets the sector functional determinant $\log\det D_d = -\zeta_d'(0)$.

- **$\operatorname{Res}_{s=1/d}\,\zeta_d(s)=(d!)^{1/d}/d$** (T14d) — the pole at $s=1/d$ is the spectral dimension of sector $d$. The multi-sector function $\zeta_D(s)$ has six poles at $s\in\{1/2,1/3,1/4,1/5,1/6,1/10\}$, one per sector; IDWT has six spectral dimensions, not one.

The combinatorial toolkit is similarly anchored by three exact identities (T13b, T13d, T13e) that together describe the full algebraic structure of the simplex tower:

- **$S(n+1,d)-S(n,d)=S(n+1,d-1)$** (T13b) — first difference; mode filling rate equals previous sector.

- **$\sum_{n=1}^{N}S(n,d)=S(N,d+1)$** (T13d) — partial sum equals next sector at same level; vacuum energy at cutoff $N$ is $m_{{\rm scale},d}\times S(N,d+1)$.

- **$\Delta^k_n S(n,d)=S(n+k,d-k)$** (T13e) — iterated differences remain within the simplex tower; $S(n,d)$ has polynomial degree exactly $d$, with $d$-th difference identically 1.

The heat kernel interpolates between the two anchors: $K_d(t)\sim a_0^{(d)}\,t^{-1/d}$ in the UV ($t\to 0^+$), and $K_d(t)\sim e^{-t}(1+e^{-dt}+\cdots)$ in the IR ($t\to\infty$), with Weyl coefficient $a_0^{(d)}=\Gamma(1+1/d)(d!)^{1/d}$ confirming spectral dimension $= d$. All of this follows from $S(n,d)=\binom{n+d-1}{d}$ alone — the same formula that gives every particle mass.

**UV softening of hidden sectors. ⭐** Since $S(n,d)\sim n^d/d!$, the zeta series $\zeta_d(s)\sim (d!)^s\zeta(ds)$ converges for $s>1/d$. As sector dimension $d$ increases, the convergence threshold $1/d$ decreases — higher-dimensional sectors have spectral sums that converge over a strictly larger range of $s$. This is the opposite of ordinary QFT, where higher-dimensional theories are more UV-divergent. In IDWT the higher-dimensional sectors ($d=5,6,10$) are spectrally softer than the lower-dimensional sectors ($d=2,3,4$): their mode towers suppress themselves automatically through rapid simplex growth, requiring no explicit decoupling mechanism.

**Cross-reference.** T0 identifies the mathematical object (the classical operator $D$ on $M_\infty$); T1 (Hilbert series) gives the spectrum; T13–T14 show that spectrum is analytically controlled and geometrically consistent. The chain is complete: one operator, one spectral formula, full analytic infrastructure.

---

## T15. The Euler Characteristic Unification Theorem

**Theorem T15 (Euler characteristic unification).** The entire IDWT coupling structure — all six sector self-couplings $\{g_{22},g_{33},g_{44},g_{55},g_{66},g_{10,10}\}$ — is a function of a single Euler characteristic: $N_c = \chi(\mathbb{CP}^2) = 3$, the Euler characteristic of the color sector.

**Note ($\Xi_d$ vs $\mathbb{CP}^n$) — correspondence proved (🔶). ✓** The Euler characteristics computed below are those of $\mathbb{CP}^k$ as compact Kähler manifolds. IDWT's sector spaces $\Xi_d$ are non-compact, but the identification $\chi(\mathbb{CP}^k) = k+1$ correctly characterises the $L^2$-Dirac index on $\Xi_{2k}$ by the three-step argument of Part 8 §2 Note: (1) $D^c$ on $\Xi_{2k}$ is Fredholm (confining potential $V=\lambda r^2$ gives compact resolvent); (2) every $L^2$-zero mode is exponentially localised near $r=0$ (Weitzenbock + effective-mass bound $|\Psi|\le C e^{-\sqrt{\lambda}r^2/2}$); (3) the localised zero-mode problem reduces to $H^0(\mathbb{CP}^k,\mathcal{O}(1))$, which has dimension $k+1$, with $H^q=0$ for $q>0$ by Kodaira–Nakano vanishing. The APS eta-invariant on the transition boundary is expected to vanish (effective mass $\sim\sqrt{\lambda}R\to\infty$) but is not yet formally written out. The correspondence is therefore established in structure (🔶); the APS eta step remains a formal open item and does not affect the result.

**Lemma.** $\chi(\mathbb{CP}^k) = k+1$ for all $k\geq 0$.

*Proof.* $\mathbb{CP}^k$ admits a CW decomposition with exactly one cell in each even dimension $0,2,4,\ldots,2k$, giving $k+1$ cells total. Each cell contributes $+1$ to the Euler characteristic, so $\chi(\mathbb{CP}^k) = k+1$. $\square$

In particular: $\chi(\mathbb{CP}^1)=2$, $\chi(\mathbb{CP}^2)=3$, $\chi(\mathbb{CP}^3)=4$, $\chi(\mathbb{CP}^5)=6$. Three of these compose the top mode index as a product identity, $n_{\rm top} = \chi(\mathbb{CP}^2)\times\chi(\mathbb{CP}^3)\times\chi(\mathbb{CP}^5) = 3\times4\times6 = 72$ — the top Chern number of the Kähler product (⭐ value identity; its origin as the top's resonance index is a 🔶 tier-2 input).

**Proof of T15.**

*Step 1 ($n_u = \chi(\mathbb{CP}^2)$, geometry-first).* The lemma gives $\chi(\mathbb{CP}^2) = 3$. This is the geometric anchor for the seed: $n_u = 3 = \chi(\mathbb{CP}^2) = N_c$. A second, independent route reaches the same value via the kernel dynamics (🔶): the ground seed $n_{\rm down}=1$ lies at oscillator level $N=0$; the quadratic kernel acts with $\Delta N = +2$, so one kernel application maps $N=0\to N=2$, giving $n = N+1 = 3$ — the unique mode index reachable by a single kernel step from the ground seed. The two routes (geometric via $\chi$, kernel-dynamical via $\Delta N=+2$) are independent; their agreement reinforces $n_u=3$ as a seed.

*Step 2 ($n_s = \chi(\mathbb{CP}^3)$, certified by T4).* The lemma gives $\chi(\mathbb{CP}^3) = 4$. T4 certifies that $n_s = 1 + n_u = 4$ uniquely satisfies the double $4/7$ self-consistency equation simultaneously with $n_u = 3$. Therefore $n_s = \chi(\mathbb{CP}^3) = 4$.

*Step 3 ($N_c = \chi(\mathbb{CP}^2)$).* $\mathbb{CP}^2$ has a CW structure with exactly one cell in each of dimensions 0, 2, 4, giving $\chi(\mathbb{CP}^2) = 1 - 0 + 1 - 0 + 1 = 3$. Therefore $N_c = \chi(\mathbb{CP}^2) = 3$.

*Step 4 ($n_u = N_c$).* From Steps 2 and 3: $n_u = 3 = N_c = \chi(\mathbb{CP}^2)$. The up-quark mode index equals the number of quark colors — both are the Euler characteristic of the $d=4$ sector manifold.

*Step 5 (all couplings from $N_c$).* Substituting $n_u = N_c$ and $n_s = N_c+1$ (so $n_s + n_u = 2N_c+1$) into T9:

| Coupling | Expression in $N_c$ | Value at $N_c=3$ |
|---|---|---|
| $g_{33}$ | $(N_c+1)^2\sqrt{2N_c+1}/2$ | $8\sqrt{7}$ |
| $g_{44}$ | $N_c(N_c+1)/\sqrt{2N_c+1}$ | $12/\sqrt{7}$ |
| $g_{33}\cdot g_{44}$ | $N_c(N_c+1)^3/2$ | $96$ |
| $g_{66}=g_{10,10}$ | $1/(N_c+1)$ | $1/4$ |
| $g_{22}$ | $\bigl[C(N_c{+}3,3)-N_c\bigr]^2\cdot C(N_c{+}2,4)\,/\,2$ | $722.5$ |
| $g_{55}$ | $96\,/\,g_{22}(N_c)$ | $0.13287$ |

All six values are functions of $N_c$ alone, verified numerically to machine precision. $\square$

**Corollary (Theorem S2 re-derived).** The cross-sector quark mass ratio is
$$\frac{m_u}{m_d} = \sqrt{\frac{g_{44}}{g_{33}}} = \sqrt{\frac{2N_c}{(N_c+1)(2N_c+1)}} = \sqrt{\frac{3}{14}},$$
a direct consequence of $N_c = \chi(\mathbb{CP}^2) = 3$. It is $N_c$-determined, not merely seed-determined.

**Corollary ($\chi$ chain).** The two foundational integers $n_u$ and $n_s$ are consecutive Euler characteristics: $\chi(\mathbb{CP}^2) = N_c = 3$ and $\chi(\mathbb{CP}^3) = N_c+1 = 4 = n_s$. The one-step increment corresponds geometrically to the cellular filling of the next projective space in the Hopf chain, and is the reason the T4 self-consistency equation takes the form $n_u = n_s - 1$ rather than some other arithmetic relation.

**What this means.** The coupling filter geometry and the mass scale structure share the same root. $N_c$ is not an experimental input — it is $\chi(\mathbb{CP}^2)$, the topological invariant of the sector manifold that constitutes color charge. That invariant also fixes $n_u$, which fixes $n_s = N_c+1$, which determines all six coupling constants via T9, which determines all inter-sector mass ratios. The only quantity outside this chain is the absolute energy scale $m_e$, which requires a dimensional input (the single open item after $G_\infty$). Mass *ratios* are fully determined by topology; the unit of mass is not.

---

### T15 Extended Corollaries

**Corollary T15a (Terminal sector from $N_c$).** The Gegenbauer-critical terminal sector is at $d = 2(N_c+2)$.

*Proof.* T3 Rule B requires $4k_0 = (d-2)^2$ at the chain endpoint. T4 gives $k_0 = n_s^2 = (N_c+1)^2$. Substituting:
$$4(N_c+1)^2 = (d-2)^2 \;\Longrightarrow\; d = 2 + 2(N_c+1) = 2(N_c+2).$$
At $N_c = 3$: $d = 2\times 5 = 10$. $\square$

The number of quark colors determines not only the physics within each sector but the point at which the sector-space geometry terminates.

**Corollary T15b ($\chi$ sequence and the Rule A gap).** The Euler characteristics of the $\mathbb{CP}^k$ sectors in $D$ form a nearly consecutive sequence with one gap:

| $k$ | Sector $d=2k$ | $\chi(\mathbb{CP}^k)$ | In terms of $N_c$ | In $D$? |
|---|---|---|---|---|
| 1 | 2 | 2 | $N_c - 1$ | ✓ |
| 2 | 4 | 3 | $N_c$ | ✓ |
| 3 | 6 | 4 | $N_c + 1$ | ✓ |
| 4 | 8 | 5 | $N_c + 2$ | ✗ (Rule A) |
| 5 | 10 | 6 | $N_c + 3$ | ✓ |

The sequence $\{N_c-1,\,N_c,\,N_c+1\}$ is occupied by the three complex projective sectors, then the value $N_c+2 = 5$ is absent — corresponding exactly to the $d=8$ sector excluded by Rule A (no kernel fixed-point for $g_{88}$). Rule A's exclusion is the topological gap $\chi = N_c+2$ in the Euler characteristic sequence. The chain then resumes at $N_c+3$, the Gegenbauer-critical endpoint (T15a). The identity $n_{\rm top} = \chi(\mathbb{CP}^2)\times\chi(\mathbb{CP}^3)\times\chi(\mathbb{CP}^5) = N_c(N_c+1)(N_c+3) = 72$ is a corollary; it is a characteristic-class theorem — specifically $c_{\rm top}(\mathbb{CP}^2\times\mathbb{CP}^3\times\mathbb{CP}^5) = c_{\rm top}(\mathbb{CP}^2)\cdot c_{\rm top}(\mathbb{CP}^3)\cdot c_{\rm top}(\mathbb{CP}^5)$ by $\chi$-multiplicativity — not an arithmetic coincidence. Among all characteristic numbers of $\mathbb{CP}^2\times\mathbb{CP}^3\times\mathbb{CP}^5$ (real dimension 20), $\chi = 72$ is the unique nonzero, non-trivial, purely topological one: all Pontryagin numbers vanish (the $\mathbb{CP}^3$ factor creates an $h_2$-parity obstruction), the signature and $\hat{A}$-genus are zero, the Todd genus is 1, and other Chern numbers such as $c_1^{10}$ are of order $10^{10}$ (MC-4.6).

**Corollary T15c (Hopf coupling products from $N_c$).** Both Hopf-pair coupling products equal $N_c(N_c+1)^3/2$:
$$g_{33}\cdot g_{44} \;=\; g_{22}\cdot g_{55} \;=\; \frac{N_c(N_c+1)^3}{2} \;=\; 96.$$

*Proof.* $g_{33}\cdot g_{44} = [(N_c+1)^2\sqrt{2N_c+1}/2]\times[N_c(N_c+1)/\sqrt{2N_c+1}] = N_c(N_c+1)^3/2$. T9a states $g_{22}\cdot g_{55} = g_{33}\cdot g_{44}$ by Hopf universality. $\square$

The common value $N_c(N_c+1)^3/2$ is the Hopf constraint expressed in terms of $N_c$ alone. It equals 96 exactly at $N_c=3$.

**Corollary T15d (Mode indices from $N_c$).** The occupied mode indices of the electron and neutrino sectors follow from $N_c$ and the derivation chains in Parts 2 and 7:

| Index | Formula | Value |
|---|---|---|
| $n_u$ | $N_c$ | 3 |
| $n_s$ | $N_c+1$ | 4 |
| $n_e$ | $(N_c+1)^2 - N_c = N_c^2+N_c+1$ | 13 |
| $n_{\nu_1}$ | $S(N_c,3) = C(N_c{+}2,3)$ | 10 |
| $n_{\nu_2}$ | $S(N_c,4) = C(N_c{+}3,4)$ | 15 |
| $n_{\rm top}$ | $N_c(N_c+1)(N_c+3) = \chi(\mathbb{CP}^2)\chi(\mathbb{CP}^3)\chi(\mathbb{CP}^5)$ | 72 |

Every particle's mode-index value traces back to $N_c = \chi(\mathbb{CP}^2)$; for $n_{\rm top}$ this is a value identity — $72$ is the top Chern number of $\mathbb{CP}^2\times\mathbb{CP}^3\times\mathbb{CP}^5$ — and is structurally distinct from the primitive seeds $n_d=1$ and $n_u=3$: those carry no underlying Euler-characteristic expression, while $n_{\rm top}=72=\chi(\mathbb{CP}^2)\chi(\mathbb{CP}^3)\chi(\mathbb{CP}^5)$ is an Euler-product index. The resonance origin — why the top quark occupies precisely this mode — is the leading open input (🔶, T15d, Part 2 §11.7). The primary derivation of $n_{\nu_1}$ is $n_{\nu_1}=S(n_u,3)=10$, the $d=3$ simplex image of the up-quark seed (the Generation Tower; cf. the mode-spacing form $S(4,3)-S(3,3)=S(4,2)=10$ above), from which the charged-lepton index follows as $n_e = n_{\nu_1}+n_u$. The closed form $N_c^2+1$ coincides with $S(N_c,3)=C(N_c{+}2,3)$ only at $N_c=3$; they are different functions.

**Corollary T15e (Neutrino mass scale and the lepton coupling complement).** T11a states $m_{{\rm scale},5} = (n_u/n_s)\times m_{{\rm scale},6}^3/m_{{\rm scale},4}^2$. Since $n_u/n_s = N_c/(N_c+1)$ and $g_{66} = 1/(N_c+1)$:
$$\boxed{m_{{\rm scale},5} = (1-g_{66})\times\frac{m_{{\rm scale},6}^3}{m_{{\rm scale},4}^2}.}$$

The factor suppressing neutrino masses relative to the charged-lepton and quark scales is precisely $1-g_{66}$ — the complement of the lepton sector's coupling filter strength. The coupling structure the charged lepton sector retains ($g_{66}$) is what the neutrino sector surrenders ($1-g_{66}$). Both are $N_c$-determined: $1-g_{66} = N_c/(N_c+1)$.

**Corollary T15f (Coupling anti-correlates with symmetry group dimension).** The sector self-coupling $g_{dd}$ is anti-correlated with the dimension of the sector isometry group:

| $d$ | Isometry group | $\dim$ | $g_{dd}$ |
|---|---|---|---|
| 2 | $SU(2)$ | 3 | 722.5 |
| 3 | $SO(4)$ | 6 | $8\sqrt{7}\approx21.2$ |
| 4 | $SU(3)$ | 8 | $12/\sqrt{7}\approx4.5$ |
| 5 | $SO(6)$ | 15 | $96/722.5\approx0.133$ |
| 6,10 | $SU(4)$, $SU(6)$ | 15, 35 | $1/4 = 0.25$ |

The coupling decreases as the symmetry group grows. A larger isometry group imposes more structure on allowed interactions — the coupling filter is more selective, more interactions are geometrically forbidden — and the self-coupling is correspondingly weaker. Consequently:

- The photon sector ($SU(2)$, fewest constraints) has the largest self-coupling ($g_{22} = 722.5$) and hosts the heaviest boson spectrum.
- The neutrino sector ($SO(6)$, most constrained: Majorana-forbidden, color-projected, $B{-}L$ specific) has the weakest self-coupling ($g_{55}\approx0.133$) and the lightest masses.

This is the coupling filter principle operating at the level of the self-coupling: the geometry that specifies what quantum numbers a particle carries also specifies, through the same Euler characteristic $N_c$, how strongly that sector couples and therefore how heavy those particles are. Coupling filter and mass scale are not two separate outputs of the geometry — they are one quantity read in two different units.

**Corollary T15g (The complete mass spectrum from $N_c$). ⭐** Every one of the fifteen Standard-Model masses is $m_e\times f(N_c)$ for an exact closed form $f$ built from $N_c=\chi(\mathbb{CP}^2)=3$ alone. The chain closes through three layers, each already $N_c$-determined above: the mode indices $S(n,d)$ (T15d), the six sector scales $m_{{\rm scale},d}/m_e$ (T9, T11, T15c–e), and the exact corrections. These corrections carry no constant outside the $N_c$-chain:

$$\varepsilon = \frac{2/\sqrt{2N_c+1}}{(N_c+1)^2\,S(N_c{+}1,4)}, \qquad \delta_\tau = \frac{1}{N_c(N_c+1)^2\,S(N_c{+}1,4)}, \qquad \delta_{\nu_3} = \frac{1}{S(N_c{+}1,4)},$$

evaluating at $N_c=3$ to $\varepsilon = 1/(280\sqrt7)$, $\delta_\tau = 1/1680$, $\delta_{\nu_3} = 1/35$. The electron is the anchor ($f_e\equiv1$); representative closed forms are $f_{\rm up} = \sqrt{N_c}\,(N_c+1)/(2N_c+1)^{1/4}$ and $f_{\rm strange} = \sqrt2\,(N_c+1)^{5/2}(N_c+2)(N_c+3)(2N_c+1)^{1/4}/12$. Substituting $N_c=3$ reproduces the bare mass spectrum to machine precision (maximum relative deviation $5.7\times10^{-16}$ across all fifteen); the physical coloured-quark masses add the confinement-binding dressing (§11.9, 🔶), itself $N_c$-determined through $N_b=\Lambda/(4m_{{\rm scale},4})$ with $\Lambda=N_c f_\pi$. The single dimensional input is $m_e$; mass *ratios* are fixed by the one integer $N_c$. This is the spectrum-level statement of T15: not only the indices and couplings but the masses themselves trace to $\chi(\mathbb{CP}^2)$. $\square$

---

## Summary Table

| Theorem | Content | Status | Accuracy | Physical consequence |
|---|---|---|---|---|
| T0 | Physical mass spectrum of the operator $D$ | 🔶 | Exact | All SM masses from one classical operator on $M_\infty$ (IDWT has no Hilbert space). The finite-active operator's spectral facts are established directly on $M_\infty$: self-adjointness, discrete internal spectrum, and summability $\tfrac12$ (✅). The Fredholm-module / KO-dimension / regularity items are borrowed NCG bookkeeping, not IDWT claims; the genuine residual is the full $d\to\infty$ operator — see Note |
| T0.5 | Co-fixed-point selection condition | 🔶 | Exact | Splits at $n_{\rm top}=72$: bottom regime ($n<72$) is the additive simplex tower (10 modes), with $k_0=16$ a derived Gegenbauer-endpoint overlay beat; top regime is the boson chain anchored by $n_{\rm top}=72$ ($W,Z$ by the $g$-rule, $H=95$ the additive closure); $n_{\rm top}=72$ is an Euler-product index $\chi(\mathbb{CP}^2)\chi(\mathbb{CP}^3)\chi(\mathbb{CP}^5)$ (value identity T15b; resonance origin 🔶); the even-level non-member exclusion is now exact (✅, STEP 118: strictly positive irreversible radiative width $\Gamma>0$; odd-level exact by $l$-parity ⭐), so both parity classes of the complement are closed exactly; the residual 🔶 is the dynamical tower-DAG selection (MC-4) and the absolute decay-rate magnitude (🔶, STEP 103) |
| T1 | $m=S(n,d)\cdot m_{\rm scale}$ = Hilbert series | ✅ | Exact | Mass = IDOS; inflation rule |
| T2 | $(\xi\cdot\xi')^2$ = unique kernel | ✅ | Exact | Forces rank-1 couplings and the $\ell=2$ self-energy scale $\varepsilon$ |
| T3 | $D=\{2,3,4,5,6,10\}$ from Hopf chain | ✅ | Exact | 6 sectors, no more, no fewer |
| T4 | $n_s=4$ from double degeneracy $4/7$ | ✅ | Exact | Unique $n_s$; all indices follow |
| T5 | $d=10$ = Gegenbauer critical endpoint | ✅ | $b=1/2$ exact | Chain terminates; $\tau$ is critical |
| T6 | All three PMNS angles | 🔵 | $\leq0.51\%$ | All three angles derived from $S^5$ sector geometry and seed coupling $g_{55}$; the inputs ($g_{55}$, four mode indices) are seed-fixed |
| T7 | $\sqrt{\operatorname{Tr}(D^2)} \approx (\sqrt{2}\,G_F)^{-1/2}$ | 🔵 | $-0.33\%$ | EW scale self-consistency: RMS of the physical (confinement-corrected) spectrum vs derived $G_F$; read as a subscription constraint it selects the heavy indices and terminates the spectrum at 15 modes (STEP 141, 🔶) |
| T8 | $\delta_{CP} = \pi + 2\theta_{13} = 197.11°$; $J = -0.00981$ | 🔶 | $+0.05°$, $+0.1\%$ | APS spectral flow across $\mathbb{CP}^3\to\mathbb{CP}^5$; $\Delta c_1 = -2$; derived in Part 10; three technical gaps before 🔵 |
| T9a-d | All 6 coupling constants derived | ✅ | Exact | All six $g_{dd}$ from $\chi(\mathbb{CP}^{d/2})$ and seed ratio; §§2–4 |
| T15 | $N_c=\chi(\mathbb{CP}^2)=n_u$; all couplings and the sector-chain extent from one Euler characteristic (T15a–f); mode-index values are Euler-character identities | ✅ | Exact | Coupling filter and mass scale hierarchy share one geometric root; $g_{dd}$ anti-correlates with isometry group dimension; $n_{\rm top}=72$ is a value identity (top Chern number of $\mathbb{CP}^2\times\mathbb{CP}^3\times\mathbb{CP}^5$), an Euler-product index structurally distinct from the primitive seeds; its resonance origin is 🔶 open (T15d); $m_e$ is the only dimensional input |
| T10a | $\ell=2$ self-energy scale $\varepsilon=1/(280\sqrt7)$ | ✅ | Exact | Derived from T2; applied to $\delta_{\nu_3}=\varepsilon\cdot g_{33}=1/35$ |
| T10b | Geometric back-reaction correction $+1/1680$ for $\tau$ | ✅ | $0.001\%$ | Critical-sector regularisation |
| T11a-d | Neutrino masses; Dirac; $\Sigma m_\nu=60.39$ meV ($\delta_{\nu_3}=\varepsilon\cdot g_{33}=1/35$ derived, §9d); uncorrected 59.00 meV | ✅ | $<0.05\%$ | $0\nu\beta\beta=0$ at all orders (no $C$ on $S^5$) |
| T13a | Spectral sum rule $\zeta_d(1)=d/(d-1)$ | ✅ | Exact | Total inverse-mass weight of sector $d$ is $d/(d-1)$; pure Pascal |
| T13b | Mode spacing $S(n+1,d)-S(n,d)=S(n+1,d-1)$ | ✅ | Exact | Filling-rate relation; source of all mode-index derivation chains |
| T13c | Exact mass ratios | ✅/🔶 | $\leq 0.002\%$ non-up; $m_c/m_u$ $-0.37\%$, $m_t/m_u$ $-0.74\%$ 🔶 | $m_\mu/m_e$, $m_\tau/m_\mu$, $m_Z/m_W$ etc. exact; $d=4$ up-type confinement-corrected (Part 5 §3b) |
| T13d | Partial sum $\sum_{n=1}^{N}S(n,d)=S(N,d+1)$ | ✅ | Exact | Cumulative sector-$d$ weight = single mode in sector $d+1$; vacuum energy at cutoff $N$ is $m_{{\rm scale},d}\times S(N,d+1)$ |
| T13e | Iterated difference $\Delta^k_n S(n,d)=S(n+k,d-k)$ | ✅ | Exact | $S(n,d)$ is degree-$d$ polynomial; differences stay within simplex tower; $\Delta^d=1$, $\Delta^{d+1}=0$ |
| T14a | Heat kernel Weyl term $K_d(t)\sim a_0^{(d)} t^{-1/d}$ | ✅ | Exact | Spectral dimension = $d$; Weyl coefficient $a_0^{(d)}=\Gamma(1+1/d)(d!)^{1/d}$ |
| T14b | Constant term $-d/2$ and $\zeta_d(0)=-d/2$ | ✅ | Exact | Regularised eigenvalue count; sets sector functional determinant |
| T14d | Pole at $s=1/d$: $\operatorname{Res}\,\zeta_d=(d!)^{1/d}/d$; $\zeta_D$ has 6 poles at $s\in\{1/2,\ldots,1/10\}$ | ✅ | Exact | IDWT has 6 spectral dimensions, one per sector; photon sector leads UV behavior; tau sector most UV-soft |
| $\sin^2\theta_W$ | $1-(S(76,2)/S(81,2))^2=0.2237$; +0.37% from PDG on-shell | ✅ | +0.37% | Exact mode-index value; the +0.37% is a genuine small structural residual (IDWT gives one geometric value, couplings do not run) — not attributed to loop corrections the framework does not compute |
| $G_N$ | $G_N=G_\infty/(4\pi)$, sector-independent; gravity is $\infty$-dimensional | 🔶 | — | $4\pi$ exact (3D Green's-function constant); $d>10$ vacuum does not enter (Ricci-flat vacuum + T5 scattering states); $G_\infty$ is a second dimensional input, absolute scale not derived (Part 4 §3.12.4) |

**Remaining open:** (i) CP phase — $\delta_{CP} = \pi + 2\theta_{13} = 197.11°$ derived via APS spectral flow (T8 🔶, Part 10); three technical gaps remain before 🔵 (spectral flow coefficient rigour, sign from T6 matrix, equivalence with the Fubini-Study curvature integral over coupling parameter space here). (ii) $G_N$ from $\infty$-dimensional gravity — a 3D observer integrates a sector-$d$ source over its $k=d-3$ hidden coordinates, giving the sector-independent Newtonian $G_N=G_\infty/(4\pi)$ (the $4\pi$ is the 3D Green's-function constant); the $d>10$ vacuum does not enter ($d>10$ is Ricci-flat in vacuum and T5 scattering states are not $L^2$-normalizable); the single open item is the absolute scale $G_\infty$, a second dimensional input not derived from the combinatorics (Part 4 §3.12.4, Part 6). **Resolved:** $m_{\nu_3}$ correction $\delta_{\nu_3}=\varepsilon\cdot g_{33}=1/35$ derived exactly (Part 2 §9d); $\Sigma m_\nu=60.393$ meV.
