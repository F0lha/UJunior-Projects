#Challenge 324

def getDigits(number, decimalBool):
    if not decimalBool:
        if len(number) == 0:
            return False
        else:
            return number[0]+number[1]
    else:
        if len(number) == 0:
            return str(0) + str(0)
        elif len(number) == 1:
            return number[0] + str(0)
        else:
            return number[0]+number[1]

def reformat(number,decimalBool):
    if decimalBool:
        if len(number) > 1:
            return number[2:]
        else:
            return ""
    else:
        if(len(number)>1):
            return number[2:]
        else:
            return ""
#to return square root number
def squareRoot(decimals, number):
    #format things
    part = number.split('.')[0]
    if(len(part) % 2 != 0):
        part = str(0)+part
    #leftovers
    left = 0
    result = ""
    decimalBool = False
    #integer part
    section = getDigits(part, decimalBool)
    part = reformat(part, decimalBool)
    
    decimalCounter = 0
    left += int(section)
    while True:
        #The A phase        
        if(len(result) == 0):
            for x in range(0,10):
                if x**2 > left:
                    x -= 1
                    break
            result += str(x)
            
            left -= x**2
            continue
        else:
            if not decimalBool:
                x = int(result)
            else:
                x = float(result)

        section = getDigits(part, decimalBool)
        #calculate B
        if not section:
            #hit the point
            #Count decimal Places
            decimalBool = True
            if(int(decimals) == decimalCounter and decimalBool):
                return result
            result += "." 
            
            part = number.split('.')[1]
            section = getDigits(part, decimalBool)
            part = reformat(part, decimalBool)
        else:
            #Count decimal Places
            if(int(decimals) == decimalCounter and decimalBool):
                return result[:-1]
            elif decimalBool:
                decimalCounter += 1
            part = reformat(part, decimalBool)
        
                

        print(section)
        left = left*100 + int(section)
        print("Start B: x = " + result + "left=" + str(left)+ "part=" + part+ "section=" + str(section))
        for y in range(0,10):
            if (2*10*x + y)*y > left:
                y -= 1
                break
        result += str(y)
        left -= (2*10*x + y)*y
    


#solving
for line in open("input.txt",'r'):
    print("Result: " + squareRoot(line.split()[0],line.split()[1]))
