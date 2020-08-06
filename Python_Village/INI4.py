# Program Description
# 
# Given two positive integers "a" and "b", where a < b < 10,000, 
# you need to return the sum of all odd integers from a to b, inclusive.

# Implementation Design:
# 
# I will implement the solution as follows:
# Iterate from a to b inclusive and sum together all of the odd integers.

int_sum = 0;
a = input("Enter the value of 'a': ")
b = input("Enter the value of 'b': ")
a = int(a)
b = int(b)

for i in range(a,b+1):
    if i % 2 == 1:
        int_sum += i

print(f"The sum is: {int_sum}")