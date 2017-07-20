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
        return int(form[0])
    else:
        if
        

def countdown(numbers):
    rightCombinations = []
    finalScore = numbers.pop()
    combinations = returnAllCombinations(len(numbers) - 1)
    perms =  list(permutations(numbers))
    for combination in combinations:
        for permut in perms:
            formula = create_formula(combination,permut)
            form = re.split("([*+-/])",formula)
            print(form)
            print(int(evaluate(form)))
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

