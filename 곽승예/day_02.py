# 2일차 프로젝트: 팁 계산기

print("Welcome to the tip calculator.")
bill = input("What was the total bill?")
per = input("What percentage tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")
each = round((float(bill[1:])*(1+int(per)/100))/int(people),2)
print(f"Each person should pay: ${each}") 
