# to print even and odd count in a list
"""
i/p:7
    22 44 55 42 11 66 55
o/p:4 3
"""
"""
n=int(input())
data=list(map(int,input().split()))
ec,oc=0,0
for i in data:
    if i%2:
        oc+=1
    else:
        ec+=1
print(ec,oc)
"""
#by using dictionaries
"""
#method-1
n=int(input())
data=list(map(int,input().split()))
dic={0:0,1:0}
for i in data:
    dic[i%2]+=1
for v in dic.values():
    print(v,end=" ")
"""
"""
#method-2
n=int(input())
data=list(map(int,input().split()))
dic={}
for i in data:
    k=i%2
    if k not in dic:
        dic[k]=1
    else:
        dic[k]+=1
for v in dic.values():
    print(v,end=" ")
"""
#to print the number of elements with the same digit in a number
"""
i/p:
11
564 786 453 786 234 321 456 676 463 236 120
o/p:
4 2
6 5
3 2
1 1
0 1
"""
"""
n=int(input())
data=list(map(int,input().split()))
dic={}
for i in data:
    r=i%10
    if r not in dic:
        dic[r]=1
    else:
        dic[r]+=1
for k,v in dic.items():
    print(k,v)
"""
# to print in an sorted order
"""
n=int(input())
data=list(map(int,input().split()))
dic={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
for i in data:
    dic[i%10]+=1
for k,v in dic.items():
    if v!=0:
        print(k,v)
"""
#to print the minimum values of an dictionary
"""
n=int(input())
data=list(map(int,input().split()))
dic={}
for i in data:
    r=i%10
    if r not in dic:
        dic[r]=1
    else:
        dic[r]+=1
mi=min(dic.values())
for k,v in dic.items():
    if v==mi:
        print(k,v)
"""
# print the unique values in a dictionary
n=int(input())
data=list(map(int,input().split()))
dic={}
for i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
ma=max(dic.values())
a=[]
for k,v in dic.items():
    if v==ma:
       a.append(k)
       b=a[-1]
print(b,ma)
        
        
       
    
       
    
