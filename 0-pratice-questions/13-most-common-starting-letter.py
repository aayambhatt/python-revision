def most_common_starting_letter(pet_list: list) -> str:
    # empty dictionary to store counts
    letter_count = {}

    # loop through the pet list
    for pet in pet_list:
        first_letter = pet[0]
        if first_letter in letter_count:
            letter_count[first_letter]+=1
        else:
            letter_count[first_letter]=1
    
    max_letter = None
    max_count = 0

    for letter, count in letter_count.items():
        if count > max_count:
            max_count = count
            max_letter = letter

    return max_letter

pet_list = ["dog", "cat", "hamster", "hedgehog", "rabbit", "parrot", "horse", "dove"]
print(most_common_starting_letter(pet_list))  # Output: 'h'





