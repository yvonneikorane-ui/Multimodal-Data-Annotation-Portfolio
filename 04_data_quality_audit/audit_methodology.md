### File 4: `04_data_quality_audit/audit_methodology.md`
**Path:** `Multimodal-Data-Annotation-Portfolio/04_data_quality_audit/audit_methodology.md`

```markdown
# Data Quality Operations & Inter-Annotator Agreement Methodology

**Author:** Yvonne Obi (Lead AI Data Evaluation Specialist)  
**Scope:** Automated QA auditing, telemetry error logging, and agreement metric calculation  



## 1. Inter-Annotator Agreement (IAA) Metrics

The statistical measure used for evaluator reliability is **Cohen's Kappa ($\kappa$)**:

$$\kappa = \frac{P_o - P_e}{1 - P_e}$$

Where:
- **$P_o$**: Relative observed agreement among evaluators.
- **$P_e$**: Hypothetical probability of chance agreement.



## 2. Enterprise Quality Thresholds

| Agreement Metric ($\kappa$) | Quality Status | Operational Action |
| :--- | :--- | :--- |
| **0.81 – 1.00** | **Production Grade** | Batch approved for training set ingestion. |
| **0.61 – 0.80** | **Moderate Variance** | Guideline clarification distributed; 10% re-audit. |
| **< 0.60** | **Unacceptable** | Batch rejected; full annotator re-alignment required. |

<Image src="image_agent_tag_3547723137061829949" alt="Inter-Annotator Agreement workflow pipeline diagram" caption="Quality Assurance and Inter-Annotator Agreement workflow" />



## 3. Severity Categorization Matrix
- **High Severity:** Null coordinates, schema violations, out-of-range ratings (blocks parser).
- **Medium Severity:** Class taxonomy typos, incorrect occlusion estimates.
- **Low Severity:** Date formatting discrepancies (ISO-8601 vs epoch).
