def most_common_length(pet_list: list) -> int:
    length_count = {}

    #  loop through the pet list and get the length of each name:
    for pet in pet_list:
        length = len(pet)

        if length in length_count:
            length_count[length]+=1
        else:
            length_count[length]=1
    
    # find the length that has the highest count
    max_length = None
    max_count = 0

    for length, count in length_count.items():
        if count>max_count:
            max_count = count
            max_length = length

    return max_length

pet_list = ["dog", "cat", "parrot", "ant", "hamster", "owl", "fox", "bat"]
print(most_common_length(pet_list))  
    

