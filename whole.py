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
total_word_count = 0
valid_input=0
count_even=0
count_vowels=0
count_no_vowels=0
contain_lipogram=False
total_lipogram_count=0


print("My choosen word are as follows:\nPie with a weight of 2\nCookie with a weight of 3\nMy choosen bad luck letter is: t\n")


some_text=input("please enter some text or type esc to exit :").lower().split()[0].strip()
index = 0
while some_text !="esc":
    index=0
    count_lipogram=0
    while index < len(some_text):
        char_1 = some_text[index]
        if char_1 == "t":
            contain_lipogram=True
            count_lipogram += 1 
            break 
        index += 1

    
    total_lipogram_count+=count_lipogram
    



    
    print(f'the word provided by the user:{some_text.replace(bad_luck,"")}')

    lenght=(len(some_text))
    total_word_count +=lenght        #total word
    valid_input +=1             #how many time the user input

    
    if some_text=="pie":
        weight = Pie

    elif some_text=="cookie":
        weight =Cookie

    else:
        weight = 1
    
    total_weight +=weight          #calculate the total weight at last 

    index_1=0
    contain_vowels=False


    while index_1<len(some_text):         #to check for the each character of the word if it is vowels or not using the index method 
        char=some_text[index_1]           #here first index_1=0 and goes upto to the length of the word 

        if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':    #check each and every word if it's vowel
            contain_vowels=True

    
        index_1+=1                                      #after checking for teh one word goes up again 
    print(contain_vowels)

    if not contain_vowels:              #count if the word doesnot contains vowels 
        count_no_vowels+=1

    

    if len(some_text.replace(bad_luck,""))%2==0:             #to check if the word has even length
        count_even +=1

    some_text=input("please enter some text or type esc to exit : ").lower().split()[0].strip()  # loop ending condition


average_count=(total_word_count)/valid_input                 #total soeaking time ie total word character divide by total valid input given by the user 
speaking_time = (valid_input/180)*60                        #speaking time per second 


print("~~ program summary~~")
print(f'speaking time per second:{speaking_time:.2f}s')
print(f"the total weight of the words is {total_weight}")
print(f'total character count:{total_word_count}')
print(f'average character count:{average_count:.2f}')
print(f'number of words with even lenght:{count_even} ')
print(f'number of words with no vowels:{count_no_vowels} ')
print(f'number of words with vowels:{count_vowels} ')
print(f'number of words containing lipogram:{total_lipogram_count} ')
print("end of processing")




    


    















