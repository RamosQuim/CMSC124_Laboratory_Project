import keywords
import syntax

modified_varidents = {}

def getVaridents(text):
    semantics(text)
    print(modified_varidents)
    return modified_varidents

def semantics(text):
    semanticsResult = ''
    varidents = syntax.getVaridents(text)
    literals = ['NUMBR Literal', 'NUMBAR Literal', 'YARN Literal', 'TROOF Literal', 'Type Literal']
    
    for h in range(0, len(text.splitlines())):
        lexeme = keywords.lex(text.splitlines()[h].lstrip().rstrip())
        if lexeme is not None:
            if ['BTW', 'Comment Delimiter'] in lexeme:
                lexeme.pop(lexeme.index(['BTW', 'Comment Delimiter'])+1)
                lexeme.pop(lexeme.index(['BTW', 'Comment Delimiter']))
                
            for i in range(0, len(lexeme)):
                if lexeme[i][0] == 'BOTH SAEM' and len(lexeme) == 4:
                    if float(lexeme[i+1][0]) == float(lexeme[i+3][0]):
                        semanticsResult += f'WIN\n'
                    else:
                        semanticsResult += f'FAIL\n'
                elif lexeme[i][0] == 'DIFFRINT' and len(lexeme) == 4:
                    if float(lexeme[i+1][0]) != float(lexeme[i+3][0]):
                        semanticsResult += f'WIN\n'
                    else:
                        semanticsResult += f'FAIL\n'
                elif lexeme[i][0] == 'BOTH SAEM' and len(lexeme) > 4 and lexeme[3][0] == 'SMALLR OF':
                    if float(lexeme[i+1][0]) >= float(lexeme[i+6][0]):
                        semanticsResult += f'WIN\n'
                    else:
                        semanticsResult += f'FAIL\n'
                elif lexeme[i][0] == 'BOTH SAEM' and len(lexeme) >= 4 and lexeme[3][0] == 'BIGGR OF':
                    if float(lexeme[i+1][0]) <= float(lexeme[i+6][0]):
                        semanticsResult += f'WIN\n'
                    else:
                        semanticsResult += f'FAIL\n'
                elif lexeme[i][0] == 'DIFFRINT' and len(lexeme) > 4 and lexeme[3][0] == 'SMALLR OF':
                    if float(lexeme[i+1][0]) > float(lexeme[i+6][0]):
                        semanticsResult += f'WIN\n'
                    else:
                        semanticsResult += f'FAIL\n'
                elif lexeme[i][0] == 'DIFFRINT' and len(lexeme) > 4 and lexeme[3][0] == 'BIGGR OF':
                    if float(lexeme[i+1][0]) < float(lexeme[i+6][0]):
                        semanticsResult += f'WIN\n'
                    else:
                        semanticsResult += f'FAIL\n'
                ##INFINITE ARITY BOOLEAN SYNTAX - ANY OF
                elif lexeme[i][0] == 'ALL OF':
                    boolean_index = 1
                    result = []
                    while boolean_index <= len(lexeme)-2:
                        if lexeme[boolean_index][0] == "BOTH OF":
                            if lexeme[boolean_index+1][1] == 'TROOF Literal' and lexeme[boolean_index+3][1] == 'TROOF Literal':
                                if lexeme[boolean_index+1][0] == 'WIN' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append(f'WIN')
                                elif lexeme[boolean_index+1][0] == 'WIN' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append(f'FAIL')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append(f'FAIL')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append(f'FAIL')
                            elif lexeme[boolean_index+1][1] == 'Identifier' and lexeme[boolean_index+3][1] == 'TROOF Literal':
                                if varidents[lexeme[boolean_index+1][0]] == 'WIN' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append(f'WIN')
                                elif varidents[lexeme[boolean_index+1][0]] == 'WIN' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append(f'FAIL')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append(f'FAIL')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append(f'FAIL')
                            elif lexeme[boolean_index+1][1] == 'TROOF Literal' and lexeme[boolean_index+3][1] == 'Identifier':
                                if lexeme[boolean_index+1][0] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append(f'WIN')
                                elif lexeme[boolean_index+1][0] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append(f'FAIL')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append(f'FAIL')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append(f'FAIL')
                            elif lexeme[boolean_index+1][1] == 'Identifier' and lexeme[boolean_index+3][1] == 'Identifier':
                                if varidents[lexeme[boolean_index+1][0]] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append(f'WIN')
                                elif varidents[lexeme[boolean_index+1][0]] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append(f'FAIL')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append(f'FAIL')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append(f'FAIL')
                            boolean_index += 5
                        elif lexeme[boolean_index][0] == "EITHER OF":
                            if lexeme[boolean_index+1][1] == 'TROOF Literal' and lexeme[boolean_index+3][1] == 'TROOF Literal':
                                if lexeme[boolean_index+1][0] == 'WIN' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append(f'WIN')
                                elif lexeme[boolean_index+1][0] == 'WIN' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append(f'WIN')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append(f'WIN\n')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append(f'FAIL')
                            elif lexeme[boolean_index+1][1] == 'Identifier' and lexeme[boolean_index+3][1] == 'TROOF Literal':
                                if varidents[lexeme[boolean_index+1][0]] == 'WIN' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append(f'WIN')
                                elif varidents[lexeme[boolean_index+1][0]] == 'WIN' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append(f'WIN')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append(f'WIN\n')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append(f'FAIL')
                            elif lexeme[boolean_index+1][1] == 'TROOF Literal' and lexeme[boolean_index+3][1] == 'Identifier':
                                if lexeme[boolean_index+1][0] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append(f'WIN')
                                elif lexeme[boolean_index+1][0] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append(f'WIN')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append(f'WIN\n')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append(f'FAIL')
                            elif lexeme[boolean_index+1][1] == 'Identifier' and lexeme[boolean_index+3][1] == 'Identifier':
                                if varidents[lexeme[boolean_index+1][0]] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append(f'WIN')
                                elif varidents[lexeme[boolean_index+1][0]] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append(f'WIN')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append(f'WIN\n')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append(f'FAIL')
                            boolean_index += 5
                        elif lexeme[boolean_index][0] == "WON OF":
                            if lexeme[boolean_index+1][1] == 'TROOF Literal' and lexeme[boolean_index+3][1] == 'TROOF Literal':
                                if lexeme[boolean_index+1][0] == 'WIN' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append(f'FAIL')
                                elif lexeme[boolean_index+1][0] == 'WIN' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append(f'WIN')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append(f'WIN')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append(f'FAIL')
                            elif lexeme[boolean_index+1][1] == 'Identifier' and lexeme[boolean_index+3][1] == 'TROOF Literal':
                                if varidents[lexeme[boolean_index+1][0]] == 'WIN' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append(f'FAIL')
                                elif varidents[lexeme[boolean_index+1][0]] == 'WIN' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append(f'WIN')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append(f'WIN')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append(f'FAIL')
                            elif lexeme[boolean_index+1][1] == 'TROOF Literal' and lexeme[boolean_index+3][1] == 'Identifier':
                                if lexeme[boolean_index+1][0] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append(f'FAIL')
                                elif lexeme[boolean_index+1][0] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append(f'WIN')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append(f'WIN')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append(f'FAIL')
                            elif lexeme[boolean_index+1][1] == 'Identifier' and lexeme[boolean_index+3][1] == 'Identifier':
                                if varidents[lexeme[boolean_index+1][0]] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append(f'FAIL')
                                elif varidents[lexeme[boolean_index+1][0]] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append(f'WIN')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append(f'WIN')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append(f'FAIL')
                            boolean_index += 5
                        elif lexeme[boolean_index][0] == "NOT":
                            if lexeme[boolean_index+1][1] == 'TROOF Literal':
                                if lexeme[boolean_index+1][0] == 'WIN':
                                    result.append(f'FAIL')
                                elif lexeme[boolean_index+1][0] == 'FAIL':
                                    result.append(f'WIN')
                            else:
                                if varidents[lexeme[boolean_index+1][0]] == 'WIN':
                                    result.append(f'FAIL')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL':
                                    result.append(f'WIN')
                            boolean_index += 3
                        elif lexeme[boolean_index][0] in varidents:
                            result.append(varidents[lexeme[boolean_index][0]])
                            boolean_index += 2
                        elif lexeme[boolean_index][1] in literals:
                            if lexeme[boolean_index][1] == 'TROOF Literal':
                                result.append(lexeme[boolean_index][0])
                            elif f'{int(float(lexeme[boolean_index][0]))}' != '0':
                                result.append('WIN')
                            else:
                                result.append('FAIL')
                            boolean_index += 2
                    if 'FAIL' in result:
                        semanticsResult += f'FAIL\n'
                    else:
                        semanticsResult += f'WIN\n'
                    break
                ##INFINITE ARITY BOOLEAN SYNTAX - ANY OF
                elif lexeme[i][0] == 'ANY OF':
                    boolean_index = 1
                    result = []
                    while boolean_index < len(lexeme)-2:
                        if lexeme[boolean_index][0] == "BOTH OF":
                            if lexeme[boolean_index+1][1] == 'TROOF Literal' and lexeme[boolean_index+3][1] == 'TROOF Literal':
                                if lexeme[boolean_index+1][0] == 'WIN' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append('WIN')
                                elif lexeme[boolean_index+1][0] == 'WIN' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append('FAIL')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append('FAIL')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append('FAIL')
                            elif lexeme[boolean_index+1][1] == 'Identifier' and lexeme[boolean_index+3][1] == 'TROOF Literal':
                                if varidents[lexeme[boolean_index+1][0]] == 'WIN' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append('WIN')
                                elif varidents[lexeme[boolean_index+1][0]] == 'WIN' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append('FAIL')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append('FAIL')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append('FAIL')
                            elif lexeme[boolean_index+1][1] == 'TROOF Literal' and lexeme[boolean_index+3][1] == 'Identifier':
                                if lexeme[boolean_index+1][0] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append('WIN')
                                elif lexeme[boolean_index+1][0] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append('FAIL')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append('FAIL')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append('FAIL')
                            elif lexeme[boolean_index+1][1] == 'Identifier' and lexeme[boolean_index+3][1] == 'Identifier':
                                if varidents[lexeme[boolean_index+1][0]] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append('WIN')
                                elif varidents[lexeme[boolean_index+1][0]] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append('FAIL')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append('FAIL')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append('FAIL')
                            boolean_index += 5
                        elif lexeme[boolean_index][0] == "EITHER OF":
                            if lexeme[boolean_index+1][1] == 'TROOF Literal' and lexeme[boolean_index+3][1] == 'TROOF Literal':
                                if lexeme[boolean_index+1][0] == 'WIN' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append('WIN')
                                elif lexeme[boolean_index+1][0] == 'WIN' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append('WIN')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append('WIN\n')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append('FAIL')
                            elif lexeme[boolean_index+1][1] == 'Identifier' and lexeme[boolean_index+3][1] == 'TROOF Literal':
                                if varidents[lexeme[boolean_index+1][0]] == 'WIN' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append('WIN')
                                elif varidents[lexeme[boolean_index+1][0]] == 'WIN' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append('WIN')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append('WIN\n')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append('FAIL')
                            elif lexeme[boolean_index+1][1] == 'TROOF Literal' and lexeme[boolean_index+3][1] == 'Identifier':
                                if lexeme[boolean_index+1][0] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append('WIN')
                                elif lexeme[boolean_index+1][0] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append('WIN')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append('WIN\n')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append('FAIL')
                            elif lexeme[boolean_index+1][1] == 'Identifier' and lexeme[boolean_index+3][1] == 'Identifier':
                                if varidents[lexeme[boolean_index+1][0]] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append('WIN')
                                elif varidents[lexeme[boolean_index+1][0]] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append('WIN')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append('WIN\n')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append('FAIL')
                            boolean_index += 5
                        elif lexeme[boolean_index][0] == "WON OF":
                            if lexeme[boolean_index+1][1] == 'TROOF Literal' and lexeme[boolean_index+3][1] == 'TROOF Literal':
                                if lexeme[boolean_index+1][0] == 'WIN' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append('WIN')
                                elif lexeme[boolean_index+1][0] == 'WIN' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append('WIN')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append('WIN\n')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append('FAIL')
                            elif lexeme[boolean_index+1][1] == 'Identifier' and lexeme[boolean_index+3][1] == 'TROOF Literal':
                                if varidents[lexeme[boolean_index+1][0]] == 'WIN' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append('WIN')
                                elif varidents[lexeme[boolean_index+1][0]] == 'WIN' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append('WIN')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and lexeme[boolean_index+3][0] == 'WIN':
                                    result.append('WIN\n')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and lexeme[boolean_index+3][0] == 'FAIL':
                                    result.append('FAIL')
                            elif lexeme[boolean_index+1][1] == 'TROOF Literal' and lexeme[boolean_index+3][1] == 'Identifier':
                                if lexeme[boolean_index+1][0] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append('WIN')
                                elif lexeme[boolean_index+1][0] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append('WIN')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append('WIN\n')
                                elif lexeme[boolean_index+1][0] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append('FAIL')
                            elif lexeme[boolean_index+1][1] == 'Identifier' and lexeme[boolean_index+3][1] == 'Identifier':
                                if varidents[lexeme[boolean_index+1][0]] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append('WIN')
                                elif varidents[lexeme[boolean_index+1][0]] == 'WIN' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append('WIN')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'WIN':
                                    result.append('WIN\n')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL' and varidents[lexeme[boolean_index+3][0]] == 'FAIL':
                                    result.append('FAIL')
                            boolean_index += 5
                        elif lexeme[boolean_index][0] == "NOT":
                            if lexeme[boolean_index+1][1] == 'TROOF Literal':
                                if lexeme[boolean_index+1][0] == 'WIN':
                                    result.append('FAIL')
                                elif lexeme[boolean_index+1][0] == 'FAIL':
                                    result.append('WIN')
                            else:
                                if varidents[lexeme[boolean_index+1][0]] == 'WIN':
                                    result.append('FAIL')
                                elif varidents[lexeme[boolean_index+1][0]] == 'FAIL':
                                    result.append('WIN')
                            boolean_index += 3
                        elif lexeme[boolean_index][0] in varidents:
                            result.append(varidents[lexeme[boolean_index][0]])
                            boolean_index += 2
                        elif lexeme[boolean_index][1] in literals:
                            if lexeme[boolean_index][1] == 'TROOF Literal':
                                result.append(lexeme[boolean_index][0])
                            elif f'{int(float(lexeme[boolean_index][0]))}' != '0':
                                result.append('WIN')
                            else:
                                result.append('FAIL')
                            boolean_index += 2
                    if 'WIN' in result:
                        semanticsResult += f'WIN\n'
                    else:
                        semanticsResult += f'FAIL\n'
                    break
                elif lexeme[i][0] == 'BOTH OF' and len(lexeme) == 4:
                    if lexeme[i+1][1] == 'TROOF Literal' and lexeme[i+3][1] == 'TROOF Literal':
                        if lexeme[i+1][0] == 'WIN' and lexeme[i+3][0] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif lexeme[i+1][0] == 'WIN' and lexeme[i+3][0] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                        elif lexeme[i+1][0] == 'FAIL' and lexeme[i+3][0] == 'WIN':
                            semanticsResult += f'FAIL\n'
                        elif lexeme[i+1][0] == 'FAIL' and lexeme[i+3][0] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                    elif lexeme[i+1][1] == 'Identifier' and lexeme[i+3][1] == 'TROOF Literal':
                        if varidents[lexeme[i+1][0]] == 'WIN' and lexeme[i+3][0] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'WIN' and lexeme[i+3][0] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and lexeme[i+3][0] == 'WIN':
                            semanticsResult += f'FAIL\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and lexeme[i+3][0] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                    elif lexeme[i+1][1] == 'TROOF Literal' and lexeme[i+3][1] == 'Identifier':
                        if lexeme[i+1][0] == 'WIN' and varidents[lexeme[i+3][0]] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif lexeme[i+1][0] == 'WIN' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                        elif lexeme[i+1][0] == 'FAIL' and varidents[lexeme[i+3][0]] == 'WIN':
                            semanticsResult += f'FAIL\n'
                        elif lexeme[i+1][0] == 'FAIL' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                    elif lexeme[i+1][1] == 'Identifier' and lexeme[i+3][1] == 'Identifier':
                        if varidents[lexeme[i+1][0]] == 'WIN' and varidents[lexeme[i+3][0]] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'WIN' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and varidents[lexeme[i+3][0]] == 'WIN':
                            semanticsResult += f'FAIL\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                elif lexeme[i][0] == 'EITHER OF' and len(lexeme) == 4:
                    if lexeme[i+1][1] == 'TROOF Literal' and lexeme[i+3][1] == 'TROOF Literal':
                        if lexeme[i+1][0] == 'WIN' and lexeme[i+3][0] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif lexeme[i+1][0] == 'WIN' and lexeme[i+3][0] == 'FAIL':
                            semanticsResult += f'WIN\n'
                        elif lexeme[i+1][0] == 'FAIL' and lexeme[i+3][0] == 'WIN':
                            result.append('WIN\n')
                        elif lexeme[i+1][0] == 'FAIL' and lexeme[i+3][0] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                    elif lexeme[i+1][1] == 'Identifier' and lexeme[i+3][1] == 'TROOF Literal':
                        if varidents[lexeme[i+1][0]] == 'WIN' and lexeme[i+3][0] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'WIN' and lexeme[i+3][0] == 'FAIL':
                            semanticsResult += f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and lexeme[i+3][0] == 'WIN':
                            result.append('WIN\n')
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and lexeme[i+3][0] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                    elif lexeme[i+1][1] == 'TROOF Literal' and lexeme[i+3][1] == 'Identifier':
                        if lexeme[i+1][0] == 'WIN' and varidents[lexeme[i+3][0]] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif lexeme[i+1][0] == 'WIN' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'WIN\n'
                        elif lexeme[i+1][0] == 'FAIL' and varidents[lexeme[i+3][0]] == 'WIN':
                            result.append('WIN\n')
                        elif lexeme[i+1][0] == 'FAIL' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                    elif lexeme[i+1][1] == 'Identifier' and lexeme[i+3][1] == 'Identifier':
                        if varidents[lexeme[i+1][0]] == 'WIN' and varidents[lexeme[i+3][0]] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'WIN' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and varidents[lexeme[i+3][0]] == 'WIN':
                            result.append('WIN\n')
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                elif lexeme[i][0] == 'WON OF' and len(lexeme) == 4:
                    if lexeme[i+1][1] == 'TROOF Literal' and lexeme[i+3][1] == 'TROOF Literal':
                        if lexeme[i+1][0] == 'WIN' and lexeme[i+3][0] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif lexeme[i+1][0] == 'WIN' and lexeme[i+3][0] == 'FAIL':
                            semanticsResult += f'WIN\n'
                        elif lexeme[i+1][0] == 'FAIL' and lexeme[i+3][0] == 'WIN':
                            result.append('WIN\n')
                        elif lexeme[i+1][0] == 'FAIL' and lexeme[i+3][0] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                    elif lexeme[i+1][1] == 'Identifier' and lexeme[i+3][1] == 'TROOF Literal':
                        if varidents[lexeme[i+1][0]] == 'WIN' and lexeme[i+3][0] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'WIN' and lexeme[i+3][0] == 'FAIL':
                            semanticsResult += f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and lexeme[i+3][0] == 'WIN':
                            result.append('WIN\n')
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and lexeme[i+3][0] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                    elif lexeme[i+1][1] == 'TROOF Literal' and lexeme[i+3][1] == 'Identifier':
                        if lexeme[i+1][0] == 'WIN' and varidents[lexeme[i+3][0]] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif lexeme[i+1][0] == 'WIN' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'WIN\n'
                        elif lexeme[i+1][0] == 'FAIL' and varidents[lexeme[i+3][0]] == 'WIN':
                            result.append('WIN\n')
                        elif lexeme[i+1][0] == 'FAIL' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                    elif lexeme[i+1][1] == 'Identifier' and lexeme[i+3][1] == 'Identifier':
                        if varidents[lexeme[i+1][0]] == 'WIN' and varidents[lexeme[i+3][0]] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'WIN' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and varidents[lexeme[i+3][0]] == 'WIN':
                            result.append('WIN\n')
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                elif lexeme[i][0] == 'NOT' and len(lexeme) == 2:
                    if lexeme[i+1][1] == 'TROOF Literal':
                        if lexeme[i+1][0] == 'WIN':
                            semanticsResult += f'FAIL\n'
                        elif lexeme[i+1][0] == 'FAIL':
                            semanticsResult += f'WIN\n'
                    else:
                        if varidents[lexeme[i+1][0]] == 'WIN':
                            semanticsResult += f'FAIL\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL':
                            semanticsResult += f'WIN\n'
                elif lexeme[i][0] == 'R' and len(lexeme) == 3:
                    # if lexeme[i+1][0] :#check type of the value to be assigned to variable
                    for j in varidents:
                        if lexeme[i-1][0] == j:
                            modified_varidents[lexeme[i-1][0]] = lexeme[i+1][0]
                    
                    # varidents[lexeme[i-1][0]] = lexeme[i+1][0]
            lexeme.clear()
    
    return semanticsResult