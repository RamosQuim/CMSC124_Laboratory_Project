import keywords

def semantics(text):
    semanticsResult = ''
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
            lexeme.clear()
    
    return semanticsResult