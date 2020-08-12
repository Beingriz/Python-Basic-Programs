# prog to Find Sum of Square of First N Natural Numbers
num = int(input("Enter the Natural Number : "))
sum = 0
total = 0
if(num>0):
    print("=",end=" ")
    for i in range(1,num+1):
        sum =i**3
        total +=sum
        print(sum,end="+" )

else:
    print("Invalid Input")
print("=",total)
