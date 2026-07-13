import art
x=art.logo
print(x)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
restart=""
while restart != "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(original_text,shift_amount,direction):
        text=""
        for letter in original_text:
            if letter in alphabet:
                if direction=="decode":
                    letter_index=alphabet.index(letter)
                    x=letter_index-shift_amount
                    new_letter_index=x%26
                    converted_letter=alphabet[new_letter_index]
                    text += converted_letter
                elif direction=="encode":
                    letter_index=alphabet.index(letter)
                    x=letter_index+shift_amount
                    new_letter_index=x%26
                    converted_letter=alphabet[new_letter_index]  
                    text += converted_letter
            else:
                text+=letter
        print(f"the {direction}d text is {text}")

    caesar(original_text=text,shift_amount=shift,direction=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
