import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
image = [scissors, rock, paper]
letter = ["가위", "바위", "보"]

#Write your code below this line 👇



# 시스템 가위1-바위2-보3
sys_pick = random.randint(0,1)
# if sys_pick == 2: 
#   sys_pick_str = rock
# elif sys_pick == 1: 
#   sys_pick_str = scissors
# else: 
#   sys_pick_str = paper

# 유저 1, 2, 3 input
user_pick = int(input("""무엇을 내시겠습니까?
> 가위(1), 바위(2), 보(3)
>> """))
if user_pick not in [0, 1, 2]:
  print("잘못된 입력입니다.\n당신이 졌습니다.")  
else: # 유저 가위1-바위2-보3
  # if user_pick == 2:
  #   user_pick_str = rock
  # elif user_pick == 1:
  #   user_pick_str = scissors
  # else:
  #   user_pick_str = paper
  print(f"당신은 {letter[user_pick]}을 냈습니다.\n{image[user_pick]}")
  print(f"시스템은 {letter[sys_pick]}을 냈습니다.\n{image[sys_pick]}")
  # 
  if user_pick == sys_pick:
    print("\n***비겼습니다.***")
  elif user_pick == 0:
    if sys_pick == 1: #가위:바위
      print("\n***당신이 졌습니다.***")
    else: #가위:보
      print("\n***당신이 이겼습니다.***")
  elif user_pick == 1:
    if sys_pick == 0: #바위:가위
      print("\n***당신이 이겼습니다.***")
    else: #바위:보
      print("\n***당신이 졌습니다.***")
  else:
    if sys_pick == 0: #보:가위
      print("\n***당신이 졌습니다.***")
    else: #보:바위
      print("\n***당신이 이겼습니다.***")

# 1 가위 2 바위 3 보

# 1:3 = 승
# 1:2 = 패

# 2:1 = 승
# 2:3 = 패

# 3:2 = 승
# 3:1 = 패
