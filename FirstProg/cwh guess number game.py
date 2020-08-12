# Program to Guess the word
turn = 5
number = 15
count =0
while (turn>0):
    guess = input("Guess the Number : ")
    try:
        val = int(guess)
        if val == number:
            print("You won\n Number is ",number)
            count+=1
            print("Number of Attempts",count)
            break
        elif val > number:
            print("Please Enter lesser Number than ", val)
            count+=1
            turn-=1
            print(turn,"Turns Left")
        else:
            print("Please Enter Greater Number than", val)
            count+=1
            turn-=1
            print(turn, "Turns Left")
    except:
        print("Invalid Input")
