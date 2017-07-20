from itertools import permutations
import re

def create_formula(combination,numbers):
    formula = ""
    index = 0
    for op in combination:
        formula += str(numbers[index]) + op
        index += 1
    formula += numbers[index]
    return formula

def evaluate(form):
    if len(form) == 1:
        print(form)
        return int(form[0])
    plus = False
    minus = False
    try:
        plusIndex = form.index('+')
    except:
        plus = True
        plusIndex = -1
    try:
        minusIndex = form.index('-')
    except:
        minus = True
        minusIndex = -1

    if not minus:
        if not plus:
            if plusIndex < minusIndex:
                return evaluate(form[:plusIndex]) + evaluate(form[plusIndex+1:])
            else:
                return evaluate(form[:minusIndex]) - evaluate(form[minusIndex+1:])
        else:
             return evaluate(form[:minusIndex]) - evaluate(form[minusIndex+1:])
    else:
        if not plus:
             return evaluate(form[:plusIndex]) - evaluate(form[plusIndex+1:])
    
    print
    return int(eval(''.join(form)))
        

def countdown(numbers):
    rightCombinations = []
    finalScore = numbers.pop()
    combinations = returnAllCombinations(len(numbers) - 1)
    perms =  list(permutations(numbers))
    for combination in combinations:
        for permut in perms:
            formula = create_formula(combination,permut)
            form = re.split("([*|+|-|/])",formula)
            if int(evaluate(form)) == finalScore:
                rightCombinations.append(formula)
    return rightCombinations

def returnAllCombinations(size):
    listFinal = []
    for x in range(0,size):
        if len(listFinal) == 0:
            for y in range(0,4):
                if y == 0:
                    listFinal.append("+")
                elif y == 1:
                    listFinal.append("-")
                elif y == 2:
                    listFinal.append("*")
                else:
                    listFinal.append("/")
        else:
            newList = []
            for l in listFinal:
                for y in range(0,4):
                    newLine = list(l)
                    if y == 0:
                        newLine.append("+")
                    elif y == 1:
                        newLine.append("-")
                    elif y == 2:
                        newLine.append("*")
                    else:
                        newLine.append("/")
                    newList.append(newLine)
            listFinal = list(newList)
            
            
    return listFinal

for line in open("input.txt",'r'):
    print(countdown(line.split(" ")))

