# 문제출처: https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    number1= ([1,2,3,4,5]*2000)[:len(answers)]
    number2= ([2,1,2,3,2,4,2,5]*1250)[:len(answers)]
    number3= ([3,3,1,1,2,2,4,4,5,5]*1000)[:len(answers)]
    student_list= [number1, number2, number3]
    
    # 정답 개수
    for number in student_list:
        count= 0
        for i, j in zip(number,answers):
            if i == j:
                count += 1
            else:
                continue
        answer.append(count)
    
    # 가장 많이 맞춘사람
    if (answer[0] > answer[1]) & (answer[0] > answer[2]):
        return [1]
    elif (answer[1] > answer[0]) & (answer[1] > answer[2]):
        return [2]
    elif (answer[2] > answer[0]) & (answer[2] > answer[1]):
        return [3]
    elif (answer[0] == answer[1]) & (answer[0] > answer[2]):
        return [1,2]
    elif (answer[1] == answer[2]) & (answer[1] > answer[0]):
        return [2,3]    
    elif (answer[0] == answer[2]) & (answer[0] > answer[1]):
        return [1,3]
    else:
        return [1,2,3]