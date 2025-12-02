# Bloomberg Data Package (Instructor Supplied)

This folder is intentionally empty in the public repo. Instructors should place the zipped data bundle here **without committing it to Git**. Suggested contents:

| File | Source function | Key columns | Notes |
| --- | --- | --- | --- |
| `esg_scores_YYYYMMDD.csv` | `ESG <GO>` → Fundamentals export | `TICKER`, `COUNTRY`, `INDUSTRY_SECTOR`, `ENV_DISCLOSURE_SCORE`, `SOC_DISCLOSURE_SCORE`, `GOV_DISCLOSURE_SCORE`, `LAST_UPDATE_DT` | Use "Long Format" CSV; include metadata sheet if available. |
| `credit_spreads_YYYYMMDD.csv` | `CRPR <GO>` or `CACS <GO>` | `TICKER`, `ASOF_DATE`, `RATING`, `SECTOR`, `REGION`, `SPREAD_BPS` | Daily/weekly panel; keep within ~30 issuers to fit Colab memory. |
| `macro_indicators_YYYYMMDD.csv` | `ECST <GO>` / `WECO <GO>` | `ASOF_DATE`, `GDP_SURPRISE`, `INFLATION_SURPRISE`, `POLICY_RATE`, `SENTIMENT_SCORE` | Can be sourced from Bloomberg Economic Surprise Index or custom macro sheet. |
| `yield_curve_YYYYMMDD.csv` | `YC <GO>` | `DATE`, `TENOR`, `YIELD` (1M–30Y) | Choose consistent tenor set; include data for ≥ 3 years monthly. |
| Optional extras | `NEWS <GO>`, `ETF <GO>`, `PORT <GO>` | Sentiment scores, ETF flows, etc. | Useful for capstone extensions. |

## Handling Instructions
1. Keep data under 50 MB per file to respect Colab upload limits.
2. Rename files to match the expected placeholders in the labs (or update notebook constants accordingly).
3. Share the bundle via secure Drive or LMS; remind students **not** to upload Bloomberg data back to GitHub.
4. If you need to regenerate data, update the `_YYYYMMDD` suffix so teams know they have the latest drop.

## Synthetic Fallbacks
Each lab notebook can synthesize sample data if these files are missing, ensuring workshops proceed even if Bloomberg access is temporarily unavailable. For authentic results and deliverables, instructors should provide the real exports above.
