import streamlit as st

# Adding a tropical background photo
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvMPjkvIpGCKu98eeCCdXVKSYrVaZMn_mlKuy3wspy23FYvydM&s", use_column_width=True)
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
