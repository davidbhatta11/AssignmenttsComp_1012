Pie = 2 
Cookie = 3 
bad_luck = "t"

print("My chosen words are as follows:\nPie with a weight of 2\nCookie with a weight of 3\nMy chosen bad luck letter is: t\n")

some_text0 = input("Please enter some text or esc: ").strip().lower().split()[0]


total_lipogram_count = 0

while some_text0 != "esc":
    print(f'The word provided by the user: {some_text0}')
    
    contain_lipogram = False
    count_lipogram = 0

   
    index = 0
    while index < len(some_text0):
        char_1 = some_text0[index]
        if char_1 == bad_luck:
            contain_lipogram=True
            count_lipogram += 1 
        index += 1
        

    total_lipogram_count += count_lipogram

   
    print(f'Does the word contain lipogram: {contain_lipogram}')
    
   
    some_text0 = input("Please enter some text or esc: ").strip().lower().split()[0]


print("Total number of lipograms found:", total_lipogram_count)
