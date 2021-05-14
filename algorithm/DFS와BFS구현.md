# 개념

그래프의 각 정점을 방문하는 그래프의 순회. 깊이우선탐색(DFS)와 너비우선탐색(BFS)가 있다.
- 깊이우선탐색(DFS)
재귀, 스택 이용
- 너비우선탐색(BFS)
큐 이용

## DFS
### 재귀 이용
장점 : 구현이 좀 더 편하다<br>
단점 : 실행시간이 좀 더 오래걸린다

- 그래프를 인접리스트로 표현
- 키는 출발노드, 값은 도착노드
```python
graph = {'1':[2,3,4],
         '2':[5],
         '3':[5],
         '4':[],
         '5':[6,7],
         '6':[],
         '7':[3],
}

def recursive_dfs(start, visited=[]):
  visited.append(start) # 방문
  for node in graph[start]: # 현재 방문노드 인접리스트중 방문하지 않은곳을 재귀로 방문
    if node not in visited:
      visited = recursive_dfs(node, visited)
  return visited


#결과값
[1,2,5,6,7,3,4]
```

### 스택이용
장점 : 직관적이라 이해하기 쉽고, 실행속도가 빠르다<br>
차이점 : 실행순서가 DFS와 반대


```python
graph = {'1':[2,3,4],
         '2':[5],
         '3':[5],
         '4':[],
         '5':[6,7],
         '6':[],
         '7':[3],
}

def iterative_dfs(root):
  visited = []
  stack = [root]
  
  while stack:
    start = stack.pop() #스택은 pop()으로 맨 뒤에 노드 추출
    if start not in visited: # start노드에 방문한적 없으면 방문하고 스택에 방문노드의 인접노드리스트 추가
      visited.append(start)
      stack.extend(graph[start])
  return visited

#결과값
[1,2,5,6,7,3,4]
```


## BFS
최단경로를 찾는 다익스트라 알고리즘 등에 쓰인다
### 큐 이용

```python
graph = {'1':[2,3,4],
         '2':[5],
         '3':[5],
         '4':[],
         '5':[6,7],
         '6':[],
         '7':[3],
}

def iterative_bfs(root):
  visited = [root]
  queue = [root]
  
  while queue:
    start = queue.pop(0) # 큐는 인덱스를 넣어 맨 앞의 노드 추출
    for node in graph[start]: # 근접노드를 모두 순회하며 방문하지 않았다면 방문하고 큐에 추가
      if node not in visited:
        visited.append(node)
        queue.append(node)
  return visited

#결과값
[1,2,3,4,5,6,7]
```







[파이썬알고리즘인터뷰 - 박상길저] <br>
[깊이우선탐색 구현하기](https://juhee-maeng.tistory.com/25)
