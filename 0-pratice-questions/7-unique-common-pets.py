def unique_common_pets(pet_list1: list, pet_list2: list) -> set:
    set1 = set()
    for pet in pet_list1:
        set1.add(pet)
    
    set2 = set()
    for pet in pet_list2:
        set2.add(pet)
        
    return set1.intersection(set2)

pet_list1 = ["dog", "cat", "hamster", "parrot"]
pet_list2 = ["cat", "hamster", "rabbit", "dog", "cat"]

print(unique_common_pets(pet_list1, pet_list2))
