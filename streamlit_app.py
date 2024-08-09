import streamlit as st

# App Introduction
st.title("Cloud Migration CSP Suggestion Tool")
st.markdown("""
Welcome to the Cloud Migration CSP Suggestion Tool. This tool is designed to assist companies in evaluating 
and selecting the most suitable Cloud Service Provider (CSP) based on a variety of factors including 
industry requirements, geographical location, and specific cloud migration challenges.

Please provide the following information to get started:
""")

# Questionnaire Section 1: Industry and Location
st.header("1. Company Information")

# Industry Type Input
industry = st.selectbox("What type of industry does your company operate in?", 
                        ["Healthcare", "Finance", "Retail", "Manufacturing", "Technology", "Other"])

# Location Input
location = st.text_input("Where is your company primarily located? (e.g., City, Country)")

# Display inputs
st.write("**Industry:**", industry)
st.write("**Location:**", location)
