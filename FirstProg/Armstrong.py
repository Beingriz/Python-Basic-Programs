# Program to Find Number is Armstrong In an Interval

num1 = int(input("Enter Starting Range : "))
num2 = int(input(" Enter Ending Range : "))

for i in range(num1, num2+1):
    sum = 0
    temp=i
    while(temp>0):
        digit = temp%10
        sum+=digit**3
        temp//=10
        if sum == i:
            print(i)

print (1//10)