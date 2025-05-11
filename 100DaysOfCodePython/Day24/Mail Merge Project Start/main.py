#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open('./Input/Letters/starting_letter.txt', mode='r+') as starting_letter:
    letter = starting_letter.readlines()

with open('./Input/Names/invited_names.txt') as invited_names:
    names = invited_names.readlines()
    
for name in names:
    name = name.strip()
    first_line = letter[0].replace("[name]", name)
    with open(f'./Output/ReadyToSend/letter_to_{name}', mode='w') as output_file:
        output_file.write(first_line)
        for line in letter[1:]:
            output_file.write(line)



    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: This method will help you: https://www.w3schools.com/python/ref_string_strip.asp