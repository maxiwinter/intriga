# A Metrological Framework for Measuring the Scale- and Resolution-Dependent Descriptive Compressibility of Empirical Regularities

**Draft v0.4 — 2026-08-26 — not for circulation**

> **On the title.** Earlier drafts opened with "A *Preregistered* Metrological Framework". The word has been removed until a public deposit exists. Protocol v1.1 has **not** been frozen and **no public preregistration exists**; both are pending acts of the investigator (§5.8). The body of the paper describes the framework as *preregistration-ready*, *designed for preregistration* and *to be preregistered* — never as publicly preregistered, frozen or completed — and no hash, registry identifier or deposit date is claimed anywhere. The word may return to the title once the deposit exists.

Maximiliano Winter¹

¹ *Affiliation: [to be completed]*

> **Title note.** The title follows the one recommended by the originality audit (see `notas-auditoria-impacto-originalidad.md`), minus the word "Preregistered" (see the note above). The working title of the milestone was "Measuring the Descriptive Compressibility of Scientific Regularities: A Pre-registered Framework"; it is retained as a short running title. The final choice is the author's.

> **Status of citations.** Every reference marked `[VERIFY]` has not yet been checked against its primary source. See `PENDIENTES.md`. No claim in this draft that rests on such a reference should be considered established.

---

## Abstract

Whether empirical data are algorithmically compressible has been argued rather than measured. McAllister (2003) held that empirical data sets are algorithmically random; Twardy, Gardner and Dowe (2005) replied that they are compressible; McAllister (2005) answered that compression under Minimum Message Length is not exact algorithmic compressibility, so the two sides were not, in the end, measuring the same thing. We do not decide this question by argument. We measure, operationally, how much descriptive cost can be transferred from data to reusable structure, how that transfer scales with the amount of data *n*, the required resolution *ε*, and the descriptive level, and how much of it generalises out of sample. We present a protocol (v1.1, consolidated and prepared for freezing but **not yet frozen and not publicly preregistered**) written so that every accounting decision is fixed before any empirical data set is examined, built on two-part Minimum Description Length accounting with explicit distortion, quantisation, reference-code and null-model declarations; three separately reported ratios — a raw generic-compressor ratio *r*_generic, an oracle ratio *ρ*_oracle available only for synthetic controls, and the effective MDL ratio *ρ*_MDL, bounded above by 1 by construction once the baseline charges the null model's own description; a normalised resolution slope *η*_ε defined only for continuous variables; and a pair of out-of-sample ratios — *g*_pred, purely predictive, and *g*_total, which additionally asks whether a model earns its own description on the test block, each against its matching baseline. A synthetic pilot (Lorenz trajectories, elementary cellular automata Rules 110 and 30, a PCG64 pseudo-random stream, operating-system entropy, and surrogate data) validates the instrument: it separates four strata of compressibility, recovers exact generating rules out of sample (*g*_pred = 0) while refusing spurious ones on noise (*g*_pred = 1), collapses surrogates, and recovers the Lyapunov predictability scale of the Lorenz system to within roughly 12–16 %, a discrepancy we report without correction and without an assigned cause. To the best of our knowledge, previous work has studied algorithmic compressibility, MDL/MML inference, algorithmic rate-distortion and practical complexity estimators separately, but has not combined them into a preregistered cross-domain framework for measuring descriptive scaling across data set size, resolution and descriptive level, with out-of-sample and surrogate controls. The pilot validates the metrology; it says nothing about nature. We state the preregistered analysis and the qualitative predictions for the first empirical measurement (experimental atomic spectra) and the outcomes that would falsify the hypotheses.

**Keywords.** Minimum description length; Kolmogorov complexity; algorithmic rate-distortion; preregistration; compressibility of laws; out-of-sample generalisation; surrogate data; Lyapunov exponents.

---

## 1. Introduction

The known universe is, at present, described by two equations and roughly thirty-two measured numbers. That fact is old and its interpretation is contested, but a more modest observation precedes every interpretation: an enormous quantity of physical regularities admits relatively short descriptions with predictive power, and some of those descriptions anticipated phenomena that played no part in their construction. The question this programme asks is not whether the universe "is compressible" — a question that presupposes a canonical representation of its complete state and a computable measure of its complexity, neither of which we possess — but a narrower, measurable one:

> *Why does the descriptive cost of physical regularities grow so slowly relative to the quantity, diversity and precision of the world they explain?*

Posed this way, the question has the form of a scaling relation. One can ask how the length of the best generalising description of a domain grows as the number of observations, their diversity and the resolution demanded of them increase, without presupposing a power law or a universal exponent. Scaling relations are measured, not argued.

**Position of this paper.** We do not decide by argument whether scientific data are algorithmically compressible. We measure operationally how much descriptive cost can be transferred from the data to reusable structures, how that transfer scales with *n*, *ε* and descriptive level, and how much of it generalises out of sample. The contribution is metrological rather than conceptual. The idea that laws compress observations has a long lineage — Solomonoff's universal induction, the best-system account of laws, algorithmic theories of lawhood, and the Wigner tradition of asking why mathematics fits the world so well. What is missing, to our knowledge, is an *instrument*: a preregistered, cross-domain measurement of how much structural description the world demands per bit of observation, with the accounting decisions frozen before any empirical result is examined, with controls that can fail, and with a declared list of outcomes that would count against the hypothesis.

**Where this paper sits.** The programme has six rungs: conceptual framework → preregistered protocol → reproducible synthetic pilot → robust multi-domain measurement → independently reproduced stratigraphy → a new, predictive physical regularity. This paper reports the third rung. The pilot is *not* the discovery: it validates the metrology. Any test of scientific originality begins with the first descriptive-scaling surfaces measured on real empirical data, which are the subject of the next milestone (§8).

**Structure.** §2 states the dispute this instrument is designed to address and the distinction the exchange left unresolved. §3 situates the framework in related work and gives an explicit map of which components are original and which are not. §4 gives the formal definitions. §5 summarises the protocol, its success criteria and its falsifiers. §6 reports the synthetic pilot with the numbers actually obtained. §7 lists limitations, including one unresolved quantitative discrepancy. §8 states the preregistered predictions for the first empirical measurement. §9 concludes.

---

## 2. The dispute this instrument addresses

McAllister (2003) `[VERIFY]` argued that empirical data sets, taken as they come from instruments, are algorithmically random: the regularities scientists extract are patterns imposed on, or selected from, data whose full description cannot be shortened. Twardy, Gardner and Dowe (2005) `[VERIFY]` replied that empirical data sets are algorithmically compressible, and supported the reply with Minimum Message Length inference: a two-part message consisting of a model and the data encoded given the model is, for real scientific data, shorter than the data encoded literally. McAllister (2005) `[VERIFY]` answered that MML compression is not exact algorithmic compressibility: a two-part code that is shorter than a literal code shows that a *particular* family of models saves bits under a *particular* coding convention, not that the Kolmogorov complexity of the data is substantially smaller than its length.

Read carefully, the exchange did not end because one side won. It ended because the two sides were measuring different quantities under different conventions and neither had an instrument that made the difference explicit. That debate, in its original terms, was therefore *not* this programme. What the present framework offers is a reformulation in which the question becomes quantitative and scale-dependent:

- The compressibility of a data set is not a single number but a function of the distortion measure *d*, the resolution *ε*, the reference code *U*_ref, the amount of data *n* and the descriptive level at which the data are read (§4).
- The quantity that a two-part code measures — the ratio *ρ*_MDL of best-model-plus-residual to literal length — is reported *separately* from anything that could be read as a claim about exact algorithmic complexity. In synthetic controls, where the generator is known, a third quantity *ρ*_oracle bounds what exists; in empirical domains it is unavailable, and *ρ*_MDL is explicitly an upper bound on what exists, never a verdict on incompressibility (§4.3).
- The residual is accounted for, not discarded. A small *ρ* with an algorithmically random residual is compatible with *both* positions in the original dispute: the regularity compresses most of the description, and the irreducible perturbation lives in the residual. The protocol does not choose between the two positions; it measures the *boundary* between them — how much of each bit of observation is absorbed by reusable structure and how much must be paid literally, as a function of *n*, *ε* and level.

We are careful not to present the 2003–2005 exchange as an experiment that has been "waiting" for this instrument. It is the clearest published statement, on both sides, of what a measurement would need to distinguish, and that is the use we make of it.

---

## 3. Related work and originality map

This section serves two purposes: to acknowledge the lineage of every component of the framework, and to state, component by component, what we do and do not claim as new. References marked `[VERIFY]` await confirmation against primary sources (see `PENDIENTES.md`).

### 3.1 Laws as compression

The view that scientific laws are compressed descriptions of observations is not ours. Solomonoff (1964) `[VERIFY]` gave universal induction its formal basis and, later, its convergence theorem for computable sources; Hutter (2005) `[VERIFY]` developed the framework into a theory of universal agents. The best-system account of laws (Lewis) `[VERIFY]` characterises laws as the axioms of the deductive system that best balances simplicity and strength — an informal compression criterion. Wheeler's algorithmic theory of laws `[VERIFY]` makes the compression reading explicit. We take from this tradition only the "core that resists" (v5.2 §1): short descriptions of large sets of regularities exist and some of them predicted phenomena not used in their construction. We separate, following the conceptual framework, two questions that Solomonoff's theorem leaves distinct: *why do physical regularities appear computable?* and *why do they appear computable by such short programs?* A computable world with an enormous source complexity would be learnable in principle and intractable in practice; the programme is about the second question.

### 3.2 MDL and MML

