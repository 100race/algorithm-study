from os import startfile
import sys
#sys.stdin = open("input.txt","rt") #채점시 꼭 주석처리 할것

n,m = map(int,(input().split()))
lst = list(map(int,input().split()))

lst.sort()


s = 0
e = n-1
while s <= e:
    mid = (s+e)//2
    if m == lst[mid]:
        print(mid+1)
        break
    elif m > lst[mid]:
        s = mid+1      
    else:
        e = mid-1

