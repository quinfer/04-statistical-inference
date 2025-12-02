# Labs Overview
All hands-on work lives in the `labs/` directory and is designed for Google Colab. Each notebook includes `pip install` cells, Drive upload helpers, and synthetic fallback data so you can test without Bloomberg files.

| Notebook | Theme | Inputs | Outputs |
| --- | --- | --- | --- |
| `day1_data_controls.ipynb` | ESG data governance & quality controls | `esg_scores_YYYYMMDD.csv` | Data dictionary JSON, quality report table, `data_access_log.csv` |
| `day2_causal_fairness.ipynb` | Credit-spread causal inference + fairness | `credit_spreads_YYYYMMDD.csv`, `macro_indicators_YYYYMMDD.csv` (optional fairness map) | DML ATE estimate, fairness metrics, mitigation comparison |
| `day3_bayesian_risk.ipynb` | Bayesian yield-curve scenario analysis | `yield_curve_YYYYMMDD.csv`, `macro_surprises.csv` | Posterior summaries, fan chart, scenario tables |
| `day4_capstone_app.ipynb` | ESG-aware treasury app sprint | Reuse prior datasets (+ optional NEWS/ETF data) | Gradio demo, optional Streamlit/ngrok link, model card notes |

## Running Locally vs. Colab
- **Colab:** click the notebook → "Open in Colab" and follow on-screen instructions.
- **Local Jupyter:** install dependencies via `pip install -r ../requirements.txt`, then run `jupyter lab`. Some cells call Colab-specific APIs; they include guards to skip when running locally.

## Deliverables Checklist
- Day 1: PDF or HTML of notebook sections + `data_access_log.csv`.
- Day 2: Model risk memo summarizing causal/fairness insights.
- Day 3: Visuals (fan chart + scenario table) embedded into slides.
- Day 4: Link/screenshot of the app, plus model card & pitch slide.

Feel free to duplicate notebooks for additional cohorts (e.g., `day1_data_controls_cohortB.ipynb`). Keep synthetic helper data so future instructors can rehearse without Bloomberg access.
