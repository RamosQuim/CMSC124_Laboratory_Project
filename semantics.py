import keywords
import syntax
import for_input
# import ui 

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
    arithmetic = ['SUM OF','DIFF OF','PRODUKT OF', 'QUOSHUNT OF', 'MOD OF', 'BIGGR OF', 'SMALLR OF']
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
            print(f"lexeme: {lexeme}")
            if ['BTW', 'Comment Delimiter'] in lexeme:
                lexeme.pop(lexeme.index(['BTW', 'Comment Delimiter'])+1)
                lexeme.pop(lexeme.index(['BTW', 'Comment Delimiter']))
            
            print(f"len(lexeme): {len(lexeme)}")
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
                        semanticsResult += f'FAIL\n'

                #THIS PART IS FOR THE COMPUTATIONS!!
                elif lexeme[i][0] in arithmetic:
                    semanticsResult += str(ArithmeticAnalyzer(varidents,arithmetic,lexeme))
                    break #hindi ko alam baket nag break pa pero pag wala siya nag error shadkashdkadhaskhdahdsa
                
                #THIS IS TO CATER GIMMEH - ASKING USER FOR INPUT
                elif lexeme[i][0] == 'GIMMEH':
                    # resolved na :>>
                    input_value = for_input.get_user_input()
                    varidents[lexeme[i+1][0]] = str(input_value)
                    semanticsResult += f"{lexeme[i+1][0]} is: {varidents[lexeme[i+1][0]]}\n"
                    
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
                
                elif lexeme[i][0] == 'VISIBLE':
                    print("UMABOT DITO")
                    visible_index = i + 1
                    temp_result = ""
                    #result = "uwu"
                    print(f"i: {i}")
                    print(f"current lexeme: {lexeme}")
                    print(f"len(lexeme) sa visible: {len(lexeme)}")
                    print(f"visible_index: {visible_index}")
                    print(f"currently pointed to: {lexeme[visible_index]}")
                    while visible_index < len(lexeme):
                        #print(f"visible_index: {visible_index}")
                        #print(f"currently pointed to right now: {lexeme[visible_index]}")
                        if lexeme[visible_index][1] == 'String Delimiter':
                            temp_result += str(lexeme[visible_index+1][0])
                            visible_index +=3
                        elif lexeme[visible_index][1] == 'Output Delimiter':
                            visible_index +=1
                        elif lexeme[visible_index][0] in arithmetic:
                            #kunin ang lexeme until +
                            temp = []
                            temp_index = visible_index
                            print(f"current lexeme: {lexeme}")
                            print(f"temp_index: {temp_index}")
                            while temp_index < len(lexeme):
                                if lexeme[temp_index][1] == "Output Delimiter":
                                    break
                                else:
                                    print(f"temp_index: {temp_index}")
                                    temp.append(lexeme[temp_index])
                                    temp_index+=1
                            print(f"lexeme na ipapasa:{temp}")
                            #temp_result += str(ArithmeticAnalyzer(varidents,arithmetic,temp))
                            visible_index = temp_index
                    semanticsResult += f"{temp_result}\n"

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
    

