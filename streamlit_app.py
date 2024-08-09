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
st.subheader("5. What Types of Assets Do You Have on the Cloud?")
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

# Priorities in Selecting a CSP - Checkboxes for multiple selections
st.subheader("6. What Are Your Top Priorities When Selecting a CSP?")
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
if st.checkbox("Other"):
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
st.subheader("7. What Security Measures Are Most Important to You?")
security_preferences = []
if st.checkbox("Advanced Encryption"):
    security_preferences.append("Advanced Encryption")
if st.checkbox("Multi-Factor Authentication (MFA)"):
    security_preferences.append("Multi-Factor Authentication (MFA)")
if st.checkbox("Regular Security Audits"):
    security_preferences.append("Regular Security Audits")
if st.checkbox("Data Loss Prevention (DLP)"):
    security_preferences.append("Data Loss Prevention (DLP)")
if st.checkbox("Intrusion Detection and Prevention"):
    security_preferences.append("Intrusion Detection and Prevention")
if st.checkbox("Compliance with Industry Standards (e.g., GDPR, ISO 27001)"):
    security_preferences.append("Compliance with Industry Standards (e.g., GDPR, ISO 27001)")

# Desired Features in a CSP - Checkboxes for multiple selections
st.subheader("8. What Features Are You Looking For in a CSP?")
desired_features = []
if st.checkbox("High Availability and Uptime Guarantees"):
    desired_features.append("High Availability and Uptime Guarantees")
if st.checkbox("24/7 Customer Support"):
    desired_features.append("24/7 Customer Support")
if st.checkbox("Scalable Infrastructure"):
    desired_features.append("Scalable Infrastructure")
if st.checkbox("Cost Management Tools"):
    desired_features.append("Cost Management Tools")
if st.checkbox("AI and Machine Learning Capabilities"):
    desired_features.append("AI and Machine Learning Capabilities")
if st.checkbox("Integration with Existing Systems"):
    desired_features.append("Integration with Existing Systems")
if st.checkbox("Other"):
    desired_features.append("Other")

# Summary of Selections
st.markdown("### 🌟 Here's a summary of your security preferences and feature wishlist:")
st.write(f"**Security Measures:** {', '.join(security_preferences) if security_preferences else 'No security measures selected.'}")
st.write(f"**Desired CSP Features:** {', '.join(desired_features) if desired_features else 'No features selected.'}")

# 🚶‍♂️🚶‍♀️ Choosing Your Cloud Companions
st.header("🚶‍♂️🚶‍♀️ Choosing Your Cloud Companions")

st.markdown("""
Every great adventure needs trusted companions. Based on the journey you've mapped out, let’s explore the Cloud Service Providers (CSPs) that could be your ideal allies. 
Select the CSPs you’re considering or let us suggest some based on your preferences.
""")

# Information about AWS, Azure, and GCP
st.subheader("Learn About Your Potential Companions")

st.markdown("### 🌩️ Amazon Web Services (AWS)")
st.markdown("""
- **Overview**: AWS is the most comprehensive and widely adopted cloud platform in the world, offering over 200 fully featured services from data centres globally.
- **Strengths**:
  - Extensive global network with a vast array of services.
  - Strong developer community and ecosystem.
  - Highly scalable and flexible infrastructure.
  - Advanced AI and machine learning capabilities.
  - Deep security and compliance support.
- **Use Cases**: Ideal for companies needing robust infrastructure, wide-ranging services, and advanced AI/ML tools.
""")

st.markdown("### ☁️ Microsoft Azure")
st.markdown("""
- **Overview**: Microsoft Azure is a leading cloud service provider offering a range of solutions including IaaS, PaaS, and SaaS. Azure is integrated with Microsoft's enterprise software, making it a strong choice for businesses already using Microsoft products.
- **Strengths**:
  - Seamless integration with Microsoft tools like Office 365, Dynamics 365, and Active Directory.
  - Strong enterprise focus with extensive hybrid cloud capabilities.
  - Advanced analytics and data solutions, including Azure Synapse Analytics.
  - Comprehensive AI and machine learning tools.
  - Wide support for open-source technologies and platforms.
- **Use Cases**: Best suited for enterprises already embedded in the Microsoft ecosystem, and those looking for hybrid cloud solutions.
""")

