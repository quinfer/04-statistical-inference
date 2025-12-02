# Google Colab Delivery Guide

This course is optimized for Google Colab so participants can work from managed laptops without local Python installs. Follow the steps below to keep sessions smooth and compliant.

## 1. Instructor Prep
1. **Bundle data**: Zip the latest Bloomberg CSV/XLSX exports into `data/bloomberg/mini-mba-data.zip`. Include:
   - `esg_scores_YYYYMMDD.csv`
   - `credit_spreads_YYYYMMDD.csv`
   - `macro_indicators_YYYYMMDD.csv`
   - `yield_curve_YYYYMMDD.csv`
   - Optional extras (news sentiment, ETF flows)
2. **Distribute securely**: Upload to a private Google Drive or LMS resource folder. Share read-only links at least 48 hours before Day 1.
3. **Verify notebooks**: Open each `labs/dayX_*.ipynb` in Colab, run `Runtime → Run all`, ensure the synthetic-fallback path works when data files are absent.

## 2. Participant Checklist
- Google account with Drive access.
- Stable internet; Chrome/Edge recommended.
- Ability to download the provided data bundle locally (for manual upload) or copy into personal Drive.

## 3. Launching a Lab
1. Navigate to the GitHub repo page → click the notebook → "Open in Colab" badge (or use `https://colab.research.google.com/github/<ORG>/<REPO>/blob/main/labs/...`).
2. Once Colab loads:
   - Select `Runtime → Change runtime type → Python 3` (no GPU needed).
   - Run the first cell to install dependencies. This takes ~2–3 minutes on free tiers.
3. Provide data:
   - **Preferred**: Upload the instructor bundle to your Google Drive (e.g., `MyDrive/mini-mba-data/`) and update the notebook helper `copy_from_drive("mini-mba-data")`.
   - **Alternative**: Use `files.upload()` to drag-drop the CSVs directly; they persist only for the current session.
4. Update placeholder filenames (e.g., replace `esg_scores_SAMPLE.csv` with your actual file names). Cells will raise `FileNotFoundError` if paths are wrong—fix names and re-run.

## 4. Saving Work
- Use `File → Save a copy in Drive` early in each session; rename to `dayX_lastname_team.ipynb`.
- After completing the lab, download both `.ipynb` and exported PDF (`File → Print → Save as PDF`).
- Ensure generated artifacts (`data_access_log.csv`, plots, screenshots) are downloaded or synced to Drive before closing the tab—runtime storage resets when idle for ~1 hour.

## 5. Troubleshooting
| Issue | Fix |
| --- | --- |
| `pip install` takes too long | Run cells once; avoid restarting runtime mid-lab. Consider Colab Pro if class consistently exceeds 12h limits. |
| `ModuleNotFoundError` after restart | Re-run the installation cell; Colab clears packages when runtime resets. |
| `FileNotFoundError` for CSV | Double-check Drive mount path (`/content/drive/MyDrive/...`) and casing. Verify you ran `copy_from_drive`. |
| `ngrok` tunnel fails (Day 4) | Rerun the Streamlit helper; ensure only one `ngrok.connect` is active. Share screenshot backups if URL expires. |

## 6. Security & Compliance
- Bloomberg T&Cs forbid exposing raw data in public repos. Do **not** push CSVs to GitHub; keep files local or in secure Drive folders.
- Instruct learners to delete data from Colab at session end (`!rm -rf /content/data`) if required by policy.
- Remind participants not to paste customer names or sensitive identifiers into notebooks—use provided synthetic IDs.

With these guidelines, the full mini-MBA can run on free Colab tiers while maintaining reproducibility and compliance.
