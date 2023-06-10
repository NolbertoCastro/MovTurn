# MOV TURN

# Instituto Tecnológico y de Estudios Superiores de Monterrey

![tec de monterrey Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Logo_del_ITESM.svg/320px-Logo_del_ITESM.svg.png)

### Team:

Nolberto Castro Sánchez | A01641501

Jesús Enrique Díaz Bernal Robinson Bours | A00227255

# Problem Description

Industry 4.0 encompasses intelligent manufacturing and the emergence of smart factories, which have recently extended their influence to the mechanical industry. This expansion is driven by the rapid advancement of technology and the growing demand for high-quality products with increased efficiency. Consequently, the role of robots has become crucial, highlighting the significance of robot programming languages. To address this challenge, the development and implementation of a robust robot language compiler are necessary.

This project tries to encourage the students to simulate the CPU of a car robot, create the programing language and its compiler

The Robot has the next constraints

* Only 2 supported instructions: 
	* MOV <num of blocks to move>
	* TURN <either: {90,180,270,360}>

* The field where the robot will move is a 2-D square matrix of 10 blocks

* If the instruction leads the robot out of the boundaries of the matrix, the CPU should return an illegal instruction error. 

* The programing language must be polite: 
	* Examples of valid sentences: 
		* Robot please move 2 blocks ahead
		* Robot please move 3 blocks ahead and then turn 90 degrees, then move 2 blocks
	* Examples of invalid sentences:
		* Robot moves 2 blocks
		* Robot moves 2 blocks quickly
		* Move 2 blocks right now
		* Robot  2 blocks moves
		* Moves Robot 2 blocks and turn 89 degrees

You can use ChatGPT to generate more examples of possible sentences to be analyzed by the compiler.

Compiler constraints: 

* Compiler must be in LEX and YACC
* Compiler must read the sentence from a file
* Compiler must generate a file: instructions. asm with the list of instructions, ie:

```
	MOV,2
	TURN,90
	MOV,4
```

# CPU Automata for basic robot 🤖

## Automata

![CPU Automata](https://raw.githubusercontent.com/NolbertoCastro/MovTurn/main/cpu/Automata.png)

## **Language**

Python

## Instructions

**MOV** = Move in the directions the robot is facing.

**TURN** = Turns 90, 180, 270 or 360 degrees to the left.

## Example

```
MOV, 4
TURN, 270
MOV, 5
```

## Output:

### Starting Point:

```
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
```

### First Movement:

```
['--', '--', '--', '--', 'XX', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
```

### Rotation and Second Movement:

```
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', 'XX', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
```


# LEX generator with valid tokens 

## Description:

A language must be created to be able to communicate with the robot. In the LEX we must specify all the characters that the language will detect and it must turn them into tokens that will then be read by the parser. At this point if the tokens are detected correctly, it's working fine.

The language for the robot will be variations of the next sentence: 

### Robot, please move 3 blocks, then move 2 blocks.

It must containt the word robot at the beginning, followed by a kind word, followed by one or many instructions. There are many ways of formulation the previous sentences, so ChatGPT was used to get many variations. 

The tokens are as follows:

- ROBOT
- PLEASE
- VERB
- TURN
- ROTATE
- AHEAD
- NUMBER
- BLOCKS
- DEGREES
- COMMA
- POINT
- AND
- THEN
- BY
- FOR
- DISTANCE
- OF
- MAKE
- A

Many of the tokens can be detected with multiple words like the token verb which is detected with move, proceed, shift, travel, etc.

The LEX must detect any of these words correctly, but it won't be able to detect grammar.

## Example

### ACCEPTED

- Robot, please
- move 3 blocks
- turn 90 degrees
- make a robot.
- . and then, please robot move

### REJECTED

- asldkaskdljsadklj
- kjweoiuew91239823198qwioeuqweoiuwqe
- make me a sandwich
- fly to the moon
- turn on the lights


# CFG and YACC/LEX 
	
## DESCRIPTION:

Once the LEX is done, and it detects all the words of the language, we need to create a grammar. This grammar will identify if the instructions read form the text file are correctly written. Stating the problem again, the language for the robot will be variations of the next sentence:
	
### Robot, please move 3 blocks, then move 2 blocks.
	
It must containt the word robot at the beginning, followed by a kind word, followed by one or many instructions. There are many ways of formulation the previous sentences, so ChatGPT was used to get many variations. 
	
## CFG

The resulting CFG is as follows: 

instructions: instruction | instruction POINT | instructions EOL | instructions EOL instructions 

instruction: ROBOT PLEASE SIMPLE_INSTRUCTION | ROBOT COMMA PLEASE SIMPLE_INSTRUCTION

SIMPLE_INSTRUCTION: PHRASE | PHRASE EXTRA

PHRASE: ROTATE NUMBER DEGREES | VERB NUMBER BLOCKS AHEAD | VERB NUMBER BLOCKS | TURN NUMBER DEGREES | VERB BY NUMBER BLOCKS | VERB AHEAD BY NUMBER BLOCKS | VERB AHEAD FOR A DISTANCE OF NUMBER BLOCKS | MAKE A NUMBER DEGREE TURN
	
EXTRA: CONNECTOR SIMPLE_INSTRUCTION
	
CONNECTOR: COMMA AND | COMMA THEN | COMMA AND THEN | COMMA | AND THEN
	
## Inputs
Some of the insputs that must be accepted are the following:
	- Robot, please move ahead by 2 blocks.
	- Robot, please advance 3 blocks forward
	- Robot, please advance by 3 blocks, make a 90 degree turn, and then proceed forward by 2 blocks.
Some of the inputs that must be rejected are the following:
	- Robot move 30 blocks
	- Robot, please fly 100 blocks to Europe
	- Robot, please forward 3 blocks turn . move
