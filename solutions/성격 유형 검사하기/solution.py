# 문제출처: https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ""
    dic = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for s, c in zip(survey, choices):
        # RT 점수계산
        if "R" in s or "T" in s:
            if s[1] == "R" and c >= 4:
                dic["R"] += c-4
            elif s[0] == "T" and c < 4:
                dic["T"] += 4-c
            elif s[1] == "T" and c >= 4:
                dic["T"] += c-4
            elif s[0] == "R" and c < 4:
                dic["R"] += 4-c

        # CF 점수계산
        if "C" in s or "F" in s:
            if s[1] == "C" and c >= 4:
                dic["C"] += c-4
            elif s[0] == "F" and c < 4:
                dic["F"] += 4-c
            elif s[1] == "F" and c >= 4:
                dic["F"] += c-4
            elif s[0] == "C" and c < 4:
                dic["C"] += 4-c

        # JM 점수계산
        if "J" in s or "M" in s:
            if s[1] == "J" and c >= 4:
                dic["J"] += c-4
            elif s[0] == "M" and c < 4:
                dic["M"] += 4-c
            elif s[1] == "M" and c >= 4:
                dic["M"] += c-4
            elif s[0] == "J" and c < 4:
                dic["J"] += 4-c

        # AN 점수계산
        if "A" in s or "N" in s:
            if s[1] == "A" and c >= 4:
                dic["A"] += c-4
            elif s[0] == "N" and c < 4:
                dic["N"] += 4-c
            elif s[1] == "N" and c >= 4:
                dic["N"] += c-4
            elif s[0] == "A" and c < 4:
                dic["A"] += 4-c
    # RT
    if dic["R"] >= dic["T"]:
        answer += "R"
    elif dic["R"] < dic["T"]:
        answer += "T"

    # CF
    if dic["C"] >= dic["F"]:
        answer += "C"
    elif dic["C"] < dic["F"]:
        answer += "F"

    # JM
    if dic["J"] >= dic["M"]:
        answer += "J"
    elif dic["J"] < dic["M"]:
        answer += "M"

    # AN
    if dic["A"] >= dic["N"]:
        answer += "A"
    elif dic["A"] < dic["N"]:
        answer += "N"

    return answer
