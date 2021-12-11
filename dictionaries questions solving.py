"""
6
1 2 6 5 4 7
8
8 7 9 4 5 3 2 1
NOTE:lists having unique elements
"""
#1)common elements in the two lists
"""
n=int(input())
data1=list(map(int,input().split()))
m=int(input())
data2=list(map(int,input().split()))
dic={}
for i in data1:
    dic[i]=1
for i in data2:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for k,v in dic.items():
    if v==2:
        print(k,end=" ")
"""
#2)non common elements in two lists
"""
n=int(input())
data1=list(map(int,input().split()))
m=int(input())
data2=list(map(int,input().split()))
dic={}
for i in data1:
    dic[i]=1
for i in data2:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for k,v in dic.items():
    if v==1:
        print(k,end=" ")
"""
#3)common elememts count in two lists
"""
n=int(input())
data1=list(map(int,input().split()))
m=int(input())
data2=list(map(int,input().split()))
c=0
dic={}
for i in data1:
    dic[i]=1
for i in data2:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for k,v in dic.items():
    if v==2:
        c+=1
print(c)
"""
#4)non-common elements count in two lists
"""
n=int(input())
data1=list(map(int,input().split()))
m=int(input())
data2=list(map(int,input().split()))
nc=0
dic={}
for i in data1:
    dic[i]=1
for i in data2:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for k,v in dic.items():
    if v==1 and v!=0:
        nc+=1
print(nc)
"""
#5)sum of common elements in two lists
"""
n=int(input())
data1=list(map(int,input().split()))
m=int(input())
data2=list(map(int,input().split()))
dic={}
for i in data1:
    dic[i]=1
for i in data2:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
s=0
for k,v in dic.items():
    if v==2:
        s+=k
        print(s)
"""
#6)sum of non-common elements in two lists
"""
n=int(input())
data1=list(map(int,input().split()))
m=int(input())
data2=list(map(int,input().split()))
dic={}
for i in data1:
    dic[i]=1
for i in data2:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
s=0
for k,v in dic.items():
    if v==1:
        s+=k
        print(s) 
"""
#7)difference of sum of common and non-common elements in two lists
"""
n=int(input())
data1=list(map(int,input().split()))
m=int(input())
data2=list(map(int,input().split()))
dic={}
for i in data1:
    dic[i]=1
for i in data2:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
s1,s2=0,0
for k,v in dic.items():
    if v==2:
        s1+=k
    if v==1:
        s2+=k
print(abs(s1-s2))
"""
#8)maximum elements of a common elements from  two lists
"""
n=int(input())
data1=list(map(int,input().split()))
m=int(input())
data2=list(map(int,input().split()))
dic={}
for i in data1:
    dic[i]=1
for i in data2:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
m=0
for k,v in dic.items():
    if v==2:
        if m<k:
            m=k
print(m)
"""
#9)minimum elements of a common elements from  two lists
"""
n=int(input())
data1=list(map(int,input().split()))
m=int(input())
data2=list(map(int,input().split()))
dic={}
for i in data1:
    dic[i]=1
for i in data2:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
m=10**3
for k,v in dic.items():
    if v==2:
        if m>k:
            m=k
print(m)
"""
#10)maximum elements of a non-common elements from  two lists
"""
n=int(input())
data1=list(map(int,input().split()))
m=int(input())
data2=list(map(int,input().split()))
dic={}
for i in data1:
    dic[i]=1
for i in data2:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
m=0
for k,v in dic.items():
    if v==1:
        if m<k:
            m=k
print(m)
"""
#11)minimum elements of a common elements from a two lists
n=int(input())
data1=list(map(int,input().split()))
m=int(input())
data2=list(map(int,input().split()))
dic={}
for i in data1:
    dic[i]=1
for i in data2:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
m=10**3
for k,v in dic.items():
    if v==1:
        if m>k:
            m=k
print(m)
