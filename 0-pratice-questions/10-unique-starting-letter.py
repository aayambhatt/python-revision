def unique_starting_letter_pets(pet_list: list) -> list:
    letter_count = {}
    # count how many pets start with each letter
    for pet in pet_list:
        first_letter = pet[0]
        if first_letter in letter_count:
            letter_count[first_letter]+=1
        else:
            letter_count[first_letter]=1
    
    # build the result list
    result = []
    for pet in pet_list:
        first_letter = pet[0]
        if letter_count[first_letter]==1:
            result.append(pet)
    
    return result

pet_list = ["dog", "cat", "hamster", "parrot", "dove", "hedgehog"]
print(unique_starting_letter_pets(pet_list))


