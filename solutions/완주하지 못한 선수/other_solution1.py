# Hashing 방식으로 풀어내기
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        print(hash(part), temp)
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print("\n")
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print("\n")
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
