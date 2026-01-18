import random
import time
import datetime

def Game():
        

         
    level = ["YLMASS", "CL Project:Bingo Game", "A:Easy Level", "B:Intermediate Level", "C:Advance level", "D:Challanging Level", "E:Exit"]
    
    for i in level:
        width = 50
        text = i
        print_out_text = text.center(width)
        print(print_out_text)
    
    level = input("Your choise(Please type in):")
    now1=datetime.datetime.now()
    print('Now time',now1)
    print ('hour',now1.hour)
    print ('min',now1.minute)
    print ('second',now1.second)

    def Lv_EC():
        lower_value = 0
        upper_value = 100
        computer = random.randint(1,100)
        #print(computer)
        found = False
        while found == False:
            player = input("Enter a no.:")
            player = int(player)
            while player < 1 or player > 100:
                print("Input out of range, please input again.")
                player = input("Enter a no.:")
                player = int(player)
            if player == computer:
                print("Bingo")
                found = True
                now2=datetime.datetime.now()
                print('Now time',now2)
                print('hour',now2.hour)
                print('min',now2.minute)
                print('second',now2.second)
                hour2 = int(now2.hour) - int(now1.hour)
                min2 = int(now2.minute) - int(now1.minute)
                sec2 = int(sec2.second) - int(sec1.second)
                print("You use", hour2, "hours", min2, "minutes", "and", sec2, "seconds")
            elif player > computer and player < upper_value:
                print("Too Big!")
                upper_value = player
                print(lower_value, "-", upper_value)
            elif player < computer and player > lower_value:
                print("Too Small!")
                lower_value = player
                print(lower_value, "-", upper_value)
                
        Game()
        
        
    def Lv_INT():
        computer = random.randint(1,100)
        #print(computer)
        found = False
        while found == False:
            player = input("Enter a no.:")
            player = int(player)
            while player < 1 or player > 100:
                print("Input out of range, please input again.")
                player =  input("Enter a no.:")
                player = int(player)
            if player == computer:
                print("Bingo")
                found = True
                now2=datetime.datetime.now()
                print('Now time',now2)
                print('hour',now2.hour)
                print('min',now2.minute)
                print('second',now2.second)
                hour2 = int(now2.hour) - int(now1.hour)
                min2 = int(now2.minute) - int(now1.minute)
                sec2 = int(sec2.second) - int(sec1.second)
                print("You use", hour2, "hours", min2, "minutes", "and", sec2, "seconds")
            elif player > computer and player < upper_value:
                print("Too Big!")
            elif player < computer and player > lower_value:
                print("Too Small!")
            Game()
            
            
    def Lv_ADV():
         
        #gen six unique number from 1 to 10
        nolist=[]
        total_no=6
        index=0
        while index<total_no:
            randno=random.randint(1,10)
            if not(randno in nolist):
                nolist.append(randno)
                index=index+1
        print(nolist)
         
        newlist=['','','','','','']
        newlist_address=[]
        index=0
        while index<total_no:
            address=random.randint(0,5)
            if not(address in newlist_address):
                newlist_address.append(address)
                newlist[address]=nolist[index]
                index=index+1
         
         
        print(newlist)
        newlist=['','','','','','']
        newlist_address=[]
        index=0
        while index<total_no:
            address=random.randint(0,5)
            if not(address in newlist_address):
                newlist_address.append(address)
                newlist[address]=nolist[index]
                index=index+1
 
        print(newlist)
        
        
        
    def Lv_CHL():
        computer = random.randint(1,100)
        #print(computer)
        found = False
        while found == False:
            player = input("Enter a no.:")
            player = int(player)
            while player < 1 or player > 100:
                print("Input out of range, please input again.")
                player = input("Enter a no.:")
                player = int(player)
            if player == computer:
                print("Bingo")
                found = True
                now2=datetime.datetime.now()
                print('Now time',now2)
                print('hour',now2.hour)
                print('min',now2.minute)
                print('second',now2.second)
                hour2 = int(now2.hour) - int(now1.hour)
                min2 = int(now2.minute) - int(now1.minute)
                sec2 = int(sec2.second) - int(sec1.second)
                print("You use", hour2, "hours", min2, "minutes", "and", sec2, "seconds")
            else:
                print("Not correct")
                Game()
                

    if level == "A" or level == "a":
        print("a")
        Lv_EC()
    elif level == "B" or level == "b":
        Lv_INT()
    elif level == "C" or level == "c":
        Lv_ADV()
    elif level == "D" or level == "d":
        Lv_CHL()
    elif level == "E" or level == "e":
        quit()


Game()
