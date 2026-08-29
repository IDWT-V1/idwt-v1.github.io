# Infinite Dimensional Wave Theory, Second Edition — Part 3: Forces and Couplings

## 0. What this Part teaches

By the end of this Part you can answer, with mechanisms rather than names: why electromagnetism reaches everything charged and falls off as $1/R$ in a universe of many dimensions; why quarks are confined and what colour actually is; why the weak interaction touches only left-handed particles; **why neutrinos barely interact with anything**; where the electric charges $+2/3$, $-1/3$, $-1$ come from; what the numerical values of the couplings are and how to compute them; and how quark mixing probabilities are calculated from the same counting function that priced the masses.

There is one interaction in this framework — the wave's quartic self-coupling on shared sector coordinates (Part 1 §1.2) — and the "forces" are that single coupling read through different sector geometries. Two questions govern every case: *containment* (do the two structures share coordinates at all?) and the *filter* (what does each geometry permit on the shared coordinates?). Both must pass.

**Force is interference — and the claim is checked mathematics, not imagery.** Before the individual forces, see what the single coupling *is* when two particles are present. There is one wave, so "two particles" means two centered ripple patterns of the same field (Part 1 §1.4): $\Psi = \Psi_A + \Psi_B$. Write the local moduli and relative phase as $a$, $b$, $\delta$, so the joint intensity is $|\Psi|^2 = a^2 + b^2 + 2ab\cos\delta$, and put it into the quartic self-coupling. The expansion is exact:

$$|\Psi_A+\Psi_B|^4 = \underbrace{a^4 + b^4}_{\text{each pattern's self-binding}} \;+\; \underbrace{4a^2b^2}_{\text{phase-blind interaction}} \;+\; \underbrace{4ab\,(a^2+b^2)\cos\delta + 4a^2b^2\cos^2\delta - 2a^2b^2}_{\text{phase-sensitive interaction}}.$$

Averaging over the relative phase $\delta$ kills every phase-sensitive term and leaves exactly $4a^2b^2$: the density-against-density coupling — the form the kernel wears throughout this edition — is the *phase-blind core* of the interference, present between any two patterns whatever their frequencies (two particles of different mass are standing waves of different pitch, so their coherent terms average away, but their intensities always meet). The phase-sensitive terms ride on top wherever a definite relative phase is held. One interaction, two physical faces: an always-on intensity–intensity piece, and a coherent piece that can push or pull.

The coherent piece has a clean force law, worth displaying because it is the engine of the long-range forces. Two coherent centered ripple fields, each thinning geometrically from its center as $\phi_i = q_i/(4\pi|x-x_i|)$, have mutual interference energy

$$E_{\rm int} = \int \nabla\phi_1\!\cdot\!\nabla\phi_2\;d^3x = \frac{q_1\,q_2}{4\pi R}$$

— an exact identity (verified symbolically and on the grid in the computation record): energy falling as $1/R$, force as $1/R^2$, and the *sign flips with the relative phase* ($q_2\to-q_2$ turns attraction into repulsion). Two in-phase ripple sources pull together; two opposed ones push apart. This is measured classical physics as well as theorem — the Bjerknes forces between pulsating bubbles in water are exactly this pattern — and it is the framework's answer to what charge *is* at the level of mechanism: attraction versus repulsion is relative phase between centered ripples, carried here on the $d=2$ phase component.

The self-terms are what hold each particle together (Part 1 §1.3). *Everything we call force between them is the cross terms* — contributions that exist only where the two patterns overlap and interfere. Force is not something added to the wave picture; it is what one wave's self-intensity does when two of its ripple patterns share territory. Three structural facts follow at once:

- **The dimensional gate.** The cross terms are integrals, nonzero only where *both* patterns have structure — the shared sector coordinates. Patterns with no shared structured dimensions generate no interference and no force. Containment is an overlap condition on ripples.
- **The two ranges.** A massive pattern's ripples die off steeply near its own scale (self-concentration is what mass *is*), so direct pattern-on-pattern interference gives the short-range, contact-scale forces — the strong interaction below. But the wave has genuinely unbounded components: the massless $d=2$ phase ripple carries no envelope and thins only geometrically, like a real lake ripple crossing ever larger circles — and interference through *that* component is long-range. Its geometric thinning, read by a three-dimensional observer, is the $1/R$ of §1.2: the inverse-square law is the intensity falloff of an unbounded ripple.
- **Attraction and repulsion are phase relationships.** Interference can reinforce or cancel, so interference forces carry a sign set by the relative phase of the two patterns — and this is not a metaphor but measured classical physics: pulsating bubbles in water push and pull each other through their ripples (the Bjerknes forces), in-phase pairs attracting, out-of-phase pairs repelling. Like and unlike charges are the framework's version of that phase relationship, carried on the $d=2$ phase component.

---

## 1. Electromagnetism: the phase of the wave

### 1.1 The photon is a ripple of pure phase

$\Psi_\infty$ is complex, so it has a phase everywhere, and phase is physical: the wave's conserved density (Part 1 §5.3) is the Noether charge of exactly this phase symmetry. Write the wave locally as $\Psi = A\,e^{i\theta}$. On the $d=2$ plane — the sector every other sector contains — the gradient of the phase defines a field:

$$A_\mu = \partial_\mu\theta, \qquad F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu.$$

This *is* the electromagnetic potential and field strength: Maxwell's source-free structure is the statement that $F$ is the curl of a gradient's connection, and the Lorentz force is geodesic motion of a charged mode in this phase geometry. The photon is the $d=2$ sector's ground mode — the propagating ripple of phase with nothing excited, hence (Part 2) exactly massless.

Why does everything charged feel it? Containment: the two coordinates of the $d=2$ plane are literally two coordinates of every sector, so a phase ripple in that plane is a perturbation *inside* every charged particle's own coordinate space. Nothing is exchanged and nothing propagates "to" the electron; the photon's plane is part of the electron.

The masslessness is protected twice over, and the protection is worth seeing because it is a parity argument a reader can check. The kernel's angular factor $(\xi\cdot\xi')^2$ is *even* under $\xi\cdot\xi' \to -(\xi\cdot\xi')$, so its expansion in angular harmonics contains only even terms ($\ell = 0$ and $\ell = 2$), with the $\ell=1$ coefficient exactly zero. A photon mass would require the kernel to generate an $\ell = 1$ (vector) self-energy — and the matrix element $\langle\gamma|K|\gamma\rangle$ vanishes identically, at every order, because the coefficient it needs does not exist. The photon cannot be given a mass by the only interaction in the theory.

