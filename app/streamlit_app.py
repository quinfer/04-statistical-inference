from datetime import datetime
from pathlib import Path
from typing import Dict

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

DATA_ROOT = Path("/content/data") if Path("/content").exists() else Path(__file__).resolve().parents[1] / "data" / "bloomberg"
DATA_ROOT.mkdir(parents=True, exist_ok=True)

ESG_FALLBACK = pd.DataFrame({
    "ticker": [f"Issuer{i:02d}" for i in range(8)],
    "env_disclosure_score": np.linspace(55, 90, 8),
    "soc_disclosure_score": np.linspace(50, 85, 8),
    "gov_disclosure_score": np.linspace(52, 88, 8),
    "country": ["US", "UK", "FR", "DE", "US", "BR", "SG", "ZA"],
})

YIELD_FALLBACK = pd.DataFrame({
    "ticker": np.repeat(ESG_FALLBACK["ticker"], 3),
    "tenor": np.tile(["3M", "6M", "1Y"], len(ESG_FALLBACK)),
    "yield": np.random.default_rng(0).normal(2.7, 0.35, len(ESG_FALLBACK) * 3)
})

POLICY = {
    "min_esg_score": 60,
    "max_country_weight": 0.4,
    "max_single_issuer_weight": 0.2,
}


@st.cache_data
def load_csv_or_fallback(path: Path, fallback: pd.DataFrame) -> pd.DataFrame:
    if path.exists():
        df = pd.read_csv(path)
        st.sidebar.success(f"Loaded {path.name}")
        return df
    st.sidebar.warning(f"{path.name} missing. Using fallback dataset.")
    return fallback.copy()


def summarize_inputs(esg: pd.DataFrame, yields: pd.DataFrame) -> pd.DataFrame:
    pivot = yields.pivot_table(index="ticker", values="yield", aggfunc="mean")
    merged = esg.merge(pivot, on="ticker", how="left")
    merged.rename(columns={"yield": "avg_yield"}, inplace=True)
    return merged.dropna(subset=["avg_yield"])


def allocate_portfolio(df: pd.DataFrame, policy: Dict[str, float], total_weight: float = 1.0) -> pd.DataFrame:
    eligible = df[(df[["env_disclosure_score", "soc_disclosure_score", "gov_disclosure_score"]].min(axis=1) >= policy["min_esg_score"])]
    eligible = eligible.sort_values("avg_yield", ascending=False)
    country_usage: Dict[str, float] = {}
    weights = []
    remaining = total_weight
    for _, row in eligible.iterrows():
        if remaining <= 0:
            break
        country = row["country"]
        country_cap = policy["max_country_weight"]
        issuer_cap = policy["max_single_issuer_weight"]
        available = min(issuer_cap, country_cap - country_usage.get(country, 0.0), remaining)
        if available <= 0:
            weights.append(0.0)
            continue
        weights.append(available)
        country_usage[country] = country_usage.get(country, 0.0) + available
        remaining -= available
    eligible = eligible.iloc[: len(weights)].copy()
    eligible["weight"] = weights
    return eligible[eligible["weight"] > 0]


def build_model(data: pd.DataFrame) -> Pipeline:
    pipe = Pipeline([
        ("scale", StandardScaler()),
        ("rf", RandomForestRegressor(n_estimators=400, random_state=42)),
    ])
    pipe.fit(data[["env_disclosure_score", "soc_disclosure_score", "gov_disclosure_score"]], data["avg_yield"])
    return pipe


def feature_contributions(model: Pipeline) -> pd.Series:
    rf = model.named_steps["rf"]
    return pd.Series(rf.feature_importances_, index=["Env", "Soc", "Gov"])


def main():
    st.title("ESG-Aware Treasury Advisor")
    st.caption("Mini-MBA Capstone — Responsible Fintech Analytics")

    esg = load_csv_or_fallback(DATA_ROOT / "esg_scores_SAMPLE.csv", ESG_FALLBACK)
    yields = load_csv_or_fallback(DATA_ROOT / "yield_curve_SAMPLE.csv", YIELD_FALLBACK)
    inputs = summarize_inputs(esg, yields)
    model = build_model(inputs)

    st.sidebar.header("Policy Controls")
    POLICY["min_esg_score"] = st.sidebar.slider("Min ESG score", 40, 90, POLICY["min_esg_score"])
    POLICY["max_country_weight"] = st.sidebar.slider("Max country weight", 0.1, 0.8, POLICY["max_country_weight"], 0.05)
    POLICY["max_single_issuer_weight"] = st.sidebar.slider("Max issuer weight", 0.05, 0.5, POLICY["max_single_issuer_weight"], 0.05)

    portfolio = allocate_portfolio(inputs, POLICY)
    st.subheader("Recommended allocation")
    if portfolio.empty:
        st.warning("No issuers satisfy the ESG policy. Relax constraints or refresh data.")
    else:
        st.dataframe(portfolio[["ticker", "country", "avg_yield", "weight"]])
        fig = px.bar(portfolio, x="ticker", y="weight", color="country", title="Weights by issuer")
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Explainability")
    contrib = feature_contributions(model)
    st.bar_chart(contrib)

    st.subheader("What-if analysis")
    env = st.slider("Env disclosure", 40, 95, 75)
    soc = st.slider("Soc disclosure", 40, 95, 70)
    gov = st.slider("Gov disclosure", 40, 95, 73)
    pred = model.predict([[env, soc, gov]])[0]
    st.metric(label="Predicted compliant yield", value=f"{pred:.2f}%")

    notebook_hint = {
        "timestamp": datetime.utcnow().isoformat(),
        "policy": POLICY,
        "portfolio_size": int(portfolio.shape[0]),
    }
    st.json(notebook_hint)


if __name__ == "__main__":
    main()
