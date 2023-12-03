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
            if len(lexeme) < 2:
                print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tVISIBLE must have a Variable Identifier, Literal, or an Expression')
            else:
                if lexeme[i+1][1] != 'String Delimiter':
                    if lexeme[i+1][1] != 'Literal':
                        if lexeme[i+1][1] != 'Arithmetic Keyword' | lexeme[i+1][1] != 'Boolean Keyword' | lexeme[i+1][1] != 'Comparison Keyword':
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\tVISIBLE only accepts Variable Identifier, Literal, and Expression')
                            success = 0
                else:
                    #condition para pag nakalimutan ng quotation sa dulo!
                    if lexeme[i+3][1] != 'String Delimiter':
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i+3][1]}>: \n\tVariable Identifier ')
                        success = 0
        
        #FFOR LOOP OPERATORS (UPPIN_YR varident | NERFIN_YR varident)
        #if lexeme[i][1] == 'Loop Operator':
        #    if lexeme[i+1][1] != '':
        #        print('uwu')

if success == 1:
    print('>> No syntax errors.')
        