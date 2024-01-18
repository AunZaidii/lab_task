best_dishes_set = set()

num_dishes = int(input("Enter the number of best dishes: "))
for i in range(num_dishes):
    dish_name = input(f"Enter the name of the {i+1}st dish: ")
    best_dishes_set.add(dish_name)

print("Set of best dishes:", best_dishes_set)

while best_dishes_set:
    popped_dish = best_dishes_set.pop()
    print(f"Popped dish: {popped_dish}")
    print(f"Remaining dishes: {best_dishes_set}")

print("Updated set of best dishes:", best_dishes_set)

