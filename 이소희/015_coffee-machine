### import
import math

### 딕셔너리
MENU = {
    1: {"name": "에스프레소",
        "ingredients": {
            "water": 50,
            "coffee": 18,
            },
        "cost": 2500,
        },
    2: {"name":"카페라뗴",
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
            },
        "cost": 3500,
        },
    3: {"name": "카푸치노",
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
            },
        "cost": 4000,
        }
}

resources = {
    "water": 200,
    "milk": 50,
    "coffee": 100,
}

money_box_machine = {
    "만원": 10
    , "천원": 30
    , "오백원": 20
    , "백원": 100
}

money_box_user = {
    "만원": 0
    , "천원": 0
    , "오백원": 0
    , "백원": 0
}

bending_on = True
order_on = True

user_order = ""
user_bill = 0
user_ing =  {}

### user defined functions
def money_calc(money_box_name):
    """딕셔너리명을 입력하면 총 금액(int)를 리턴한다."""
    return (money_box_name["백원"]*100
            + money_box_name["오백원"] * 500
            + money_box_name["천원"]*1000
            + money_box_name["만원"]*10000
            )

def ing_check(dict):
    """재료 딕셔너리를 입력하면 재료 재고를 여부를 True/False로 리턴한다."""
    checklist = []
    no_ing = []
    for ing in dict:
        check = resources[ing] >= dict[ing]
        checklist.append(check)
        if resources[ing] < dict[ing]:
            no_ing.append(ing)
    checkresult = 1
    for tf in checklist:
        checkresult *= tf
    return [checkresult, no_ing]

# 잔돈 거슬러주기
def process_change(int_amount):
    """int_amount 금액을 money_box_machine에서 차감하고, 잔돈 금액을 print한다."""
    천원count = math.floor(int_amount / 1000)
    int_amount = int_amount - 1000 * 천원count
    오백원count = math.floor(int_amount / 500)
    int_amount = int_amount - 500 * 오백원count
    백원count = math.floor(int_amount / 100)
    int_amount = int_amount - 100 * 백원count
    money_box_machine["천원"] = money_box_machine["천원"] - 천원count
    money_box_machine["오백원"] = money_box_machine["오백원"] - 오백원count
    money_box_machine["백원"] = money_box_machine["백원"] - 백원count
    print(f"천원 {천원count}장, 오백원 {오백원count}개, 백원 {백원count}개 입니다.")

# 커피 제조
def process_coffee(ing_dict):
    global resources
    for item in ing_dict:
        resources[item] -= ing_dict[item]

# report
def report():
    global resources
    print(f"""\n** COFFEE MACHINE STATUS REPORT **
      💧 water  : {resources["water"]} ml
      🍼 milk   : {resources["milk"]} ml
      🫘 coffee : {resources["coffee"]} g
      💸 money  : {money_calc(money_box_machine)} 원""")

# def order():
#     global user_order
#     global user_bill
#     global user_ing


# 자판기 동작
def bending():
    global bending_on
    global order_on
    global MENU
    global resources
    global money_box_machine
    global money_box_user

    # TEST PRINT
    print("""      )  (
     (   ) )
      ) ( (
   ___)____)_
 .-'---------|  소희 커피머신
( C|/\\/\\/\\/\\/|  환영합니다.
 '-./\\/\\/\\/\\/|  WELCOME TO SOHEE COFFEE
   '_________'
    '-------'""")

    # 주문
    while order_on:
        user_choice = input("""\n어떤 음료를 드릴까요? \n👉 1 에스프레소\n👉 2 카페라떼\n👉 3 카푸치노\n  : """)
        if user_choice == "report":
            report()
            input("\n계속 진행하려면 'Enter'를 누르세요.")
        elif user_choice == "off":
            exit()
        else:
            user_choice = int(user_choice)
            user_order = MENU[user_choice]["name"]
            user_bill = MENU[user_choice]["cost"]
            user_ing = MENU[user_choice]["ingredients"]

            order_check = ing_check(user_ing)  # 주문 가능 여부

            print(f"\n{user_order}를 택하셨군요.")
            if ing_check(user_ing)[0] == False:
                print(f"{user_order}는 현재 {ing_check(user_ing)[1]} 부족으로 주문이 어렵습니다.")
                input("메뉴 선택을 다시 하시려면 'Enter'를 눌러주세요.")
            else:
                print(f"{user_order}는 현재 주문이 가능합니다")
                print(f"가격은 {user_bill}원 입니다.")
                input("금액을 투입하시려면 'Enter'를 눌러주세요.")
                order_on = False

    # 금액 투입
    money_box_user["만원"] = int(input("""\n금액을 투입해주세요.
만원권은 몇 장 투입하시나요?: 10,000원 * """))
    money_box_user["천원"] = int(input("""천원권은 몇 장 투입하시나요?: 1,000원 * """))
    money_box_user["오백원"] = int(input("""오백원 동전은 몇 개 투입하시나요?: 500 * """))
    money_box_user["백원"] = int(input("""백원 동전은 몇 개 투입하시나요?: 100 * """))

    # user 투입 금액을 money_box_machine에 넣기
    money_box_machine["만원"] += money_box_user["만원"]
    money_box_machine["천원"] += money_box_user["천원"]
    money_box_machine["오백원"] += money_box_user["오백원"]
    money_box_machine["백원"] += money_box_user["백원"]

    # 투입 금액 확인 및 거스름돈 계산
    user_paid = money_calc(money_box_user)
    user_change = user_paid - user_bill

    print(f"\n감사합니다.🥰 총 {user_paid}원을 지불하셨습니다.")
    print(f"{user_change}원을 거슬러드릴게요.")

    # 잔돈 거슬러주기
    process_change(user_change)
        # 잔액 print

    # 커피 제작
    process_coffee(user_ing)

    # 커피 서빙
    print(f"\n{user_order} 나왔습니다. ☕")
    rebend = input(f"더 주문하시려면 'Enter'키를, 종료하시려면 'off'를 입력해주세요.")
    if rebend == "off":
        bending_on = False
    else:
        order_on = True
        bending()

bending()
