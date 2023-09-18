# Microprocessor Simulation

A microprocessor performs different operations on its inputs, based on a signal
that tells it which operation to perform.

In this exercise, you'll write code to simulate what a processor does.

A program, from the view of a microprocessor, is a set of operations and values.
The processor will perform each operation on the values, one by one. For our simplified
example, it might look like:

```txt
add 8 16
mul 10 3
or 1 0
nand 1 1
```

At each step, our model of a processor outputs a value. For this
pretend program, the output at each step would be:

```txt
24
30
1
0
```

## Processor Operations

Below are the processor operations that you should support, and what they should do.

| Operation 	| Description                           	| Sample       	| Output 	|
|-----------	|---------------------------------------	|--------------	|--------	|
| noop      	| Do nothing, print empty line          	| noop         	|        	|
| add       	| Add arguments                         	| add 3 140    	| 143    	|
| mul       	| Multiply arguments                    	| mul 10 21    	| 210    	|
| gt        	| Check if first is greater than second 	| gt 3 10      	| 0      	|
| or        	| Logical or                            	| or 6 0       	| 1      	|
| nand      	| Logical nand ("not and")              	| nand 1 1     	| 0      	|
| min       	| Find the minimum value of arguments   	| min 14 8 103 	| 8      	|
| shift     	| Shift left by a number of bits        	| shift 8 2    	| 32     	|
| invalid     | Any non-valid operations                | not an op     | invalid operation not an op |



**Task 2:**  Add support for the following additional operations to your microprocessor simulation.  Note that we are *not* providing test cases for these new operations, so it is your responsibility to test that they work properly, likely by creating your own input files with the operations and running the input files with your program.  The new operations are as follows:

Operation: push
Description: Pushes the provided single argument onto the top of a stack and prints nothing.
Sample: push 5
Output: There is no output, but your program should maintain a list that contains the stack.  So the last item in the list will be the value that was most recently pushed.

Operation: pop
Description: Removes the value that is on top of the stack and prints the value.  If the stack is empty, print invalid operation.  
Sample: pop
Output: If `push 5` was the most recently performed stack operation, then `pop` would print 5.


Sample program using push and pop:
```
push 5
push 10
pop
push 20
pop
pop
pop
```

The above program, would produce the following output:
```
10
20
5
invalid operation
```






**Notes:**

* All of the operations are defined for integer arguments. Floats or other 
    arguments are invalid.
* Most operations take exactly two arguments.
* `noop` takes no arguments (it should be invalid if there are any arguments). 
    `min` should work with 2 or more arguments.
* The logical `or` and `nand` operations always print out a `0` or `1`, no matter
    their inputs. 0 is treated as false, any other number is treated as true.
* `shift` takes the bit representation of its argument, and moves the bits left,
    with the number of places to shift given by the second argument. So, 8
    (00001000) gets shifted left by 2 to become 32 (00100000).
* `shift` is only defined for positive arguments. It is invalid for negative numbers or zero.
* For our processor, numbers have arbitrarily many bits. Don't worry about
    overflow or truncation for `add`, `mul`, or `shift`.
* If the processor encounters an invalid operation, it should print an error 
    message and stop.

## Starter Code

`main.py` has the function `run` already written for you. It reads a file
containing a program and calls the `process` function on each line.

There is also a `__name__ == "__main__"` module guard, to call the run function 
if the file is executed on the command line.

Your task is to implement the `process` function (right now it just prints each 
line) and any helper functions you need.

## Testing

As you develop your program, try running your helper functions with sample
inputs, to check that they are returning the results you expect. To run the
first whole sample program, enter `python main.py sample1.txt` in the terminal.
You can use the same pattern for the other samples, or write your own sample.

The automated tests will call the `process` or `run` function with some sample 
operations or programs, and check that the functions print the correct result. 
How you organize your code is up to you -- your helper functions are not tested 
directly in the automated tests.

## Hints

First, you'll need to turn the line of input into an operation and its
arguments. All of the values in the programs will be ints, so you should convert
the values from strings.

In order to write this program effectively, you should split the problem into
lots of small functions, and then use a single function to decides which other 
function to call.

Note: Python has built-in functions called `or` and `min`, so you can't use
those as names of functions in your code. Rename the functions to something
else



