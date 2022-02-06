_input = input()
inputlist = [w for w in _input]

def changeint(string):
    try:
        return int(string)
    except:
        if string == 'A':
            return 10
        elif string == 'B':
            return 11
        elif string == 'C':
            return 12
        elif string == 'D':
            return 13
        elif string == 'E':
            return 14
        elif string == 'F':
            return 15
        
answer = 0
for i in range(len(inputlist)):
    answer += 16**(len(inputlist) - i - 1)*changeint(inputlist[i])

print(answer)    