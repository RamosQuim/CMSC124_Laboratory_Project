import keywords
import syntax

modified_varidents = {}
explicit_typecast = []
varidents = {}

def getExplicitTypecast(text):
    semantics(text)
    return explicit_typecast

def getVaridents(text):
    semantics(text)
    # print(modified_varidents, "semantics")
    return modified_varidents

def semantics(text):
    semanticsResult = ''
    global varidents
    global explicit_typecast
    explicit_typecast.clear()
    modified_varidents.clear()
    varidents = syntax.getVaridents(text)
    literals = ['NUMBR Literal', 'NUMBAR Literal', 'YARN Literal', 'TROOF Literal', 'Type Literal']
    # print(varidents)
    
    for h in range(0, len(text.splitlines())):
        lexeme = keywords.lex(text.splitlines()[h].lstrip().rstrip())
        if lexeme is not None:
            if ['BTW', 'Comment Delimiter'] in lexeme:
                lexeme.pop(lexeme.index(['BTW', 'Comment Delimiter'])+1)
                lexeme.pop(lexeme.index(['BTW', 'Comment Delimiter']))
                
            for i in range(0, len(lexeme)):
                # if lexeme[i][0] == 'BOTH SAEM' and len(lexeme) == 4:
                #     if float(lexeme[i+1][0]) == float(lexeme[i+3][0]):
                #         semanticsResult += f'WIN\n'
                #     else:
                #         semanticsResult += f'FAIL\n'
                # elif lexeme[i][0] == 'DIFFRINT' and len(lexeme) == 4:
                #     if float(lexeme[i+1][0]) != float(lexeme[i+3][0]):
                #         semanticsResult += f'WIN\n'
                #     else:
                #         semanticsResult += f'FAIL\n'
                # elif lexeme[i][0] == 'BOTH SAEM' and len(lexeme) > 4 and lexeme[3][0] == 'SMALLR OF':
                #     if float(lexeme[i+1][0]) >= float(lexeme[i+6][0]):
                #         semanticsResult += f'WIN\n'
                #     else:
                #         semanticsResult += f'FAIL\n'
                # elif lexeme[i][0] == 'BOTH SAEM' and len(lexeme) >= 4 and lexeme[3][0] == 'BIGGR OF':
                #     if float(lexeme[i+1][0]) <= float(lexeme[i+6][0]):
                #         semanticsResult += f'WIN\n'
                #     else:
                #         semanticsResult += f'FAIL\n'
                # elif lexeme[i][0] == 'DIFFRINT' and len(lexeme) > 4 and lexeme[3][0] == 'SMALLR OF':
                #     if float(lexeme[i+1][0]) > float(lexeme[i+6][0]):
                #         semanticsResult += f'WIN\n'
                #     else:
                #         semanticsResult += f'FAIL\n'
                # elif lexeme[i][0] == 'DIFFRINT' and len(lexeme) > 4 and lexeme[3][0] == 'BIGGR OF':
                #     if float(lexeme[i+1][0]) < float(lexeme[i+6][0]):
                #         semanticsResult += f'WIN\n'
                #     else:
                #         semanticsResult += f'FAIL\n'

                #-- BOTH SAEM AND DIFFRINT WITH VARIDENTS
                if lexeme[i][0] == 'BOTH SAEM' and len(lexeme) == 4:
                    one = convertFloat(lexeme[i+1][0])
                    three = convertFloat(lexeme[i+3][0])
                    if one == True and three == True:
                        if float(lexeme[i+1][0]) == float(lexeme[i+3][0]):
                            semanticsResult += f'WIN\n'
                        else:
                            semanticsResult += f'FAIL\n'
                    elif one == False and three == True:
                        value = ""
                        for j in varidents:
                            if j == lexeme[i+1][0]:
                                value = varidents[j]
                        if convertFloat(value) == True:
                            if float(value) == float(lexeme[i+3][0]):
                                semanticsResult += f'WIN\n'
                            else:
                                semanticsResult += f'FAIL\n'
                    elif one == True and three == False:
                        value = ""
                        for j in varidents:
                            if j == lexeme[i+3][0]:
                                value = varidents[j]
                        if convertFloat(value) == True:
                            if float(lexeme[i+1][0]) == float(value):
                                semanticsResult += f'WIN\n'
                            else:
                                semanticsResult += f'FAIL\n'
                    elif one == False and three == False:
                        value = []
                        for j in varidents:
                            if j == lexeme[i+3][0] or j == lexeme[i+1][0]:
                                value.append(varidents[j])
                        if len(value) == 2:
                            if convertFloat(value[0]) == True and  convertFloat(value[1]) == True:
                                if float(value[0]) == float(value[1]):
                                    semanticsResult += f'WIN\n'
                                else:
                                    semanticsResult += f'FAIL\n'
                elif lexeme[i][0] == 'DIFFRINT' and len(lexeme) == 4:
                    one = convertFloat(lexeme[i+1][0])
                    three = convertFloat(lexeme[i+3][0])
                    if one == True and three == True:
                        if float(lexeme[i+1][0]) != float(lexeme[i+3][0]):
                            semanticsResult += f'WIN\n'
                        else:
                            semanticsResult += f'FAIL\n'
                    elif one == False and three == True:
                        value = ""
                        for j in varidents:
                            if j == lexeme[i+1][0]:
                                value = varidents[j]
                        if convertFloat(value) == True:
                            if float(value) != float(lexeme[i+3][0]):
                                semanticsResult += f'WIN\n'
                            else:
                                semanticsResult += f'FAIL\n'
                    elif one == True and three == False:
                        value = ""
                        for j in varidents:
                            if j == lexeme[i+3][0]:
                                value = varidents[j]
                        if convertFloat(value) == True:
                            if float(lexeme[i+1][0]) != float(value):
                                semanticsResult += f'WIN\n'
                            else:
                                semanticsResult += f'FAIL\n'
                    elif one == False and three == False:
                        value = []
                        for j in varidents:
                            if j == lexeme[i+3][0] or j == lexeme[i+1][0]:
                                value.append(varidents[j])
                        if len(value) == 2:
                            if convertFloat(value[0]) == True and  convertFloat(value[1]) == True:
                                if float(value[0]) != float(value[1]):
                                    semanticsResult += f'WIN\n'
                            else:
                                semanticsResult += f'FAIL\n'
                elif lexeme[i][0] == 'BOTH SAEM' and len(lexeme) > 4 and lexeme[3][0] == 'SMALLR OF':
            # if float(lexeme[i+1][0]) >= float(lexeme[i+6][0]):
            #     result = f'WIN\n'
            # else:
            #     result = f'FAIL\n'
                    one = convertFloat(lexeme[i+1][0])
                    three = convertFloat(lexeme[i+6][0])
                    if one == True and three == True:
                        if float(lexeme[i+1][0]) >= float(lexeme[i+6][0]):
                            semanticsResult += f'WIN\n'
                        else:
                            semanticsResult += f'FAIL\n'
                    elif one == False and three == True:
                        value = ""
                        for j in varidents:
                            if j == lexeme[i+1][0]:
                                value = varidents[j]
                        if convertFloat(value) == True:
                            if float(value) >= float(lexeme[i+6][0]):
                                semanticsResult += f'WIN\n'
                            else:
                                semanticsResult += f'FAIL\n'
                    elif one == True and three == False:
                        value = ""
                        for j in varidents:
                            if j == lexeme[i+6][0]:
                                value = varidents[j]
                        if convertFloat(value) == True:
                            if float(lexeme[i+1][0]) >= float(value):
                                semanticsResult += f'WIN\n'
                            else:
                                result = f'FAIL\n'
                    elif one == False and three == False:
                        value = []
                        for j in varidents:
                            if j == lexeme[i+6][0] or j == lexeme[i+1][0]:
                                value.append(varidents[j])
                        if len(value) == 2:
                            if convertFloat(value[0]) == True and  convertFloat(value[1]) == True:
                                if float(value[0]) >= float(value[1]):
                                    semanticsResult += f'WIN\n'
                                else:
                                    semanticsResult += f'FAIL\n'
                elif lexeme[i][0] == 'BOTH SAEM' and len(lexeme) >= 4 and lexeme[3][0] == 'BIGGR OF':
            # if float(lexeme[i+1][0]) <= float(lexeme[i+6][0]):
            #     result = f'WIN\n'
            # else:
            #     result = f'FAIL\n'
                    one = convertFloat(lexeme[i+1][0])
                    three = convertFloat(lexeme[i+6][0])
                    if one == True and three == True:
                        if float(lexeme[i+1][0]) <= float(lexeme[i+6][0]):
                            semanticsResult += f'WIN\n'
                        else:
                            semanticsResult += f'FAIL\n'
                    elif one == False and three == True:
                        value = ""
                        for j in varidents:
                            if j == lexeme[i+1][0]:
                                value = varidents[j]
                        if convertFloat(value) == True:
                            if float(value) <= float(lexeme[i+6][0]):
                                semanticsResult += f'WIN\n'
                            else:
                                semanticsResult += f'FAIL\n'
                    elif one == True and three == False:
                        value = ""
                        for j in varidents:
                            if j == lexeme[i+6][0]:
                                value = varidents[j]
                        if convertFloat(value) == True:
                            if float(lexeme[i+1][0]) <= float(value):
                                semanticsResult += f'WIN\n'
                            else:
                                semanticsResult += f'FAIL\n'
                    elif one == False and three == False:
                        value = []
                        for j in varidents:
                            if j == lexeme[i+6][0] or j == lexeme[i+1][0]:
                                value.append(varidents[j])
                        if len(value) == 2:
                            if convertFloat(value[0]) == True and  convertFloat(value[1]) == True:
                                if float(value[0]) <= float(value[1]):
                                    semanticsResult += f'WIN\n'
                                else:
                                    semanticsResult += f'FAIL\n'
                elif lexeme[i][0] == 'DIFFRINT' and len(lexeme) > 4 and lexeme[3][0] == 'SMALLR OF':
            # if float(lexeme[i+1][0]) > float(lexeme[i+6][0]):
            #     result = f'WIN\n'
            # else:
            #     result = f'FAIL\n'
                    one = convertFloat(lexeme[i+1][0])
                    three = convertFloat(lexeme[i+6][0])
                    if one == True and three == True:
                        if float(lexeme[i+1][0]) > float(lexeme[i+6][0]):
                            semanticsResult += f'WIN\n'
                        else:
                            semanticsResult += f'FAIL\n'
                    elif one == False and three == True:
                        value = ""
                        for j in varidents:
                            if j == lexeme[i+1][0]:
                                value = varidents[j]
                        if convertFloat(value) == True:
                            if float(value) > float(lexeme[i+6][0]):
                                semanticsResult += f'WIN\n'
                            else:
                                semanticsResult += f'FAIL\n'
                    elif one == True and three == False:
                        value = ""
                        for j in varidents:
                            if j == lexeme[i+6][0]:
                                value = varidents[j]
                        if convertFloat(value) == True:
                            if float(lexeme[i+1][0]) > float(value):
                                semanticsResult += f'WIN\n'
                            else:
                                semanticsResult += f'FAIL\n'
                    elif one == False and three == False:
                        value = []
                        for j in varidents:
                            if j == lexeme[i+6][0] or j == lexeme[i+1][0]:
                                value.append(varidents[j])
                        if len(value) == 2:
                            if convertFloat(value[0]) == True and  convertFloat(value[1]) == True:
                                if float(value[0]) > float(value[1]):
                                    semanticsResult += f'WIN\n'
                                else:
                                    semanticsResult += f'FAIL\n'
                elif lexeme[i][0] == 'DIFFRINT' and len(lexeme) > 4 and lexeme[3][0] == 'BIGGR OF':
            # if float(lexeme[i+1][0]) < float(lexeme[i+6][0]):
            #     result = f'WIN\n'
            # else:
            #     result = f'FAIL\n'
                    one = convertFloat(lexeme[i+1][0])
                    three = convertFloat(lexeme[i+6][0])
                    if one == True and three == True:
                        if float(lexeme[i+1][0]) < float(lexeme[i+6][0]):
                            semanticsResult += f'WIN\n'
                        else:
                            semanticsResult += f'FAIL\n'
                    elif one == False and three == True:
                        value = ""
                        for j in varidents:
                            if j == lexeme[i+1][0]:
                                value = varidents[j]
                        if convertFloat(value) == True:
                            if float(value) < float(lexeme[i+6][0]):
                                semanticsResult += f'WIN\n'
                            else:
                                semanticsResult += f'FAIL\n'
                    elif one == True and three == False:
                        value = ""
                        for j in varidents:
                            if j == lexeme[i+6][0]:
                                value = varidents[j]
                        if convertFloat(value) == True:
                            if float(lexeme[i+1][0]) < float(value):
                                semanticsResult += f'WIN\n'
                            else:
                                semanticsResult += f'FAIL\n'
                    elif one == False and three == False:
                        value = []
                        for j in varidents:
                            if j == lexeme[i+6][0] or j == lexeme[i+1][0]:
                                value.append(varidents[j])
                        if len(value) == 2:
                            if convertFloat(value[0]) == True and  convertFloat(value[1]) == True:
                                if float(value[0]) < float(value[1]):
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
                #FINITY ARITY OF BOOLEAN
                #BOTH OF
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
                    elif lexeme[i+1][1] == 'TROOF Literal' and lexeme[i+3][0] in varidents:
                        if lexeme[i+1][0] == 'WIN' and varidents[lexeme[i+3][0]] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif lexeme[i+1][0] == 'WIN' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                        elif lexeme[i+1][0] == 'FAIL' and varidents[lexeme[i+3][0]] == 'WIN':
                            semanticsResult += f'FAIL\n'
                        elif lexeme[i+1][0] == 'FAIL' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                    elif lexeme[i+1][1] == 'Identifier' and lexeme[i+3][0] in varidents:
                        if varidents[lexeme[i+1][0]] == 'WIN' and varidents[lexeme[i+3][0]] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'WIN' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and varidents[lexeme[i+3][0]] == 'WIN':
                            semanticsResult += f'FAIL\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                #EITHER OF
                elif lexeme[i][0] == 'EITHER OF' and len(lexeme) == 4:
                    if lexeme[i+1][1] == 'TROOF Literal' and lexeme[i+3][1] == 'TROOF Literal':
                        if lexeme[i+1][0] == 'WIN' and lexeme[i+3][0] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif lexeme[i+1][0] == 'WIN' and lexeme[i+3][0] == 'FAIL':
                            semanticsResult += f'WIN\n'
                        elif lexeme[i+1][0] == 'FAIL' and lexeme[i+3][0] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif lexeme[i+1][0] == 'FAIL' and lexeme[i+3][0] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                    elif lexeme[i+1][1] == 'Identifier' and lexeme[i+3][1] == 'TROOF Literal':
                        if varidents[lexeme[i+1][0]] == 'WIN' and lexeme[i+3][0] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'WIN' and lexeme[i+3][0] == 'FAIL':
                            semanticsResult += f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and lexeme[i+3][0] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and lexeme[i+3][0] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                    elif lexeme[i+1][1] == 'TROOF Literal' and lexeme[i+3][0] in varidents:
                        if lexeme[i+1][0] == 'WIN' and varidents[lexeme[i+3][0]] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif lexeme[i+1][0] == 'WIN' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'WIN\n'
                        elif lexeme[i+1][0] == 'FAIL' and varidents[lexeme[i+3][0]] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif lexeme[i+1][0] == 'FAIL' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                    elif lexeme[i+1][1] == 'Identifier' and lexeme[i+3][0] in varidents:
                        if varidents[lexeme[i+1][0]] == 'WIN' and varidents[lexeme[i+3][0]] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'WIN' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and varidents[lexeme[i+3][0]] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                #WON OF
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
                            semanticsResult += f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and lexeme[i+3][0] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                    elif lexeme[i+1][1] == 'TROOF Literal' and lexeme[i+3][1] == 'Identifier':
                        if lexeme[i+1][0] == 'WIN' and varidents[lexeme[i+3][0]] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif lexeme[i+1][0] == 'WIN' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'WIN\n'
                        elif lexeme[i+1][0] == 'FAIL' and varidents[lexeme[i+3][0]] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif lexeme[i+1][0] == 'FAIL' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                    elif lexeme[i+1][1] == 'Identifier' and lexeme[i+3][1] == 'Identifier':
                        if varidents[lexeme[i+1][0]] == 'WIN' and varidents[lexeme[i+3][0]] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'WIN' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and varidents[lexeme[i+3][0]] == 'WIN':
                            semanticsResult += f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                #NOT
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
                #R
                elif lexeme[i][0] == 'R':
                    if len(lexeme) == 3:

                        for j in varidents:
                            if lexeme[i-1][0] == j:
                                print(lexeme[i+1][0])
                            # print(lexeme[i+1][0].isnumeric())
                                if lexeme[i+1][0].isnumeric():
                                    varidents[j] = int(lexeme[i+1][0])
                                    # print(varidents)
                                    modified_varidents[lexeme[i-1][0]] = int(lexeme[i+1][0])
                                else:
                                    if convertFloat(lexeme[i+1][0]):
                                        varidents[j] = float(lexeme[i+1][0])
                                        # print(varidents)
                                        modified_varidents[lexeme[i-1][0]] = float(lexeme[i+1][0])
                                    elif lexeme[i+1][0] == 'WIN' or lexeme[i+1][0] == 'FAIL':
                                        varidents[j] = lexeme[i+1][0]
                                        # print(varidents)
                                        modified_varidents[lexeme[i-1][0]] = lexeme[i+1][0]
                                    else:
                                        for k in varidents:
                                            if lexeme[i+1][0] == k:
                                                varidents[j] = varidents[k]
                                                modified_varidents[lexeme[i-1][0]] = varidents[k]
                                                break
                                
                    elif len(lexeme) == 5:
                        # print(varidents)
                        for j in varidents:
                            if lexeme[i-1][0] == j:
                                if lexeme[i+1][0] == '"' and lexeme[i+3][0] == '"':
                                    varidents[j] = lexeme[i+2][0]
                                    modified_varidents[lexeme[i-1][0]] = str(lexeme[i+2][0])
                    else:
                        if lexeme[i+1][0] == 'BOTH SAEM' or lexeme[i+1][0] == 'DIFFRINT':
                            for j in varidents:
                                if lexeme[i-1][0] == j:
                                    result = comparison_expression(lexeme[i+1:])
                                    if len(result) != 0:
                                        varidents[j] = result
                                        modified_varidents[lexeme[i-1][0]] = str(result)
                                        break
                                    break
                        elif lexeme[i+1][0] == 'BOTH OF' or lexeme[i+1][0] == 'EITHER OF' or lexeme[i+1][0] == 'WON OF' or lexeme[i+1][0] == 'NOT':
                            # fin_boolean_expression(lexeme)
                            for j in varidents:
                                if lexeme[i-1][0] == j:
                                    result = fin_boolean_expression(lexeme[i+1:])
                                    if len(result) != 0:
                                        varidents[j] = result
                                        modified_varidents[lexeme[i-1][0]] = str(result)
                                        break
                                    break
                #MAEK    
                elif lexeme[i][0] == 'MAEK':
                    if len(lexeme) == 3 or len(lexeme) == 4 :
                        for j in varidents:
                            if j == lexeme[i+1][0]:
                                if varidents[j] == 'NOOB':
                                    if lexeme[i+2][0] == 'YARN' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'YARN'):
                                        explicit_typecast.append("")
                                    elif lexeme[i+2][0] == 'NUMBAR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBAR'):
                                        explicit_typecast.append("0.0")
                                    elif lexeme[i+2][0] == 'NUMBR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBR'):
                                        explicit_typecast.append("0")
                                    elif lexeme[i+2][0] == 'TROOF' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'TROOF'):
                                        explicit_typecast.append("FAIL")
                                    elif lexeme[i+2][0] == 'NOOB' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NOOB'):
                                        explicit_typecast.append("NOOB")
                                else:
                                    if str(varidents[j]).isnumeric():
                                        if lexeme[i+2][0] == 'YARN' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'YARN'):
                                            explicit_typecast.append(str(varidents[j]))
                                        elif lexeme[i+2][0] == 'NUMBAR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBAR'):
                                            explicit_typecast.append(float(varidents[j]))
                                        elif lexeme[i+2][0] == 'NUMBR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBR'):
                                            explicit_typecast.append(int(float(varidents[j])))
                                        elif lexeme[i+2][0] == 'NOOB' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NOOB'):
                                            explicit_typecast.append("NOOB")
                                    elif convertFloat(varidents[j]):
                                        if lexeme[i+2][0] == 'YARN' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'YARN'):
                                            explicit_typecast.append(str(varidents[j]))
                                        elif lexeme[i+2][0] == 'NUMBAR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBAR'):
                                            explicit_typecast.append(float(varidents[j]))
                                        elif lexeme[i+2][0] == 'NUMBR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBR'):
                                            explicit_typecast.append(int(float(varidents[j])))
                                        elif lexeme[i+2][0] == 'NOOB' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NOOB'):
                                            explicit_typecast.append("NOOB")
                                    elif varidents[j] == 'WIN':
                                        if lexeme[i+2][0] == 'YARN' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'YARN'):
                                            explicit_typecast.append(str(varidents[j]))
                                        elif lexeme[i+2][0] == 'NUMBAR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBAR'):
                                            explicit_typecast.append('1.0')
                                        elif lexeme[i+2][0] == 'NUMBR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBR'):
                                            explicit_typecast.append('1')
                                        elif lexeme[i+2][0] == 'TROOF' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'TROOF'):
                                            explicit_typecast.append(varidents[j])
                                        elif lexeme[i+2][0] == 'NOOB' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NOOB'):
                                            explicit_typecast.append("NOOB")
                                    elif varidents[j] == 'FAIL':
                                        if lexeme[i+2][0] == 'YARN' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'YARN'):
                                            explicit_typecast.append(str(varidents[j]))
                                        elif lexeme[i+2][0] == 'NUMBAR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBAR'):
                                            explicit_typecast.append('0.0')
                                        elif lexeme[i+2][0] == 'NUMBR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBR'):
                                            explicit_typecast.append('0')
                                        elif lexeme[i+2][0] == 'TROOF' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'TROOF'):
                                            explicit_typecast = varidents[j]
                                        elif lexeme[i+2][0] == 'NOOB' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NOOB'):
                                            explicit_typecast.append("NOOB")
            lexeme.clear()
    return semanticsResult



