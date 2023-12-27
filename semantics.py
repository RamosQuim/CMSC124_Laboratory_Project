import keywords
import syntax

def semantics(text):
    semanticsResult = ''
    varidents = syntax.getVaridents(text)
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

                elif lexeme[i][0] == 'BOTH OF' and len(lexeme) == 4:
                    # print(lexeme[i])
                    if lexeme[i+1][0] == 'WIN' and lexeme[i+3][0] == 'WIN':
                        semanticsResult += f'WIN\n'
                    elif lexeme[i+1][0] == 'WIN' and lexeme[i+3][0] == 'FAIL':
                        semanticsResult += f'FAIL\n'
                    elif lexeme[i+1][0] == 'FAIL' and lexeme[i+3][0] == 'WIN':
                        semanticsResult += f'FAIL\n'
                    elif lexeme[i+1][0] == 'FAIL' and lexeme[i+3][0] == 'FAIL':
                        semanticsResult += f'FAIL\n'
                    else:
                        semanticsResult += f'FAIL\n'
                elif lexeme[i][0] == 'EITHER OF' and len(lexeme) == 4:
                    # print(lexeme[i])
                    if lexeme[i+1][0] == 'WIN' and lexeme[i+3][0] == 'WIN':
                        semanticsResult += f'WIN\n'
                    elif lexeme[i+1][0] == 'WIN' and lexeme[i+3][0] == 'FAIL':
                        semanticsResult += f'WIN\n'
                    elif lexeme[i+1][0] == 'FAIL' and lexeme[i+3][0] == 'WIN':
                        semanticsResult += f'WIN\n'
                    elif lexeme[i+1][0] == 'FAIL' and lexeme[i+3][0] == 'FAIL':
                        semanticsResult += f'FAIL\n'
                    else:
                        semanticsResult += f'FAIL\n'
                elif lexeme[i][0] == 'WON OF' and len(lexeme) == 4:
                    # print(lexeme[i])
                    if lexeme[i+1][0] == 'WIN' and lexeme[i+3][0] == 'WIN':
                        semanticsResult += f'FAIL\n'
                    elif lexeme[i+1][0] == 'WIN' and lexeme[i+3][0] == 'FAIL':
                        semanticsResult += f'WIN\n'
                    elif lexeme[i+1][0] == 'FAIL' and lexeme[i+3][0] == 'WIN':
                        semanticsResult += f'WIN\n'
                    elif lexeme[i+1][0] == 'FAIL' and lexeme[i+3][0] == 'FAIL':
                        semanticsResult += f'FAIL\n'
                    else:
                        semanticsResult += f'FAIL\n'
                elif lexeme[i][0] == 'NOT' and len(lexeme) == 2:
                    # print(lexeme[i])
                    if lexeme[i+1][0] == 'WIN':
                        semanticsResult += f'FAIL\n'
                    elif lexeme[i+1][0] == 'FAIL':
                        semanticsResult += f'WIN\n'
                    else:
                        semanticsResult += f'FAIL\n'
            lexeme.clear()
    
    return semanticsResult