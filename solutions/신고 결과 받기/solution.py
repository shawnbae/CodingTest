# 문제출처: https://programmers.co.kr/learn/courses/30/lessons/92334

from itertools import chain
from collections import Counter, defaultdict

def solution(id_list, report, k):
    from_to = {}
    for rep in report:
        from_to.setdefault(rep.split(" ")[0], set()).add(rep.split(" ")[1])
    
    reported_list = [key for key, val in Counter(chain(*from_to.values())).items() if val >= k]

    def name_to_num(list):
        num = 0
        for li in list:
            if li in reported_list:
                num += 1
        return num
    
    answer_dict = defaultdict(int)
    for i in id_list:
        if i in from_to:
            answer_dict[i] = name_to_num(from_to[i])
        else:
            answer_dict[i] = 0
            
    return list(answer_dict.values())