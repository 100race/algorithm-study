import sys
#sys.stdin = open("input.txt","rt") #채점시 꼭 주석처리 할것

n = int(input())
lst = list(map(int,input().split()))
res1 = [0]*n
res2 = [0]*n
def DFS(v):
    if sum(res1) == sum(res2): #두 부분집합의 합이 같으면
        return "YES"
    
    res1[v] = lst[v]
    DFS(lst[v+1])
    res2[v] = lst[v]
    DFS(lst[v+1])


print(DFS(0))
