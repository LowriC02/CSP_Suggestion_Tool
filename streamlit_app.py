import streamlit as st

# Initialise session state for criteria if not already done
if 'evaluation_criteria' not in st.session_state:
    st.session_state['evaluation_criteria'] = {}

# Title and Sidebar with Navigation
st.set_page_config(page_title="Cloud Migration Tool", layout="wide", initial_sidebar_state="expanded")
st.title("Cloud Migration Recommendation Tool")
st.sidebar.title("Navigation")

# Navigation sections
sections = ["Company and Migration Details", "User Preferences", "Risk Management Recommendations", "Final CSP Recommendation"]
selected_section = st.sidebar.radio("Go to", sections)

# Company and Migration Details Section
if selected_section == "Company and Migration Details":
    st.header("Company and Migration Details")

    industry = st.selectbox("Select Industry", ["Healthcare", "Finance", "Retail", "Technology", "Other"], key="industry")
    location = st.selectbox("Select Location", ["North America", "Europe", "Asia", "Other"], key="location")
    current_cloud_usage = st.radio("Current Cloud Usage", ["None", "Partial (Hybrid)", "Full Cloud Deployment"], key="current_cloud_usage")
    critical_assets = st.multiselect("Select Critical Assets", ["Data Storage", "Applications", "Databases", "Development Tools", "Other"], key="critical_assets")

    # Save to session state
    st.session_state['user_input'] = {
        "industry": industry,
        "location": location,
        "current_cloud_usage": current_cloud_usage,
        "critical_assets": critical_assets,
    }

    st.success("Company and migration details saved!")

# User Preferences Section
if selected_section == "User Preferences":
    st.header("User Preferences")

    cost_attitude = st.radio(
        "What is your attitude towards cost?",
        ["Cost is a primary concern", "Cost is important but secondary to security", "Willing to pay more for the best service"],
        key="cost_attitude"
    )

    risk_appetite = st.radio(
        "What is your risk appetite?",
        ["Low", "Medium", "High"],
        key="risk_appetite"
    )

    # Save to session state
    st.session_state['user_preferences'] = {
        "cost_attitude": cost_attitude,
        "risk_appetite": risk_appetite,
    }

    st.success("User preferences saved!")

# Risk Management Recommendations Section
if selected_section == "Risk Management Recommendations":
    st.header("Risk Management and Compliance Recommendations")

    industry = st.session_state['user_input'].get("industry", "")
    location = st.session_state['user_input'].get("location", "")
    
    if industry == "Healthcare" or location == "Europe":
        st.write("**Compliance Notice**: Given your industry/location, consider strict adherence to GDPR and HIPAA regulations.")
        st.write("Ensure that the selected CSP provides robust encryption and regular compliance audits.")

    if st.checkbox("Focus on advanced security features"):
        st.session_state['evaluation_criteria']["Security"] = True
        st.write("We will prioritise CSPs offering advanced security features like end-to-end encryption and multi-factor authentication.")
    else:
        st.session_state['evaluation_criteria']["Security"] = False

# Final CSP Recommendation Section
if selected_section == "Final CSP Recommendation":
    st.header("Final CSP Recommendation")
    
    # Fetch all user inputs
    user_input = st.session_state.get('user_input', {})
    user_preferences = st.session_state.get('user_preferences', {})
    evaluation_criteria = st.session_state.get('evaluation_criteria', {})

    # Logic to determine CSP recommendation based on combined criteria
    recommended_csp = "AWS"  # Default recommendation
    
    if user_preferences['cost_attitude'] == "Willing to pay more for the best service" and evaluation_criteria.get("Security", False):
        recommended_csp = "Azure"
    elif user_input['industry'] == "Technology" and user_input['current_cloud_usage'] == "Full Cloud Deployment":
        recommended_csp = "Google Cloud"
    elif user_preferences['cost_attitude'] == "Cost is a primary concern" and user_preferences['risk_appetite'] == "Low":
        recommended_csp = "AWS"
    else:
        if evaluation_criteria.get("Security", False):
            recommended_csp = "Azure"
        else:
            recommended_csp = "AWS"  # Use AWS as a more general recommendation when no specific preferences are met.

    # Display the recommendation
    st.markdown(f"### Based on your preferences and company details, we recommend: **{recommended_csp}**")

# Add a "Back to top" button at the bottom
if st.button("Back to top"):
    st.experimental_rerun()

