print('GUESS GAME')
secret_number = 6
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess a number between 0-10: '))
    guess_count += 1
    if guess == secret_number:
        print('Great job , you guessed it right')
        break
else:
    print('oops,better luck next time' )