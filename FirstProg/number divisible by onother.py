# Program to Chek the Number is Divisible by onothe Number
lst = list()
while True:
    num = input("Enter the List Itmes : ")
    if (num=="done"):
        break
    try:
        val = int(num)
        lst.append(val)
    except:
        print("Invalid input")
        continue
di = int(input("Enter the Number to chek the Divisibility : "))
newlst = list(filter(lambda x:(x%di==0),lst))
print("Even Number list is", newlst)