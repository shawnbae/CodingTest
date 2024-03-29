# 0의 value를 갖는 초기 list / dictionary에 반복적으로 해당 값을 더해주는 방식
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print("\n")
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))


# def solution(id_list, report, k):
#     answer = [0] * len(id_list)
#     dic = {x:0 for x in id_list}
    
#     for r in set(report):
#         reports[r.split(" ")[1]] += 1
    
#     for r in set(report):
#         if reports
    
#     return answer