# prog to get Multiplication Table
"""while True:
    num = input("Enther the Table Number : ")
    if (num=="done"):
        break
    try:
        table = int(num)
        for i in range(1,10+1):
            sum = i*table
            print(num,"x",i,"=",sum)

    except:
        print("Invalid Input")
        continue"""


# progrm to find Square root
num = int(input(" Enter the number"))
num2 = int(input(" Enter the number"))
num3 = int(input(" Enter the number"))
s =  (num+num2+num3)/2
area = (s*(s-num)*(s-num2)*(s-num3))**0.5
print(area)
