# IDWT Appendix B — Tower and Index Patterns

*Part of the IDWT Appendix A working log (§10–20).*
*See also: Appendix A (§1–9), B (§10–20), C (§21–41 selected), D (§15,22,42–43,48), E (§31,38,44–47).*

---

### §10. New additive forms of the mode indices

**Cross-sector ratio identity:**  
n_charm × N_c = n_ν₁ × N_f = 4 × n_ν₂  
✅ Polynomial identity (holds for all n_s). All three equal n_s(n_s−1)(n_s+1)(n_s+2)/6. Proof: n_charm = C(n_s+2,3), N_c = n_s−1 → product = C(n_s+2,3)·(n_s−1) = n_s(n_s+1)(n_s+2)(n_s-1)/6. n_ν₁ = C(n_s+1,3), N_f = n_s+2 → product = same. 4·n_ν₂ = 4·C(n_s+2,4) = same. Equivalently: n_ν₁/n_ν₂ = 4/N_f and n_charm/n_ν₁ = N_f/N_c. These are simplex ratio identities following directly from the binomial formula. The ratio of the first two neutrino mode indices equals 4/(n_s+2) for any n_s; at n_s=4 this is 2/3. Verified: n_s=3: 10=10=20 ✓; n_s=4: 60=60=60 ✓; n_s=5: 140=140=140 ✓.

**Charm–up spacing equals p:**  
n_charm − n_up = **p** (for all n_s)  
✅ By definition: p = S(n_s,3) − n_up = n_charm − n_up. Restated as a sector-spacing identity: the quark mode-index gap within d=4 from depth-0 to depth-1 equals the Dirac eigenstate count p that enters g₂₂.

**Neutrino spacing identity:**  
n_ν₃ − n_ν₂ = n_ν₁ − n_up (for all n_s)  
✅ Follows from n_ν₃ = n_ν₁ + n_ν₂ − n_up → n_ν₃ − n_ν₂ = n_ν₁ − n_up. At n_s=4: 22−15 = 10−3 = 7.  
❓ Additional claim: n_ν₃ − n_ν₂ = n_s + n_up = 7 at n_s=4. True numerically but fails at n_s=5 (n_ν₃−n_ν₂=16≠9). The value 7 = n_s+n_up also appears as the radicand under √ in g₃₃; whether this connection is structural is unresolved.

**Second neutrino minus electron equals q minus n_up:**  
n_ν₂ − n_e = q − n_up  
✅ Proof: n_ν₂ − n_e = [S(n_up,4)] − [S(n_up,3) + n_up] = [S(n_up,4)−S(n_up,3)] − n_up = q − n_up, using the definition q = S(n_up,4)−S(n_up,3) and the tower identity n_e = n_ν₁ + n_up. At n_s=4: q−n_up = 5−3 = 2, so n_ν₂ = n_e + 2.

**d=3 sector sum equals q:**  
n_down + n_strange = 1 + 4 = **5 = q** (for any n_s: n_down + n_s = n_s+1 = q)  
✅ Immediate from n_down = 1 and n_strange = n_s.

**d=4 sector sum equals Higgs:**  
n_up + n_charm + n_top = **n_H** (documented, §5)

**Higgs as Z plus electron plus down:**  
n_H = n_Z + n_e + n_down  
✅ Follows from n_H = n_Z + n_ν₂ − n_down (§5) and n_ν₂ = n_e + 2·n_down (from n_ν₂ − n_e = q − n_up = 2 at n_s=4, with n_down=1).

---

The following identities hold **only at n_s=4** (verified to fail at n_s=3,5,6). They are recorded as observed coincidences without mechanism. Status: ❓

**n_μ + n_ν₂ + n_ν₃ = 72 = n_top** ❓ (fails at n_s=3: 27≠12; n_s=5: 156≠266)

**n_top + n_τ = 95 = n_H** ❓ (fails at n_s=3: 19≠8; n_s=5: 318≠309)

**(n_s+1)(n_s+n_up) = n_μ** ❓ (fails at n_s=5: 54≠70)

**n_e + n_τ = 36 = N_f²** ❓ (fails at n_s=5: 76≠49)

**n_ν₁ + n_ν₃ = 32 = 2⁵** ❓ (fails at n_s=5: 71≠64; note 32 = 2^(n_s+1) only at n_s=4)

**n_charm = 2·n_ν₁** ❓ (C(n_s+2,3)/C(n_s+1,3) = (n_s+2)/(n_s-1) = 2 only at n_s=4; consequence of Pascal row n_s+1=5 having equal middle entries C(5,2)=C(5,3)=10)

**n_top − n_charm = n_s·n_e = 52** ❓ (fails at n_s=5: 231≠120)

**Each massive d=2 boson pairs with one matter mode to the Hopf product 96 = N_c(N_c+1)³/2 = g₃₃g₄₄ = g₂₂g₅₅** ❓ (2026-06-13):
n_W + n_charm = 76 + 20 = 96 (charm, d=4);
n_Z + n_ν₂ = 81 + 15 = 96 (ν₂, d=5);
n_H + n_down = 95 + 1 = 96 (down, d=3).
One matter primary from each of the three matter sectors d=3,4,5, reflected through the carrier 96, lands on a d=2 boson — ascending bosons W<Z<H pair with descending matter charm>ν₂>down (the sideband-about-carrier reflection that surfaced in the modulational-comb run, §15 2026-06-13). All three are n_s=4 specific exactly as the single n_Z+n_ν₂ case is (fails at n_s=5: 310≠192; the value 96=N_c(N_c+1)³/2 is fixed by N_c while the indices scale with n_s). Honest caveat: 96 minus the seven primaries also produces four non-tower values {61,86,92,93}, so the pairing is an exact relation for {W,Z,H} but not a spurious-free generator. Not a structural identity; companion to the run #5 heavy-boson-off-top cascade (Part 3 §11) and the §13 Vandermonde forms, recorded here as the completed ❓ pattern. Do not promote to a Part document without an n_s-general derivation.

**Tau identities at n_s=4:**  
n_τ = n_charm + n_up = n_e + n_ν₁ = 23 🔵 (both are consequences of n_charm=2·n_ν₁ which is itself ❓)

**n_μ = n_ν₃ + n_e = 22 + 13 = 35** ❓ (fails at n_s=3: 13≠15; n_s=5: 75≠70. Equivalent to n_charm = 2·n_ν₁: n_ν₃ + n_e = 2n_ν₁ + n_ν₂ while n_μ = n_charm + n_ν₂. Found 2026-06-10.)

**Three "+1" offsets in the compact tower form all equal n_down = 1. ❓** (2026-06-09, Fable-5 pass)

The compact tower relations for the three heaviest modes contain a "+1" offset whose origin is underived:
- n_τ = n_ν₃ + n_down (explicit in Part 5 §6; the +1 here is n_down = 1)
- n_top = T − r + 1 (compact form; r is a simplex evaluation; the +1 is uninterpreted)
- n_H = T + a + 1 (compact form; a is an additive index; the +1 is uninterpreted)

Observation: all three are consistent with the +1 being the down-quark seed n_down = 1. Reading the two underived offsets as T − r + n_down and T + a + n_down reduces the unexplained residue from "three bare integer units" to "why n_down = 1 attaches at the three anchor/heaviest-mode vertices." This is a physical question — the d=3 seed touching the three heaviest modes — rather than an arithmetic blemish. At n_s = 4 this is numerically invisible (n_down = 1 regardless), but the reframing is consistent with the DAG structure where every additive edge adds either a seed index or a simplex evaluation.

