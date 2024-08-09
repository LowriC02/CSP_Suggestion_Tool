import streamlit as st
import pandas as pd

# Simulated data
questionnaire_data = pd.DataFrame({
    'Industry': ['Healthcare', 'Finance', 'Retail', 'Technology', 'Other'],
    'Location': ['North America', 'Europe', 'Asia', 'Other', 'Other'],
    'Current Cloud Usage': ['None', 'Partial (Hybrid)', 'Full Cloud Deployment', 'None', 'Partial (Hybrid)'],
    'Critical Assets': ['Data Storage', 'Applications', 'Databases', 'Development Tools', 'Other'],
    'Cost Sensitivity': ['High', 'Medium', 'Low', 'Medium', 'High'],
    'Risk Appetite': ['Low', 'Medium', 'High', 'Low', 'Medium'],
    'Recommended CSP': ['AWS', 'Azure', 'Google Cloud', 'IBM Cloud', 'Oracle Cloud']
})

# Title and Sidebar
st.title("Cloud Migration Recommendation Tool")
st.sidebar.title("Navigation")
st.sidebar.markdown("Select a section to begin.")

# User Input Section
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = {}

def get_user_input():
    st.header("Company and Migration Details")

    industry = st.selectbox("Select Industry", ["Healthcare", "Finance", "Retail", "Technology", "Other"])
    location = st.selectbox("Select Location", ["North America", "Europe", "Asia", "Other"])
    current_cloud_usage = st.selectbox("Current Cloud Usage", ["None", "Partial (Hybrid)", "Full Cloud Deployment"])
    critical_assets = st.multiselect("Select Critical Assets", ["Data Storage", "Applications", "Databases", "Development Tools", "Other"])

    st.session_state['user_input'] = {
        "industry": industry,
        "location": location,
        "current_cloud_usage": current_cloud_usage,
        "critical_assets": critical_assets,
    }

    st.success("Company and migration details saved!")

if st.sidebar.button("Enter Company Details"):
    get_user_input()

# User Preferences Section
if 'user_preferences' not in st.session_state:
    st.session_state['user_preferences'] = {}

def get_user_preferences():
    st.header("User Preferences")

    cost_attitude = st.selectbox(
        "What is your attitude toward cost?",
        ["Cost is a primary concern", "Cost is important but secondary to security", "Willing to pay more for the best service"]
    )

    risk_appetite = st.selectbox(
        "What is your risk appetite?",
        ["Low", "Medium", "High"]
    )

    st.session_state['user_preferences'] = {
        "cost_attitude": cost_attitude,
        "risk_appetite": risk_appetite,
    }

    st.success("User preferences saved!")

if st.sidebar.button("Enter User Preferences"):
    get_user_preferences()

# Risk Management and Compliance Recommendations
def get_risk_management_recommendations():
    st.header("Risk Management and Compliance Recommendations")

    industry = st.session_state['user_input'].get("industry")
    location = st.session_state['user_input'].get("location")
    
    if industry == "Healthcare" or location == "Europe":
        st.write("Given your industry/location, consider strict adherence to GDPR and HIPAA regulations.")
        st.write("Ensure that the selected CSP provides robust encryption and regular compliance audits.")

    if "Security" in st.session_state['evaluation_criteria'] and st.session_state['evaluation_criteria']["Security"]:
        st.write("Focus on CSPs that offer advanced security features like end-to-end encryption and multi-factor authentication.")

if st.sidebar.button("Get Risk Management Recommendations"):
    get_risk_management_recommendations()

# Final CSP Recommendation
def final_csp_recommendation():
    st.header("Final CSP Recommendation")
    
    cost_attitude = st.session_state['user_preferences'].get("cost_attitude")
    risk_appetite = st.session_state['user_preferences'].get("risk_appetite")
    
    # Filter the simulated questionnaire data based on user preferences
    filtered_data = questionnaire_data.copy()
    
    if cost_attitude == "Cost is a primary concern":
        filtered_data = filtered_data[filtered_data['Cost Sensitivity'] == 'High']
    elif cost_attitude == "Willing to pay more for the best service":
        filtered_data = filtered_data[filtered_data['Cost Sensitivity'] == 'Low']
    
    if risk_appetite == "Low":
        filtered_data = filtered_data[filtered_data['Risk Appetite'] == 'Low']
    elif risk_appetite == "High":
        filtered_data = filtered_data[filtered_data['Risk Appetite'] == 'High']
    
    # Display the filtered recommendation
    if not filtered_data.empty:
        recommended_csp = filtered_data.iloc[0]['Recommended CSP']
        st.write(f"Based on your preferences, we recommend: **{recommended_csp}**")
    else:
        st.write("No suitable CSP found based on the selected criteria. Consider adjusting your preferences.")

if st.sidebar.button("Get Final Recommendation"):
    final_csp_recommendation()
