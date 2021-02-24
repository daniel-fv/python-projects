numbers = [5, 2, 1, 5, 7, 4]

count = 0
duplicate_pos = 0
current_value = 0

while count <= numbers.:
    current_value = numbers[count]

    # Do we have duplicates?
    if numbers.count(current_value) > 1:
        pos_to_delete = numbers.index(current_value)
        numbers.remove(pos_to_delete)


# numbers.append(1)           # adds value at the end of the list
# numbers.insert(0, 10)       # inserts 10 at the 0 position
# numbers.remove(5)           # removes the 5th item
# numbers.clear()             # empties the list
# numbers.pop()               # removes the last item on the list
# numbers.index(5)            # finds the first occurrence of the value
# 5 in numbers                # checks if the number 5 is on the list
# numbers.count(5)            # count the times the number 5 is on the list
# numbers.sort()              # sorts the list in ascending order
# numbers.reverse()           # sorts the list in descending order
# numbers2 = numbers.copy()   # copies the list to another list
