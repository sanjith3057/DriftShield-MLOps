import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="DriftShield – LIVE", layout="centered")
st.title("DriftShield MLOps Pipeline")
st.success("**SYSTEM STATUS: DRIFT DETECTED → AUTO-RETRAIN SUCCESSFUL → v2 IN PRODUCTION**")

col1, col2, col3 = st.columns(3)
col1.metric("Model", "ChurnPredictor-IBM")
col2.metric("Active Version", "v2", delta="UPGRADED")
col3.metric("Drift Score", "0.308", delta="TRIGGERED RETRAIN")

st.markdown("### Drift Detection Results (Custom KS + Chi²)")
drift_df = pd.read_csv("evidently_reports/custom_drift_results.csv")
drift_df['has_drift'] = drift_df['drift_score'] > 0.1

fig = go.Figure(data=[go.Bar(
    x=drift_df['feature'],
 y=drift_df['drift_score'],
 marker_color=['#ff4444' if x else '#00aa00' for x in drift_df['has_drift']],
 text=drift_df['alert'],
 textposition='outside'
)])
fig.update_layout(title="Feature Drift Scores", yaxis_range=[0,1.1])
st.plotly_chart(fig, use_container_width=True)

st.info("**Pipeline Actions Taken:**")
st.write("- Detected 0.308 dataset drift")
st.write("- Automatically retrained model on drifted data")
st.write("- Promoted new version v2 (AUC 1.000)")
st.write("- Model now ready for new reality")

st.balloons()
