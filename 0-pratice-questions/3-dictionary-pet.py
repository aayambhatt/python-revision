pet_list = ["dog", "cat", "cat", "dog", "rabbit", "cat", "hamster"]

pet_count = {}

for pet in pet_list:
    if pet in pet_count:
        pet_count[pet] += 1  # Already counted before, so add 1
    else:
        pet_count[pet] = 1   # First time seeing this pet

print(pet_count)
