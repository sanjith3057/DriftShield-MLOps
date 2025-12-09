# DriftShield – Self-Healing MLOps Pipeline  
**Live Demo (Permanent):** https://driftshield-mlops-53bhffscprpqt2jgqmi5d9.streamlit.app/  
**GitHub:** https://github.com/sanjith3057/DriftShield-MLOps  
**Built in <24 hours • December 2025**

When production data drifts → my model doesn’t die.  
It detects → auto-retrains → promotes new version → recovers live.

### Live Demo Screenshots

**Real-time monitoring dashboard (auto-recovery in action)**  
![Live Dashboard](https://github.com/user-attachments/assets/7412af2a-ecbf-4f2d-8b93-a3aa66bce0a2)

**Custom drift detection (KS + Chi-Square) – 7/9 features drifted**  
![Drift Detection](https://github.com/user-attachments/assets/52b46a7f-3b5d-4325-adfc-5f4530e634e2)

**Exploratory Data Analysis (IBM Telecom Churn)**  
![EDA Overview](https://github.com/user-attachments/assets/a4ab3469-55a1-44cf-bf2c-959f6d11be3c)

**Feature Correlation Heatmap – What actually drives churn?**  
![Correlation Heatmap](https://github.com/user-attachments/assets/724db96a-3217-4395-8c28-8c900cc104e8)

### How It Works (End-to-End)
1. XGBoost model trained → registered in MLflow (v1)
2. Real-world drift injected (recession + price hikes)
3. Custom statistical drift detector flags **0.308 overall drift**
4. Drift > 0.1 → **auto-retrain triggers**
5. New model trained on drifted data → promoted to **v4**
6. Dashboard shows full recovery + balloons

### Tech Stack
Python • XGBoost • MLflow • Plotly • Streamlit • Custom KS/Chi² • Google Colab

### Why This Gets You Hired
- Full closed-loop MLOps (not just a notebook)
- Production-grade monitoring + self-healing
- Live, permanent deployment
- Built & shipped in one day

Fresher | December 2025 | Open to **Data Science / MLOps / ML Engineer** roles 2026  
DMs open — let’s talk

Made with love (and zero sleep) — Sanji3057e

---
⭐ Star if you want this kind of pipeline in production
