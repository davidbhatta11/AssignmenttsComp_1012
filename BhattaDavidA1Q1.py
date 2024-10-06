"""BhattaDavidA0Q1
COMP 1012 SECTION A03
INSTRUCTOR [Connor Hryhoruk]
ASSIGNMENT: A1 Question 1
AUTHOR [David Bhatta]
VERSION [2014-Sep-20]
PURPOSE: To check if the numbers provided by the user is perfect number 
"""
import math 
number = int(input("Enter how many numbers you want to test: "))  

count =1
while count<=number :

    test_number=int(input(f'Enter number {count } to test: '))      #asking user to input the test numbers 

    square_root= math.sqrt(test_number)                             #finding the sqaure root of the number 
    

    if int(square_root)**2 == test_number:                          
        print(f"{test_number} is a perfect square number ")
    else:
        print(f"{test_number } is not a perfect square number ")
    count +=1
print("program terminated")

   
