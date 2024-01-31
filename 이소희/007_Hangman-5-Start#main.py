#Step 5

import random

import hangman_words
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
import hangman_art
print(hangman_art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for letter in range(word_length):
    display += "_"

# 유저가 선택한 단어 목록
user_choice = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in user_choice:
        print(f"{guess}는 이미 선택한 단어 입니다. 목숨 -1")
        lives -= 1
    #Check guessed letter
    else:
      user_choice.append(guess)
      for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
      if guess not in chosen_word:
          #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
          lives -= 1
          print(f"{guess}는 잘못 짚으셨습니다. 목숨 -1")
          if lives == 0:
              end_of_game = True
              print("You lose.")
  
      #Join all the elements in the list and turn it into a String.
      print(f"{' '.join(display)}")
  
    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(f"남은 목숨은 {lives}개 입니다.")
    print(hangman_art.stages[lives])
    print("======================")
