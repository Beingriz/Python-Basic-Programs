#program to chek the given number is a prime or not
while True:
    print("Enter the Number to chek Prime or Not:")
    num =  input()
    low = num.lower()
    if low =="done":
        break
    try:
        val = int(low)
        for i in range(2,val):
            if val%i==0:
                print(val,"Not a Prime")
                break
        else:
            print(val, "is Prime")
    except Exception as e:
        print(e,"\n Invalind Input")