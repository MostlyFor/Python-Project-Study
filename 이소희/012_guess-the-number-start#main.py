import random

#변수 선언
def game():
  attempt = 0
  game_on = True
  
  print("Welcome to Number Guessing Game.")
  
  # 게임 레벨 선택
  game_level = input("Type 'Easy' or 'Hard'.  ").lower()
  if game_level == 'hard':
    attempt = 10
  else:
    attempt = 5
  
  # 숫자 생성
  num = random.randrange(1,101)
  print(num)
  
  while game_on:
    user_guess = int(input("Guess the number. "))
    if num == user_guess:
      print(f">> You Win. The number was {num}.\n")
      game_on = False
    elif num > user_guess:
      attempt += -1
      print(f">> Too low. Now you have {attempt} tries.\n")
    elif num < user_guess:
      attempt += -1
      print(f">> Too high. Now you have {attempt} tries.\n")
    if attempt == 0:
      print(">> You lose. Game end.\n")
      game_on = False
  
  new_game = input("Press 'yes' to restart. ").lower()
  if new_game == "yes":
    game()
  else:
    print("Okay. Bye.")

game()



#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

