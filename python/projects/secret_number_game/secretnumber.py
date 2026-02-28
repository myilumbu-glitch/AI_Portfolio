import random

while True:                     #outer loop to allow restarting the game
    secret = random.randint(1, 10)
    attempt = 0 #must be outside loop to count attempts correctly
    
    while True:          #inner loop to allow multiple guesses until the correct secret number is guessed
        guess = int(input('Enter your secret guess (1-10): '))
        attempt += 1

        if guess == secret: #checks secret number
            print(f'Correct! You got it right in {attempt} attempts!')
            break
        elif guess < secret:
            print('Too low!')
        elif guess > secret:
            print('Too high!')

    again = input('Do you want to play again? (y/n):') #restart if user selects y and ends if user selects n
    if again.lower() == 'y':
            continue #restarts game
    elif again.lower() == 'n':
            print('Thanks for playing')
            break #breaks the loop and ends the game
    
    
