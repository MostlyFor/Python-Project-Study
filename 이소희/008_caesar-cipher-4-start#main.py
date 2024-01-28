import myart
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"

def caesar(start_text, shift_amount, cipher_direction):
  start_list = list(start_text)
  end_list = []
  if cipher_direction == "decode":
    shift_amount = - shift_amount
  for n in start_list:
    if n in alphabet:
      position = shift_amount
      position = (position + alphabet.index(n) + 1 ) % len(alphabet) - 1
      end_list += alphabet[position]
    else:
      end_list += n
  end_text = "".join(end_list)
  print(end_text)

print(myart.logo)
#caesar("hello abc * xyz", 52, "encode")  
#caesar("mjqqt fgh * cde", 52, "decode")
  
#print(f"Here's the {cipher_direction}d result: {end_text}")


#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

game_on = "yes"

while game_on == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  game_on = input("Do you want to continue? Type 'yes' or 'no'\n").lower()