Two-part coding as a model-selection principle is Rissanen's (1978) `[VERIFY]`, developed by Grünwald (2007) `[VERIFY]`; Minimum Message Length is Wallace and Boulton's (1968) and Wallace's (2005) `[VERIFY]`. Our accounting rule — Δ*C* = Δ(model + residual), compression only if Δ*C* < 0, fewer parameters is not by itself a better theory — is standard MDL. Our precision-aware treatment of continuous parameters (§4.2) follows the MDL literature on identifiable precision and is not new. What we add is only the insistence that the rule be *preregistered* per domain before any test data are inspected, and that the cost of *selecting* a model within a family, and the cost of selecting a coder within a class of coders, be charged explicitly (§4.3, Amendment 5 of the protocol).

### 3.3 Algorithmic rate-distortion

The closest antecedent to our compression function *C*(*D*, *ε*) is the algorithmic rate-distortion theory of individual objects: Vereshchagin and Vitányi (2010) `[VERIFY]` and, especially, de Rooij and Vitányi's experimental construction of rate-distortion graphs of individual data with real compressors, including lossy compression and denoising across several domains `[VERIFY]`. This is the **principal antecedent** of the resolution-dependent cost in our framework, and we treat it as such. The difference is one of purpose and design: de Rooij and Vitányi build the rate-distortion curve of an *object*; we measure the comparative *scaling* of descriptive cost across domain × descriptive level × *n* × *ε*, with the cost of the theory charged, with preregistration, with surrogate controls and with out-of-sample generalisation. Whether our normalised resolution slope *η*_ε (§4.4) already exists under another name in classical or algorithmic rate-distortion theory is an open bibliographic question we have not yet resolved; until it is, we present *η*_ε as a possible, unconfirmed novelty.

### 3.4 Compressors as complexity estimators, and their disagreement

Using real compressors as upper-bound proxies for Kolmogorov complexity is established practice: the normalised compression distance of Cilibrasi and Vitányi (2005) `[VERIFY]` is its best-known form. NCD is useful for similarity between objects; as the framework states (v5.2 §7), it does not ground our ratio *ρ*, whose anchors are MDL, algorithmic statistics and algorithmic rate-distortion. Execution-based estimators — the Coding Theorem Method and Block Decomposition Method of Zenil and colleagues `[VERIFY]` — approach complexity from the algorithmic-probability side. Leyva-Acosta, Acuña Yeomans and Hernández-Quiroz (2026) `[VERIFY]` report weak correlation between compression-based and execution-based estimators. If confirmed, that result supports two design decisions of ours: the requirement of at least two independent reference stacks *U*_ref, and the separation of the raw generic ratio *r*_generic from the effective MDL ratio *ρ*_MDL. The pilot reproduces the underlying phenomenon operationally: Rule 30 and a PCG64 stream are incompressible to generic compressors (*r*_generic ≈ 1.00) and yet have generators a few hundred bits long (§6.2).

### 3.5 Computational mechanics, symbolic regression, language models

Crutchfield's computational mechanics `[VERIFY]` measures the statistical complexity of a process's minimal predictive model (ε-machines); it shares our concern with *reusable* structure but measures a different quantity (the memory required for optimal prediction) under a different accounting. Symbolic regression — Schmidt and Lipson (2009) `[VERIFY]`, AI Feynman (Udrescu and Tegmark, 2020) `[VERIFY]`, and exhaustive symbolic regression with MDL model selection in astrophysics (2026, reference to be located) `[VERIFY]` — *selects the best equation for a data set*; we *measure the scaling of the descriptive transfer* as data grow, and we would use such methods only as members of a preregistered model family. "Language modeling is compression" (Delétang et al., 2023) `[VERIFY]` shows that large predictive models are strong general-purpose compressors; for us this is a candidate element of a model family, subject to full accounting of the model's own description length. Bennett's logical depth (1988) `[VERIFY]` is mentioned in the framework only as a candidate for characterising accumulated historical complexity and plays no role in the present measurement.

### 3.6 Originality map

| Component | Status | Nearest antecedent |
|---|---|---|
| Laws as compressed descriptions | not original | Solomonoff; best-system; Wheeler |
| Two-part MDL/MML accounting of theory vs. residual | not original | Rissanen; Wallace; Grünwald |
| Resolution-dependent cost *C*(*D*, *ε*) | close antecedent | de Rooij–Vitányi; Vereshchagin–Vitányi |
| Real compressors as upper bounds on *K* | not original | Cilibrasi–Vitányi; Li–Vitányi |
| Comparison and disagreement of complexity estimators | not original | Zenil et al.; Leyva-Acosta et al. |
| Surrogate-data controls | not original | Theiler et al. (1992) `[VERIFY]` |
| Out-of-sample evaluation with frozen models | not original | standard prequential/MDL practice |
| Dependence on the reference machine, controlled by multiple stacks | not original | invariance theorem; standard caveat |
| Normalised resolution slope *η*_ε | **possible novelty — unconfirmed** | bibliographic search pending |
| Stratigraphy over domain × level × *n* × *ε* | **possible novelty** | no systematic antecedent found yet |
| The combination in one preregistered, cross-domain protocol with three-column reporting, surrogates and out-of-sample controls | **most defensible contribution** | — |

We therefore claim the following and nothing stronger: *to the best of our knowledge, previous work has studied algorithmic compressibility, MDL/MML inference, algorithmic rate-distortion and practical complexity estimators separately, but has not combined them into a preregistered cross-domain framework for measuring descriptive scaling across data set size, resolution and descriptive level, with out-of-sample and surrogate controls.* This is not a new theory of the compressibility of the universe.

---

## 4. Formal definitions

Notation follows the conceptual framework (v5.2, frozen) and the experimental protocol (v1.0 plus Amendments 1–6 = v1.1, pending freezing). Where the pilot forced a correction, the corrected form is given and the amendment cited.

### 4.1 Three layers: fidelity, accounting, reference code

Physical data have no information length independent of the precision at which they are to be reproduced: *x* = 1.234 ± 0.001 carries more than *x* = 1.2 ± 0.5. The framework therefore separates three decisions that are commonly conflated.

**Layer A — fidelity (rate-distortion).** For each domain, a distortion measure *d*, a tolerance *ε* and a deterministic quantiser *Q*(*d*, *ε*) are fixed before analysis, with *d*[*D*, *Q*(*d*, *ε*)(*D*)] ≤ *ε*. The measure *d* says which differences count as physical loss; it must depend on the meaning of the observable, not on the convenience of the algorithm. If several scientifically defensible metrics exist, all are preregistered.

**Layer B — accounting (MDL).** Once discretised, the theory *T* pays for the residual. If *T* induces a predictive distribution,

  *L*(*D*_ε | *T*) = −log₂ *P*_*T*[*Q*(*d*, *ε*)(*D*)],

where, for a continuous density, *P*_*T*[·] is the probability mass integrated over the quantisation cell, not the point value of the density. Rate-distortion fixes what fidelity is required; MDL decides how many bits it costs. The bridge is explicit: *d* → *Q*(*d*, *ε*) → *P*_*T*[*Q*(*d*, *ε*)(*D*)] → −log₂ *P*.

**Layer C — reference code.** A reference stack *U*_ref = fixed interpreter + common primitives + charged libraries is fixed before analysis. Domain-specific libraries pay their length; shared libraries are amortised only under a rule fixed in advance; no primitive may be added after *D*_test has been seen. To control the additive constant of the invariance theorem, results are reported under at least two reasonable stacks, and a result counts as robust only if the observed ordering of conditions survives both. **Amendment 1 (from the pilot):** the specification of each stack must also declare its *reference arithmetic* — floating-point format, rounding, and the integrator's order of operations where applicable — and the resulting *precision floor*. No statement about resolution slopes is interpretable in the regime where *ε* approaches that floor. For empirical data the floor is that of the measuring instrument and must be declared with the same obligation as the units.

### 4.2 The compression function and the accounting rule

For a model family *M* frozen in advance,

  *C*(*d*, *U*; *D*_*n*, *ε*) = min_{*T* ∈ *M*} [ *L*_*U*(*T*) + *L*_*U*(*Q*(*d*, *ε*)(*D*_*n*) | *T*) ].

The first term is the cost of the model, *L*_*U*(*T*) = *L*_*U*(structure) + *L*_*U*(*θ* | structure), with every domain-specific equation, operator, library or sub-model charged. Continuous parameters are not penalised for "how many decimals are written"; a preregistered MDL rule of identifiable precision is used, and the precision demanded of *θ* must *increase* when needed to sustain predictions at smaller *ε* — otherwise *L*(*T*) would be treated as constant while *ε* → 0, which is an artefact.

The general accounting rule is

  Δ*C* = *C*(new) − *C*(previous);  effective compression **only if Δ*C* < 0**.

A relation among parameters is not automatically a compression. If a theory removes 100 bits of data but requires 500 new bits of machinery, the total description has worsened. Fewer parameters does not mean a simpler theory. What counts is model + residual, under the same reference code and the same fidelity rule.

### 4.3 The descriptive ratio and the three columns

Each domain has a null code *M*₀ that does not exploit the structure being sought — a literal or near-literal code — so that the procedure can legitimately conclude *no useful compression within the evaluated family*. The descriptive ratio is

  *ρ*(*d*, *ε*, *U*; *D*_*n*) = *C*(*d*, *U*; *D*_*n*, *ε*) / *L*₀^full,  with ***L*₀^full = *L*_*U*(*M*₀) + *L*_*U*(*D*_*n*, *ε* | *M*₀)**.

