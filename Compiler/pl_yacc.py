import ply.yacc as yacc
import sys
import re

from pl_lex import tokens
from pl_lex import literals
from pl_lex import reserved

def p_grammar(p):
    """
    prog : declrs funcs main
         | declrs main
         | main      
    main : MAIN '{' instrs '}'    
    funcs : funcs func
          | func
    func  : DEF ID '(' ')' '{' instrs '}'
    instrs : instrs instr
           | instr
    instr : atr    
          | write 
          | read            
          | cond   
          | loop            
          | fcall  
          |                 
    fcall : ID '(' ')' ';' 
    cond : IF '(' expr ')' '{' instrs '}'                          
         | IF '(' expr ')' '{' instrs '}' ELSE '{' instrs '}'  
         | IF '(' expr ')' '{' instrs '}' ELSE cond              
    loop : WHILE '(' expr ')' DO '{' instrs '}'
    write : WRITE '(' STR ')'
    read : READ '(' STR ')'
    atr : ID '=' expr ';'            
        | ID '=' read ';'                 
        | ID '[' expr ']' '=' expr
        | ID '[' expr ']' '=' read
    declrs : declrs declr   
           | declr
    declr : INT decllist      
    decllist : decllist ',' singdecl 
             | singdecl        
    singdecl : ID ';'                           
             | ID '[' NUM ']' ';'                
             | ID '=' expr ';'               
             | ID '=' read ';'                       
             | ID '[' NUM ']' '=' '[' list ']' ';'   
    list : expr ',' list       
         | expr                 
    expr : expr AND lexpr   
         | expr OR lexpr     
         | '!' lexpr     
         | lexpr            
    lexpr : lexpr EQ arithm   
          | lexpr NEQ arithm  
          | lexpr GEQ arithm  
          | lexpr LEQ arithm 
          | lexpr '>' arithm    
          | lexpr '<' arithm    
          | arithm              
    arithm : arithm '+' term    
           | arithm '-' term    
           | term               
    term : term '*' par    
         | term '/' par    
         | term '%' par    
         | par             
    par : '(' expr ')'        
        | factor              
    factor : NUM                    
           | ID                     
           | ID '[' expr ']'
    """
# vai ficar a faltar a negacao pq n sei como vai funcionar por causa da subtracao. mas a fazer depois é so mexer nos factor

def p_error(p):
    parser.success = False
    print("erro: ",p)


# Build the parser
parser = yacc.yacc()
parser.success = True

inputfile = open(sys.argv[1], 'r')
res = re.match('([_a-zA-Z0-9]+)',sys.argv[1])
outputfilename = res.group(1) + ".vm"
out = "START\n"

parser.parse(inputfile.read(), debug=True)
if parser.success:
    print('Parsing completed!')
    out+= "STOP\n"
    outfile = open(outputfilename,"w+")
    outfile.write(out)
    outfile.close
    print("Gerado o ficheiro ",outputfilename)
