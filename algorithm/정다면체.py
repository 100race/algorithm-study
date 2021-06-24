import sys
#sys.stdin = open("input.txt","rt") #채점시 꼭 주석처리 할것

n,m = map(int,input().split())
#scores = list(map(int,input().split()))

sumdict = dict()

for i in range(1,n+1):
    for j in range(1,m+1):
        try:
            sumdict[i+j] += 1
        except: #없으면
            sumdict[i+j] = 1

m = max(sumdict.values())
for k,v in sumdict.items():
    if v == m:
        print(k, end=" ")

