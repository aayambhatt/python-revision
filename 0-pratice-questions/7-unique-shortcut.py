def unique_common_pets(pet_list1: list, pet_list2: list) -> set:
    set1 = set(pet_list1)
    set2 = set(pet_list2)
    return set1 & set2  # or set1.intersection(set2)
