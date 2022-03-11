# 문제출처: https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import defaultdict

def solution(n, computers):
    graph = defaultdict(list)
    for i in range(n):
        graph[i] = [idx for idx, x in enumerate(computers[i]) if x == 1]   

    case_visited = []
    for start_vertex in graph:
        visited, queue = [start_vertex], [start_vertex]
        while queue:
            vertex = queue.pop()

            for adj_v in graph[vertex]:
                if adj_v not in visited:
                    queue.append(adj_v)
                    visited.append(adj_v)
    
        if sorted(visited) not in case_visited:
            case_visited.append(sorted(visited))
            
    return len(case_visited)