# Next Steps & Enhancements

1. **Slide Decks (xaringan/Quarto)**
   - Create `slides/day1/...day4` with speaker notes and embedded screenshots from labs.
   - Use a shared SCSS theme to match branding.

2. **Assessment Rubrics**
   - Draft rubrics for Day 1–3 labs (data quality, causal reasoning, Bayesian interpretation) and capstone pitch.
   - Include pass/fail criteria aligned with Mini-MBA grading policies.

3. **Automation Scripts**
   - Add `scripts/bloomberg_export_templates/` with sample Excel formulas or BQL queries to standardize data pulls.
   - Consider a `make refresh-data` helper that copies the latest instructor bundle into `data/bloomberg/`.

4. **Optional Python Packages**
   - Evaluate `econml` and `pymc` install times on institutional networks; provide light versions (e.g., `dowhy`, `cmdstanpy`) if bandwidth is constrained.

5. **Video Walkthroughs**
   - Record 5–10 min screencasts per lab for asynchronous learners; host privately (LMS, Vimeo, or Panopto).

6. **Capstone Extensions**
   - Add modules for streaming data (Kafka mock), real-time alerts, or integration with policy engines.
   - Provide a Docker Compose file for teams who want to run the app locally with persistence.

7. **Certification & Badging**
   - Define completion criteria (e.g., >70% lab average + capstone pass) and design a digital badge for LinkedIn.

Use this checklist to prioritize future iterations based on cohort feedback and resource availability.
