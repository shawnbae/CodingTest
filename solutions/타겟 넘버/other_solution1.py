# 모법적인 깊이우선탐색 알고리즘 풀이법
def DFS(nums, idx, n, t):
    res = 0 # 결과
    # 최종 index에 도달하는지 검사 후 DFS를 재귀적으로 반복. while문과 비슷한 효과
    # 입력받은 array의 길이와 index깊이가 같아지는 순간
    if idx == len(nums):
        if n == t: return 1 # index를 모두 탐색하여 더한 결과와 target값이 같다면 res에 1을 더해줌
        else: return 0 # 그렇지 않다면 res를 그대로 둠
    
    # DFS 함수를 재귀적으로 반복 (index 깊이 별로 탐색)
    res += DFS(nums, idx+1, n+nums[idx], t)
    res += DFS(nums, idx+1, n-nums[idx], t)

    return res
    
def solution(numbers, target):
    answer = DFS(numbers, 0, 0, target)
    return answer