# PythonBaseNumberEncoder
By Collapseeee. 24 September 2024.
Undone, Logic error on number input that between 0 to 1. Will be fixed later.

## What does the program do?
To translate or encode the input float number to the base number that the user wanted to.
_(the wanted base must be in between 2-16 and the input number must not equal to 0.)_

## Each defined function in the program.
**float_to_base_b(float x, int b)**
is the main function with parameter x and b to translate the input number to the base number.
x is a float number. it will be translated later.
b is an integer number. it will be used to translate the float number.

**encodeNumberToBase(int inputNumber, int inputDecimal, int toBaseNumber)**
is the sub-function that translate number from and decimal from the input with toBaseNumber.
before calling this function, you need to seperate the number and decimal from number and store them into the variables.
the translating process will run seperately, the number and the decimal from number. since, the process of them are completely different.

## Build-in function called.
**str()**

**int()**

**float()**

**math.floor()** to floor a float to an integer.

**_listVariable_.append()** to add a new list to the _listVariable_

**_listVariable_.[::-1]** to reverse the _listVariable_. e.g. from [1, 2, 3] to [3, 2, 1]

**_strVariable_.join()** to add a new string to _strVariable_

**_strVariable_.split()**


