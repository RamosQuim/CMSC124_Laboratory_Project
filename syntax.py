import keywords

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

lexemes = keywords.main()
success = 1

comparison = ['BOTH SAEM', 'DIFFRINT']
literals = ['NUMBR Literal', 'NUMBAR Literal', 'YARN Literal', 'TROOF Literal', 'Type Literal']
booleans = ['BOTH OF', 'EITHER OF', 'WON OF', 'NOT']
varidents = []
hasHai = -1
hasKthxbye = -1
hasWazzup = -1
hasBuhbye = -1
hasVarDec = 0
lines = lexemes.splitlines()

for h in range(0, len(lines)):
    lexeme = keywords.lex(lexemes.splitlines()[h].lstrip().rstrip())
    if lexeme is not None:
        if ['BTW', 'Comment Delimiter'] in lexeme:
            lexeme.pop(lexeme.index(['BTW', 'Comment Delimiter'])+1)
            lexeme.pop(lexeme.index(['BTW', 'Comment Delimiter']))
            
        for i in range(0, len(lexeme)):
            ## PROGRAM BLOCK SYNTAX - HAI
            if lexeme[i][0] == 'HAI' and hasHai == -1 and hasKthxbye == -1:
                hasHai = 0
                break
            else:
                    if lexeme[i][0] == 'HAI' and hasHai > -1:
                        print(f'>> SyntaxError in line {h+1} near <HAI>: \n\tAlready has HAI; it must be declared once')
                        success = 0
                        break
                    elif lexeme[i][0] == 'HAI' and hasKthxbye > -1:
                        print(f'>> SyntaxError in line {h+1} near <HAI>: \n\HAI must be declared before KTHXBYE')
                        success = 0
                        break
            if hasHai == 0:
                ## VARIABLE BLOCK SYNTAX - WAZZUP
                if lexeme[i][0] == 'WAZZUP' and hasWazzup == -1 and hasBuhbye == -1:
                    hasWazzup = 0
                    break
                else:
                    if lexeme[i][0] == 'WAZZUP' and hasWazzup > -1:
                        print(f'>> SyntaxError in line {h+1} near <WAZZUP>: \n\tAlready has WAZZUP; it must be declared once')
                        success = 0
                        break
                    elif lexeme[i][0] == 'WAZZUP' and hasBuhbye > -1:
                        print(f'>> SyntaxError in line {h+1} near <WAZZUP>: \n\tWAZZUP must be declared before BUHBYE')
                        success = 0
                        break
                ## VARIABLE DECLARATION SYNTAX
                if lexeme[i][0] == 'I HAS A' and hasWazzup == 0:
                    if len(lexeme) < 2 or lexeme[i+1][1] != 'Variable Identifier':
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tI HAS A must have a variable identifier')
                        success = 0
                        break
                    elif len(lexeme) > 2:
                        if lexeme[i+2][0] != 'ITZ':
                            print(f">> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'ITZ' keyword?")
                            success = 0
                            break
                        elif len(lexeme) < 4 or (lexeme[i+3][1] != 'Literal' and lexeme[i+3][1] != 'Variable Identifier'):
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\tITZ must have a literal or variable identifier')
                            success = 0
                            break
                    hasVarDec = 1
                    varidents.append(lexeme[i][0])
                    break
                else:
                    if lexeme[i][0] != 'I HAS A' and lexeme[i][0] != 'BUHBYE' and lexeme[i][0] != 'KTHXBYE' and hasWazzup == 0 and hasBuhbye == -1: 
                        print(f'>> SyntaxError in line {h+1} in <WAZZUP> block: \n\tonly I HAS A statements can be inside WAZZUP and BUHBYE')
                        success = 0
                        break
                    elif lexeme[i][0] == 'I HAS A':
                        print(f'>> SyntaxError in line {h+1} near <I HAS A>: \n\tI HAS A statements must be inside WAZZUP and BUHBYE')
                        success = 0
                        break
                ## VARIABLE BLOCK SYNTAX - BUHBYE
                if lexeme[i][0] == 'BUHBYE' and hasWazzup == 0:
                    hasBuhbye = 0
                    hasWazzup = 1
                    break
                else:
                    if lexeme[i][0] == 'BUHBYE' and hasWazzup == -1 and hasBuhbye == -1:
                        print(f'>> SyntaxError in line {h+1} near <BUHBYE>: \n\tBUHBYE must be declared after WAZZUP')
                        success = 0
                        break
                    elif lexeme[i][0] == 'BUHBYE' and hasWazzup == 0 and hasBuhbye == 1:
                        print(f'>> SyntaxError in line {h+1} near <BUHBYE>: \n\tAlready has BUHBYE; it must be declared once')
                        success = 0
                        break
                
                ## COMPARISON SYNTAX - BOTH SAEM
                if lexeme[i][0] == 'BOTH SAEM':
                    print(isfloat(lexeme[i+1][0]))
                    if len(lexeme) != 4 and len(lexeme) != 7:
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tBOTH SAEM <value> [[AN BIGGR OF|SMALLR OF] <value>] AN <value>')
                        success = 0
                        break
                    elif isfloat(lexeme[i+1][0]) == False:
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tBOTH SAEM only accepts NUMBR or NUMBAR type')
                        success = 0
                        break
                    elif len(lexeme) == 4:
                        if lexeme[i+2][0] != 'AN':
                            print(f">> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                            success = 0
                            break
                        elif isfloat(lexeme[i+3][0]) == False:
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tBOTH SAEM only accepts NUMBR or NUMBAR type')
                            success = 0
                            break
                    elif len(lexeme) == 7:
                        if lexeme[i+2][0] != 'AN':
                            print(f">> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                            success = 0
                            break
                        elif lexeme[i+3][0] != 'SMALLR OF' and lexeme[i+3][0] != 'BIGGR OF':
                            print(f">> SyntaxError in line {h+1} near <{lexeme[i+2][0]}>: \n\t{lexeme[i+3][0]} is recognized incorrectly. Perhaps you need a 'SMALLR OF' or 'BIGGR OF' keyword?")
                            success = 0
                            break
                        elif isfloat(lexeme[i+4][0]) == False:
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                            success = 0
                            break
                        elif lexeme[i+5][0] != 'AN':
                            print(f">> SyntaxError in line {h+1} near <{lexeme[i+4][0]}>: \n\t{lexeme[i+5][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                            success = 0
                            break
                        elif isfloat(lexeme[i+6][0]) == False:
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                            success = 0
                            break
                    else:
                        break
                ## COMPARISON SYNTAX - DIFFRINT
                if lexeme[i][0] == 'DIFFRINT':
                    if len(lexeme) != 4 and len(lexeme) != 7:
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tDIFFRINT <value> [[AN BIGGR OF|SMALLR OF] <value>] AN <value>')
                        success = 0
                        break
                    elif isfloat(lexeme[i+1][0]) == False or isfloat(lexeme[i+1][0]) == False:
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tDIFFRINT only accepts NUMBR or NUMBAR type')
                        success = 0
                        break
                    elif len(lexeme) == 4:
                        if lexeme[i+2][0] != 'AN':
                            print(f">> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                            success = 0
                            break
                        elif isfloat(lexeme[i+3][0]) == False or isfloat(lexeme[i+3][0]) == False:
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tDIFFRINT only accepts NUMBR or NUMBAR type')
                            success = 0
                            break
                    elif len(lexeme) == 7:
                        if lexeme[i+2][0] != 'AN':
                            print(f">> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                            success = 0
                            break
                        elif lexeme[i+3][0] != 'SMALLR OF' and lexeme[i+3][0] != 'BIGGR OF':
                            print(f">> SyntaxError in line {h+1} near <{lexeme[i+2][0]}>: \n\t{lexeme[i+3][0]} is recognized incorrectly. Perhaps you need a 'SMALLR OF' or 'BIGGR OF' keyword?")
                            success = 0
                            break
                        elif isfloat(lexeme[i+4][0]) == False or isfloat(lexeme[i+4][0]) == False:
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                            success = 0
                            break
                        elif lexeme[i+5][0] != 'AN':
                            print(f">> SyntaxError in line {h+1} near <{lexeme[i+4][0]}>: \n\t{lexeme[i+5][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                            success = 0
                            break
                        elif isfloat(lexeme[i+6][0]) == False or isfloat(lexeme[i+6][0]) == False:
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                            success = 0
                            break
                    else:
                        break
                # ##BOOLEAN SYNTAX - BOTH OF
                # if lexeme[i][0] == "BOTH OF":
                #     if len(lexeme) > 4 or len(lexeme) <= 3:
                #         success = 0
                #         print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tBOTH OF [WIN|FAIL] AN [WIN|FAIL]')
                #         break
                #     elif len(lexeme) == 4:
                #         if lexeme[i+1][0] != 'WIN':
                #             if lexeme[i+1][0] != 'FAIL':
                #                 success = 0
                #                 print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                #                 break
                #         elif lexeme[i+1][0] != 'FAIL':
                #             if lexeme[i+1][0] != 'WIN':
                #                 success = 0
                #                 print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                #                 break
                        
                #         if lexeme[i+2][0] != 'AN':
                #             success = 0
                #             print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tThere is a need for AN to indicate "and".')
                #             break
                    
                #         if lexeme[i+3][0] != 'WIN':
                #             if lexeme[i+3][0] != 'FAIL':
                #                 success = 0
                #                 print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                #                 break
                #             break
                #         elif lexeme[i+3][0] != 'FAIL':
                #             if lexeme[i+3][0] != 'WIN':
                #                 success = 0
                #                 print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                #                 break
                #             break
                ##BOOLEAN SYNTAX - EITHER OF
                # if lexeme[i][0] == "EITHER OF":
                #     if len(lexeme) > 4 or len(lexeme) <= 3:
                #         success = 0
                #         print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tBOTH OF [WIN|FAIL] AN [WIN|FAIL]')
                #         break
                #     elif len(lexeme) == 4:
                #         if lexeme[i+1][0] != 'WIN':
                #             if lexeme[i+1][0] != 'FAIL':
                #                 success = 0
                #                 print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                #                 break
                #         elif lexeme[i+1][0] != 'FAIL':
                #             if lexeme[i+1][0] != 'WIN':
                #                 success = 0
                #                 print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                #                 break
                        
                #         if lexeme[i+2][0] != 'AN':
                #             success = 0
                #             print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tThere is a need for AN to indicate "and".')
                #             break
                    
                #         if lexeme[i+3][0] != 'WIN':
                #             if lexeme[i+3][0] != 'FAIL':
                #                 success = 0
                #                 print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                #                 break
                #             break
                #         elif lexeme[i+3][0] != 'FAIL':
                #             if lexeme[i+3][0] != 'WIN':
                #                 success = 0
                #                 print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                #                 break
                #             break
                
                # ##BOOLEAN SYNTAX - WON OF
                # if lexeme[i][0] == "WON OF":
                #     if len(lexeme) > 4 or len(lexeme) <= 3:
                #         success = 0
                #         print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tBOTH OF [WIN|FAIL] AN [WIN|FAIL]')
                #         break
                #     elif len(lexeme) == 4:
                #         if lexeme[i+1][0] != 'WIN':
                #             if lexeme[i+1][0] != 'FAIL':
                #                 success = 0
                #                 print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                #                 break
                #         elif lexeme[i+1][0] != 'FAIL':
                #             if lexeme[i+1][0] != 'WIN':
                #                 success = 0
                #                 print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                #                 break
                        
                #         if lexeme[i+2][0] != 'AN':
                #             success = 0
                #             print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tThere is a need for AN to indicate "and".')
                #             break
                    
                #         if lexeme[i+3][0] != 'WIN':
                #             if lexeme[i+3][0] != 'FAIL':
                #                 success = 0
                #                 print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                #                 break
                #             break
                #         elif lexeme[i+3][0] != 'FAIL':
                #             if lexeme[i+3][0] != 'WIN':
                #                 success = 0
                #                 print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                #                 break
                #             break
                
                # ##BOOLEAN SYNTAX - NOT
                # if lexeme[i][0] == "NOT":
                #     if len(lexeme) > 3 or len(lexeme) < 2: 
                #         success = 0
                #         print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tNOT [WIN|FAIL]')
                #         break
                #     elif len(lexeme) == 2:
                #         if lexeme[i+1][0] != 'WIN':
                #             if lexeme[i+1][0] != 'FAIL':
                #                 success = 0
                #                 print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                #                 break
                #         elif lexeme[i+1][0] != 'FAIL':
                #             if lexeme[i+1][0] != 'WIN':
                #                 success = 0
                #                 print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                #                 break

                ##INFINITE ARITY BOOLEAN SYNTAX - ALL OF
                if lexeme[i][0] == 'ALL OF':
                    boolean_index = 1
                    if len(lexeme) <= 5:
                        success = 0
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tALL OF <finite_bool_expr> AN <finite_bool_expr> [[AN <finite_bool_expr>...] MKAY')
                        break
                    while boolean_index < len(lexeme)-2:
                        if lexeme[boolean_index][0] not in booleans:
                            success = 0
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index][0]} is not a finite boolean keyword.')
                            break
                        else:
                            ##BOOLEAN SYNTAX - BOTH OF
                            if boolean_index+3 >= len(lexeme):
                                success = 0
                                if lexeme[boolean_index][0] != 'NOT':
                                    print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\t{lexeme[boolean_index][0]} [WIN|FAIL] AN [WIN|FAIL]')
                                else:
                                    print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\t{lexeme[boolean_index][0]} [WIN|FAIL]')
                                break
                            else:
                                if lexeme[boolean_index][0] == "BOTH OF":
                                    if lexeme[boolean_index+1][0] != 'WIN':
                                        if lexeme[boolean_index+1][0] != 'FAIL':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                                            break
                                    elif lexeme[boolean_index+1][0] != 'FAIL':
                                        if lexeme[boolean_index+1][0] != 'WIN':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                                            break
                                    if lexeme[boolean_index+2][0] != 'AN':
                                        success = 0
                                        print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tThere is a need for AN to indicate "and".')
                                        break
                                
                                    if lexeme[boolean_index+3][0] != 'WIN':
                                        if lexeme[boolean_index+3][0] != 'FAIL':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                                            break
                                    elif lexeme[boolean_index+3][0] != 'FAIL':
                                        if lexeme[boolean_index+3][0] != 'WIN':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                                            break
                                    if ((boolean_index+4) < len(lexeme)):
                                        if lexeme[boolean_index+4][0] != 'AN' and (lexeme[boolean_index+4][0] != 'MKAY' and boolean_index+4 != len(lexeme)-1):
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+4][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                            break
                                    boolean_index += 5
                                elif lexeme[boolean_index][0] == "EITHER OF":
                                    if lexeme[boolean_index+1][0] != 'WIN':
                                        if lexeme[boolean_index+1][0] != 'FAIL':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of EITHER OF must be either WIN OR FAIL.')
                                            break
                                    elif lexeme[boolean_index+1][0] != 'FAIL':
                                        if lexeme[boolean_index+1][0] != 'WIN':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of EITHER OF must be either WIN OR FAIL.')
                                            break
                                    if lexeme[boolean_index+2][0] != 'AN':
                                        success = 0
                                        print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tThere is a need for AN to indicate "and".')
                                        break
                                
                                    if lexeme[boolean_index+3][0] != 'WIN':
                                        if lexeme[boolean_index+3][0] != 'FAIL':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of EITHER OF must be either WIN OR FAIL.')
                                            break
                                    elif lexeme[boolean_index+3][0] != 'FAIL':
                                        if lexeme[boolean_index+3][0] != 'WIN':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of EITHER OF must be either WIN OR FAIL.')
                                            break
                                    if ((boolean_index+4) < len(lexeme)):
                                        if lexeme[boolean_index+4][0] != 'AN' and (lexeme[boolean_index+4][0] != 'MKAY' and boolean_index+4 != len(lexeme)-1):
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+4][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                            break
                                    boolean_index += 5
                                elif lexeme[boolean_index][0] == "WON OF":
                                    if lexeme[boolean_index+1][0] != 'WIN':
                                        if lexeme[boolean_index+1][0] != 'FAIL':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of WON OF must be either WIN OR FAIL.')
                                            break
                                    elif lexeme[boolean_index+1][0] != 'FAIL':
                                        if lexeme[boolean_index+1][0] != 'WIN':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of WON OF must be either WIN OR FAIL.')
                                            break
                                    if lexeme[boolean_index+2][0] != 'AN':
                                        success = 0
                                        print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tThere is a need for AN to indicate "and".')
                                        break
                                
                                    if lexeme[boolean_index+3][0] != 'WIN':
                                        if lexeme[boolean_index+3][0] != 'FAIL':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of WON OF must be either WIN OR FAIL.')
                                            break
                                    elif lexeme[boolean_index+3][0] != 'FAIL':
                                        if lexeme[boolean_index+3][0] != 'WIN':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of WON OF must be either WIN OR FAIL.')
                                            break
                                    if ((boolean_index+4) < len(lexeme)) and (lexeme[boolean_index+4][0] != 'MKAY' and boolean_index+4 != len(lexeme)-1):
                                        if lexeme[boolean_index+4][0] != 'AN':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+4][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                            break
                                    boolean_index += 5
                                elif lexeme[boolean_index][0] == "NOT":
                                    if lexeme[boolean_index+1][0] != 'WIN':
                                        if lexeme[boolean_index+1][0] != 'FAIL':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of NOT must be either WIN OR FAIL.')
                                            break
                                    elif lexeme[boolean_index+1][0] != 'FAIL':
                                        if lexeme[boolean_index+1][0] != 'WIN':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of NOT must be either WIN OR FAIL.')
                                            break
                                    if ((boolean_index+2) < len(lexeme)):
                                        if lexeme[boolean_index+2][0] != 'AN' and (lexeme[boolean_index+2][0] != 'MKAY' and boolean_index+2 != len(lexeme)-1):
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+2][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                            break
                                    boolean_index += 3
                    else:
                        if lexeme[len(lexeme)-1][0] != 'MKAY':
                            success = 0
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tMKAY must be the end, see correct syntax. \n\tALL OF <finite_bool_expr> AN <finite_bool_expr> [[AN <finite_bool_expr>...] MKAY')
                            break
                    break

                ##INFINITE ARITY BOOLEAN SYNTAX - ANY OF
                if lexeme[i][0] == 'ANY OF':
                    boolean_index = 1
                    if len(lexeme) <= 5:
                        success = 0
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tANY OF <finite_bool_expr> AN <finite_bool_expr> [[AN <finite_bool_expr>...] MKAY')
                        break
                    while boolean_index < len(lexeme)-2:
                        if lexeme[boolean_index][0] not in booleans:
                            success = 0
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index][0]} is not a finite boolean keyword.')
                            break
                        else:
                            ##BOOLEAN SYNTAX - BOTH OF
                            if boolean_index+3 >= len(lexeme):
                                success = 0
                                if lexeme[boolean_index][0] != 'NOT':
                                    print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\t{lexeme[boolean_index][0]} [WIN|FAIL] AN [WIN|FAIL]')
                                else:
                                    print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\t{lexeme[boolean_index][0]} [WIN|FAIL]')
                                break
                            else:
                                if lexeme[boolean_index][0] == "BOTH OF":
                                    if lexeme[boolean_index+1][0] != 'WIN':
                                        if lexeme[boolean_index+1][0] != 'FAIL':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                                            break
                                    elif lexeme[boolean_index+1][0] != 'FAIL':
                                        if lexeme[boolean_index+1][0] != 'WIN':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                                            break
                                    if lexeme[boolean_index+2][0] != 'AN':
                                        success = 0
                                        print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tThere is a need for AN to indicate "and".')
                                        break
                                
                                    if lexeme[boolean_index+3][0] != 'WIN':
                                        if lexeme[boolean_index+3][0] != 'FAIL':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                                            break
                                    elif lexeme[boolean_index+3][0] != 'FAIL':
                                        if lexeme[boolean_index+3][0] != 'WIN':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                                            break
                                    if ((boolean_index+4) < len(lexeme)):
                                        if lexeme[boolean_index+4][0] != 'AN' and (lexeme[boolean_index+4][0] != 'MKAY' and boolean_index+4 != len(lexeme)-1):
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+4][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                            break
                                    boolean_index += 5
                                elif lexeme[boolean_index][0] == "EITHER OF":
                                    if lexeme[boolean_index+1][0] != 'WIN':
                                        if lexeme[boolean_index+1][0] != 'FAIL':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of EITHER OF must be either WIN OR FAIL.')
                                            break
                                    elif lexeme[boolean_index+1][0] != 'FAIL':
                                        if lexeme[boolean_index+1][0] != 'WIN':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of EITHER OF must be either WIN OR FAIL.')
                                            break
                                    if lexeme[boolean_index+2][0] != 'AN':
                                        success = 0
                                        print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tThere is a need for AN to indicate "and".')
                                        break
                                
                                    if lexeme[boolean_index+3][0] != 'WIN':
                                        if lexeme[boolean_index+3][0] != 'FAIL':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of EITHER OF must be either WIN OR FAIL.')
                                            break
                                    elif lexeme[boolean_index+3][0] != 'FAIL':
                                        if lexeme[boolean_index+3][0] != 'WIN':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of EITHER OF must be either WIN OR FAIL.')
                                            break
                                    if ((boolean_index+4) < len(lexeme)):
                                        if lexeme[boolean_index+4][0] != 'AN' and (lexeme[boolean_index+4][0] != 'MKAY' and boolean_index+4 != len(lexeme)-1):
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+4][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                            break
                                    boolean_index += 5
                                elif lexeme[boolean_index][0] == "WON OF":
                                    if lexeme[boolean_index+1][0] != 'WIN':
                                        if lexeme[boolean_index+1][0] != 'FAIL':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of WON OF must be either WIN OR FAIL.')
                                            break
                                    elif lexeme[boolean_index+1][0] != 'FAIL':
                                        if lexeme[boolean_index+1][0] != 'WIN':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of WON OF must be either WIN OR FAIL.')
                                            break
                                    if lexeme[boolean_index+2][0] != 'AN':
                                        success = 0
                                        print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tThere is a need for AN to indicate "and".')
                                        break
                                
                                    if lexeme[boolean_index+3][0] != 'WIN':
                                        if lexeme[boolean_index+3][0] != 'FAIL':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of WON OF must be either WIN OR FAIL.')
                                            break
                                    elif lexeme[boolean_index+3][0] != 'FAIL':
                                        if lexeme[boolean_index+3][0] != 'WIN':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of WON OF must be either WIN OR FAIL.')
                                            break
                                    if ((boolean_index+4) < len(lexeme)) and (lexeme[boolean_index+4][0] != 'MKAY' and boolean_index+4 != len(lexeme)-1):
                                        if lexeme[boolean_index+4][0] != 'AN':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+4][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                            break
                                    boolean_index += 5
                                elif lexeme[boolean_index][0] == "NOT":
                                    if lexeme[boolean_index+1][0] != 'WIN':
                                        if lexeme[boolean_index+1][0] != 'FAIL':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of NOT must be either WIN OR FAIL.')
                                            break
                                    elif lexeme[boolean_index+1][0] != 'FAIL':
                                        if lexeme[boolean_index+1][0] != 'WIN':
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of NOT must be either WIN OR FAIL.')
                                            break
                                    if ((boolean_index+2) < len(lexeme)):
                                        if lexeme[boolean_index+2][0] != 'AN' and (lexeme[boolean_index+2][0] != 'MKAY' and boolean_index+2 != len(lexeme)-1):
                                            success = 0
                                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+2][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                            break
                                    boolean_index += 3
                    else:
                        if lexeme[len(lexeme)-1][0] != 'MKAY':
                            success = 0
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tMKAY must be the end, see correct syntax. \n\tANY OF <finite_bool_expr> AN <finite_bool_expr> [[AN <finite_bool_expr>...] MKAY')
                            break
                    break

                ## CONCATENATION BLOCK SYNTAX - SMOOSH
                if lexeme[i][0] == 'SMOOSH':
                    if len(lexeme) <= 2 or len(lexeme)%2 == 1:
                        success = 0
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tSMOOSH <value> AN <value> [[AN <value>]...]')
                        break
                    elif lexeme[i+1][1] not in literals:
                        if lexeme[i+1][1] not in varidents and lexeme[i+1][0] != '"':
                            success = 0
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i+1][0]} is not declared.')
                            break
                    else:
                        for j in range(0, int((len(lexeme)-2)/2)):
                            if lexeme[(j+1)*2][0] != 'AN':
                                success = 0
                                print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[(j+1)*2][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                break
                            elif lexeme[((j+1)*2)+1][1] not in literals:
                                if lexeme[((j+1)*2)+1][1] not in varidents and lexeme[((j+1)*2)+1][0] != '"':
                                    success = 0
                                    print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[((j+1)*2)+1][0]} is not declared.')
                                    break

            else:
                print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tStatements must be inside HAI and KTHXBYE')
                success = 0
                break

            ## PROGRAM BLOCK SYNTAX - KTHXBYE
            if lexeme[i][0] == 'KTHXBYE' and hasHai == 0:
                    hasKthxbye = 0
                    hasHai = 1
                    break
            else:
                if lexeme[i][0] == 'KTHXBYE' and hasHai == -1 and hasKthxbye == -1:
                    print(f'>> SyntaxError in line {h+1} near <KTHXBYE>: \n\tKTHXBYE must be declared after HAI')
                    success = 0
                    break
                elif lexeme[i][0] == 'KTHXBYE' and hasHai == 0 and hasKthxbye == 1:
                    print(f'>> SyntaxError in line {h+1} near <KTHXBYE>: \n\tAlready has KTHXBYE; it must be declared once')
                    success = 0
                    break
        lexeme.clear()

if hasHai == 0 and hasKthxbye == -1:
    print(f'>> SyntaxError in line {h+1} in <HAI>: \n\tHAI must be enclosed with KTHXBYE')

if hasWazzup == 0 and hasBuhbye == -1:
    print(f'>> SyntaxError in line {h+1} in <WAZZUP>: \n\tWAZZUP must be enclosed with BUHBYE')

if success == 1:
    print('>> No syntax errors.')
        
