# 문제출처: https://programmers.co.kr/learn/courses/30/lessons/42839


    sosu_list= []
    for i in range(2,10000000):
        for j in range(2, 10000000):
            if i%j != 0:
                sosu_list.append(i)
            else:
                continue
              
        
from collections import defaultdict
