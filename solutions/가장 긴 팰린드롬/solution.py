# 문제출처: https://school.programmers.co.kr/learn/courses/30/lessons/12904

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            tmp = s[i:j+1]
                
            if (tmp == tmp[::-1]):
                answer = max(answer, len(tmp))
    return answer