**The baseline must be complete.** The numerator *C* is a minimum over the family *including M*₀, so it is bounded by the *total* cost of the null option, model description included: *C* ≤ *L*_*U*(*M*₀) + *L*_*U*(*D*_ε | *M*₀) = *L*₀^full. Normalising by the complete baseline therefore makes **ρ ≤ 1 an exact consequence of *M*₀ being a member of the family**, not an approximation; *ρ* = 1 when the null description is optimal, possibly tied with another model of equal total cost. Normalising instead by the bare residual *L*_*U*(*D*_ε | *M*₀), as is often done informally, gives only *ρ* ≤ 1 + *L*_*U*(*M*₀)/*L*_*U*(*D*_ε | *M*₀), which exceeds 1: the null option would be charged for its own description in the numerator and not credited for it in the denominator. With the complete baseline, *ρ* ≈ 1 keeps the operational meaning "no useful compression was found". The limit *ε* → 0 of *ρ* is never interpreted in isolation.

**Consequence for the numbers reported in §6, stated rather than smoothed.** The pilot normalised by the literal length *L*₀ = *L*_*U*(*D*_ε | *M*₀), without charging *L*_*U*(*M*₀), which its code never defines. Every *ρ* in §6 is therefore a ratio against the bare-residual baseline, not against *L*₀^full. The two conventions differ by the factor 1/(1 + *L*_*U*(*M*₀)/*L*₀); with literal baselines of 10⁵–10⁶ bits and a null-model description of at most a few hundred bits, the difference lies below the rounding of the tables — but it is a difference, and we do not recompute it here. Fixing *L*_*U*(*M*₀) and re-running the scripts under the traceability rule (§5.8) is a pending action, not a result of this draft (§7.5).

The pilot audit (Amendment 5) showed that three quantities that are easily conflated must be reported in **three separate columns**:

- ***r*_generic** — the raw ratio of the best generic compressor to the literal length. It can *exceed* 1 because of header overhead. It measures what an off-the-shelf coder finds.
- ***ρ*_oracle** — the ratio obtained with the *known* generator and its seed. It is available **only for synthetic controls**. It is an existence bound: it measures "a short description exists", not "our family finds it".
- ***ρ*_MDL** — the effective minimum over the preregistered family, *including M₀*, and including the cost of *identification at both levels*: log₂ *k* bits to select among *k* competing coders of the same meta-class, plus the identifier of the winning model within the family. Under the complete baseline *L*₀^full, *ρ*_MDL ≤ 1 holds by construction. In synthetic controls *ρ*_MDL ≃ *ρ*_oracle (not exact equality, because of the identification costs) whenever the family contains the generator. In empirical domains there is no oracle: only *ρ*_MDL exists, and it is permanently an **upper bound** on what exists. No high *ρ*_MDL may be read as a verdict of incompressibility.

The separation matters because a family of generic compressors run in parallel is *not* two reference stacks; it is a set of competing coders within one meta-class, and selecting the best pays log₂ *k* bits. True stacks *U*_ref⁽¹⁾, *U*_ref⁽²⁾ are two complete, independent coding conventions.

### 4.4 Resolution slope *η*_ε (continuous variables only)

For continuous variables, refining *ε* increases the literal length by roughly log₂(1/*ε*) per degree of freedom. The framework measures whether the best generalising description must absorb those bits too:

  *s*_*C*(*n*, *ε*) = ∂*C* / ∂log₂(1/*ε*),  *s*₀(*n*, *ε*) = ∂*L*₀ / ∂log₂(1/*ε*),  ***η*_ε(*n*) = *s*_*C* / *s*₀,**

estimated by finite differences between preregistered resolutions *ε*₁ > *ε*₂ > … > *ε*_*m*. *η*_ε ≈ 1 means each new bit of precision must be paid almost literally; *η*_ε ≪ 1 means reusable structure absorbs most of the refinement. *ρ* and *η*_ε are interpreted together; no isolated asymptotic trend suffices.

**Scope restriction (protocol Rule 4; Amendment 3).** *η*_ε is defined only for continuous variables. For discrete systems (elementary cellular automata, binary symbols) there is no physical *ε* → 0; their scaling with lattice size, time horizon and representational granularity is studied separately and those variables are *not* identified with *ε*.

### 4.5 Out-of-sample generalisation

A grammar can be built retrospectively to compress what it has already seen. The stronger criterion is that it keeps compressing new information. Before any model is trained or selected, the partition *D* = *D*_train ∪ *D*_test is frozen; model structure, hyperparameters, library, quantiser, metric and representation may not be modified after *D*_test is consulted. Then

  *G*(*T*) = *L*_*U*(*D*_test, *ε* | *T*_train),  Δ*G* = *L*_*U*(*D*_test, *ε* | *M*₀) − *G*(*T*).

**Two ratios, each against its matching baseline.** The residual cost and the model-plus-residual cost answer different questions, and a single symbol *g* has been used for both — including in earlier drafts of this paper. We report them separately, and **each is normalised by the baseline of the same kind**, so that neither charges the model on one side of the ratio and forgives the null model on the other:

  ***g*_pred(*T*) = *L*_*U*(*D*_test, *ε* | *T*_train) / *L*_*U*(*D*_test, *ε* | *M*₀)**
  — *once the trained model is known, how well does it encode unseen data?*

  ***g*_total(*T*) = [ *L*_*U*(*T*_train) + *L*_*U*(*D*_test, *ε* | *T*_train) ] / [ *L*_*U*(*M*₀) + *L*_*U*(*D*_test, *ε* | *M*₀) ]**
  — *does the model earn its own description cost on the test block?*

Readings: *g*_pred ≪ 1, strong predictive compression; *g*_pred = 0, the frozen model reproduces the test block exactly; *g*_pred ≈ 1, no useful predictive generalisation; ***g*_pred > 1, the model predicts worse than the baseline**. Separately, ***g*_total > 1 means that model plus test block together cost more than null model plus test block** — the description was not earned on this block.

**No inequality between them is assumed.** The two ratios have different denominators, so *g*_total > *g*_pred does not follow and is not asserted anywhere in this paper. What does hold, and matters for interpretation, is that a model may show *g*_pred ≪ 1 and *g*_total > 1 at the same time when the test block is too small to amortise *L*_*U*(*T*_train); that is a statement about the block size, not a failure of prediction, and it is why the success criterion (§5.5) treats the two asymmetrically.

**A third quantity, kept visible for traceability.** The pilot's scripts compute neither of the above but

  ***g*_total^bare = [ *L*_*U*(*T*_train) + *L*_*U*(*D*_test, *ε* | *T*_train) ] / *L*_*U*(*D*_test, *ε* | *M*₀)**,

which charges the model in the numerator without crediting *M*₀ in the denominator. Every historical *g* value in the pilot literature — 0.0088, 1.009, 1.0088 — is a *g*_total^bare. It is reported under that name in §6.2 and is **not** silently reinterpreted as *g*_total. Historical cases (the positron; the Higgs mechanism, but not the Higgs mass, which the Standard Model left free) are approximations to this criterion, not literal runs of it.

### 4.6 Descriptive levels

Cross-domain comparisons are made only between approximately equivalent levels: **Level A** — general regularities, reusable across many instances; **Level B** — particular trajectories or realisations generated under those regularities; **Level C** — microstate or fine detail of one realisation. A fundamental law is not compared with a particular microscopic biological history as if they were objects of the same level. The experimental object is the surface 𝒞(domain, level, *n*, *ε*, *U*_ref) and its *ρ*, *η*_ε and *g*.

### 4.7 Sensitive dynamics: re-synchronising coders and the required precision of the initial state

**Amendment 2.** For domains with sensitive dependence on initial conditions, the family *M* must include coders with *state re-synchronisation* — checkpoints that re-specify the state every re-synchronisation horizon *h*(*p*, *ε*), defined below — with each checkpoint charged in *L*(*T*) or in the residual under the preregistered convention. A naive two-part coder (one initial condition plus a literal residual after divergence) produces an artefact: *ρ* of the generative model *grows* with *n* for chaotic systems, falsely suggesting that the descriptive advantage is exhausted (§6.3). Without re-synchronising coders, no conclusion of "exhaustion of compressibility" at Level B is valid.

**The re-synchronisation horizon *h*(*p*, *ε*), and what it is not.** A checkpoint coder needs the number of steps for which a state specified to *p* bits per coordinate reproduces the reference trajectory quantised at resolution *ε*. That quantity is **measured, not derived**: we write it *h*(*p*, *ε*) and always record both arguments. It must not be identified with the Lyapunov horizon ≈ *p*·ln 2/*λ* that theory would predict, for two reasons the pilot makes concrete (§6.4): *h* varies with *ε* as well as with *p* — measured values 3194, 2655, 2655, 2655 and 2458 steps at 4, 6, 8, 10 and 12 bits per coordinate — and over the range where it is flat it is limited by the **arithmetic floor of the reference**, not by the dynamics. A horizon pinned at one value while resolution changes is the signature of a precision floor (Amendment 1), not of a Lyapunov time. Every checkpoint count in this paper is ⌈*n*/*h*(*p*, *ε*)⌉ with *h* stated, each checkpoint pays its cost, and none is presented as a theoretical prediction. The theoretical horizon may be used as a reference or a prediction against which *h* is compared — that comparison is the subject of §7.1 — but it never replaces the measurement. If *h* is *optimised* rather than fixed in advance, the cost of selecting it within the model family must be charged like any other model-selection decision. This definition, together with the requirement to declare the arithmetic or instrumental floor that bounds *h*, is carried into the consolidated protocol (`protocol/protocolo-v1-1-consolidado.md`, §5.4).

