import sys
import re
import os
import ply.yacc as yacc
from lexer import tokens
from lexer import literals
from lexer import reserved

#criacao do ficheiro de código para a VM
res = re.match('([_a-zA-Z0-9]+)',sys.argv[1])
outputfilename = res.group(1) + ".vm"
out = open(outputfilename,"w+")
out.write("START\n")

#vars
def p_prog_declrs_funcs(p):
    "prog : declrs funcs main"

def p_prog_declrs_main(p):
    "prog : declrs main"

def p_prog_main(p):
    "prog : main"

def p_main(p):
    "main : MAIN '{' instrs '}'"
    p[0] = p[3]

def p_declrs_declrs(p):
    "declrs : declrs declr"

def p_declrs_declr(p):
    "declrs : declr"
    p[0] = p[1]

def p_declr(p):
    "declr : INT decllist"
    p[0] = p[2]

#def p_decllist(p):
#    "decllist : decllist ',' singdecl"

def p_decllist_single(p):
    "decllist : singdecl"
    p[0] = p[1]

def p_funcs_funcs(p):
    "funcs : funcs func"

def p_singdecl_id(p):
    "singdecl : ID ';'"
    parser.vars[p[1]] = (parser.contador,1)
    out.write("PUSHI 0\n")
    parser.contador+=1
    out.write

def p_singdecl_expr(p):
    "singdecl : ID '=' expr ';'"
    parser.vars[p[1]] = (parser.contador,1)
    parser.contador+=1
    p[0] = p[3]

#def p_singdecl_read(p):
#    "singdecl : ID '=' read;'"  # Acho que o ';' esta a mais pq read ja termina com ;
#    pass

def p_singdecl_arr(p):
    "singdecl : ID '[' NUM ']' ';'"
    parser.vars[p[1]] = (parser.contador,p[3])
    out.write("PUSHN " + p[3] + "\n")
    parser.contador+=int(p[3])
    out.write


#def p_singdecl_arr_list(p):
#    "singdecl : ID '[' NUM ']' '=' '[' list ']' ';'"
#    pass


def p_list_exprl(p):
    "list : list ',' expr"

def p_list_expr(p):
    "list : expr"
    p[0] = p[1]


#def p_expr_and(p):
#    "expr : expr AND lexpr"
#    pass
#
#
#def p_expr_or(p):
#    "expr : expr OR lexpr"
#    pass
#
#
#def p_expr_not(p):
#    "expr : '!' lexpr"
#    pass


def p_expr_lexpr(p):
    "expr : lexpr"
    p[0] = p[1]


def p_lexpr_eq(p):
    "lexpr : lexpr EQ arithm"
    out.write("EQUAL\n")

#def p_lexpr_neq(p):
#    "lexpr : lexpr NEQ arithm"
#    pass


def p_lexpr_g(p):
    "lexpr : lexpr '>' arithm"
    out.write("SUP\n")


def p_lexpr_l(p):
    "lexpr : lexpr '<' arithm"
    out.write("INF\n")



def p_lexpr_geq(p):
    "lexpr : lexpr GEQ arithm"
    out.write("SUPEQ\n")


def p_lexpr_leq(p):
    "lexpr : lexpr LEQ arithm"
    out.write("INFEQ\n")



def p_lexpr_arithm(p):
    "lexpr : arithm"
    p[0] = p[1]


def p_arithm_plus(p):
    "arithm : arithm '+' term"
    out.write("ADD\n")

def p_arithm_minus(p):
    "arithm : arithm '-' term"   
    out.write("SUB\n")

def p_arithm_term(p):
    "arithm : term"
    p[0] = p[1]

def p_term_mul(p):
    "term : term '*' par"
    out.write("MUL\n")
    
def p_term_div(p):
    "term : term '/' par"
    out.write("DIV\n")


def p_term_mod(p):
    "term : term '%' par"
    out.write("MOD\n")


def p_term_par(p):
    "term : par"
    p[0] = p[1]


def p_par_expr(p):
    "par : '(' expr ')'"
    p[0] = p[2]


def p_par_factor(p):
    "par : factor"
    p[0] = p[1]


def p_factor_num(p):
    "factor : NUM"
    out.write("PUSHI " + p[1] + "\n")

def p_factor_id(p):
    "factor : ID"
    out.write("PUSHG " + str(parser.vars.get(p[1])[0])+"\n")

def p_factor_arr(p):
    "factor : ID '[' expr ']'"
    pass