def fin_boolean_expression(lexeme):
    result = []
    for i in range(0, len(lexeme)):
        # print(lexeme[i][0])
        if lexeme[i][0] == 'BOTH OF' and len(lexeme) == 4:
                    if lexeme[i+1][1] == 'TROOF Literal' and lexeme[i+3][1] == 'TROOF Literal':
                        if lexeme[i+1][0] == 'WIN' and lexeme[i+3][0] == 'WIN':
                           result = f'WIN\n'
                        elif lexeme[i+1][0] == 'WIN' and lexeme[i+3][0] == 'FAIL':
                            result = f'FAIL\n'
                        elif lexeme[i+1][0] == 'FAIL' and lexeme[i+3][0] == 'WIN':
                            result = f'FAIL\n'
                        elif lexeme[i+1][0] == 'FAIL' and lexeme[i+3][0] == 'FAIL':
                            result = f'FAIL\n'
                    elif lexeme[i+1][0] in varidents and lexeme[i+3][1] == 'TROOF Literal':
                        if varidents[lexeme[i+1][0]] == 'WIN' and lexeme[i+3][0] == 'WIN':
                            result = f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'WIN' and lexeme[i+3][0] == 'FAIL':
                            result = f'FAIL\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and lexeme[i+3][0] == 'WIN':
                            result = f'FAIL\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and lexeme[i+3][0] == 'FAIL':
                            result = f'FAIL\n'
                    elif lexeme[i+1][1] == 'TROOF Literal' and lexeme[i+3][0] in varidents:
                        if lexeme[i+1][0] == 'WIN' and varidents[lexeme[i+3][0]] == 'WIN':
                            result = f'WIN\n'
                        elif lexeme[i+1][0] == 'WIN' and varidents[lexeme[i+3][0]] == 'FAIL':
                            result = f'FAIL\n'
                        elif lexeme[i+1][0] == 'FAIL' and varidents[lexeme[i+3][0]] == 'WIN':
                            result = f'FAIL\n'
                        elif lexeme[i+1][0] == 'FAIL' and varidents[lexeme[i+3][0]] == 'FAIL':
                            semanticsResult += f'FAIL\n'
                    elif lexeme[i+1][0] in varidents and lexeme[i+3][0] in varidents:
                        if varidents[lexeme[i+1][0]] == 'WIN' and varidents[lexeme[i+3][0]] == 'WIN':
                            result = f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'WIN' and varidents[lexeme[i+3][0]] == 'FAIL':
                            result = f'FAIL\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and varidents[lexeme[i+3][0]] == 'WIN':
                            result = f'FAIL\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and varidents[lexeme[i+3][0]] == 'FAIL':
                            result = f'FAIL\n'
        elif lexeme[i][0] == 'EITHER OF' and len(lexeme) == 4:
                    if lexeme[i+1][1] == 'TROOF Literal' and lexeme[i+3][1] == 'TROOF Literal':
                        if lexeme[i+1][0] == 'WIN' and lexeme[i+3][0] == 'WIN':
                            result = f'WIN\n'
                        elif lexeme[i+1][0] == 'WIN' and lexeme[i+3][0] == 'FAIL':
                            result = f'WIN\n'
                        elif lexeme[i+1][0] == 'FAIL' and lexeme[i+3][0] == 'WIN':
                            result = f'WIN\n'
                        elif lexeme[i+1][0] == 'FAIL' and lexeme[i+3][0] == 'FAIL':
                            result = f'FAIL\n'
                    elif lexeme[i+1][0] in varidents and lexeme[i+3][1] == 'TROOF Literal':
                        if varidents[lexeme[i+1][0]] == 'WIN' and lexeme[i+3][0] == 'WIN':
                            result = f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'WIN' and lexeme[i+3][0] == 'FAIL':
                            result = f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and lexeme[i+3][0] == 'WIN':
                            result = f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and lexeme[i+3][0] == 'FAIL':
                            result = f'FAIL\n'
                    elif lexeme[i+1][1] == 'TROOF Literal' and lexeme[i+3][0] in varidents:
                        if lexeme[i+1][0] == 'WIN' and varidents[lexeme[i+3][0]] == 'WIN':
                            result = f'WIN\n'
                        elif lexeme[i+1][0] == 'WIN' and varidents[lexeme[i+3][0]] == 'FAIL':
                            result = f'WIN\n'
                        elif lexeme[i+1][0] == 'FAIL' and varidents[lexeme[i+3][0]] == 'WIN':
                            result = f'WIN\n'
                        elif lexeme[i+1][0] == 'FAIL' and varidents[lexeme[i+3][0]] == 'FAIL':
                            result = f'FAIL\n'
                    elif lexeme[i+1][0] in varidents and lexeme[i+3][0] in varidents:
                        if varidents[lexeme[i+1][0]] == 'WIN' and varidents[lexeme[i+3][0]] == 'WIN':
                            result = f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'WIN' and varidents[lexeme[i+3][0]] == 'FAIL':
                            result = f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and varidents[lexeme[i+3][0]] == 'WIN':
                            result = f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and varidents[lexeme[i+3][0]] == 'FAIL':
                            result = f'FAIL\n'
                #WON OF
        elif lexeme[i][0] == 'WON OF' and len(lexeme) == 4:
                    if lexeme[i+1][1] == 'TROOF Literal' and lexeme[i+3][1] == 'TROOF Literal':
                        if lexeme[i+1][0] == 'WIN' and lexeme[i+3][0] == 'WIN':
                            result = f'FAIL\n'
                        elif lexeme[i+1][0] == 'WIN' and lexeme[i+3][0] == 'FAIL':
                            result = f'WIN\n'
                        elif lexeme[i+1][0] == 'FAIL' and lexeme[i+3][0] == 'WIN':
                            result = f'WIN\n'
                        elif lexeme[i+1][0] == 'FAIL' and lexeme[i+3][0] == 'FAIL':
                            result = f'FAIL\n'
                    elif lexeme[i+1][0] in varidents and lexeme[i+3][1] == 'TROOF Literal':
                        if varidents[lexeme[i+1][0]] == 'WIN' and lexeme[i+3][0] == 'WIN':
                            result = f'FAIL\n'
                        elif varidents[lexeme[i+1][0]] == 'WIN' and lexeme[i+3][0] == 'FAIL':
                            result = f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and lexeme[i+3][0] == 'WIN':
                            result = f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and lexeme[i+3][0] == 'FAIL':
                            result = f'FAIL\n'
                    elif lexeme[i+1][1] == 'TROOF Literal' and lexeme[i+3][0] in varidents:
                        if lexeme[i+1][0] == 'WIN' and varidents[lexeme[i+3][0]] == 'WIN':
                            result = f'FAIL\n'
                        elif lexeme[i+1][0] == 'WIN' and varidents[lexeme[i+3][0]] == 'FAIL':
                            result = f'WIN\n'
                        elif lexeme[i+1][0] == 'FAIL' and varidents[lexeme[i+3][0]] == 'WIN':
                            result = f'WIN\n'
                        elif lexeme[i+1][0] == 'FAIL' and varidents[lexeme[i+3][0]] == 'FAIL':
                            result = f'FAIL\n'
                    elif lexeme[i+1][0] in varidents and lexeme[i+3][0] in varidents:
                        if varidents[lexeme[i+1][0]] == 'WIN' and varidents[lexeme[i+3][0]] == 'WIN':
                            result = f'FAIL\n'
                        elif varidents[lexeme[i+1][0]] == 'WIN' and varidents[lexeme[i+3][0]] == 'FAIL':
                            result = f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and varidents[lexeme[i+3][0]] == 'WIN':
                            result = f'WIN\n'
                        elif varidents[lexeme[i+1][0]] == 'FAIL' and varidents[lexeme[i+3][0]] == 'FAIL':
                            result = f'FAIL\n'
                #NOT
        elif lexeme[i][0] == 'NOT' and len(lexeme) == 2:
                # print('hehe')
                if lexeme[i+1][0] == 'WIN':
                            result = f'FAIL\n'
                elif lexeme[i+1][0] == 'FAIL':
                            result = f'WIN\n'
                elif lexeme[i+1][0] in varidents:

                    if varidents[lexeme[i+1][0]] == 'WIN':
                            result = f'FAIL\n'
                    elif varidents[lexeme[i+1][0]] == 'FAIL':
                            result = f'WIN\n'
    return result

