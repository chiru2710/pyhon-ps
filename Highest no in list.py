
l=[1,5,2,3,8,6]
l.sort()
print(l)
print("Second Highest Number in The list is: ",l[-2])


#Method-1 -->Removing Duplicates in the list
#find second highest number in list
l=[1,5,2,3,8,6,1,5]
#for removing Duplicates we are converting list in set
s=set(l)
print(type(l))
print(type(s))
l1=list(s)  #converting set into list
l1.sort() #used for sorting
print(l1)
print("Second Highest Number in The list is: ",l1[-2])


#Method-2 --> Removing Duplicates in the list
l=[1,5,2,3,8,6,1,5]
ans=[]
for i in l:
    if i not in ans:
        ans.append(i)
print(ans)
ans.sort()
print("Highest Number in The list is: ",ans[-1])
    