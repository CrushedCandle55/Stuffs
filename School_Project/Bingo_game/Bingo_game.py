#CL Project: random number game
import random


def game():
    #easy level
    def lv_ec():
        print("You have choose Easy Level")
        computer = random.randint(1, 100)
        print(computer)
        found = False
        lower_no = 1
        upper_no = 100
        while found is False:
            player = input("Enter a no.:")
            player = int(player)
            number_guess = player
            if player < lower_no or player > upper_no:
                print("Input out of range, please input again.")
            elif player == computer:
                print("Bingo")
                found = True
            elif player > computer:
                print("Too Big!")
                upper_no = number_guess/,.m
                print("the number is", lower_no, "-", upper_no)
            elif player < computer:
                print("Too Small!")
                lower_no = number_guess
                print("the number is", lower_no, "-", upper_no)
        game()

    #intermediate level
    def lv_int():
        print("You have choose intermediate")
        computer = random.randint(1, 100)
        print(computer)
        found = False
        while found is False:
            player = input("Enter a no.:")
            player = int(player)
            if player < 1 or player > 100:
                print("Input out of range, please input again.")
            elif player == computer:
                print("Bingo")
                found = True
            elif player > computer:
                print("Too Big!")
            elif player < computer:
                print("Too Small!")
            game()

    #advanced level
    def lv_adv():
        print("You have choose Advance level")

    #challenging level
    def lv_chl():
        print("You have choose Challenging level")
        computer = random.randint(1, 100)
        print(computer)
        found = False
        while found is False:
            player = input("Enter a no.:")
            player = int(player)
            if player < 1 or player > 100:
                print("Input out of range, please input again.")
            elif player == computer:
                print("Bingo")
                found = True
            else:
                print("Not correct")
                game()

    #the starting page
    width = 50
    text = ["YLMASS", "CL Project:Bingo Game\n", "A: Easy Level", "B: Intermediate Level",
            "C: Advance level", "D: Challenging Level\n ", "E: Exit\n"]
    for i in text:
        print(i.center(width))

    #getting level
    level = input("Your choice(Please type in):")
    if level == "A" or "a":
        lv_ec()
    elif level == "B" or "b":
        lv_int()
    elif level == "C" or "c":
        lv_adv()
    elif level == "D" or "d":
        lv_chl()
    elif level == "E" or "e":
        confirm = input("Please type in \"E\" again")
        if confirm == "E" or confirm == "e":
            quit()
        else:
            game()
    else:
        print("Invalid input")
        quit()


game()
