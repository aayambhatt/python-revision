list = [2,3,6,6,5]

max_so_far = float("-inf")

for item in list:
    if item>max_so_far:
        max_so_far=item

filtered_list = []

for item in list:
    if item!=max_so_far:
        filtered_list.append(item)

second_max_so_far = float("-inf")

for item in filtered_list:
    if item>second_max_so_far:
        second_max_so_far=item

print(second_max_so_far)






