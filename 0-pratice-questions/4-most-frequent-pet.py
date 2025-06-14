
def most_frequent_pet(pet_list: list) -> str:
    pet_dict = {}
    # count all pets
    for pet in pet_list:
        if pet in pet_dict:
            pet_dict[pet]+=1
        else:
            pet_dict[pet]=1
    
    # find pet with max count
    max_pet = None
    max_count = 0

    for pet, count in pet_dict.items():
        if count > max_count:
            max_count = count
            max_pet=pet
    
    return max_pet

pet_list = ["dog", "cat", "dog", "rabbit", "cat", "cat", "dog", "dog"]
print(most_frequent_pet(pet_list))

        
        

    
