#함수(연산자별) 정의
def add(n1, n2):
  """더하기"""
  return n1 + n2
  
def sub(n1, n2):
  """빼기"""
  return n1 - n2

def mul(n1, n2):
  """곱하기"""
  return n1 * n2

def div(n1, n2):
  """나누기"""
  return n1 / n2

# 딕셔너리 정의 # 함수 정의보다 아래에 정의해야 정상 작동함
operators = {
  "+": add,
  "-": sub,
  "*": mul,
  "/": div
}
test = operators["+"]
print(test)
print(test(2, 5))

# 함수 작동 확인
print(f"""add : {operators["+"](2, 5)}""")
print(f"""sub : {operators["-"](2, 5)}""")
print(f"""mul : {operators["*"](2, 5)}""")
print(f"""div : {operators["/"](2, 5)}""")

# 딕셔너리를 스트링 join 해서 보여주기
list = []
for operator in operators:
  list.append(operator) 
operator = ", ".join(list)

# 게임 지속/종료 조건
game_on = True

# 사용자 입력
num1 = int(input("What's the first number? \n"))

while game_on:
  num2 = int(input("What's the other number? \n"))
  
  sign = input(f"Pick an operator: {operator} \n")
  function = operators[sign]
  answer = function(num1, num2)
  
  print(f"{num1} {sign} {num2} is ... {answer} \n")

  num1 = answer

  user_reply = input("""Do you want to continue? "yes" or "no" \n""").lower()
  if user_reply != "yes":
    game_on = False
