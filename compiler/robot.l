%{
#include "y.tab.h"
#include <stdio.h>
extern int yylval;
%}
%%
robot	 			{return ROBOT; }
Robot	 			{return ROBOT; }
please				{return PLEASE; }
move				{return VERB; }
advance				{return VERB; }
shift				{return VERB; }
travel				{return VERB; }
proceed				{return VERB; }
go				{return VERB; }
march				{return VERB; }
propel				{return VERB; }
turn				{return TURN; }
rotate				{return ROTATE; }
[0-9]+				{ yylval = atoi(yytext); return NUMBER; }
ahead				{return AHEAD; }
forward				{return AHEAD; }
blocks				{return BLOCKS; }
degrees				{return DEGREES; }
degree				{return DEGREE; }
,				{return COMMA;}
by				{return BY;}
and				{return AND;}
then				{return THEN;}
for				{return FOR;}
a				{return A;}
distance			{return DISTANCE;}
of				{return OF;}
make				{return MAKE;}
[ \t] ; 			/* ignore whitespace */
[\n] return EOL; 		 		/* logical EOF */
. return POINT;
%%
int yywrap()
{
return 1;
}
