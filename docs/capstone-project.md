# Capstone Project: ESG-Aware Treasury Analytics App

## Narrative
Corporate treasurers must allocate short-term cash while satisfying ESG policies and regulatory expectations. Teams will build a lightweight analytics app that ingests instructor-supplied Bloomberg data, applies responsible investment policies, and communicates recommendations transparently.

## Core Requirements
1. **Data Ingestion & Validation**
   - Import ESG disclosure scores (`esg_scores_YYYYMMDD.csv`) and yield curve data (`yield_curve_YYYYMMDD.csv`).
   - Run schema + range checks (reuse Day 1 helpers) and log results.
   - Provide a short lineage note (input files, timestamp, validator initials).

2. **Policy Engine**
   - Implement configurable thresholds: minimum ESG score, max country/issuer weights, and optional exclusion lists.
   - Compute recommended allocations (weights summing to 100%) optimizing for yield while respecting policy.

3. **Explainability Module**
   - Train a simple predictive model (e.g., RandomForestRegressor) linking ESG inputs to yields.
   - Surface SHAP or feature-importance visuals explaining why issuers were up- or down-weighted.

4. **User Interface**
   - Build an interactive front-end using **Gradio** (default) or **Streamlit**.
   - Minimum UI elements:
     - Policy sliders/inputs
     - Table of recommended issuers with yields & weights
     - Visualization (bar or sunburst) of allocation
     - Explainability section showing factor impacts
     - Export/Download button for policy report (CSV or PDF summarizing allocation)

5. **Governance Artifacts**
   - Model card covering data sources, assumptions, fairness considerations, monitoring triggers.
   - Audit log entry describing deployment decision.
   - Short pitch deck (3–4 slides) summarizing business value, controls, and roadmap.

## Stretch Goals (Optional)
- Integrate additional Bloomberg data (news sentiment, ETF flows) to enrich signals.
- Add fairness checks for issuer regions/countries and adjust policy accordingly.
- Deploy Streamlit app via ngrok and capture a live URL for demo.
- Incorporate scenario toggles (e.g., recession vs. boom) affecting allocations.

## Deliverables
1. Running app (Gradio link or Streamlit URL + screenshots).
2. Source notebook(s)/script(s) committed to repo (`labs/day4...`, `app/streamlit_app.py`).
3. Model card (Markdown or PDF).
4. Pitch slide deck (PDF) for final presentation.
5. Short reflection (≤250 words) documenting team roles, risks mitigated, and next steps.

## Evaluation Criteria (see rubrics for weights)
- Accuracy & Data Integrity
- Policy Compliance & Controls
- Explainability & Communication
- UX & User Story Alignment
- Documentation & Presentation

Teams will have ~3 hours of build time plus 30 minutes for presentations and feedback. Each team should appoint a spokesperson but involve all members in Q&A.
