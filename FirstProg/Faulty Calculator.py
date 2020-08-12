# Program to DIsplay Faulty results for the following operation and rest all operations will be Correctly
# s0lved

print("Choos the Operation \n 1. Addition \n 2. Multiplicaiton \n 3. Division ")
op = int(input())
if op in (1,2,3):
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))
    if op==1:
        if (num1==56 and num2 == 9):
            print(77)
        else:
            sum = num1+num2
            print(sum)
    elif op ==2:
        if (num1==56 and num2 == 3):
            print(555)
        else:
            mul = num1*num2
            print(mul)
    else:
        if (num1==56 and num2 == 6):
            print(4)
        else:
            div = num1/num2
            print(div)
else:
    print("Choose from Aove operations")



