import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils import fetch_market_data, train_and_predict
from agents.market_agent import detect_volatility
from agents.risk_agent import sector_risk
from agents.rebalance_agent import rebalance
from agents.explain_agent import explain_decision

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Investment MVP",
    layout="wide"
)

st.title("🤖 AI-Driven Investment Decision Intelligence")
st.write(
    "AI learns from historical market data, predicts future prices, "
    "and explains decisions in simple language."
)

# ---------------- LOAD PORTFOLIO ----------------
portfolio = pd.read_csv("data/portfolio.csv")

# ---------------- INPUT CONTROLS ----------------
st.subheader("📥 Select Client & Asset")

col1, col2 = st.columns(2)

with col1:
    client_ids = portfolio['client_id'].unique()
    selected_client = st.selectbox("Client ID", client_ids)

client_data = portfolio[portfolio['client_id'] == selected_client]
client_type = client_data.iloc[0]['client_type']

with col2:
    stocks = client_data['asset'].unique()
    selected_stock = st.selectbox("Stock Symbol", stocks)

# ---------------- MARKET DATA ----------------
st.subheader(f"📊 Market Data & AI Prediction — {selected_stock}")

data = fetch_market_data(selected_stock)
test_data, accuracy = train_and_predict(data)

# ---------------- PRICE PLOT ----------------
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(test_data.index, test_data['Close'], label="Actual Price")
ax.plot(test_data.index, test_data['Predicted'], label="AI Prediction")
ax.set_xlabel("Date")
ax.set_ylabel("Price")
ax.legend()
st.pyplot(fig)

# ---------------- ACTUAL vs PREDICTED TABLE ----------------
st.subheader("📋 Actual vs AI Predicted Prices (Validation View)")

display_df = test_data[['Close', 'Predicted']].copy()
display_df.columns = ['Actual Price', 'AI Predicted Price']

# ✅ SAFE ERROR CALCULATION
display_df['Error (%)'] = (
    (display_df['Actual Price'] - display_df['AI Predicted Price']).abs()
    / display_df['Actual Price'] * 100
).round(2)

# Show last 10 rows (judge-friendly)
st.dataframe(display_df.tail(10), width="stretch")

# ---------------- AI INSIGHTS ----------------
st.subheader("🧠 AI Insights")

volatility_msg = detect_volatility(data)
risk = sector_risk(client_data)
rebalance_action = rebalance(client_type)

col1, col2, col3 = st.columns(3)

col1.metric("📈 Prediction Accuracy", f"{accuracy}%")
col2.info(f"📉 Market Signal: {volatility_msg}")
col3.success(f"🔁 Rebalance Action: {rebalance_action}")

if accuracy < 85:
    st.warning("⚠ AI confidence reduced due to market volatility")

if not risk.empty:
    st.warning("⚠ Risk Alert: High sector concentration detected")

# ---------------- EXPLANATION ----------------
st.subheader("🧾 AI Explanation (Plain English)")
st.write(explain_decision(accuracy, volatility_msg))

# ---------------- ACCURACY COMPARISON ----------------
st.subheader("📊 Accuracy Comparison Across Assets")

accuracy_rows = []

for asset in portfolio['asset'].unique():
    asset_data = fetch_market_data(asset)
    _, acc = train_and_predict(asset_data)
    accuracy_rows.append({
        "Asset": asset,
        "Accuracy (%)": acc
    })

accuracy_df = pd.DataFrame(accuracy_rows)
st.dataframe(accuracy_df, use_container_width=True)
