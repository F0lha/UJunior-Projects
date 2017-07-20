#Challenge 324

def getDigits(number, decimalBool):
    if not decimalBool:
        if(number[0] == '.'):
            return False
        elif(number[1] == '.'):
            number = number[1:]
            return number[0]
        else:
            number = number[2:]
            return number[0]+number[1]
    else:
        if len(number) == 0:
            return str(0) + str(0)
        elif len(number) == 1:
            number = number[1:]
            return number[0] + str(0)
        else:
            number = number[2:]
            return number[0]+number[1]
    

#to return square root number
def squareRoot(decimals, number):
    #format things
    part = number.split('.')[0]

    #leftovers
    left = 0
    result = ""
    decimalBool = False
    #integer part
    section = getDigits(part, decimalBool)
    decimalCounter = 0
    left += int(section)
    while True:
        if not section:
            #hit the point
            result += "."
            decimalBool = True
            part = number.split('.')[1]

            section = getDigits(part, decimalBool)

        #Count decimal Places
        if(int(decimals) == decimalCounter):
            return result
        elif decimalBool:
            decimalCounter += 1


        #The A phase        
        if(len(result) == 0):
            for x in range(0,10):
                if x**2 > left:
                    x -= 1
                    break
            result += str(x)
            #calculate B
            left -= x**2
            continue
        else:
            x = int(result)    

        for y in range(0,10):
            if (2*10*x + y)*y > left:
                y -= 1
                break
        result += str(y)
        left -= (2*10*x + y)*y
        section = getDigits(part, decimalBool)
        left = left*100 + int(section)
    


#solving
for line in open("input.txt",'r'):
    print(squareRoot(line.split()[0],line.split()[1]))