Status: ❓ Observation only; no mechanism derived. Fails to add new numerical content but unifies the three offsets under a single seed label.

### §11. Modular structure (mod n_s)

Writing n = n_s · a + r, the working set partitions into four residue classes mod n_s = 4:

| r | Members | Character |
|---|---------|----------|
| 0 | 0 (γ), 4 (s), 16 (k₀), 20 (c), 72 (t), 76 (W) | bosons and quark scale anchors; all divisible by n_s |
| 1 | 1 (d), 13 (e), 17 (p), 81 (Z) | d=3 ground state, d=6 ground state, g₂₂ parameter, Z boson |
| 2 | 10 (ν₁), 22 (ν₃) | **exclusively ν₁ and ν₃** |
| 3 | 3 (u), 15 (ν₂), 23 (τ), 35 (μ), 95 (H) | up quark plus lepton/Higgs cluster |

Residue 2 contains only ν₁ and ν₃. The algebraic reason: n_ν₃ − n_ν₁ = n_ν₂ − n_up = 15 − 3 = 12 = 3·n_s ≡ 0 mod n_s. The second neutrino escapes to residue 3 because S(n_up,4) − S(n_up,3) = q = 5 ≡ 1 mod 4, not 0.

### §13. W-Z mode gap equals q

n_Z − n_W = q = n_s + 1  
✅ Polynomial identity (holds for all n_s). Proof: n_W = g(d_ν, n_top) = d_ν + n_top − 1 = (n_s+1) + n_top − 1 = n_top + n_s. n_Z = g(d_ℓ, n_W) = d_ℓ + n_W − 1 = (n_s+2) + n_W − 1 = n_W + (n_s+1). So n_Z − n_W = n_s+1 = q exactly.

