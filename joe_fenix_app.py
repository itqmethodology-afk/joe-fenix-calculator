import streamlit as st
import pandas as pd
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Joe Fenix Method Calculator",
    page_icon="🔥",
    layout="wide"
)

# Brand colors
SAGE_GREEN = "
"
ENERGY_ORANGE = "
"

# Title
st.title("🔥 Joe Fenix Method + Meal Prep Calculator")
st.markdown("**BUILD. PROTECT. FUEL.**")

# Sidebar - User Input
st.sidebar.header("Your Profile")

# Authentication
reader_code = st.sidebar.text_input("Reader Code", type="password", help="Enter your unique code from the cookbook")

if reader_code:
    # Basic Info
    age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=60)
    weight = st.sidebar.number_input("Weight (kg)", min_value=40, max_value=200, value=70)
    height = st.sidebar.number_input("Height (cm)", min_value=140, max_value=220, value=170)
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    
    # Activity Level
    activity = st.sidebar.selectbox("Activity Level", [
        "Sedentary",
        "Lightly Active",
        "Moderately Active",
        "Very Active"
    ])
    
    # Goal
    goal = st.sidebar.selectbox("Goal", [
        "Maintain Weight",
        "Lose Weight",
        "Gain Muscle"
    ])
    
    # Dietary Preference
    diet_pref = st.sidebar.selectbox("Dietary Preference", [
        "Omnivore",
        "Vegetarian",
        "Vegan"
    ])
    
    # Health Conditions
    st.sidebar.subheader("Health Considerations")
    diabetes = st.sidebar.checkbox("Diabetes")
    hypertension = st.sidebar.checkbox("Hypertension")
    intolerances = st.sidebar.text_input("Food Intolerances (comma separated)")
    
    # Calculate BMI
    bmi = weight / ((height/100) ** 2)
    
    # Display Results
    st.header("Your Personalized Plan")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("BMI", f"{bmi:.1f}")
    
    with col2:
        st.metric("Daily Protein Target", "100-120g")
    
    with col3:
        st.metric("Daily Calories", "1800-2000")
    
    # The Perfect Day
    st.subheader("🌅 The Perfect Day")
    st.markdown("""
    - **Breakfast**: ~30g protein
    - **Lunch**: 40-50g protein
    - **Dinner**: 30-40g protein
    - **Snacks**: Protein-rich support
    """)
    
    # Export buttons
    st.subheader("📥 Export Your Plan")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.button("📄 Export PDF")
    with col2:
        st.button("📝 Export Word")
    with col3:
        st.button("🌐 Web View")

else:
    st.info("👆 Enter your reader code from the cookbook to access the calculator")
    st.markdown("---")
    st.markdown("### About the Joe Fenix Method")
    st.markdown("""
    **BUILD. PROTECT. FUEL.**
    
    A practical approach to daily nutrition:
    - **BUILD** — Include protein at every meal
    - **PROTECT** — Load your plate with vegetables and micronutrients  
    - **FUEL** — Add smart carbs and healthy fats
    
    This calculator is free for readers of *The Anti-Inflammatory High Protein Meal Prep Cookbook* (2026).
    """)
