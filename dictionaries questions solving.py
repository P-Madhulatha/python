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
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for j in data2:
    if j not in dic:
        dic[j]=1
    else:
        dic[j]+=1
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
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for j in data2:
    if j not in dic:
        dic[j]=1
    else:
        dic[j]+=1
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
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for j in data2:
    if j not in dic:
        dic[j]=1
    else:
        dic[j]+=1
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
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for j in data2:
    if j not in dic:
        dic[j]=1
    else:
        dic[j]+=1
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
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for j in data2:
    if j not in dic:
        dic[j]=1
    else:
        dic[j]+=1
a=[]
for k,v in dic.items():
    if v==2:
        a.append(k)
print(sum(a))
"""
#6)sum of non-common elements in two lists
"""
n=int(input())
data1=list(map(int,input().split()))
m=int(input())
data2=list(map(int,input().split()))
dic={}
for i in data1:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for j in data2:
    if j not in dic:
        dic[j]=1
    else:
        dic[j]+=1
a=[]
for k,v in dic.items():
    if v==1:
        a.append(k)
print(sum(a))
"""
#7)difference of sum of common and non-common elements in two lists
"""
n=int(input())
data1=list(map(int,input().split()))
m=int(input())
data2=list(map(int,input().split()))
dic={}
for i in data1:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for j in data2:
    if j not in dic:
        dic[j]=1
    else:
        dic[j]+=1
a=[]
b=[]
for k,v in dic.items():
    if v==2:
        a.append(k)
        c=sum(a)
    if v==1:
        b.append(k)
        nc=sum(b)
print(abs(c-nc))
"""
#8)maximum elements of a common elements from  two lists
"""
n=int(input())
data1=list(map(int,input().split()))
m=int(input())
data2=list(map(int,input().split()))
dic={}
for i in data1:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for j in data2:
    if j not in dic:
        dic[j]=1
    else:
        dic[j]+=1
a=[]
for k,v in dic.items():
    if v==2:
        a.append(k)
print(max(a))
"""
#9)minimum elements of a common elements from  two lists
"""
n=int(input())
data1=list(map(int,input().split()))
m=int(input())
data2=list(map(int,input().split()))
dic={}
for i in data1:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for j in data2:
    if j not in dic:
        dic[j]=1
    else:
        dic[j]+=1
a=[]
for k,v in dic.items():
    if v==2:
        a.append(k)
print(min(a))
"""
#10)maximum elements of a non-common elements from  two lists
"""
n=int(input())
data1=list(map(int,input().split()))
m=int(input())
data2=list(map(int,input().split()))
dic={}
for i in data1:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for j in data2:
    if j not in dic:
        dic[j]=1
    else:
        dic[j]+=1
a=[]
for k,v in dic.items():
    if v==1:
        a.append(k)
print(max(a))
"""
#11)minimum elements of a common elements from a two lists
n=int(input())
data1=list(map(int,input().split()))
m=int(input())
data2=list(map(int,input().split()))
dic={}
for i in data1:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for j in data2:
    if j not in dic:
        dic[j]=1
    else:
        dic[j]+=1
a=[]
for k,v in dic.items():
    if v==1:
        a.append(k)
print(min(a))
