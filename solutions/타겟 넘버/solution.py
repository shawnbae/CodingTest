# 문제출처: https://programmers.co.kr/learn/courses/30/lessons/43165

from itertools import product

def solution(numbers, target):
    ziplist = [(x, -x) for x in numbers]
    answer = 0
    for prod in product(*ziplist):
        if sum(prod) == target:
            answer += 1
    
    return answer