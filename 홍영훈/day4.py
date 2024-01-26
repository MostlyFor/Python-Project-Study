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
rsp_list = [rock, scissors, paper, rock]

player = 10
while player:
    player = int(input('가위 = 1, 바위 = 0, 보 = 2 중 하나를 숫자로 고르시오\n'))
    if player != 1 and player != 0 and player != 2:
        print('잘못 입력했습니다. 다시 입력해주세요')
        player = 10
    else:
        break
    
print('you\n', rsp_list[player])

computer = random.randint(0,2)
print('computer\n', rsp_list[computer])

# 비긴 경우
if computer == player:
    print('비김')
    quit()

# 인간 승리 경우
if computer == 0:
    computer = 3
if computer-player == 1:
    print('승리')
else:
    print('패배')