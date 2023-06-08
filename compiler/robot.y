%{
#include <stdio.h>
extern int yylex(void);
extern int yyparse();
int yyerror(char* s);
extern FILE *yyin;
int passed;
FILE *fresult;

%}
%token ROBOT PLEASE VERB TURN AHEAD NUMBER EOL BLOCKS DEGREES COMMA AND THEN BY POINT FOR A DISTANCE OF DEGREE MAKE ROTATE
%%

instructions: instruction
 | instruction POINT
 | instructions EOL 
 | instructions EOL instructions 
 ;

instruction: ROBOT PLEASE SIMPLE_INSTRUCTION 
| ROBOT COMMA PLEASE SIMPLE_INSTRUCTION
;
 
SIMPLE_INSTRUCTION: PHRASE
| PHRASE EXTRA
;

PHRASE: ROTATE NUMBER DEGREES					{fprintf(fresult, "TURN, %d\n", $2);}
| VERB NUMBER BLOCKS AHEAD				{fprintf(fresult, "MOV, %d\n", $2);}
| VERB NUMBER BLOCKS					{fprintf(fresult, "MOV, %d\n", $2);}
| TURN NUMBER DEGREES					{fprintf(fresult, "TURN, %d\n", $2);}
| VERB BY NUMBER BLOCKS					{fprintf(fresult, "MOV, %d\n", $3);}
| VERB AHEAD BY NUMBER BLOCKS				{fprintf(fresult, "MOV, %d\n", $4);}
| VERB AHEAD FOR A DISTANCE OF NUMBER BLOCKS		{fprintf(fresult, "MOV, %d\n", $7);}
| MAKE A NUMBER DEGREE TURN				{fprintf(fresult, "TURN, %d\n", $3);}

EXTRA: CONNECTOR SIMPLE_INSTRUCTION
;

CONNECTOR: COMMA AND
| COMMA THEN
| COMMA AND THEN
| COMMA
| AND THEN
;
 
%% 
int main(int argc, char **argv) {
    FILE *fd;
    fresult = fopen("instructions.asm", "w");
    char c;

    if (argc == 2)
    {
        if (!(fd = fopen(argv[1], "r")))
        {
            perror("Error: ");
            return (-1);
        }
        yyin = fd;
        
        yyparse();
        yylex();
        fclose(fd);
    	fclose(fresult);
    }
    else
        printf("Usage: a.out filename\n");
    return (0);
}
