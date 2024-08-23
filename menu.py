# Activity:  Design a personalized menu using nested dictionaries in Python. Your menu should feature different categories, such as appetizers (apps), main courses, desserts, and beverages. For each item in your menu, include details like price, ingredients, and any other relevant information you think would be helpful.

# Appetizer
    # Samosas - Shafee
        # Price: $3
    # Fries - Jeremy
        # Price: $5
    # Calamari - Ayanna
        # Price: $10
    # Dumpling - Kenneth
# Main Course
# Desserts
# Bev

food_menu = {
    "appetizer": {
        "samosa": {
            "price": 3.00
        },
        "fries": {
            "price": 5.00
        },
        "calamari": {
            "price": 10.00
        },
        "dumplings": {
            "price": 7.50
        }
    },
    "main course": {
        "lasagna": {
            "description": "Type of layered pasta dish"
        },
        "pizza": {
            "description": "A cheesy pie"
        },
        "burger": {
            "description": "It's a burger"
        },
        "paella": {
            "description": "Medley of rice, seafood, sausage, vegetables"
        }
    },
    "desserts": {
        "milkshake": {
            "calories": 400
        },
        "sundae": {
            "calories": 600
        },
        "lava_cake": {
            "calories": 800
        },
        "sorbet": {
            "calories": 200
        }
    },
    "beverages": {
        "mango lassi": {
            "is_vegan": False,
            "ingredients": ['mango', 'yogurt', 'water']
        },
        "thai iced tea": {
            "is_vegan": False,
            "ingredients": ['milk', 'black tea', 'sugar']
        },
        "sugarcane juice": {
            "is_vegan": True,
            "ingredients": ['sugarcane', 'ice']
        },
        "water": {
            "is_vegan": True,
            "ingredients": ['hydrogen^2', 'oxygen']
        }
    }
}
