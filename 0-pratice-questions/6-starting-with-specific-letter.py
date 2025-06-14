def pets_starting_with(pet_list: list, letter: str) -> list:
    result = []
    
    for pet in pet_list:
        if pet[0]==letter:
             result.append(pet)
       
    
    return result

pet_list = ["dog", "cat", "hamster", "hedgehog", "rabbit"]
print(pets_starting_with(pet_list, "h"))

