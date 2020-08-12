#program of sum of natural nos
num=int(input("Enter the number"))
sum=0
if (num<0):
    print("Enter valid number")
elif(num==1):
    print(1)
else:
    for i in range(1,num+1):
        sum=sum+i
    print(sum)

