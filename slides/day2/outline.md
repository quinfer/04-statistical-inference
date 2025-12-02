# Day 2 Slide Outline — Causal & Fair Modelling for Credit Decisions

## 1. Recap & Objectives (5 min)
- Key takeaways from Day 1
- Day 2 goals: causal thinking, fairness metrics, mitigation toolkit

## 2. Motivation: When Correlation Fails (15 min)
- Case study: misinterpreting spread compression
- Illustrate Simpson’s paradox with sector splits
- Bridge to causal DAGs

## 3. Causal Inference Primer (25 min)
- Treatment/control terminology, potential outcomes
- DAG example for credit spread analysis
- Randomization vs. observational data
- Adjustment strategies: covariate control, DML overview

## 4. Hands-On Example (20 min)
- Step-by-step look at LinearDML pipeline
- Visualize ATE and heterogeneity across sectors
- Discuss policy interpretations

## 5. Break (10 min)

## 6. Fairness in Finance (30 min)
- Regulators: ECOA, FCA’s AI expectations, OCC model risk bulletins
- Metrics: demographic parity, equalized odds, predictive parity
- Trade-offs & documentation requirements (model risk memos)

## 7. Fairness Diagnostics Demo (20 min)
- Show Fairlearn MetricFrame outputs
- Interpret disparity table from lab dataset
- Introduce mitigation techniques (reweighing, thresholding, reductions)

## 8. Lab Briefing (15 min)
- Walk through `day2_causal_fairness.ipynb`
- Highlight data join steps, DML cell, fairness section
- Outline deliverable: one-page memo template (include in resources)

## 9. Wrap-Up & Prep for Day 3 (10 min)
- Q&A on fairness regulators might ask
- Preview Bayesian uncertainty and scenario analysis

### Slide Assets Needed
- DAG diagrams (credit spread example)
- Fairness metric definitions table
- Screenshots of lab outputs (ATE chart, parity table)
- Memo template snippet
