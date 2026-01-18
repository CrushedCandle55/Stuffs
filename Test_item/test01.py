def rd():
    import random
    import time
    rdn = input("input your number: ")
    if rdn == " " or rdn == "X":
        rdn = random.randint(100000, 999999)
    x = 100000
    print(rdn)
    while x != rdn and x < 999999:
        x += 1
        print(x)
        time.sleep(0.0017966)
    if x == rdn:
        print("暴力破解rdn=", x, "原数字为", rdn)
    elif x == 999999:
        print("破解失败")
    time.sleep(3)
while True:
    rd()
# import random
# import time
# rdn1 = random.randint(1000, 9999)w
# while rdn1 != 9126:
#     print(rdn1)
#     rdn1 = random.randint(1000, 9999)
# time.sleep(3)
