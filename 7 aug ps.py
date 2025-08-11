# 12345
# 1234
# 123
# 12
# 1

rows=5
for i in range(rows,0,-1):# i=2
    for j in range(1,i+1): # 1, 3
        print(j,end="") # 12
    print()   


# 55555
# 4444
# 333
# 22
# 1

rows=5
for i in range(rows,0,-1): #i=2
    for j in range(1,i+1): #1,4, j=1,2,3
        print(i,end="")
    print()    
        

# 11111
# 2222
# 333
# 44
# 5

rows=5
for i in range(1,rows+1):#i=2
    for j in range(i,rows+1):# i,rows+1
                              # 2,6 
        print(i,end="") #11111
    print()  
    
# 12345
# 6789
# 101112
# 1314
# 15

rows=5
n=1
for i in range(1,rows+1):
    for j in range(i,rows+1):
        print(n,end="")
        n+=1
    print()    

# 1514131211
# 10987
# 654
# 32
# 1

rows=5
n=15
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(n,end="")
        n-=1
    print()   

# aaaaa
# aaaaa
# aaaaa
# aaaaa
# aaaaa

rows=5
for i in range(1,rows+1):
    for j in range(1,6):
        print(chr(90),end="")
    print()    
  
# KKKKK
# aaaaa
# KKKKK
# aaaaa
# KKKKK
rows=5
for i in range(1,rows+1):
    for j in range(1,6):
        if i % 2 == 0:
            print(chr(97),end="")
        else:
            print(chr(75),end="")
    print()        
            
            
# A
# BC
# DEF
# GHIJ
# KLMNO

rows=5
a=65
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(chr(a),end="")
        a+=1
    print()    


# ABCDE
# FGHI
# JKL
# MN
# O

rows=5
a=65
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(chr(a),end="")
        a+=1
    print()    

# o
# mn
# jkl
# fghi
# abcde


rows=5
a=111
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(chr(a),end="")
        a-=1
    print() 

# ABCDE
# ABCD
# ABC
# AB
# A

rows=5
for i in range(1,rows+1):
    for j in range(i,rows+1): #
        print(chr(64+j),end="")
    print()
