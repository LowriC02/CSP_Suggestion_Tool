import streamlit as st

# Fun and Engaging App Introduction
st.title("Welcome to the Cloud Adventure: Your CSP Suggestion Tool!")

st.markdown("""
Embark on your cloud migration journey with us! Whether you're scaling the peaks of performance or navigating the valleys of cost efficiency, 
this tool is your trusty guide. Let's chart the best course to your perfect Cloud Service Provider (CSP) based on your unique needs and challenges. 
Ready to get started? Let's go!
""")

# Questionnaire Section 1: Company Information
st.header("1. Tell Us About Your Company")

# Industry Type Input - Free text input
industry = st.text_input("First, what industry are you in?")

# Location Input - Predefined options (Global and Continents)
location = st.radio("Where does your company operate?", 
                    ["Global", "Africa", "Asia", "Europe", "North America", "South America", "Australia"])

# Display inputs
st.write("**Industry:**", industry)
st.write("**Location:**", location)
