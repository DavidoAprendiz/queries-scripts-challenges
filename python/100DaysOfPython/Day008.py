# Day 08 - Caesar Cipher

def caesar(message, shift, choice):
    result: str = ""
    if choice == "encode":
        for l in message:
            if alphabet.index(l) + shift < len(alphabet):
                position = alphabet.index(l) + shift
                result += alphabet[position]
            else:
                position = alphabet.index("a") + (shift - 1)
                result += alphabet[position]
        print(f"Here's the encoded result: {result}")
    elif choice == "decode":
        for l in message:
            position = alphabet.index(l) - shift
            result += alphabet[position]
        return print(f"Here's the decoded result: {result}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
run_program: str = "yes"


while run_program != "no":
    user_choice: str = input("Type 'encode' to encrypt, type 'decode' do decrypt\n").lower()
    user_message: str = input("Type your message:\n").lower()
    shift_number: int = int(input("Type the shift number:"))

    caesar(message=user_message, choice=user_choice, shift=shift_number)
    run_program = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()



import math


# Exercise 1
def paint_calc(height: int, width: int, cover: int):
    result = math.ceil((height * width) / cover)
    return print(f"You'll need {result} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# Exercise 2
# if it is greater than 1 and cannot be written as the product of two smaller natural numbers.
def numeros_primos(numero: int = 0):
    for i in range(2, numero):
        if numero % i == 0:
            return "It's not a prime number."
    return "It's a prime number."

numero_user: int = int(input("Number: "))
print(numeros_primos(numero_user))



