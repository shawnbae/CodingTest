# 문제출처: https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    queue = [(i, pr) for i, pr in enumerate(priorities)]
    answer = 0
    
    while True:            
        q = queue.pop(0)
        if queue:            
            if max(que[1] for que in queue) <= q[1]:
                answer += 1
                if q[0] == location:
                    break
            else:
                queue.append(q)
        else:
            if q[0] == location:
                answer += 1
                break
    return answer