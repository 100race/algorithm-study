import sys
#sys.stdin = open("input.txt","rt")

N, K = map(int,input().split())

count = 0
for x in range(1,N+1):
    if N%x == 0:
        count += 1
        if count == K:
            print(x)
            break
if(count<K):
    print(-1)