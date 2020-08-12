# Prog To Find Positive, Negative & Zero
count = 0
sum = 0
while True:
    num = input("Enter the Number : ")
    if num =="Exit":
        break

    try:
        inum = int(num)
        if (inum > 0):
            print("Positive Number")
        elif (inum < 0):
            print("Negative Number")
        else:
            print("Zero")
    except:
        print("Invalid Input! Please Enter Number")
        continue
    count = count+1
    sum = sum+inum
print("Total = :", sum , "Iterations = :", count, "Average = :" ,sum/count)
