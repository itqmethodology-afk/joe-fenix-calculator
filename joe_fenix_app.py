"""
Joe Fenix Method Calculator
Main Streamlit application with reader authentication
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import config
from calculator import calculate_daily_targets
from meal_prep import generate_weekly_plan, generate_shopping_list
from recipes import get_recipes_by_diet
from export_utils import export_to_pdf, export_to_word

# ============================================
# AUTHENTICATION SYSTEM
# ============================================
def check_access():
    """Check if user has valid access code"""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    if not st.session_state.authenticated:
        # Login page
        st.title("🔒 Joe Fenix Method Calculator")
        st.markdown(f"**Accesso riservato ai lettori del cookbook**")
        st.markdown(f"*{config.COOKBOOK_TITLE}*")
        st.markdown("---")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            access_code = st.text_input(
                "Inserisci il tuo codice lettore:",
                type="password",
                help="Trovi il codice all'interno del tuo cookbook"
            )
            
            if st.button("🔓 Accedi", use_container_width=True):
                if access_code.strip().upper() in [code.upper() for code in config.VALID_READER_CODES]:
                    st.session_state.authenticated = True
                    st.success("✅ Accesso consentito! Benvenuto.")
                    st.balloons()
                    st.rerun()
                else:
                    st.error("❌ Codice non valido. Controlla il tuo cookbook o contatta il supporto.")
        
        st.markdown("---")
        st.info("📖 Non hai ancora il cookbook? Scopri come ottenerlo su joefenixmethod.com")
        st.stop()

# Call authentication at the start
check_access()

# ============================================
# MAIN APP (only accessible after authentication)
# ============================================

# Page config
st.set_page_config(
    page_title=config.APP_TITLE,
    page_icon="🔥",
    layout="wide"
)

# Custom CSS with brand colors
st.markdown(f"""
    <style>
    .main-header {{
        color: {config.SAGE_GREEN};
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
    }}
    .subtitle {{
        color: {config.ENERGY_ORANGE};
        font-size: 1.5rem;
        text-align: center;
        margin-bottom: 2rem;
    }}
    .stButton>button {{
        background-color: {config.ENERGY_ORANGE};
        color: white;
    }}
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown(f'<div class="main-header">{config.APP_TITLE}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="subtitle">{config.APP_SUBTITLE}</div>', unsafe_allow_html=True)

# Sidebar - User inputs
st.sidebar.header("📊 I tuoi dati")

# Basic info
age = st.sidebar.number_input("Età", min_value=18, max_value=100, value=35)
weight = st.sidebar.number_input("Peso (kg)", min_value=40.0, max_value=200.0, value=70.0, step=0.5)
height = st.sidebar.number_input("Altezza (cm)", min_value=140, max_value=220, value=170)
gender = st.sidebar.selectbox("Sesso", ["Maschio", "Femmina"])

# Activity level
activity = st.sidebar.selectbox(
    "Livello di attività",
    ["Sedentario", "Leggermente attivo", "Moderatamente attivo", "Molto attivo", "Estremamente attivo"]
)

# Goal
goal = st.sidebar.selectbox(
    "Obiettivo",
    ["Perdita peso", "Mantenimento", "Aumento massa"]
)

# Diet preference
diet_pref = st.sidebar.selectbox(
    "Preferenza alimentare",
    ["Onnivoro", "Vegetariano", "Vegano"]
)

# Calculate button
if st.sidebar.button("🔥 Calcola il tuo piano", use_container_width=True):
    # Calculate targets
    targets = calculate_daily_targets(
        weight=weight,
        height=height,
        age=age,
        gender=gender.lower(),
        activity_level=activity,
        goal=goal
    )
    
    # Store in session state
    st.session_state.targets = targets
    st.session_state.diet_pref = diet_pref

