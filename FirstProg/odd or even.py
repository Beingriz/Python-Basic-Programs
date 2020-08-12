# Prog to find even or odd no
while True:
    num=input("enter the no\n")
    if(num=="exit"):
        break
    try:
        inum=int(num)
        if (inum%2==0):
            print("Even")
        else:
            print("odd")
    except:
        print("Invalid input")
        continue

