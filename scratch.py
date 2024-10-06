"""BhattaDavidA1Q1
Comp 1012 Section A03 
Connor Hryhoruk
ASSIGNMNET; A0 Q1 
DAVID BHATTA 
2024-09-23

PURPOSE ; to  find a number is a perfect square number or not 
"""

Pie = 2 
Cookie = 3 
bad_luck = "t"
total_weight = 0
total_count = 0
valid_input=0
count_even=0
count_lipogram=0
count_no_vowels=0


print("My choosen word are as follows:\nPie with a weight of 2\nCookie with a weight of 3\nMy choosen bad luck letter is: t\n")


some_text=input("please enter some text or type esc to exit :").lower().split()[0].strip()




while some_text != "esc":
    print(f'the word provided by the user:{some_text}')

    lenght=(len(some_text))
    total_count +=lenght
    valid_input +=1

    
    if some_text=="pie":
        weight = Pie

    elif some_text=="cookie":
        weight =Cookie

    else:
        weight = 1
    
    total_weight +=weight

    index=0
    contain_vowels=False


    while index<len(some_text):
        char=some_text[index]

        if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
            contain_vowels=True

       
        index +=1
    print(contain_vowels)

    if not contain_vowels:
        count_no_vowels+=1

    if len(some_text)%2==0:
        count_even +=1

   




    

    some_text=input("please enter some text or type esc to exit : ").lower().replace(bad_luck,'').split()[0].strip()

   

average_count=(total_count)/valid_input
speaking_time = (valid_input/180)*60

print("~~ program summary~~")
print(f'speaking time per second:{speaking_time:.2f}s')
print(f"the total weight of the words is {total_weight}")
print(f'total character count:{total_count}')
print(f'average character count:{average_count:.2f}')
print(f'number of words with even lenght:{count_even} ')
print(f'number of words with no vowels:{count_no_vowels} ')
print(f'number of lipogram:{count_lipogram} ')

print("end of processing")



    
        
    
    
     


    










   

   