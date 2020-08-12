#prog to find simple interest
"""p=int(input("Enter the principle: "))
t=int(input("Enter the time: "))
r=int(input("Enter the rate: "))
if(p>0):
    if(t>0):
        if(r>0):
            si=(p*t*r)/100
            print("Simple interest is:%0.2f" %si)
        else:
            print("Enter valid rate")
    else:
        print("Enter valid time")
else:
    print("Enter valid principle")"""


# Program to Find Simple Interest Using Function and try & Except
def simpleinterest(p,t,r):
    si = (p*t*r)/100
    print("Simple Interest is : %0.2f"%si)

p=input("Enter the principle: ")
t=input("Enter the time: ")
r=input("Enter the rate: ")
try:
    ip = int(p)
    it = int(t)
    ir = int(r)
    simpleinterest(ip,it,ir)
except:
    print("Please Enter Valid Inputs!...")
