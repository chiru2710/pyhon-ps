#tables using for loop
n=int(input("Enter a value: "))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")
#3 table
print("3 Table")
for i in range(1,11):
    print(f"{3} * {i} = {3*i}")

#for multiple tables at a time
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
    print("-------------------")

#patterns
#star
#1 --> * *
#      * *
for i in range(1,3):
    for j in range(1,3):
        print("*",end="")
    print()
#2
# *
# * *
# * * *
# * * * *
# * * * * *
for i in range(1,6):
    print(i * "*")
#reverse of 2nd problem
for i in range(5,0,-1):
    print(i * "*")
#numbers
for i in range(1,11):
    for j in range(1,11):
        print(j,end="")
    print()

# 1
# 22
# 333
# 4444
# 55555
for i in range(1,6):
    print(str(i) * i)
#reverse
for i in range(5,0,-1):
    print(str(i) * i)

# 1
# 12
# 123
# 1234
# 12345
n=int(input("enter the value: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

# 1
# 22
# 333
# 4444
# 55555
n=int(input("enter the value: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()

n = 1  # Starting number

rows = int(input("enter a no of rows :-- "))  # User input for number of rows

for i in range(1, rows + 1):  # Outer loop for each row
    for j in range(1, i + 1):  # Inner loop for numbers in each row
        print(n, end="")  # Print the current number without newline
        n += 1  # Increment the number
    print()  # Move to the next line after each row

# ****1
# ***21
# **321
# *4321
# 54321
rows=5
for i in range(1,rows+1):
    print(" " * (rows-i),end="")
    for j in range(i,0,-1):
        print(j,end="")
    print()
# ****1
# ***12
# **123
# *1234
# 12345
rows=5
for i in range(1,rows+1):
    print(" " * (rows-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    print()
# ****1
# ***22
# **333
# *4444
# 55555
rows=5
for i in range(1,rows+1):
    print(" " * (rows-i),end="")
    for j in range(1,i+1):
        print(i,end="")
    print()
