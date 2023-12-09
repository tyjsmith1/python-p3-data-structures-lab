spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_names = [food["name"] for food in spicy_foods]
    return food_names

def get_spiciest_foods(spicy_foods):
    spiciest_food = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_food

def print_spicy_foods(spicy_foods):
    emoji = "🌶"
    formatted = ""
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = emoji * food["heat_level"]
        formatted += f"{name} ({cuisine}) | Heat Level: {heat_level}\n"
    print(formatted.strip()) 

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    emoji = "🌶"
    formatted = ""
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = emoji * food["heat_level"]
            formatted += f"{name} ({cuisine}) | Heat Level: {heat_level}\n"
    print(formatted.strip())

def get_average_heat_level(spicy_foods):
    total_heat = 0
    num_foods = len(spicy_foods)
    for food in spicy_foods:
        total_heat += food["heat_level"]
    if num_foods > 0:
        average_spice = total_heat / num_foods
    else:
        average_spice = 0
    return average_spice

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
