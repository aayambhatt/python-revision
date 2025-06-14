def count_unique_pets(pet_list: list) -> int:
    pet_set = set()

    for pet in pet_list:
        pet_set.add(pet)
    
    count = len(pet_set)

    return count

print(count_unique_pets(pet_list = ["dog", "cat", "dog", "rabbit", "cat", "hamster", "dog"]
))

