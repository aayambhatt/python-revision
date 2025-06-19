def pets_with_most_vowels(pet_list: list) -> list:
    vowel_count = {}
    vowels = ['a', 'e', 'i', 'o', 'u']

    for pet in pet_list:
        count = 0
        for letter in pet: # Loop through each letter in the name
            if letter in vowels:
                count+=1  # Count vowels
        vowel_count[pet] = count # Store the pet name and its vowel count
    
    # max vowel count
    max_vowel_count = max(vowel_count.values())

    # Return all pet names that match the max vowel count
    result = []
    for pet, count in vowel_count.items():
        if count == max_vowel_count:
            result.append(pet)

    return result

pet_list = ["dog", "cat", "hamster", "iguana", "eel", "octopuus"]
print(pets_with_most_vowels(pet_list))
# Output: ['iguana', 'octopus']

   

