# data_visualization.py
import matplotlib.pyplot as plt
import pandas as pd
import io

def generate_budget_summary_chart(user_profile):
    """
    Generates a bar chart showing income, expenses, and savings.
    """
    income = user_profile.get('income', 0)
    expenses = user_profile.get('expenses', 0)
    savings = user_profile.get('savings', 0)
    
    data = {'Category': ['Income', 'Expenses', 'Savings'],
            'Amount': [income, expenses, savings]}
    df = pd.DataFrame(data)

    fig, ax = plt.subplots()
    ax.bar(df['Category'], df['Amount'], color=['green', 'red', 'blue'])
    ax.set_title('Budget Summary')
    ax.set_ylabel('Amount ($)')
    
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    return buf