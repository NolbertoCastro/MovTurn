# MOV TURN

# Instituto Tecnológico y de Estudios Superiores de Monterrey

![tec de monterrey Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Logo_del_ITESM.svg/320px-Logo_del_ITESM.svg.png)

### Team:

Nolberto Castro Sánchez | A01641501

Jesús Enrique Díaz Bernal Robinson Bours | A00227255

### Github Repository Link:

https://github.com/NolbertoCastro/MovTurn

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
