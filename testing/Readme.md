# Unit test

# Video link

https://youtu.be/tEuIHIFSHGM

# **CPU Automata for basic robot**

For the testing of the CPU automata we created a file called `test.py` which includes the commands and expected outputs of the different test. In this case it creates a file called input.txt that is used by the `main.py` file to move the robot, the `test.py` file gets the console printed output and compares it with the expected output to know if the test passed or failed.

In this case we did 4 test cases, 3 in which the robot doesn’t exit the map and one in which it passes the limit, all of this cases passed the test successfully.

## Example of test:

### Input.txt

```
MOV, 11
```

### Expected output:

```
División------------------------
['XX', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
Invalid Operation, out of range
```

## Result

Test 3 passed

# **LEX and YACC**

For the testing of the CFG, a bash file was created. It runs the lex and yacc with different file inputs and checks if the language passed or if there was a syntax error. 4 tests were created, in which 2 are accepted and 2 are rejected. All tests must pass.

## Example of test:

### testlex1.txt

```
Robot, please move ahead by 2 blocks.
Robot, please advance 3 blocks forward
```

### Expected output:

```
```

## Result

Test 1 passed



![test results.jpeg](https://github.com/NolbertoCastro/MovTurn/blob/main/testing/screenshots/test%20results.jpeg)

