# Program to Show the Power of 2 using Ananymos / Lambda Functio
while True:
    num = input("Enter the number : ")
    if(num=="done"):
        break
    try:
        val = int(num)
        for i in range(val+1):
            sq = lambda i : i**2
            print(i,"Power of 2 =",sq(i))
    except:
        print("Invalid Input")
        continue