### 1.2 Why $1/R$ survives infinitely many dimensions — the projection theorem

The inverse-square law is supposed to be the signature of three dimensions; a world with large extra dimensions should show forces dying faster. Here is why it doesn't, worked in full, because the integral is short and the conclusion is load-bearing for the whole framework.

A particle interacting in $d\ge3$ dimensions has the $d$-dimensional Coulomb kernel $G_d(r) = 1/r^{d-2}$. A three-dimensional observer cannot resolve the $k = d-3$ hidden coordinates and integrates over them. With $R$ the observable distance and $y$ the hidden radial coordinate,

$$\varphi_{\rm obs}(R) = S_{k-1}\!\int_0^\infty \frac{y^{\,k-1}\,dy}{(R^2+y^2)^{(d-2)/2}},$$

$S_{k-1}$ the hidden unit-sphere area. Substitute $y = R\tan\alpha$; the integral becomes a beta function, and the power of $R$ that survives is

$$R^{\,k - (d-2)} = R^{\,(d-3)-(d-2)} = R^{-1} \qquad \text{for every } d.$$

The extra integrations cancel the extra powers of $r$ *exactly*, in every sector. What changes with $d$ is only a dimensionless prefactor ($C_3 = 1$, $C_4 = \pi$, $C_6 = \pi^2$, $C_{10} = \pi^4/6$). So:

**A three-dimensional observer sees $1/R$ from a source of any dimensionality.** The inverse-square force law is not evidence that reality has three dimensions — it is what *any* higher-dimensional interaction looks like through a three-coordinate window. The hidden dimensions were never hiding from force-law tests; they are structurally invisible to them. (Part 4 runs the same integral for gravity, with the same conclusion plus a bonus: the observed Newton constant.)

