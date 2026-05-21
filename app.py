import streamlit as st
import pandas as pd
from datetime import datetime

# Configurazione pagina
st.set_page_config(
    page_title="Joe Fenix Method Calculator",
    page_icon="🔥",
    layout="wide"
)

# Colori brand
SAGE_GREEN = "
"
ENERGY_ORANGE = "
"

# Header
st.markdown(f"""
    <h1 style='text-align: center; color: {ENERGY_ORANGE};'>
        🔥 Joe Fenix Method Calculator
    </h1>
    <h3 style='text-align: center; color: {SAGE_GREEN};'>
        Build. Protect. Fuel.
    </h3>
    """, unsafe_allow_html=True)

st.markdown("---")

# Sidebar - Input utente
st.sidebar.header("📊 I Tuoi Dati")

# Dati personali
eta = st.sidebar.number_input("Età", min_value=18, max_value=100, value=40)
peso = st.sidebar.number_input("Peso (kg)", min_value=40.0, max_value=200.0, value=75.0, step=0.5)
altezza = st.sidebar.number_input("Altezza (cm)", min_value=140, max_value=220, value=170)
sesso = st.sidebar.selectbox("Sesso", ["Maschio", "Femmina"])

# Livello di attività
st.sidebar.subheader("🏃 Livello di Attività")
attivita = st.sidebar.select_slider(
    "Seleziona il tuo livello",
    options=["Sedentario", "Leggero", "Moderato", "Attivo", "Molto Attivo"],
    value="Moderato"
)

# Obiettivo
st.sidebar.subheader("🎯 Obiettivo")
obiettivo = st.sidebar.radio(
    "Cosa vuoi ottenere?",
    ["Perdere peso", "Mantenere peso", "Aumentare massa"]
)

# Preferenze alimentari
st.sidebar.subheader("🥗 Preferenze Alimentari")
dieta = st.sidebar.selectbox(
    "Tipo di dieta",
    ["Onnivoro", "Vegetariano", "Vegano"]
)

# Patologie (opzionale)
st.sidebar.subheader("⚕️ Patologie (opzionale)")
diabete = st.sidebar.checkbox("Diabete")
ipertensione = st.sidebar.checkbox("Ipertensione")
intolleranze = st.sidebar.multiselect(
    "Intolleranze",
    ["Lattosio", "Glutine", "Frutta secca", "Uova"]
)

# Calcolo BMR (Mifflin-St Jeor)
def calcola_bmr(peso, altezza, eta, sesso):
    if sesso == "Maschio":
        return 10 * peso + 6.25 * altezza - 5 * eta + 5
    else:
        return 10 * peso + 6.25 * altezza - 5 * eta - 161

# Fattore attività
fattori_attivita = {
    "Sedentario": 1.2,
    "Leggero": 1.375,
    "Moderato": 1.55,
    "Attivo": 1.725,
    "Molto Attivo": 1.9
}

# Calcolo TDEE
bmr = calcola_bmr(peso, altezza, eta, sesso)
tdee = bmr * fattori_attivita[attivita]

# Aggiustamento per obiettivo
if obiettivo == "Perdere peso":
    calorie_target = tdee - 500
elif obiettivo == "Aumentare massa":
    calorie_target = tdee + 300
else:
    calorie_target = tdee

# Calcolo macronutrienti
proteine_g = peso * 2.2  # 2.2g per kg (high protein)
grassi_g = (calorie_target * 0.25) / 9  # 25% delle calorie
carboidrati_g = (calorie_target - (proteine_g * 4) - (grassi_g * 9)) / 4

# Main content
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🔥 Calorie Giornaliere", f"{int(calorie_target)} kcal")
    st.caption(f"TDEE: {int(tdee)} kcal")

with col2:
    st.metric("💪 Proteine", f"{int(proteine_g)} g")
    st.caption(f"{int((proteine_g * 4 / calorie_target) * 100)}% delle calorie")

