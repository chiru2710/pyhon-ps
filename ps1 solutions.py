#1. Area of Square
#Question: Calculate the area of a square.
# Formula: Area = side × side - Input: - Side = 5 - 
side=int(input("enter side value: "))
area=side*side
print("Area of Sqaure: ",area)

#2. Area of Rectangle
#Question: Calculate the area of a rectangle.
# Formula: Area = length × breadth 
length=int(input("Enter a Length of Rectangle: "))
breadth=int(input("Enter a Breadth of Rectangle: "))
area=length*breadth
print("Area of Rectangle: ",area)

# 3. Area of Triangle
# Question: Calculate the area of a triangle using base and height.
#Formula: Area = (1/2) × base × height 
base=float(input("Enter base: "))
height=float(input("Enter height: "))
area=0.5*base*height
print("Area of Triangle: ",area)

#4. Perimeter of Square
#Question: Calculate the perimeter of a square.
#Formula: Perimeter = 4 × side
side=int(input("Enter a side value: "))
Perimeter = 4 * side
print("Perimeter of Square: ",Perimeter)

#5. Perimeter of Rectangle
#Question: Calculate the perimeter of a rectangle.
#Formula: Perimeter = 2 × (length + breadth) 
length=int(input("Enter a Length of Rectangle: "))
breadth=int(input("Enter a Breadth of Rectangle: "))
perimeter=2*(length+breadth)
print("Perimeter of Rectangle: ",perimeter)

#6. Perimeter of Triangle
#Question: Calculate the perimeter of a triangle.
#Formula: Perimeter = side1 + side2 + side3 
s1=int(input("enter side1 value: "))
s2=int(input("enter side2 value: "))
s3=int(input("enter side3 value: "))
Perimeter = s1 + s2 + s3 
print("Perimeter of Triangle: ",Perimeter)

#7. Break Amount into 1000s, 500s, and Remaining Change
#Question: Break the total amount into denominations.
amount = int(input("Enter amount: "))
th = amount // 1000
rem1 = amount % 1000
five = rem1 // 500
rem2 = rem1 % 500
print("Rs/-1000 notes:", th)
print("Rs/-500 notes:", five)
print("Remaining change: Rs/-", rem2)

#8. Convert Seconds into Hours, Minutes, and Seconds
#Question: Convert total seconds into hours, minutes, and seconds.
input= 3672 
hour=input//3600
rem1=input%3600
minute=rem1//60
rem2=rem1%60
print("hours : ",hour)
print("minutes: ",minute)
print("Seconds:", rem2)

#9. Sum of Marks (Maths, Physics, Chemistry)
#Question: Calculate the sum of marks in 3 subjects
Maths = 85
Physics = 90
Chemistry = 88 
total=Maths+Physics+Chemistry
print("Sum of Marks (Maths, Physics, Chemistry): ",total)

#10. Average of Marks (Maths, Physics, Chemistry)
#Question: Calculate the Average of marks in 3 subjects
Maths = 85
Physics = 90
Chemistry = 88 
total=Maths+Physics+Chemistry
average=total/3
print("Average of Marks (Maths, Physics, Chemistry): ",float(average))