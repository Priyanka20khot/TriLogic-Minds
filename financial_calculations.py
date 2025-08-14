class FinancialAdvisor:
    def _init_(self):
        # Set a default tax rate (10%)
        self.tax_rate = 0.10

    def calculate_tax(self, income):
        return income * self.tax_rate

    def get_savings_recommendation(self, user_profile):
        savings = user_profile['savings']
        income = user_profile['income']
        if savings < income * 0.2:
            return "You should try to save at least 20% of your income."
        else:
            return "Great job! You're saving well."

    def get_investment_suggestion(self, user_profile):
        if user_profile['role'] == "student":
            return "Consider low-risk investments like index funds."
        else:
            return "You can diversify into stocks, bonds, and mutual funds."

    def get_spending_insights(self, user_profile):
        expenses = user_profile['expenses']
        income = user_profile['income']
        expense_ratio = expenses / income
        if expense_ratio > 0.8:
            return "Your expenses are high. Try reducing unnecessary spending."
        else:
            return "Your expenses are well-managed."