**Accounting corollary (corrected form, Amendments 2 and 5; protocol Rule 5).** Under deterministic computable dynamics, *K*(*S*_*t*) ≲ *K*(*S*₀) + *K*(law) + *K*(*t*) + *O*(1): if the initial state and the law are known exactly, no new bits appear. What grows with the horizon is the *precision of S₀ that must be resolved* to keep a trajectory located at fixed observational resolution. Where the Pesin relation applies — under its conditions on the dynamics and the invariant measure, which are not universal — the asymptotic rate is *h*_KS = (1/ln 2) Σ *λ*_*i*⁺ bits per unit time, the sum of the positive Lyapunov exponents, not in general only the largest. Those revealed bits are charged to *K*(*D* | *T*, *S*₀). We formulate every statement about information rates in deterministic dynamics as *required precision of the initial state*; we never describe it as the creation of information by the dynamics. The rule (Level A) is paid once; the particular trajectory (Level B) additionally pays ≈ *λ*/ln 2 bits per unit time, irreducibly, at fixed resolution.

---

## 5. Protocol summary, success criteria and falsifiers

The full protocol is the document to be frozen (v1.0 `.docx` plus the changelog of Amendments 1–5 and Amendment 6 = v1.1). Amendments 1–5 arose from the pilot; Amendment 6 arose from the reproduction of the pilot from the assembled repository, not from any result (§5.8, §7.5). This section summarises the operative content.

### 5.1 Hypotheses

- **H1 — Structural compression.** There exist domains or descriptive levels for which *C* ≪ *L*_*U*(*D*_*n*, *ε*) persistently as *n* and 1/*ε* grow.
- **H2 — Generalisation.** The compression is not only retrospective: models selected on training data keep a descriptive advantage on observations not used in their construction.
- **H3 — Robustness.** Observed differences survive prespecified changes of *U*_ref, resolution, admissible distortion metrics, corpus size and train/test partition.
- **H4 — Structure versus marginal content.** The advantage of a real data set falls substantially when its relevant structure is destroyed by surrogates that preserve marginal properties.
- **H5 — Stratigraphy.** Compressibility need not be uniform across domains or within one domain.

### 5.2 What must be preregistered before any comparison

For each data set: the representation (mathematical structure, units, variable order, normalisation, missing-data treatment, permitted transformations, metadata in and out; every transformation deterministic from the raw data); the **provenance class** (§5.3); the distortion metric *d*; the discrete set of resolutions *ε*₁ > … > *ε*_*m*, expressed relative to *d*, never chosen after seeing which value favours the hypothesis; the quantiser *Q*(*d*, *ε*); the residual code (explicit predictive distribution or equivalent prequential code); the precision rule for continuous parameters; **at least two reference stacks** with interpreter, primitives, number representation, operators, general and domain libraries, cost of adding a library, amortisation rule, and — Amendment 1 — reference arithmetic and precision floor; the null model *M*₀; the model family *M* (which may include differential equations, probabilistic models, grammars, symbolic models, universal compressors, autoregressive models, dynamical systems and predefined learning architectures), with the cost of any hyperparameter search that uses training information charged; the nested corpora *D*₁ ⊂ *D*₂ ⊂ … ⊂ *D*_*n*, increasing diversity and not only redundant samples; and the train/test partition with the moment at which the model is frozen. No power law is assumed; the object is the scaling curve or surface.

### 5.3 Provenance and theoretical contamination (protocol §4.2; Rule 7)

Every corpus is classified as (1) primary instrumental measurement, (2) calibrated data, (3) processed data, or (4) product of theoretical fit, and the physical, statistical and numerical models involved in its production are documented. **A data set whose generation already incorporates the structure a candidate model is trying to discover cannot be used as principal evidence for that model**; it may serve only as methodological test or control. Ephemeris catalogues derived by dynamical fitting, for instance, may demonstrate the method but cannot be evidence that gravitational dynamics was "discovered" by compression.

### 5.4 Surrogates and robustness

For each real data set, where scientifically possible, surrogates are defined *before* analysis: temporal permutation, phase randomisation, spatial permutation, block shuffling, histogram-preserving correlation destruction. The structural hypothesis predicts *C*(*D*) < *C*(*D*_surrogate) once size and resolution are normalised. Every principal result is repeated under more than one *U*_ref, several preregistered resolutions, alternative defensible metrics, several *n*, several partitions, surrogates and alternative declared null models. Numerical equality across codes is not demanded; qualitative stability of the relevant separations is.

### 5.5 Primary success criterion (protocol §16)

Success is not declared because a single metric is small. Evidence of extraordinary structural compressibility requires *jointly*

  **ρ_MDL ≪ 1, η_ε ≪ 1, g_pred ≪ 1**

with ***g*_total reported alongside as a condition of descriptive amortisation, not as a threshold**. The asymmetry is deliberate. *g*_pred measures predictive generalisation and must be small for the claim to hold at all. *g*_total measures whether the model earns its own description on the block it was tested against, and that depends on the size of the block: demanding *g*_total ≪ 1 at every test size would penalise a correct reusable structure merely for being evaluated on a small sample. What is required of *g*_total is therefore a **scaling prediction rather than a threshold**: if the structure is genuinely reusable, then as the test block or *n* grows, *L*_*U*(*T*_train) is amortised over more data and

  ***g*_total → *g*_pred**

from above. A *g*_total that stays flat, or diverges from *g*_pred, as the test block grows indicates a model whose description grows with the data it explains — the signature of fitting rather than compressing, and a result to be reported as such. Beyond these, robustness to the preregistered decisions is required; and, in addition, the advantage must (1) persist as *n* grows; (2) persist as resolution increases within the studied regime; (3) survive on *D*_test; (4) fall significantly on surrogates; (5) survive across reference stacks; (6) not be explicable by theoretical contamination of the pipeline; (7) be compared across domains only at comparable descriptive levels.

### 5.6 Outcomes that falsify or weaken the hypothesis (protocol §17)

- *ρ* converges systematically towards values near 1;
- the advantage disappears out of sample;
- it changes radically when *U*_ref is changed;
- there is no difference between real data and their surrogates;
- the apparent advantage of physics disappears when descriptive levels are equalised;
- the advantage is explained by prior processing of the data set;
- refinement of *ε* forces the model to pay practically all additional bits;
- other domains show curves indistinguishable from fundamental physics.

**A negative result is part of the programme and is published as such.**

### 5.7 Scope of any conclusion (protocol §19)

Even a positive result would not show that the universe has low Kolmogorov complexity. It would show something narrower: that within the studied domains, scales and resolutions, growing quantities of observational information can be replaced by reusable descriptive structures whose cost grows much more slowly than that of the data they explain, and that this advantage generalises out of sample.

### 5.8 Freezing, preregistration and mandatory expert review

**Neither freezing nor public preregistration has taken place at the time of writing; what follows describes a procedure to be carried out, and nothing in this paper reports a completed deposit.** A consolidated text of v1.0 plus Amendments 1–6 now exists as `protocol/protocolo-v1-1-consolidado.md`, carrying the status line *"Prepared for freezing — NOT YET FROZEN OR PREREGISTERED"*; the original v1.0 document and the changelog are unmodified beside it. Protocol v1.1 is to be frozen by exporting the consolidated document, recording its SHA-256 hash and date, tagging the code repository, and depositing the same hash in a public preregistration (OSF). From that moment, nothing found during the first empirical measurement modifies v1.1: it is recorded as a documented deviation or motivates an explicit v1.2. **Amendment 6 (traceability and dual noise control)**, adopted before freezing, requires that every number published in a report of the programme be generated by a versioned script whose output is archived, and splits the negative control into an unseeded source (`os.urandom`; reportable invariants only: test error ≈ 0.5, *g* > 1; the identity of the spurious rule is run-dependent and is not cited) and a seeded pseudo-random source for the reproducible row. The framework and protocol were developed through rounds of cross-criticism among several AI systems under human supervision. That process is robust against errors the systems do *not* share and blind to biases they share by construction (overlapping training corpora, similar formalisation conventions). **Before the first empirical data set with a publishable claim, the protocol must pass at least one human expert reviewer in MDL/algorithmic information theory and one in the chosen physical domain.** This is the framework's own observability boundary applied to its method: internal criticism cannot measure the common blind spot of those who exercise it.

---

## 6. Pilot §10.1: validation of the instrument on synthetic controls

**Declared scope.** The controls validate the instrument; they say nothing about nature. All data sets were generated by the executor, so theoretical contamination is total and deliberate: the generative model *is* the generator. That is exactly what a positive control must be.

### 6.1 Setup (declared before running)

Fixed seeds (42, 7); single run, no post-hoc selection. **Lorenz** system with *σ* = 10, *ρ* = 28, *β* = 8/3, RK4 integrator, d*t* = 0.01, 1000 transient steps discarded, 20 000 recorded steps, quantised at 8 bits per coordinate over the ranges [−25, 25] × [−30, 30] × [0, 55]. **Elementary cellular automata** Rules 110 and 30, 256 cells × 400 steps, periodic boundary, random initial row. **PRNG**: NumPy PCG64, seed 7, 32 768 bytes. **Noise**: 32 768 bytes from the operating-system entropy source (`os.urandom`, unseeded by nature). **Surrogates**: Rule 110 with bits permuted; Lorenz with bytes permuted. Null model *M*₀: literal coding. Generic family: {zlib, bz2, lzma} — three competing coders within one meta-class, *not* two reference stacks; selection of the best pays log₂ 3 ≈ 1.6 bits, included in *ρ*_MDL. Generative two-part models: compressed source code + parameters + initial condition at precision *p* bits per coordinate. **Preregistered prediction:** the largest Lyapunov exponent of Lorenz, *λ* ≈ 0.906, predicts ln 2 / *λ* ≈ 0.765 time units per bit, i.e. ≈ 76.5 integration steps of *ε*-fidelity bought per additional bit of initial condition at d*t* = 0.01.

### 6.2 Main table

| Domain | *L*₀ (bits) | *r*_generic | *ρ*_oracle | *ρ*_MDL |
|---|---|---|---|---|
| Lorenz (20 000 steps, checkpoint coder) | 480 000 | 0.53 | **0.0053** | 0.0053 |
| Rule 110 | 102 400 | 0.50 | **0.0107** | 0.0107 |
| Rule 30 | 102 400 | 1.0009 | **0.0107** | 0.0107 |
| PRNG (PCG64) | 262 144 | 1.0005 | **0.0018** | 0.0018 |
| Noise (`os.urandom`) | 262 144 | 1.0005 | — | **1** (*M*₀ wins) |
| Surrogate Rule 110 (bits permuted) | 102 400 | 0.9945 | — | 0.9945 |
| Surrogate Lorenz (bytes permuted) | 480 000 | 0.9261 | — | 0.9261 |

In these controls *ρ*_MDL ≃ *ρ*_oracle because the family contained the generator — a laboratory privilege no empirical domain will grant. The strict accounting adds the identifier of the winning model and the log₂ 3 of the coder meta-class; the effect disappears at the table's rounding.

**Out-of-sample generalisation** (rule inferred from 40 rows, frozen, tested on 360): Rule 110 → rule recovered exactly, 0.0 % test error. Rule 30 → same. Noise treated as an automaton → a spurious "rule", ≈ 50 % test error. In the metrics of §4.5, with *L*_*U*(*T*_train) = 808 bits and *L*_*U*(*D*_test, *ε* | *M*₀) = 92 160 bits:

| Control | test error | ***g*_pred** | ***g*_total^bare** (historical) | ***g*_total** (symmetric) |
|---|---|---|---|---|
| Rule 110 | 0.0000 | **0.0000** | 0.0088 | requires *L*_*U*(*M*₀) — **not computed** |
| Rule 30 | 0.0000 | **0.0000** | 0.0088 | requires *L*_*U*(*M*₀) — **not computed** |
| Noise, PCG64 seed 2026 | 0.5001 | **1.0000** | 1.0088 | requires *L*_*U*(*M*₀) — **not computed** |
| Noise, `os.urandom` (unseeded) | ≈ 0.50 | ≈ 1 | 1.009 | requires *L*_*U*(*M*₀) — **not computed** |

**Which quantity these numbers are.** The historical pilot values 0.0088, 1.009 and 1.0088 are ***g*_total^bare**, not *g*_total: `piloto_10_1.py` computes `(L(T) + L_test)/tot`, charging the model in the numerator without crediting *M*₀ in the denominator. They are **not reinterpreted** as the symmetric *g*_total of §4.5. The *g*_pred column is printed by `src/g_metricas_oos.py` (`results/g-metricas-oos-salida.txt`), a script added for this draft that recomputes the out-of-sample procedure with the pilot's own seeds and prints *g*_pred and *g*_total^bare side by side; it reproduces the historical *g*_total^bare exactly and modifies no earlier script or output. The symmetric *g*_total is **not computed anywhere**, because it requires *L*_*U*(*M*₀), which the protocol does not yet define; no value has been assumed for it (§7.5 bis). The unseeded `os.urandom` row reports only invariants, per Amendment 6(b).

**Measured Lyapunov slope:** 66 steps per bit of initial condition (float64 reference; prediction ≈ 76.5; same order — see §6.4 and §7.1).

### 6.3 What the instrument showed it can do

1. **It detects strata (H5).** Four levels cleanly separated: known generator (*ρ* ~ 0.002–0.01); structure visible to a generic compressor (*ρ* ~ 0.5); structure invisible to the generic compressor but with a short generator (Rule 30, PRNG: *r*_generic ≈ 1, *ρ*_oracle ≈ 0.002–0.01); true noise (*ρ* ≈ 1 throughout).

2. **The Rule 30 / PRNG gap is the key conceptual result of the pilot.** "Incompressible for gzip" is not "incompressible". The distance between *r*_generic ≈ 1.00 and *ρ*_oracle ≈ 0.002–0.01 is the distance between *what our model family finds* and *what exists*. It is an operational demonstration of the dependence on the model family that the incomputability of *K* makes unavoidable — it illustrates the problem; it is not an experimental demonstration of Chaitin's theorem. The failure of a compressor never certifies incompressibility. In real data there will be no oracle, and this gap is why no high *ρ*_MDL can be read as a verdict of incompressibility.

3. **Surrogates collapse (H4).** Permuting the bits of Rule 110 takes *ρ* from 0.50 / 0.0107 to 0.99: the advantage was measuring structure, not marginals. The Lorenz surrogate retains *ρ* = 0.93 because byte permutation preserves the non-uniform histogram — compression of marginals, exactly what the control must isolate.

4. **Generalisation discriminates (H2).** The exact rule was recovered from 40 rows and sustained over 360 out-of-sample rows with *g*_pred = 0 (and *g*_total^bare = 0.0088); on noise the procedure is not fooled: *g*_pred = 1.0000, *g*_total^bare > 1.

5. **The metric empirically recovered the predictability scale set by the Lyapunov exponent.** 66 steps/bit measured against ≈ 76.5 predicted (*λ*/ln 2 ≈ 1.307 bits per time unit). The ≈ 13 % discrepancy is reported without correction (§7.1).

