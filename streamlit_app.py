import streamlit as st

# Engaging App Introduction
st.title("Welcome to the Cloud Adventure: Your CSP Suggestion Tool!")

st.markdown("""
🌴 **Welcome aboard!** Embark on your cloud migration journey with us. Whether you're optimising performance, balancing costs, 
or ensuring top-notch security, this tool is your trusted companion. Let’s help you navigate the cloud landscape 
and find the perfect Cloud Service Provider (CSP) tailored to your needs. Ready to get started? Let's dive in! 🏝️
""")

# Industry Type Input - Specific industries from the text
industry = st.radio("What industry does your company operate in?", 
                    ["Healthcare", "Finance", "Retail", "Manufacturing", "Technology", "Other"])

# Location Input - Predefined options (Global and Continents)
location = st.radio("Where does your company operate?", 
                    ["Global", "Africa", "Asia", "Europe", "North America", "South America", "Australia"])



# Continuing the adventure with a new section
st.header("🌥️ Let's Explore Your Cloud Landscape")

st.markdown("""
Now that we know a bit about your company, it's time to delve into your cloud journey. 
This will help us suggest the perfect cloud migration path for you. 
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


import streamlit as st

# Introducing the next section
st.header("💻 Digging Deeper into Your Cloud Assets and Priorities")

st.markdown("""
Let’s take a closer look at what you currently have on the cloud and what you consider most important when selecting a Cloud Service Provider (CSP). 
This will help us suggest the best CSP options tailored to your needs.
""")

# Type of Assets - using radio buttons for primary focus (each asset group)
st.subheader("5. What Types of Assets Do You Primarily Have on the Cloud?")
primary_asset = st.radio(
    "Select the most significant type of asset your company has on the cloud:",
    ["Data Storage", "Applications", "Databases", "Development Tools", "Other"]
)

# Additional assets (optional, using checkboxes to allow multiple selections)
st.markdown("Do you have any other types of assets on the cloud? Select all that apply:")
additional_assets = []
if st.checkbox("Data Storage"):
    additional_assets.append("Data Storage")
if st.checkbox("Applications"):
    additional_assets.append("Applications")
if st.checkbox("Databases"):
    additional_assets.append("Databases")
if st.checkbox("Development Tools"):
    additional_assets.append("Development Tools")
if st.checkbox("Other"):
    additional_assets.append("Other")

# Priorities in Selecting a CSP - using radio buttons for primary priority
st.subheader("6. What Is Your Top Priority When Selecting a CSP?")
primary_priority = st.radio(
    "Select your company’s top priority when choosing a CSP:",
    ["Performance", "Compliance", "Support", "Scalability", "Cost Efficiency", "Security", "Innovation"]
)

# Additional priorities (optional, using checkboxes to allow multiple selections)
st.markdown("Do you have any other priorities? Select all that apply:")
additional_priorities = []
if st.checkbox("Performance"):
    additional_priorities.append("Performance")
if st.checkbox("Compliance"):
    additional_priorities.append("Compliance")
if st.checkbox("Support"):
    additional_priorities.append("Support")
if st.checkbox("Scalability"):
    additional_priorities.append("Scalability")
if st.checkbox("Cost Efficiency"):
    additional_priorities.append("Cost Efficiency")
if st.checkbox("Security"):
    additional_priorities.append("Security")
if st.checkbox("Innovation"):
    additional_priorities.append("Innovation")

# Summary of Selections
st.markdown("### 🌟 Here's a summary of your input:")
st.write(f"**Primary Asset on the Cloud:** {primary_asset}")
st.write(f"**Additional Assets on the Cloud:** {', '.join(additional_assets) if additional_assets else 'None selected.'}")
st.write(f"**Top Priority in CSP Selection:** {primary_priority}")
st.write(f"**Additional Priorities in CSP Selection:** {', '.join(additional_priorities) if additional_priorities else 'None selected.'}")

