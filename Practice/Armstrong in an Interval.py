#program to get the list of Armstrong numbers in an given interval
while True:
    s= input("Enter the Starting Range : ")
    if s=="done":
        break
    e = input("Enter Ending Range : ")
    try:
        st = int(s)
        en = int(e)
        for i in range(st, en+1):
            temp = i
            sum=0
            digit = 0
            while(temp>0):
                digit = temp%10
                sum+=digit**3
                temp//=10
            if sum==i:
                print(i)
    except Exception as e:
        print(e, "\n Invalid Input")