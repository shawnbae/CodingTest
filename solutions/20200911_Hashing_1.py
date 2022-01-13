# 문제출처: https://www.acmicpc.net/problem/15829

letter_dict= {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6,
'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14,
'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22,
'w':23, 'x':24, 'y':25, 'z':26}

def solution(s):
    letter_list= []
    for letter in s:
        letter_list.append(letter)
    letter_list= [letter_dict[letter] for letter in letter_list]
    hash_list= [31**(idx)*(x) for idx, x in enumerate(letter_list)]
    return sum(hash_list)

print(solution('abcde'))
print(solution('zzz'))