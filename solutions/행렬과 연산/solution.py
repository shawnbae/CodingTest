# 문제출처: https://school.programmers.co.kr/learn/courses/30/lessons/118670
from collections import deque


def solution(rc, operations):
    inner_rows = deque(deque(rc[r][1:-1]) for r in range(len(rc)))
    outer_cols = [deque(rc[r][0] for r in range(len(rc))),
                  deque(rc[r][len(rc[0])-1] for r in range(len(rc)))]

    for oper in operations:
        # ShiftRow 연산
        if oper == "ShiftRow":
            # 내부 행들 pop
            inner_rows.rotate(1)
            # inner_rows.appendleft(inner_rows.pop())
            # 외부 열들 rotate
            outer_cols[0].rotate(1)
            outer_cols[1].rotate(1)

        # Rotate 연산
        else:
            # 왼쪽 열 처리
            outer_cols[0].rotate(-1)
            inner_rows[0].appendleft(outer_cols[0].pop())

            # 내부 행 처리
            outer_cols[1].appendleft(inner_rows[0].pop())

            # 오른쪽 열 처리
            outer_cols[1].rotate(1)
            inner_rows[len(rc)-1].append(outer_cols[1].popleft())

            # 내부 행 처리 2
            outer_cols[0].append(inner_rows[len(rc)-1].popleft())

    inner_rows = [list(inner_row) for inner_row in inner_rows]

    # 행의 개수만큼 돌면서 내부 행 양 끝에 outer_cols를 삽입
    for idx in range(len(rc)):
        inner_rows[idx].insert(0, outer_cols[0][idx])
        inner_rows[idx].insert(len(rc[0]), outer_cols[1][idx])

    return inner_rows
