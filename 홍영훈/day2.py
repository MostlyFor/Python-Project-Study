print('팁 계산기, 총 지불 금액 k$에 대해 n명이 왔을 때 인당 얼마의 팁을 내야 하는가?')
total_bill = float(input('총 금액?: '))
tip_percent = float(input('팁 %?: '))
people = float(input('총 사람 수?: '))

bill_per_person = (total_bill * (1 + tip_percent / 100)) / people


print("인당 {:.2f}".format(bill_per_person))