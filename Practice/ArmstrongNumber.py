#program to chek the number is armstrong or not
while True:
    number = input("Enter the Number to : ")
    if number == "done":
        break
    try:
        val = int(number)
        temp = val
        sum = 0
        while(temp>0):
            digit = temp%10
            sum = sum+digit**3
            temp//=10
        if sum==val:
            print("Numbe is armstrong",val)
        else:
            print("not an armstrong")
    except Exception as e:
        print(e, "\n Invalid Literal")