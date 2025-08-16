import random , time

def play_game():
    number = random.randint(1,100)
    attempts = 0
    
    print("Welcome to the number Guessing Game!")
   
    print("I am thinking...")
      
    
    while True:
        try:
            guess = int(input("Enter your guess : "))
        except ValueError:
            print("Invalid input. please enter a number.")
            continue
        
        attempts += 1
        
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"congratulation! you guessed the number in {attempts} attempts!")
            break
        
if __name__ == "__main__":
    play_game()