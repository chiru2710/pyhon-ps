#write a program to find iteration of a given number and print all digits in it without type casting
#(or) Reveraing a number
n=int(input("enter a number: "))
while n>0:
    reminder=n%10
    print(reminder)
    n=n//10