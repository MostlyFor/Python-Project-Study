from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

bidder_dict = {} #
game_over = False
game_continue = ""

print(logo)
while game_over == False :
  bidder_name = input("What is your name?")
  #print(bidder_dict)
  bid_amout = input("How mush do you want to bid?")
  bidder_dict[bidder_name] = bid_amout
  #print(bidder_dict)
  game_continue = input("Is there other bidder?").lower()
  if game_continue == "yes" :
    clear()
  else:
    game_over = True

#print(bidder_dict)
print(f"Winner : {max(bidder_dict, key=bidder_dict.__getitem__)}")
print(f"Bid : {max(bidder_dict.values())}")
