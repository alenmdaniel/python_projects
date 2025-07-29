#TODO: Redo Algorithm with Width rather than diff
def arithmetic_arranger(problems, ans = False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    topnums = []
    botnums = []
    operator = []
    answer = []
    #stores string data in arrays
    for prob in problems:
        stop1 = prob.find(' ')
        first = prob[:stop1]
        topnums.append(first)
        aft = prob[stop1 +1::] 
        stop2 = aft.find(' ')
        second = aft[:stop2]
        operator.append(second)
        fin = aft[stop2+1::]
        botnums.append(fin)
    #TODO: add check function for numbers
    for dig in range(len(topnums)):
        if (not(topnums[dig].isdigit()) or not(botnums[dig].isdigit())):
            return 'Error: Numbers must only contain digits.'
        if (operator[dig] != '+' and operator[dig] != '-'):
            return "Error: Operator must be '+' or '-'."
        if (len(topnums[dig]) > 4 or len(botnums[dig]) > 4):
            return 'Error: Numbers cannot be more than four digits.'
    #now we need to find bigger digit number
    #and store that data in another array
    #print(topnums, botnums, operator)
    width = widArr(topnums, botnums)
    tArr = topR(topnums, width)
    bArr = botR(botnums, width, operator)
    dArr = dLine(width)
    if(ans):
        alist = resultlist(topnums, botnums, operator)
        aArr = ansLine(alist, width)
        return tArr + '\n' + bArr + '\n' + dArr + '\n' + aArr
    else:
        return tArr + '\n' + bArr + '\n' + dArr
    

#defines width of number section
def widArr(tnums, bnums):
    wR = []
    for i in range(len(tnums)):
        wR.append(max(len(tnums[i]), len(bnums[i])))
    return wR

#write the top line
def topR(top, width):
    topStr = ''
    for i in range(len(top)):
        currStr = '  '
        diff = width[i] - len(top[i])
        if (diff > 0):
            for d in range(diff):
                currStr+=' '
        currStr+=top[i]
        topStr+=currStr
        if (i != len(top)-1):
            topStr+='    '
    #print(topStr)
    return topStr

def botR(bot, width, opr):
    botStr = ''
    for i in range(len(bot)):
        currStr = opr[i] + ' '
        diff = width[i] - len(bot[i])
        if (diff > 0):
            for d in range(diff):
                currStr+=' '
        currStr+=bot[i]
        botStr+=currStr
        if (i != len(bot) -1):
            botStr+='    '
    #print(botStr)
    return botStr    

def dLine(width):
    dStr = ''
    for i in range(len(width)):
        dcur = '--'
        for d in range(width[i]):
            dcur+='-'
        dStr+=dcur
        if (i != len(width)-1):
            dStr+='    '
    #print(dStr)
    return dStr


def resultlist (top, bot, opr):
    arr_ans = []
    for i in range(len(top)):
        if (opr[i] == '+'):
            arr_ans.append(str(int(top[i]) + int(bot[i])))
        else:
            arr_ans.append(str(int(top[i]) - int(bot[i])))

    return arr_ans


def ansLine(anlist, length):
    aStr = ''
    for i in range(len(anlist)):
        cStr = ''
        diff = length[i] + 2 - len(anlist[i])
        for d in range(diff):
            cStr+=' '
        cStr+=anlist[i]
        aStr+=cStr
        if (i != len(anlist) -1):
            aStr+='    '
    #print(aStr)
    return(aStr)

def main():
    arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])

main()
print('  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------')

