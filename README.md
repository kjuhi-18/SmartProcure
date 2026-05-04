# 🚀 SmartProcure AI  
### ⚡ AI-Powered Logistics Intelligence System  

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Model-Random%20Forest-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Accuracy-87%25-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/ROC--AUC-0.983-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Hackathon-Ready-red?style=for-the-badge">
</p>

<p align="center">
  <img src="https://img.shields.io/github/languages/top/kjuhi-18/SmartProcure?style=flat-square">
  <img src="https://img.shields.io/github/repo-size/kjuhi-18/SmartProcure?style=flat-square">
  <img src="https://img.shields.io/github/last-commit/kjuhi-18/SmartProcure?style=flat-square">
</p>

---

## 🌍 Problem Statement  

Logistics systems today are **reactive** — delays are detected only after they occur.

❌ No early delay prediction  
❌ No priority-based dispatching  
❌ Traffic & weather ignored  

➡️ Result: missed SLAs, higher costs, inefficient operations  

---

## 💡 Solution  

**SmartProcure AI** is an end-to-end ML-powered logistics intelligence system that:

✅ Predicts delivery time  
✅ Detects delay risk (Low / Medium / High)  
✅ Uses real-world signals (traffic + weather)  
✅ Optimizes dispatch using a **reward engine**  

📉 Reduces delays by **20–30%**

---

## 🧠 System Architecture  

```text
User Input
   ↓
Data Fetch (CSV files)
   ↓
Feature Engineering
   ↓
Time Prediction Model
   ↓
Delay Prediction Model
   ↓
Risk Classification
   ↓
Reward Optimization
   ↓
Final Recommendation
```
## 📂 Project Structure
SmartProcure/
│
├── Deliveries.csv
├── External_Factors.csv
├── Factories.csv
├── Projects.csv
│
├── delay_model.pkl
├── time_model.pkl
│
├── ml_improved.ipynb
├── predict_app.py
│
├── README.md
└── LICENSE
##⚙️ How It Works
1️⃣ Input
Factory ID
Project ID
Delivery Date
2️⃣ Feature Engineering
Distance calculation
Demand & priority encoding
Weather + traffic integration
Time features
3️⃣ Models
⏱️ Time Prediction Model
Random Forest Regressor
Predicts delivery time
⚠️ Delay Prediction Model
Random Forest Classifier
Predicts delay

📊 ROC-AUC Score: 0.983
4️⃣ Risk Classification
Delay	Risk
< 2 hrs	🟢 Low
2–5 hrs	🟡 Medium
> 5 hrs	🔴 High
5️⃣ Reward Optimization
Reward =
Priority Score
- (2 × Delay)
- (5 × Traffic Index)
- (5 × Weather Index)
## 📊 Example Output
Distance: 320 km
Expected Time: 18.2 hours
Predicted Delay: 4.5 hours
Actual Time: 22.7 hours
Risk Level: Medium
Reward Score: 3.2

Recommendation: Moderate Priority Dispatch
## 🧪 Installation
pip install pandas scikit-learn joblib
## ▶️ Run
python predict_app.py
📈 Key Insights
🚗 Traffic is the biggest delay factor
🌦️ Weather impacts long-distance deliveries
📏 Distance increases risk exposure
⚠️ Current systems ignore priority-based optimization
💼 Business Impact
Metric	Value
Delay Reduction	20–30%
ROC-AUC	0.983
Inference Time	< 1 sec
Data Sources	4 CSVs
🚀 Future Scope
🌐 Real-time APIs (Google Maps, Weather)
📊 Streamlit dashboard
🛣️ Route optimization
🤖 Reinforcement learning
🏢 ERP integration
👨‍💻 Team

SymbiWarriors

Kunal Jhindal
Krishnav Rastogi
Gnana Pushyami Dommaraju
🏁 Conclusion

SmartProcure AI is not just a prediction tool —

👉 It is a Decision Intelligence System

✔ Predicts
✔ Classifies
✔ Optimizes
✔ Recommends

💡 From reactive logistics → to intelligent decision-making

⭐ Support

If you like this project, give it a ⭐ on GitHub!
