import re

def spaces(count, val):
    rtn = ""
    for x in range(count):
        rtn = rtn + val
    return rtn

def arithmetic_arranger(problems, *true):
    arranged_problems = ""

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    cnt = 0
    for x in problems:
        cnt += 1

        if cnt > 5:
            return "Error: Too many problems."

        y = x.split()
        
        try:
            int(y[0])
            int(y[2])
        except:
            return "Error: Numbers must only contain digits."
        
        if y[1] == "+":
            sum = int(y[0]) + int(y[2])
        elif y[1] == "-":
            sum = int(y[0]) - int(y[2])
        else:
            return "Error: Operator must be \'+\' or \'-\'."
        sum = str(sum)

        if len(y[0]) > len(y[2]):
            space1 = len(y[0])
        else:
            space1 = len(y[2])
        
        if len(y[0]) > 4 or len(y[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        spaceneeded = space1 - len(y[0]) + 2
        line1 = line1 + spaces(spaceneeded," ")+y[0] + "    "

        spaceneeded = space1 - len(y[2]) + 1
        line2 = line2 + "" + y[1] + spaces(spaceneeded," ") + y[2]+"    "

        spaceneeded = space1 + 2
        line3 = line3 + "" + spaces(spaceneeded, "-")+"    "

        if true :
            spaceneeded = space1 - len(str(sum)) + 2
            line4 = line4 + "" + spaces(spaceneeded, " ") + sum + "    "

    line1 = line1.rstrip()
    line2 = line2.rstrip()
    line3 = line3.rstrip()
    line4 = line4.rstrip()

    if True:
        arranged_problems = line1 + "\n" + line2 + "\n" + line3+ "\n"+line4
    else:
        arranged_problems = line1 + "\n" + line2 + "\n" + line3

    arranged_problems = arranged_problems.rstrip()

    return arranged_problems
