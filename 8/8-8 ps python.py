# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
n=5
k=4
for i in range(1,n*2):
    if i<=5:
        print("*" * i)
    else:
        print("*" * k)
        k-=1
# 1
# 01
# 101
# 0101
# 10101
rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
        if (i+j)%2==0:
            print(1,end="")
        else:
            print(0,end="")
    print()
# 1      1
# 12    21
# 123  321
# 12344321
rows=4
for i in range(1,rows+1):
    logic=(rows*2)-(i*2)
    for j in range(1,i+1):
        print(j,end="")
    print(" "*logic,end="")
    for j in range(i,0,-1):
        print(j,end="")
    print()
