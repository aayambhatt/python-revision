def pets_in_either_but_not_both(pet_list1: list, pet_list2: list) -> list:
    unique1 = set(pet_list1) - set(pet_list2)
    unique2 = set(pet_list2) - set(pet_list1)

    total_unique = unique1 | unique2

    return list(total_unique)


pet_list1 = ["dog", "cat", "hamster"]
pet_list2 = ["cat", "rabbit", "hamster", "parrot"]

print(pets_in_either_but_not_both(pet_list1, pet_list2))

