def scramble_game(name):
    print("                                   --->#WELCOME TO WORD SCRAMBLE GAME#<---")
    import random
    score=0
    for i in name:
        a=list(i)
        random.shuffle(a)
        c=''.join(a)
        print("shuffled word is:",c)
        d=input("Guess the correct word:")
        if i==d:
            print("you win")
            score+=1
        else:
            print("you lose")
    print("you scored",score)
    if score>=(len(name)-1):
        print("you perfomed nice keep it up")
    elif score<=(len(name)-2) and score>1:
        print("you have to work hard for english")
    else:
        print("you have to practice it again")
scramble_game(["shahzadpur","chandigarh","masters","connection","applications"])