**The naive-coder artefact and its correction (Amendment 2).** A two-part coder with a single initial condition and a literal residual after divergence gives, for Lorenz, *ρ*_model = 0.057 at *n* = 1000, 0.024 at 2500, 0.48 at 5000, 0.74 at 10 000 and 0.87 at 20 000 — the generative advantage *appears* to be exhausted as the horizon grows. A coder with checkpoints — re-specification of the state every *h*(52, 8 bits) = 2655 measured steps, ⌈*n*/*h*⌉ checkpoints of 156 bits each — removes the artefact (*ρ* = 0.0602, 0.0241, 0.0133, 0.0080, 0.0053 at the same five *n*) and reveals the cost structure, which must be read as a **Level A / Level B decomposition of the Lorenz description**, never as one number. (This decomposition is about *descriptive levels* in the sense of §4.6. It has nothing to do with the Track A / Track B design of the empirical measurement in §8, which is a different distinction entirely and is never applied to Lorenz.)

| | **Level A — the rule** | **Level B — this trajectory** |
|---|---|---|
| What it buys | the reusable regularity | the location of one realisation at fixed resolution |
| Cost | **1288 bits, fixed** (1096 compressed source + 192 parameters) | **156 · ⌈*n*/*h*⌉ bits**: 156, 156, 312, 624, 1248 at *n* = 1000 … 20 000 |
| Scaling in *n* | constant | grows ≈ *λ*/ln 2 ≈ 1.3 bits per unit time |
| At *n* = 20 000 | 1288 of 2536 bits | 1248 of 2536 bits |

Both levels are verifiable in `results/lorenz-checkpoints-salida.txt`; their sum is the *C* from which each *ρ* is formed. Reporting only the combined *ρ* = 0.0053 hides the fact that one level is flat and the other is linear in the horizon: at *n* = 1000 the rule is 89 % of the description, at *n* = 20 000 it is 51 %, and it keeps falling. This is the miniature stratigraphy *law → realisation → microstate* measured inside one system, and it is the reason the protocol forbids comparing domains across descriptive levels (§4.6).

*Traceability note (Amendment 6).* The Level A figure is **1288 bits**, not the "≈ 1400 bits" of the original pilot report, which used the stale source-length constant 1252 corrected in §7.5. The pilot report's own errata section does not yet carry this correction; it is recorded in `docs/ERRATA-piloto-v1-1.md` and listed as a pending action. Under the traceability rule, the subtotals 1288 and 156·⌈*n*/*h*⌉ are at present sums of quantities the script prints rather than quantities the script prints itself; making the script emit the Level A subtotal, the Level B subtotal and the total directly is a pending action, and no final table should derive them by hand.

### 6.4 Verification addendum (Amendments 1 and 3 executed)

**The precision floor (Amendment 1).** In the original run, match lengths — the number of steps for which a truncated initial condition reproduces the quantised reference trajectory — saturated at ≈ 2655 steps even at 52 bits per coordinate, and the horizon stayed pinned at ≈ 2655 for quantisations from 6 to 10 bits: the signature of an arithmetic floor, not of the dynamics. Hypothesis: the reference trajectory itself lives in float64. Pre-declared test: recompute the reference in 160-bit arithmetic (mpmath), same integrator and quantiser, and check whether the saturation point *moves*. Result: match lengths stop saturating — *p* = 40: 2699 steps; *p* = 52: 3052 (versus 2655 with the float64 reference); *p* = 64: 4228; *p* = 76: 5011 — all increasing, no ceiling. **The floor hypothesis is confirmed as the cause of the saturation** by the pre-declared criterion. Lesson for the protocol: the reference stack fixes not only the language but the precision floor against which all fidelity is measured; in real data that floor is the measuring instrument.

**What the verification did *not* resolve.** In extended precision the slope remains well below the prediction: mean of the per-segment slopes over *p* = 40…76, 64.2 steps/bit (segments 29.4, 98.0, 65.2 — range 29–98); least-squares fit, 67.6 steps/bit; against 76.5 predicted. The floor explained the saturation, not the slope discrepancy, which remains **without an assigned cause** (§7.1).

