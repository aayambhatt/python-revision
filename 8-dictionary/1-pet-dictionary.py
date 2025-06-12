pet = {
    "name": "Tofu",
    "age": 4,
    "type": "dog",
    "color": "white"
}

print(pet["name"])  # Should print: Tofu
print(pet["age"])   # Should print: 4
print(pet["type"])  # Should print: Dog
print(pet["color"])

pet["age"]+=1 # age increased
pet["fav_food"] = "bread & milk"

print(pet)
