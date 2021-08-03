##  문제설명
다음과 같이 여러 단위의 동전들이 주어져 있을때 거스름돈을 가장 적은 수의 동전으로 교환
해주려면 어떻게 주면 되는가? 각 단위의 동전은 무한정 쓸 수 있다.

## 입출력 예시
Input: 3 <br>
1 2 5<br>
15<br>
Output: 3


## 풀이
```python 
from os import startfile
import sys
sys.stdin = open("input.txt","rt") #채점시 꼭 주석처리 할것

#L(Level)이 동전 개수
def DFS(L,sum):
    global res
    #가지치기
    if L > res:
        return
    #탈출조건
    if sum > m:
        return
    elif sum == m:
        if L<res:
            res = L
        return
    #가지내리기 반복
    else :
        for i in a:
            DFS(L+1,sum+i)

if __name__ =="__main__":
    n = int(input())
    a= list(map(int,input().split()))
    m = int(input())
    res = 9999999999
    a.sort(reverse=True) #연산 횟수를 줄여주기. 큰 동전부터 계산
    DFS(0,0)
    print(res)
```
- 기존 풀이에서 개선한 점 : 
- sum을 따로 변수 선언해서 넘기려고 했던것
- res를 리스트로 저장해서 결과를 모두 저장하려했는데 그럴 필요 없이 바로 최소결과 res를 찾아가면 됨
- 가지치기로 실행시간 단축 -> 최소 res 를 구했는데 그 이상을 level을 구할 필요 없음
