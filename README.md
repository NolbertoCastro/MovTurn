# MOV TURN

# Instituto Tecnológico y de Estudios Superiores de Monterrey

![tec de monterrey Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Logo_del_ITESM.svg/320px-Logo_del_ITESM.svg.png)

### Team:

Nolberto Castro Sánchez | A01641501

Jesús Enrique Díaz Bernal Robinson Bours | A00227255

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

