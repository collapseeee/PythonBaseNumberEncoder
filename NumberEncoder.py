import math

#===================================================================================================================#
# take input as number on base 10 and ask for which base user want the number to translate into and floor the number's decimal to 6 digits.
while(True):
    usersInputNumber = (float(input("Enter decimal value: ")))
    usersInputToBase = int(input("Enter the toBase: "))
    usersInputNumber = (math.floor(usersInputNumber * (10**6)))/10**6
    # check the input.
    if (usersInputNumber==0):
        print("The input number must not equals to 0.")
    else:
        break

    if (usersInputToBase>=2 and usersInputToBase<=16):
        break
    else:
        print("The inputToBase must be in between 2 and 16.")
#===================================================================================================================#


#===================================================================================================================#
# define float_to_base_b function
def float_to_base_b(x,b):
    inputNumber = x
    toBaseNumber = b
    # split number and decimal.
    inputNumber = str(inputNumber)
    splittedString = inputNumber.split(".")
    splittedNumber = int(splittedString[0])
    splittedDecimal = ("0."+splittedString[1])
    splittedDecimal = float(splittedDecimal)
    encodedNumber = encodeNumberToBase(splittedNumber, splittedDecimal, toBaseNumber)
    return encodedNumber
#===================================================================================================================#


#===================================================================================================================#
# define the function to get the value of the number in a base number that user have provided.
def encodeNumberToBase(inputNumber, inputDecimal, toBaseNumber):
    if (inputNumber<0):
        isNegativeNumber = True
        inputNumber = inputNumber*(-1)
    else:
        isNegativeNumber = False

    listOfNumbersRemainder = []
    listOfDecimalsNumber = []
    decimalMultiplyCounter = 0
    #Number encoding.
    while(True):
        i = str(inputNumber%toBaseNumber)
        #case of toBase 11  to 16.
        match (i):
            case "10":
                i = "A"
            case "11":
                i = "B"
            case "12":
                i = "C"
            case "13":
                i = "D"
            case "14":
                i = "E"
            case "15":
                i = "F"

        listOfNumbersRemainder.append(i)
        inputNumber = inputNumber//toBaseNumber
        if (inputNumber==0):
            break
    unsortedNumbersRemainder = ""
    unsortedNumbersRemainder = unsortedNumbersRemainder.join(listOfNumbersRemainder)
    encodedNumber = unsortedNumbersRemainder[::-1]

    #Decimal encoding.
    decimalMultiplied = 0
    while(True):
        inputDecimal = inputDecimal*toBaseNumber
        i = int(inputDecimal//1)
        if (inputDecimal>=1):
            inputDecimal -= inputDecimal//1
        listOfDecimalsNumber.append(str(i))
        decimalMultiplied += 1
        if (decimalMultiplied==6):
            break
    encodedDecimal = ""
    encodedDecimal = encodedDecimal.join(listOfDecimalsNumber)
    result = encodedNumber+"."+encodedDecimal
    if (isNegativeNumber):
        result = "-" + result
    return result
#===================================================================================================================#

#===================================================================================================================#
# main method
print("Result: " ,float_to_base_b(usersInputNumber,usersInputToBase))
#===================================================================================================================#