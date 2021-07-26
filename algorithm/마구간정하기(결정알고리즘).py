from os import startfile
import sys
sys.stdin = open("input.txt","rt") #채점시 꼭 주석처리 할것

n,c = map(int,(input().split()))
coordinate = []

#입력받음
for i in range(n):
    tmp = int(input())
    coordinate.append(tmp)

#
def Count(len):
    cnt = 1
    ep = coordinate[0]
    for i in range(1,n):
        if coordinate[i] - ep >=len:
            cnt += 1
            ep = coordinate[i]
    return cnt

coordinate.sort()
result = 0
left = 1
right = coordinate[n-1]


while left <= right:
    mid = (left+right)//2
    if Count(mid) >= c:
        result = mid
        left = mid+1
    else :
        right = mid-1


print(result)


