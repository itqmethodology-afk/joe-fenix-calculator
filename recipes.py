"""
Joe Fenix Signature Recipes
From "The Anti-Inflammatory High Protein Meal Prep Cookbook" (2026)
"""

RECIPES = {
    "quinoa_spinach_frittata": {
        "name": "Quinoa & Spinach Frittata",
        "servings": 4,
        "prep_time": "10 min",
        "cook_time": "25 min",
        "protein_per_serving": 18,
        "calories_per_serving": 220,
        "diet": ["omnivore", "vegetarian"],
        "ingredients": [
            "6 large eggs",
            "1 cup cooked quinoa",
            "2 cups fresh spinach",
            "1/2 cup feta cheese",
            "1/4 cup milk",
            "2 tbsp olive oil",
            "Salt and pepper to taste"
        ],
        "instructions": [
            "Preheat oven to 180°C (350°F)",
            "Sauté spinach in olive oil until wilted",
            "Whisk eggs with milk, salt, and pepper",
            "Mix in quinoa, spinach, and feta",
            "Pour into greased baking dish",
            "Bake for 25 minutes until set",
            "Cool and portion into 4 servings"
        ]
    },
    "blueberry_almond_pancakes": {
        "name": "Blueberry Pancakes with Almond Flour",
        "servings": 4,
        "prep_time": "5 min",
        "cook_time": "15 min",
        "protein_per_serving": 12,
        "calories_per_serving": 180,
        "diet": ["omnivore", "vegetarian"],
        "ingredients": [
            "1 cup almond flour",
            "2 large eggs",
            "1/4 cup milk",
            "1/2 cup fresh blueberries",
            "1 tsp baking powder",
            "1 tsp vanilla extract",
            "Pinch of salt"
        ],
        "instructions": [
            "Mix almond flour, baking powder, and salt",
            "Whisk eggs, milk, and vanilla in separate bowl",
            "Combine wet and dry ingredients",
            "Fold in blueberries gently",
            "Cook on medium heat, 2-3 min per side",
            "Makes 8 pancakes (2 per serving)"
        ]
    },
    "greek_yogurt_bowl": {
        "name": "Greek Yogurt Bowl with Nuts & Chia",
        "servings": 1,
        "prep_time": "5 min",
        "cook_time": "0 min",
        "protein_per_serving": 20,
        "calories_per_serving": 280,
        "diet": ["omnivore", "vegetarian"],
        "ingredients": [
            "200g Greek yogurt (plain, full-fat)",
            "1 tbsp chia seeds",
            "2 tbsp mixed nuts (walnuts, almonds)",
            "1/2 cup mixed berries",
            "1 tsp honey (optional)",
            "Cinnamon to taste"
        ],
        "instructions": [
            "Place Greek yogurt in bowl",
            "Top with chia seeds and nuts",
            "Add fresh berries",
            "Drizzle with honey if desired",
            "Sprinkle cinnamon",
            "Serve immediately"
        ]
    }
}

def get_recipe(recipe_id):
    """Get recipe by ID"""
    return RECIPES.get(recipe_id)

def get_all_recipes():
    """Get all recipes"""
    return RECIPES

def filter_recipes_by_diet(diet_preference):
    """Filter recipes by dietary preference"""
    filtered = {}
    for recipe_id, recipe in RECIPES.items():
        if diet_preference.lower() in recipe["diet"]:
            filtered[recipe_id] = recipe
    return filtered
