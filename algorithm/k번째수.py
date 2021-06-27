import sys
#sys.stdin = open("input.txt","rt")

def solution(N,s,e,k,N_list):
    r_list = sorted(N_list[s-1:e])
    return r_list[k-1]

T = int(input()) #테스트 케이스 개수 주어짐
for i in range(T):
    N,s,e,k = map(int,input().split())
    N_list = list(map(int,input().split()))
    #print(T,N,s,e,k)
    result = solution(N,s,e,k,N_list)
    print(f'#{i+1} {result}')
        

    


