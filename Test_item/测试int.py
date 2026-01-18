import random
a = random.randint(1, 10000000)
b = random.randint(1, 10000000)
c = b
x = 0
while a != b:
    x = x+1
    print(x)
    b = random.randint(1, 100000)
print("Load successfully")
print("a=", a)
print("b=", b)
print("LHS=RHS")
print("original b=", c)
print("try", x, "times")
