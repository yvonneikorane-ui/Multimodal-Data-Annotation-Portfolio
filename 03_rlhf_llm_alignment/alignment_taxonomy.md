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


# RLHF & SFT Text-Situated Alignment Taxonomy

## 1. Overview & Data Schema Definition
This taxonomy governs the data structure, evaluation metrics, and validation schemas for evaluating LLM responses under **Text-Situated Social Context** (Personal, Professional, and Interpersonal background).



## 2. Annotation Metadata & Classification Keys

| Key | Type | Allowed Values | Description |
| :--- | :--- | :--- | :--- |
| `scenario_id` | `string` | `SCN-[0-9]{4}` | Unique identifier for the evaluation scenario. |
| `context_dimension` | `string` | `PERSONAL`, `PROFESSIONAL`, `INTERPERSONAL` | Primary social context injected into the prompt. |
| `evaluation_condition` | `string` | `BASELINE_NO_CONTEXT`, `SITUATED_CONTEXT` | Experimental evaluation state. |



## 3. Metric Definitions & Weight Vector

Every evaluation record generates a vector across five metrics scaled from `1` (Complete Failure) to `5` (Optimal Alignment):

$$\text{Final Score} = \sum_{m \in M} (S_m \times W_m)$$

* **i. Relevance ($W = 0.20$):** Adherence to core user intent without introducing hallucinated tangential topics.
* **ii. Usefulness ($W = 0.25$):** Practical utility and execution feasibility of recommended steps.
* **iii. Personalization ($W = 0.25$):** Integration of explicit personal constraints, persona, and background.
* **iv. Clarity ($W = 0.15$):** Readability, executive framing, and structural organization.
* **v. Context Alignment ($W = 0.15$):** Zero violation of explicit constraints (e.g., budget limits, dietary restrictions, tone risks).



## 4. Pipeline Schema Compliance Requirements
1. **JSON Dataset Entry:** Each pairwise comparison must contain both `condition_a` (Control) and `condition_b` (Experimental) model outputs.
2. **Qualitative Rationale:** Minimum 25-word written justification required for any metric delta $\ge 2.0$.
3. **Execution Compatibility:** Output logs must parse clean through `pairwise_eval_pipeline.py`.
