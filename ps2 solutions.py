#1. Check Even or Odd
#Question: Determine whether a number is even or odd
#Explanation: A number is even if it is divisible by 2 Otherwise, it’s odd
a=int(input("enter a Number to check Even or Odd: "))
if a%2==0:
     print("It's a Even number")
else:
   print("It's a Odd number")

#2. Divisible by 5 but Not by 10
#Question: Check if a number is divisible by 5 but not by 10
#Explanation: Use modulo (%) to check if the number % 5 == 0 and number % 10 != 0. 
num = int(input("Enter a Number: "))
if num%5==0 and num%10!=0:
    print("Satisfy")
else:
    print("Not Satisfy")

#3.Biggest Among Two Numbers
#Question: Find the biggest number among two.
#Explanation: Use comparison operators (>) to check which number is greater.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if a>b:
    print("Biggest number is: ",a)
else:
    print("Biggest number is: ",b)

#4. Smallest Among Two Numbers
#Question: Find the smallest number among two. 
#Explanation: Use comparison operators (<) to find the smaller value. 
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if a<b:
    print("Smallest number is: ",a)
else:
    print("Smallest number is: ",b)

#5. Divisible by 2, 3, and 6
#Question: Check if a number is divisible by 2, 3, and 6. 
# Explanation: If a number is divisible by both 2 and 3, it is also divisible by 6
num = int(input("Enter a number: "))
if num % 2 == 0 and num % 3 == 0 and num % 6 == 0:
    print("Satisfy")
else:
    print("Not Satisfy")

#6.Voting Eligibility
#Question: Check if a person is eligible to vote (age >= 18). 
#Explanation: A person is eligible to vote if their age is 18 or above
age=int(input("Enter your Age: "))
if age>=18:
    print("Eligible for voting")
else:
    print("Not Eligible for voting")

#7. Student Pass/Fail Based on All Subjects >= 35
#Question: Check if a student passed all subjects (maths, physics, chemistry). 
#Explanation: Student passes only if marks in all subjects are 35 or more.
m=int(input("Enter marks in Maths: "))
p=int(input("Enter marks in Physics: "))
c=int(input("Enter marks in Chemistry: "))
if m>=35 and c>=35 and p>=35:
    print("Pass")
else:
    print("Fail")

#8.Student Pass if Passed Any One Subject (>= 35)
#Question: Check if the student passed at least one subject. 
#Explanation: Use logical OR to check if any one subject has marks >= 35. 
m=int(input("Enter marks in Maths: "))
p=int(input("Enter marks in Physics: "))
c=int(input("Enter marks in Chemistry: "))
if m>=35 or c>=35 or p>=35:
    print("Pass")
else:
    print("Fail")

#9. Student Pass if Passed Any Two Subjects
#Question: Check if the student passed any two out of three subjects. 
#Explanation: Use a counter or logical conditions to verify two subjects >= 35. 
m=int(input("Enter marks in Maths: "))
p=int(input("Enter marks in Physics: "))
c=int(input("Enter marks in Chemistry: "))
passed=0
if m>=35:
    passed+=1
if p>=35:
    passed+=1
if c>=35:
    passed+=1
if passed>=2:
    print("Pass")
else:
    print("Fail")

#10. Biggest Among Three Numbers
#Question: Find the biggest number among three. 
#Explanation: Compare each pair of numbers using if-else conditions
a=int(input("Enter First number: "))
b=int(input("Enter Second number: "))
c=int(input("Enter Third number: "))
if a>=b and a>=c:
    print("First number is biggest number: ",a)
elif b>=a and b>=c:
    print("Second number is biggest number: ",b)
else:
    print("Third number is biggest number: ",c)

#11. Smallest Among Three Numbers
#Question: Find the smallest number among three. 
#Explanation: Use comparison logic to determine the minimum value. 
a=int(input("Enter First number: "))
b=int(input("Enter Second number: "))
c=int(input("Enter Third number: "))
if a<=b and a<=c:
    print("First number is Smallest number: ",a)
elif b<=a and b<=c:
    print("Second number is Smallest number: ",b)
else:
    print("Third number is Smallest number: ",c)

#12. Perfect Square or Not
#Question: Check if a number is a perfect square. 
#Explanation: A number is a perfect square if the square of its square root equals the number.
import math
n = int(input("Enter a number: "))
root = int(math.sqrt(n))
if root * root == n:
    print("Perfect square")
else:
    print("Not a perfect square")

#13. Cars Required for Members (Max 5 per car)
#Question: Calculate how many cars are needed for a given number of people. 
#Explanation: Divide total people by 5 and round up using ceiling logic. 
import math
members=int(input("Enter number of people: "))
car_capacity=5
if members>0:
    car_count=math.ceil(members/car_capacity)
    print("cars are needed: ",car_count)
else:
    print("no cars are needed")

#14. Second Biggest Among Three Numbers
#Question: Find the second largest number among three inputs.
#Explanation: Use sorting or nested conditions to find the second largest value.
#First way
items = list(map(int, input("Enter 3 numbers separated by space: ").split()))
items.sort()
print("Second largest number is:", items[1])
#second way
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b:
    if a < c:
        second = a
    elif b > c:
        second = b
    else:
        second = c
else:
    if b < c:
        second = b
    elif a > c:
        second = a
    else:
        second = c
print("Second largest number is:", second)

#15. Leap Year or Not
#Question: Check if a given year is a leap year. 
#Explanation: A year is a leap year if it is divisible by 4, and (not divisible by 100 unless divisible by 400). 
year=int(input("Enter Year: "))
if year%4==0 and year%100!=0 or year%400==0:
    print("It is a Leap year: ",year)
else:
    print("It is not a Leap year: ",year)