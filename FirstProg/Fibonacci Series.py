# Program to Find Fibonacci Series
num=int(input("Enter the Number : "))
a=0
b=1
count = 2
#print(a,b,end=",")
while (count < num):
    sum = a+b
    a=b
    b=sum
    count+=1
    if(sum==num):
        print("Yes")
        break
else:
    print("No")
