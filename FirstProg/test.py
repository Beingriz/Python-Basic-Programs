"""print("MD Rizwan")
a=20
b=800
c=250
d=320
s=(a+b+c+d)/4
print(s)
print(type(s))
print(int(s))
a=222
b=523
c=a+b
print(c)
print(float(c)
name=input("Enter the name\n")
print("welcome",name)
number=input("Enter the Number\n")
result=int(number)+15
print("Added Value ",result)
fnum=input("Enter the first number\n")
snum=input("Enter the 2nd number\n")
fres=int(fnum)
sres=int(snum)
sum=fres+sres
print('total=',sum)
fname=input("Enter First name\n")
sname=input("Enter  Last name\n")n
result=(fname)+sname
print('Welcome',result)
name = input("Enter the Name\n")
sname = input("Enter the Last Name \n")
print("Welcome",name, sname)
num1 = input("enter Bangalore Cases\n")
num2 = input("enter Mangalore Cases\n")
num3 = input("enter China Cases\n")
num4 = input("enter Hyderabad Cases\n")
result = (int(num1)+int(num2)+int(num3)+int(num4))/4
#result = result/4
print("Average Cases in all Cities",  result)
num1=input("Enter 1st num\n")
num2=input("Enter 2nd num\n")
sum=int(num1)+int(num2)
difference=float(num1)-float(num2)
product=int(num1)*int(num2)
divide=float(num1)/float(num2)
print("sum of 2 nos are\n",sum)
print("difference of 2 nos are\n",difference)
print("product of 2 nos are\n",product)
print("division of 2 nos are\n",divide)

a= input("Enter the a value\n")
b= input("Enter the b value\n")
c =input("Enther the c Value\n")
swap = a
a =b
b =c
c = swap
print("values after swap a =",a, "b=",b, "c= ",c  )

a=float(input("Enter the Fist Side \n"))
b=float(input("Enter the Second Side \n"))
c=float(input("Enter the Third Side \n"))
s= (a+b+c)/2
area  = (s*(s-a)*(s-b)*(s-c))**0.5
print("Area of triangle is %0.2f" %area)
import random
a=random.randint(10,2000)
st=input("Enter Student Name\n ")
print("Welcome to Oue Academy", st,  "Your Register Number Is ID=16HUSAC",a)
import calendar
yy = int(input("year"))
mm = int(input("Month"))

print(calendar.month(yy,mm))

num =float(input("enter the number \n"))

if num>0:
    print("Positive Number")
elif num ==0:
    print("Zero")
else:
    print("Negative Number")
print("End")
def checknum(num):
    if (num % 2)==0:
        return "Even"
    else:
       return  "Odd"

num = int(input("Enter the Numer : \n"))
checknum(num)
print(checknum(num))

def totalpay(day,rate):
    result = day*rate
    return result
day = input("enter days :")
rate =input("enter Rate : ")

try:
    fday = float(day)
    frate = float(rate)
    print(totalpay(fday,frate))
except :
    print("Error ! Please Enter Numeric Values...")
a=0
while(a<4):
    a=a+1
    print("Hello")
while True:
    a=input("Enter")
    if a=="done":
        break
    if a[0]=="@":
      continue
    print(a)
print("Done!")
print("for loop demo")

l= ["hi","we","are","learning","python"]
for i in l:
    print(i)
print("loop over")
large=-1
l =[3,5,4,5,44,74,54,1,11,4,11111]
for num in l:
    if num>large:
        large=num
print(" List of Numbers:\n", l ,"\n The Largest Value",large)

count = 0
sum =0
l = [1,10,11,12,14,14,11,15,14,111,412,415,14]
for i in l:
    count = count+1
    sum = sum+i
avg = sum/count

print("The Number of items Present in list are ",l, "Average of List are : %0.5f "%avg)

small = None
l = [1,2,3,4,5,6,0,34,]
for num in l:
    if small == None:
        small=num
    elif num < small:
        small = num
print(" LIST IS :", l , "the Smallest Value in List is : ", small)

l = [1,2,3,4,5,66,7,8,10,11,15]
print(" Available Numbers are \n ",l)
s = int(input("\nSearch \n"))
for num in l:
    if num == s:
        print("Available")
        break
    else:
       continue

sum = 0
count = 0
while True:
    inp = input("Enter the Data\n")
    if inp =="exit":
        break
    try:
        val = int(inp)
    except:
        print("Invalid Data ")
    count = count+1
    sum = sum+val
    print(count, sum, sum/count)
num = 0
tot = 0.0
while True:
   val = input("Enter a number: ")
   if val == 'done':
       break
   try:
       fval = float(val)
   except:
       print('Invalid')
       continue
   num = num + 1
   tot = tot + fval

print(tot,num,tot/num) """
sum=0
total=0
num = int(input("Enter the number"))
if(num>0):
  for i in range(0,num):
      sum+=i

  print(sum)