# Main content
if 'targets' in st.session_state:
    targets = st.session_state.targets
    
    # Display targets
    st.header("🎯 I tuoi target giornalieri")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Calorie", f"{targets['calories']} kcal")
    with col2:
        st.metric("Proteine", f"{targets['protein']} g")
    with col3:
        st.metric("Carboidrati", f"{targets['carbs']} g")
    with col4:
        st.metric("Grassi", f"{targets['fats']} g")
    
    # BMI
    bmi = weight / ((height/100) ** 2)
    st.info(f"📊 Il tuo BMI: {bmi:.1f}")
    
    st.markdown("---")
    
    # Weekly plan
    st.header("📅 Piano settimanale")
    
    weekly_plan = generate_weekly_plan(targets, st.session_state.diet_pref)
    
    # Display plan as table
    df_plan = pd.DataFrame(weekly_plan)
    st.dataframe(df_plan, use_container_width=True)
    
    st.markdown("---")
    
    # Shopping list
    st.header("🛒 Lista della spesa")
    
    shopping_list = generate_shopping_list(st.session_state.diet_pref)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Proteine")
        for item in shopping_list['proteins']:
            st.write(f"• {item}")
    
    with col2:
        st.subheader("Carboidrati")
        for item in shopping_list['carbs']:
            st.write(f"• {item}")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Grassi")
        for item in shopping_list['fats']:
            st.write(f"• {item}")
    
    with col4:
        st.subheader("Verdure")
        for item in shopping_list['vegetables']:
            st.write(f"• {item}")
    
    st.markdown("---")
    
    # Recipes
    st.header("🍳 Ricette signature")
    
    recipes = get_recipes_by_diet(st.session_state.diet_pref)
    
    for recipe in recipes:
        with st.expander(f"📖 {recipe['name']}"):
            st.write(f"**Tipo:** {recipe['meal_type']}")
            st.write(f"**Porzioni:** {recipe['servings']}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Ingredienti:**")
                for ing in recipe['ingredients']:
                    st.write(f"• {ing}")
            
            with col2:
                st.write("**Macro per porzione:**")
                st.write(f"• Calorie: {recipe['macros']['calories']} kcal")
                st.write(f"• Proteine: {recipe['macros']['protein']} g")
                st.write(f"• Carboidrati: {recipe['macros']['carbs']} g")
                st.write(f"• Grassi: {recipe['macros']['fats']} g")
            
            st.write("**Istruzioni:**")
            for i, step in enumerate(recipe['instructions'], 1):
                st.write(f"{i}. {step}")
    
    st.markdown("---")
    
    # Export options
    st.header("📥 Esporta il tuo piano")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📄 Esporta PDF", use_container_width=True):
            pdf_file = export_to_pdf(targets, weekly_plan, shopping_list)
            st.download_button(
                "⬇️ Scarica PDF",
                data=pdf_file,
                file_name=f"joe_fenix_plan_{datetime.now().strftime('%Y%m%d')}.pdf",
                mime="application/pdf"
            )
    
    with col2:
        if st.button("📝 Esporta Word", use_container_width=True):
            word_file = export_to_word(targets, weekly_plan, shopping_list)
            st.download_button(
                "⬇️ Scarica Word",
                data=word_file,
                file_name=f"joe_fenix_plan_{datetime.now().strftime('%Y%m%d')}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
    
    with col3:
        st.info("🌐 Versione web interattiva già disponibile!")

else:
    # Welcome message
    st.info("👈 Inserisci i tuoi dati nella barra laterale e clicca su 'Calcola il tuo piano' per iniziare!")
    
    st.markdown("---")
    
    # Method explanation
    st.header("💡 Il Joe Fenix Method")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🏗️ BUILD")
        st.write("Proteine a ogni pasto per costruire e mantenere la massa muscolare")
    
    with col2:
        st.subheader("🛡️ PROTECT")
        st.write("Verdure e micronutrienti per proteggere il corpo dall'infiammazione")
    
    with col3:
        st.subheader("⚡ FUEL")
        st.write("Carboidrati intelligenti e grassi buoni per energia sostenibile")

# Footer
st.markdown("---")
st.markdown(
    f"<div style='text-align: center; color: {config.SAGE_GREEN};'>"
    f"© 2026 Joe Fenix Method | {config.COOKBOOK_TITLE}"
    "</div>",
    unsafe_allow_html=True
)
