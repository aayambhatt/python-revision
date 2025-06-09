fav_food = ["fries", "pizza", "tacos", "sandwich", "garlic bread", "burger"]

food_count = 0

for food in fav_food:
    if "a" in food:
        food_count+=1
        print(f"Found 'a' in: {food} ")

print(f"{food_count} of your fav food contains letter 'a' ")



