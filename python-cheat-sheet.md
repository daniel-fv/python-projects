## Python Cheat Sheet

## Input / Output
```python
name = input("What's your name? ")
print("Your name is " + name)
```

## Variables
```python
a = 1       # integer
b = 1.1     # float
c = 1 + 2j  # complex number (a + bi)
d = “a”     # string
e = True    # boolean (True / False)
```

## Strings
```python
x = “Python”
len(x)      # 6
x[0]        # P
x[-1]       # n
x[0:3]      # Pyt
x[:]        # Python
x[1:-1]     # ytho

print("This is text combined with the ", x, " value")

# String concatenation
name = first + ' ' + last
 
# Formatted strings
name = f"{first} {last}"
 
# Escape sequences
\” \’ \\ \n
 
# String methods
x.upper()
x.lower()
x.title()
x.strip()
x.find(“p”)
x.replace(“a”, “b”)
"a" in x       # boolean, is "a" in the variable x?
```
## Type Conversion
```python
int(x)  
float(x) 
bool(x) 
string(x)
```
## Arithmetic Operations
```python
10 + 3      # 13
10 - 3      # 7
10 / 3      # 3.333 (floating point)
10 // 3     # 3  (integer)
10 % 3      # 1 (remainder)
10 ** 3     # 1000 (exponent 10^3)

# Augmented assignment operation
x += 3      # the same as x = x + 3 

```
## Operator Precedence
Order of operations

    1- Parenthesis
    2- Exponentiation: 2 ** 3
    3- Multiplication or division
    4- Addition or subtraction

```python
x = 10 + 3 * 2          # 16 (3 * 2 then + 10)
x = (10 + 3) * 2 ** 2   # 52 (10 + 3 then 2 ** 2 then * 2)
x = (2 + 3) * 10 - 3    # 47 (2 + 3 then * 10 then - 3)
```

## False Values
```python
0
“”
[]
```
## Math Functions
```python
x = -2.9
round(x)        # -3
abs(x)          # 2.9 (absolute value)

# Math module
import math
math.ceil(2.9)  # 3 (ceiling)
math.floor(2.9) # 2 (floor)
```
More on the math module https://docs.python.org/3/library/math.html

## Conditional statements
```python
if x == 1:  
    print(“a”)
elif x == 2:  
    print(“b”)
else:   
    print(“c”)

# Logical operators
# AND: both conditions have to be true
# OR: at least one condition has to be true
# NOT: reverses the condition
if x == 1 and y == 2

if has_good_credit and not has_criminal_record:
    print("Eligible for loan)

# Ternary operator 
x = “a” if n > 1 else “b”
 
# Chaining comparison operators
if 18 <= age < 65:
```

## Loops
```python
# For loops
for n in range(1, 10, 1): # using the range function
    print(n)

for item in 'Python':   
    print(item)     # P y t h o n

for item in ['This', 'is', 'a', 'list', 'of', 'strings']:
    print(item)

# While loops
while n < 10: 
    print(n)
    n += 1
else:
    print('loop ended')  # this is executed after the loop ends

```

## Lists
```python
names = ['John', 'Bob', 'Daniel', 'Sarah', 'Mary']
print(names)       # ['John', 'Bob', 'Daniel', 'Sarah', 'Mary']
print(names[2])     # Daniel
print(names[-1])    # Mary
print(names[2:])    # ['Daniel', 'Sarah', 'Mary']
names[0] = 'Jon'
```

## 2D Lists
```python
# List within a list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0]       # [1, 2, 3]
matrix[0][1]    # 2

# Print each item of a 2D list
for row in matrix:      # for every list in matrix
    for item in row:    # for every item in each list
        print(item)
```
## List methods
```python
numbers = [5, 2, 1, 7, 4]
numbers.append(1)           # adds value at the end of the list
numbers.insert(0, 10)       # inserts 10 at the 0 position
numbers.remove(5)           # removes the 5th item
numbers.clear()             # empties the list
numbers.pop()               # removes the last item on the list
numbers.index(5)            # finds the first occurrence of the value   
5 in numbers                # checks if the number 5 is on the list 
numbers.count(5)            # count the times the number 5 is on the list   
numbers.sort()              # sorts the list in ascending order
numbers.reverse()           # sorts the list in descending order
numbers2 = numbers.copy()   # copies the list to another list

```


## About this cheat sheet

**Colaborators**

    1- Daniel Fajardo Valenti
 
This cheat sheet is inspired by the [Programming with Mosh Python Tutorial on Youtube](https://programmingwithmosh.com/python/python-3-cheat-sheet/)