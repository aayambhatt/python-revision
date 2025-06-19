def group_by_length(pet_list: list) -> dict:
    result = {}

    for pet in pet_list:
        length = len(pet)

        if length in result:
            result[length].append(pet)
        else:
            result[length] = [pet]

    return result

pet_list = ["dog", "cat", "hamster", "parrot", "ant", "bat", "cow", "snake"]
print(group_by_length(pet_list))
