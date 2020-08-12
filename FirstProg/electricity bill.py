"""nput: U = 250
Output: 3500
Explanation:
Charge for the first 100 units – 10*100 = 1000
Charge for the 100 to 200 units – 15*100 = 1500
Charge for the 200 to 250 units – 20*50 = 1000
Total Electricity Bill = 1000 + 1500 + 1000 = 3500

Input: U = 95
Output: 950
Explanation:
Charge for the first 100 units – 10*95 = 950
Total Electricity Bill = 950"""
# Program to Calculate Electricity Bill
unit = int(input("Enter the Number of Units : "))
def unitcal(x):
    if x==0:
        return 0
    elif x<=100:
        return x*10
    elif x<=200:
        return ((100*10)+((x-100)*15))
    elif x<=300:
        return ((100*10)+(100*15)+(x-200)*20)
    else:
        return ((100*10)+(100*15)+(100*20)+((x-300)*25))
print("Total Bill for ",unit ,"units is", unitcal(unit))