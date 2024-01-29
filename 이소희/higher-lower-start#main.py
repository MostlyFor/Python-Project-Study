import random
from game_data import data #50개
from art import logo, vs

# 함수 - 0~49 사이의 랜덤 정수를 반환
def randnum():
  return random.randrange(0,49)

# 함수 - data 딕셔너리의 관련 정보 조회
def getdata(number, key):
  return data[number].get(key)

def game():
  # 게임 초기 세팅
  game_on = True
  spell_check = False
  score = 0
  
  # B 정보
  bnum = randnum() # 랜덤 번호 생성 
  b_name = getdata(bnum, 'name')
  b_follower = getdata(bnum, 'follower_count')
  b_description = getdata(bnum, 'description')
  b_country = getdata(bnum, 'country')
  
  while game_on:
    spell_check = False
    # A-B 스위치 (B 인물정보를 A 인물정보로 밀어넣는다. 다음 게임의 연속성을 위해서.)
    a_name = b_name
    a_follower = b_follower
    a_description = b_description
    a_country = b_country
    
    # B 정보 신규생성
    bnum = randnum() # 랜덤 번호 생성 
    b_name = getdata(bnum, 'name')
    b_follower = getdata(bnum, 'follower_count')
    b_description = getdata(bnum, 'description')
    b_country = getdata(bnum, 'country')
    
    
    # 게임 로고 및 인물정보 프린트
    print("=================================")
    print(logo)
    print("=================================")
    print(f"\nCompare A : {a_name}, {a_description}, from {a_country}")
    print(f"🤫 {a_follower}")
    print(vs)
    print(f"""\nAganinst B : {b_name}, {b_description}, from {b_country}""")
    print(f"🤫 {b_follower}\n")
    
    # 유저 A vs B 선택
    while spell_check == False:
      user_choice = input("Who has more followers? Type 'A' or 'B'.  ").lower()
      if user_choice == 'a' or user_choice == 'b':
        spell_check = True # (a, b, A, B)를 입력한 경우만 Pass
      if user_choice == 'a':
        user_sign = 1
      elif user_choice == 'b':
        user_sign = -1
      else:
        print("You mis-spelled. Type 'A' or 'B'.")
    
    if (a_follower - b_follower) * user_sign > 0:
      score += 1
      input(f"""You Win! Now your score is {score}.
'Enter' for more guess.  """)
    elif  (a_follower - b_follower) * user_sign < 0:
      game_on = False
      input(f"""You lose. Your score is {score}.
Game Over.  """)
      game() # 게임 초기화 및 재시작
    else:
      input(f"""Draw. Your score is {score}.
'Enter' for more guess.  """)

game()
