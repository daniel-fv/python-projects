# Largest number in a list
greater_number = 0

my_list = [5, 60, 20, 50]
for item in my_list:
    if item > greater_number:
        greater_number = item
print(f'Highest number is {greater_number}')
