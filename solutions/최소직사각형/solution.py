# 문제출처: https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    sizes = [[max(size), min(size)] for size in sizes]

    tmp_h, tmp_w = 0, 0

    for size in sizes:
        tmp_h, tmp_w = max(tmp_h, size[0]), max(tmp_w, size[1])

    return tmp_h * tmp_w
