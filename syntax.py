import keywords

#note: 
#VARIABLE ASSIGNMENT USING R = wala pang syntax para sa expression
varidents = {}
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def getVaridents(text):
    syntax(text)
    # print(varidents, "syntax")
    return varidents

def syntax(text):
    global varidents
    varidents.clear()
    syntaxResult = ''
    success = 1
    comparison = ['BOTH SAEM', 'DIFFRINT']
    arithmetic = ['SUM OF','DIFF OF','PRODUKT OF', 'QUOSHUNT OF', 'MOD OF', 'BIGGR OF', 'SMALLR OF']
    literals = ['NUMBR Literal', 'NUMBAR Literal', 'YARN Literal', 'TROOF Literal', 'Type Literal']
    varAssignment_literals = ['NUMBR Literal', 'NUMBAR Literal', 'YARN Literal', 'TROOF Literal', 'Type Literal']
    booleans = ['BOTH OF', 'EITHER OF', 'WON OF', 'NOT']
    hasHai = -1
    hasKthxbye = -1
    hasWazzup = -1
    hasBuhbye = -1
    hasVarDec = 0
    for h in range(0, len(text.splitlines())):
        lexeme = keywords.lex(text.splitlines()[h].lstrip().rstrip())
        if lexeme is not None:
            if ['BTW', 'Comment Delimiter'] in lexeme:
                lexeme.pop(lexeme.index(['BTW', 'Comment Delimiter'])+1)
                lexeme.pop(lexeme.index(['BTW', 'Comment Delimiter']))
                
            for i in range(0, len(lexeme)):
                # print(lexeme[i][0])
                ## PROGRAM BLOCK SYNTAX - HAI
                if lexeme[i][0] == 'HAI' and hasHai == -1 and hasKthxbye == -1:
                    hasHai = 0
                    break
                else:
                        if lexeme[i][0] == 'HAI' and hasHai > -1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <HAI>: \n\tAlready has HAI; it must be declared once')
                            success = 0
                            break
                        elif lexeme[i][0] == 'HAI' and hasKthxbye > -1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <HAI>: \n\HAI must be declared before KTHXBYE')
                            success = 0
                            break
                if hasHai == 0:
                    ## VARIABLE BLOCK SYNTAX - WAZZUP
                    if lexeme[i][0] == 'WAZZUP' and hasWazzup == -1 and hasBuhbye == -1:
                        hasWazzup = 0
                        break
                    else:
                        if lexeme[i][0] == 'WAZZUP' and hasWazzup > -1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <WAZZUP>: \n\tAlready has WAZZUP; it must be declared once')
                            success = 0
                            break
                        elif lexeme[i][0] == 'WAZZUP' and hasBuhbye > -1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <WAZZUP>: \n\tWAZZUP must be declared before BUHBYE')
                            success = 0
                            break
                    ## VARIABLE DECLARATION SYNTAX
                    if lexeme[i][0] == 'I HAS A' and hasWazzup == 0:
                        if len(lexeme) < 2 or lexeme[i+1][1] != 'Variable Identifier':
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tI HAS A must have a variable identifier')
                            success = 0
                            break
                        elif len(lexeme) > 2:
                            if lexeme[i+2][0] != 'ITZ':
                                syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'ITZ' keyword?")
                                success = 0
                                break
                            elif len(lexeme) < 4 or (lexeme[i+3][1] not in varAssignment_literals and lexeme[i+3][1] != 'Variable Identifier'):
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\tITZ must have a literal or variable identifier')
                                success = 0
                                break
                        hasVarDec = 1
                        if len(lexeme) == 2:
                            varidents[lexeme[i+1][0]] = 'NOOB'
                        elif len(lexeme) == 4:
                            if isfloat(lexeme[i+3][0]) != False and int(float(lexeme[i+3][0])) - float(lexeme[i+3][0]) != 0:
                                varidents[lexeme[i+1][0]] = float(lexeme[i+3][0])       # if NUMBAR
                            elif isfloat(lexeme[i+3][0]) != False and int(float(lexeme[i+3][0])) - float(lexeme[i+3][0]) == 0:
                                varidents[lexeme[i+1][0]] = int(float(lexeme[i+3][0]))         # if NUMBR
                            else:
                                varidents[lexeme[i+1][0]] = lexeme[i+3][0]              # if TROOF or YARN
                        break
                    else:
                        if lexeme[i][0] != 'I HAS A' and lexeme[i][0] != 'BUHBYE' and lexeme[i][0] != 'KTHXBYE' and hasWazzup == 0 and hasBuhbye == -1: 
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} in <WAZZUP> block: \n\tonly I HAS A statements can be inside WAZZUP and BUHBYE')
                            success = 0
                            break
                        elif lexeme[i][0] == 'I HAS A':
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <I HAS A>: \n\tI HAS A statements must be inside WAZZUP and BUHBYE')
                            success = 0
                            break
                    ## VARIABLE BLOCK SYNTAX - BUHBYE
                    if lexeme[i][0] == 'BUHBYE' and hasWazzup == 0:
                        hasBuhbye = 0
                        hasWazzup = 1
                        break
                    else:
                        if lexeme[i][0] == 'BUHBYE' and hasWazzup == -1 and hasBuhbye == -1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <BUHBYE>: \n\tBUHBYE must be declared after WAZZUP')
                            success = 0
                            break
                        elif lexeme[i][0] == 'BUHBYE' and hasWazzup == 0 and hasBuhbye == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <BUHBYE>: \n\tAlready has BUHBYE; it must be declared once')
                            success = 0
                            break
                    # ## PRINTING
                    # if lexeme[i][0] == 'VISIBLE':
                    #     # if less than
                    #     if len(lexeme) < 2:
                    #         print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tVISIBLE must have a Variable Identifier, Literal, or an Expression')
                    #     else:
                    #         #VARIDENT
                    #         if lexeme[i+1][1] != 'String Delimiter':
                    #             #LITERAL
                    #             if lexeme[i+1][0].isnumeric() == False:
                    #                 #EXPRESSIONS
                    #                 if lexeme[i+1][1] != 'Arithmetic Keyword' | lexeme[i+1][1] != 'Boolean Keyword' | lexeme[i+1][1] != 'Comparison Keyword':
                    #                     print(f'>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\tVISIBLE only accepts Variable Identifier, Literal, and Expression')
                    #                     success = 0
                    #         else:
                    #             #condition para pag nakalimutan ng quotation sa dulo!
                    #             if lexeme[i+3][1] != 'String Delimiter':
                    #                 print(f'>> SyntaxError in line {h+1} near <{lexeme[i+3][1]}>: \n\tVariable Identifier ')
                    #                 success = 0

                    ## COMPARISON SYNTAX - BOTH SAEM
                    # print(lexeme[i][0])
                    if lexeme[i][0] == 'BOTH SAEM':
                        # /print(lexeme, "syntax")
                        # print(varidents)
                        

                        if isfloat(lexeme[i+1][0]) == False:
                            # print("pasok")
                            if lexeme[i+1][0] not in varidents:
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tBOTH SAEM only accepts NUMBR or NUMBAR type')
                                success = 0
                                break
                            else:
                                if isfloat(varidents[lexeme[i+1][0]]) == False:
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tBOTH SAEM only accepts NUMBR or NUMBAR type variable')
                                    success = 0
                                    break

                        
                        if len(lexeme) == 4 or (len(lexeme) == 6 and lexeme[i-1][0] == 'R'):
                            if lexeme[i+2][0] != 'AN':
                                syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                                success = 0
                                break
                            
                            elif isfloat(lexeme[i+3][0]) == False:
                                if lexeme[i+3][0] not in varidents:
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tBOTH SAEM only accepts NUMBR or NUMBAR type')
                                    success = 0
                                    break
                                else:
                                    if isfloat(varidents[lexeme[i+3][0]]) == False:
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tBOTH SAEM only accepts NUMBR or NUMBAR type variable')
                                        success = 0
                                        break
                                
                        elif len(lexeme) == 7 or (len(lexeme) == 9 and lexeme[i-1][0] == 'R'):
                            if lexeme[i+2][0] != 'AN':
                                syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                                success = 0
                                break
                            elif lexeme[i+3][0] != 'SMALLR OF' and lexeme[i+3][0] != 'BIGGR OF':
                                syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+2][0]}>: \n\t{lexeme[i+3][0]} is recognized incorrectly. Perhaps you need a 'SMALLR OF' or 'BIGGR OF' keyword?")
                                success = 0
                                break
                            elif isfloat(lexeme[i+4][0]) == False and  lexeme[i+4][0] != lexeme[i+1][0]:
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                                success = 0
                                break
                            elif lexeme[i+5][0] != 'AN':
                                syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+4][0]}>: \n\t{lexeme[i+5][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                                success = 0
                                break
                            elif isfloat(lexeme[i+6][0]) == False:
                                if lexeme[i+6][0] not in varidents:
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                                    success = 0
                                    break
                                else:
                                    if isfloat(varidents[lexeme[i+6][0]]) == False:
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                                        success = 0
                                        break
                        else:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tBOTH SAEM <value> [[AN BIGGR OF|SMALLR OF] <value>] AN <value>')
                            success = 0
                            break  
                    ## COMPARISON SYNTAX - DIFFRINT
                    if lexeme[i][0] == 'DIFFRINT':
                        # if len(lexeme) != 4 and len(lexeme) != 7:
                        #     if len(lexeme) == 6 and lexeme[i-1][0] != 'R':
                        #         syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tBOTH SAEM <value> [[AN BIGGR OF|SMALLR OF] <value>] AN <value>')
                        #         success = 0
                        #         break
                            
                        if isfloat(lexeme[i+1][0]) == False or isfloat(lexeme[i+1][0]) == False:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tDIFFRINT only accepts NUMBR or NUMBAR type')
                            success = 0
                            break
                        
                        if len(lexeme) == 4 or (len(lexeme) == 6 and lexeme[i-1][0] == 'R'):
                            if lexeme[i+2][0] != 'AN':
                                syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                                success = 0
                                break
                            elif isfloat(lexeme[i+3][0]) == False or isfloat(lexeme[i+3][0]) == False:
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tDIFFRINT only accepts NUMBR or NUMBAR type')
                                success = 0
                                break
                        elif len(lexeme) == 7 or (len(lexeme) == 9 and lexeme[i-1][0] == 'R'):
                            if lexeme[i+2][0] != 'AN':
                                syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                                success = 0
                                break
                            elif lexeme[i+3][0] != 'SMALLR OF' and lexeme[i+3][0] != 'BIGGR OF':
                                syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+2][0]}>: \n\t{lexeme[i+3][0]} is recognized incorrectly. Perhaps you need a 'SMALLR OF' or 'BIGGR OF' keyword?")
                                success = 0
                                break
                            elif isfloat(lexeme[i+4][0]) == False or isfloat(lexeme[i+4][0]) == False:
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                                success = 0
                                break
                            elif lexeme[i+5][0] != 'AN':
                                syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+4][0]}>: \n\t{lexeme[i+5][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                                success = 0
                                break
                            elif isfloat(lexeme[i+6][0]) == False or isfloat(lexeme[i+6][0]) == False:
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                                success = 0
                                break
                        else:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tBOTH SAEM <value> [[AN BIGGR OF|SMALLR OF] <value>] AN <value>')
                            success = 0
                            break

                    ##INFINITE ARITY BOOLEAN SYNTAX - ALL OF
                    if lexeme[i][0] == 'ALL OF':
                        boolean_index = 1
                        if len(lexeme) < 5:
                            success = 0
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tALL OF <finite_bool_expr> AN <finite_bool_expr> [[AN <finite_bool_expr>...] MKAY')
                            break
                        while boolean_index < len(lexeme)-2:
                            if lexeme[boolean_index][0] not in booleans and lexeme[boolean_index][0] not in varidents and lexeme[boolean_index][1] not in literals:
                                success = 0
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index][0]} is not a finite boolean keyword.')
                                break
                            else:
                                ##BOOLEAN SYNTAX - BOTH OF
                                if boolean_index+3 >= len(lexeme) or boolean_index+2 >= len(lexeme):
                                    success = 0
                                    if lexeme[boolean_index][0] != 'NOT' or lexeme[boolean_index][0] not in varidents:
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\t{lexeme[boolean_index][0]} [WIN|FAIL] AN [WIN|FAIL]')
                                    else:
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\t{lexeme[boolean_index][0]} [WIN|FAIL]')
                                    break
                                else:
                                    if lexeme[boolean_index][0] == "BOTH OF":
                                        if lexeme[boolean_index+1][0] != 'WIN':
                                            if lexeme[boolean_index+1][0] != 'FAIL':
                                                if lexeme[boolean_index+1][0] not in varidents or varidents[lexeme[boolean_index+1][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                                                    break
                                        elif lexeme[boolean_index+1][0] != 'FAIL':
                                            if lexeme[boolean_index+1][0] != 'WIN':
                                                if lexeme[boolean_index+1][0] not in varidents or varidents[lexeme[boolean_index+1][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                                                    break
                                        if lexeme[boolean_index+2][0] != 'AN':
                                            success = 0
                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tThere is a need for AN to indicate "and".')
                                            break
                                    
                                        if lexeme[boolean_index+3][0] != 'WIN':
                                            if lexeme[boolean_index+3][0] != 'FAIL':
                                                if lexeme[boolean_index+3][0] not in varidents or varidents[lexeme[boolean_index+3][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                                                    break
                                        elif lexeme[boolean_index+3][0] != 'FAIL':
                                            if lexeme[boolean_index+3][0] != 'WIN':
                                                if lexeme[boolean_index+3][0] not in varidents or varidents[lexeme[boolean_index+3][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                                                    break
                                        if ((boolean_index+4) < len(lexeme)):
                                            if lexeme[boolean_index+4][0] != 'AN' and (lexeme[boolean_index+4][0] != 'MKAY' and boolean_index+4 != len(lexeme)-1):
                                                success = 0
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+4][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                                break
                                        boolean_index += 5
                                    elif lexeme[boolean_index][0] == "EITHER OF":
                                        if lexeme[boolean_index+1][0] != 'WIN':
                                            if lexeme[boolean_index+1][0] != 'FAIL':
                                                if lexeme[boolean_index+1][0] not in varidents or varidents[lexeme[boolean_index+1][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of EITHER OF must be either WIN OR FAIL.')
                                                    break
                                        elif lexeme[boolean_index+1][0] != 'FAIL':
                                            if lexeme[boolean_index+1][0] != 'WIN':
                                                if lexeme[boolean_index+1][0] not in varidents or varidents[lexeme[boolean_index+1][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of EITHER OF must be either WIN OR FAIL.')
                                                    break
                                        if lexeme[boolean_index+2][0] != 'AN':
                                            success = 0
                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tThere is a need for AN to indicate "and".')
                                            break
                                    
                                        if lexeme[boolean_index+3][0] != 'WIN':
                                            if lexeme[boolean_index+3][0] != 'FAIL':
                                                if lexeme[boolean_index+3][0] not in varidents or varidents[lexeme[boolean_index+3][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of EITHER OF must be either WIN OR FAIL.')
                                                    break
                                        elif lexeme[boolean_index+3][0] != 'FAIL':
                                            if lexeme[boolean_index+3][0] != 'WIN':
                                                if lexeme[boolean_index+3][0] not in varidents or varidents[lexeme[boolean_index+3][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of EITHER OF must be either WIN OR FAIL.')
                                                    break
                                        if ((boolean_index+4) < len(lexeme)):
                                            if lexeme[boolean_index+4][0] != 'AN' and (lexeme[boolean_index+4][0] != 'MKAY' and boolean_index+4 != len(lexeme)-1):
                                                success = 0
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+4][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                                break
                                        boolean_index += 5
                                    elif lexeme[boolean_index][0] == "WON OF":
                                        if lexeme[boolean_index+1][0] != 'WIN':
                                            if lexeme[boolean_index+1][0] != 'FAIL':
                                                if lexeme[boolean_index+1][0] not in varidents or varidents[lexeme[boolean_index+1][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of WON OF must be either WIN OR FAIL.')
                                                    break
                                        elif lexeme[boolean_index+1][0] != 'FAIL':
                                            if lexeme[boolean_index+1][0] != 'WIN':
                                                if lexeme[boolean_index+1][0] not in varidents or varidents[lexeme[boolean_index+1][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of WON OF must be either WIN OR FAIL.')
                                                    break
                                        if lexeme[boolean_index+2][0] != 'AN':
                                            success = 0
                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tThere is a need for AN to indicate "and".')
                                            break
                                    
                                        if lexeme[boolean_index+3][0] != 'WIN':
                                            if lexeme[boolean_index+3][0] != 'FAIL':
                                                if lexeme[boolean_index+3][0] not in varidents or varidents[lexeme[boolean_index+3][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of WON OF must be either WIN OR FAIL.')
                                                    break
                                        elif lexeme[boolean_index+3][0] != 'FAIL':
                                            if lexeme[boolean_index+3][0] != 'WIN':
                                                if lexeme[boolean_index+3][0] not in varidents or varidents[lexeme[boolean_index+3][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of WON OF must be either WIN OR FAIL.')
                                                    break
                                        if ((boolean_index+4) < len(lexeme)) and (lexeme[boolean_index+4][0] != 'MKAY' and boolean_index+4 != len(lexeme)-1):
                                            if lexeme[boolean_index+4][0] != 'AN':
                                                success = 0
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+4][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                                break
                                        boolean_index += 5
                                    elif lexeme[boolean_index][0] == "NOT":
                                        if lexeme[boolean_index+1][0] != 'WIN':
                                            if lexeme[boolean_index+1][0] != 'FAIL':
                                                if lexeme[boolean_index+1][0] not in varidents or varidents[lexeme[boolean_index+1][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of NOT must be either WIN OR FAIL.')
                                                    break
                                        elif lexeme[boolean_index+1][0] != 'FAIL':
                                            if lexeme[boolean_index+1][0] != 'WIN':
                                                if lexeme[boolean_index+1][0] not in varidents or varidents[lexeme[boolean_index+1][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of NOT must be either WIN OR FAIL.')
                                                    break
                                        if ((boolean_index+2) < len(lexeme)):
                                            if lexeme[boolean_index+2][0] != 'AN' and (lexeme[boolean_index+2][0] != 'MKAY' and boolean_index+2 != len(lexeme)-1):
                                                success = 0
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+2][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                                break
                                        boolean_index += 3
                                    elif lexeme[boolean_index][0] in varidents:
                                        if varidents[lexeme[boolean_index][0]] == 'NOOB':
                                            success = 0
                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tVariable must be initialized.')
                                            break
                                        if ((boolean_index+1) < len(lexeme)):
                                            if lexeme[boolean_index+1][0] != 'AN' and (lexeme[boolean_index+1][0] != 'MKAY' and boolean_index+1 != len(lexeme)-1):
                                                success = 0
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+1][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                                break
                                        boolean_index += 2
                                    elif lexeme[boolean_index][1] in literals:
                                        if ((boolean_index+1) < len(lexeme)):
                                            if lexeme[boolean_index+1][0] != 'AN' and (lexeme[boolean_index+1][0] != 'MKAY' and boolean_index+1 != len(lexeme)-1):
                                                success = 0
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+1][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                                break
                                        boolean_index += 2
                                        
                        else:
                            if lexeme[len(lexeme)-1][0] != 'MKAY':
                                success = 0
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tMKAY must be the end, see correct syntax. \n\tALL OF <finite_bool_expr> AN <finite_bool_expr> [[AN <finite_bool_expr>...] MKAY')
                                break
                        break

                    ##INFINITE ARITY BOOLEAN SYNTAX - ANY OF
                    if lexeme[i][0] == 'ANY OF':
                        boolean_index = 1
                        if len(lexeme) < 5:
                            success = 0
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tANY OF <finite_bool_expr> AN <finite_bool_expr> [[AN <finite_bool_expr>...] MKAY')
                            break
                        while boolean_index < len(lexeme)-2:
                            if lexeme[boolean_index][0] not in booleans and lexeme[boolean_index][0] not in varidents and lexeme[boolean_index][1] not in literals:
                                success = 0
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index][0]} is not a finite boolean keyword.')
                                break
                            else:
                                ##BOOLEAN SYNTAX - BOTH OF
                                if boolean_index+3 >= len(lexeme) or boolean_index+2 >= len(lexeme):
                                    success = 0
                                    if lexeme[boolean_index][0] != 'NOT' or lexeme[boolean_index][0] not in varidents:
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\t{lexeme[boolean_index][0]} [WIN|FAIL] AN [WIN|FAIL]')
                                    else:
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\t{lexeme[boolean_index][0]} [WIN|FAIL]')
                                    break
                                else:
                                    if lexeme[boolean_index][0] == "BOTH OF":
                                        if lexeme[boolean_index+1][0] != 'WIN':
                                            if lexeme[boolean_index+1][0] != 'FAIL':
                                                if lexeme[boolean_index+1][0] not in varidents or varidents[lexeme[boolean_index+1][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                                                    break
                                        elif lexeme[boolean_index+1][0] != 'FAIL':
                                            if lexeme[boolean_index+1][0] != 'WIN':
                                                if lexeme[boolean_index+1][0] not in varidents or varidents[lexeme[boolean_index+1][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                                                    break
                                        if lexeme[boolean_index+2][0] != 'AN':
                                            success = 0
                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tThere is a need for AN to indicate "and".')
                                            break
                                    
                                        if lexeme[boolean_index+3][0] != 'WIN':
                                            if lexeme[boolean_index+3][0] != 'FAIL':
                                                if lexeme[boolean_index+3][0] not in varidents or varidents[lexeme[boolean_index+3][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                                                    break
                                        elif lexeme[boolean_index+3][0] != 'FAIL':
                                            if lexeme[boolean_index+3][0] != 'WIN':
                                                if lexeme[boolean_index+3][0] not in varidents or varidents[lexeme[boolean_index+3][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                                                    break
                                        if ((boolean_index+4) < len(lexeme)):
                                            if lexeme[boolean_index+4][0] != 'AN' and (lexeme[boolean_index+4][0] != 'MKAY' and boolean_index+4 != len(lexeme)-1):
                                                success = 0
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+4][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                                break
                                        boolean_index += 5
                                    elif lexeme[boolean_index][0] == "EITHER OF":
                                        if lexeme[boolean_index+1][0] != 'WIN':
                                            if lexeme[boolean_index+1][0] != 'FAIL':
                                                if lexeme[boolean_index+1][0] not in varidents or varidents[lexeme[boolean_index+1][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of EITHER OF must be either WIN OR FAIL.')
                                                    break
                                        elif lexeme[boolean_index+1][0] != 'FAIL':
                                            if lexeme[boolean_index+1][0] != 'WIN':
                                                if lexeme[boolean_index+1][0] not in varidents or varidents[lexeme[boolean_index+1][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of EITHER OF must be either WIN OR FAIL.')
                                                    break
                                        if lexeme[boolean_index+2][0] != 'AN':
                                            success = 0
                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tThere is a need for AN to indicate "and".')
                                            break
                                    
                                        if lexeme[boolean_index+3][0] != 'WIN':
                                            if lexeme[boolean_index+3][0] != 'FAIL':
                                                if lexeme[boolean_index+3][0] not in varidents or varidents[lexeme[boolean_index+3][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of EITHER OF must be either WIN OR FAIL.')
                                                    break
                                        elif lexeme[boolean_index+3][0] != 'FAIL':
                                            if lexeme[boolean_index+3][0] != 'WIN':
                                                if lexeme[boolean_index+3][0] not in varidents or varidents[lexeme[boolean_index+3][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of EITHER OF must be either WIN OR FAIL.')
                                                    break
                                        if ((boolean_index+4) < len(lexeme)):
                                            if lexeme[boolean_index+4][0] != 'AN' and (lexeme[boolean_index+4][0] != 'MKAY' and boolean_index+4 != len(lexeme)-1):
                                                success = 0
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+4][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                                break
                                        boolean_index += 5
                                    elif lexeme[boolean_index][0] == "WON OF":
                                        if lexeme[boolean_index+1][0] != 'WIN':
                                            if lexeme[boolean_index+1][0] != 'FAIL':
                                                if lexeme[boolean_index+1][0] not in varidents or varidents[lexeme[boolean_index+1][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of WON OF must be either WIN OR FAIL.')
                                                    break
                                        elif lexeme[boolean_index+1][0] != 'FAIL':
                                            if lexeme[boolean_index+1][0] != 'WIN':
                                                if lexeme[boolean_index+1][0] not in varidents or varidents[lexeme[boolean_index+1][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of WON OF must be either WIN OR FAIL.')
                                                    break
                                        if lexeme[boolean_index+2][0] != 'AN':
                                            success = 0
                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tThere is a need for AN to indicate "and".')
                                            break
                                    
                                        if lexeme[boolean_index+3][0] != 'WIN':
                                            if lexeme[boolean_index+3][0] != 'FAIL':
                                                if lexeme[boolean_index+3][0] not in varidents or varidents[lexeme[boolean_index+3][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of WON OF must be either WIN OR FAIL.')
                                                    break
                                        elif lexeme[boolean_index+3][0] != 'FAIL':
                                            if lexeme[boolean_index+3][0] != 'WIN':
                                                if lexeme[boolean_index+3][0] not in varidents or varidents[lexeme[boolean_index+3][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of WON OF must be either WIN OR FAIL.')
                                                    break
                                        if ((boolean_index+4) < len(lexeme)) and (lexeme[boolean_index+4][0] != 'MKAY' and boolean_index+4 != len(lexeme)-1):
                                            if lexeme[boolean_index+4][0] != 'AN':
                                                success = 0
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+4][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                                break
                                        boolean_index += 5
                                    elif lexeme[boolean_index][0] == "NOT":
                                        if lexeme[boolean_index+1][0] != 'WIN':
                                            if lexeme[boolean_index+1][0] != 'FAIL':
                                                if lexeme[boolean_index+1][0] not in varidents or varidents[lexeme[boolean_index+1][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of NOT must be either WIN OR FAIL.')
                                                    break
                                        elif lexeme[boolean_index+1][0] != 'FAIL':
                                            if lexeme[boolean_index+1][0] != 'WIN':
                                                if lexeme[boolean_index+1][0] not in varidents or varidents[lexeme[boolean_index+1][0]] == 'NOOB':
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of NOT must be either WIN OR FAIL.')
                                                    break
                                        if ((boolean_index+2) < len(lexeme)):
                                            if lexeme[boolean_index+2][0] != 'AN' and (lexeme[boolean_index+2][0] != 'MKAY' and boolean_index+2 != len(lexeme)-1):
                                                success = 0
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+2][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                                break
                                        boolean_index += 3
                                    elif lexeme[boolean_index][0] in varidents:
                                        if varidents[lexeme[boolean_index][0]] == 'NOOB':
                                            success = 0
                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tVariable must be initialized.')
                                            break
                                        if ((boolean_index+1) < len(lexeme)):
                                            if lexeme[boolean_index+1][0] != 'AN' and (lexeme[boolean_index+1][0] != 'MKAY' and boolean_index+1 != len(lexeme)-1):
                                                success = 0
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+1][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                                break
                                        boolean_index += 2
                                    elif lexeme[boolean_index][1] in literals:
                                        if ((boolean_index+1) < len(lexeme)):
                                            if lexeme[boolean_index+1][0] != 'AN' and (lexeme[boolean_index+1][0] != 'MKAY' and boolean_index+1 != len(lexeme)-1):
                                                success = 0
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+1][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                                break
                                        boolean_index += 2
                                        
                        else:
                            if lexeme[len(lexeme)-1][0] != 'MKAY':
                                success = 0
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tMKAY must be the end, see correct syntax. \n\tANY OF <finite_bool_expr> AN <finite_bool_expr> [[AN <finite_bool_expr>...] MKAY')
                                break
                        break

                    ##BOOLEAN SYNTAX - BOTH OF
                    if lexeme[i][0] == "BOTH OF":
                        # print(len(lexeme))
                        # print(lexeme[i][0])
                        # if len(lexeme) > 4 or len(lexeme) <= 3:
                            
                        if len(lexeme) == 4 or lexeme[i-1][0] == 'R':
                            if lexeme[i+1][0] != 'WIN':
                                if lexeme[i+1][0] != 'FAIL':
                                    if lexeme[i+1][0] not in varidents or varidents[lexeme[i+1][0]] == 'NOOB':
                                        success = 0
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                                        break
                            elif lexeme[i+1][0] != 'FAIL':
                                if lexeme[i+1][0] != 'WIN':
                                    if lexeme[i+1][0] not in varidents or varidents[lexeme[i+1][0]] == 'NOOB':
                                        success = 0
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                                        break
                            
                            if lexeme[i+2][0] != 'AN':
                                success = 0
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tThere is a need for AN to indicate "and".')
                                break
                        
                            if lexeme[i+3][0] != 'WIN':
                                if lexeme[i+3][0] != 'FAIL':
                                    if lexeme[i+3][0] not in varidents or varidents[lexeme[i+3][0]] == 'NOOB':
                                        success = 0
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                                        break
                                break
                            elif lexeme[i+3][0] != 'FAIL':
                                if lexeme[i+3][0] != 'WIN':
                                    if lexeme[i+3][0] not in varidents or varidents[lexeme[i+3][0]] == 'NOOB':
                                        success = 0
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                                        break
                                break
                        # elif lexeme[i-1][0] == 'R':
                        else:
                            success = 0
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tBOTH OF [WIN|FAIL] AN [WIN|FAIL]')
                            break

                    #BOOLEAN SYNTAX - EITHER OF
                    if lexeme[i][0] == "EITHER OF":
                        # if len(lexeme) > 4 or len(lexeme) <= 3:
                        #     success = 0
                        #     syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tBOTH OF [WIN|FAIL] AN [WIN|FAIL]')
                        #     break
                        if len(lexeme) == 4 or lexeme[i-1][0] == 'R':
                            if lexeme[i+1][0] != 'WIN':
                                if lexeme[i+1][0] != 'FAIL':
                                    if lexeme[i+1][0] not in varidents or varidents[lexeme[i+1][0]] == 'NOOB':
                                        success = 0
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                                        break
                            elif lexeme[i+1][0] != 'FAIL':
                                if lexeme[i+1][0] != 'WIN':
                                    if lexeme[i+1][0] not in varidents or varidents[lexeme[i+1][0]] == 'NOOB':
                                        success = 0
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                                        break
                            
                            if lexeme[i+2][0] != 'AN':
                                success = 0
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tThere is a need for AN to indicate "and".')
                                break
                        
                            if lexeme[i+3][0] != 'WIN':
                                if lexeme[i+3][0] != 'FAIL':
                                    if lexeme[i+3][0] not in varidents or varidents[lexeme[i+3][0]] == 'NOOB':
                                        success = 0
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                                        break
                                break
                            elif lexeme[i+3][0] != 'FAIL':
                                if lexeme[i+3][0] != 'WIN':
                                    if lexeme[i+3][0] not in varidents or varidents[lexeme[i+3][0]] == 'NOOB':
                                        success = 0
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                                        break
                                break
                        else:
                            success = 0
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tBOTH OF [WIN|FAIL] AN [WIN|FAIL]')
                            break
                    
                    ##BOOLEAN SYNTAX - WON OF
                    if lexeme[i][0] == "WON OF":
                        # if len(lexeme) > 4 or len(lexeme) <= 3:
                        #     success = 0
                        #     syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tBOTH OF [WIN|FAIL] AN [WIN|FAIL]')
                        #     break
                        if len(lexeme) == 4 or lexeme[i-1][0] == 'R':
                            if lexeme[i+1][0] != 'WIN':
                                if lexeme[i+1][0] != 'FAIL':
                                    if lexeme[i+1][0] not in varidents or varidents[lexeme[i+1][0]] == 'NOOB':
                                        success = 0
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                                        break
                            elif lexeme[i+1][0] != 'FAIL':
                                if lexeme[i+1][0] != 'WIN':
                                    if lexeme[i+1][0] not in varidents or varidents[lexeme[i+1][0]] == 'NOOB':
                                        success = 0
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                                        break
                                
                            if lexeme[i+2][0] != 'AN':
                                success = 0
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tThere is a need for AN to indicate "and".')
                                break
                        
                            if lexeme[i+3][0] != 'WIN':
                                if lexeme[i+3][0] != 'FAIL':
                                    if lexeme[i+3][0] not in varidents or varidents[lexeme[i+3][0]] == 'NOOB':
                                        success = 0
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                                        break
                                break
                            elif lexeme[i+3][0] != 'FAIL':
                                if lexeme[i+3][0] != 'WIN':
                                    if lexeme[i+3][0] not in varidents or varidents[lexeme[i+3][0]] == 'NOOB':
                                        success = 0
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                                        break
                                break
                        else:
                            success = 0
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tBOTH OF [WIN|FAIL] AN [WIN|FAIL]')
                            break
                    
                    ##BOOLEAN SYNTAX - NOT
                    if lexeme[i][0] == "NOT":
                        # print(lexeme)
                        # print(lexeme[i][0], lexeme[i-1][0])
                        # if len(lexeme) > 3 or len(lexeme) < 2: 
                        #     success = 0
                        #     syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tNOT [WIN|FAIL]')
                        #     break
                        if len(lexeme) == 2 or lexeme[i-1][0] == 'R':
                            # print('pasok')
                            if lexeme[i+1][0] != 'WIN' and lexeme[i+1][0] != 'FAIL' and (lexeme[i+1][0] not in varidents or varidents[lexeme[i+1][0]] == 'NOOB'):
                                        success = 0
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                                        break
                            # elif lexeme[i+1][0] != 'FAIL':
                            #     if lexeme[i+1][0] != 'WIN':
                            #         if lexeme[i+1][0] not in varidents or varidents[lexeme[i+1][0]] == 'NOOB':
                            #             success = 0
                            #             syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                            #             break
                        else:
                            success = 0
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tNOT [WIN|FAIL]')
                            break

                    ## CONCATENATION BLOCK SYNTAX - SMOOSH
                    if lexeme[i][0] == 'SMOOSH':
                        if len(lexeme) <= 2 or len(lexeme)%2 == 1:
                            success = 0
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tSMOOSH <value> AN <value> [[AN <value>]...]')
                            break
                        elif lexeme[i+1][1] not in literals:
                            if lexeme[i+1][1] not in varidents and lexeme[i+1][0] != '"':
                                success = 0
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i+1][0]} is not declared.')
                                break
                        else:
                            for j in range(0, int((len(lexeme)-2)/2)):
                                if lexeme[(j+1)*2][0] != 'AN' and lexeme[(j+1)*2][0] != '"':
                                    success = 0
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[(j+1)*2][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                    break
                                elif lexeme[((j+1)*2)+1][1] not in literals:
                                    if lexeme[((j+1)*2)+1][1] not in varidents and lexeme[((j+1)*2)+1][0] != '"':
                                        success = 0
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[((j+1)*2)+1][0]} is not declared.')
                                        break
                        
                    #  #FOR VARIABLE ASSIGNMENT USING R AND R WITH MAEK
                    # wala pang ano para sa expression
                    if lexeme[i][0] == 'R':
                        
                        if len(lexeme) == 3:
                            
                            if lexeme[i-1][0] not in varidents:
                                # print('hello', lexeme[i-1][0])
                                success = 0
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i-1][0]} is not a variable identifier.')
                                break
                            if lexeme[i+1][1] not in varAssignment_literals and lexeme[i+1][0] not in varidents:
                                    success = 0
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near  <{lexeme[i][0]}>: \n\t{lexeme[i+1][0]} is not a [Variable identifier | NUMBAR Literal | NUMBR Literal | TROOF Literal | YARN Literal].')
                                    break    
                        elif len(lexeme) == 5:
                            if lexeme[i+1][0] != '"' and lexeme[i+3][0] != '"':

                                if lexeme[i-1][0] not in varidents or varidents[lexeme[i-1][0]] == 'NOOB':
                                    success = 0
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i-1][0]} is not a variable identifier or is an uninitialized variable.')
                                    break
                                if lexeme[i+1][1] not in varAssignment_literals and lexeme[i+1][0] not in varidents:
                                    if lexeme[i+1][0] != 'MAEK':
                                        success = 0
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near  <{lexeme[i][0]}>: \n\t{lexeme[i+1][0]} is not a [MAEK | Variable identifier | NUMBAR Literal | NUMBR Literal | TROOF Literal | YARN Literal].')
                                        break 
                                if lexeme[i+2][0] != lexeme[i-1][0] or varidents[lexeme[i+2][0]] == 'NOOB':
                                    success = 0
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i+2][0]} and {lexeme[i-1][0]} should be same variable when recasting and must be initialized.')
                                    break
                                if lexeme[i+3][1] != 'Type Literal':
                                    success = 0
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i+3][0]} should be a type literal.')
                                    break
                            break
                        elif len(lexeme) <= 2 :
                            success = 0
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tincorrect number of parameters.')
                            break

                        
                    
                    #MAEK TYPECASTING
                    if lexeme[i][0] == 'MAEK':
                        if len(lexeme) >= 6 or len(lexeme) <=2:
                            success = 0
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tincorrect number of parameters.')
                            break
                        else:
                            if lexeme[i+1][0] not in varidents :
                                success = 0
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i+1][0]} should be a variable identifier and must be initialized.')
                                break

                            if lexeme[i-1][0] == 'R' and len(lexeme) == 4:
                                success = 0
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tincorrect number of parameters.')
                                break
                            elif lexeme[i-1][0] == 'R' and len(lexeme) == 5:
                                if lexeme[i-2][0] != lexeme[i+1][0]:
                                    success = 0
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i-2][0]} and {lexeme[i+1][0]} should be same variable for recasting.')
                                    break

                                if lexeme[i+2][1] != 'Type Literal':
                                    success = 0
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i+2][0]} should be a type literal.')
                                    break
                            else:
                                if lexeme[i+2][0] != 'A' and lexeme[i+2][1] != 'Type Literal':
                                    success = 0
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i+2][0]} should be a type literal or an A.')
                                    break
                                elif lexeme[i+2][0] == 'A':
                                    if len(lexeme) == 3:
                                        success = 0
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tincorrect number of parameters.')
                                        break
                                    else:
                                        if lexeme[i+3][1] != 'Type Literal' or len(lexeme) == 3:
                                            success = 0
                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i+2][0]} should be a type literal.')
                                            break

                    #IS NOW A
                    if lexeme[i][0] == 'IS NOW A':
                        # print(lexeme)
                        if len(lexeme) == 3:
                            # print(lexeme[i-1][0])
                            if lexeme[i-1][0] not in varidents or varidents[lexeme[i-1][0]] == 'NOOB':
                                success = 0
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i-1][0]} should be a variable identifier.')
                                break
                            if lexeme[i+1][1] != 'Type Literal':
                                success = 0
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i+1][0]} should be a type literal.')
                                break
                        else:
                            success = 0
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tincorrect number of parameters.')
                            break
                    # #ARITHMETIC OPERATIONS SYNTAX - FOR ALL ARITHMETIC OPERATIONS!
                    if lexeme[i][0] in arithmetic: # 'SUM OF','DIFF OF','PRODUKT OF', 'QUOSHUNT OF', 'MOD OF', 'BIGGR OF', 'SMALLR OF'
                        #arithmetic counter  for indexing
                        an_counter = 0
                        operation_counter = 0
                        arithmetic_index = 0
                        if len(lexeme) < 4:
                            success = 0
                            syntaxResult+= (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\t{lexeme[i][0]} <x> AN <y>')
                            break
                        else:
                            #loop para macater yung more than 1 operations
                            while arithmetic_index < len(lexeme)-1:
                                #this is for hahving another 
                                if lexeme[arithmetic_index][1] == 'Arithmetic Operation':
                                    #mag add lang siya ng indexx?
                                    arithmetic_index += 1
                                    operation_counter += 1
                                # this one if may AN !!
                                elif lexeme[arithmetic_index][1] == "Parameter Delimiter":
                                    #before ng "AN"
                                    if lexeme[arithmetic_index-1][1] != "NUMBR Literal":
                                        if lexeme[arithmetic_index-1][1] != "NUMBAR Literal":
                                            if lexeme[arithmetic_index-1][1] != "String Delimiter":
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[arithmetic_index][0]}>: \n\tIncorrect syntax, see correct syntax. \n\t{lexeme[i][0]} <x> AN <y>')
                                                success = 0
                                                break
                                    #after ng "AN"
                                    if lexeme[arithmetic_index+1][1] != "NUMBR Literal":
                                        if lexeme[arithmetic_index+1][1] != "NUMBAR Literal":
                                            if lexeme[arithmetic_index+1][1] != 'String Delimiter':
                                                if lexeme[arithmetic_index+1][1] != 'Arithmetic Operation':
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[arithmetic_index][0]}>: \n\tIncorrect syntax, see correct syntax. \n\t{lexeme[i][0]} <x> AN <y>')
                                                    success = 0
                                                    break                                    
                                    
                                    arithmetic_index +=1
                                    an_counter += 1
                                #this is for catering the operands!!
                                else:
                                    #proceed to if else ganern!! 
                                    #if lexeme[arithmetic_index]   
                                    if lexeme[arithmetic_index][1] != "NUMBR Literal":
                                        if lexeme[arithmetic_index][1] != "NUMBAR Literal":
                                            if lexeme[arithmetic_index][1] != "String Delimiter":
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[arithmetic_index][0]}>: \n\t{lexeme[i][0]} only accepts NUMBR, NUMBAR, and YARN!')
                                                success = 0
                                                break
                                            #if yarn nga siya
                                            else:
                                                if lexeme[arithmetic_index+1][0].isnumeric() == False:
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[arithmetic_index][0]}>: \n\tYARN is not a NUMBR or NUMBAR!')
                                                    success = 0
                                                    break
                                                if lexeme[arithmetic_index+2][1] != "String Delimiter":
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[arithmetic_index][0]}>: \n\tYARN should start and end with " "')
                                                    success = 0
                                                    break                                                                                                        
                                                arithmetic_index += 3
                                        else:
                                            arithmetic_index +=1
                                    else:
                                        arithmetic_index +=1
                            if an_counter != operation_counter:
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[arithmetic_index][0]}>: \n\tTotal no. of {lexeme[i][0]} should be equal to AN')
                                success = 0
                                break   
                            break
                                
                        
                           
                            


                        
                        
                        
                else:
                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tStatements must be inside HAI and KTHXBYE')
                    success = 0
                    break

                ## PROGRAM BLOCK SYNTAX - KTHXBYE
                if lexeme[i][0] == 'KTHXBYE' and hasHai == 0:
                        hasKthxbye = 0
                        hasHai = 1
                        break
                else:
                    if lexeme[i][0] == 'KTHXBYE' and hasHai == -1 and hasKthxbye == -1:
                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <KTHXBYE>: \n\tKTHXBYE must be declared after HAI')
                        success = 0
                        break
                    elif lexeme[i][0] == 'KTHXBYE' and hasHai == 0 and hasKthxbye == 1:
                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <KTHXBYE>: \n\tAlready has KTHXBYE; it must be declared once')
                        success = 0
                        break
            lexeme.clear()

    if hasHai == 0 and hasKthxbye == -1:
        syntaxResult += (f'\n>> SyntaxError in line {h+1} in <HAI>: \n\tHAI must be enclosed with KTHXBYE')

    if hasWazzup == 0 and hasBuhbye == -1:
        syntaxResult += (f'\n>> SyntaxError in line {h+1} in <WAZZUP>: \n\tWAZZUP must be enclosed with BUHBYE')

    if success == 1:
        syntaxResult += ('>> No syntax errors.')
            
    return syntaxResult