import random

def guess(guessNumber):
    if guessNumber < num:
        print('Your guess is too low.')
    elif guessNumber > num:
        print('Your guess is too high.')        

num = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
print('Take a guess.')

i = 1
attempt = int(input())
while attempt != num:
 i = i + 1
 guess(attempt)
 attempt = int(input())
print('Good job! You guessed my number in ' + str(i) + ' guesses!')
