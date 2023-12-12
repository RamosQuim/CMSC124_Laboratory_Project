import keywords

lexemes = keywords.main()
success = 1

str = '''
I HAS A var1
I HAS A var2
I HAS A var3 ITZ 123
I HAS A var4 ITZ
KTHXBYE
'''
# print(str.splitlines())

for h in range(0, len(lexemes.splitlines())):
    lexeme = keywords.lex(lexemes.splitlines()[h])
    print(f"lexeme: {lexeme}\n")
    if ['BTW', 'Comment Identifier'] in lexeme:
        lexeme.pop(lexeme.index(['BTW', 'Comment Identifier'])+1) 
        lexeme.pop(lexeme.index(['BTW', 'Comment Identifier']))

    #----------------SYNTAX FOR VARIABLE DECLARATION
    for i in range(0, len(lexeme)):
        if lexeme[i][0] == 'I HAS A':
            if len(lexeme) < 2 or lexeme[i+1][1] != 'Variable Identifier':
                print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tI HAS A must have a variable identifier')
                success = 0
            elif len(lexeme) > 2:
                if lexeme[i+2][0] != 'ITZ':
                    print(f">> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'ITZ' keyword?")
                    success = 0
                elif len(lexeme) < 4 or lexeme[i+3][1] != 'Literal':
                    print(f'>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\tITZ must have a literal')
                    success = 0
        
        #PRINTING
        if lexeme[i][0] == 'VISIBLE':
            # if less than
            if len(lexeme) < 2:
                print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tVISIBLE must have a Variable Identifier, Literal, or an Expression')
            else:
                #VARIDENT
                if lexeme[i+1][1] != 'String Delimiter':
                    #LITERAL
                    if lexeme[i+1][0].isnumeric() == False:
                        #EXPRESSIONS
                        if lexeme[i+1][1] != 'Arithmetic Keyword' | lexeme[i+1][1] != 'Boolean Keyword' | lexeme[i+1][1] != 'Comparison Keyword':
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\tVISIBLE only accepts Variable Identifier, Literal, and Expression')
                            success = 0
                else:
                    #condition para pag nakalimutan ng quotation sa dulo!
                    if lexeme[i+3][1] != 'String Delimiter':
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i+3][1]}>: \n\tVariable Identifier ')
                        success = 0
        
        #ARITHMETIC SYNTAX - ADD
        # LITERALS PA LANG ANG ACCEPTED, TRY TO FIND A SOLUTION PAG 
        #gawan nalang na arithmetic 
        if lexeme[i][0] == "SUM OF":
            if len(lexeme) < 4:
                print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tSUM OF <x> AN <y>')
            else:
                if lexeme[i+1][0].isnumeric() == False:
                    print(f'>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\tSUM OF only accepts numbr and numbar')
                    success = 0
                    break
                if lexeme[i+2][0] != "AN":
                    print(f'>> SyntaxError in line {h+1} near <{lexeme[i+2][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tSUM OF <x> AN <y>')
                    success = 0
                    break
                if lexeme[i+3][0].isnumeric() == False:
                    print(f'>> SyntaxError in line {h+1} near <{lexeme[i+3][0]}>: \n\tSUM OF only accepts numbr and numbar')
                    success = 0
                    break
                
if success == 1:
    print('>> No syntax errors.')        


'''

        if lexeme[i][0] == 'DIFFRINT':
                if len(lexeme) != 4 and len(lexeme) != 7:
                    print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tDIFFRINT <value> [[AN BIGGR OF|SMALLR OF] <value>] AN <value>')
                    success = 0
                    break
                elif lexeme[i+1][0].isnumeric() == False or lexeme[i+1][0].isnumeric() == False:
                    print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tDIFFRINT only accepts NUMBR or NUMBAR type')
                    success = 0
                    break
                elif len(lexeme) == 4:
                    if lexeme[i+2][0] != 'AN':
                        print(f">> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                        success = 0
                        break
                    elif lexeme[i+3][0].isnumeric() == False or lexeme[i+3][0].isnumeric() == False:
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
                    elif lexeme[i+4][0].isnumeric() == False or lexeme[i+4][0].isnumeric() == False:
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                        success = 0
                        break
                    elif lexeme[i+5][0] != 'AN':
                        print(f">> SyntaxError in line {h+1} near <{lexeme[i+4][0]}>: \n\t{lexeme[i+5][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                        success = 0
                        break
                    elif lexeme[i+6][0].isnumeric() == False or lexeme[i+6][0].isnumeric() == False:
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                        success = 0
                        break
                else:
                    break

        else:
            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\Statements must be inside HAI and KTHXBYE')
            success = 0
            break

        ##BOOLEAN SYNTAX - WON OF
        if lexeme[i][0] == "WON OF":


            if len(lexeme) > 4 or len(lexeme) <= 3:
                success = 0
                print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tBOTH OF [WIN|FAIL] AN [WIN|FAIL]')
                break
            elif len(lexeme) == 4:
                if lexeme[i+1][0] != 'WIN':
                    if lexeme[i+1][0] != 'FAIL':
                        success = 0
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                        break
                elif lexeme[i+1][0] != 'FAIL':
                    if lexeme[i+1][0] != 'WIN':
                        success = 0
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                        break
                
                if lexeme[i+2][0] != 'AN':
                    success = 0
                    print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tThere is a need for AN to indicate "and".')
                    break
            
                if lexeme[i+3][0] != 'WIN':
                    if lexeme[i+3][0] != 'FAIL':
                        success = 0
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                        break
                    break
                elif lexeme[i+3][0] != 'FAIL':
                    if lexeme[i+3][0] != 'WIN':
                        success = 0
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                        break
                    break
                
                    -----------------------------------------------------------
        
        #ARITHMETIC SYNTAX - ADD
        if lexeme[i][0] == "SUM OF":
            
            if len(lexeme) < 4:
                print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tSUM OF <x> AN <y>')
            else:
                #SUM OF 123 AN 123
                if len(lexeme) == 4:

                
                #SUM OF "123" AN 123 or SUM OF 123 AN "123"
                elif len(lexeme) == 6:

                #SUM OF "123" AN "123" 
                elif len(lexeme) == 8:
                if lexeme[i+1][0].isnumeric() == False:
                    if lexeme[i+1][1] != "String Delimiter":
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\tArithmetic Operations only accept numbr, numbar, and implicitly typecast.')
                        success = 0
                
                elif lexeme[i+2][0].isnumeric() != False:
                    if lexeme[i+2][1]  != "":
                    
                    #SUM OF "123" AN 123
                    #SUM OF "123" AN "123"
                    #SUM OF 123 AN 123
                    #SUM OF 123 AN "123"
                

                if lexeme[i+2][0] != 'AN':
                    success = 0
                    print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tThere is a need for AN to indicate "and".')

'''

        