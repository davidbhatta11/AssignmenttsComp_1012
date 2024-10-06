text=input("enter some text or quit ")
while text != "quit":
    space_index= text.find(" ")
    second_index= text.find(" ",space_index+1)
    second_word = text[space_index+1:second_index]
    text=input("enter some text or quit ")
print(second_word)