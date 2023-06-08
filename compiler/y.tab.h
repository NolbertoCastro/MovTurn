/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    ROBOT = 258,                   /* ROBOT  */
    PLEASE = 259,                  /* PLEASE  */
    VERB = 260,                    /* VERB  */
    TURN = 261,                    /* TURN  */
    AHEAD = 262,                   /* AHEAD  */
    NUMBER = 263,                  /* NUMBER  */
    EOL = 264,                     /* EOL  */
    BLOCKS = 265,                  /* BLOCKS  */
    DEGREES = 266,                 /* DEGREES  */
    COMMA = 267,                   /* COMMA  */
    AND = 268,                     /* AND  */
    THEN = 269,                    /* THEN  */
    BY = 270,                      /* BY  */
    POINT = 271,                   /* POINT  */
    FOR = 272,                     /* FOR  */
    A = 273,                       /* A  */
    DISTANCE = 274,                /* DISTANCE  */
    OF = 275,                      /* OF  */
    DEGREE = 276,                  /* DEGREE  */
    MAKE = 277,                    /* MAKE  */
    ROTATE = 278                   /* ROTATE  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif
/* Token kinds.  */
#define YYEMPTY -2
#define YYEOF 0
#define YYerror 256
#define YYUNDEF 257
#define ROBOT 258
#define PLEASE 259
#define VERB 260
#define TURN 261
#define AHEAD 262
#define NUMBER 263
#define EOL 264
#define BLOCKS 265
#define DEGREES 266
#define COMMA 267
#define AND 268
#define THEN 269
#define BY 270
#define POINT 271
#define FOR 272
#define A 273
#define DISTANCE 274
#define OF 275
#define DEGREE 276
#define MAKE 277
#define ROTATE 278

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
