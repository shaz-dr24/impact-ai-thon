def detect_volatility(data):
    # Always force Close to Series
    close_prices = data['Close']
    if hasattr(close_prices, "iloc"):
        close_prices = close_prices.squeeze()

    returns = close_prices.pct_change().dropna()

    # 🔒 Force scalar float
    volatility = float(returns.std() * 100)

    if volatility > 2:
        return "High volatility detected — AI confidence reduced"
    else:
        return "Market volatility within normal range"
