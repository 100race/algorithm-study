import sys
#sys.stdin = open("input.txt","rt") #채점시 꼭 주석처리 할것

c,n = map(int,(input().split()))
#lst = list(map(int,input().split()))
lst =[]
for i in range(n):
    lst.append(int(input()))
    


def DFS(L,sum,tsum):
    global max_s
    if sum+(total-tsum) < max_s:
        return
    if sum > c: 
        return
    elif L ==n :
        if sum > max_s:
            max_s = sum
        return
    else:    
        DFS(L+1,sum+lst[L],tsum+lst[L]) #현재강아지선택
        DFS(L+1,sum,tsum+lst[L]) #현재강아지선택x

total = sum(lst)
max_s = -1
DFS(0,0,0)
print(max_s)
