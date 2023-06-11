# CFG and YACC/LEX 

# Instituto Tecnológico y de Estudios Superiores de Monterrey

![tec de monterrey Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Logo_del_ITESM.svg/320px-Logo_del_ITESM.svg.png)

### Team:

Nolberto Castro Sánchez | A01641501

Jesús Enrique Díaz Bernal Robinson Bours | A00227255

### Github Repository Link:

https://github.com/NolbertoCastro/MovTurn

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
Some of the inputs that must be accepted are the following:
* Robot, please move ahead by 2 blocks.
* Robot, please advance 3 blocks forward
* Robot, please advance by 3 blocks, make a 90 degree turn, and then proceed forward by 2 blocks.


Some of the inputs that must be rejected are the following:
* Robot move 30 blocks
* Robot, please fly 100 blocks to Europe
* Robot, please forward 3 blocks turn . move
