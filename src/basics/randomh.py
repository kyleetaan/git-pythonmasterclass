#! python3
import random

num = random.randint(1,10)
guess = None
count = 0
while guess != num:
    count += 1
    guess = int(input('guess my number: '))
    if guess == 0:
        print('quitter :P')
        break
    if guess > num:
        print('lower!')
        continue
    if guess < num:
        print('higher!')
        continue
    else:
        print('number {} is right!'.format(guess))
if guess != 0:
    print('you took {} guesses to figure out my number!'.format(count))