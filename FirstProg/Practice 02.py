#prime no

"""while True:
    num=input("Enter the number:\n")
    if(num=="exit"):
        break
    try:
        inum=int(num)

        if(inum>0):
            for i in range(2,inum):
                if(inum%i==0):
                    print("It is not a Prime")
                    break
            else:
                print ("It is a Prime")

    except:
        print("Enter valid no")

        continue
#prime interval program

lower=int(input("Enter the lower limit:\n"))
upper=int(input("Enter the upper limit\n"))
for num in range(lower,upper+1):
    for i in range(2,num):
        if(num%i==0):
            break
    else:
        print(num)
#armstrong

num=int(input("Enter the number"))
temp=num
sum=0
while(temp>0):
    digit=temp%10
    sum=sum+digit**3
    temp//=10
if(sum==num):
    print("Armstrong num")
else:
   print("Not a armstrong number")
#armstrong range
lower=int(input("Enter the lower limit:\n"))
upper=int(input("Enter the upper limit:\n"))
for num in range(lower,upper+1):
    temp=num
    sum=0
    while(temp>0):
        digit=temp%10
        sum=sum+digit**3
        temp//=10
    if(sum==num):
        print(num)
#fibonacci
num=int(input("Enter the number:\n"))
a=0
b=1
count=2
print(a,b,end=",")
while(count<num):
    sum=a+b
    a=b
    b=sum
    count=count+1
    print(sum,end=",")
#compound interest
def compound(p,t,r,n):
    ci=p*pow((1+(r/n)),t*n)
    print(ci)
compound(5000,10,0.05,12)
#simple interest
def simple(p,t,r):
    si=(p*t*r)/100
    print(si)
simple(100,2,2)
#ascii
char=input("Enter the character:\n")
val=ord(char)
print(val)
#sum of squares
num=int(input("Enter the number:\n"))
sum=0
for i in range(1,num+1):
    sq=i**2
    sum=sum+sq
print(sum)
#even/odd
lower=int(input("Enter the lower limit:\n"))
upper=int(input("Enter the upper limit:\n"))
for num in range(lower,upper):
    if(num>0):
        for i in range(0,num):
            if (i%2==0):
                print("Even",i, end="," "\n")
                break
            else:
                print("odd",i, end=",""\n")
                break

while True:
    s=input("Enter Starting Range : ")
    if (s=="exit"):
        break
    e=input("Enter Ending Range : ")
    try:
        iss = int(s)
        ie =int(e)
        if(iss>0):
            for i in range(iss,ie+1):
                for j in range(1,i):
                    if(i%2==0):
                        print("Even",i, end=",")
                        break
                    else:
                        print("odd",i)
                        break
        else:
            print("Enter Valid Number!...")
    except:
        print("Invalid Input")
        continue
data="nigarsp@gmail.com 05 dec 1994 monday"
atpos=data.find("@")
print(atpos)
stpos=data.find(' ',atpos)
print(stpos)
host=data[atpos+1:stpos]
print(host)
#leap year
year=int(input("enter the year"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not a leap year")


f=open("file.txt")
for i in f:
    i=i.rstrip()
    print(i.upper())

l = [54,10,11,151,15,"Hi","Hello","Bye","c u"]
var1 = l[:]
print(var1)

empty = list()
empty.append(100)
empty.append(80)
empty.append(52)
empty.append(60)
empty.sort()
print(empty)
total = sum(empty)*len(empty)
print(total)
for i in empty:
    print(i)
print(int(total))
if 80  in empty:
    print("yes")

st = "sa s d as asd asd adcad@asdada @das @fasdsa"
lst = st.split()
print(len(lst))
email = lst[6]
print(email)
domain = email.split("@")
print(domain[1])
for i in lst:
    print(i)

x = list(range(3))
print(x)
a = [1,2,3]
b= [4,5,6]
c= a+b
print(len(c))
fh = open("file.txt", "r")
read = fh.read()
lst = read.split("\n")
for i in lst:
    lst2 = i.split()
    print(lst2[2])

han = open ('file.txt')
for line in han:
    line = line.rstrip()
    wds = line.split()
    if len(wds)<3 or wds[0]!='From' :
        continue
    print(wds[2])
dir = dict()
dir['a']=1
dir['c']=5
dir['e']=45
dir['d']=35
dir['b']=18
l =list()
for i,j in dir.items():
    l.append((j,i))
print(l)
sor = sorted(l,reverse=True)
print(sor)
dir = dict()
dir['a']=1
dir['c']=5
dir['e']=45
dir['d']=35
dir['b']=18
print( sorted(  [ (v,k) for k,v in dir.items()] ))
t = tuple()
print(t)
num = int(input("Enter the Number : "))
fact = list()
for i in range(1,num+1):
    if (num%i==0):
        fact.append(i)
print(fact)

num = int(input("Enter the number : "))
print(" The Factors of", num,"are")
def fact(x):
    for i in range(1,x+1):
        if (x%i==0):
            print(i)
fact(num)
import calendar
mm = int(input("Enter Month"))
yy = int(input("Enter Year"))
print(calendar.month(yy,mm))

#simple calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print("1.addition\n")
print("2.Subtraction\n")
print("3.multiplication\n")
print("4.Division\n")
i=input(" enter the choice:\n")
while True:
    if i  in ('1','2','3','4'):
        a=int(input("Enter a number:\n"))
        b=int(input("Enter another number:\n"))
        if i=='1':
            print(add(a,b))
        elif i=='2':
            print(sub(a,b))
        elif i=='3':
            print(mul(a,b))
        elif i=='4':
            print(div(a,b))
        break
    else:

        print("Invalid ")
        break

# program to Display Fibbonaci Series
num = int(input("Enter The Number : "))
def fib(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return x+(fib(x-1))
print("Sum of First",num,"Natural Numbers are ", fib(num))

st = list(input("Enter the string to check pallindrome \n"))
vowel =  "aeiouAEIOU"
count=0
lst=list()
for i in st:
    if i in vowel:
        lst.append(i)
        count+=1
print(count)
print(lst)
# Program to Demonstrate a Simple Dictionary to get the Meaning of a Word
di= {"Set":"A Colletion of words", "Delima":"Confusion","Rizwan":"Jannat ka Darogha"}
while True:
    key = input("Enter the Word to know meaning : ")
    if key == "done":
        break
    try:
        if key in di.keys():
            print("Meaning of",key,"is", di[key])

    except:
        print("Sorry No Meaning Available")
        continue
s1 = set()
s2 = set()
while True:
    ele1 =  input("enter the Element to add on set 1 : ")
    if ele1 == "done":
        break
    ele2 = input("enter the Element to add on set 2 : ")
    if ele2 == "done":
        break
    else:
        s1.add(ele1)
        s2.add(ele2)
        print("Set 1 : ", s1)
        print("Set 2: ",s2)
print("Please Select any 1 operation")
print("1. Union")
print("2. Intersection")
print("3. Disjoint")
while True:
    inp = input("Enter your Choice : ")
    if inp=="done":
        break
    if inp in ("1","2","3"):
        if inp=="1":
            un = s1.union(s2)
            print("Union of  Set is : ", un)
        elif inp =="2":
            inter = s1.intersection(s2)
            print("Intersection of Set is : ", inter)
        elif inp == "3":
            joi = s1.isdisjoint(s2)
            print("Disjoint of set is ", joi)
        else:
            print("Invalid Choice")

x=[[1],[2],[3],[4]]
y = [0,0,1,1]
from sklearn.neighbors import KNeighborsClassifier
n = KNeighborsClassifier(n_neighbors=3)
n.fit(x,y)
print(n.predict([[1.1],[2.1],[0.1],[8.1]])) """

