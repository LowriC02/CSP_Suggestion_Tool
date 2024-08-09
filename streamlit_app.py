import streamlit as st

# Adding a tropical background image (hosted online or in your local directory)
st.image("https://r.search.yahoo.com/_ylt=AwrNPKkwd7Zmfb8y2VpNBQx.;_ylu=c2VjA3NyBHNsawNpbWcEb2lkAzA0NmEyOGVmZThiMGEwYzgzN2NhMzUzZWE3ZDE3NTUxBGdwb3MDMQRpdANiaW5n/RV=2/RE=1723262896/RO=11/RU=https%3a%2f%2fwww.pinterest.com%2fpin%2f679973243720371474%2f/RK=2/RS=QMI2P4TrVr1IHF4io.kSMBXoyYI-", use_column_width=True)

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

# Optional: Add another tropical-themed image or icon
st.image("https://example.com/tropical-icon.png", width=100)
