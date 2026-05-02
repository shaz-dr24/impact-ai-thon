# AI-Driven Investment Decision Intelligence

Welcome to the **AI Investment MVP** (Minimum Viable Product). This project is a streamlined, AI-powered investment decision platform built using **Streamlit**, **scikit-learn**, and **yfinance**. It leverages historical market data to predict future stock prices, analyzes market volatility, evaluates risk concentration, recommends rebalancing actions, and explains its decisions in plain English.

## 🚀 Features

*   **Market Data Fetching:** Automatically retrieves up to 2 years of historical stock data via `yfinance`.
*   **AI Price Prediction:** Uses a `LinearRegression` model (`scikit-learn`) based on feature engineering (Moving Average 5, Moving Average 10, Momentum) to predict closing prices.
*   **Agent-Based Insights:** Modular agent architecture providing key analytics:
    *   **Market Agent:** Detects market volatility based on recent price movements.
    *   **Risk Agent:** Evaluates sector concentration risk for a given client portfolio.
    *   **Rebalance Agent:** Recommends portfolio rebalancing actions tailored to the client type.
    *   **Explain Agent:** Generates plain English explanations for the AI's confidence levels and market signals.
*   **Interactive Dashboard:** An intuitive UI built with **Streamlit** for seamless data visualization and interaction. Includes actual vs. predicted price graphs and accuracy comparisons.

## 📁 Project Structure

```text
impact-ai-thon-main/
│
├── app.py                  # Main Streamlit application
├── utils.py                # Utility functions for data fetching and ML modeling
├── requirements.txt        # Python dependencies
├── data/
│   └── portfolio.csv       # Sample client portfolio data (required)
└── agents/                 # Modular AI insights
    ├── explain_agent.py    # Generates plain English AI explanations
    ├── market_agent.py     # Volatility detection logic
    ├── rebalance_agent.py  # Portfolio rebalancing logic
    └── risk_agent.py       # Risk assessment logic
```

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/impact-ai-thon.git
   cd impact-ai-thon-main
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser:**
   The Streamlit app will automatically open in your default browser at `http://localhost:8501`.

## 📦 Dependencies

The application relies on the following major Python libraries:
*   `streamlit` - Web application framework
*   `pandas` - Data manipulation and analysis
*   `numpy` - Numerical computing
*   `yfinance` - Yahoo Finance market data downloader
*   `matplotlib` - Plotting and visualization
*   `scikit-learn` - Machine learning and predictive modeling

## 📊 How it Works

1.  **Select Client & Asset:** Choose a client and an asset (stock symbol) from the provided portfolio dataset.
2.  **Market Data & AI Prediction:** The app fetches the data, trains a Linear Regression model on 70% of the data, and tests it on the remaining 30%. It displays a graph comparing the actual vs. predicted prices.
3.  **Validation View:** A tabular breakdown of actual prices, AI predicted prices, and the error percentage.
4.  **AI Insights:** Key metrics regarding prediction accuracy, market signals (volatility), and rebalance recommendations are displayed. Alerts are triggered for low confidence or high risk.
5.  **Plain English Explanation:** The AI translates its prediction accuracy and market findings into an easy-to-understand summary.

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
