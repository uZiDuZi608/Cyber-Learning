import random
import hangman_art
import hangman_words
logo= hangman_art.logo
print(logo)
stages = hangman_art.stages
lives=6
word_list=hangman_words.word_list
chosen_word=random.choice(word_list)
placeholder=""
wordlength=len(chosen_word)
for letter in range(wordlength):
    placeholder += "_"
print(placeholder)
display=[]
for letter in range(wordlength):
    display.append("_")
word=""
guessed_letters=[]
while word!=chosen_word:
    guess = input("Guess a letter: ").lower()
    while guess in guessed_letters:
        print(f"You have already guessed {guess}")  
        guess = input("Guess a letter: ").lower()
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = letter

    
    if guess not in chosen_word:
            lives-=1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            print(stages[lives])
            print(f"You have {lives} lives left")
            if lives==0:
                print(f"you lose game over\n{stages[lives]}\nand the word was {chosen_word}")
                break
    guessed_letters.append(guess)                


    word = "".join(display) 
    print(word)

