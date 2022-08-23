# 문제출처: https://school.programmers.co.kr/learn/courses/30/lessons/118667

def solution(queue1, queue2):
    lst = list(queue1 + queue2)
    length = len(queue1) * 2
    idx1, idx2 = 0, length // 2
    target = sum(lst) // 2

    answer = 0
    curr = sum(lst[idx1:idx2])
    while idx1 >= 0 and idx2 < length and idx1 < idx2:
        if curr == target:
            return answer
        elif curr < target:
            curr += lst[idx2]
            idx2 += 1
            answer += 1
        else:
            curr -= lst[idx1]
            idx1 += 1
            answer += 1
    return -1
