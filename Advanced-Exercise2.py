# -------------------------------------------
# Advanced Python Challenge: Exercise 02 Operators and Conditionals
# -------------------------------------------

# Overview:
# This exercise challenges your understanding of Python operators, conditionals, and input handling.
# Complete each section with the required logic, using good variable names and adding comments where necessary.

# -------------------------------------------
# Question 1: Multi-Step Arithmetic Operations
# -------------------------------------------

# Task:
# Use compound arithmetic operators to modify values of a, b, and c.
# Then calculate the square root of the sum of their squares.
# Tip: Use the math module.

import math

# Start with some base values
a = 5
b = 10
c = 7

# TODO: Add 3 to a using +=
a += 3
# TODO: Multiply b by 2 using *=
b *= 2
# TODO: Modulo c by 4 using %=
c %= 4

# TODO: Calculate the square root of (a^2 + b^2 + c^2)
# had root as root = input (a ** 2 + b ** 2) till it didnt work
root = math.sqrt((a ** 2) + (b ** 2) + (c ** 2))
# TODO: Print the final result rounded to 2 decimal places
rounded_result = round(root, 2 )
print("The result is:", rounded_result)

# -------------------------------------------
# Question 2: Complex Conditional Evaluation
# -------------------------------------------

# Task:
# Ask the user to input three integers (x, y, z).
# Then evaluate and print whether:
# - x is even
# - y is positive
# - z is between 10 and 50
# Use logical operators to combine the conditions.

# Tip: Use and/or to join conditions.

# TODO: Input x, y, z
x = int(input("place a value for x:  "))
y = int(input("place a value for y:  "))
z = int(input("place a value for z:  "))
# TODO: Create conditions:
#   is_even = True if x is even
#   is_positive = True if y > 0
#   is_in_range = True if z between 10 and 50
is_even = (x % 2 == 0)
is_positive = (y > 0)
is_in_range = (10 <= z <= 50)

# TODO: Create final_condition = is_even and is_positive and is_in_range
final_condition = is_even and is_positive and is_in_range
# TODO: Print final_condition
print("are all condition met?", final_condition)

# -------------------------------------------
# Question 3: Grading with Adjustments
# -------------------------------------------

# Task:
# Ask the user for their base score, then apply:
# - bonus points (+5)
# - late penalty (-10)
# Final score must not exceed 100 or drop below 0.
# Then assign a Grade.

# Tip: Use min() and max() to constrain the score.

# TODO: Input score from user
score = int(input("give score: "))
# TODO: Apply adjustments
# guessing you mean adding an addtion
score = score + 5 - 10
# TODO: Clamp score between 0 and 100
score = min(0, max(100,score))
# TODO: Use if-elif-else to determine Grade and print it
if score>= 90:
    Grade= "A"
elif  score>= 80:
    Grade= "B"
elif  score>= 70:
    Grade= "C"
elif  score>= 60:
    Grade= "D"
elif score>= 50:
    Grade= "E"
else:
    Grade= "F"

print ("Grade: ", Grade)


# -------------------------------------------
# Question 4: Advanced Calculator
# -------------------------------------------

# Task:
# Ask the user to input two numbers and an operation (+, -, *, /, %, **).
# Handle division/modulus by zero with error checking.
# Perform the operation and print the result.

# Tip: Use try-except and elif branches for each operation.

# TODO: Input num1, num2
num1 = float(input("enter number first number: "))
num2 = float(input("enter number second number: "))
# TODO: Input operation
operation = input("Enter an operation (+, -, *, /): ")
# TODO: Match operation using if-elif
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
     result= num1 / num2
# TODO: Handle division/modulus by zero with try-except
if num2 == 0:
        print("Error: Division by zero is not allowed.")
else:
     result = num1 / num2

if operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
       result = num1 / num2
       print("The result is: " ,result)

   
# TODO: Print result
print (result)