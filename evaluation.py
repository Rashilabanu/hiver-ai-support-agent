import pandas as pd
from sklearn.metrics import accuracy_score

df = pd.read_csv("golden_evaluation_set.csv")

def baseline_predict(text):
    text = str(text).lower()

    if "refund" in text:
        return "refund"
    if "payment" in text or "charged" in text:
        return "payment_issue"
    if "login" in text or "password" in text:
        return "account_access"
    if "cancel" in text:
        return "cancellation"
    if "delivery" in text or "order" in text:
        return "order_delivery"

    return "other"

df["predicted_intent"] = df["text"].apply(baseline_predict)

accuracy = accuracy_score(df["intent"], df["predicted_intent"])

print("Intent Accuracy:", round(accuracy * 100, 2), "%")
