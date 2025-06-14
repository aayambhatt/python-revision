def frequent_pets(pet_list: list) -> dict:
    dict1 = {}
    for pet in pet_list:
        if pet in dict1:
            dict1[pet] += 1
        else:
            dict1[pet] = 1
            
    res_dict = {}
    
    for pet, pet_count in dict1.items():
        if pet_count > 1:
            res_dict[pet] = pet_count  
    
    return res_dict

print(frequent_pets(["dog", "cat", "dog", "rabbit", "cat", "cat", "hamster", "dog"]))
