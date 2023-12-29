import keywords
import syntax
import for_input
# import ui 

def semantics(text):
    arithmetic = ['SUM OF','DIFF OF','PRODUKT OF', 'QUOSHUNT OF', 'MOD OF', 'BIGGR OF', 'SMALLR OF']
    semanticsResult = ''
    varidents = syntax.getVaridents(text)
    for h in range(0, len(text.splitlines())):
        lexeme = keywords.lex(text.splitlines()[h].lstrip().rstrip())
        if lexeme is not None:
            print(f"lexeme: {lexeme}")
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

                #THIS PART IS FOR THE COMPUTATIONS!!
                elif lexeme[i][0] in arithmetic:
                    #tanggalin na muna yung string para hindi mahirapan mag add
                    
                    remover_index = 0
                    is_float = False

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
                        #THIS IS FOR CHECKING IF MAY KATABI BA SIYA OR WALA NA OPERATION
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
                    
                    #this one is created to cater yung mga nauna 
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
                        semanticsResult += f"{int(result)}\n"
                    else:
                        semanticsResult += f"{result}\n"
                    break

                #THIS IS TO CATER GIMMEH - ASKING USER FOR INPUT
                elif lexeme[i][0] == 'GIMMEH':
                    # #loop lang siya hanggang wala pang input si user! (do nothing)
                    # while ui.get_inputchecker() != 1:
                    #     #ui.get_inputchecker
                    #     print("hey")
                    # print("success")
                    # #dapat yung input_value ay yung value na nilagay ni user :<
                    # resolved na :>>
                    input_value = for_input.get_user_input()
                    varidents[lexeme[i+1][0]] = str(input_value)
                    semanticsResult += f"{lexeme[i+1][0]} is: {varidents[lexeme[i+1][0]]}\n"
            lexeme.clear()
    
    return semanticsResult