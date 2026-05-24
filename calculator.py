"""
Joe Fenix Method Calculator
Calculates personalized nutrition targets
"""

def calculate_bmr(weight, height, age, gender):
    """Calculate Basal Metabolic Rate using Mifflin-St Jeor equation"""
    if gender.lower() == "male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    return bmr

def calculate_tdee(bmr, activity_level):
    """Calculate Total Daily Energy Expenditure"""
    activity_multipliers = {
        "sedentary": 1.2,
        "lightly active": 1.375,
        "moderately active": 1.55,
        "very active": 1.725
    }
    multiplier = activity_multipliers.get(activity_level.lower(), 1.2)
    return bmr * multiplier

def calculate_calorie_target(tdee, goal):
    """Adjust calories based on goal"""
    if goal.lower() == "lose weight":
        return tdee - 500  # 500 cal deficit
    elif goal.lower() == "gain muscle":
        return tdee + 300  # 300 cal surplus
    else:
        return tdee  # maintenance

def calculate_protein_target(weight, goal, activity_level):
    """Calculate daily protein target in grams"""
    if goal.lower() == "gain muscle":
        return weight * 2.0  # 2g per kg
    elif activity_level.lower() in ["moderately active", "very active"]:
        return weight * 1.8  # 1.8g per kg
    else:
        return weight * 1.6  # 1.6g per kg (minimum for health)

def calculate_macros(calories, protein_grams):
    """Calculate full macro breakdown"""
    protein_calories = protein_grams * 4
    
    # 30% calories from fat
    fat_calories = calories * 0.30
    fat_grams = fat_calories / 9
    
    # Remaining calories from carbs
    carb_calories = calories - protein_calories - fat_calories
    carb_grams = carb_calories / 4
    
    return {
        "protein_g": round(protein_grams),
        "carbs_g": round(carb_grams),
        "fat_g": round(fat_grams),
        "calories": round(calories)
    }

def distribute_protein_meals():
    """The Perfect Day protein distribution"""
    return {
        "breakfast": "~30g protein",
        "lunch": "40-50g protein",
        "dinner": "30-40g protein",
        "snacks": "Protein-rich support"
    }

def calculate_bmi(weight, height):
    """Calculate Body Mass Index"""
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 1)

def get_bmi_category(bmi):
    """Get BMI category"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"
