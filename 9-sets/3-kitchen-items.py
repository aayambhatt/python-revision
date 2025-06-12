menu_a = {"pizza", "burger", "pasta"}
menu_b = {"pasta", "burrito", "sushi"}

print("All options:", menu_a.union(menu_b))
print("Common items:", menu_a.intersection(menu_b))
print("A-only items:", menu_a.difference(menu_b))
