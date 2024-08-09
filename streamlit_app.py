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

# Type of Assets
st.subheader("5. What Types of Assets Do You Have on the Cloud?")
st.markdown("Select all that apply:")

# Checkboxes for selecting cloud assets
assets = []
if st.checkbox("Data Storage"):
    assets.append("Data Storage")
if st.checkbox("Applications"):
    assets.append("Applications")
if st.checkbox("Databases"):
    assets.append("Databases")
if st.checkbox("Development Tools"):
    assets.append("Development Tools")
if st.checkbox("Other"):
    assets.append("Other")

# Priorities in Selecting a CSP
st.subheader("6. What Are Your Top Priorities When Selecting a CSP?")
st.markdown("Select all that apply:")

# Checkboxes for selecting CSP priorities
priorities = []
if st.checkbox("Performance"):
    priorities.append("Performance")
if st.checkbox("Compliance"):
    priorities.append("Compliance")
if st.checkbox("Support"):
    priorities.append("Support")
if st.checkbox("Scalability"):
    priorities.append("Scalability")
if st.checkbox("Cost Efficiency"):
    priorities.append("Cost Efficiency")
if st.checkbox("Security"):
    priorities.append("Security")
if st.checkbox("Innovation"):
    priorities.append("Innovation")

# Summary of Selections
st.markdown("### 🌟 Here's a summary of your input:")
st.write(f"**Assets on the Cloud:** {', '.join(assets) if assets else 'No assets selected.'}")
st.write(f"**Top Priorities in CSP Selection:** {', '.join(priorities) if priorities else 'No priorities selected.'}")

