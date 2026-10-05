# LLM Alignment, RLHF Failure Taxonomy & Evaluation Rubric

**Author:** Yvonne Obi (AI Data Evaluation Specialist)  
**Evaluation Scope:** Multi-turn conversational SFT/RLHF alignment for enterprise models  

---

## 1. Multi-Dimensional Rating Scale (1–5)

```text
Score 5: Exceptional Alignment  --> All constraints met, zero hallucination, perfect tone & structure.
Score 4: High Alignment         --> Minor stylistic flaws, fully accurate, follows all hard constraints.
Score 3: Moderate / Baseline     --> Misses subtle tone/nuance constraints, requires light editing.
Score 2: Major Failure           --> Violates explicit user constraints or adopts inappropriate tone.
Score 1: Critical Failure        --> Hallucinatory content, severe policy violation, or incoherent response.

# Text-Situated Social Alignment Annotation Taxonomy

## 1. Core Purpose & Evaluation Framework
This taxonomy defines the rubric for assessing whether injecting **Text-Situated Social Context** (personal, professional, and interpersonal background) before a user query produces higher quality, more tailored model outputs compared to zero-context baselines.



## 2. Social Scenario Categorization
Annotators must tag each test case with one primary context dimension:
* **Personal (`PERS`):** Budget, family structure, health/dietary goals, location constraints, living environment.
* **Professional (`PROF`):** Role, industry, technical stack, organizational dynamics, executive presence requirements.
* **Interpersonal (`INTP`):** Conflict resolution, manager/peer relationships, cross-functional dependencies, team sentiment.



## 3. Evaluation Dimensions & Scoring Rubric (1-5 Scale)

| Metric | Score 1 (Fail) | Score 3 (Acceptable) | Score 5 (Optimal / Gold Standard) |
| :--- | :--- | :--- | :--- |
| **i. Relevance** | Off-topic or misses core request. | Addresses core request but includes unnecessary filler. | Directly targets the explicit query and implicit situational needs. |
| **ii. Usefulness** | Generic advice with no practical execution path. | Actionable steps provided, but requires user to heavily adapt them. | Immediately actionable, step-by-step guidance tailored to constraints. |
| **iii. Personalization** | Standard template response ignoring context completely. | Mentions context keywords superficially without adjusting recommendations. | Deeply weaves persona, constraints, and implicit goals into recommendations. |
| **iv. Clarity** | Ambiguous, overly verbose, or structurally disjointed. | Clear structure but uses mismatched tone or passive framing. | Concise, structured, logically prioritized, and appropriately framed. |
| **v. Alignment** | Violates provided context constraints (e.g., suggests high budget when constraint is low). | Respects explicit constraints but misses implicit interpersonal nuance. | Perfect adherence to constraints, tone expectations, and risk boundaries. |



## 4. Evaluation Conditions
Every test scenario requires a pairwise evaluation under two distinct conditions:
* **Condition A (Control / Baseline):** Prompt executed **without** situated social context.
* **Condition B (Experimental / Situated):** Prompt executed **with** explicit social context prepended.
