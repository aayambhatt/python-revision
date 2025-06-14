def group_pets_by_letter(pet_list: list) -> dict:
    result = {}
    for pet in pet_list:
        first_letter = pet[0]
        if first_letter in result:
            result[first_letter].append(pet)
        else:
            result[first_letter] = [pet]    

    return result

pet_list = ["dog", "cat", "hamster", "hedgehog", "rabbit", "deer"]
print(group_pets_by_letter(pet_list))