**Resolution sweep (Amendment 3).** Lorenz with the checkpoint coder at 4, 6, 8, 10 and 12 bits per coordinate (*n* = 5000): *ρ*_MDL = 0.0267, 0.0178, 0.0133, 0.0107, 0.0098 (values recomputed with the traced source-code length under Amendment 6; the original run reported 0.0293–0.0106 with a stale constant, see §7.5); by finite differences, unaffected by that constant, ***η*_ε = 0.0000, 0.0000, 0.0000, 0.0052** — the generalising description absorbs almost every new bit of resolution. Continuous uniform noise at 8 and 16 bits: *r*_generic ≈ 1.0007 and 1.0005, *ρ*_MDL = 1 (*M*₀ wins), ***η* = 1** — every bit of resolution is paid literally. The behaviour of *η* is validated at both extremes.

**Central operational result of the controls.** For noise, Δ*C* ≃ Δ*L*₀ as resolution increases; for Lorenz, Δ*C* ≪ Δ*L*₀. The instrument has measured, in the laboratory, the central idea of the programme: more observational precision does not demand proportionally more structural description when a reusable generative regularity exists. This is not a result about nature (self-generated data, family with an oracle); it is the proof that the instrument does what it was built to do.

### 6.5 Reproduction

On 2026-08-26 the two pilot scripts were re-executed from the assembled repository (Python 3.12, NumPy 2.5, mpmath 1.4). Every seeded quantity — the seven-row table, the float64 slope (66.1), the match lengths at *p* = 12…52, the naive-coder scaling, the out-of-sample results for Rules 110 and 30, the extended-precision match lengths, the resolution sweep and *η*_ε values — reproduced exactly. The only difference was the out-of-sample row for the unseeded `os.urandom` control (spurious rule identifier and test error 50.07 % → 50.23 %; *g* = 1.0088 in both runs), as expected for an unseeded source. Details, hashes and three pre-existing bookkeeping inconsistencies found during the reproduction are recorded in `reproduccion-2026-08-26.md`; their closure under Amendment 6, the same day, is described in §7.5.

### 6.6 What the pilot does NOT show

**The two kinds of claim, kept apart.** Everything in §6 is a *metrological* claim: a statement about how the instrument behaves when the truth is known by construction. No statement in §6 is a claim about nature, and none may be cited as one. The empirical track — claims about how much structural description the world demands — begins in §8 and has produced no measurement yet.

Nothing about nature. The data sets are synthetic and self-contaminated by design; the generic compressors are coarse approximations of *K*; the generative family contained the true generator, a luxury no empirical domain will grant. The pilot validates that *ρ*, *g*_pred, *g*_total^bare and the resolution slope behave as the protocol demands *when the truth is known*. The next stage is §11.1 of the protocol: empirical data with a documented processing chain — experimental atomic spectra against the null model and against families that do not contain the answer in advance.

---

## 7. Limitations

We list the limitations in the order of their importance for a reader deciding how much weight the pilot can bear. None of them is softened here; two of them are quantitative discrepancies we could not close.

### 7.1 The unresolved slope discrepancy: ≈ 64 measured versus ≈ 76.5 predicted steps per bit

The preregistered prediction was that each additional bit of initial-condition precision buys ln 2 / (*λ* · d*t*) ≈ 76.5 integration steps of *ε*-fidelity for Lorenz at *λ* ≈ 0.906. The float64 run measured 66 steps/bit; the extended-precision run, 64.2 steps/bit as the mean of per-segment slopes over *p* = 40…76 (segments 29.4, 98.0 and 65.2 steps/bit over the three 12-bit intervals) and 67.6 steps/bit by least squares. The precision-floor correction (§6.4) explained the *saturation* of the match lengths and was confirmed by the pre-declared displacement criterion; it did **not** explain the slope. The discrepancy of roughly 12–16 % **survived the correction and has no assigned cause**. The non-uniformity across segments (29–98) is itself a datum that any future causal hypothesis must account for. Candidate causes, none of them verified: finite-time Lyapunov exponents along the particular trajectory; the divergence threshold implied by the quantiser; quantisation itself; the time step; the RK4 integrator error; the initial orientation of the truncation error relative to the unstable manifold; and the convention by which one bit of precision per coordinate is counted as one bit of initial condition. We have not "corrected" this number and will not do so without a test that isolates one candidate. It is recorded in the project as an open debt: to be investigated or reported, never adjusted.

### 7.2 One meta-class of compressors, not two reference stacks

The generic family {zlib, bz2, lzma} consists of three competing coders within a single meta-class. It does not satisfy the protocol's requirement of at least two complete and independent coding conventions *U*_ref⁽¹⁾, *U*_ref⁽²⁾. True reference stacks have not yet been implemented. Every generic ratio in §6 is therefore an *r*_generic under one convention, and the robustness criterion H3 with respect to *U*_ref has not been tested.

### 7.3 Self-generated data and an oracle in the family

All pilot data sets are class-4 (product of the very generator being scored) by design. The generative family contained the true generator, so *ρ*_MDL ≃ *ρ*_oracle. Nothing in §6 constrains what will happen when the family must *find* structure it was not handed.

### 7.4 *η*_ε measured on two continuous controls only

The resolution sweep was run on Lorenz and on continuous uniform noise, at one corpus size (*n* = 5000) and one seed. Discrete controls (Rules 30/110, PCG64) have no *ε* sweep by protocol rule; their scaling with size, horizon and granularity has not been measured.

### 7.5 Bookkeeping gaps found during reproduction, and their closure (Amendment 6)

The reproduction of 2026-08-26 found three numbers in the pilot report that no versioned script produced: (i) the headline Lorenz figure *ρ*_oracle = 0.0053 (20 000 steps, checkpoint coder) — the main script reports the naive coder (0.5307) for that row and the verification script runs the checkpoint coder only at *n* = 5000; (ii) the spurious-rule identifier and test error of the unseeded negative control, which differ between the report, the archived output and the reproduction; (iii) the "≈ 64 steps/bit" extended-precision slope, derived by hand from archived match lengths. Amendment 6 — adopted before freezing and arising from the reproduction, not from any result — now requires every published number to be generated by a versioned script with archived output. A new script reproduces (i) exactly: 8 checkpoints of 156 bits, 192 bits of parameters and 1096 bits of compressed source give 2536 bits and *ρ* = 0.0053, confirming the report. In doing so it exposed a fourth gap: the verification script hard-codes 1252 bits for the compressed source where the declared source measures 1096, which shifted the *ρ*_MDL values of the resolution sweep upward by 156 bits each (corrected in §6.4; *η*_ε is a difference and is unaffected). Item (ii) is handled by the dual noise control (§5.8, §6.2); item (iii) is now printed by the script as a mean, a per-segment range and a least-squares fit (§7.1). All corrections are recorded as visible errata in the pilot report, with the old values struck through, never silently. The original verification script and its archived output are left unmodified as the record of the original run.

### 7.5 bis Formal definitions repaired in this draft, with their numerical debts

Three definitional defects present in v0.2 are corrected in §4 of this draft. None of them changes a measured quantity, but two leave a numerical debt that we state rather than absorb.

