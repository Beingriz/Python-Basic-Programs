#prog to check prime no
while True:

    num=input("Enter the number\n")
    if (num=="Exit"):
        break
    try:
        inum=int(num)
        if(inum>0):
            for i in range(2,inum):
                if(inum%i==0):
                    print("It is not Prime")
                    break
            else:
                print(" Prime")
        else:
            print("Not a prime")
    except:
        print("Enter valid no")
        continue