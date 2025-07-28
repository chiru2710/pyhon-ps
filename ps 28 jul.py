#write a program to find iteration of a given number and print all digits in it without type casting
#(or) Reveraing a number
n=int(input("enter a number: "))
while n>0:
    reminder=n%10
    print(reminder)
    n=n//10
'''OUTPUT:
enter a number: 65489
9
8
4
5
6'''
#print sum of odd and even numbers
n=int(input("enter a number: "))
evensum=0
oddsum=0
while n>0:
    digit =n%10
    print(digit)
    if digit%2==0:
        evensum+=digit
    else:
        oddsum+=digit
print("Even Sum: ",evensum)
print("Odd Sum: ",oddsum)

#iterate a number and find no.of digits in it
n = int(input("Enter a number: "))
count = 0
while n > 0:  # Example input: 1234
    digit = n % 10
    count += 1
    n = n // 10
print(count, "total number of digits in the number")

#