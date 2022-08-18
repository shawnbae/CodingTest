# 문제출처: https://school.programmers.co.kr/learn/courses/30/lessons/17676

from datetime import datetime, timedelta

def solution(input):
    tmp = [(dt - timedelta(seconds = interval - 0.001), dt) for dt, interval in zip(map(lambda x: datetime.strptime(x.split()[0] + x.split()[1], '%Y-%m-%d%H:%M:%S.%f'), input), map(lambda x: float(x.split()[2].replace("s", "")), input))]
    
    cnt, answer = 0, 0
    for k in range(2):
        for j in range(len(tmp)):
            threshold = tmp[j][k]
            for i in range(len(tmp)):

                if threshold > tmp[i][0] and threshold>tmp[i][1]:
                    pass
                elif threshold+timedelta(seconds=0.999) < tmp[i][0] and threshold+timedelta(seconds=0.999)<tmp[i][1]:
                    pass
                else:
                    cnt += 1
            answer = max(cnt,answer)
            cnt = 0
    return answer