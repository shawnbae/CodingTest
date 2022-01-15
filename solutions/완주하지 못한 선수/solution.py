# 문제출처: https://programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter

def solution(participant, completion):
    pardict= Counter(participant)
    comdict= Counter(completion)
    
    answer = ''.join((pardict - comdict).keys())
        
    return answer
