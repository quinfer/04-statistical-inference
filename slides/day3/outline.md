# Day 3 Slide Outline — Bayesian Yield-Curve Risk

## 1. Recap & Objectives (5 min)
- Review fairness insights from Day 2
- Objectives: priors, posterior predictive checks, scenario storytelling

## 2. Classical vs. Bayesian Mindset (15 min)
- Contrast confidence intervals vs. credible intervals
- Discuss when Bayesian approaches add value (low data, policy constraints)
- Example: treasury desk wanting "probabilities" not point estimates

## 3. Term Structure Refresher (15 min)
- Components: level, slope, curvature
- Data sources (YC <GO>) and common issues
- Introduce macro linkages (GDP surprise, FOMC events)

## 4. Building the Model (25 min)
- PyMC walkthrough: priors for alpha, tenor offsets, macro betas
- Visual diagram of model graph
- Explain sampling parameters (chains, target_accept)

## 5. Break (10 min)

## 6. Posterior Analysis (20 min)
- ArviZ summary interpretation
- Posterior predictive checks & fan charts
- Translating statistics to risk narratives

## 7. Scenario Design (20 min)
- Define stress scenarios (e.g., stagflation, dovish pivot)
- Use scenario builder outputs to recommend treasury actions
- Discuss communication tips for exec audiences

## 8. Lab Briefing (15 min)
- Walk through `day3_bayesian_risk.ipynb`
- Emphasize data prep, sampling runtime expectations, saving charts
- Deliverable guidance: insert outputs into provided slide template

## 9. Wrap-Up (10 min)
- Collect questions on Bayesian interpretation
- Preview Day 4 capstone sprint and governance focus

### Slide Assets Needed
- Bayesian vs. classical comparison graphic
- Model diagram (plates showing priors, data)
- Example fan chart screenshot
- Scenario table template
