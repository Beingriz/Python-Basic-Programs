# Prog to Find Prime Numbers in an Given Intrvals
while True:
    lower=input("Enter Starting Range : ")
    if (lower=="done"):
        break
    upper=input("Enter Ending Range : ")

    try:
        ilower=int(lower)
        iupper =int(upper)
        for num in range(ilower,iupper+1):
            if(num>1):
                for i in range(2,num):
                    if(num%i==0):
                        break
                else:
                    print(num)
    except:
        print("Enter valid data")
        continue

# Sum of n natural numbers
