# Assessment Rubrics

Each lab and the capstone have structured rubrics to ensure consistent scoring across cohorts. Default grading scale: **Outstanding (4)**, **Meets (3)**, **Developing (2)**, **Insufficient (1)**. Multiply each dimension by weight for final score.

## Day 1 Lab — ESG Data Controls (Weight 15%)
| Dimension | Weight | Outstanding (4) | Meets (3) | Developing (2) | Insufficient (1) |
| --- | --- | --- | --- | --- | --- |
| Data Handling & Lineage | 0.3 | All files clearly referenced, timestamps recorded, lineage diagram included | Files referenced, minimal lineage note | Partial lineage, missing timestamps | No lineage or unclear sources |
| Quality Checks | 0.35 | Automated checks cover schema, ranges, duplicates, stale dates; remediation plan documented | Checks run with minor gaps, remediation noted | Manual or incomplete checks, limited remediation detail | No evidence of validation |
| Compliance Log & Reporting | 0.2 | Log updated with complete metadata, summary memo crisp | Log updated but summary shallow | Log incomplete or inconsistent | Missing log |
| Reflection & Communication | 0.15 | Insightful takeaways linking to governance framework | Basic summary | Vague commentary | Missing reflection |

## Day 2 Lab — Causal & Fair Modelling (Weight 15%)
| Dimension | Weight | Outstanding | Meets | Developing | Insufficient |
| --- | --- | --- | --- | --- | --- |
| Causal Specification | 0.3 | DAG + rationale, correct covariate selection, assumptions stated | DAG provided, assumptions partly noted | Minimal causal reasoning | None |
| Treatment Effect Estimation | 0.25 | DML run with diagnostics, ATE interpreted in business terms | DML run, basic interpretation | Model errors or misinterpretation | Not attempted |
| Fairness Diagnostics | 0.25 | Multiple metrics computed, disaggregated insights, clear disparities | At least one metric computed and discussed | Metrics misapplied or not interpreted | Missing fairness analysis |
| Mitigation Strategy | 0.2 | Appropriate technique applied, trade-offs discussed | Mitigation attempted with limited analysis | Superficial or incorrect approach | None |

## Day 3 Lab — Bayesian Risk (Weight 15%)
| Dimension | Weight | Outstanding | Meets | Developing | Insufficient |
| --- | --- | --- | --- | --- | --- |
| Model Construction | 0.3 | Priors justified, data prepared cleanly, model converges | Model runs with minor issues | Model unstable or unjustified priors | No working model |
| Posterior Interpretation | 0.3 | Summaries & fan charts interpreted for business stakeholders | Charts present with brief notes | Visuals lacking explanation | No outputs |
| Scenario Analysis | 0.25 | Scenario table ties macro shocks to actions | Scenario built but weak narrative | Minimal scenario detail | None |
| Communication | 0.15 | Reflection integrates policy implications | Basic reflection | Shallow response | Missing |

## Capstone — ESG-Aware Treasury App (Weight 40%)
| Dimension | Weight | Outstanding | Meets | Developing | Insufficient |
| --- | --- | --- | --- | --- | --- |
| Data Integrity & Controls | 0.2 | Automated validation + logs, policies enforced, no hard-coded secrets | Controls partially implemented | Minor data issues, limited logging | Missing controls |
| Policy Engine & Analytics | 0.25 | Allocation logic robust, configurable, aligns with policy | Core logic works with minor gaps | Partially functional | Not functional |
| Explainability & Fairness | 0.15 | SHAP/feature insights clear, fairness considerations documented | Basic feature importance shown | Minimal explainability | None |
| UX & App Experience | 0.15 | Clean UI, intuitive workflow, exports or screenshots provided | Functional UI with minor UX issues | Clunky or incomplete UI | No UI |
| Governance Artifacts | 0.15 | Model card + audit log + pitch deck complete | Most artifacts present | Artifacts incomplete | Missing |
| Presentation & Q&A | 0.1 | Engaging demo, clear value prop, confident Q&A | Adequate presentation | Unclear messaging | No presentation |

## Grading Notes
- Overall passing threshold: 70% cumulative score + capstone score ≥ 3 (Meets).
- Teams receive rubric feedback per dimension; individuals receive participation notes.
- Rubrics can be adapted if local accreditation requires letter grades; adjust weights accordingly.