with col3:
    st.metric("🍚 Carboidrati", f"{int(carboidrati_g)} g")
    st.caption(f"{int((carboidrati_g * 4 / calorie_target) * 100)}% delle calorie")

st.markdown("---")

col4, col5 = st.columns(2)

with col4:
    st.metric("🥑 Grassi", f"{int(grassi_g)} g")
    st.caption(f"{int((grassi_g * 9 / calorie_target) * 100)}% delle calorie")

with col5:
    bmi = peso / ((altezza / 100) ** 2)
    st.metric("📊 BMI", f"{bmi:.1f}")
    if bmi < 18.5:
        st.caption("⚠️ Sottopeso")
    elif bmi < 25:
        st.caption("✅ Normopeso")
    elif bmi < 30:
        st.caption("⚠️ Sovrappeso")
    else:
        st.caption("⚠️ Obesità")

st.markdown("---")

# The Perfect Day
st.header("🌟 The Perfect Day")
st.subheader("Distribuzione proteica ottimale")

col_breakfast, col_lunch, col_dinner, col_snack = st.columns(4)

with col_breakfast:
    st.markdown(f"**🌅 Colazione**")
    st.markdown(f"<h2 style='color: {ENERGY_ORANGE};'>~30g</h2>", unsafe_allow_html=True)
    st.caption("Proteine")

with col_lunch:
    st.markdown(f"**☀️ Pranzo**")
    st.markdown(f"<h2 style='color: {ENERGY_ORANGE};'>40-50g</h2>", unsafe_allow_html=True)
    st.caption("Proteine")

with col_dinner:
    st.markdown(f"**🌙 Cena**")
    st.markdown(f"<h2 style='color: {ENERGY_ORANGE};'>30-40g</h2>", unsafe_allow_html=True)
    st.caption("Proteine")

with col_snack:
    st.markdown(f"**🍎 Snack**")
    st.markdown(f"<h2 style='color: {ENERGY_ORANGE};'>~{int(proteine_g - 110)}g</h2>", unsafe_allow_html=True)
    st.caption("Proteine")

st.markdown("---")

# Joe Fenix Method CORE
st.header("🎯 Joe Fenix Method (CORE)")

col_build, col_protect, col_fuel = st.columns(3)

with col_build:
    st.markdown(f"### <span style='color: {ENERGY_ORANGE};'>BUILD</span>", unsafe_allow_html=True)
    st.markdown("**Proteine a ogni pasto**")
    st.markdown(f"Target: **{int(proteine_g)}g/giorno**")
    st.caption("Pollo, pesce, uova, yogurt greco, legumi")

with col_protect:
    st.markdown(f"### <span style='color: {SAGE_GREEN};'>PROTECT</span>", unsafe_allow_html=True)
    st.markdown("**Verdure e micronutrienti**")
    st.markdown("Target: **5+ porzioni/giorno**")
    st.caption("Broccoli, spinaci, zucchine, peperoni")

with col_fuel:
    st.markdown(f"### <span style='color: {ENERGY_ORANGE};'>FUEL</span>", unsafe_allow_html=True)
    st.markdown("**Carboidrati + Grassi**")
    st.markdown(f"**{int(carboidrati_g)}g** carbo | **{int(grassi_g)}g** grassi")
    st.caption("Riso, avena, quinoa | Olio EVO, avocado, noci")

st.markdown("---")

# Note finali
st.info("""
📖 **Accesso gratuito per i lettori del cookbook**  
*"The Anti-Inflammatory High Protein Meal Prep Cookbook"* (2026)

🔗 Repository: [github.com/itqmethodology-afk/joe-fenix-calculator](https://github.com/itqmethodology-afk/joe-fenix-calculator)
""")

st.caption("© 2026 Giuseppe Visconti (Joe Fenix) | Build. Protect. Fuel. 🔥")