One corollary sharpens the point: if the Coulomb law came from the photon propagating in its *own* two dimensions, the potential would be logarithmic ($2$D Green's function), which is wrong. The $1/R$ belongs to the projection, not to the photon's sector — the force law is a fact about observers.

---

## 2. Colour: three classes and an admissibility rule

### 2.1 What colour is

The $d=4$ geometry $\mathbb{CP}^2$ has isometry group $\mathrm{SU}(3)$ and exactly three independent classes ($\chi = 3$). A quark bound in that geometry therefore carries a three-component internal state, transforming in the fundamental of $\mathrm{SU}(3)$ — not because a gauge group was chosen, but because three components in the fundamental is what the shape of the well provides. *Colour is the coordinate frame of the quark's own space.* Down-type quarks, whose three dimensions nest inside the four, inherit the same structure through containment.

The colour interaction is the kernel's direct $d=4$ contact term, $\mathrm{SU}(3)$-symmetric because the geometry is. There is no gluon field and nothing propagates colour; the covariant bookkeeping of local colour-frame freedom exists (a connection can be written from the wave's own colour components, and it transforms correctly), but the action contains no kinetic term for it — it is geometry, not a dynamical field. Consequently the framework predicts *no glueballs*: there is no colour field to bind into one, and any claimed glueball must resolve into an ordinary quark-sector resonance (a falsifier — Part 6).

### 2.2 Confinement as admissibility

Assign each quark its colour expectation vector $\vec n$ (the eight isometry-generator expectations; antiquarks carry $-\vec n$). The unique $\mathrm{SU}(3)$-invariant energy linear in the total is

$$E_{\rm conf} = \lambda_c\,\Bigl|\sum_i\vec n(q_i)\Bigr|.$$

Its consequences are immediate: a colour-matched quark–antiquark pair, or one quark of each colour, sums to zero and costs nothing; every other combination carries energy growing with its net colour. An isolated quark is therefore not an expensive state but an *inadmissible* one — like a wave required to close on itself failing to close. Confinement here is a selection rule on what can exist in isolation, not a dynamical tug-of-war; scattering can no more liberate a single colour than it can produce half a standing wave.

The scale is derived and triple-checked. From Part 2 §8.1, $\Lambda = N_c f_\pi = 282$ MeV, and the colour energy coefficient built from it reproduces three measured quantities at once: the string tension $\sqrt\sigma$ (within $0.5\%$ of the Regge determination), the Regge slope $\alpha' \approx 0.89$ GeV$^{-2}$, and the deconfinement temperature $T_c \approx 266$ MeV — one derived scale, three observables.

**Why the attraction grows with distance — the interference mechanism (candidate).** The linearity itself has a mechanism in the interference picture of §0, presented here as a candidate: the shape and the scale both land, and the coefficient-level derivation is open work.

Two colour-locked quarks are phase-locked ripple patterns of the one wave, and between two coherent centers stands an interference fringe field. Pull the centers apart and that field does not fade — it *lengthens*: one more fringe fits into the gap per wavelength of separation, and each fringe carries a fixed quantum of energy. Constant energy per unit separation is a linear potential. What makes this happen for colour and for nothing else is where the interference energy is allowed to go. An electromagnetic disturbance rides the massless phase mode and radiates freely into the bulk — its interference energy spreads over all space, thinning geometrically into the $1/R$ Coulomb energy. A *colour-carrying* disturbance has no such exit: by the admissibility rule above, a colour-nonsinglet ripple is not a permitted configuration of the bulk wave, so the colour mismatch between separating quarks cannot disperse as radiation. It is forced to stay strung along the line between the centers, keeping the one wave colour-closed — and energy that must connect two points and may not spread lives in a tube, growing with its length. *The string is the standing colour ripple the wave is obliged to maintain between centers it is not allowed to disconnect.*

The linearity itself is a two-line theorem once said this way, and it is verified in the computation record: a standing channel of fixed amplitude $A$ and wavenumber $k$ held between two locked centers carries uniform energy density $A^2k^2/2$, so the energy in the gap is *exactly*

$$E(L) = \frac{A^2k^2}{2}\,L \qquad\Longrightarrow\qquad \sigma = \frac{A^2k^2}{2}$$