- ***ρ*_MDL ≤ 1 was asserted, not guaranteed.** With the baseline taken as the bare residual *L*_*U*(*D*_ε | *M*₀), the bound is 1 + *L*_*U*(*M*₀)/*L*₀ > 1. §4.3 now normalises by the complete baseline *L*₀^full, under which the bound is exact. **The numbers in §6 do not yet use *L*₀^full**, and this draft does not claim they do. **Debt:** the pilot's code never defines *L*_*U*(*M*₀), so every *ρ* in §6 is still against the bare-residual baseline. The shift is below the tables' rounding, but it has not been computed, and no value here has been silently adjusted. Fixing *L*_*U*(*M*₀) and re-running is a pending action.
- ***g* was defined as residual-only and reported as model-plus-residual, and the model-plus-residual form was itself asymmetric.** §4.5 now defines *g*_pred and a **symmetric** *g*_total in which the numerator's model cost is matched by *L*_*U*(*M*₀) in the denominator, and states that no inequality between the two ratios is assumed. **Partly closed:** *g*_pred is now printed by `src/g_metricas_oos.py`. **Debt that remains:** the symmetric *g*_total cannot be computed until *L*_*U*(*M*₀) is defined, so §6.2 reports the historical *g*_total^bare under its own name and leaves the *g*_total column explicitly empty. No historical value was reinterpreted.
- **The re-synchronisation horizon was called a Lyapunov horizon.** 2655 steps is a *measured* *h*(*p*, *ε*) that is flat across four resolutions because it is limited by the reference arithmetic — the precision floor that Amendment 1 exists to record — and not by the Lyapunov time. §4.7 introduces *h*(*p*, *ε*) explicitly. No number changes; the earlier label contradicted the pilot's own finding. Whether this definition should enter the consolidated protocol text before freezing is a decision for the investigator, not an edit made here.

A fourth item is a value, not a definition: the Level A cost of the Lorenz rule is **1288 bits**, not the ≈ 1400 of the pilot report, whose source-length constant was corrected by Amendment 6 (§7.5). The pilot report's errata section does not yet carry this correction.

### 7.6 Decisions the protocol leaves open

Two do not block v1.1 but must be settled before cross-domain comparison: the exact amortisation policy for libraries shared between domains (§6 of the protocol), and the identifiable-precision rule for continuous parameters in non-regular model families (§5.2).

### 7.7 Method of development and mandatory expert review

The framework and protocol were produced through rounds of cross-criticism among several AI systems under human supervision. This is robust to errors the systems do not share and blind to those they do. No empirical result from this programme is publishable before the protocol has been reviewed by at least one human expert in MDL/algorithmic information theory and one in the chosen physical domain (§5.8).

### 7.8 Originality of *η*_ε not confirmed

We have not completed the bibliographic search that would establish whether the normalised resolution slope exists under another name in rate-distortion theory. Until we have, *η*_ε is presented as a possibly novel *reporting* quantity, not as a theoretical contribution.

---

## 8. Prespecified design and predictions for the first empirical measurement: atomic spectra (protocol §11.1)

### 8.1 Why atomic spectra first, and why never the CMB first

The protocol prioritises instrumental measurements whose processing chain does not explicitly incorporate the theory under evaluation. Experimental atomic line spectra are the cleanest available case: wavelengths and intensities measured by spectroscopy are class-1 or class-2 data (primary or calibrated), while *fitted energy levels* and *computed transition probabilities* derived from them are class-4 products of theoretical fit and may serve only as controls. The cosmic microwave background is expressly *not* a first target: the protocol (§11.2) treats it as a structured stochastic physical domain, not as noise, and requires the separation of cosmological signal, instrumental noise, masks, selection effects and processed products before any comparison — a separation that is itself theory-laden and belongs to a later stage.

### 8.2 Two tracks, asking two different questions

The measurement is split into two tracks that must never be conflated, because they answer questions that a single number cannot separate. The distinction is the empirical counterpart of the sharpest result of the pilot (§6.3, item 2): the gap between what a model family *finds* and what *exists*.

> **EXISTENCE OF COMPRESSIBLE STRUCTURE ≠ ABILITY OF A MODEL FAMILY TO DISCOVER IT.**

#### Track A — known-physics benchmark

*How much descriptive cost can known physical regularities absorb?*

Track A measures the **existence and magnitude** of compression achievable by physical regularities we already possess, applied to experimental data that were not produced using those regularities. In this track the model family **may contain the physics explicitly**: the Rydberg formula, appropriate known models of level structure, and any other physical regularity whose compressibility we wish to measure. Handing the family the answer is not a defect here — it is the design. What Track A reports is how much of the literal description of measured spectra a known law absorbs, at what resolutions, and how that absorption scales.

**Critical condition, without which Track A is void:** the data set must not have been constructed, calibrated or fitted using the same structure being evaluated. Line wavelengths measured by spectroscopy are admissible; energy levels obtained by fitting a level model to those wavelengths, and transition probabilities computed from such a model, are class-4 products (§5.3) and may serve only as controls. A violation of this condition turns Track A into a measurement of the pipeline rather than of the world, and the provenance classification is what stands between the two.

Track A reports, at minimum: *ρ*_MDL; *η*_ε across the preregistered resolutions; *g*_pred and *g*_total on held-out elements; the scaling of all of these with *n*; robustness across the two reference stacks; and the surrogate comparison.

#### Track B — blind discovery

*Can a generic model family discover the compression?*

Track B measures whether structure that Track A shows to exist can be **found** by a family that was never given it. The family must **not** receive as primitives or as charged libraries: the Rydberg formula, any quantum-defect parametrisation, level structure, or equivalent physical tables. It may include symbolic regression, generic algebraic families, structural search, and other generic methods declared in advance. Any structure the family discovers **pays its own description length in full**, so that a rediscovered Rydberg relation competes against the literal line list on the same accounting.

We state the restriction at the level of primitives deliberately: any family expressive enough to be interesting contains such a regularity implicitly, as something it can construct, and no declaration makes that false. What preregistration buys is not a family innocent of the answer but a family that must pay for it.

**How a Track B result must be read.** A high *ρ*_MDL in Track B does **not** show that atomic spectra are incompressible. It shows that the declared generic family did not find the structure — a statement about the family, not about the world. The pilot makes the point unmistakable: Rule 30 and a PCG64 stream have *r*_generic ≈ 1.0009 and 1.0005 while their generators are a few hundred bits long (§6.2). A ratio near 1 is never a certificate of incompressibility. Track A exists precisely so that, in this domain, we have an independent measurement of what is there to be found.

#### What is preregistered for both tracks before *D*_test is seen

For the chosen spectral corpus, and separately for each track: the representation (line list with wavelength, uncertainty, intensity, element and ionisation stage; units; ordering; treatment of blended or unresolved lines); the provenance class of each field, with the database version and access date; the distortion metric *d* (in the first instance, absolute and relative wavelength error, both preregistered); the resolution set *ε*₁ > … > *ε*_*m*, expressed relative to the *declared instrumental uncertainty* of each line, so that no *ε* below the measurement floor is interpreted (Amendment 1); the quantiser; the residual code; the precision rule for continuous parameters; two reference stacks with declared arithmetic; the null model *M*₀ (literal coding of the quantised line list) together with its description length *L*_*U*(*M*₀), which the pilot never defined (§7.5 bis) and which both *ρ*_MDL and *g*_total require; the model family for that track, with members at increasing expressive power and their full description length charged; nested corpora by element and by ionisation stage, increasing diversity and not only line count; the train/test partition by element (and, within elements, by spectral region) frozen before any model is fitted; and the surrogates (wavelength shuffling within element, histogram-preserving permutation across elements).

### 8.3 Predictions (qualitative and conditional; no numbers are asserted)

We state the *form* of the predictions and their falsifiers, not their values. Any number placed here before the measurement would be a number we had not measured.

**Track A.** If H1 and H2 hold for this domain, then within the valid regime (*ε* above the instrumental floor) the family containing the known physics will reach *ρ*_MDL clearly below 1 on the training corpus and *g*_pred clearly below 1 on held-out elements, and *η*_ε will be ≪ 1 across the preregistered resolutions: additional wavelength precision will be absorbed by reusable structure rather than paid literally. The advantage will persist as *n* grows by adding elements and ionisation stages, not only lines. *g*_total will be reported alongside *g*_pred and is expected to **fall towards *g*_pred as the test block grows** (§5.5); it is not required to be small at every block size.

**Track B.** No prediction is made about whether the blind family recovers the structure. Both outcomes are informative and neither is a falsifier of H1: recovery would show that the regularity is reachable by generic search at a description cost worth paying; failure would locate atomic spectra on the far side of the same gap that separates *r*_generic ≈ 1 from *ρ*_oracle ≈ 0.01 for Rule 30 in the pilot. The quantity of interest is the **distance between the two tracks**, which is the empirical analogue of the oracle gap and, to our knowledge, has not been measured for a physical domain.

**Surrogates**, in both tracks: wavelength-shuffled line lists will yield *ρ*_MDL near the null value, and the surrogate/real gap will be reported under both reference stacks.

**Falsifiers**, from §5.6, and applying to **Track A**, where the structure is known to be in the family: *ρ*_MDL converging towards 1; *g*_pred ≈ 1 on held-out elements; *g*_total failing to approach *g*_pred as the test block grows; a qualitative change of the ordering between real and surrogate data when *U*_ref is changed; no difference between real data and surrogates; *η*_ε ≈ 1 across the valid regime. A high *ρ*_MDL in **Track B** is not on this list, for the reason given in §8.2.

### 8.4 Outcomes that are valuable even if the hypothesis fails

The programme's value does not depend on H1 being confirmed for physics. Two negative-looking outcomes are informative:

(a) **Physics is not special at equal level and resolution.** If, once descriptive levels and resolutions are matched, *ρ*_MDL for atomic spectra in Track A is comparable to *ρ*_MDL for a non-physical control domain, the apparent exceptionality of physics came from the *stratum* usually chosen, not from the domain. That would be a measured correction to a widely held intuition.

(b) **A universal stratigraphy.** If every domain shows the same ordering *laws → realisations → microhistory*, the interesting quantity is not "which domain compresses" but the *shape* of the surface 𝒞(level, *n*, *ε*) that all domains share. The pilot already measured (b) in miniature inside Lorenz (§6.3, Level A / Level B decomposition): a rule of 1288 fixed bits; a trajectory costing ≈ *λ*/ln 2 bits per time unit at fixed resolution; a literal microstate.

### 8.5 Deviations

Anything found during this measurement that conflicts with v1.1 will be recorded as a documented deviation or will motivate an explicit v1.2. Once frozen, the protocol will not be edited. Until then — its present state — amendments remain admissible, and Amendment 6 is one (§7.5).

---

## 9. Conclusion

We have described an instrument, not a discovery. The instrument is a preregistration-ready, two-part MDL accounting with explicit fidelity, quantisation, reference-code and null-model declarations, reported in three columns that keep "what a generic coder finds", "what exists" (synthetic controls only) and "what the preregistered family finds, including its own cost" from being confused; a resolution slope defined only where resolution is physical; an out-of-sample ratio that can exceed 1; and a declared list of outcomes that count against the hypothesis. On synthetic controls it separates strata, recovers generators out of sample, refuses spurious ones, collapses surrogates, and recovers the Lyapunov predictability scale to within a discrepancy that we report rather than adjust.

The exchange did not resolve the distinction relevant to the present programme: compression achieved under a specified model family and coding convention is not identical to exact algorithmic compressibility. We do not claim the dispute was unresolvable, nor that it was waiting for an instrument, nor that anything measured here settles it. Declaring the conventions and measuring the boundary between "the regularity compresses most of the description" and "the irreducible perturbation lives in the residual", as a function of data set size, resolution and descriptive level, is what this framework is for. Whether fundamental physics occupies an exceptionally low region of that surface, whether that region survives changes of reference code, resolution and out-of-sample test, and whether other domains share its shape, are now empirical questions. A negative answer is a result and will be published as one.

If the empirical surfaces should show that certain regularities keep absorbing growing quantities of observational information without paying a comparable descriptive cost — after the precision of parameters is paid, the language fixed and the quantisation frozen — then the fact that started the programme stands: there is far more world explained than information used to formulate the rules that explain it.

---

## Acknowledgements

*[To be completed.]* The framework and protocol were developed by the author with the assistance of several AI systems used for cross-criticism; the limits of that method are stated in §5.8 and §7.7.

## Data and code availability