st.markdown("### ☀️ Google Cloud Platform (GCP)")
st.markdown("""
- **Overview**: GCP offers a range of cloud services focused on data analytics, AI, and machine learning. It is known for its data management and analytics capabilities, leveraging Google’s experience in handling large-scale data.
- **Strengths**:
  - Industry-leading data analytics and machine learning capabilities.
  - Strong emphasis on open source and multi-cloud environments.
  - Integration with Google’s other services, such as BigQuery for data analytics.
  - Competitive pricing for compute and storage services.
  - High-performance networking and security infrastructure.
- **Use Cases**: Ideal for organizations focused on big data, analytics, and AI/ML projects.
""")

# Suggested CSPs - Based on user input, we'll suggest CSPs here
st.subheader("9. Which Cloud Service Providers Are You Considering?")
csps = []
if st.checkbox("Amazon Web Services (AWS)"):
    csps.append("Amazon Web Services (AWS)")
if st.checkbox("Microsoft Azure"):
    csps.append("Microsoft Azure")
if st.checkbox("Google Cloud Platform (GCP)"):
    csps.append("Google Cloud Platform (GCP)")


# Summary of Selections
st.markdown("### 🌟 Here's a summary of your cloud companions:")
st.write(f"**Selected CSPs:** {', '.join(csps) if csps else 'No CSPs selected.'}")

# 🏝️ Wrapping Up Your Tropical Cloud Adventure
st.header("🏝️ Wrapping Up Your Tropical Cloud Adventure")

st.markdown("""
The path ahead is clear, but before you set off on your tropical cloud migration journey, let's ensure everything is in place. 
Review your selections and make sure you have all the tools and companions you need for a successful expedition through the cloud forests.
""")

# Final Review of Selections
st.subheader("14. Reviewing Your Selections")
st.markdown("### 🛠️ Tools & Resources")
st.write(f"**Key Assets on the Cloud:** {', '.join(assets) if assets else 'No assets selected.'}")

st.markdown("### 🛡️ Security Measures")
st.write(f"**Security Preferences:** {', '.join(security_preferences) if security_preferences else 'No security preferences selected.'}")

st.markdown("### 📦 Desired Features")
st.write(f"**CSP Features:** {', '.join(desired_features) if desired_features else 'No features selected.'}")

st.markdown("### 🌩️ Cloud Companions")
st.write(f"**Selected CSPs:** {', '.join(csps) if csps else 'No CSPs selected.'}")

# CSP Websites
if "Amazon Web Services (AWS)" in csps:
    st.markdown("[Visit AWS](https://aws.amazon.com/)")
if "Microsoft Azure" in csps:
    st.markdown("[Visit Microsoft Azure](https://azure.microsoft.com/)")
if "Google Cloud Platform (GCP)" in csps:
    st.markdown("[Visit Google Cloud](https://cloud.google.com/)")

# Suggesting the Best CSP Based on Selections
st.subheader("15. Our CSP Recommendation")
if "Security" in priorities or "Compliance" in priorities:
    st.markdown("### 🛡️ We recommend **Microsoft Azure** for its strong focus on enterprise security and compliance features.")
elif "AI and Machine Learning Capabilities" in desired_features or "Data Analytics" in priorities:
    st.markdown("### 🤖 We recommend **Google Cloud Platform (GCP)** for its industry-leading AI, machine learning, and data analytics capabilities.")
elif "Scalability" in priorities or "Infrastructure" in assets:
    st.markdown("### 🌐 We recommend **Amazon Web Services (AWS)** for its highly scalable and flexible infrastructure.")
else:
    st.markdown("### 🌍 Based on your preferences, all three CSPs—**AWS, Azure, and GCP**—could be good fits. Consider exploring each further to find the best match for your needs.")

# Final Confirmation
st.subheader("16. Are You Ready to Embark?")
ready = st.radio(
    "Do you feel ready to embark on your tropical cloud migration adventure?",
    ["Yes, I’m ready!", "I need to make some adjustments."]
)

# Conditional message based on readiness
if ready == "Yes, I’m ready!":
    st.markdown("### 🏝️ All systems go! Your tropical cloud journey awaits. Best of luck!")
else:
    st.markdown("### 🌴 No worries! Take your time to review and adjust your plan before setting off.")