— linear to machine precision, with the tension as one scale squared. That is the shape the committed scale-match found: with amplitude-scale and wavenumber both at the colour scale, $\sigma \sim \lambda_c^2 = 0.179\ \mathrm{GeV}^2$, against the lattice's $0.18$–$0.19$ and phenomenology's $\sim900$ MeV/fm (here: $908$). The mechanism predicts the *square*; what remains underived is the $O(1)$ amplitude coefficient from the kernel.

**The short-range physics: repulsion, attraction, and unmasking.** Attraction is half the story. When two quark patterns *overlap*, the phase-blind interference term is strictly positive — $+4a^2b^2$, the checked identity of §0; the kernel is a sum of squares — so overlapping cores genuinely push apart, with a push that fades on the contact scale because it exists only where the cores overlap. Riding alongside it at short range are the *phase-sensitive* coherent terms, which for a colour-locked pair pull; the net short-range force is the competition of the two, and in the quark–antiquark singlet channel the measured answer (the lattice's Cornell form, $-a/r + \sigma r$) is weak net attraction up close. The framework reads that weakness as near-cancellation plus geometric dilution ($g_{\rm eff} = g_{dd}/S(n,d)$ — §2.3): quarks inside a hadron feel almost nothing locally, the native counterpart of asymptotic freedom, and the hadron's size is that weak net potential balancing the quarks' own standing-wave spread. The positive overlap push does claim one famous strong-force phenomenon outright: the *hard core* between nucleons — two colour-singlet composites resist merging with a repulsion that dies over the contact scale, which is the empirical nucleon–nucleon core.

- **The attraction "strengthens" with distance** without any force strengthening: the constant string pull $\sigma$ is progressively *unmasked* as the short-range overlap physics — push and coherent pull alike — dies away, until the bare tension is all that remains. And at sufficient stretch, creating a new quark pair is cheaper than another fringe, which is why pulling on quarks yields hadrons, never free colour. This unmasking is the whole of the strong force's famous "weirdness," and it is independent of the short-range sign details.

Status, plainly: the admissibility rule and the $\sigma = \lambda_c^2$ scale are committed results; the fringe linearity and the positivity of the overlap push are verified identities; the assembled account — fringes plus overlap physics reproducing the Cornell shape — is a *candidate* mechanism awaiting the kernel-level computation of the fringe amplitude (the $O(1)$ coefficient) and the channel-resolved short-range sign.

### 2.3 The coupling strength

The effective colour coupling comes from integrating the kernel over the $\mathbb{CP}^2$ volume ($\pi^2/2$ in sector units):

$$g_s^2 = \frac{2\,g_{44}}{\pi^2} = \frac{2\times12/\sqrt7}{\pi^2} = 0.919.$$

And the framework's replacement for "running": the coupling felt by mode $n$ is the sector coupling diluted over the mode's states, $g_{\rm eff} = g_{dd}/S(n,d)$ — a power-law dilution over configurations, not a logarithmic renormalization flow. At the strange level, $g_{\rm eff} = 21.17/20 \approx 1.06$: the crossing of unity that located the confinement scale in Part 2 §8.1.

---

## 3. The weak interaction: the handedness of complex geometry

### 3.1 Where handedness comes from

Four sectors — $d = 2, 4, 6, 10$ — are complex (Kähler) geometries, and a complex structure is an *oriented* structure: multiplication by $i$ rotates every tangent plane in a definite sense. Concretely, on a Kähler sector of complex dimension $m$, the spinor bundle decomposes by anti-holomorphic degree,

$$S = \Lambda^{0,0}\oplus\Lambda^{0,1}\oplus\cdots\oplus\Lambda^{0,m},$$

and the Kähler form assembles a chirality operator $\gamma_5^{\rm K}$ that grades this sum: odd degrees are one handedness (call it left), even degrees the other. This is an intrinsic property of the geometry — the real spheres $d=3$ and $d=5$ have no complex structure, no such operator, and hence no handedness of their own.

### 3.2 Why the weak coupling touches only the left

The weak structure is the $\mathrm{SU}(2)$ part of the $d=4$ geometry's internal symmetry $U(2)$ (the isotropy group in $\mathbb{CP}^2 = \mathrm{SU}(3)/U(2)$), and it acts on the *holomorphic tangent directions* — which is exactly the $\Lambda^{0,1}$ summand and nothing else. Run the ledger for $d=4$ ($m=2$):

- $\Lambda^{0,0} = \mathbb{C}$: a $U(2)$ singlet — right-handed, weak-blind ($u_R$, $d_R$);
- $\Lambda^{0,1} = \mathbb{C}^2$: the fundamental $U(2)$ doublet — left-handed ($u_L, d_L$);
- $\Lambda^{0,2}$: a determinant character — again a singlet, right-handed.

The left-handed doublet and the sterile right-handed singlets of the Standard Model are, line for line, the anti-holomorphic degrees of the quark sector's own spinor bundle. Nothing was chosen: the weak interaction sees only the left because only the odd-degree forms live in the representation the geometry gives it to act on. The lepton sector ($m=3$) splits the same way, $4$ left and $4$ right per spinor.

The vector-like sectors inherit. Down-type quarks ($S^3$, no handedness) couple weakly through their containment in $d=4$ and the cross-coupling $g_{34}$ — their observed left-handedness is borrowed from the complex sector above them. The neutrino ($S^5$) likewise has no chirality operator of its own, which is the first half of why it is a Dirac particle; the second half is sharper and comes next.

### 3.3 The Dirac lock on the neutrino

Spinor algebra depends on dimension mod 8, and $d = 5$ is the unique class in which *neither* a reality (Majorana) condition *nor* a chirality (Weyl) condition can be imposed: no charge-conjugation matrix with the required properties exists on the five-sphere's spinor bundle at all. Consequently no term of the lepton-number-violating form $\psi^T C\psi$ can even be *written* for neutrino modes — not suppressed at low energy, not forbidden by a symmetry that might break: unwritable, at every order, forever. Neutrinos are Dirac fermions; neutrinoless double beta decay never occurs; there is no see-saw and no heavy Majorana partner. This is the framework's sharpest falsifier (Part 6), and it comes from nothing but the dimension of the neutrino's home.

---

## 4. Why neutrinos barely interact with anything

The neutrino's famous aloofness — trillions passing through your body per second, interactions per lifetime countable on one hand — is, in this framework, four independent doors closing, each for a stated geometric reason:

**The electromagnetic door: closed.** Coupling to the photon requires charge — a nonzero eigenvalue under the phase geometry of §1. The neutrino's charge, computed in §5 below from the same eigenvalue bookkeeping that prices every other particle, is exactly zero: $Q = T_3 + Y = \tfrac12 - \tfrac12 = 0$. No charge, no phase coupling, no electromagnetic interaction at any strength. (Containment holds — the neutrino's five dimensions contain the photon's plane — but the filter projects the coupling to zero. Containment without the filter is nothing.)

**The colour door: closed by fibration.** The neutrino's coordinates contain the entire colour sector ($\Xi_4 \subset \Xi_5$), so naively it should feel the strong force. But the neutrino's geometry is the *circle bundle over* the colour geometry ($S^1\to S^5\to\mathbb{CP}^2$), and averaging around the fiber circle projects every colour representation onto its invariant part — the singlet. The neutrino is colour-neutral not by assignment but because its own shape averages colour away.

**The Majorana/exotic door: unwritable.** §3.3 — no lepton-number-violating vertex of any kind exists for it.

**What remains: the weak channel, and only weakly.** The one interaction the geometry permits is the $\mathrm{SU}(2)$ coupling on the left-handed component (§3.2) — and even that is quantitatively feeble, for a scale reason Part 2 §3.2 derived: the neutrino sector has no self-closure (its sphere is neither complex nor a group), its coupling is the forced hand-me-down $g_{55} = 96/g_{22} = 0.133$ — the *smallest* sector coupling, five thousand times below the electroweak sector's — and its mass scale is borrowed through the fibration at $10^{-13}$ MeV. A particle whose only open channel is the weak vertex, in the sector with the feeblest coupling and the shallowest well, is a particle that crosses light-years of lead. Nothing about this is tuned; it is what lives at the address $d=5$.

The same accounting, run for the other extreme, is worth one sentence: the tau's ten dimensions contain *every* sector, every door stands open, and correspondingly the tau decays into everything — electrons, muons, pions, kaons, multiple neutrinos — with no channel dominant, its coupling weight spread thin by the critical-endpoint geometry (Part 1 §3.3). The interaction personality of every particle in the table is readable this way: which doors its geometry opens, and how wide.

---

## 5. Charges are eigenvalues

The Standard Model's hypercharge assignments — the strange fractions that make anomalies cancel — are outputs here. The hypercharge generator is not new structure: it is the diagonal generator $T_8$ of the colour geometry's own isometry group, the one singling out the fiber direction, normalized by the lepton coupling:

$$Y = \frac{1}{\sqrt3}\,T_8 = \frac{1}{6}\,\mathrm{diag}(1,1,-2), \qquad Y_L = -\sqrt{g_{66}} = -\tfrac12.$$

Charges follow from $Q = T_3 + Y$:

| mode | $T_3$ | $Y$ | $Q$ |
|---|---|---|---|
| $u_L$ | $+\tfrac12$ | $+\tfrac16$ | $+\tfrac23$ |
| $d_L$ | $-\tfrac12$ | $+\tfrac16$ | $-\tfrac13$ |
| $\nu_L$ | $+\tfrac12$ | $-\tfrac12$ | $0$ |
| $e_L$ | $-\tfrac12$ | $-\tfrac12$ | $-1$ |

Fractional quark charges are the price of a single class in a three-class geometry — $Y_Q = 1/(2N_c) = 1/6$ — not a convention. And the four anomaly-cancellation conditions, which the Standard Model must arrange by hand, cancel identically, as they must for eigenvalues of one geometry's generators. Display the checks; each is one line of arithmetic:

$$[\mathrm{SU}(2)]^2[U(1)]: \quad 3\times\tfrac16 + (-\tfrac12) = 0.$$
$$[\mathrm{SU}(3)]^2[U(1)]: \quad 2\times\tfrac16 - \tfrac23 + \tfrac13 = 0.$$
$$[\mathrm{grav}]^2[U(1)]: \quad 6\times\tfrac16 + 2\times(-\tfrac12) - 3\times\tfrac23 + 3\times\tfrac13 + 1 = 0.$$
$$[U(1)]^3: \quad 6(\tfrac16)^3 + 2(-\tfrac12)^3 - 3(\tfrac23)^3 - 3(-\tfrac13)^3 + 1 = 0.$$

The generation count comes from the same class accounting: the lepton geometry has four classes, one of which is the constant/vacuum class — not a particle — leaving three generations. Four minus the vacuum is three.

---

## 6. The coupling numbers

The coupling strengths descend from the sector couplings of Part 2 §2 through one cascade with no adjustable step:

$$g_{44} \;\xrightarrow{\ \mathbb{CP}^2\text{ volume}\ }\; g_s = \sqrt{\tfrac{2g_{44}}{\pi^2}} \;\xrightarrow{\ \times\,Q_u\ }\; g_2 = \tfrac23\sqrt{g_s} \;\longrightarrow\; \sin^2\theta_W \;\longrightarrow\; g_1,\ \alpha.$$

Evaluate each step. $g_s = \sqrt{0.919} = 0.9587$. The factor $2/3$ entering the weak coupling is the up quark's charge from §5 — and, not coincidentally, the ratio of the photon's dimension count to the colour count, $d_{\rm photon}/N_c = 2/3$; the same number for a geometric reason. So

$$g_2 = \tfrac23\sqrt{0.9587} = 0.65275 \qquad(\text{measured } 0.65270,\ +0.008\%).$$

The Weinberg angle is a *mass ratio* — hence, by Part 2, a ratio of state counts:

$$\sin^2\theta_W = 1 - \frac{m_W^2}{m_Z^2} = 1 - \left(\frac{S(76,2)}{S(81,2)}\right)^2 = 1 - \left(\frac{2926}{3321}\right)^2 = 0.2237$$

against the on-shell $0.2229$ — a $+0.37\%$ residual, the largest structural residual in the coupling sector, stated as such. Equivalently $\cos\theta_W = 2926/3321 = 0.88106$ against $0.88108$. From $g_2$ and the derived W mass,

$$G_F = \frac{g_2^2}{4\sqrt2\,m_W^2} = 1.1658\times10^{-5}\ \mathrm{GeV}^{-2} \qquad(\text{measured } 1.1664\times10^{-5},\ -0.05\%)$$

— the Fermi constant, the strength of every beta decay, with no Higgs vacuum value anywhere in its derivation (the framework has no spontaneous symmetry breaking; the electroweak scale is simply $(\sqrt2\,G_F)^{-1/2} = 246$ GeV, and the Higgs is a particle like any other). The $\rho$ parameter is exactly 1 for free: W and Z inhabit one sector, so the custodial symmetry the Standard Model must arrange is automatic. Downstream, $g_1 = g_2\tan\theta_W$ and the fine-structure constant follow; these are defined at the sector scale and *do not run* (couplings dilute over states, §2.3, they do not renormalize), so comparisons to values quoted at the Z mass require the standard vacuum-polarization translation on the other side — done consistently, $\alpha$ lands on the measured value with the residual traceable to the $\sin^2\theta_W$ gap above.

---

## 7. Quark mixing: the counting function again

### 7.1 The mechanism

When a down quark becomes a strange quark at a weak vertex, what sets the probability? The same physics as the Born rule (Part 1 §5.3): relative intensity. A mode spread over $S(n,d)$ configurations carries amplitude $1/\sqrt{S(n,d)}$ per configuration at the shared coordinates — normalization spreads it thin — so the transition weight between a lighter and heavier mode of one sector is the intensity ratio

$$|V|^2 = \frac{S(n_{\rm light},d)}{S(n_{\rm heavy},d)}.$$

Mixing is not new machinery: it is the mass law's own counting, pointed at transitions. Heavier modes mix in weakly because their amplitude is diluted over more configurations — the *same* dilution that makes their effective coupling small (§2.3).

### 7.2 The Cabibbo angle, with its correction derived

Down $\to$ strange, both in $d=3$:

$$\sin^2\theta_C = \frac{S(1,3)}{S(4,3)} = \frac{1}{20} \;\Longrightarrow\; \sin\theta_C = 0.22361 \quad\text{(bare)}.$$

Measured: $0.22450\pm0.00044$. The bare count sits $-0.4\%$ ($2\sigma$) low, and — in keeping with this edition's discipline (Part 2 §5) — it is *left standing*: one integer ratio, one square root, no adjustment. For the record, the first edition carries a found-after-the-fact candidate for exactly this gap (a curvature correction from the mediating sector's sphere, the heat-kernel factor $(1-Rt/12)$ giving $\sin\theta_C = (1+1/240)/\sqrt{20} = 0.22454$, $+0.09\sigma$) — geometric in every ingredient, and discovered, like the mass corrections, by hunting the residual. The reader can weigh it with that provenance known.

