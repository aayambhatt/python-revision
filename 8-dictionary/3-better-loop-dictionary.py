pet = {
    "name": "Tofu",
    "age": 4,
    "type": "dog",
    "color": "white"
}

for key, value in pet.items():
    print(f"{key}: {value}")



for key in pet.keys():
    print(f"{key}")
for value in pet.values():
    print(f"{value}")

sentence = f"{pet['name']} is a {pet['age']} year old {pet['color']} {pet['type']}."
print(sentence)
