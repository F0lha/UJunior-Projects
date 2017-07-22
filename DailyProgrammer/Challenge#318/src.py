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
'''
    Unnecessary Funtion
'''
def evaluate(form):
    result = 0
    for index in range(len(form)):
        if form[index] == "+":
            result += int(form[index+1])
            index += 1
        elif form[index] == "-":
            result -= int(form[index+1])
            index += 1
        elif form[index] == "*":
            result *= int(form[index+1])
            index += 1
        elif form[index] == "/":
            result //= int(form[index+1])
            index += 1
        else:
            result += int(form[index])  
    return result

def countdown(numbers):
    rightCombinations = []
    finalScore = numbers.pop()
    combinations = returnAllCombinations(len(numbers) - 1)
    perms =  list(permutations(numbers))
    for combination in combinations:
        for permut in perms:
            formula = create_formula(combination,permut)
            #form = re.split("([*+-/])",formula)
            #if int(evaluate(form)) == int(finalScore):
            if int(eval(formula)) == int(finalScore):
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

out = open("output.txt",'w')

for line in open("input.txt",'r'):
    for formula in countdown(line.split(" ")):
        out.write(formula)
        out.write("\n")
    out.write("\n\n")


