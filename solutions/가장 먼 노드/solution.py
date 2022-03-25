# 문제출처: https://programmers.co.kr/learn/courses/30/lessons/49189

def solution(n, edge):
    graph =[  [] for _ in range(n + 1) ]
    distances = [ 0 for _ in range(n) ]
    visited = [False for _ in range(n)]
    queue = [0]
    visited[0] = True
    for (a, b) in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    while queue:
        i = queue.pop(0)

        for j in graph[i]:
            if visited[j] == False:
                visited[j] = True
                queue.append(j)
                distances[j] = distances[i] + 1

    return distances.count(max(distances))