import pandas as pd

DATA_PATH = "/kaggle/input/datasets/thoughtvector/customer-support-on-twitter/twcs/twcs.csv"

df = pd.read_csv(DATA_PATH)

def classify_intent(text):
    text = str(text).lower()

    if any(w in text for w in ["refund", "money back"]):
        return "refund"
    if any(w in text for w in ["payment", "charged", "billing"]):
        return "payment_issue"
    if any(w in text for w in ["login", "password", "sign in"]):
        return "account_access"
    if any(w in text for w in ["cancel", "cancellation"]):
        return "cancellation"
    if any(w in text for w in ["delivery", "shipping", "order"]):
        return "order_delivery"

    return "other"

def support_agent(message):
    intent = classify_intent(message)

    replies = {
        "refund": "Sorry for the inconvenience. We can help with your refund request.",
        "payment_issue": "Sorry about the payment issue. Please share the relevant details so we can check it.",
        "account_access": "Sorry you're having trouble accessing your account. Please try the account recovery option.",
        "cancellation": "We can help with your cancellation request. Please share your order details.",
        "order_delivery": "Sorry about the delivery issue. Please share your order details so we can check the status.",
        "other": "Sorry for the inconvenience. Our support team will look into this."
    }

    decision = "ESCALATE" if intent == "other" else "AUTO-HANDLE"

    return {
        "intent": intent,
        "reply": replies[intent],
        "decision": decision
    }

if __name__ == "__main__":
    message = input("Customer message: ")
    print(support_agent(message))
