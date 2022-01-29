# 모법적인 아잔 분할 알고리즘 풀이법
def solution(n, times):
    start = min(times) * n // len(times)
    end = max(times) * n // len(times)
    
    while start <= end:
        mid = (start + end) //2
        
        cnt = 0
        for time in times:
            cnt += mid // time 
            
        if cnt < n:
            start = mid + 1
        else:
            end = mid - 1 
            
    return start