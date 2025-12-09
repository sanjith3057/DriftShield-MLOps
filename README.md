# DriftShield – Self-Healing MLOps Pipeline with Data Drift Detection & Auto-Retrain

**Live Demo (Permanent):** https://driftshield-mlops-53bhffscprpqt2jgqmi5d9.streamlit.app/  
**GitHub:** https://github.com/sanjith3057/DriftShield-MLOps  
**Built in 1 day • December 2025 • Fresher → MLOps Ready**

## What Happens When Your Model Breaks in Production?

Most portfolios: “I trained a model. AUC 0.82. Done.”  
**This one:** “Watch my model detect drift → auto-retrain itself → recover live.”

### Live Demo Screenshots

**Real-time monitoring dashboard (Streamlit)**  
<img width="1918" height="988" alt="image" src="https://github.com/user-attachments/assets/7412af2a-ecbf-4f2d-8b93-a3aa66bce0a2" />


**Custom drift detection (KS + Chi-Square) – 7/9 features drifted!**  
![Drift Detection] (<img width="1268" height="875" alt="image" src="https://github.com/user-attachments/assets/52b46a7f-3b5d-4325-adfc-5f4530e634e2" />)


**Exploratory Data Analysis (IBM Telecom Churn)**  
![EDA Overview](<img width="1990" height="1432" alt="image" src="https://github.com/user-attachments/assets/a4ab3469-55a1-44cf-bf2c-959f6d11be3c" />
)

**Feature Correlation Heatmap – What actually drives churn?**  
![Correlation Matrix](<img width="1210" height="880" alt="image" src="https://github.com/user-attachments/assets/724db96a-3217-4395-8c28-8c900cc104e8" />
)

## How It Works (End-to-End)

1. Trains XGBoost churn model on clean data → logs in MLflow
2. Simulates real-world drift (recession, price hikes, forced bundles)
3. **Custom drift detector** (no Evidently) flags **0.308 overall drift**
4. When drift > 0.1 → **auto-retrain triggers**
5. New model trained on drifted data → promoted to v4 in MLflow
6. Live dashboard instantly shows recovery + balloons

Tech: Python • XGBoost • MLflow • Plotly • Streamlit • Google Colab

## Why Recruiters Stop Scrolling

- No hand-wavy theory  
- No Kaggle notebook  
- Full production pipeline that **fixes itself**  
- Deployed live in under 10 hours

Open to **Data Scientist / MLOps Engineer / ML Engineer** roles 2026  
Drop a comment or DM if you want this running in your stack

 by — Sanji3057e
