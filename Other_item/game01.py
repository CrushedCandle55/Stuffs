#项目：猜文字游戏
x = 1
chance = 0
while x == 1:
    x = 0
    import random
    guessing_no = -1
    random_number = -2
    gamemode = input("请选择你的游戏模式：1（1-100）2（1-1000）3（1-5000）4（自定范围）")
    while gamemode != "1" and gamemode != "2" and gamemode != "3" and gamemode != "4":
        print("请不要输入除1、2、3、4之外的文字")
        gamemode = input("请选择你的游戏模式：1（1-100）2（1-1000）3（1-5000）4（自定范围）")
    gamemode = int(gamemode)
    if gamemode == 1:
        random_number = random.randint(1, 100)
        print("你有20次机会")
        chance = 50
    elif gamemode == 2:
        random_number = random.randint(1, 1000)
        print("你有200次机会")
        chance = 500
    elif gamemode == 3:
        random_number = random.randint(1, 5000)
        print("你有1000次机会")
        chance = 2500
    elif gamemode == 4:
        a = input("最小值")
        b = input("最大值")
        a = int(a)
        b = int(b)
        chance = int((b-a)/54)
        print("你有", chance, "次机会")
        random_number = random.randint(a, b)
    while int(guessing_no) != int(random_number):
        guessing_no = input("你认为数字是：")
        guessing_no = int(guessing_no)
        if guessing_no > random_number:
            print("大了")
            chance = chance - 1
            print("你还有", chance, "次机会")
            if chance >= 0:
                print("机会用尽")
                guessing_no = random_number
                x = 1
        elif guessing_no < random_number:
            print("小了")
            chance = chance - 1
            print("你还有", chance, "次机会")
            if chance <= 0:
                print("机会用尽")
                guessing_no = random_number
                x = 1
        elif guessing_no == random_number:
            print("猜对了")
            x = 1

