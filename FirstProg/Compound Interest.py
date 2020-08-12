# Program to Find Compound Interst
def compound(p,t,r,n):
    ci= p*pow(1+(r/n), n*t)
    print("Compound Interest is : %0.2f"%ci)



p = input("Enter Principal : ")
t = input("Enter Time : ")
r = input("Enter Rate : ")
n = input("Enter the No of Time Interest : ")
try:
    ip = int(p)
    it = int(t)
    ir = float(r)
    inn = int(n)
    compound(ip,it,ir,inn)
except:
    print("Enter the Valid Input!....")

