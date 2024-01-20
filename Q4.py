your_choice_dishes = {
    'Spaghetti Bolognese',
    'Chicken Alfredo',
    'Margherita Pizza',
    'Caesar Salad',
    'Chocolate Cake'
}

dishes_cooked_in_week = {
    'Spaghetti Bolognese',
    'Chicken Alfredo',
    'Margherita Pizza',
    'Greek Salad',
    'Fruit Salad',
    'Chocolate Cake'
}

dishes_to_be_cooked = your_choice_dishes.intersection(dishes_cooked_in_week)

print("Dishes to be cooked in the next week based on your choice:")
for dish in dishes_to_be_cooked:
    print(f"- {dish}")
    
    
