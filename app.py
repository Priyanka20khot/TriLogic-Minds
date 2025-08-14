# app.py
import streamlit as st
from nlp_handler import NLPHandler
from financial_calculations import FinancialAdvisor
from data_visualization import generate_budget_summary_chart

# --- THIS IS THE CORRECTED SECTION ---
# Use st.session_state to cache expensive objects like the NLP pipeline.
# This ensures they are created only once per user session.
if 'nlp_handler' not in st.session_state:
    st.session_state.nlp_handler = NLPHandler()

if 'financial_advisor' not in st.session_state:
    st.session_state.financial_advisor = FinancialAdvisor()

# We now access the objects through st.session_state
nlp_handler = st.session_state.nlp_handler
financial_advisor = st.session_state.financial_advisor
# --------------------------------

# In-memory dictionary to act as a user database
if "user_db" not in st.session_state:
    st.session_state.user_db = {}
    
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    
if "current_user" not in st.session_state:
    st.session_state.current_user = None

# --- User Authentication and Profile Management ---
def login_form():
    st.title("Personal Finance Chatbot")
    st.subheader("Login or Create Profile")
    
    with st.form("login_form"):
        user_name = st.text_input("Name")
        user_role = st.selectbox("Role", ["student", "professional"])
        income = st.number_input("Monthly Income ($)", min_value=0.0, step=100.0)
        expenses = st.number_input("Monthly Expenses ($)", min_value=0.0, step=100.0)
        
        submitted = st.form_submit_button("Start Chatting")
        
        if submitted and user_name:
            st.session_state.user_db[user_name] = {
                'name': user_name,
                'role': user_role,
                'income': income,
                'expenses': expenses,
                'savings': income - expenses
            }
            st.session_state.logged_in = True
            st.session_state.current_user = user_name
            st.rerun()

# --- Chatbot Interaction Logic ---
def chatbot_interface():
    st.sidebar.title("User Profile")
    user_profile = st.session_state.user_db[st.session_state.current_user]
    st.sidebar.write(f"*Name:* {user_profile['name']}")
    st.sidebar.write(f"*Role:* {user_profile['role'].capitalize()}")
    st.sidebar.write(f"*Monthly Income:* ${user_profile['income']:.2f}")
    st.sidebar.write(f"*Monthly Expenses:* ${user_profile['expenses']:.2f}")
    st.sidebar.write(f"*Current Savings:* ${user_profile['savings']:.2f}")

    st.title(f"Hello, {user_profile['name']}!")
    st.markdown("I'm your personal finance chatbot. How can I help you today?")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Ask me about savings, taxes, or investments..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                intent = nlp_handler.classify_intent(prompt)
                
                response = ""
                
                if intent == "taxes":
                    tax_amount = financial_advisor.calculate_tax(user_profile['income'])
                    response = f"Based on a flat 10% rate, your estimated monthly tax is ${tax_amount:.2f}."
                
                elif intent == "savings":
                    response = financial_advisor.get_savings_recommendation(user_profile)
                    
                elif intent == "investments":
                    response = financial_advisor.get_investment_suggestion(user_profile)

                elif intent == "budget":
                    st.markdown("Here is a summary of your budget:")
                    st.image(generate_budget_summary_chart(user_profile), use_column_width=True)
                    response = financial_advisor.get_spending_insights(user_profile)
                    
                elif intent == "expenses":
                    response = financial_advisor.get_spending_insights(user_profile)
                
                elif intent == "greetings":
                    response = "Hello! I'm here to help with your personal finances. Ask me about your budget, savings, taxes, or investments."
                
                else:
                    response = (
                        "I'm sorry, I'm not sure how to respond to that. "
                        "I can provide guidance on savings, taxes, investments, and your budget."
                    )
            
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# --- Main App Logic ---
if not st.session_state.logged_in:
    login_form()
else:
    chatbot_interface()