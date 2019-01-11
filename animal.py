#!/usr/bin/env python3

def checkguess(guess,answer):
    global score
    still_guess = True
    try_ing = 0
    while still_guess and try_ing <3:
        if guess.lower() == answer.lower():
            print('that corrent')
            score = score +1 
            still_guess = False

        else:
            if try_ing <2:
                guess = input('try again:  ')

            try_ing += 1




        if try_ing ==3:

            print('solution' + anser)



score = 0

print('Guess Animal')
guess1=  input('which bear live at noth pole     ')
checkguess(guess1,'polar bear')
guess2 = input('which is the fastest land animal')
checkguess(guess2,'cheetah')
guess3 = input('which the largest animal')
checkguess(guess3,'blue whale')
print('your score is '  + str(score))
