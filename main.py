# Microprocessor simulation
# supports a small set of simulated operations
# prints the output for each operation
import sys
import re

# Memory Stack
stack = []

# Define a custom InvalidOperationException
class InvalidOperationException(Exception):
    def __init__(self, message="Operation is not a supported operation or an operand is not an integer"):
        self.message = message
        super().__init__(self.message)
    

# Compute the minimum value in a list of integers
def computeMinimum(arr):
    mini = arr[0]
    for num in arr[1:]:
        if num < mini:
            mini = num
    return mini

# Compute the maximum value in a list of integers
def computeMaximum(arr):
    maximum = arr[0]
    for num in arr[1:]:
        if num > maximum:
            maximum = num
    return maximum

def pushStack(instructionTokens):
    if len(instructionTokens) != 2:
        raise InvalidOperationException(f"invalid operation {' '.join(instructionTokens)}")
    stack.append(instructionTokens[1])

def popStack(instructionTokens):
    if len(instructionTokens) != 1:
        raise InvalidOperationException(f"invalid operation {' '.join(instructionTokens)}")
    
    if len(stack) > 0:
        print(stack.pop())
    else:
        raise InvalidOperationException("invalid operation")

def computeHighestPower(num, base, power=0):
    if num < base:
        return power
    else:
        power = computeHighestPower(num/base, base, power+1)
    return power

def decimalToBinary(num):
    highestPower = computeHighestPower(num, 2)
    binaryArray = []
    for i in range(highestPower, -1, -1):
        if num >= 2**i:
            num = num - 2**i
            binaryArray.append(1)
        else:
            if i== 0:
                binaryArray.append(num)
            else:
                binaryArray.append(0)
    return "".join([ str(j) for j in binaryArray])

def binaryToDecimal(binaryString):
    binaryArray = [ eval(k) for k in binaryString]
    binaryArray.reverse()
    return sum([ (2**i) * binaryArray[i] for i in range(len(binaryString) - 1, -1, -1)])
        

# Shifting bits
def shiftBits(num, n):
    binaryString = decimalToBinary(num)
    firstOne = re.search(r'1', binaryString)
    if firstOne is not None:
        index = firstOne.span()[0]
        return binaryToDecimal(binaryString[index:] + ("0"*n))
    else:
        return binaryToDecimal(binaryString)

# Noop operation
def noop(instructionTokens):
    if len(instructionTokens) > 1:
        raise InvalidOperationException(f"invalid operation {' '.join(instructionTokens)}")
    print()

# Addition operation
def add(instructionTokens):
    if len(instructionTokens) != 3:
        raise InvalidOperationException(f"invalid operation {' '.join(instructionTokens)}")
    print(eval(instructionTokens[1]) + eval(instructionTokens[2]))

# Multiplication operation
def mul(instructionTokens):
    if len(instructionTokens) != 3:
        raise InvalidOperationException(f"invalid operation {' '.join(instructionTokens)}")
    print(eval(instructionTokens[1]) * eval(instructionTokens[2]))

# Greater than comparison operation
def gt(instructionTokens):
    if len(instructionTokens) != 3:
        raise InvalidOperationException(f"invalid operation {' '.join(instructionTokens)}")
    if eval(instructionTokens[1]) > eval(instructionTokens[2]):
        print("1")
    else:
        print("0")

# Logical OR operation
def _or(instructionTokens):
    if len(instructionTokens) > 3:
        raise InvalidOperationException(f"invalid operation {' '.join(instructionTokens)}")
    if (eval(instructionTokens[1]) == 0) and (eval(instructionTokens[2]) == 0):
        print("0")
    else:
        print("1")

# Logical AND operation
def nand(instructionTokens):
    if len(instructionTokens) != 3:
        raise InvalidOperationException(f"invalid operation {' '.join(instructionTokens)}")
    if eval(instructionTokens[1]) == 0 or eval(instructionTokens[2]) == 0:
        print("1")
    else:
        print("0")

# Minimum value finder operation
def min_operation(instructionTokens):
    if len(instructionTokens) < 3:
        raise InvalidOperationException(f"invalid operation {' '.join(instructionTokens)}")
    print(computeMinimum([eval(i) for i in instructionTokens[1:]]))

# Bit shifting
def shift(instructionTokens):
    if len(instructionTokens) != 3 or (re.match(r'-', instructionTokens[1]) is not None) or (re.match(r'-', instructionTokens[2]) is not None) or (eval(instructionTokens[1]) == 0) or (eval(instructionTokens[2]) == 0):
        raise InvalidOperationException(f"invalid operation {' '.join(instructionTokens)}")
    print(shiftBits(eval(instructionTokens[1]), eval(instructionTokens[2])))

def push(instructionTokens):
    if len(instructionTokens) != 2:
        raise InvalidOperationException(f"invalid operation {' '.join(instructionTokens)}")
    pushStack(eval(instructionTokens[1]))


# You need to update the process function to actually handle the operations. To
# start, it just prints out each line of the input.
def process(instruction):

    try:

        # Split instruction into tokens
        instructionTokens = re.split("\s+", instruction)

        # Initialize the operation to None
        op = None

        # Set the op iff and only if there exists atleast 
        # one token(first token) as the operation to perform.
        if(len(instructionTokens) > 0):
            op = instructionTokens[0]
        else:
            raise InvalidOperationException(f"invalid operation {instruction}")
        
        if len(instructionTokens) > 1 :
            for token in instructionTokens[1:]:
                if (re.match('[^+\-0-9]', token) is not None) or (re.search(r'\.', token) is not None):
                    raise InvalidOperationException(f"invalid operation {instruction}")
        
        if op == "noop":
            noop(instructionTokens)
        elif op == "add":
            add(instructionTokens)
        elif op == "mul":
            mul(instructionTokens)
        elif op == "gt":
            gt(instructionTokens)
        elif op == "or":
            _or(instructionTokens)
        elif op == "nand":
            nand(instructionTokens)
        elif op == "min":
            min_operation(instructionTokens)
        elif op == "shift":
            shift(instructionTokens)
        elif op == "push":
            pushStack(instructionTokens)
        elif op == "pop":
            popStack(instructionTokens)
        else:
            raise InvalidOperationException(f"invalid operation {instruction}")

    except InvalidOperationException as invalidOperationException:
        print(invalidOperationException.message)

# The run function is provided, you don't need to change it.
# It reads all the lines from a file, then calls the process function
#   for each line 
def run(filename):
    with open(filename, 'r') as file:
        for operation in file.readlines():
            process(operation.strip())

# This code will call the run function with a filename, if it's provided on the 
# command line. It would pass samples/sample2.txt with this invocation:
# python3 main.py samples/sample2.txt
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py [path/to/sample]")
    else:
        run(sys.argv[1])