"""BhattaDavidA1Q1
Comp 1012 Section A03 
Connor Hryhoruk
ASSIGNMNET; A0 Q1 
DAVID BHATTA 
2024-09-23

PURPOSE ; to  find a number is a perfect square number or not 
"""
import math 
number = int(input("Enter how many numbers you want to test: "))

count =1
while count<=number :

    test_number=int(input(f'Enter number {count} to test: '))
    count +=1
    square_root= math.sqrt(test_number)


if int(square_root)**2 == test_number:
    print(f"{test_number} is a perfect square number ")
else:
    print(f"{test_number } is not a perfect square number ")

print("program terminated")

   
