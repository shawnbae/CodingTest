# 문제출처: https://programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations

def solution(numbers):
    answer= []
    iterlist= list(combinations(numbers, 2))
    
    for iteration in iterlist:
        answer.append(sum(iteration))
    
    answer_set= set(answer)
    answer= list(answer_set)
    
    answer.sort()
    return answer