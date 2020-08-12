# Pecentage Calculation for all Semister
count = 0
num=0
while True:
    sem = input("Enter the Marks Obtained \n")
    if sem=="done":
        break
    tot = input("Enter the  Total Marks \n")
    try:
        semister = int(sem)
        total = int(tot)
        per = (semister/total)*100
        print("percetage %0.2f"%float(per))
        num = num+1
        count += per
        print("Total Average %0.2f"%float(count/num))
    except Exception as e:
        print(e)