### 7.3 The rest of the matrix

Up $\to$ charm, both in $d=4$:

$$|V_{cb}| = \sqrt{\frac{S(3,4)}{S(20,4)}} = \sqrt{\frac{15}{8855}} = 0.04116 \qquad(\text{measured } 0.04100\pm0.0014,\ +0.11\sigma),$$

and by third-row unitarity $|V_{ts}| \approx |V_{cb}|$ ($-0.96\sigma$). The matrix is *exactly unitary by construction* — mixing weights are intensity fractions of one wave, and fractions sum to one — so exact first-row unitarity is a prediction, not bookkeeping. The measured first row currently misses unitarity by $\sim3\sigma$ (the "Cabibbo angle anomaly," a tension internal to the measurements: beta-decay $|V_{ud}|$ versus kaon $|V_{us}|$); the framework agrees with the kaon determination at $0.1\sigma$ and stakes itself on unitarity holding as the measurements settle. If exact unitarity is cleanly excluded, the counting mechanism is falsified — Part 6 carries it as such.

The remaining entries — the tiny $|V_{ub}|$ and the CP-violating phases — involve cross-sector transitions between a complex and a real geometry, and carry mechanisms the framework has sketched but not settled: the quark CP phase localizes to the single charge-permitted cross-sector hop and comes out as a winding of $67.5°$ against the measured $\sim65.7°$, and the same counting law applied to that hop gives $|V_{ub}| = 3.7\times10^{-3}$ ($-0.6\sigma$). Both are presented in Part 6 among the candidate results, with their open premises named, rather than claimed here as settled.

