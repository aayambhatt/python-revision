def count_cats(pet_list):
    count = 0
    for pet in pet_list:
        if pet=="cat":
            count+=1

    return count

pet_list = ["dog", "cat", "cat", "dog", "rabbit", "cat", "hamster"]
print(count_cats(pet_list))
