import random
def guess_the_number(): 
    n = random.randint(1, 100)   
    while True:
        x = int(input("Guess the number (1-100): "))        
        if x == n:
            print("EXACTLY!")
            break
        elif x > n:
            print(f"n < {x}")
        else:
            print(f"n > {x}")
guess_the_number()