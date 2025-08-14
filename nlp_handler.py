class NLPHandler:
    def _init_(self):
        pass

    def classify_intent(self, text):
        text = text.lower()
        if "tax" in text:
            return "taxes"
        elif "save" in text or "savings" in text:
            return "savings"
        elif "invest" in text:
            return "investments"
        elif "budget" in text:
            return "budget"
        elif "expense" in text:
            return "expenses"
        elif any(greet in text for greet in ["hello", "hi", "hey"]):
            return "greetings"
        else:
            return "unknown"