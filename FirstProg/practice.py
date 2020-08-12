#progam to chek prime number
"""while True:
    num = input("Enter the Number to chek Prime : ")
    if num == "done":
        break
    try:
        val = int(num)
        for i in range(2, val):
            if val%i==0:
                print("Not a Prime")
                break
        else:
            print(val,"is Prime")
    except:
        print("Invalid Input")
        continue

# Program to chek prime in an given interval
while True:
    s = input("Enter the Starting Range  : ")
    if s == "done":
        break
    e = input("Enter the ENding Range : ")
    try:
        st = int(s)
        en = int(e)
        for i in range(st,en+1):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i)
    except:
        print("Invalid input")
        continue
# Program to chek number is odd or even
while True:
    num = input("Enter the Number  : ")
    if num == "done":
        break
    try:
        val = int(num)
        if val>0:
            if val %2==0:
                print(val,"Is Even")
            else:
                print(val,"is Odd")
        else:
            print("Enter Valid Number")
    except:
        print("Invalid Input")
        continue
# progrma to chek odd or Even in an given intervals
while True:
    s= input("Enter the starting  range : ")
    if s=="done":
        break
    e = input("Enter the Ending Range : ")
    try:
        st = int(s)
        en = int(e)
        for i in range(st, en):
            if i%2==0:
                print(i,"Even", end=",")
            else:
                print(i,"Odd")
    except:
        print("Invlid Input")
        continue
# program to chek the number is Armstrong or Not
while True:
    num = input("Enter the Number : ")
    if num=="done":
        break
    try:
        val = int(num)
        temp = val
        sum = 0
        digit = 0
        while(temp>0):
            digit = temp%10
            sum  = sum+digit**3
            temp//=10
        if val == sum:
            print(val,"is Armstrong")
        else:
            print("Not a Armstrong")
    except:
        print("Invalid Input")
        continue
# program to chek armstrong number in an given intervals
while True:
    s = input("Enter the starting Range : ")
    if s=="done":
        break
    e= input("Enter the Ending Range : ")
    try:
        st = int(s)
        en = int(e)
        for i in range(st, en+1):
            temp = i
            sum = 0
            digit = 0
            while(temp>0):
                digit = temp%10
                sum+=digit**3
                temp//=10
            if(sum==i):
                print(i)

    except:
        print("Invalid input")
        continue
# program to Generate Fibbonacii Series
while True:
    num = input("\n Enter the Number of Terms : ")
    if num=="done":
        break
    try:
        val = int(num)
        a=0
        b=1
        count = 2
        sum = 0
        print(a,b,end=",")
        while(count<val):
            sum = a+b
            a=b
            b=sum
            count+=1
            print(sum,end="," )
    except:
        print("Invalid Input")
        continue
# Progam to generate fibbonacvi series ysing recursion
def fib(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)

for i in range(8):
    print(fib(i),end=
from mpl_toolkits import mplot3d
