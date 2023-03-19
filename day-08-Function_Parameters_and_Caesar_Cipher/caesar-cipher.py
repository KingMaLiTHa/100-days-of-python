alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

newalphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)




#TODO-3: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(plain_text,shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount

        #? METHOD 01
        if new_position>26:
            new_position = new_position - 26

        #? METHOD 02
        # new_position = new_position % 25

        #? METHOD 03
         #index function outputs on first result, without searching for second result.So, instead of above method, we can duplicate the alphabet list and get relevant results.
        # cipher_text += newalphabet[new_position]

        cipher_text += alphabet[new_position]
    print(f'Your encoded message: {cipher_text}')

#TODO-4:Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

def decrypt(cipher_text,shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f'Your decoded message: {plain_text}')

#TODO-5:Combine the encrypt() and decrypt() functions into a single function called caesar()

def caesar(start_text, shift_amount, cipher_direction):
    end_text= ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        #TODO-6: What happens if the user enters a number/symbol/space?
        if char in newalphabet:
            position= newalphabet.index(char)
            new_position = position + shift_amount
            end_text += newalphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")
 

# Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)
# else:
#     print("Wrong Input")

#TODO-4: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

restart= True
while(restart): 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    shift= shift % 25
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    #TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?

    restart = input("Do you want to restart the cipher program? Type 'yes' or 'no':\n")
    if restart == "yes":
        restart = True
    else:
        restart = False
        print("Good Bye!")


