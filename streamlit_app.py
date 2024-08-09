import streamlit as st

# Engaging App Introduction
st.title("Welcome to the Cloud Adventure: Your CSP Suggestion Tool!")

st.markdown("""
🌴 **Welcome Adventurer!** Embark on your cloud migration journey with us. Whether you're optimising performance, balancing costs, 
or ensuring top-notch security, this tool is your trusted companion. Let’s help you navigate the cloud landscape 
and find the perfect Cloud Service Provider (CSP) tailored to your needs. Ready to get started? Let's dive in! 🏝️
""")

# Industry Type Input - Multiple Choice
st.subheader("What industries does your company operate in?")
industries = []
if st.checkbox("Healthcare", key="industry_healthcare"):
    industries.append("Healthcare")
if st.checkbox("Finance", key="industry_finance"):
    industries.append("Finance")
if st.checkbox("Retail", key="industry_retail"):
    industries.append("Retail")
if st.checkbox("Manufacturing", key="industry_manufacturing"):
    industries.append("Manufacturing")
if st.checkbox("Technology", key="industry_technology"):
    industries.append("Technology")
if st.checkbox("Other", key="industry_other"):
    industries.append("Other")

# Location Input - Multiple Choice
st.subheader("Where does your company operate?")
locations = []
if st.checkbox("Global", key="location_global"):
    locations.append("Global")
if st.checkbox("Africa", key="location_africa"):
    locations.append("Africa")
if st.checkbox("Asia", key="location_asia"):
    locations.append("Asia")
if st.checkbox("Europe", key="location_europe"):
    locations.append("Europe")
if st.checkbox("North America", key="location_north_america"):
    locations.append("North America")
if st.checkbox("South America", key="location_south_america"):
    locations.append("South America")
if st.checkbox("Australia", key="location_australia"):
    locations.append("Australia")

# Displaying the selected choices
st.markdown("### Selected Industries:")
st.write(', '.join(industries) if industries else "No industries selected.")

st.markdown("### Selected Locations:")
st.write(', '.join(locations) if locations else "No locations selected.")




# Continuing the adventure with a new section
st.header("⛅️ Mapping Your Cloud Terrain")
st.markdown("""
Time to map out where your company currently stands in its cloud journey. This will help us understand your starting point.
""")

# Current Cloud Situation
st.subheader("2. What's Your Current Cloud Situation?")
cloud_situation = st.radio(
    "How would you describe your company’s current use of cloud services?",
    [
        "We’re fully on the cloud and loving it!",
        "We’re dabbling with a hybrid approach.",
        "We haven’t touched the cloud yet."
    ]
)

# Risk Appetite
st.subheader("3. What’s Your Appetite for Risk?")
risk_appetite = st.radio(
    "When it comes to embracing risk, how does your company generally approach it?",
    [
        "We're bold risk-takers, always ready to innovate.",
        "We prefer a balanced approach, weighing risks carefully.",
        "We’re risk-averse, focusing on stability and security."
    ]
)

# Attitude to Cost
st.subheader("4. How Do You View Costs in Cloud Migration?")
cost_attitude = st.radio(
    "When it comes to cost, what's your company’s attitude towards spending on cloud migration?",
    [
        "We’re willing to invest heavily for the best outcomes.",
        "We aim to balance cost and quality—value is key.",
        "We’re focused on minimising costs wherever possible."
    ]
)

# Summary of Selections
st.markdown("### 🌟 Here's a quick look at your preferences:")
st.write(f"**Cloud Situation:** {cloud_situation}")
st.write(f"**Risk Appetite:** {risk_appetite}")
st.write(f"**Cost Attitude:** {cost_attitude}")



# Introducing the next section
st.header("🏔️ Scaling the Cloud Peaks")

st.markdown("""
As we climb higher, let's identify the key assets and priorities that will guide us to the summit of your cloud strategy.
""")

# Type of Assets - Checkboxes for multiple selections
assets = []
st.subheader("5. What Types of Assets Do You Have on the Cloud?")
if st.checkbox("Data Storage", key="asset_datastorage"):
    assets.append("Data Storage")
if st.checkbox("Applications", key="asset_applications"):
    assets.append("Applications")
if st.checkbox("Databases", key="asset_databases"):
    assets.append("Databases")
if st.checkbox("Development Tools", key="asset_devtools"):
    assets.append("Development Tools")
if st.checkbox("Other", key="asset_other"):
    assets.append("Other")

# Priorities in Selecting a CSP - Checkboxes for multiple selections
priorities = []
st.subheader("6. What Are Your Top Priorities When Selecting a CSP?")
if st.checkbox("Performance", key="priority_performance"):
    priorities.append("Performance")
if st.checkbox("Compliance", key="priority_compliance"):
    priorities.append("Compliance")
if st.checkbox("Support", key="priority_support"):
    priorities.append("Support")
if st.checkbox("Scalability", key="priority_scalability"):
    priorities.append("Scalability")
if st.checkbox("Cost Efficiency", key="priority_cost_efficiency"):
    priorities.append("Cost Efficiency")
if st.checkbox("Security", key="priority_security"):
    priorities.append("Security")
if st.checkbox("Innovation", key="priority_innovation"):
    priorities.append("Innovation")
if st.checkbox("Other", key="priority_other"):
    priorities.append("Other")

# Summary of Selections
st.markdown("### 🌟 Here's a summary of your input:")
st.write(f"**Assets on the Cloud:** {', '.join(assets) if assets else 'No assets selected.'}")
st.write(f"**Top Priorities in CSP Selection:** {', '.join(priorities) if priorities else 'No priorities selected.'}")