def p_funcs_func(p):
    "funcs : func"
    p[0] = p[1]


def p_func(p):
    "func : DEF ID '(' ')' '{' instrs '}'"  # Funcoes com argumentos ??
    pass


def p_instrs_instrs(p):
    "instrs : instrs instr"

def p_instrs_instr(p):
    "instrs : instr"
    p[0] = p[1]

def p_instr_atr(p):
    "instr : atr"
    p[0] = p[1]


def p_instr_write(p):
    "instr : write"
    p[0] = p[1]


def p_instr_read(p):
    "instr : read"
    p[0] = p[1]


def p_instr_cond(p):
    "instr : cond"
    p[0] = p[1]

def p_instr_loop(p):
    "instr : loop"
    p[0] = p[1]


def p_instr_fcall(p):
    "instr : fcall"
    p[0] = p[1]

def p_instr_vazio(p):
    "instr : "
    pass


def p_atr_expr(p):
    "atr : ID '=' expr ';'"
    out.write("STOREG " + str(parser.vars.get(p[1])[0]) + "\n")
    p[0] = p[3]


def p_atr_read(p):
    "atr : ID '=' read"
    out.write("READ\n")
    out.write("ATOI\n")
    out.write("STOREG " + str(parser.vars.get(p[3])[0]) + "\n")


#def p_atr_arr_expr(p):
#    "atr : ID '[' expr ']' '=' expr ';'"
#    pass


def p_atr_arr_read(p):
    "atr : ID '[' expr ']' '=' read"
    out.write("READ\n")
    out.write("ATOI\n")
    out.write("STOREG " + str(parser.vars.get(p[1])[0]+parser.vars.get(p[3])[1]) + "\n")

def p_write_str(p):
    "write : WRITE '(' STR ')' ';' "
    out.write("PUSHS" + p[3] + "\n")
    out.write("WRITES\n")
    out.write("PUSHS\"\\n\"\n")
    out.write("WRITES\n")

def p_write_id(p):
    "write : WRITE '(' ID ')' ';'"
    out.write("PUSHG " + str(parser.vars.get(p[3])[0]) +"\n")
    out.write("WRITEI\n")
    out.write("PUSHS\"\\n\"\n")
    out.write("WRITES\n")

def p_read(p):
    "read : READ '(' ID ')' ';'"
    out.write("READ\n")
    out.write("ATOI\n")
    out.write("STOREG " + str(parser.vars.get(p[3])[0]) + "\n")

#if then else

def p_cond_ifelse(p):
    "cond : ifelseexpr instrscondifelse elsecond"

def p_ifelseexpr(p):
    "ifelseexpr : IF '(' expr ')'"
    out.write("JZ ELSE\n")

def p_instrscondifelse(p):
    "instrscondifelse : '{' instrs '}'"
    out.write("JUMP FIM\n")
    out.write("ELSE:\n")

def p_elsecond(p):
    "elsecond : ELSE '{' instrs '}'"
    out.write("FIM:\n")  

#if
def p_cond_if(p):
    "cond : ifexpr instrscondif"

def p_ifexpr(p):
    "ifexpr : IF '(' expr ')'"
    out.write("JZ FIM\n")

def p_instrscondif(p):
    "instrscondif : '{' instrs '}'"
    out.write("FIM:\n") 

# while do
def p_loop_while_do(p):
    "loop : whiledo whilexprs doinstrs"

def p_while(p):
    "whiledo : WHILE"
    out.write("WHILE:\n")

def p_whileexprs(p):
    "whilexprs : '(' expr ')'"
    out.write("JZ FIM\n")

def p_doinstrs(p):
    "doinstrs : DO '{' instrs '}' "
    out.write("JUMP WHILE\n")
    out.write("FIM:\n")
   

def p_fcall(p):
    "fcall : ID '(' ')' ';'"
    pass

def p_error(p):
    print(f'Syntatic  Error {p}')
    parser.success = False


# Build the parser
parser = yacc.yacc()

# Build the parser
parser = yacc.yacc()
parser.success = True
parser.vars = {}
parser.contador = 0

inputfile = open(sys.argv[1], 'r')

parser.parse(inputfile.read(), debug=True)
if parser.success:
    print('Parsing completado!')
    out.write("STOP\n")
    out.close
    print("Gerado o ficheiro ",outputfilename)
    #print(parser.vars)
    #print(parser.contador)
else:
   os.remove(outputfilename) 