The lepton-side mixing (the PMNS matrix) rests on a genuine symmetry worth stating even in brief: the electron/muon sector and the tau sector couple to neutrinos with *identical* strength ($g_{56} = g_{5,10}$, since $g_{66} = g_{10,10}$ — Part 2 §2.2), making the maximal atmospheric mixing angle a symmetry consequence rather than a coincidence; the measured deviations from the symmetric values track the small neutrino self-coupling $g_{55} = 0.133$. The three predicted angles sit within $0.5$–$1\%$ of the measured values (Part 6 table).

---

## 8. Putting it together: interference × dimensionality = the forces

Assemble the pieces of this Part and of Part 1, and the coverage closes. The interference of §0 supplies exactly **two faces** of one interaction — the phase-blind push (positive, always on, alive wherever intensities overlap) and the coherent face (sign set by relative phase, alive wherever a definite phase relationship is held) — riding on **three kinds of carrier**: overlapping cores (fading on the contact scale), constrained channels that may not disperse (constant force, by the fringe law), and unbounded massless components (thinning only geometrically, hence long-range). Dimensionality then does the distribution: *which* particles feel *which* face through *which* carrier is fixed by which coordinates their sectors share (containment), what each sector's geometry permits on them (the filter), and what a three-dimensional observer's projection turns the law into (§1.2). Every force phenomenon in physics is a cell of that small product:

