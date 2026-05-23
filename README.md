# 📈 Retail Sales Forecasting — Predictive Analytics

A end-to-end predictive analytics project that forecasts future 
retail sales trends using historical data from the Sample Superstore dataset.

## 🎯 Objective
Build a predictive model to forecast monthly sales trends using 
regression techniques, with full data preprocessing, EDA, and visualization.

## 🗂️ Dataset
- **Source:** Sample - Superstore.csv
- **Features used:** Order Date, Sales, Category, Region
- **Target:** Monthly Sales Forecasting

## 🔧 Tech Stack
- Python 3.x
- Pandas, NumPy
- Scikit-learn (Linear Regression)
- Matplotlib, Seaborn
- Jupyter Notebook

## 📁 Project Structure
predictive-analytics/
├── data/
│   ├── raw/                  # Original dataset
│   └── processed/            # Cleaned data
├── notebooks/
│   ├── 01_eda.ipynb          # Exploratory Data Analysis
│   └── 02_model.ipynb        # Model Training & Forecasting
├── outputs/
│   └── plots/                # Saved visualizations
├── src/
│   ├── data_loader.py        # Data loading & preprocessing
│   ├── model.py              # Model training & evaluation
│   └── visualize.py          # Plotting functions
└── README.md

## ⚙️ How to Run
1. Clone the repository
   git clone https://github.com/your-username/predictive-analytics.git

2. Create virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install pandas numpy matplotlib seaborn scikit-learn statsmodels

4. Run notebooks in order
   - 01_eda.ipynb
   - 02_model.ipynb

## 📊 Results
| Metric | Value |
|--------|-------|
| Model  | Linear Regression |
| Target | Monthly Sales |
| Output | 6-Month Future Forecast |
| Evaluation | MAE, RMSE, R² Score |

## 📉 Key Visualizations
- Monthly Sales Trend (EDA)
- Actual vs Predicted Sales
- 6-Month Future Forecast

## 🙋 Author
Durga V
B.Tech Information Technology
Sri Krishna College of Engineering and Technology
