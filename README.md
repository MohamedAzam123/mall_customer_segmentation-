# Customer Segmentation & Clustering Web App 🛒

This project is an end-to-end Machine Learning application that segments mall customers into different groups based on their demographics and spending patterns. It includes the entire pipeline from data analysis to a live web application.

## 🚀 Live Demo
[https://fehfwcn4vgwxd7x7xdxsfr.streamlit.app/]

## 📊 Project Overview
The goal of this project is to help a retail store understand its customers better to design targeted marketing strategies. We used the **K-Means Clustering** algorithm to group customers based on:
* Age
* Annual Income (k$)
* Spending Score (1-100)

## 🛠️ Tech Stack
* **Language:** Python
* **Data Analysis:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (K-Means, StandardScaler)
* **Deployment:** Streamlit
* **Model Serialization:** Pickle

## 📈 Methodology
1. **Exploratory Data Analysis (EDA):** Analyzed customer distributions and relationships.
2. **Finding Optimal Clusters:** * Applied the **Elbow Method** to identify the best number of clusters (K=5).
   * Validated using **Silhouette Score** (~0.35) to ensure cluster cohesion.
3. **Preprocessing:** Used `StandardScaler` to normalize features for distance-based clustering.
4. **Deployment:** Created a user-friendly interface using Streamlit where users can input customer data and get instant classification.

## 📁 File Structure
* `mall_customers.ipynb`: Detailed analysis and model training.
* `cluster_web.py`: Streamlit application code.
* `cluster.sav`: The trained K-Means model.
* `scaler.sav`: Saved scaler for data normalization.
* `requirements.txt`: List of dependencies to run the project.

## 💻 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name
