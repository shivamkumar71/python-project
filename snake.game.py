import random
computer = random.choice([1,-1,0])
you_str = input("enter your choice (s for snake , g for gun and w for water) : ")

you_dict = {"s": 1, "w":-1,"g":0}
reverse_dict = {1: "snake", -1:"water",0:"gun"}

you = you_dict.get(you_str)
print(f"you choose {reverse_dict[you]}\n computer choice {reverse_dict[computer]}")
                       
if (computer == you ):                      
    print("its draw")

else:
    if (computer == -1 and you == 1):
        print("you win!")
        print("thanks for playing ! have a good day")
        
    elif (computer == 1 and you == -1):
        print("you lose")
        print("thanks for playing ! have a good day")
        
    elif(computer == 1 and you == 0):
        print("you win!")
        print("thanks for playing ! have a good day")
        
    elif(computer ==0 and you == 1):
        print("you lose")
        print("thanks for playing ! have a good day")
        
    elif(computer == -1 and you == 0):
        print("you lose")
        print("thanks for playing ! have a good day")
        
    elif(computer == 0 and you == -1):
        print("you win")
        print("thanks for playing ! have a good day")
        
    else:
        print("invalid choice")







