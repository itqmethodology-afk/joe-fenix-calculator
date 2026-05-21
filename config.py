"""
Configurazione del Joe Fenix Method Calculator
"""

# Brand Colors
SAGE_GREEN = "
"
ENERGY_ORANGE = "
"
WHITE = "
"

# Costanti nutrizionali
PROTEINE_PER_KG = 2.2  # grammi per kg di peso corporeo
PERCENTUALE_GRASSI = 0.25  # 25% delle calorie totali
CALORIE_PER_G_PROTEINE = 4
CALORIE_PER_G_CARBOIDRATI = 4
CALORIE_PER_G_GRASSI = 9

# Fattori di attività (moltiplicatori TDEE)
FATTORI_ATTIVITA = {
    "Sedentario": 1.2,
    "Leggero": 1.375,
    "Moderato": 1.55,
    "Attivo": 1.725,
    "Molto Attivo": 1.9
}

# Aggiustamenti calorici per obiettivo
DEFICIT_PERDITA_PESO = 500  # kcal
SURPLUS_MASSA = 300  # kcal

# Distribuzione proteica giornaliera (The Perfect Day)
PROTEINE_COLAZIONE = 30  # grammi
PROTEINE_PRANZO_MIN = 40  # grammi
PROTEINE_PRANZO_MAX = 50  # grammi
PROTEINE_CENA_MIN = 30  # grammi
PROTEINE_CENA_MAX = 40  # grammi

# Porzioni verdure giornaliere
PORZIONI_VERDURE_MIN = 5

# Smart Grocery List - Categorie essenziali
GROCERY_PROTEINE = [
    "Pollo (petto)",
    "Uova",
    "Pesce (salmone, merluzzo)",
    "Yogurt greco",
    "Legumi (lenticchie, ceci)"
]

GROCERY_CARBOIDRATI = [
    "Riso (basmati, integrale)",
    "Avena",
    "Quinoa",
    "Patate dolci"
]

GROCERY_GRASSI = [
    "Olio EVO",
    "Avocado",
    "Frutta secca (mandorle, noci)",
    "Semi (chia, lino)"
]

GROCERY_VERDURE = [
    "Broccoli",
    "Spinaci",
    "Zucchine",
    "Peperoni",
    "Pomodori"
]

# Meal Prep - Timing
MEAL_PREP_TEMPO_MINUTI = 60
MEAL_PREP_GIORNI = 7

# Portion Control (metodo a mano)
PORTION_CONTROL = {
    "Proteine": "Palmo della mano",
    "Carboidrati": "Pugno chiuso",
    "Grassi": "Pollice",
    "Verdure": "Due mani a coppa"
}

# Ricette signature (dal cookbook)
RICETTE_SIGNATURE = [
    "Quinoa & Spinach Frittata",
    "Blueberry Pancakes (farina di mandorle)",
    "Yogurt greco con noci e semi di chia",
    "Pollo al curry con riso basmati",
    "Salmone al forno con verdure"
]

# Lingue supportate
LINGUE = ["Italiano", "English (US)"]

# Info autore
AUTORE = "Giuseppe Visconti (Joe Fenix)"
COOKBOOK_TITOLO = "The Anti-Inflammatory High Protein Meal Prep Cookbook"
COOKBOOK_ANNO = 2026
GITHUB_REPO = "https://github.com/itqmethodology-afk/joe-fenix-calculator"
