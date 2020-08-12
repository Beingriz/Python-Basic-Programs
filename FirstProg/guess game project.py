# First Project : Game to Guess the Word
import random
print("Enter Your Name ")
name = input()
print("Good Luck Mr/Mrs. ", name )
words =  ["python","laptop","desktop","chair","computer","google"]
word = random.choice(words)
guesing = ''
turn = len(word)+5
while (turn>0):
    fail = 0
    gues = input("Guess the Charecter : ")
    guesing += gues
    for char in word:
        if char in guesing:
            print(char)
        else:
            print("*")
            fail+=1
    print("number of turens left", turn)
    if gues not in word:
        turn-=1
    if fail==0:
        print("You won the Game", name)
        print("The word is", word)
        break
    if turn==0:
        print("You Loos! Sorry")
