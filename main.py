# Task1
number = int(input("Enter a number: "))
if number > 7:
    print("Hello")

# Task2
name = input("Enter a name: ")
if name == "John":
    print("Hello, John")
else:
    print("There is no such name")

# Task3
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Numbers are multiples of 3:")
for n in numbers:
    if n % 3 == 0:
        print(n)

"""
Given bracket sequence: [((())()(())]] 

Can this sequence be considered correct? 
No, this sequence is incorrect.

Rationale: 
1.The closing order is broken: the square bracket is closed before all the round brackets.
2.The balance of parentheses is broken (extra ]).

to make this sequence correct:
1.The number of opening and closing parentheses is the same.
2.Each closing parenthesis corresponds to the last open one.

Corrected version:
[((())()(()))]
"""