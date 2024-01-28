#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("반갑습니다. 엔빵 계산기에 오신 걸 환영합니다.")
total = input("얼마를 먹으셨나요?\n >> ")
total = int(total)
tippct = input("팁으로 몇 퍼센트(%)를 주실건가요?\n >> ")
tippct = int(tippct)
person = input("몇 명이서 엔빵하나요?\n >> ")
person = int(person)
nwon = total * ( tippct + 100 ) / 100 / person
nwon = round(nwon, 2)
print(f"""{total}원을 {person}명이 드셨군요.
팁 {tippct}%를 포함해서 {person}명이 엔빵하려면 {nwon}원 씩 내세요.""")
