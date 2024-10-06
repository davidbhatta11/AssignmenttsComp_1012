"""BhattaDavidA1Q2
COMP 1012 SECTION A03
INSTRUCTOR [Connor Hryhoruk]
ASSIGNMENT: A1 Question 2
AUTHOR [David Bhatta]
VERSION [2024-Sep-20]

PURPOSE ; 
The total speaking time (in seconds, up to 2 decimals).
 The total and average (up to 2 decimals) character count
 The total weight of all entered words
 The number of words entered with no vowels
 The number of words with an even length (excluding length of 0)
 The number of words that were a Lipogram
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

total_lipogram_count=0


print("My choosen word are as follows:\nPie with a weight of 2\nCookie with a weight of 3\nMy choosen bad luck letter is: t\n")


some_text=input("please enter some text or type esc to exit: ").lower().strip()

while some_text !="esc":
    
    space_index = some_text.find(' ')  # Finding  the index of the first space
    if space_index==-1:
        first_word=some_text
    else:
        first_word = some_text[0:space_index]  # Get the text up to the first space
   

    index=0
    contain_lipogram=False
    count_lipogram=0
    while index < len(first_word):            #to check for the each character of the word if it contain the bad luck letter   
        char_1 = first_word[index]              #first the value of index will be zero and goes upto the lenght of word provied by user 
        if char_1 == bad_luck:
            contain_lipogram=True
        index += 1

    if contain_lipogram:
        total_lipogram_count+=1

    cleaned_word=first_word.replace("t","")             # to remove the badluck letter for the word 
    print(f'the word provided by the user:{cleaned_word}')
    


    
    
    lenght=(len(cleaned_word))
    total_word_count +=lenght      #total word
    valid_input +=1             #how many time the user input until the esc 

    
    if cleaned_word=="pie":
        weight = Pie

    elif cleaned_word=="cookie":
        weight =Cookie

    else:
        weight = 1
    
    total_weight +=weight          #calculate the total weight 

    index_1=0
    contain_vowels=False
    while index_1<len(cleaned_word):         #to check for the each character of the word if it contains  vowels or not
        char=first_word[index_1]           #here first index_1=0 and goes upto to the length of the word 

        if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':    #check each and every word if it's vowel
            contain_vowels=True

    
        index_1+=1                                      #after checking for the one word goes up again 
    print(contain_vowels)

    if not contain_vowels:              #count if the word doesnot contains vowels 
        count_no_vowels+=1

    

    if len(cleaned_word)%2==0:             #to check if the word has even length
        count_even +=1

    some_text=input("please enter some text or type esc to exit : ").lower().strip()  # loop ending condition


average_count=(total_word_count)/valid_input                 #total soeaking time ie total word character divide by total valid input given by the user 
speaking_time = (valid_input/180)*60                        #speaking time per second 


print("~~ program summary~~")
print(f'speaking time per second:{speaking_time:.2f}s')
print(f'total character count:{total_word_count}')
print(f'average character count:{average_count:.2f}')
print(f"the total weight of the words is {total_weight}")
print(f'number of words with no vowels:{count_no_vowels} ')
print(f'number of words with even lenght:{count_even} ')
print(f'number of words containing lipogram:{total_lipogram_count} ')
print("end of processing")




    


    















