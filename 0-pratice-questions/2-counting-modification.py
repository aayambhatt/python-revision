def count_pets(pet_list, pet_name):
    count = 0
    for pet in pet_list:
        if pet==pet_name:
            count+=1

    return count

pet_list = ["dog", "cat", "cat", "dog", "rabbit", "cat", "hamster"]
print(count_pets(pet_list, "rabbit")) 