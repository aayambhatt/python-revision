list1 = [3, 3, 4, 5, 6, 7, 9, 6, 10]
list2 = [10, 44, 55, 1, 2, 88, 9, 6, 20]

# Create a dictionary to count occurrences of each number in list1
count_dict = {}

for num in list1:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

# Check and print how many times each number from list2 appears in list1
for num in list2:
    count = count_dict.get(num, 0)  # Returns 0 if num not found in count_dict
    print(f"{num} appears {count} time(s) in list1")
