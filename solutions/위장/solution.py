# 문제출처: https://school.programmers.co.kr/learn/courses/30/lessons/42578

# from collections import defaultdict
# from itertools import combinations
# from functools import reduce

# Test Case 1번 통과못함
# def solution(clothes):
#     dic = defaultdict(int)

#     for cloth, types in clothes:
#         dic[types] += 1

#     answer = 0
#     for n in range(len(dic)):
#         answer += sum(map(lambda x: reduce(lambda a, b: a * b, x), combinations(dic.values(), n+1)))
#     return answer


from collections import defaultdict


def solution(clothes):
    dic = defaultdict(list)

    for cloth, types in clothes:
        dic[types].append(cloth)

    answer = 1
    for key in dic.keys():
        answer *= len(dic[key]) + 1

    return answer - 1
