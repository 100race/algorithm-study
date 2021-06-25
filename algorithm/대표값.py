import sys
sys.stdin = open("input.txt","rt") #채점시 꼭 주석처리 할것

N = int(input())
scores = list(map(int,input().split()))


dif = [] #점수차 리스트
avg = round(sum(scores)/N)
scores_sort = sorted(scores)
dif = [ abs(avg - x) for x in scores_sort]

min = scores[0]
min_dif = dif[0]

for i in range(N):
    if dif[i] <= min_dif:
        min = scores_sort[i]
        min_dif = dif[i]

print(avg, scores.index(min)+1)

