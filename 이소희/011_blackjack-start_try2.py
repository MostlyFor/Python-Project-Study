import random
from art import logo

# 카드 및 덱 생성
cards = {"A": 11
         ,"2": 2
         ,"3": 3
         ,"4": 4
         ,"5": 5
         ,"6": 6
         ,"7": 7
         ,"8": 8
         ,"9": 9
         ,"10": 10
         ,"J": 10
         ,"Q": 10
         ,"K": 10
        } #, 11, 11, 11, 11]

# 함수 - 카드 뽑기
def pick_a_card(deck):
  new_card = random.choice(list(cards.keys()))
  deck.append(new_card)

# 함수 - 점수 계산
def scoring(deck):
  global game_on
  score = 0
  for card in deck:
    score += cards[card]
  for card in deck:
    if cards[card] == 11 and score > 21:
      score -= 10
  return score

# 함수 - 잭 or 버스트
def jack(score):
  global game_on
  if score == 21:
    game_on = False
    return "Jack Black"
  if score > 21:
    game_on = False
    return "Bust"

##### 게임 리셋 ##########
# 카드 덱
deck_user = []
deck_computer = []
# 스코어 생성
score_computer = 0
score_user = 0

game_money = 500
betting = 0

game_on = True
game_

# 게임 스타트
print(logo)
print("Welcome to Sohee's House.")
print(f"Your have now ${game_money}.\n")
bet()

# 첫 카드 뽑기
pick_a_card(deck_computer)
pick_a_card(deck_computer)
pick_a_card(deck_user)
pick_a_card(deck_user)

# 딜러 카드 생성
deck_computer_open = []
for i in range(len(deck_computer)):
  if i == 0:
    deck_computer_open.append("?")
  else:
    deck_computer_open.append(deck_computer[i])

# 점수 계산
score_computer = scoring(deck_computer)
score_user = scoring(deck_user)
if score_user == 21:
  win()
gamestat()

# 뽑말 물어보기
while game_on:
  user_choice = input("'Stand' or 'Hit'? ").lower()
  # 계속 뽑는 경우
  if user_choice == "hit":
    hit(deck_user)
  # User가 그만 뽑는 경우    
  if user_choice == "stand":
    # 컴퓨터 Hit
    while score_computer + sum(cards)/len(cards) <= 21: # Hit 스코어 기댓값이 21을 넘지 않는 경우 Pick a card
      pick_a_card(deck_computer)
      score_computer = scoring(deck_computer)
    gameover()
    if score_computer == 21:
      #game_money -= betting
      print("Dealer's Jack Black!")
      lose()
    if score_computer > 21:
      game_money += betting * 2
      print("Dealer's Bust!")
      win()
    if score_computer < 21:
      if score_computer == score_user:
        tie()
      if score_computer > score_user:
        lose()
      if score_computer < score_user:
        win()

#pick_a_card(deck_computer)
#pick_a_card(deck_user)

#print(f"deck_user: {deck_user}")
#print(f"deck_computer: {deck_computer}")

#score_user = scoring(deck_user)
#score_computer = scoring(deck_computer)

print(f"score_user: {score_user}")
print(f"score_computer: {score_computer}")




      
### 두번째 베팅이 시작됨과 동시에 game_on == False가 됨

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