| phenomenon | interference face | carrier | dimensional gate | resulting law |
|---|---|---|---|---|
| electromagnetism | coherent (sign = phase) | unbounded massless phase component | $d=2$ plane inside every charged sector | $1/R^2$, attracts or repels |
| weak interaction | coherent, handed | gapped channel of the complex geometry | left-handed components, every fermion sector | short range $\sim 1/m_W$ |
| strong, short-range | *both*: blind push + colour-locked pull | overlapping quark cores | quark block $\{3,4\}$ only | contact range, weak net (Cornell short-range) |
| confinement | coherent, constrained | strung colour channel (admissibility forbids dispersal) | colour only | linear, $\sigma = \lambda_c^2$ |
| nuclear hard core | phase-blind push | overlapping singlet composites | shared $d=3$ | fading repulsion at the contact scale |
| collective-channel attraction | phase-blind, through the condensate | screened condensate response | all sectors, coupling $\propto m_1m_2$ | short range $\sim1/m_H$ |
| **gravity** | **not interference** — the one exception, proved (Part 4) | the manifold itself | all axes, no sector boundary | $1/R^2$, $\propto m_1m_2$, unscreenable |

Read the table's logic: the *faces* explain sign (why electromagnetism both attracts and repels while the blind push only pushes); the *carriers* explain range (contact, linear, infinite — nothing else is available to a wave); the *dimensional gates* explain reach (why electromagnetism is universal among the charged, colour never leaves the quark block, the weak coupling touches every fermion but only half of it, neutrinos feel almost nothing, the tau feels everything); and the projection theorem explains why every long-range entry lands on the same $1/R^2$ for us regardless of the source's dimensionality. The exhaustiveness is not an accident of listing: the rank-1 theorem (Part 1 §1.2) says the wave possesses exactly *one* interaction channel, so the faces and carriers above are the complete repertoire of what that single self-coupling can do — and the manifold's response to energy density (gravity) is the one interaction that is not the wave talking to itself, established by the framework's own failed attempt to make it one. One wave, one self-coupling, one geometry: full coverage of force.

## 9. What this Part leaves open

The linearity of the confinement energy at mechanism level (§2.2 — the invariant form and the scale are in hand). The counting law's underlying premise — that a localized mode loads its configurations with equal weight — proved as a geometric identity on every sector shape, with its physical applicability resting on the particle-size result of Part 4. The $+0.37\%$ Weinberg residual. The closed form of charge quantization — why the fiber topology's integers yield exactly thirds — stated as open. And the cross-sector CP structure, held at candidate status. None of these is a place where a measurement disagrees with a computed number; across this Part, everything measured sits within a fraction of a percent of a value computed from the geometry and two integers.

---

*Second edition, 2026. Full derivations and machine verification: first-edition Parts 3, 8, 10 at https://fedgeno.github.io/; the computation record `idwt-v2.py` is distributed with these documents.*
