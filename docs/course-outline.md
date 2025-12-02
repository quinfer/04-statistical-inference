# Mini-MBA: Responsible Data Science for Finance — 4-Day Outline

| Day | Theme | Morning Block | Afternoon Block | Bloomberg Inputs | Deliverables |
| --- | --- | --- | --- | --- | --- |
| 1 | Responsible Foundations & Data Controls | Regulatory landscape (Basel III/IV, EU AI Act, SFDR), ethics playbook, data-governance lifecycle | Lab `day1_data_controls.ipynb`: ingest ESG exports, build data dictionary, run validation report, append compliance log | `ESG <GO>` fundamentals export (ENV/SOC/GOV disclosure scores, sector, country) | Quality report screenshot + 3-bullet mitigation note + `data_access_log.csv` |
| 2 | Causal & Fair Modelling | Causal DAGs for credit spreads, uplift vs. correlation, fairness frameworks (ECOA, FCA) | Lab `day2_causal_fairness.ipynb`: join spreads + macro series, run DML ATE, audit parity & equalized odds, mitigate with Fairlearn | `CRPR <GO>` or `CACS <GO>` credit-spread panel, `ECST <GO>` macro surprises, optional fairness attribute mapping | One-page model risk memo + notebook export |
| 3 | Bayesian Yield-Curve Risk | Bayesian vs. classical inference, prior setting aligned to policy, scenario communication | Lab `day3_bayesian_risk.ipynb`: PyMC term-structure model, posterior predictive checks, scenario builder | `YC <GO>` term-structure export (1M–30Y), optionally `FOMC <GO>` events, `ECST` macro surprises | Fan chart + scenario table + reflection paragraph |
| 4 | Governance & Capstone App | Model cards, monitoring, deployment-lite patterns, sprint planning | Lab `day4_capstone_app.ipynb` + `app/streamlit_app.py`: ESG-aware treasury advisor (Gradio/Streamlit), SHAP explanations, policy sliders | Reuse prior datasets; optionally `NEWS <GO>` sentiment or ETF flows for extra signals | Working demo link/screenshot + model card + pitch slide |

## Course Logistics
- Format: 4 consecutive days, ~6.5 instructional hours each (AM theory, PM lab, evening deliverable).
- Modality: in-person or live-virtual with Google Colab; instructors distribute Bloomberg CSV bundle beforehand via secure channel (SFTP or Drive).
- Cohort size: 20–30 participants, working in pairs for labs and teams of 3–4 for the capstone.
- Assessment weighting: Day 1–3 labs (45%), capstone app (40%), participation/reflections (15%).

## Learning Objectives by Day
### Day 1
- Explain why governance, ethics, and regulation matter in financial data science.
- Operationalize a data lineage log and automated QC script for ESG disclosures.

### Day 2
- Distinguish causal vs. correlational interpretations in spread analytics.
- Quantify fairness metrics and apply at least one mitigation strategy.

### Day 3
- Translate policy beliefs into priors and communicate Bayesian uncertainty to non-technical stakeholders.
- Build stress scenarios that tie macro shocks to yield-curve outcomes.

### Day 4
- Integrate governance controls, explainability, and UI design into a fintech-style analytics workflow.
- Pitch a responsible AI product aligned with treasury/fintech business value.

## Required Assets in Repo
- `labs/dayX_*.ipynb` notebooks (Colab friendly).
- `app/streamlit_app.py` for optional local/Streamlit demo.
- `data/bloomberg/` directory for instructor-provided CSVs.
- `docs/` for syllabus, setup guides, rubrics (expand as needed).

Use this outline when recruiting students, planning instructor notes, or preparing accreditation paperwork. Adjust timings to reflect breaks and Q&A slots for your delivery context.
