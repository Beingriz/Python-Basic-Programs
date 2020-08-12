# Program to Find Positive Negative or Zero
"""while True:
    num = input("Enter the Number : ")
    if(num == "exit"):
        break
    try:
        inum = int(num)
        if (inum>0):
            print("Positive")
        elif (inum<0):
            print("Negative")
        else:
            print("Zero")
    except:
        print("Enter Valid Input")
        continue

# Program to Check a Number is Prime or Not

while True:
    num = input("Enter the Number : ")
    if(num=="exit"):
        break
    try:
        inum=int(num)
        if(inum>0):
            for i in range(2,inum):
                if(inum%i)==0:
                    print("Not a Prime Number!...")
                    break
            else:
                print("Prime Number", num)
        else:
            print("Enter the Number ")
    except:
        print("Enter the Valid Input")
        continue

# Program to Find Prime Numbers in an Given Intervals
while True:
    s=input("\nEnter the Starting Range From 2: ")
    if(s=="exit"):
        break
    e=input("\nEnter the Ending Range : ")
    count =0
    try:
        iss= int(s)
        ie=int(e)
        for i in range(iss,ie):
            if (i>0):
                for j in range(2, i):
                    if(i%j==0):
                        count+=1
                        break

                else:
                    print(i,end=",")

    # print("\n Total Iterations = ",count)
    except:
        print("Invalid Input")
        continue

# Program to Find odd even Numbers
while True:
    num = input("Enter the Number : ")
    if(num=="exit"):
        break
    try:
        inum = int(num)
        if(inum>0):
            if(inum%2==0):
                print("Even Numver",inum)
            else:
                print("Odd Number", inum)
        else:
            print("Invalid Number")
    except:
        print("Invalid Iinput")
        continue

# Program to Find odd even Numbers in an interval

while True:
    s=input("Enter Starting Range : ")
    if (s=="exit"):
        break
    e=input("Enter Ending Range : ")
    try:
        iss = int(s)
        ie =int(e)
        if(iss>0):
            for i in range(iss,ie+1):
                for j in range(1,i):
                    if(i%2==0):
                        print("Even",i, end=",")
                        break
                    else:
                        print("odd",i)
                        break
        else:
            print("Enter Valid Number!...")
    except:
        print("Invalid Input")
        continue

# Program to Find armstrong Number
while True:
    n =input("Enter the Number : ")
    if(n=="exit"):
        break
    try:
        inp = int(n)
        temp = inp
        sum = 0
        digit = 0
        while(temp>0):
            digit = temp % 10
            sum+=digit**3
            temp//=10
        if sum==inp:
            print("Number is Armstrong")
        else:
            print("Not a Armstrong")
    except:
        print("Invalid Input !..")
        continue
# Program to Find armstrong Number in an Interval

while True:
    st = input("Enter the Starting Range : ")
    if (st=="exit"):
        break
    en = input("Enter the Ending Range : ")

    try:
        ist = int(st)
        ien = int(en)
        for i in range(ist,ien+1):
            temp = i
            sum=0
            digit = 0
            while(temp>0):
                digit = temp%10
                sum+=digit**3
                temp//=10
            if sum==i:
                print(sum)

    except:
        print("Invalid Input")
        continue

# Program to Print Fibbonacci Series

while True:
    num = input("\nEnter the Number of Terms : ")
    if(num == "exit"):
        break
    try:
        inum = int(num)
        a=0
        b=1
        count=2
        sum=0
        print(a,b,end=",")
        while(count<inum):
            sum = a+b
            a=b
            b=sum
            count+=1
            print(sum, end=",")
    except:
        print("Invalid Input")
        continue

# Program to Find conpound Interest
def compound(p,t,r,n):
    ci = p*pow((1+r/n),n*t)
    print("Compound Interest is : %0.2f"% ci)
while True:
    p = input("Enter Principle Amount : ")
    if (p=="exit"):
        break
    t = input("Enter Time Period : ")
    r = input("Enter Rate of Interest : ")
    n = input("Enter Duration in Months  : ")

    try:
        ip=int(p)
        ir = float(r)
        it = int(t)
        inn=int(n)
        compound(ip,it,ir,inn)
    except:
        print("Invalid Input")
        continue """

print(bin(lst))

