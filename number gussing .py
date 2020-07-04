#(Nuber_gussing_game)

import random
winnig_number= random.randint(1,100)
guess =1
game_over = False
number = int(input("Guess a Number Between 1 and 100 : "))
while not game_over:
    if number == winnig_number:
        print(f"You won and gussed this number in : {guess} times  ")#(3.6)
        game_over = True
    else:
        if number < winnig_number:
            print("Its low ")
        else:
            print("its High ")

        guess += 1
        number = int(input("guess again : "))
   