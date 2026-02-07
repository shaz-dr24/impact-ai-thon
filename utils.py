import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_percentage_error
import numpy as np

# ---------------- FETCH MARKET DATA ----------------
def fetch_market_data(symbol, period="2y"):
    data = yf.download(symbol, period=period, progress=False)

    if data.empty:
        return pd.DataFrame()

    close_prices = data['Close']
    if isinstance(close_prices, pd.DataFrame):
        close_prices = close_prices.iloc[:, 0]

    df = pd.DataFrame({'Close': close_prices}).dropna()

    # Feature engineering
    df['MA5'] = df['Close'].rolling(5).mean()
    df['MA10'] = df['Close'].rolling(10).mean()
    df['Momentum'] = df['Close'] - df['Close'].shift(5)

    df.dropna(inplace=True)
    return df


# ---------------- TRAIN & PREDICT ----------------
def train_and_predict(data):
    if data is None or len(data) < 20:
        return data, 0

    data = data.copy()
    data['Day'] = range(len(data))

    features = ['Day', 'MA5', 'MA10', 'Momentum']
    target = 'Close'

    split = int(len(data) * 0.7)

    if split < 5:
        return data, 0

    train = data.iloc[:split]
    test = data.iloc[split:].copy()

    if len(test) == 0:
        return data, 0

    model = LinearRegression()
    model.fit(train[features], train[target])

    test['Predicted'] = model.predict(test[features])

    # Avoid zero division
    test = test[test[target] > 0]

    if len(test) == 0:
        return data, 0

    accuracy = 100 - mean_absolute_percentage_error(
        test[target], test['Predicted']
    ) * 100

    accuracy = max(0, min(accuracy, 100))  # clamp

    return test, round(accuracy, 2)