# Introducing the next section
st.header("🔐 Navigating the Security Jungle")
st.markdown("""
You're deep into the cloud adventure now, where security is key to surviving the wilds of the digital jungle. 
Let’s uncover your company’s security preferences and map out the features you’re hunting for in a Cloud Service Provider (CSP).
""")

# Security Preferences - Checkboxes for multiple selections
security_preferences = []
st.subheader("7. What Security Measures Are Most Important to You?")
if st.checkbox("Advanced Encryption", key="security_encryption"):
    security_preferences.append("Advanced Encryption")
if st.checkbox("Multi-Factor Authentication (MFA)", key="security_mfa"):
    security_preferences.append("Multi-Factor Authentication (MFA)")
if st.checkbox("Regular Security Audits", key="security_audits"):
    security_preferences.append("Regular Security Audits")
if st.checkbox("Data Loss Prevention (DLP)", key="security_dlp"):
    security_preferences.append("Data Loss Prevention (DLP)")
if st.checkbox("Intrusion Detection and Prevention", key="security_intrusion"):
    security_preferences.append("Intrusion Detection and Prevention")
if st.checkbox("Compliance with Industry Standards (e.g., GDPR, ISO 27001)", key="security_compliance"):
    security_preferences.append("Compliance with Industry Standards (e.g., GDPR, ISO 27001)")

# Desired Features in a CSP - Checkboxes for multiple selections
desired_features = []
st.subheader("8. What Features Are You Looking For in a CSP?")
if st.checkbox("High Availability and Uptime Guarantees", key="features_availability"):
    desired_features.append("High Availability and Uptime Guarantees")
if st.checkbox("24/7 Customer Support", key="features_support"):
    desired_features.append("24/7 Customer Support")
if st.checkbox("Scalable Infrastructure", key="features_scalability"):
    desired_features.append("Scalable Infrastructure")
if st.checkbox("Cost Management Tools", key="features_cost_management"):
    desired_features.append("Cost Management Tools")
if st.checkbox("AI and Machine Learning Capabilities", key="features_ai_ml"):
    desired_features.append("AI and Machine Learning Capabilities")
if st.checkbox("Integration with Existing Systems", key="features_integration"):
    desired_features.append("Integration with Existing Systems")
if st.checkbox("Other", key="features_other"):
    desired_features.append("Other")

# Summary of Selections
st.markdown("### 🌟 Here's a summary of your security preferences and feature wishlist:")
st.write(f"**Security Measures:** {', '.join(security_preferences) if security_preferences else 'No security measures selected.'}")
st.write(f"**Desired CSP Features:** {', '.join(desired_features) if desired_features else 'No features selected.'}")

# 🏝️ Wrapping Up Your Tropical Cloud Adventure
st.header("🏝️ Wrapping Up Your Tropical Cloud Adventure")

st.markdown("""
The path ahead is clear, but before you set off on your tropical cloud migration journey, let's ensure everything is in place. 
Review your selections and make sure you have all the tools and companions you need for a successful expedition through the cloud forests.
""")

# Final Review of Selections
st.subheader("9. Reviewing Your Selections")
st.markdown("### 🛠️ Tools & Resources")
st.write(f"**Key Assets on the Cloud:** {', '.join(assets) if assets else 'No assets selected.'}")

st.markdown("### 🛡️ Security Measures")
st.write(f"**Security Preferences:** {', '.join(security_preferences) if security_preferences else 'No security preferences selected.'}")

st.markdown("### 📦 Desired Features")
st.write(f"**CSP Features:** {', '.join(desired_features) if desired_features else 'No features selected.'}")

st.markdown("### 🌩️ Cloud Companions")
st.write(f"**Top Priorities in CSP Selection:** {', '.join(priorities) if priorities else 'No priorities selected.'}")

# Initialize csps list to track recommendations
csps = []

# Suggesting the Best CSP Based on Selections
st.subheader("10. Our CSP Recommendation")

# Decision Logic for CSP Recommendation
if "Security" in priorities or "Compliance" in priorities:
    csps.append("Microsoft Azure")
    st.markdown("### 🛡️ We recommend **[Microsoft Azure](https://azure.microsoft.com/)** for its strong focus on enterprise security and compliance features.")
elif "AI and Machine Learning Capabilities" in desired_features or "Data Analytics" in priorities:
    csps.append("Google Cloud Platform (GCP)")
    st.markdown("### 🤖 We recommend **[Google Cloud Platform (GCP)](https://cloud.google.com/)** for its industry-leading AI, machine learning, and data analytics capabilities.")
elif "Scalability" in priorities or "Infrastructure" in assets:
    csps.append("Amazon Web Services (AWS)")
    st.markdown("### 🌐 We recommend **[Amazon Web Services (AWS)](https://aws.amazon.com/)** for its highly scalable and flexible infrastructure.")
elif "Cost Efficiency" in priorities:
    csps.append("Google Cloud Platform (GCP)")
    st.markdown("### 💰 We recommend **[Google Cloud Platform (GCP)](https://cloud.google.com/)** for its competitive pricing and strong cost management tools.")
else:
    st.markdown("### 🌍 Based on your preferences, we suggest exploring each CSP further to find the best match for your needs.")

# Final Confirmation
st.subheader("11. Are You Ready to Embark?")
ready = st.radio(
    "Do you feel ready to embark on your tropical cloud migration adventure?",
    ["Yes, I’m ready!", "I need to make some adjustments."]
)

# Conditional message based on readiness
if ready == "Yes, I’m ready!":
    st.markdown("### 🏝️ The Adventure has been planned! Your tropical cloud journey awaits. Best of luck!")
else:
    st.markdown("### 🌴 No worries! Take your time to review and adjust your plan before setting off.")
