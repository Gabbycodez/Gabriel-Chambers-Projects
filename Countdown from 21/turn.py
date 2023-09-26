import random 

def play_human_turn(n):
    h_coins = abs(int(input('How many coins? ')))
    while h_coins == 0 or h_coins >= 4:
        h_coins = abs(int(input('How many coins? (Please input a number 1-3):')))
    if n - 1 == 0:
        print("You Win!!")
        return 0
   
    elif n - 2 == 0:
        print("You Win!!")
        return 0
    
    elif n - 3 == 0:
        print("You win!!")
        return 0
   
    elif h_coins <= 3 and n > 0:
        game_coins = n - h_coins
        return game_coins
    
    elif n == 0:
        print("Human Wins!!")
        return 0
   
    elif h_coins < 3:
        h_coins = abs(int(input('How many coins? (Please input a number 1-3):')))
                    
    # 3. If the human wins, indicate that and return 0

    # You must implement this function
pass

def play_computer_turn(n):
    if n == 9:
        c_coins = (n - 1)
        print('Computer takes one coin.')
        return c_coins
    elif n == 13:
        c_coins = (n - 1)
        print('Computer takes one coin.')
        return c_coins
    
    elif n - 1 == 0:
        print('Computer takes one coin.')
        print("Computer Wins!!")
        return 0
   
    elif n - 2 == 0:
        print('Computer takes two coins.')
        print("Computer Wins!!")
        return 0
    
    elif n - 3 == 0:
        print('Computer takes three coins.')
        print("Computer Wins!!")
        return 0
   
    elif n == 5:
        c_coins = (n - 1)
        print('Computer takes one coin.')
        return c_coins
    
    elif n % 4 == 2:
        c_coins = (n - 2)
        print('Computer takes two coins.')
        return c_coins
    
    elif n / 6 == 1:
        c_coins = (n - 2)
        print('Computer takes two coins.')
        return c_coins
    
    elif n % 2 == 0: 
        c_coins = (n - 2)
        print('Computer takes two coins.')
        return c_coins
    
    elif n % 3 == 0: 
        c_coins = (n - 3)
        print('Computer takes three coins.')
        return c_coins
    
    elif n > 4:
        c_coins = (n - 3)
        print('Computer takes three coins.')
        return c_coins
    
    elif n / 7 == 1:
        c_coins = (n - 3)
        print('Computer takes three coins.')
        return c_coins
    
    else:
        print("Computer Wins!!")
        return 0 
    # 2. If computer wins, indicate that and return 0
    # 3. return number of coins remaining
    # You must implement this function 
pass
