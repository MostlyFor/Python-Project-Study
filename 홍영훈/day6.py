def turn_right():
    for i in range(3):
        turn_left()
        
while front_is_clear():
    move()
        
while not at_goal():
    # 오른쪽에 벽을 만나기 전
    if right_is_clear():
            turn_right()
            move()
    # 오른쪽에 벽을 만남
    elif front_is_clear():
        move()
    else:
        turn_left()