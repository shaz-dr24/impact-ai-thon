def explain_decision(accuracy, volatility_msg):
    return f"""
The AI learned from past market data and predicted future prices.
Prediction accuracy was {accuracy:.2f}%.
{volatility_msg}.
This helps portfolio managers make safer decisions.
"""
