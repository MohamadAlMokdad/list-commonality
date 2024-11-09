# Define three lists
list1 = [2, 4, 6, 8, 10]
list2 = [4, 6, 8, 12, 14]
list3 = [0, 4, 6, 8, 16]

# Initialize an empty list to store common elements
list4 = []

# Triple nested loop to iterate through all elements of the three lists
for i in range(len(list1)):  # Iterate through the first list
    for j in range(len(list2)):  # Iterate through the second list
        for k in range(len(list3)):  # Iterate through the third list
            # Check if the current element in all three lists are the same
            if list1[i] == list2[j] == list3[k]:
                # If they are equal, append the value to the result list (list4)
                list4.append(list1[i])

# Print the result list containing the common elements found in all three lists
print(list4)