The same q appears in three further contexts (all polynomial identities or definitions):
- q = S(n_up,4) − S(n_up,3) (definition, §6)
- n_ν₂ − n_ν₁ = q (follows from q's definition and n_ν₁ = S(n_up,3), n_ν₂ = S(n_up,4))
- n_down + n_strange = q (= 1+n_s = n_s+1 = q, trivially)
- n_Z − n_W = q (proved above)

❓ Additional observation at n_s=4: q = 5 = χ(CP⁴), the Euler characteristic of the missing sector d=8. Whether the W-Z spacing equalling the missing sector's Euler characteristic is structural or coincidental at n_s=4 is unresolved.

### §13a. The Vandermonde g-rule transition graph on the mode set

Define g(d, n) = d + n − 1, the row index of mode (n,d) in the Pascal triangle. Computing g(d, n_j) for every d ∈ D = {2,3,4,5,6,10} and every n_j ∈ NS yields **19 NS → NS transitions** out of 90 candidate (d, n_j) pairs. (Hit rate ≈ 21%; random baseline ≈ 16%.)

**The 19 transitions, by sector:**

| d | NS → NS transitions |
|---|--------------------|
| 2 | 0→1, 3→4, 22→23 |
| 3 | 1→3, 13→15, 20→22 |
| 4 | 0→3, 1→4, 10→13, 20→23 |
| 5 | 72→76 |
| 6 | 10→15, 15→20, 76→81 |
| 10 | 1→10, 4→13, 13→22, 72→81 |

**Graph structure on NS:**  
- **Sources** (no in-edge): **{0, 35, 72, 95}** = {photon, muon, top, Higgs}.  
- **Component A** (reachable from photon via g-rule alone): {0, 1, 3, 4, 10, 13, 15, 20, 22, 23} — the ten lightest particles, equivalently the seeds plus depth-1 HS evaluations plus the electron and tau.  
- **Component B** (reachable from top): {72, 76, 81} — top → W (d=5) and top → Z (d=10), W → Z (d=6).  
- **Isolated sources**: {35, 95} — muon and Higgs have no g-rule predecessor in NS.

**Erratum (2026-06-18): the graph above omitted the bottom quark.** The NS set used here is the 15-element set with the photon indexed at 0 and the bottom quark **left out** — so it never tested 16. On the correct 15-mode set (photon at the d=2 ground state, bottom beat 16 included), 16 is g-reachable: 16 = 15 + 1 (d=2, from ν₂) and 16 = 13 + 3 (d=4, from the electron), so 16 joins Component A. The bottom regime (n < 72) under the g-rule is then Component A ∪ {35}, with the muon the only g-isolated bottom member. This does not promote the g-rule to a generator: its forward closure from the seed n=1 covers every integer 1–71, so it is an adjacency relation, not a selector — the selective law on the bottom regime is the additive simplex tower of §13b, and 16 (k₀ = n_s²) is an overlay beat on it, not a tower output (`files/idwt.py` STEP 91; Part 9 T0.5). The four-source count and Components A/B above describe the bottom-quark-omitted graph and are kept for the record.

**Why the four sources.** For each source s, no (d, n_j) ∈ D × NS satisfies d + n_j − 1 = s with n_j ≠ s:

- 0 (photon): trivially a source.  
- 35 (muon): 35 = S(n_s, n_s) is the composite-square self-image; not a g-rule output of any other NS member.  
- 72 (top): the open eigenmode-selection mode index; not in the g-rule image of NS.  
- 95 (Higgs): the high-mass empirical closure; not in the g-rule image of NS.

**Structural reading.** The g-rule alone organises ten of the fifteen particles into a single connected component rooted at the photon. The W and Z sit one and two g-steps from the top quark, making them genuinely "top-anchored" rather than independent generators. Muon and Higgs are g-rule isolated: the muon is a pure depth-1 HS evaluation (S(4,4) = 35) and the Higgs is the empirical closure. Both top and Higgs are presently the un-derived rules of the generation tower, and both are graph sources — suggesting that the open derivation problem (§5, n_top) and the empirical closure (§5, n_H) are at the *structural* source of the spectrum, not anomalies layered on top of it.

**Own-sector stepping sub-pattern (❓, 2026-06-10).** Four of the 19 transitions use d' = d_own + 1, i.e. the g-step n → n + d_own: down (1,3) → strange (4), ν₁ (10,5) → ν₂ (15), ν₂ (15,5) → charm (20), top (72,4) → W (76). Equivalently, for exactly these four particles n + d_own is itself a tower mode index; the other eleven all fail (verified over the full 15). The steps chain — down → strange, ν₁ → ν₂ → charm, top → W — with each step equal to the particle's own sector dimension. Whether d' = d_own + 1 has a kernel or Hopf-chain interpretation is open. Side observation: strange (4,3) and up (3,4) share n + d = 7.

### §13b. Confluence of the generation tower — corrected analysis (2026-05-29)

**Two distinct predecessor relations.** The §13b analysis was initially run with the GENERAL additive predecessor: any n = a+b−c with a,b ∈ NS, c ∈ {0,1,3,4}. This was then corrected to examine the TOWER-SPECIFIC directed predecessor: the actual named operations of the generation tower (Part 2 §6). The two give very different results.

**GENERAL additive predecessor: cyclic graph, no source nodes.**
Under any a+b−c=n (a,b ∈ NS, c ∈ {0,1,3,4}), ALL 15 NS particles have predecessors in NS. Specifically:
- Photon (0,2): (1,3)+(3,4)−4 = 0 — predecessors: down and up.
- Down (1,3): (0,2)+(4,3)−3 = 1 — predecessors: photon and strange.
- Up (3,4): (0,2)+(4,3)−1 = 3 — predecessors: photon and strange.
- Strange (4,3): (1,3)+(3,4)−0 = 4 — predecessors: down and up.

The L-particles form a cycle: photon ↔ {down,up}; strange ↔ {down,up}. There are **no source nodes** under the general relation. The original §13b claim "seeds have no predecessors" was a verification gap: Test 5 hardcoded {(1,3),(4,3)} as seeds and skipped computing their predecessors.

**TOWER-SPECIFIC directed predecessor: acyclic DAG, unique seeds. ✅**
Using only the actual operations of the generation tower (Part 2 §6), the derivation is a finite acyclic DAG (verified: `has_cycle = False`). Each particle has a unique tower-derivation predecessor:

| Particle | Derivation | Tower predecessors |
|----------|------------|-------------------|
| photon (0,2) | d=2 ground state (n=0 trivially) | none — always present |
| down (1,3) | SEED: S(1,d)=1 for all d | none |
| strange (4,3) | COMPOSITE: n_s = n_d + n_u = 1+3 = 4 (🔶 MC-4.4); confirmed by muon fixed point S(4,4)=35 | {down, up} |
| up (3,4) | SEED: n_u = χ(CP²) = N_c = 3 (T15); unique ΔN=+2 image of ground seed | none |
| nu1 (10,5) | S(n_u,3) = 10 | {up} |
| charm (20,4) | S(n_s,3) = 20 | {strange} |
| electron (13,6) | n_nu1 + n_u = 13 | {nu1, up} |
| nu2 (15,5) | S(n_u,4) = 15 | {up} |
| muon (35,6) | n_charm + n_nu2 = 35 | {charm, nu2} |
| nu3 (22,5) | n_nu1 + n_nu2 − n_u = 22 | {nu1, nu2, up} |
| tau (23,10) | n_nu3 + n_down = 23 | {nu3, down} |
| top (72,4) | S(n_e,2) − n_charm + 1 = 72 | {electron, charm} |
| W (76,2) | g-rule: n_top + d_ν − 1 = 76 | {top} |
| Z (81,2) | g-rule: n_W + d_ℓ − 1 = 81 | {W} |
| Higgs (95,2) | n_u + n_charm + n_top = 95 | {up, charm, top} |

Derivation depths: down and up at 0 (seeds); strange, nu1, nu2 at 1; electron, charm, nu3 at 2; tau, muon, top at 3; W, Higgs at 4; Z at 5. All 13 derived particles (excluding photon ground state) reach {(1,3),(3,4)} in at most 5 backward steps. Verified: `all particles reduce to {down, up}`.

**Seed minimality.** Neither single seed alone generates all NS via tower operations (down alone: 1/15; up alone: 2/15). Together, {down, up} generate all 14 non-photon particles (14/15), with strange as their offset-additive composite at depth 1. The photon (n=0, d=2 ground state) is always present independently of the seeds — it does not require derivation.

**Why {(1,3),(3,4)} and not some other pair.** n_down=1 is forced by S(1,d)=1 for all d (the universal harmonic oscillator ground state); n_u=3 is forced by χ(CP²)=N_c=3 (T15, ✅). The composite n_s=4 = n_d+n_u is confirmed by T4 (Part 9) and χ(CP³)=4.

**Status.** The tower derivation is a finite acyclic DAG with unique source nodes {(1,3),(3,4)} (⭐, verified), composite (4,3) at depth 1. The general additive predecessor graph is cyclic with no source nodes (verified, §15 dead end).

**Seed sector derivation (🔵, 2026-05-29).** The seed sector is d=3: it is the observable spacetime sector and the first total space S³ of the complex Hopf chain, the natural starting point of the generation tower. The primitive seeds are n_d=1 (ground state S(1,d)=1 in d=3) and n_u=3 (forced by χ(CP²)=N_c=3, T15). The composite n_s=4 = n_d+n_u is confirmed by T4 (Part 9) and the muon fixed-point S(4,4)=35. Full sector assignments then propagate via the Hopf chain structure (d=3→4→5→6,10) and trivial automorphism group — see P8 update in Part 1.

**DAG automorphism group is trivial (⭐, 2026-05-29).** The tower DAG has no non-trivial automorphisms. The only degree-compatible candidate swaps are {down ↔ strange}, {nu1 ↔ nu2}, and {tau ↔ muon}; all three fail because they violate specific predecessor constraints:

- down ↔ strange: blocked because charm has predecessor {strange} only; no NS particle has predecessor {down} only.
- nu1 ↔ nu2: blocked because electron has predecessors {nu1, up}; no NS particle has predecessors {nu2, up}.
- tau ↔ muon: blocked because muon has predecessors {nu2, charm}; tau has predecessors {down, nu3} — different composition entirely.

The full backtracking search over all 15! possible permutations (with degree-pruning) confirms: **exactly one automorphism exists — the identity**. The particle labeling is uniquely determined by the DAG structure. No alternative sector/mode-index assignment preserves the derivation order. This resolves GPT's question about graph automorphisms: there is no relabeling freedom, so the coupling vector v and the rank-1 structure G_{dd'} = v_d v_{d'} are the unique coupling structure consistent with the tower DAG. The seed values (n_d=1, n_u=3) and composite n_s=4 remain the fundamental inputs; the automorphism result says that given those values, the entire labeling of the spectrum is rigid.

### §16. Mass uniqueness test for sector assignments

**Question.** Do the 15 observed SM particle masses, together with the IDWT mass formula m = S(n,d) × m_scale_d and sector scales derived from m_e and the seeds, uniquely identify the (n,d) sector assignments?

**Tests performed** (2026-05-29):

**Within Σ_indices × D only:** For each particle, given the known n, the known d is the unique minimiser of the log-residual |log(S(n,d)×m_scale_d / m_obs)|². Margin of uniqueness: 10³–10⁹× over the next-best d. Conversely, given the known d, the known n is the unique minimiser. No pairwise swap of the global assignment reduces the total squared log-residual (known total: 1.35×10⁻⁴, essentially zero). 100,000 random alternative global bijections all have residuals ≥ 10⁵× worse.

**Full scan (n ∈ [1,500], d ∈ D):** For every particle, there exist non-Σ_indices n-values within factor 2 of the observed mass in some sector. Examples: (59,4) hits W mass within 0.7%; (126,6) hits top mass within 0.4%; (11,2) hits tau mass within 2%. These are not tower outputs.

**Conclusion.** Mass matching with IDWT-derived scales does not uniquely identify Σ_indices at the individual level. The discrimination is collective: the Σ_pairs assignment achieves sub-percent accuracy for all 15 masses simultaneously — a constraint that random or arbitrary alternative assignments fail by factors of 10⁵. The sector assignments are over-determined by both the generation tower (algebraic derivation from seeds) and the mass data (empirical confirmation). Neither source alone is sufficient to close the argument: the tower provides the structured derivation; the masses confirm it cannot be replaced by an unstructured alternative. The sector-assignment derivation remains open but the empirical case for the known assignment is strong.

### §17. Prime-factor count of mass eigenvalues Ω(S(n,d)) vs sector dimension d

**Observed (Meta, 2026-05-29; evaluated 2026-05-29).** For four of the stable pairs, the total prime-factor count with multiplicity Ω(S(n,d)) equals d: strange (4,3), charm (20,4), electron (13,6), tau (23,10). The other 11 particles have Ω(S(n,d)) ≠ d.

**Assessment: likely numerological.** Ω(m) is an arithmetic function with no connection to the IDWT eigenmode equations, coupling structure, or sector geometry. A search over all (n,d) with d ∈ D and n ≤ 200 finds many pairs satisfying Ω(C(N,d))=d; the physical particles are not distinguished within that set. The "carries" framing from Kummer's theorem is a computation device — it involves adding integers in prime-number bases, which has no physical meaning. Meta's interpretation that the Ω=d particles are "pure simplex images of seeds" is also incorrect: the electron (n_e = n_ν₁ + n_up = 13) has an additive step. No mechanism connecting Ω to d has been identified. Recorded as a null-context numerical coincidence. Status: ❓

### §18. Adjacent-sector simplex ratio identity

**Theorem (2026-05-29).** For any positive integer n and sector dimension d:

S(n,d) / S(n,d+1) = (d+1) / (n+d)

**Proof.** S(n,d) = C(n+d−1, d), S(n,d+1) = C(n+d, d+1). The ratio:
C(n+d−1,d)/C(n+d,d+1) = [(n+d−1)!/(d!(n−1)!)] × [(d+1)!(n−1)!/(n+d)!] = (d+1)/(n+d). □

A clean ⭐ combinatorial identity relating adjacent-sector mode counts.

**Sector-ladder reading and pattern search (2026-06-04).** Rearranged, §18 is the multiplicative recursion $S(n,d+1)=S(n,d)\cdot(n+d)/(d+1)$ — the across-sector generator of the simplex table at fixed $n$, dual to the additive hockey-stick $S(n,d)=S(n,d-1)+S(n-1,d)$ (across $n$ at fixed $d$) on which the generation tower is built. Together they are the two Pascal recursions that generate the entire $S(n,d)$ array. Both were verified on all 15 physical $(n,d)$ pairs (14/14 for $d\ge 2$). A search for whether §18 constrains the physical mode set returned null: as an identity valid for every $(n,d)$ it cannot distinguish co-fixed-points from any other pair, and the $d=3$ selection test confirms no separation (the step $(n+d)/(d+1)$ runs $1,\,5/4,\,3/2,\,7/4,\,2$ for $n=1..5$, selected and unselected interleaved). Two isolated coincidences — the down quark has $n+d=4=n_s$, the tau's step is $(n+d)/(d+1)=3=n_u$ — form no pattern. Net positive content: the multiplicative-dual reading above; the null half is recorded in §15.

### §19. Sector set D as a function of n_s

**Conjecture / Pattern (2026-05-29).** The active sector set satisfies:

D = {2} ∪ {n_s−1, n_s, n_s+1, n_s+2} ∪ {2(n_s+1)}

For n_s=4: D = {2} ∪ {3,4,5,6} ∪ {10} = {2,3,4,5,6,10}. ✓

The three pieces have individual derivations:
- **{2}**: the EM sector CP¹, U(1)_EM; fixed as the reference sector (derived from T15 and the photon as the d=2 n=0 mode).
- **{n_s−1, n_s, n_s+1, n_s+2}** = {3,4,5,6}: the consecutive matter quartet — derived below.
- **{2(n_s+1)}** = {10}: the Gegenbauer-critical terminal sector, b_{k₀}=1/2 exactly at d=2(n_s+1) (T5). Derived.

**Derivation of the consecutive matter quartet (🔵, 2026-06-01).**

The complex Hopf chain $S^1 \to S^{2k+1} \to \mathbb{CP}^k$ produces Hopf pairs at each level $k$:
- $k=1$: total space $S^3$ (d=3), base $\mathbb{CP}^1$ (d=2, the gauge sector)
- $k=2$: total space $S^5$ (d=5), base $\mathbb{CP}^2$ (d=4)
- $k=3$: total space $S^7$ (d=7, excluded), base $\mathbb{CP}^3$ (d=6, terminal)

The gauge sector d=2 (CP¹ of the k=1 Hopf base) separates from the matter sectors. The matter quartet consists of all total spaces and non-terminal bases after d=2: $\{3, 4, 5, 6\}$.

Rule A terminates the chain when the base sector CP^{n_s-1} appears (real dimension $d_{\rm term} = 2(n_s-1)$), because $\chi(\mathbb{CP}^{n_s-1}) = n_s$ forces $g_{d_{\rm term}} = 1/n_s = $ composite ratio. For $n_s=4$: d_term $= 2\times3 = 6$ (CP³, $\chi=4=n_s$). ✓

The matter quartet runs from d=3 (first total space, always fixed by the Hopf chain) to d=$2(n_s-1)$ (terminal base). Its length is:
$$|{\rm quartet}| = 2(n_s-1) - 3 + 1 = 2n_s - 4.$$

The **self-consistency requirement** is that the matter quartet has exactly $n_s$ members — the composite n_s=4 determines the number of matter sectors:
$$2n_s - 4 = n_s \quad\Longrightarrow\quad n_s = 4. \qquad \text{⭐}$$

This is an independent derivation of $n_s=4$: the unique seed value for which the Hopf chain produces exactly $n_s$ consecutive matter sectors before Rule A termination. At $n_s=4$ the quartet is $\{3,4,5,6\} = \{n_s-1, n_s, n_s+1, n_s+2\}$, centered at $n_s + 1/2$ with $n_s-1=3$ (observable space) as the first element.

The $n_s=4$ Hopf chain gives exactly 2 complete Hopf pairs for matter: $(d=3, d=4)$ = quark sectors and $(d=5, d=6)$ = lepton sectors. This 2+2 pairing is why there are two quark multiplets (down-type, up-type) and two lepton multiplets (neutrino, charged) — a structural consequence of $n_s=4$ rather than an independent input.

**Status: 🔵** (quartet length = n_s derivation from Hopf chain + Rule A; the self-consistency requirement is motivated but not yet a theorem — it needs a derivation of WHY the composite n_s must equal the matter sector count). Verified for $n_s = 3,4,5,6$: only $n_s=4$ gives quartet length = $n_s$ while also placing observable space (d=3) as the first matter sector.

**Self-consistency of n_s=4.** The sector formula reveals two conditions that simultaneously select n_s=4:
1. Matter quartet width equals composite value: |{n_s−1,...,n_s+2}| = 4 = n_s (true only at n_s=4).
2. Matter quartet starts at spacetime: n_s−1 = 3 iff n_s = 4.

No other value of n_s satisfies both simultaneously. Both conditions are not yet derived from IDWT dynamics. (The primary derivation of n_s=4 is T4, Part 9.)

**Addendum — seed re-rooting to {1, 3}: verified (2026-06-11, Fedge proposal).** The subtraction step $n_u = n_s - 1$ has no independent justification (Part 2 §6 records it as lattice-closure consistency presented as derivation "for brevity"). Tested: take the seeds to be $\{1, 3\}$ and derive $4 = 1 + 3$, eliminating the subtraction. Result — everything regenerates, and the seed pair is better grounded than $\{1, 4\}$: **(i)** the STEP 1 compact binomial form reproduces all 14 single-mode indices from $(a,b) = (3, 4)$ with $b := 1 + a$; **(ii)** $a = 3$ carries three convergent anchors — $\chi(\mathbb{CP}^2) = N_c = 3$ (T15, geometric), the unique single-kernel-application image of the ground seed ($\Delta N = +2$: $N{=}0 \to N{=}2 \to n{=}3$, kernel-dynamical), and the T4 double-degeneracy partner; **(iii)** $4 = 1+3$ is the offset-additive composite (the MC-4.4 kernel two-density reading, 🔶), and the offset channel flips level parity ($N_{\rm comp} = N_1 + N_2 + 1$: even + even → odd), which is exactly how the odd-$l$ tree (the strange index) is sourced despite $l$-parity blocking single-mode kernel steps — the {1,4} seed pair's "mutual stabilisation" awkwardness (two seeds in disconnected parity trees) dissolves: $\{1,3\}$ is parity-pure, kernel-connected, and the odd tree is generated, not seeded; **(iv)** T4 ($4/7$ double degeneracy, unique hit at $n=4$ over $n=2..50$), the Gegenbauer crossing $b_n(3)=b_n(4)$ (unique at $n=4$), the matter-quartet condition $2n-4=n$, and the muon fixed point $S(4,4)=35$ all hold as uniqueness certificates of the derived $4$ rather than definitions; **(v)** all six couplings remain functions of $N_c = a$ alone (T15 Step 5; $g_{33}g_{44} = 96$ verified). What re-rooting does NOT fix: the three +1 offsets, the anchor $T = C(p{+}a{+}1, 2)$, and the firing-set selection (T0.5 core) — unchanged. Note on stability: seed status is generative (tower root), not dynamical — it does not by itself confer stability; the ground seed $(1,3)$ is protected by having no downward channel (STEP 64), not by seedhood. Re-rooting reshapes the protection question: $u$'s required absence $(1,4)$ is a sector *ground state*, qualitatively unlike the mid-tower absences $(11,6), (8,5), (13,5), (20,5)$ — whether the $(1,d)$ modes are condensate background (sourcing $\lambda_d$, which is ground-state-sourced) rather than available final states is an open ❓ worth pursuing.

**Candidate: n_s as the d=6 CP³ well ground-state degeneracy (❓).** A further angle on n_s=4. The geometry labels (CP^n, S^n) describe the local symmetry of the potential minimum near r=0, not global topology (Part 1 Foundation, on the well-shape reading), so the d=6 sector has a CP³-shaped well sitting in flat ℝ⁶. For a CP^n well the ground-state degeneracy (number of fixed points) is χ(CP^n)=n+1; for CP³, χ=4, so n_s=4 records the d=6 well's ground-state degeneracy. Open: the causal link from the d=6 well degeneracy to the d=3 seed — the tower connects them through n_μ=S(n_s,4), but the d=6→d=3 direction needs justification. State as candidate only, not a closed proof. The S(2,3)=4 route is circular (writing S(2,3) presupposes the d=3 sector and 2=n_d+1) — do not use it.

**Addendum — generic-a consistency census of the re-rooted tower: the selective web pins a = 3 twenty-fold (2026-06-12, Part 1).** Follow-up to the {1, 3} re-rooting above. The full tower was regenerated from the seed pair {1, a} with composite b := 1 + a, for a = 1..12, and every documented internal cross-check of the tower was classified as either an *identity in a* (tower grammar, blind to the seed) or a *selective relation* (holds only at specific a — these constrain the seed). Results:

- **Identity class (5 relations, hold for all a):** the Pascal/muon relation $s = q + r$; $n_H = n_u + n_{\rm charm} + n_{\rm top}$ (given the compact forms); the ν-spacing $n_{\nu_3} - n_{\nu_2} = n_{\nu_1} - a$; $n_W = T - q$; $g_{33}g_{44} = b^3 a/2$.
- **Selective class (20 relations): all 20 hold at a = 3 and only there in the scanned range,** with a single stray partial hit ($n_W = n_{\rm top} + 4$ also holds at a = 2, where it is not accompanied by any of the other 19). The selective relations include the τ double-derivation ($n_\tau = n_{\rm charm} + n_u \Leftrightarrow n_{\rm charm} = 2n_{\nu_1} \Leftrightarrow a = 3$), the Z and H Vandermonde forms ($q - p = 5$ and $q - p = a + 2$, each a=3-only), the top Euler product, the §10 coincidences (n_top = n_μ+n_ν₂+n_ν₃, n_H = n_top+n_τ, n_e+n_τ = (b+2)², n_ν₁+n_ν₃ = 2^{b+1}, …), the k₀ pair b² = n_e+a and b² = n_charm−b, the T4 unique hit at n = b, the Gegenbauer crossing at n = b, and the matter-quartet condition 2b−4 = b.
- **Structural gain of the re-rooting:** under b = a + 1 the muon double-derivation $S(b,4) = S(b,3) + S(a,4)$ *is* the hockey-stick/Pascal identity — it moves from the selective class (where it sat under the old {1, 4} root as "the coincidence that forced n_s = 4") into the grammar. The re-rooting converts one certificate into an identity and leaves the remaining twenty as genuine over-determination of the seed.

Honest limits: the 20 selective relations are not all independent (e.g. S1⇔S2; the H-additive form follows from the top form; the §25 single-input addendum already audited the k₀ pair to two independent coincidences), so "twenty-fold" counts documented relations, not independent constraints; the scan range is a ≤ 12 (several relations are individually proved unique for all n_s < 500 in earlier entries); and the census constrains the SEED only — it says nothing about the per-(n,d) firing-set selection (T0.5), which is untouched (see the run-#8 conjunction null, §15). Status: verified arithmetic within the scanned range; the census statement itself is a structural observation about over-determination of a = 3, complementing the kernel-dynamical and geometric anchors of the re-rooting addendum above.

### §20. Sector mode functions: explicit harmonic forms, and the saturating-potential binding deficit

**Context (2026-05-29).** Task #1 of the foundational program: write the sector mode functions χ_{n,d} explicitly as eigenfunctions of H_d, in a form that permits normalization, d=3 projection amplitudes, and kernel matrix elements. Two operators appear in the documents and they are **not** the same:

- **Harmonic** H_d^harm = −Δ_d + λ_d r² — the monomial / IDOS operator the mass formula rests on.
- **Saturating** H_d^sat = −Δ_d + λ_d r²/(1+r²) — the confining ansatz of Part 4 §3.10, introduced to obtain a discrete spectrum with finite localization length L_d and continuum threshold λ_d.

**Positive result — explicit harmonic mode functions (⭐ identity).** The eigenfunctions of H_d^harm are exact:
$$\chi_{n_r,l,m}(r,\Omega) = N_{n_r,l}\; r^{l}\, L_{n_r}^{(l+d/2-1)}(w\,r^2)\, e^{-w\,r^2/2}\, Y_{lm}(\Omega), \qquad w=\sqrt{\lambda_d},$$
with level N = 2n_r + l, energy E = √λ_d (4n_r + 2l + d) = √λ_d(2N + d), level degeneracy C(N+d−1, d−1), and cumulative count (IDOS) through level n−1 equal to S(n,d) = C(n+d−1, d). The full d-dimensional normalization ∫|R|²r^{d−1}dr = 1 gives the closed form
$$N_{n_r,l}^2 = \frac{2\,w^{\,l+d/2}\,n_r!}{\Gamma(n_r+l+d/2)}.$$
This is the explicit form requested by Task #1 for the monomial picture. The S(n,d)-dimensional "mode n" is the space of degree-(n−1) homogeneous polynomials in d+1 sector coordinates (dim Sym^{n−1}(ℝ^{d+1}) = S(n,d)). These functions are ready for use in kernel overlap integrals. (Part E).

**Structural finding — the saturating potential does not host the tower.** With the **correct** d-dimensional radial reduction (u = r^{(d−1)/2}R, l=0 centrifugal coefficient A = (d−1)(d−3)/4), the saturating operator H_d^sat has the following count of l=0 bound states below threshold λ_d (deeply-bound count, box-size independent):

| d | λ_d | A=(d−1)(d−3)/4 | E_0^harm = d√λ_d | deeply-bound l=0 states | overlap with harmonic ground |
|---|------|----------------|------------------|------------------------|------------------------------|
| 2 | 50.72 | −0.25 | 14.24 | 3 | 0.973 |
| 3 | 4.82 | 0 | 6.59 | 1 | 0.778 |
| 4 | 1.73 | 0.75 | 5.26 | 0 (one marginal threshold state) | 0.096 |
| 5 | 0.164 | 2.00 | 2.02 | 0 | — |
| 6 | 0.25 | 3.75 | 3.00 | 0 | — |
| 10 | 0.25 | 15.75 | 5.00 | 0 | — |

Three facts, in increasing severity:

1. **The harmonic ground state is bound (E_0^harm < λ_d) only when λ_d > d² — i.e. only for d=2.** For every matter sector d ∈ {3,4,5,6,10} the harmonic ground-state energy d√λ_d lies *above* the saturating continuum threshold λ_d. The harmonic well λ_d r² and the saturating well λ_d r²/(1+r²) agree only near the origin; the matter-sector ground states do not fit inside the region where they agree.

2. **For d = 5, 6, 10 the saturating operator has zero l=0 bound states — analytically certain, not numerical.** V_eff(r) = λ_d − λ_d/(1+r²) + A/r² ≥ λ_d everywhere whenever A ≥ λ_d, and A = 2, 3.75, 15.75 all exceed λ_d ≈ 0.16–0.25. The three sectors that host the neutrinos (d=5), electron and muon (d=6), and tau (d=10) therefore have **no localized s-wave bound state of the confining ansatz at all**.

3. **The §3.10 self-consistency that fixes λ_d closes only under the harmonic assumption it then contradicts.** §3.10.3 sets ⟨r²⟩_d = d/(2√λ_d) using the *harmonic* ground state, giving λ_d = (g_dd/2)^{2/3}. Substituting the actual saturating ground state (where one exists) gives a very different ⟨r²⟩ (e.g. d=4: 336 vs harmonic 1.52), so g_dd⟨r²⟩/d does not return λ_d. The derivation is internally consistent only in the harmonic limit, which the matter sectors violate.

**Reading.** The IDWT mode functions are the harmonic (monomial) functions — that picture is explicit, normalizable, and reproduces S(n,d) exactly. The saturating potential V_d = λ_d r²/(1+r²) cannot be the operator whose bound states are those modes: it supports at most a few deeply-bound states (3, 1, 0, 0, 0, 0 for d = 2,3,4,5,6,10) rather than the required infinite tower, and none in the three deepest matter sectors. This corroborates and sharpens the existing flag MC-2 (potential form is an ansatz) and the §3.13 proof correction. The resolution is in the section below.

**Resolution (2026-05-29) — flat harmonic self-binding; remove the saturation, not the flat sectors (✅).** The ontology constraint is binding: the sectors are *macroscopic, flat, extended* spatial dimensions (a d=2 photon propagates in our 3-space; the electron has a physical d=6 orbit). They are **not** tiny compact/curled dimensions, so the deficit must not be cured by compactifying the sector. The actual culprit is narrower: the deficit is caused **entirely by the saturating denominator (1+r²)**, which Part 4 §3.10.2 never derives. The kernel self-consistency derives only the near-origin r² term; the saturation is the unjustified MC-2 ansatz.

The **pure harmonic self-binding** V_d = λ_d r² in flat, extended ℝ^d cures the deficit while keeping the sectors flat:

- **Confining, infinitely many bound states, every sector.** V → ∞, so the spectrum is purely discrete (σ_ess = ∅, no continuum) and the full simplex tower is bound in all of d = 2,3,4,5,6,10 — the d=5,6,10 deficit does not occur (verified). The particle is a Gaussian-localized standing wave *within* the extended flat sector, exactly as a bound electron is localized inside extended 3-space.
- **λ_d derivation becomes exact.** §3.10.3 set ⟨r²⟩_d = d/(2√λ_d) using the harmonic ground state; with the pure harmonic well this is the *actual* ground state (verified exact for d=3,4,5,6,10), so λ_d = (g_dd/2)^{2/3} closes without circularity.
- **IDOS = S(n,d) exactly.** d-dim isotropic-HO level degeneracy C(N+d−1,d−1), cumulative S(n,d). Spectrum-generating symmetry SU(d) ⊂ SO(d+1).

**T-S1 is the dynamical-symmetry repackaging, not a compact dimension.** On S^d the Dirac operator has eigenvalues ±(k+d/2) with multiplicity 2^{⌊d/2⌋}C(k+d−1,d−1); the cumulative positive count is 2^{⌊d/2⌋}S(n,d), i.e. **per spinor component exactly S(n,d), for every d ∈ D** (verified n=1…39). This S^d is the **SO(d+1) dynamical-symmetry / spectrum-generating sphere** of the flat oscillator (a representation-theory statement), **not** a physical curled sphere. Each particle (n,d) sits at shell (n−1)+d/2. T-S1 (Part 2/Part 8, currently only d=3,5) extends to all six sectors in this reading.

**Mass law, not selector (run #6b, 2026-06-05).** Because the cumulative count is $2^{\lfloor d/2\rfloor}S(n,d)$ at *every* shell n, T-S1 assigns a mass to each candidate (n,d) — it **grounds the mass but does not select which n are physical**. Tested directly: no sector Dirac/Laplace spectral condition (on $S^d$ or $\mathbb{CP}^{d/2}$, five conditions across CP²/CP³/CP⁵/S⁵) picks out the observed per-sector n's without over-generating (§15, run #6b). The sector geometry *seeds* the per-sector generators through its Euler characteristic (§15, run #6), but selection is a separate dynamical question — co-fixed-point stability (MC-4) — not a spectral mark. Future work should not re-chase a per-sector spectral selector; the template that grounds the mass is structurally the one thing that cannot select the index.

**Even sectors.** Under flat harmonic binding the mass count is the SU(d) oscillator IDOS for *all* d, so d=4,6,10 need **no** separate CP^{d/2} Dirac computation. The complex structure ℝ^d ≅ ℂ^{d/2} furnishes CP^{d/2} as the **Kähler/chirality** structure (γ₅, χ(CP^{d/2}) = N_c at d=4, = n_s at d=6) layered on the same flat oscillator — consistent with the existing χ usage. This dissolves the earlier "carrier manifold" residue.

**Mode functions** are the flat harmonic eigenfunctions (Laguerre × Gaussian, §20 Part E, with closed-form norms) — not a proxy after all; they are the genuine self-binding modes. The spinor-harmonic / S^d picture is their SO(d+1)-covariant relabeling.

**Decision (2026-05-29) — L_d = λ_d^{−1/4}, the harmonic oscillator length.** Under the current construction L_d appears in two places: (U1) gravity V_7 = L_4 L_5 L_6 L_10⁴ → G_N = G_∞/V_7 (superseded 2026-06-20 — see note below); (U2) the KK/curvature gap (d+1)/L_d² and R/4 = m(m+1)/(4L_d²). (It formerly also entered a dimensional-visibility amplitude and the Part 7 §2.9 spurion form; both were removed with the visibility apparatus.) With harmonic confinement the ground state is the Gaussian exp(−√λ_d r²/2), whose localization length is the **oscillator length L_d = λ_d^{−1/4}** — not the threshold length λ_d^{−1/2} (that is an exponential-tail length the harmonic well has no continuum to produce). The reason this is the correct choice:

- It is the genuine length of the harmonic ground state we adopted; λ_d^{−1/2} belongs to the rejected saturating well.

Recomputed values (L_d = λ_d^{−1/4}): L_2 = 0.375, L_3 = 0.675, L_4 = 0.872, L_5 = 1.571, L_6 = 1.414, L_10 = 1.414. Downstream:
- **V_7 = 7.74** (was 113). [SUPERSEDED 2026-06-20: V_7 as a gravity factor is removed entirely. A 3D observer is uniform in a sector-d source's k=d−3 hidden coordinates and integrates its field over them; ∫d^kρ/(r²+ρ²)^{(d−2)/2}=C_k/r with C_k/[(d−2)S_{d−1}]=1/(4π) identically gives G_N = G_∞/(4π), sector-independent, no V_7 (idwt.py STEP 24; Part 4 §3.12.2). The earlier note that "V_7 is not why gravity is weak, only a geometric factor connecting G_∞ to what a 3D observer measures" anticipated this — that factor is the universal 4π, the 3D Green's-function constant.]
- **KK gap (d+1)/L_d² = (d+1)√λ_d** (21, 9, 6.6, 2.4, 3.5, 5.5 in sector units) — positive and O(few), so excited modes remain gapped; no KK tower. Fine.

L_d = λ_d^{−1/4} are the sector lengths used throughout the main documents (they feed the spectral-action a₂/a₄ and the KK gap, U2). The V_7 gravity-dilution use (U1) is superseded: G_N = G_∞/(4π), no V_7.

### §20a. T2 kernel overlap of the mode functions, and the nature of the CKM formula (2026-06-04)

First use of the explicit §20 mode functions in a kernel matrix element. The T2 density-density kernel is K = g (ξ·ξ′)² |Ψ|²|Ψ′|². Its overlap between two harmonic modes factorizes under isotropy:
$$O_{ij} = \int\!\!\int (\xi\cdot\xi')^2\,|\chi_i(\xi)|^2|\chi_j(\xi')|^2\,d\xi\,d\xi' = \frac{\langle r^2\rangle_i\,\langle r^2\rangle_j}{d}, \qquad \langle r^2\rangle_{\text{(shell }N)} = \frac{2N+d}{2\sqrt{\lambda_d}}.$$
(The ⟨r²⟩ formula is verified against direct numerical integration of the Laguerre×Gaussian modes to machine precision — confirming the §20 functions are correct and usable. ⭐ for the overlap identity.)

**Consequence — the CKM formula is state-counting, not a kernel overlap (🔶).** O_ij scales as the mode index n¹ (it is a wavefunction overlap, set by ⟨r²⟩). The combinatorial CKM formula |V_ij|² = S(n_lighter,d)/S(n_heavier,d) scales as n^d (n⁴ in d=4): for the up-type quarks the kernel ratio and the simplex ratio differ by ×112 (u–c), ×40 (c–t), ×4440 (u–t). Therefore |V_ij|² is **not** the kernel matrix element ⟨χ|K|χ⟩ — it is a mode-count (IDOS / density-of-states) ratio, a phase-space statement (rate ∝ density of final states). This closes the Part 6 item "CKM not derived from kernel" in the negative: the T2 overlap gives n¹, the formula needs n^d. The formula stays empirically good (Part 3 §0.8); its mechanism is counting, not the dynamical overlap. The overlap O_ij itself (∝ ⟨r²⟩_i⟨r²⟩_j) is the genuine kernel object and is what enters dynamical quantities (e.g. the a₄-gauge integrals, Part 4 §3.12.4).

---

### §50. ℓ=2 dressed d=4 spectrum — CLOSED NULL (2026-06-18)

**Source.** Prompted by DeepSeek (see claude-todo.md). Computed 2026-06-18 (`claude/scratchpad/explore_top_l2.py`).

**Conjecture.** The ℓ=2 kernel self-coupling in d=4 might select n=72 as a criticality threshold or fixed point of the dressed spectrum — explaining the top as a "self-induced resonance" rather than a seed input.

**Result: NULL. Three independent reasons.**

**(i) DeepSeek's ||Q||² formula is wrong.** The correct quadrupole norm for the d=4 isotropic harmonic oscillator at level N = n−1 is derived from ⟨r⁴⟩_N = (N+2)(N+3)/λ₄ and ||Q||² = ⟨r⁴⟩·(d−1)/d:
$$\|Q^{(n)}\|^2 = \frac{3(N+2)(N+3)}{4\lambda_4} = \frac{3\,n(n+1)}{4\lambda_4}$$
at N=n−1. This gives ||Q(72)||² ≈ 2347, not 182.5 as DeepSeek claimed. The discrepancy factor is ~12.9 and grows approximately as n/d for large n. DeepSeek's formula N²/(16λ₄) inserts k₀=16 by hand with no derivation.

**(ii) The ℓ=2 self-energy is zero for isotropic oscillator states.** The IDWT kernel overlap for isotropic modes is established in §20a:
$$\int\!\!\int (\xi\cdot\xi')^2\,|\chi_i|^2|\chi_j|^2\,d\xi\,d\xi' = \frac{\langle r^2\rangle_i\langle r^2\rangle_j}{d}$$
This contains only the monopole (ℓ=0) piece. The quadrupole piece vanishes because ⟨ξ_i ξ_j⟩ = δ_ij⟨r²⟩/d for spherically symmetric states, making the traceless quadrupole ⟨Q_ij⟩ = 0. The ℓ=2 "back-reaction" does not exist at this order for the actual d=4 oscillator modes.

**(iii) The monopole self-energy ratio decreases with n.** The surviving ℓ=0 piece gives ΔE_n/E_n^{bare} = g₄₄(n+1)²/[4λ₄·S(n,4)]:
- n=3 (up): 70.1% — largest, not smallest
- n=20 (charm): 3.3%
- n=72 (top): **0.29%**

n=72 is the *least* self-energized d=4 mode. The ratio decreases monotonically because S(n,4) ~ n⁴ while the numerator grows as n². There is no threshold, fixed point, or special behavior at n=72.

**(iv) No Gegenbauer criticality at n=72 in d=4.** b_n(4) = ½ has the unique solution n=1. b₇₂(4) ≈ 0.5033 — slowly approaching ½ from above as n→∞, nothing special.

**What IS structurally special about 72 (positive finding).** The Vandermonde g-rule gives g(5,72)=76=n_W and g(10,72)=81=n_Z. The top index is the unique seed for the boson chain. The question "why n=72?" is more naturally posed as: what constraint on the boson sector forces the seed to equal N_c·n_s·N_f? This is a different question from the d=4 internal dynamics, and it points toward the sector-geometry side (Euler characteristic product T15b) rather than the coupling side.

**Null result logged:** → Appendix D §15.

---

### §51. Three generations from the MC-2 deposit channels, and the α-ordering driver (2026-06-18, opus; `idwt.py` STEP 96, builds on STEP 74e)

STEP 74(e) proves MC-2 completeness on **flat C^k** (k = d/2) by U(k) representation theory: the marginal deposit channels of a Kähler condensate sector d = 2k are the U(k)-invariant (p,p)-forms on flat C^k — exactly **one per p = 0..k** (Λ^p(C^k) is an irreducible U(k)-rep, so Schur's lemma gives a one-dimensional invariant, spanned by ω^p; ω^{k+1}=0 because Λ^{k+1}(C^k)=0). This is **not** compact CP^k cohomology — that framing was rejected as framework creep (STEP 74e); the sectors are flat ℝ^d, never compact. The two condensate generators are d=4 (k=2 → ω₂, p∈{0,1,2}) and d=6 (k=3 → ω₃, p∈{0,1,2,3}); d=2 (CP¹) has no condensate (m_γ=0), d=3/d=5 are real (no Kähler form), d=10 is terminal — so two generators, fixing the "seed product" (STEP 74c). Two structural facts follow.

**(1) Three generations (⭐, given STEP 74e).** Label a deposit (α,β) = (ω₂ power, ω₃ power); its site j = α+β+2 equals the physical sector d (STEP 89). The per-sector channel count is the convolution of the two U(k)-channel counts — the coefficients of (1+x+x²)(1+x+x²+x³) = 1 + 2x + 3x² + 3x³ + 2x⁴ + x⁵ — so sectors d = 2..7 carry **1, 2, 3, 3, 2, 1** deposits. The peak of **3** at d=4 (up, charm, top) and d=5 (ν₁, ν₂, ν₃) is the three-generation count, capped by k=2,3 (the U(k) nilpotency ω₂³=ω₃⁴=0). d=3 and d=6 carry 2 deposits each; the missing third members are exactly the two known exceptions — the bottom **beat** resonance (k₀=16, not a tower deposit, Part 7) and the **τ** (the (α,β)=(2,3) channel at site 7, forced to its physical sector d=10). The deposit structure separates the regular tower modes from the two exceptions automatically.

**(2) α-ordering driver (🔶 motivated).** Within a sector the mode index n increases with α = #(ω₂) (STEP 89). The clean case is the neutrino sector, where the index *is* the re-evaluated count: ν₁ (α=0) = S(n_u,3) = S(3,3) = 10 and ν₂ (α=1) = S(n_u,4) = S(3,4) = 15 — i.e. d_eval = 3+α, with ω₂ the d=4 evaluation channel. Since S(n,d) is strictly increasing in d for n ≥ 2 (here n_u = 3), each extra ω₂ lands the seed on a strictly larger count, so n rises with α. (For n=1 the ground is degenerate, S(1,d)=1 for all d.) The other sectors order the same way but through tower constructions rather than a single S(n_u, 3+α); ν₃ = 22 = S(3,5)+1 carries a tower additive offset, and the up/down/lepton indices come from the generation DAG. **Open:** a closed n(α,β) across all sectors — the within-bidegree n-assignment, the residual T0.5 piece. The between-degree count (three generations) follows from the U(k) channel structure above.

### §51a. Operand-identity consolidation: the deposit-grid decomposition and the $+n_d$ third-generation displacement (2026-06-20, opus; `idwt.py` STEP 112, builds on §51, STEP 89/99)

This narrows the within-bidegree open item of §51(2). Write the deposit index value as $n(\alpha,\beta)$, $\alpha\in\{0,1,2\}$ ($\omega_2$ power, $d=4$ generator), $\beta\in\{0,1,2,3\}$ ($\omega_3$ power, $d=6$ generator), site $j=\alpha+\beta+2$. Removing the photon $(0,0)$ leaves the eleven matter cells.

**Decomposition (⭐ identity, verified exhaustively in STEP 112).** The eleven index values partition *uniquely* into three classes:

- **Four anchors** — the framework seeds and the Euler product: $n_d=1$ at $(0,1)$, $n_u=3$ at $(0,2)$, $n_s=n_d+n_u=4$ at $(1,0)$, and $n_\text{top}=\chi(\mathbb{CP}^2)\chi(\mathbb{CP}^3)\chi(\mathbb{CP}^5)=72$ at $(2,0)$.
- **Four seed-simplex cells** — the $2\times2$ image $\{S(n,d):n,d\in\{3,4\}\}=\{10,15,20,35\}$: $\nu_1=S(3,3)$ at $(0,3)$, $\nu_2=S(3,4)$ at $(1,2)$, charm $=S(4,3)$ at $(1,1)$, $\mu=S(4,4)$ at $(2,2)$.
- **Three operand edges** — the residual open core: $e=13$ at $(1,3)$, $\nu_3=22$ at $(2,1)$, $\tau=23$ at the $(2,3)$ corner (housed at $d=10$).

No *natural* single closed form $g(\alpha,\beta)$ reproducing all eleven is known. This is **not** an impossibility theorem: the only firm structural fact is that the $\alpha=2$ row $(72,22,35,23)$ is non-monotone in $\beta$, which rules out forms monotone in $\beta$ (necessary, not sufficient — a binomial in compound arguments can be non-monotone). The proved content is the three-class partition.

**Generational reduction (🔶 motivated).** The picture sharpens once the top and bottom are recognised as **free anchors off the hockey-stick tower** (STEP 99) rather than tower outputs. The charged leptons then satisfy a same-generation rule, charged lepton$_i = \nu_i + (\text{up-type})_i$:

$$e=\nu_1+n_u=10+3=13,\qquad \mu=\nu_2+n_c=15+20=35,$$

both documented additive edges. The third would be $\tau=\nu_3+n_\text{top}=22+72=94$, but $n_\text{top}$ is a free anchor (product form, off-tower), so the third charged lepton cannot inherit it; $\tau$ is displaced — minimally, by the ground quantum — to the corner deposit, $\tau=\nu_3+n_d=23$. This is the lepton-sector analogue of the bottom quark, whose third down-type also leaves the tower (the beat $k_0=16$, Part 7 §1.3). Given the rule, $e$ and $\mu$ are fixed; the operand "up-type, same generation" is motivated by the weak-doublet pairing, but with two generations it is a pattern, not a theorem.

**The $+n_d$ third-generation displacement (🔶, the live lead).** Both lepton-tower anomalies reduce to a single ground-quantum shift:

$$\nu_3=S(3,5)+n_d=21+1=22,\qquad \tau=\nu_3+n_d=22+1=23.$$

Equivalently this is the systematic $+1=n_d$ level-vs-index offset: level-addition of disjoint excitations ($N_c=N_a+N_b$, with $N=n-1$) forces $n_c=n_a+n_b-1$, whereas the tower's additive edges sit one higher at $n_c=n_a+n_b$. Why the $+n_d$ shift fires — index-addition over level-addition — is the unproved step; it ties to the time-dependent condensation dynamics (STEP 85).

**Caveat on the prior null record (§15).** The ~16-line selection-null battery mostly targeted the over-broad "one rule cuts the 15-set" with top and bottom *as tower outputs*; it does not close this narrowed lepton-operand question and must not be read as doing so. The open core here is the $+n_d$ third-generation displacement together with the up-type generational operand, not a generic operand scan.