#this part is for the semantics of the arithmetic operations (SUM OF, DIFF OF, ETC.)
def ArithmeticAnalyzer(varidents, arithmetic,lexeme):            
    if lexeme[0][0] in arithmetic:
        remover_index = 0
        is_float = False
        print(f"semantics lexeme sa arithmetic: {lexeme}")

        #this is created to remove the literal naming in lexeme and checking if it's a float or not
        while remover_index < len(lexeme):
            
            if lexeme[remover_index][1] == "String Delimiter":
                    lexeme.pop(remover_index)
                    remover_index = remover_index - 1
            elif lexeme[remover_index][1] == 'NUMBAR Literal' or lexeme[remover_index][1] == 'YARN Literal' or lexeme[remover_index][1] == 'Identifier':
                if lexeme[remover_index][1] == 'Identifier':
                    float_value = float(varidents[lexeme[remover_index][0]])
                    int_value = int(float_value)
                    if float_value != int_value:
                        is_float = True
                else:
                    float_value = float(lexeme[remover_index][0])
                    int_value = int(float_value)
                    if float_value != int_value:
                        is_float = True
            remover_index = remover_index + 1
        print(lexeme)
        arithmetic_index = 0
        operation_list = []
        values_list = []
        result = 0
        an_counter = 0

        while arithmetic_index < len(lexeme):
            if lexeme[arithmetic_index][0] == "VISIBLE":
                break
            #THIS IS FOR CHECKING IF MAY KATABI BA SIYA OR WALA NA OPERATION
            print(f"current lexeme sa arithemtic: {lexeme}")
            print(f"currently pointed to: {lexeme[arithmetic_index][0]}")
            print(f"varidents: {varidents}")
            if lexeme[arithmetic_index][0] in arithmetic:
                if lexeme[arithmetic_index+1][0] not in arithmetic:
                    if lexeme[arithmetic_index+3][0] not in arithmetic:
                        if lexeme[arithmetic_index][0] == 'SUM OF':
                            #this is created to cater the variables!!!
                            #print(f"lexeme[arithmetic_index+1][0]: {lexeme[arithmetic_index+1][0]}")
                            #print(f"varidents[lexeme[arithmetic_index+1][0]]: {varidents[lexeme[arithmetic_index+1][0]]}")
                            if lexeme[arithmetic_index+1][1] == 'Identifier' and lexeme[arithmetic_index+3][1] == 'Identifier':                                        
                                result = float(varidents[lexeme[arithmetic_index+1][0]])+float(varidents[lexeme[arithmetic_index+3][0]])
                            elif lexeme[arithmetic_index+1][1] == 'Identifier':
                                result = float(varidents[lexeme[arithmetic_index+1][0]])+float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'Identifier':
                                result = float(lexeme[arithmetic_index+1][0])+float(varidents[lexeme[arithmetic_index+3][0]])
                            else:
                                result = float(lexeme[arithmetic_index+1][0])+float(lexeme[arithmetic_index+3][0])
                        elif lexeme[arithmetic_index][0] == 'DIFF OF':
                            #this is created to cater the variables!!!
                            if lexeme[arithmetic_index+1][1] == 'Identifier' and lexeme[arithmetic_index+3][1] == 'Identifier':                                        
                                result = float(varidents[lexeme[arithmetic_index+1][0]])-float(varidents[lexeme[arithmetic_index+3][0]])
                            elif lexeme[arithmetic_index+1][1] == 'Identifier':
                                result = float(varidents[lexeme[arithmetic_index+1][0]])-float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'Identifier':
                                result = float(lexeme[arithmetic_index+1][0])-float(varidents[lexeme[arithmetic_index+3][0]])
                            else:
                                result = float(lexeme[arithmetic_index+1][0]) - float(lexeme[arithmetic_index+3][0])
                        elif lexeme[arithmetic_index][0] == 'PRODUKT OF':
                            #this is created to cater the variables!!!
                            if lexeme[arithmetic_index+1][1] == 'Identifier' and lexeme[arithmetic_index+3][1] == 'Identifier':                                        
                                result = float(varidents[lexeme[arithmetic_index+1][0]])*float(varidents[lexeme[arithmetic_index+3][0]])
                            elif lexeme[arithmetic_index+1][1] == 'Identifier':
                                result = float(varidents[lexeme[arithmetic_index+1][0]])*float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'Identifier':
                                result = float(lexeme[arithmetic_index+1][0])*float(varidents[lexeme[arithmetic_index+3][0]])
                            else:
                                result = float(lexeme[arithmetic_index+1][0]) * float(lexeme[arithmetic_index+3][0])
                        elif lexeme[arithmetic_index][0] == 'QUOSHUNT OF':
                            #this is created to cater the variables!!!
                            if lexeme[arithmetic_index+1][1] == 'Identifier' and lexeme[arithmetic_index+3][1] == 'Identifier':                                        
                                result = float(varidents[lexeme[arithmetic_index+1][0]]) / float(varidents[lexeme[arithmetic_index+3][0]])
                            elif lexeme[arithmetic_index+1][1] == 'Identifier':
                                result = float(varidents[lexeme[arithmetic_index+1][0]]) / float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'Identifier':
                                result = float(lexeme[arithmetic_index+1][0]) / float(varidents[lexeme[arithmetic_index+3][0]])
                            else:
                                result = float(lexeme[arithmetic_index+1][0]) / float(lexeme[arithmetic_index+3][0])
                        elif lexeme[arithmetic_index][0] == 'MOD OF':
                            #this is created to cater the variables!!!
                            if lexeme[arithmetic_index+1][1] == 'Identifier' and lexeme[arithmetic_index+3][1] == 'Identifier':                                        
                                result = float(varidents[lexeme[arithmetic_index+1][0]]) % float(varidents[lexeme[arithmetic_index+3][0]])
                            elif lexeme[arithmetic_index+1][1] == 'Identifier':
                                result = float(varidents[lexeme[arithmetic_index+1][0]]) % float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'Identifier':
                                result = float(lexeme[arithmetic_index+1][0]) % float(varidents[lexeme[arithmetic_index+3][0]])
                            else:
                                result = float(lexeme[arithmetic_index+1][0]) % float(lexeme[arithmetic_index+3][0])
                        elif lexeme[arithmetic_index][0] == 'BIGGR OF':
                            #this is created to cater the variables!!!
                            if lexeme[arithmetic_index+1][1] == 'Identifier' and lexeme[arithmetic_index+3][1] == 'Identifier':
                                if float(varidents[lexeme[arithmetic_index+1][0]]) > float(varidents[lexeme[arithmetic_index+3][0]]):
                                    result = float(varidents[lexeme[arithmetic_index+1][0]])
                                else:
                                    result = float(varidents[lexeme[arithmetic_index+3][0]])
                            elif lexeme[arithmetic_index+1][1] == 'Identifier':
                                if float(varidents[lexeme[arithmetic_index+1][0]]) > float(lexeme[arithmetic_index+3][0]):
                                    result = float(varidents[lexeme[arithmetic_index+1][0]])
                                else:
                                    result = float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'Identifier':
                                if float(lexeme[arithmetic_index+1][0]) > float(varidents[lexeme[arithmetic_index+3][0]]):
                                    result = float(lexeme[arithmetic_index+1][0]) 
                                else:
                                    result = float(varidents[lexeme[arithmetic_index+3][0]])
                            else:
                                if float(lexeme[arithmetic_index+1][0]) > float(lexeme[arithmetic_index+3][0]):
                                    result = float(lexeme[arithmetic_index+1][0])
                                else:
                                    result = float(lexeme[arithmetic_index+3][0])
                        elif lexeme[arithmetic_index][0] == 'SMALLR OF':
                            #this is created to cater the variables!!!
                            if lexeme[arithmetic_index+1][1] == 'Identifier' and lexeme[arithmetic_index+3][1] == 'Identifier':
                                if float(varidents[lexeme[arithmetic_index+1][0]]) < float(varidents[lexeme[arithmetic_index+3][0]]):
                                    result = float(varidents[lexeme[arithmetic_index+1][0]])
                                else:
                                    result = float(varidents[lexeme[arithmetic_index+3][0]])
                            elif lexeme[arithmetic_index+1][1] == 'Identifier':
                                if float(varidents[lexeme[arithmetic_index+1][0]]) < float(lexeme[arithmetic_index+3][0]):
                                    result = float(varidents[lexeme[arithmetic_index+1][0]])
                                else:
                                    result = float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'Identifier':
                                if float(lexeme[arithmetic_index+1][0]) < float(varidents[lexeme[arithmetic_index+3][0]]):
                                    result = float(lexeme[arithmetic_index+1][0]) 
                                else:
                                    result = float(varidents[lexeme[arithmetic_index+3][0]])
                            else:
                                if float(lexeme[arithmetic_index+1][0]) < float(lexeme[arithmetic_index+3][0]):
                                    result = float(lexeme[arithmetic_index+1][0]) 
                                else:
                                    result = float(lexeme[arithmetic_index+3][0])
                        arithmetic_index = arithmetic_index + 4
                    else:
                        operation_list.append(lexeme[arithmetic_index][0])
                        values_list.append(float(lexeme[arithmetic_index+1][0]))
                        arithmetic_index = arithmetic_index + 3
                        an_counter = an_counter + 1
                        print(f"next current index is : {lexeme[arithmetic_index][0]}")
                        print(f"current operation list: {operation_list}")
                        print(f"current values list: {values_list}")
                else:
                    operation_list.append(lexeme[arithmetic_index][0])
                    arithmetic_index = arithmetic_index + 1
                print(f"arithmetic_index:{arithmetic_index}")
                print(f"len of lexeme: {len(lexeme)}")                            
            elif lexeme[arithmetic_index][0] == 'AN':
                if lexeme[arithmetic_index+1][0] not in arithmetic:
                    if operation_list[-1] == 'SUM OF':
                        if lexeme[arithmetic_index+1][1] == "Identifier":
                            result = result + float(varidents[lexeme[arithmetic_index+1][0]])
                        else:
                            result = result + float(lexeme[arithmetic_index+1][0])
                    elif operation_list[-1] == 'DIFF OF':
                        if lexeme[arithmetic_index+1][1] == "Identifier":
                            result = result - float(varidents[lexeme[arithmetic_index+1][0]])
                        else:
                            result = result - float(lexeme[arithmetic_index+1][0])
                    elif operation_list[-1] == 'PRODUKT OF':
                        if lexeme[arithmetic_index+1][1] == "Identifier":
                            result = result * float(varidents[lexeme[arithmetic_index+1][0]])
                        else:
                            result = result * float(lexeme[arithmetic_index+1][0])
                    elif operation_list[-1] == 'QUOSHUNT OF':
                        if lexeme[arithmetic_index+1][1] == "Identifier":
                            result = result / float(varidents[lexeme[arithmetic_index+1][0]])
                        else:
                            result = result / float(lexeme[arithmetic_index+1][0])
                    elif operation_list[-1] == 'MOD OF':
                        if lexeme[arithmetic_index+1][1] == "Identifier":
                            result = result % float(varidents[lexeme[arithmetic_index+1][0]])
                        else:
                            result = result % float(lexeme[arithmetic_index+1][0])
                    elif operation_list[-1] == 'BIGGR OF':
                        if lexeme[arithmetic_index+1][1] == "Identifier":
                            if result < float(varidents[lexeme[arithmetic_index+1][0]]):
                                result = float(varidents[lexeme[arithmetic_index+1][0]])
                        else:
                            if result < float(lexeme[arithmetic_index+1][0]):
                                result = float(lexeme[arithmetic_index+1][0])
                    elif operation_list[-1] == 'SMALLR OF':
                        if lexeme[arithmetic_index+1][1] == "Identifier":
                            if result > float(varidents[lexeme[arithmetic_index+1][0]]):  
                                result = float(varidents[lexeme[arithmetic_index+1][0]])
                        else:
                            if result > float(lexeme[arithmetic_index+1][0]):  
                                result = float(lexeme[arithmetic_index+1][0])
                    operation_list.pop(-1)                                        
                    arithmetic_index = arithmetic_index +2
                else:
                    an_counter = an_counter + 1
                    arithmetic_index = arithmetic_index + 1
                    values_list.append(result)
                    result = 0
                    print("reset")
        
        #this one is created to cater yung mga nauna  (SUM OF SUM OF 3 AN 4 AN DIFF OF 3 AN 2)
        print(f"an_counter:{an_counter}")
        is_onelement = 0
        if an_counter == 1:
            is_onelement = 1
            an_counter = 2

        print(f"updated an_counter: {an_counter}")
        for i in range (an_counter):
            print(f"i: {i}")
            print(f"result: {result}")
            if operation_list[-(1+i)] == 'SUM OF':
                result = values_list[-(1+i)] + result   
            elif operation_list[-(1+i)] == 'DIFF OF':
                result = values_list[-(1+i)] - result 
            elif operation_list[-(1+i)] == 'PRODUKT OF':
                result = values_list[-(1+i)] * result                           
            elif operation_list[-(1+i)] == 'QUOSHUNT OF':
                result = values_list[-(1+i)] / result                  
            elif operation_list[-(1+i)] == 'MOD OF':
                result = values_list[-(1+i)] % result                      
            elif operation_list[-(1+i)] == 'BIGGR OF':
                if values_list[-(1+i)] > result:
                    result = values_list[-(1+i)]                       
            elif operation_list[-(1+i)] == 'SMALLR OF':
                if values_list[-(1+i)] < result:
                    result = values_list[-(1+i)]
            print(f"current i: {i}")
            print(f"current result:{result}")
            if is_onelement == 1:
                break

        print(f"operation list: {operation_list}")
        print(f"values list: {values_list}")
        print(f"result: {result}")
        print(f"isfloat : {is_float}")

        if is_float == False :
            semanticsResult = f"{int(result)}\n"
        else:
            semanticsResult = f"{result}\n"
        return semanticsResult
