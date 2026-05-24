"""
Joe Fenix Meal Prep System
60-minute meal prep instructions and grocery list generation
"""

from recipes import get_all_recipes, filter_recipes_by_diet

def generate_grocery_list(diet_preference="omnivore"):
    """Generate Smart Grocery List based on Joe Fenix Method"""
    
    base_list = {
        "Proteins": [
            "Chicken breast (1kg)",
            "Eggs (12 pack)",
            "Greek yogurt (500g)",
            "Salmon fillets (400g)"
        ],
        "Smart Carbs": [
            "Quinoa (500g)",
            "Oats (500g)",
            "Brown rice (1kg)",
            "Sweet potatoes (1kg)"
        ],
        "Healthy Fats": [
            "Extra virgin olive oil",
            "Mixed nuts (200g)",
            "Avocados (3)",
            "Chia seeds (100g)"
        ],
        "Vegetables": [
            "Broccoli (500g)",
            "Spinach (300g)",
            "Zucchini (4)",
            "Bell peppers (3)",
            "Cherry tomatoes (250g)"
        ],
        "Pantry": [
            "Almond flour (250g)",
            "Feta cheese (200g)",
            "Blueberries (250g)",
            "Mixed berries (300g)",
            "Cinnamon",
            "Vanilla extract"
        ]
    }
    
    if diet_preference.lower() == "vegetarian":
        base_list["Proteins"] = [
            "Eggs (18 pack)",
            "Greek yogurt (1kg)",
            "Cottage cheese (500g)",
            "Tofu (400g)",
            "Lentils (500g)"
        ]
    elif diet_preference.lower() == "vegan":
        base_list["Proteins"] = [
            "Tofu (800g)",
            "Tempeh (400g)",
            "Lentils (500g)",
            "Chickpeas (2 cans)",
            "Plant-based protein powder"
        ]
        base_list["Pantry"].remove("Feta cheese (200g)")
        base_list["Pantry"].append("Nutritional yeast (50g)")
    
    return base_list

def meal_prep_60_minutes():
    """Step-by-step 60-minute meal prep instructions"""
    return {
        "title": "Meal Prep in 60 Minutes",
        "total_time": "60 minutes",
        "steps": [
            {
                "time": "0-15 min",
                "task": "Prep Proteins",
                "instructions": [
                    "Season chicken breasts with olive oil, salt, pepper",
                    "Place in oven at 180°C (350°F)",
                    "Hard boil 6 eggs (12 min timer)",
                    "Portion Greek yogurt into containers"
                ]
            },
            {
                "time": "15-30 min",
                "task": "Cook Carbs",
                "instructions": [
                    "Start quinoa (1 cup dry, 2 cups water, 15 min)",
                    "Prep oats portions for overnight oats",
                    "Check chicken, flip if needed"
                ]
            },
            {
                "time": "30-45 min",
                "task": "Prep Vegetables",
                "instructions": [
                    "Wash and chop broccoli, zucchini, peppers",
                    "Steam broccoli (5 min)",
                    "Sauté spinach with garlic (3 min)",
                    "Store in separate containers"
                ]
            },
            {
                "time": "45-60 min",
                "task": "Portion & Store",
                "instructions": [
                    "Slice cooked chicken into portions",
                    "Peel and portion hard-boiled eggs",
                    "Divide quinoa into 4 containers",
                    "Assemble 4 complete meal containers",
                    "Label with date and contents",
                    "Store in fridge (lasts 5-7 days)"
                ]
            }
        ],
        "result": "7 days of meals ready in 1 hour"
    }

def generate_weekly_plan(macros, diet_preference="omnivore"):
    """Generate 7-day meal plan based on macro targets"""
    
    daily_protein = macros["protein_g"]
    
    # Protein distribution (The Perfect Day)
    breakfast_protein = daily_protein * 0.25  # ~30g
    lunch_protein = daily_protein * 0.40      # ~40-50g
    dinner_protein = daily_protein * 0.30     # ~30-40g
    snack_protein = daily_protein * 0.05      # support
    
    weekly_plan = {
        "daily_target": macros,
        "meal_distribution": {
            "breakfast": f"{round(breakfast_protein)}g protein",
            "lunch": f"{round(lunch_protein)}g protein",
            "dinner": f"{round(dinner_protein)}g protein",
            "snacks": f"{round(snack_protein)}g protein"
        },
        "sample_day": {
            "breakfast": "Greek Yogurt Bowl with Nuts & Chia (20g protein)",
            "lunch": "Grilled Chicken with Quinoa & Broccoli (45g protein)",
            "dinner": "Salmon with Sweet Potato & Spinach (35g protein)",
            "snack": "Hard-boiled eggs (12g protein)"
        },
        "recipes_included": filter_recipes_by_diet(diet_preference)
    }
    
    return weekly_plan

def portion_control_guide():
    """Hand-based portion control - no scale needed"""
    return {
        "protein": "Palm of your hand = 25-30g protein",
        "carbs": "Closed fist = 1 serving (~30g carbs)",
        "fats": "Thumb = 1 serving (~10g fat)",
        "vegetables": "2 open hands = unlimited"
    }
