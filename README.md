# 💻 Laptop-Price-Estimator
## 📘 Overview
Laptop Price Estimator is a **machine learning project** developed in *December 2024*, aimed at **predicting the market price of laptops** based on its **technical specifications**. Built using a combination of regression models, preprocessing pipelines and a Streamlit-based front end, this project leverages ensemble learning and provides a seamless and interactive user experience. The system also includes real-time currency conversion (with configurable exchange rates) for localized pricing insights.

## 📌 Problem Statement
The laptop market is vast, with prices ranging dramatically based on hardware specifications, brand, and features. For consumers and retailers, **estimating a fair price for a configuration** can be complex and subjective.

**Goal:**
To build a machine learning model that can **accurately predict** the price of a laptop based on its specifications, and provide the result in a currency of the user’s choice through a user-friendly Streamlit interface.

## 💡 Features
- 🎯 Predicts laptop prices based on **13+ features** (RAM, brand, CPU, GPU, screen resolution, etc.)
- 💱 Allows **real-time price conversion** to INR, USD, GBP, JPY (hardcoded for simplicity)
- 📈 Built using **advanced ML models** (XGBoost, Ridge, etc.)
- ⚡ Fast and interactive **Streamlit app interface**
- 🧼 Clean, production-ready code and **model serialization** (.pkl)

## 🧠 Machine Learning Pipeline

```
Raw Data → Feature Engineering → ColumnTransformer (Standardization + Encoding) → Model (Voting Regressor) → Prediction → Streamlit Deployment (Interactive Web Interface)
```

## 📊 Model Performance
- **Mean Squared Error (MSE)**: 81,236.243
- **R² Score**: 0.839

These metrics demonstrate the model’s strong predictive accuracy in estimating laptop prices.

## ⚙️ Getting Started

This project requires Python and some common data science libraries. Setup is straightforward with a requirements.txt to install all dependencies.

### ✅ Requirements

- **Python 3.8+**
- Libraries listed in **requirements.txt**

[->install python](https://www.python.org/downloads/)

### 🚀 Running the System

```bash
# Clone the repository
git clone https://github.com/KDitsa/Laptop-Price-Estimator.git
cd Laptop-Price-Estimator

# (Optional) Create and activate a virtual environment
python -m venv <your_environment_name>
<your_environment_name>\Scripts\activate # For Windows

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

Once running, the app will open in your browser at http://localhost:8501, where you can input your data and get price predictions instantly.

## 🛠️ Implementation Journey

### 1. 🔧 Data Preparation & Feature Engineering
- **Extracted CPU brand and clock speed** from a single text field into two distinct features.
- **Visualized GPU brands** and grouped rare entries into broader categories for generalization.
- **Split memory info** into separate fields: `HDD`, `SSD`, and `Flash_Storage`.
- **Computed PPI** (Pixels Per Inch) using screen resolution and screen size.
- Cleaned and converted `RAM` and `Weight` columns into **numerical format** by removing units (e.g., `"8GB" → 8`).
- Converted **binary flags** like `Touchscreen` and `IPS` into 0/1 format for model consumption.

---

### 2. ⚙️ Preprocessing Pipeline:
Designed a robust pipeline using `ColumnTransformer` and `Pipeline` from scikit-learn to:
- **Standardize numerical features** (e.g., PPI, Weight, RAM).
- **One-hot encode categorical variables** (e.g., Company, CPU brand, GPU, OS).
- Ensure consistent data flow for all models

---

### 3. 🤖 Model Selection & Tuning:
- Trained and compared multiple regression models: Ridge, Lasso, SVR, Random Forest, Gradient Boosting, XGBoost.
- Applied **Bayesian Optimization** for hyperparameter tuning using `BayesSearchCV`.
- All models are combined using a **Voting Regressor**, which aggregates predictions to reduce variance and improve robustness.
- This ensemble approach outperformed individual models and was adopted as the final prediction model.

---

### 4. 🌐 Streamlit App Development:
Built and deployed an intuitive web interface using **Streamlit**, allowing users to:
- Input laptop specifications
- Get real-time price predictions
- Convert prices across currencies (offline converter used for stability)

---

## ⚠️ Challenges Faced & Resolutions

Throughout the development of the Laptop Price Estimator, several technical and data-related challenges were encountered. Below is a summary of key issues and how they were addressed:

| 🔍 **Challenge** | ✅ **Resolution** |
|------------------|------------------|
| **1. Feature engineering required deep inspection** — Derived features like PPI, binary conversions (Touchscreen, IPS), and weight cleanup were not immediately obvious. | Carefully engineered features with domain logic (e.g., calculating PPI from resolution, converting weights to floats), significantly boosting model accuracy. |
| **2. Model failed without pipeline and standardization** — Error like `'Microsoft' is a string, failed to convert to float` occurred during training. | Built a full preprocessing pipeline using `ColumnTransformer` to handle categorical encoding and numerical scaling before feeding into models. |
| **3. Inconsistent preprocessing across models** — Initially, models applied preprocessing inconsistently, causing unstable results. | Standardized all preprocessing steps into a unified `Pipeline`, ensuring every model received identical transformed input. |
| **4. Dataset is not recent** — Prices reflect pre-2024 market and do not account for recent hardware trends or inflation. | ❌ Not resolved. A more recent dataset would be needed to capture post-2024 price hikes and newer laptop configurations. |
| **5. Mixed data types in DataFrame** caused **Arrow serialization warnings** in Streamlit UI. | Applied type casting (e.g., converting all display fields to string) to ensure compatibility with Streamlit’s DataFrame display engine. |

## 📝 Closing Thoughts
This project demonstrates how effective preprocessing, feature engineering, and ensemble modeling can deliver accurate laptop price predictions. Deploying with Streamlit made the model accessible and interactive. Despite some challenges, the solution is robust and practical, with room for future improvements like updated data and dynamic currency conversion.
