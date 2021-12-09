#to read the elements in a single line
"""
number of elements =5
elements in the list=10,20,30,40,50
"""
"""
n=int(input())
data=list(map(int,input().split()))
"""
# to read the elements in multiple lines
"""
number of elements =5
elements in the list
10
20
30
40
50
"""
"""
n=int(input())
data=[]
for i in range(n):
    val=int(input())
    data.append(val)
"""
#to print the values without list formate

"""
n=int(input())
data=list(map(int,input().split()))
print(*data)
"""
#to print the i value and element in the list by the index[index based]
"""
n=int(input())
data=list(map(int,input().split()))
for i in range(n):
    print(i,data[i])
"""
#for value based index
"""
n=int(input())
data=list(map(int,input().split()))
for v in data:
    print(v)
"""


#dictionaries

#to print the key values of dictionary
"""
dic={1:4,2:6,3:8}
for k in dic:
    print(k)
"""
# to print the values of dictionary
"""
dic={1:4,2:6,3:8}
for v in dic.values():
    print(v)
"""
#to print the key and values of dictionary
"""
dic={1:4,2:6,3:8}
for k,v in dic.items():
    print(k,v)
"""
    
