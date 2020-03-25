import re
m,n = map(int,input().split())
matrix=[] ; char = [] ;script=[]
for i in range(m):
    matrix.append(input()) 
string = ''
for i in range(n):
    for j in range(m):
        string += matrix[j][i]
#print(string)
pattern = re.compile(r'(\w)(\W+)(\w)')
subs = pattern.sub(r'\1 \3',string)
print(subs)