The pilot code (`src/piloto_10_1.py`, `src/verificacion_piso_y_eta.py`, `src/lorenz_checkpoints.py`, `src/ruido_oos_semilla.py`), its archived outputs (`results/`), the pilot report with its errata, the protocol changelog and Amendment 6, the reproduction record of 2026-08-26, and the consolidated protocol prepared for freezing (`protocol/protocolo-v1-1-consolidado.md`), the pilot errata (`docs/ERRATA-piloto-v1-1.md`), and the changelogs and validation reports of this and the preceding draft are in the project repository. **No preregistration record exists yet to cite.** Protocol v1.1, once frozen, is to be deposited with its SHA-256 hash in a public preregistration before the first empirical measurement; the hash will be cited here once it exists.

---

## References

*All entries are provisional. Entries marked `[VERIFY]` have not been checked against the primary source; bibliographic details left blank are unknown to the author at the time of drafting and must not be filled from memory. See `PENDIENTES.md`.*

1. McAllister, J. W. (2003). Algorithmic randomness in empirical data. *Studies in History and Philosophy of Science*, 34. `[VERIFY]`
2. Twardy, C. R., Gardner, S., & Dowe, D. L. (2005). Empirical data sets are algorithmically compressible: Reply to McAllister. *Studies in History and Philosophy of Science*, 36. `[VERIFY]`
3. McAllister, J. W. (2005). Reply to Twardy, Gardner and Dowe. *Studies in History and Philosophy of Science*, 36. `[VERIFY — title and pages]`
4. Solomonoff, R. J. (1964). A formal theory of inductive inference, Parts I and II. *Information and Control*, 7. `[VERIFY]`
5. Solomonoff, R. J. (1978). Complexity-based induction systems: comparisons and convergence theorems. *IEEE Transactions on Information Theory*, 24. `[VERIFY]`
6. Hutter, M. (2005). *Universal Artificial Intelligence*. Springer. `[VERIFY]`
7. Rissanen, J. (1978). Modeling by shortest data description. *Automatica*, 14. `[VERIFY]`
8. Grünwald, P. D. (2007). *The Minimum Description Length Principle*. MIT Press. `[VERIFY]`
9. Wallace, C. S., & Boulton, D. M. (1968). An information measure for classification. *Computer Journal*, 11. `[VERIFY]`
10. Wallace, C. S. (2005). *Statistical and Inductive Inference by Minimum Message Length*. Springer. `[VERIFY]`
11. Lewis, D. — best-system account of laws. `[VERIFY — which work is cited]`
12. Wheeler, B. — algorithmic theory of laws. `[VERIFY — full reference unknown; locate]`
13. Li, M., & Vitányi, P. M. B. *An Introduction to Kolmogorov Complexity and Its Applications*. Springer. `[VERIFY — edition]`
14. Chaitin, G. J. — incomputability of *K* / non-certifiability of incompressibility. `[VERIFY — which work]`
15. Vereshchagin, N. K., & Vitányi, P. M. B. (2010). Rate distortion and denoising of individual data using Kolmogorov complexity. *IEEE Transactions on Information Theory*, 56. `[VERIFY]`
16. de Rooij, S., & Vitányi, P. M. B. Approximating rate-distortion graphs of individual data: experiments in lossy compression and denoising. *IEEE Transactions on Computers*. `[VERIFY — year, volume]`
17. Cilibrasi, R., & Vitányi, P. M. B. (2005). Clustering by compression. *IEEE Transactions on Information Theory*, 51. `[VERIFY]`
18. Zenil, H., et al. — Coding Theorem Method / Block Decomposition Method. `[VERIFY — which paper]`
19. Leyva-Acosta, Acuña Yeomans, & Hernández-Quiroz (2026). Weak correlation between compression-based and execution-based complexity estimators. `[VERIFY — title, venue, DOI unknown]`
20. Crutchfield, J. P. (1994). The calculi of emergence. *Physica D*, 75. `[VERIFY]`
21. Shalizi, C. R., & Crutchfield, J. P. (2001). Computational mechanics: pattern and prediction, structure and simplicity. *Journal of Statistical Physics*, 104. `[VERIFY]`
22. Schmidt, M., & Lipson, H. (2009). Distilling free-form natural laws from experimental data. *Science*, 324. `[VERIFY]`
23. Udrescu, S.-M., & Tegmark, M. (2020). AI Feynman: a physics-inspired method for symbolic regression. *Science Advances*, 6. `[VERIFY]`
24. Exhaustive symbolic regression with MDL model selection in astrophysics (2026). `[VERIFY — reference to be located]`
25. Delétang, G., et al. (2023). Language modeling is compression. arXiv:2309.10668. `[VERIFY — final venue]`
26. Bennett, C. H. (1988). Logical depth and physical complexity. In *The Universal Turing Machine: A Half-Century Survey*. `[VERIFY]`
27. Theiler, J., Eubank, S., Longtin, A., Galdrikian, B., & Farmer, J. D. (1992). Testing for nonlinearity in time series: the method of surrogate data. *Physica D*, 58. `[VERIFY]`
28. Pesin, Ya. B. (1977). Characteristic Lyapunov exponents and smooth ergodic theory. *Russian Mathematical Surveys*, 32. `[VERIFY]`
29. Eckmann, J.-P., & Ruelle, D. (1985). Ergodic theory of chaos and strange attractors. *Reviews of Modern Physics*, 57. `[VERIFY]`
30. Lorenz, E. N. (1963). Deterministic nonperiodic flow. *Journal of the Atmospheric Sciences*, 20. `[VERIFY]`
31. Source for *λ*₁ ≈ 0.906 of the Lorenz system at (10, 28, 8/3). `[VERIFY — e.g. Sprott, Chaos and Time-Series Analysis, 2003]`
32. Wolfram, S. (2002). *A New Kind of Science*. Wolfram Media; Cook, M. (2004). Universality in elementary cellular automata. *Complex Systems*, 15. `[VERIFY]`
33. O'Neill, M. E. (2014). PCG: a family of simple fast space-efficient statistically good algorithms for random number generation. Harvey Mudd College technical report. `[VERIFY]`
34. Tegmark, M., Aguirre, A., Rees, M. J., & Wilczek, F. (2006). Dimensionless constants, cosmology, and other dark matters. *Physical Review D*, 73, 023505. `[VERIFY]`

---

*Version history: v0.1 (2026-08-26) — first complete draft, in English, prepared by an AI assistant under the supervision of Maximiliano Winter from the frozen conceptual framework v5.2, protocol v1.0 + changelog v1.1, the final pilot report, the archived outputs, the reproduction record of 2026-08-26 and the consolidated impact/originality audit notes. No frozen document was modified. Every number in §6 is taken from the pilot report or the archived outputs; no result was generated for this draft. — v0.2 (2026-08-26, same day): incorporates Amendment 6 (traceability; dual noise control): *ρ*_oracle = 0.0053 confirmed by script; resolution-sweep *ρ*_MDL values corrected for a stale source-length constant (0.0293–0.0106 → 0.0267–0.0098, *η*_ε unchanged); extended-precision slope reported as mean 64.2, range 29–98, least-squares 67.6; seeded negative control added; §7.5 rewritten from "gaps" to "gaps and closure". — v0.3 (2026-08-26, new file `preprint-v0-3.md`; v0.2 retained unmodified as `preprint-v0-1.md`, whose filename and content had diverged): formal repairs — complete baseline *L*₀^full making *ρ*_MDL ≤ 1 exact (§4.3); *g* split into *g*_pred and *g*_total throughout (§4.5, §6.2, §6.3, §8.3); measured re-synchronisation horizon *h*(*p*, *ε*) replacing "Lyapunov horizon" (§4.7, §6.3); every claim of a completed preregistration or freezing withdrawn (title note, abstract, §5.8, §8.5, §9); Lorenz Level A cost corrected 1400 → 1288 bits under Amendment 6 (§6.3); Track A / Track B decomposition of the Lorenz accounting (§6.3); metrological claims separated from claims about nature (§6.6); the family restriction for atomic spectra weakened from "does not contain the answer" to a restriction on primitives (§8.2); the characterisation of the 2003–2005 exchange softened from "could not be settled" to "did not converge" (§1, §9). New limitations §7.5 bis and §7.8; no limitation removed; no reference un-marked; no originality claim strengthened; no experimental figure invented. Changelog and validation report accompany this file. — v0.4 (2026-08-26, new file `preprint-v0-4.md`; v0.3 retained unmodified): "Preregistered" removed from the title until a public deposit exists; **Track A / Track B redefined** as the two-track design of the empirical measurement — known-physics benchmark and blind discovery (§8.2–§8.3) — and the Lorenz decomposition renamed **Level A / Level B** (§6.3), the earlier limitation about an unconfirmed reading of "track" being retired as resolved; *g*_total made **symmetric**, with *L*_*U*(*M*₀) in the denominator, and every assertion that *g*_total exceeds *g*_pred removed (§4.5); the historical pilot values identified as ***g*_total^bare** and not reinterpreted, with *g*_pred now printed by `src/g_metricas_oos.py` (§6.2); the success criterion restated as *ρ*_MDL ≪ 1, *η*_ε ≪ 1, *g*_pred ≪ 1 with *g*_total as a scaling prediction *g*_total → *g*_pred rather than a threshold (§5.5); "*ρ* = 1 exactly when *M*₀ wins" replaced by "when the null description is optimal, possibly tied" (§4.3); *h*(*p*, *ε*) carried into the consolidated protocol (§4.7); the McAllister–Twardy characterisation fixed in its cautious form (§2, §9). No number recomputed by hand; no limitation or erratum removed; no reference un-marked; no originality claim strengthened; no empirical data set opened.*
