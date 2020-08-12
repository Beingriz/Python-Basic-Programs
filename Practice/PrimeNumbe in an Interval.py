# progrm to chek prime numbers in an given intervals
while True:
    print("Enter Starting and Ending Range to Get Prime Number List")
    s=input("Enter Starting Range : ")
    s=s.lower()
    if s=="done":
        break
    e=input("Enter Ending Range : ")
    try:
        st = int(s)
        en = int(e)
        for i in range(st,en+1):
            for j in range(2,i):
                if i%j==0:
                     break
            else:
                print(i)
    except Exception as e:
        print(e,"\n Invalid Input")