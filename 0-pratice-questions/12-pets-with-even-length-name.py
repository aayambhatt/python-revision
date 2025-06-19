def count_even_length_names(pet_list: list) -> int:
    count = 0
    for pet in pet_list:
        if len(pet)%2==0:
            count+=1
    
    return count

pet_list = ["dog", "cat", "hamster", "rabbit", "owl", "parrot"]
print(count_even_length_names(pet_list))

