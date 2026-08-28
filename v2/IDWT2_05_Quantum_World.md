# Infinite Dimensional Wave Theory, Second Edition — Part 5: The Quantum World

## 1. Quantum mechanics is what a wave looks like from inside three of its dimensions

Part 1 set the stage: we are three-dimensional structures registering a wave that extends further. This Part collects what follows — which turns out to be, item by item, the entire quantum catalogue. None of it is postulated here. Each entry is a consequence of one wave plus the observer's vantage.

**Wave–particle duality.** There are only waves. What reads as a "particle" is a detection: the density–density self-coupling firing at a point, at a rate set by the local wave intensity. The wave is always a wave; the point-like click is a property of the interaction, not of the object.

**The Born rule.** Derived, not assumed (Part 1). The wave's phase symmetry makes $|\Psi|^2$ the conserved amount of wave; detections are density-against-density couplings, so detectors fire in proportion to local intensity; probability is relative rate. The same argument runs in any basis a detector can physically couple to — the rate for outcome $a$ is the wave's intensity in that channel, which is exactly $|\langle\phi_a|\Psi\rangle|^2$ relative to the total. One scope note with real content: only kernel-reachable bases are measurable. The framework does not grant measurement in arbitrary abstract bases — an observable is something the wave's coupling can actually touch — and this restriction costs nothing observed while trimming the measurement postulate's excess generality.

**Uncertainty.** Perspective, not ontology. Every particle is definite and sharp in its own dimensions; an observer resolving fewer dimensions sees the marginal — the object with its unseen coordinates integrated out — and a marginal is irreducibly spread. The electron's position "uncertainty" is the information living in the three coordinates we do not have.

**Pauli exclusion and statistics.** The wave is a spinor field, and spinor components anticommute: two identical fermionic excitations cannot occupy one mode, and the multi-electron state is antisymmetric under exchange — not as a new axiom but as the algebra of the one field. Spin-½ itself comes from the wave being a Dirac spinor on the manifold; antiparticles are its conjugate components, automatic in any complex spinor field.

**Entanglement.** Correlation in coordinates that three-dimensional distance does not measure. Two electrons far apart in our three dimensions can share sector coordinates outright; measuring one reads a jointly-held state, and nothing travels because nothing was ever separated. The correlations violate Bell's inequalities exactly as observed — the shared reality is in the sector coordinates, which locality-in-three-dimensions never constrained — while signalling remains impossible, since each local detection is still governed by local intensity.

**Why detection comes in clicks.** A detector is bound matter, and bound systems have discrete spectra; an exchange with a detector must land on one of its discrete states, so continuous wave intensity is read out in quanta. The quantum itself — the size of one excitation — is the framework's one genuine import beyond structure: the unit of action, the role $\hbar$ plays everywhere, here entering as the definition of a single excitation of the wave. That this import is *irreducible* has been shown; that it is *one* import, not many, is part of the framework's economy. What is not yet derived is the completion dynamics — the moment-by-moment account of a transition finishing — which shares a wall with absolute decay rates and is stated as open in Part 6.

## 2. The atom, actually

Here is what an atom is in this framework. The nucleus, a colour-neutral composite, is a purely three-dimensional object. The electron is a six-dimensional one, executing a definite closed orbit in its six dimensions, bound to the nucleus through the two-dimensional electromagnetic plane both contain. From the electron's vantage, it orbits something geometrically thin — present in three of its six directions and absent from the rest. From ours, we see the orbit only where it crosses our slice.

Everything textbook-quantum about atoms is this picture read from three dimensions:

- **Orbital shapes.** The s, p, d, f shapes are the three-dimensional projections of the orbit's angular-momentum states — genuine shadows of a definite six-dimensional path, historically misread as clouds of chance. Their degeneracies, shell counts, and selection rules fall out of the sector's symmetry chain.
- **The spectrum.** The three-dimensional marginal of the electron's dynamics is exactly the standard Coulomb problem — the Bohr spectrum, with the Rydberg built from the framework's own derived couplings.
- **Exact agreement, by theorem.** A result called Marginal Exactness closes the loop: every observable a three-dimensional apparatus can measure is fixed by the three-dimensional marginal alone, and that marginal is the standard molecular Hamiltonian. The framework therefore reproduces tested atomic and molecular physics *identically* — not approximately — and the possible residue from the wave's cross-sector contact coupling is bounded below one part in $10^9$, beneath every chemical measurement. This is a feature, not a retreat: a century of spectroscopic agreement is inherited wholesale, while the ontology under it changes completely.
- **New ontology, honestly labeled.** The sector's state space contains orbit states with no three-dimensional counterpart — hidden components at every shell that no three-dimensional probe can reach at any order. Their inaccessibility is itself a theorem, so they are ontology rather than a lab prediction; a measured coupling to one would falsify the sector identification.

## 3. Chemistry with the mystery removed

Chemistry's oddest conventions become theorems here, and one number is worth the price of the whole Part. Hybridization — the $sp^3$ mixing chemists invoke for carbon — is in this framework a *basis choice*: the sector's symmetry rotates freely among the three-dimensional projections of one orbit, at no energy cost. Bonding electrons at a center occupy mutually orthogonal directed states (orthogonality is free, from exchange antisymmetry), each containing an equal share of the isotropic state; pure linear algebra then forces the bond directions to satisfy

$$\cos\theta = -\frac{1}{n-1}$$

for $n$ equivalent bonds: $180°$ for two, $120°$ for three, and $\arccos(-1/3) = 109.47°$ — the tetrahedral angle of carbon, the shape of methane and of diamond — for four, with no empirical input anywhere. The same machinery caps equivalent bonds at four unless d-states enter, and with them forces six-coordinate centers into the octahedron's exact $90°$. Water's $104.5°$ and ammonia's $107.8°$ sit in a one-parameter family (lone pairs hoard slightly more of the isotropic share); the parameter's monotone trend with lone-pair count is reproduced, its value not yet derived.

The rest of the periodic table's skeleton follows the same way: shell capacities from the sector state count, the filling order from screening in the marginal problem, aromaticity's $4n+2$ rule from the closed-shell structure of one ring-spanning orbit — with the ring-current sign pattern (inner protons shielded, outer deshielded) coming out of the loop geometry correctly. Multi-electron energetics are standard variational work in the inherited Hamiltonian; a first helium bound lands within two percent, with the deficit being ordinary correlation energy, exactly as standard theory prices it.

## 4. What the quantum world is not, here

It is worth stating the negatives plainly, because they are where interpretation debates dissolve.

There is no collapse: a detection is an interaction with an outcome, and the wave continues being a wave. There is no fundamental randomness: probability is relative detection rate over a definite substrate, and what looks random is the unseen coordinates' information. There is no measurement problem in the usual sense — measurement is not a special process outside the dynamics but the same kernel coupling as everything else, restricted to channels it can reach. There is no many-worlds branching and no pilot wave riding on configuration space: there is one wave on one manifold, and the classical world of Part 1 — three-dimensional observers made of colour-neutral bricks — is a *derived* feature of it. What remains genuinely unfinished is stated in Section 1: the completion dynamics of a transition, and with it absolute rates. The interpretation is settled by construction; the unfinished part is a calculation, not a mystery.

---

*Second edition, 2026. Derivations and numerical verification: first-edition Parts 1, 8, 11 and `files/idwt.py` at https://fedgeno.github.io/.*
