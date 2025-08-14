# financial_calculations.py
class FinancialAdvisor:
    """
    Provides financial calculations and personalized advice.
    """
    def _init_(self):
        # A placeholder for a more complex tax system.
        # For simplicity, we use a flat rate.
        self.tax_rate = 0.10

    def calculate_tax(self, income):
        """
        Calculates a flat 10% tax on the user's income.
        """
        return income * self.tax_rate

    def get_savings_recommendation(self, user_profile):
        """
        Provides a personalized savings recommendation.
        """
        income = user_profile.get('income', 0)
        expenses = user_profile.get('expenses', 0)
        user_type = user_profile.get('role', 'professional')

        if income <= 0:
            return "Please provide your income to get a savings recommendation."

        disposable_income = income - expenses
        
        if disposable_income <= 0:
            return "It seems your expenses are higher than your income. Let's look at your budget to find areas to optimize!"
        
        # 50/30/20 rule of thumb
        needs = income * 0.5
        wants = income * 0.3
        savings_goal = income * 0.2

        if user_type == "student":
            message = (
                f"As a student, it's great that you're thinking about savings! "
                f"A good rule of thumb is to save at least 10% of your income. "
                f"With your current income, a target of ${savings_goal*0.5:.2f} per month would be a great start!"
            )
        else: # Professional
            message = (
                f"Based on the 50/30/20 rule, a good savings goal for you would be ${savings_goal:.2f} per month. "
                f"This covers 20% of your income for savings and debt repayment. "
                f"It's a great way to ensure a secure financial future."
            )
            
        return message

    def get_investment_suggestion(self, user_profile):
        """
        Suggests investments based on user type and risk tolerance.
        """
        user_type = user_profile.get('role', 'professional')
        
        if user_type == "student":
            return (
                "As a student, it's wise to start with low-risk, high-growth options. "
                "Consider investing in a diversified S&P 500 index fund or a simple savings account with a high APY. "
                "The key is to start small and be consistent."
            )
        else: # Professional
            return (
                "As a professional, you might have a higher risk tolerance. "
                "Consider diversifying your portfolio with a mix of index funds, ETFs, and a few individual stocks. "
                "Don't forget to contribute to your retirement accounts like a 401(k) or IRA."
            )

    def get_spending_insights(self, user_profile):
        """
        Analyzes spending and provides actionable tips.
        """
        income = user_profile.get('income', 0)
        expenses = user_profile.get('expenses', 0)
        
        if income <= 0 or expenses <= 0:
            return "Please provide your income and expenses for a spending analysis."
        
        disposable_income = income - expenses
        
        if disposable_income < 0:
            return (
                "Your expenses exceed your income. Actionable tips: "
                "1. Track every expense for a month to identify leaks. "
                "2. Cut back on non-essential spending (e.g., dining out, subscriptions). "
                "3. Consider a side hustle to increase income."
            )
        elif disposable_income > income * 0.5:
            return (
                "Great job! You have a high savings rate. "
                "To optimize further, consider increasing your investments to make your money work for you."
            )
        else:
            return (
                "Your budget seems balanced. To improve, try automating your savings. "
                "Set up an automatic transfer from your checking to your savings account on payday. "
                "This 'pay yourself first' strategy is highly effective."
            )