def comparison_expression(lexeme):
    # print(lexeme, "comparison exp", len(lexeme))
    # len(lexeme)
    result = []
    for i in range(0, len(lexeme)):
        if lexeme[i][0] == 'BOTH SAEM' and len(lexeme) == 4:
            one = convertFloat(lexeme[i+1][0])
            three = convertFloat(lexeme[i+3][0])
            if one == True and three == True:
                if float(lexeme[i+1][0]) == float(lexeme[i+3][0]):
                    result = f'WIN\n'
                else:
                    result = f'FAIL\n'
            elif one == False and three == True:
                value = ""
                for j in varidents:
                    if j == lexeme[i+1][0]:
                        value = varidents[j]
                if convertFloat(value) == True:
                    if float(value) == float(lexeme[i+3][0]):
                        result = f'WIN\n'
                    else:
                        result = f'FAIL\n'
            elif one == True and three == False:
                value = ""
                for j in varidents:
                    if j == lexeme[i+3][0]:
                        value = varidents[j]
                if convertFloat(value) == True:
                    if float(lexeme[i+1][0]) == float(value):
                        result = f'WIN\n'
                    else:
                        result = f'FAIL\n'
            elif one == False and three == False:
                value = []
                for j in varidents:
                    if j == lexeme[i+3][0] or j == lexeme[i+1][0]:
                        value.append(varidents[j])
                if len(value) == 2:
                    if convertFloat(value[0]) == True and  convertFloat(value[1]) == True:
                        if float(value[0]) == float(value[1]):
                            result = f'WIN\n'
                        else:
                            result = f'FAIL\n'
        elif lexeme[i][0] == 'DIFFRINT' and len(lexeme) == 4:
            one = convertFloat(lexeme[i+1][0])
            three = convertFloat(lexeme[i+3][0])
            if one == True and three == True:
                if float(lexeme[i+1][0]) != float(lexeme[i+3][0]):
                    result = f'WIN\n'
                else:
                    result = f'FAIL\n'
            elif one == False and three == True:
                value = ""
                for j in varidents:
                    if j == lexeme[i+1][0]:
                        value = varidents[j]
                if convertFloat(value) == True:
                    if float(value) != float(lexeme[i+3][0]):
                        result = f'WIN\n'
                    else:
                        result = f'FAIL\n'
            elif one == True and three == False:
                value = ""
                for j in varidents:
                    if j == lexeme[i+3][0]:
                        value = varidents[j]
                if convertFloat(value) == True:
                    if float(lexeme[i+1][0]) != float(value):
                        result = f'WIN\n'
                    else:
                        result = f'FAIL\n'
            elif one == False and three == False:
                value = []
                for j in varidents:
                    if j == lexeme[i+3][0] or j == lexeme[i+1][0]:
                        value.append(varidents[j])
                if len(value) == 2:
                    if convertFloat(value[0]) == True and  convertFloat(value[1]) == True:
                        if float(value[0]) != float(value[1]):
                            result = f'WIN\n'
                        else:
                            result = f'FAIL\n'
        elif lexeme[i][0] == 'BOTH SAEM' and len(lexeme) > 4 and lexeme[3][0] == 'SMALLR OF':
            # if float(lexeme[i+1][0]) >= float(lexeme[i+6][0]):
            #     result = f'WIN\n'
            # else:
            #     result = f'FAIL\n'
            one = convertFloat(lexeme[i+1][0])
            three = convertFloat(lexeme[i+6][0])
            if one == True and three == True:
                if float(lexeme[i+1][0]) >= float(lexeme[i+6][0]):
                    result = f'WIN\n'
                else:
                    result = f'FAIL\n'
            elif one == False and three == True:
                value = ""
                for j in varidents:
                    if j == lexeme[i+1][0]:
                        value = varidents[j]
                if convertFloat(value) == True:
                    if float(value) >= float(lexeme[i+6][0]):
                        result = f'WIN\n'
                    else:
                        result = f'FAIL\n'
            elif one == True and three == False:
                value = ""
                for j in varidents:
                    if j == lexeme[i+6][0]:
                        value = varidents[j]
                if convertFloat(value) == True:
                    if float(lexeme[i+1][0]) >= float(value):
                        result = f'WIN\n'
                    else:
                        result = f'FAIL\n'
            elif one == False and three == False:
                value = []
                for j in varidents:
                    if j == lexeme[i+6][0] or j == lexeme[i+1][0]:
                        value.append(varidents[j])
                if len(value) == 2:
                    if convertFloat(value[0]) == True and  convertFloat(value[1]) == True:
                        if float(value[0]) >= float(value[1]):
                            result = f'WIN\n'
                        else:
                            result = f'FAIL\n'
        elif lexeme[i][0] == 'BOTH SAEM' and len(lexeme) >= 4 and lexeme[3][0] == 'BIGGR OF':
            # if float(lexeme[i+1][0]) <= float(lexeme[i+6][0]):
            #     result = f'WIN\n'
            # else:
            #     result = f'FAIL\n'
            one = convertFloat(lexeme[i+1][0])
            three = convertFloat(lexeme[i+6][0])
            if one == True and three == True:
                if float(lexeme[i+1][0]) <= float(lexeme[i+6][0]):
                    result = f'WIN\n'
                else:
                    result = f'FAIL\n'
            elif one == False and three == True:
                value = ""
                for j in varidents:
                    if j == lexeme[i+1][0]:
                        value = varidents[j]
                if convertFloat(value) == True:
                    if float(value) <= float(lexeme[i+6][0]):
                        result = f'WIN\n'
                    else:
                        result = f'FAIL\n'
            elif one == True and three == False:
                value = ""
                for j in varidents:
                    if j == lexeme[i+6][0]:
                        value = varidents[j]
                if convertFloat(value) == True:
                    if float(lexeme[i+1][0]) <= float(value):
                        result = f'WIN\n'
                    else:
                        result = f'FAIL\n'
            elif one == False and three == False:
                value = []
                for j in varidents:
                    if j == lexeme[i+6][0] or j == lexeme[i+1][0]:
                        value.append(varidents[j])
                if len(value) == 2:
                    if convertFloat(value[0]) == True and  convertFloat(value[1]) == True:
                        if float(value[0]) <= float(value[1]):
                            result = f'WIN\n'
                        else:
                            result = f'FAIL\n'
        elif lexeme[i][0] == 'DIFFRINT' and len(lexeme) > 4 and lexeme[3][0] == 'SMALLR OF':
            # if float(lexeme[i+1][0]) > float(lexeme[i+6][0]):
            #     result = f'WIN\n'
            # else:
            #     result = f'FAIL\n'
            one = convertFloat(lexeme[i+1][0])
            three = convertFloat(lexeme[i+6][0])
            if one == True and three == True:
                if float(lexeme[i+1][0]) > float(lexeme[i+6][0]):
                    result = f'WIN\n'
                else:
                    result = f'FAIL\n'
            elif one == False and three == True:
                value = ""
                for j in varidents:
                    if j == lexeme[i+1][0]:
                        value = varidents[j]
                if convertFloat(value) == True:
                    if float(value) > float(lexeme[i+6][0]):
                        result = f'WIN\n'
                    else:
                        result = f'FAIL\n'
            elif one == True and three == False:
                value = ""
                for j in varidents:
                    if j == lexeme[i+6][0]:
                        value = varidents[j]
                if convertFloat(value) == True:
                    if float(lexeme[i+1][0]) > float(value):
                        result = f'WIN\n'
                    else:
                        result = f'FAIL\n'
            elif one == False and three == False:
                value = []
                for j in varidents:
                    if j == lexeme[i+6][0] or j == lexeme[i+1][0]:
                        value.append(varidents[j])
                if len(value) == 2:
                    if convertFloat(value[0]) == True and  convertFloat(value[1]) == True:
                        if float(value[0]) > float(value[1]):
                            result = f'WIN\n'
                        else:
                            result = f'FAIL\n'
        elif lexeme[i][0] == 'DIFFRINT' and len(lexeme) > 4 and lexeme[3][0] == 'BIGGR OF':
            # if float(lexeme[i+1][0]) < float(lexeme[i+6][0]):
            #     result = f'WIN\n'
            # else:
            #     result = f'FAIL\n'
            one = convertFloat(lexeme[i+1][0])
            three = convertFloat(lexeme[i+6][0])
            if one == True and three == True:
                if float(lexeme[i+1][0]) < float(lexeme[i+6][0]):
                    result = f'WIN\n'
                else:
                    result = f'FAIL\n'
            elif one == False and three == True:
                value = ""
                for j in varidents:
                    if j == lexeme[i+1][0]:
                        value = varidents[j]
                if convertFloat(value) == True:
                    if float(value) < float(lexeme[i+6][0]):
                        result = f'WIN\n'
                    else:
                        result = f'FAIL\n'
            elif one == True and three == False:
                value = ""
                for j in varidents:
                    if j == lexeme[i+6][0]:
                        value = varidents[j]
                if convertFloat(value) == True:
                    if float(lexeme[i+1][0]) < float(value):
                        result = f'WIN\n'
                    else:
                        result = f'FAIL\n'
            elif one == False and three == False:
                value = []
                for j in varidents:
                    if j == lexeme[i+6][0] or j == lexeme[i+1][0]:
                        value.append(varidents[j])
                if len(value) == 2:
                    if convertFloat(value[0]) == True and  convertFloat(value[1]) == True:
                        if float(value[0]) < float(value[1]):
                            result = f'WIN\n'
                        else:
                            result = f'FAIL\n'
        # print(result)
    return result

# def arithmetic():


def convertFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
