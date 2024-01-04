import keywords
import syntax
import for_input
# import ui 


#this part is for the semantics of the arithmetic operations (SUM OF, DIFF OF, ETC.)
def arithmeticAnalyzer(varidents, arithmetic,lexeme): 
    # print(f'ARITHMETIC ANALYZER LEXEME: {lexeme}')           
    if lexeme[0][0] in arithmetic:
        remover_index = 0
        is_float = False
        # print(f"semantics lexeme sa arithmetic: {lexeme}")

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
        # print(lexeme)
        arithmetic_index = 0
        operation_list = []
        values_list = []
        result = 0
        an_counter = 0

        while arithmetic_index < len(lexeme):
            #THIS IS FOR CHECKING IF MAY KATABI BA SIYA OR WALA NA OPERATION
            # print(f"current lexeme sa arithemtic: {lexeme}")
            # print(f"currently pointed to: {lexeme[arithmetic_index][0]}")
            # print(f"varidents: {varidents}")
            if lexeme[arithmetic_index][0] in arithmetic:
                if lexeme[arithmetic_index+1][0] not in arithmetic:
                    if lexeme[arithmetic_index+3][0] not in arithmetic:
                        if lexeme[arithmetic_index][0] == 'SUM OF':
                            #this is created to cater the variables!!!
                            if lexeme[arithmetic_index+1][1] == 'Identifier' and lexeme[arithmetic_index+3][1] == 'Identifier':                                        
                                result = float(varidents[lexeme[arithmetic_index+1][0]])+float(varidents[lexeme[arithmetic_index+3][0]])
                            elif lexeme[arithmetic_index+1][1] == 'Identifier':
                                result = float(varidents[lexeme[arithmetic_index+1][0]])+float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'Identifier':
                                result = float(lexeme[arithmetic_index+1][0])+float(varidents[lexeme[arithmetic_index+3][0]])
                            #THIS ONE IS FOR THE TROOFS
                            elif lexeme[arithmetic_index+1][1] == 'TROOF Literal' and lexeme[arithmetic_index+3][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+1][0] == 'WIN' and lexeme[arithmetic_index+3][0] == 'WIN':
                                    result = float(1)+float(1)
                                elif lexeme[arithmetic_index+1][0] == 'WIN' and lexeme[arithmetic_index+3][0] == 'FAIL':
                                    result = float(1)+float(0)
                                elif lexeme[arithmetic_index+1][0] == 'FAIL' and lexeme[arithmetic_index+3][0] == 'WIN':
                                    result = float(0)+float(1)
                                elif lexeme[arithmetic_index+1][0] == 'FAIL' and lexeme[arithmetic_index+3][0] == 'FAIL':
                                    result = float(0)+float(0)
                            elif lexeme[arithmetic_index+1][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+1][0] == 'WIN':
                                    result = float(1)+float(lexeme[arithmetic_index+3][0])
                                else:
                                    result = float(0)+float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+3][0] == 'WIN':
                                    result =float(lexeme[arithmetic_index+1][0])+ float(1)
                                else:
                                    result = float(lexeme[arithmetic_index+1][0])+float(0)
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
                            #THIS ONE IS FOR THE TROOFS
                            elif lexeme[arithmetic_index+1][1] == 'TROOF Literal' and lexeme[arithmetic_index+3][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+1][0] == 'WIN' and lexeme[arithmetic_index+3][0] == 'WIN':
                                    result = float(1)-float(1)
                                elif lexeme[arithmetic_index+1][0] == 'WIN' and lexeme[arithmetic_index+3][0] == 'FAIL':
                                    result = float(1)-float(0)
                                elif lexeme[arithmetic_index+1][0] == 'FAIL' and lexeme[arithmetic_index+3][0] == 'WIN':
                                    result = float(0)-float(1)
                                elif lexeme[arithmetic_index+1][0] == 'FAIL' and lexeme[arithmetic_index+3][0] == 'FAIL':
                                    result = float(0)-float(0)
                            elif lexeme[arithmetic_index+1][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+1][0] == 'WIN':
                                    result = float(1)-float(lexeme[arithmetic_index+3][0])
                                else:
                                    result = float(0)-float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+3][0] == 'WIN':
                                    result =float(lexeme[arithmetic_index+1][0])-float(1)
                                else:
                                    result = float(lexeme[arithmetic_index+1][0])-float(0)
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
                            #THIS ONE IS FOR THE TROOFS
                            elif lexeme[arithmetic_index+1][1] == 'TROOF Literal' and lexeme[arithmetic_index+3][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+1][0] == 'WIN' and lexeme[arithmetic_index+3][0] == 'WIN':
                                    result = float(1)*float(1)
                                elif lexeme[arithmetic_index+1][0] == 'WIN' and lexeme[arithmetic_index+3][0] == 'FAIL':
                                    result = float(1)*float(0)
                                elif lexeme[arithmetic_index+1][0] == 'FAIL' and lexeme[arithmetic_index+3][0] == 'WIN':
                                    result = float(0)*float(1)
                                elif lexeme[arithmetic_index+1][0] == 'FAIL' and lexeme[arithmetic_index+3][0] == 'FAIL':
                                    result = float(0)*float(0)
                            elif lexeme[arithmetic_index+1][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+1][0] == 'WIN':
                                    result = float(1)*float(lexeme[arithmetic_index+3][0])
                                else:
                                    result = float(0)*float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+3][0] == 'WIN':
                                    result =float(lexeme[arithmetic_index+1][0])*float(1)
                                else:
                                    result = float(lexeme[arithmetic_index+1][0])*float(0)
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
                            #THIS ONE IS FOR THE TROOFS
                            elif lexeme[arithmetic_index+1][1] == 'TROOF Literal' and lexeme[arithmetic_index+3][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+1][0] == 'WIN' and lexeme[arithmetic_index+3][0] == 'WIN':
                                    result = float(1)/float(1)
                                elif lexeme[arithmetic_index+1][0] == 'WIN' and lexeme[arithmetic_index+3][0] == 'FAIL':
                                    result = float(1)/float(0)
                                elif lexeme[arithmetic_index+1][0] == 'FAIL' and lexeme[arithmetic_index+3][0] == 'WIN':
                                    result = float(0)/float(1)
                                elif lexeme[arithmetic_index+1][0] == 'FAIL' and lexeme[arithmetic_index+3][0] == 'FAIL':
                                    result = float(0)/float(0)
                            elif lexeme[arithmetic_index+1][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+1][0] == 'WIN':
                                    result = float(1)/float(lexeme[arithmetic_index+3][0])
                                else:
                                    result = float(0)/float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+3][0] == 'WIN':
                                    result =float(lexeme[arithmetic_index+1][0])/float(1)
                                else:
                                    result = float(lexeme[arithmetic_index+1][0])/float(0)
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
                            #THIS ONE IS FOR THE TROOFS
                            elif lexeme[arithmetic_index+1][1] == 'TROOF Literal' and lexeme[arithmetic_index+3][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+1][0] == 'WIN' and lexeme[arithmetic_index+3][0] == 'WIN':
                                    result = float(1)%float(1)
                                elif lexeme[arithmetic_index+1][0] == 'WIN' and lexeme[arithmetic_index+3][0] == 'FAIL':
                                    result = float(1)%float(0)
                                elif lexeme[arithmetic_index+1][0] == 'FAIL' and lexeme[arithmetic_index+3][0] == 'WIN':
                                    result = float(0)%float(1)
                                elif lexeme[arithmetic_index+1][0] == 'FAIL' and lexeme[arithmetic_index+3][0] == 'FAIL':
                                    result = float(0)%float(0)
                            elif lexeme[arithmetic_index+1][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+1][0] == 'WIN':
                                    result = float(1)%float(lexeme[arithmetic_index+3][0])
                                else:
                                    result = float(0)%float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+3][0] == 'WIN':
                                    result =float(lexeme[arithmetic_index+1][0])%float(1)
                                else:
                                    result = float(lexeme[arithmetic_index+1][0])%float(0)
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
                            #THIS ONE IS FOR THE TROOFS
                            elif lexeme[arithmetic_index+1][1] == 'TROOF Literal' and lexeme[arithmetic_index+3][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+1][0] == 'WIN' and lexeme[arithmetic_index+3][0] == 'WIN':
                                    result = float(1)
                                elif lexeme[arithmetic_index+1][0] == 'WIN' and lexeme[arithmetic_index+3][0] == 'FAIL':
                                    result = float(1)
                                elif lexeme[arithmetic_index+1][0] == 'FAIL' and lexeme[arithmetic_index+3][0] == 'WIN':
                                    result = float(1)
                                elif lexeme[arithmetic_index+1][0] == 'FAIL' and lexeme[arithmetic_index+3][0] == 'FAIL':
                                    result = float(0)
                            elif lexeme[arithmetic_index+1][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+1][0] == 'WIN':
                                    if  float(1) > float(lexeme[arithmetic_index+3][0]):
                                        result = float(1)
                                    else: 
                                        result = float(lexeme[arithmetic_index+3][0])
                                else:
                                    if  float(0) > float(lexeme[arithmetic_index+3][0]):
                                        result = float(0)
                                    else: 
                                        result = float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+3][0] == 'WIN':
                                    if float(lexeme[arithmetic_index+1][0]) < float(1):
                                        result = float(1)
                                    else:
                                        result = float(lexeme[arithmetic_index+1][0]) 
                                else:
                                    if float(lexeme[arithmetic_index+1][0]) < float(0):
                                        result = float(0)
                                    else:
                                        result = float(lexeme[arithmetic_index+1][0])
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
                            #THIS ONE IS FOR THE TROOFS
                            elif lexeme[arithmetic_index+1][1] == 'TROOF Literal' and lexeme[arithmetic_index+3][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+1][0] == 'WIN' and lexeme[arithmetic_index+3][0] == 'WIN':
                                    result = float(1)
                                elif lexeme[arithmetic_index+1][0] == 'WIN' and lexeme[arithmetic_index+3][0] == 'FAIL':
                                    result = float(0)
                                elif lexeme[arithmetic_index+1][0] == 'FAIL' and lexeme[arithmetic_index+3][0] == 'WIN':
                                    result = float(0)
                                elif lexeme[arithmetic_index+1][0] == 'FAIL' and lexeme[arithmetic_index+3][0] == 'FAIL':
                                    result = float(0)
                            elif lexeme[arithmetic_index+1][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+1][0] == 'WIN':
                                    if  float(1) < float(lexeme[arithmetic_index+3][0]):
                                        result = float(1)
                                    else: 
                                        result = float(lexeme[arithmetic_index+3][0])
                                else:
                                    if  float(0) < float(lexeme[arithmetic_index+3][0]):
                                        result = float(0)
                                    else: 
                                        result = float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+3][0] == 'WIN':
                                    if float(lexeme[arithmetic_index+1][0]) > float(1):
                                        result = float(1)
                                    else:
                                        result = float(lexeme[arithmetic_index+1][0]) 
                                else:
                                    if float(lexeme[arithmetic_index+1][0]) > float(0):
                                        result = float(0)
                                    else:
                                        result = float(lexeme[arithmetic_index+1][0])
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
                        # print(f"next current index is : {lexeme[arithmetic_index][0]}")
                        # print(f"current operation list: {operation_list}")
                        # print(f"current values list: {values_list}")
                else:
                    operation_list.append(lexeme[arithmetic_index][0])
                    arithmetic_index = arithmetic_index + 1
                # print(f"arithmetic_index:{arithmetic_index}")
                # print(f"len of lexeme: {len(lexeme)}")                            
            elif lexeme[arithmetic_index][0] == 'AN':
                if lexeme[arithmetic_index+1][0] not in arithmetic:
                    if operation_list[-1] == 'SUM OF':
                        if lexeme[arithmetic_index+1][1] == "Identifier":
                            result = result + float(varidents[lexeme[arithmetic_index+1][0]])
                        elif lexeme[arithmetic_index+1][1] == "TROOF Literal":
                            if lexeme[arithmetic_index+1][0] == 'WIN':
                                result = result + 1
                            else:
                                result = result + 0
                        else:
                            result = result + float(lexeme[arithmetic_index+1][0])
                    elif operation_list[-1] == 'DIFF OF':
                        if lexeme[arithmetic_index+1][1] == "Identifier":
                            result = result - float(varidents[lexeme[arithmetic_index+1][0]])
                        elif lexeme[arithmetic_index+1][1] == "TROOF Literal":
                            if lexeme[arithmetic_index+1][0] == 'WIN':
                                result = result - 1
                            else:
                                result = result - 0                        
                        else:
                            result = result - float(lexeme[arithmetic_index+1][0])
                    elif operation_list[-1] == 'PRODUKT OF':
                        if lexeme[arithmetic_index+1][1] == "Identifier":
                            result = result * float(varidents[lexeme[arithmetic_index+1][0]])
                        elif lexeme[arithmetic_index+1][1] == "TROOF Literal":
                            if lexeme[arithmetic_index+1][0] == 'WIN':
                                result = result * 1
                            else:
                                result = result * 0                        
                        else:
                            result = result * float(lexeme[arithmetic_index+1][0])
                    elif operation_list[-1] == 'QUOSHUNT OF':
                        if lexeme[arithmetic_index+1][1] == "Identifier":
                            result = result / float(varidents[lexeme[arithmetic_index+1][0]])
                        elif lexeme[arithmetic_index+1][1] == "TROOF Literal":
                            if lexeme[arithmetic_index+1][0] == 'WIN':
                                result = result / 1
                            else:
                                result = result / 0
                        else:
                            result = result / float(lexeme[arithmetic_index+1][0])
                    elif operation_list[-1] == 'MOD OF':
                        if lexeme[arithmetic_index+1][1] == "Identifier":
                            result = result % float(varidents[lexeme[arithmetic_index+1][0]])
                        elif lexeme[arithmetic_index+1][1] == "TROOF Literal":
                            if lexeme[arithmetic_index+1][0] == 'WIN':
                                result = result % 1
                            else:
                                result = result % 0
                        else:
                            result = result % float(lexeme[arithmetic_index+1][0])
                    elif operation_list[-1] == 'BIGGR OF':
                        if lexeme[arithmetic_index+1][1] == "Identifier":
                            if result < float(varidents[lexeme[arithmetic_index+1][0]]):
                                result = float(varidents[lexeme[arithmetic_index+1][0]])
                        elif lexeme[arithmetic_index+1][1] == "TROOF Literal":
                            if lexeme[arithmetic_index+1][0] == 'WIN':
                                if float(1) > result:
                                    result = float(1)
                            else:
                                if float(0) > result:
                                    result = float(0)
                        else:
                            if result < float(lexeme[arithmetic_index+1][0]):
                                result = float(lexeme[arithmetic_index+1][0])
                    elif operation_list[-1] == 'SMALLR OF':
                        if lexeme[arithmetic_index+1][1] == "Identifier":
                            if result > float(varidents[lexeme[arithmetic_index+1][0]]):  
                                result = float(varidents[lexeme[arithmetic_index+1][0]])
                        elif lexeme[arithmetic_index+1][1] == "TROOF Literal":
                            if lexeme[arithmetic_index+1][0] == 'WIN':
                                if float(1) < result:
                                    result = float(1)
                            else:
                                if float(0) < result:
                                    result = float(0)
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
                    # print("reset")
        
        #this one is created to cater yung mga nauna  (SUM OF SUM OF 3 AN 4 AN DIFF OF 3 AN 2)
        # print(f"an_counter:{an_counter}")
        is_onelement = 0
        if an_counter == 1:
            is_onelement = 1
            an_counter = 2

        # print(f"updated an_counter: {an_counter}")
        for i in range (an_counter):
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
            # print(f"current i: {i}")
            # print(f"current result:{result}")
            if is_onelement == 1:
                break

        # print(f"operation list: {operation_list}")
        # print(f"values list: {values_list}")
        # print(f"result: {result}")
        # print(f"isfloat : {is_float}")

        if is_float == False :
            semanticsResult = f"{int(result)}"
        else:
            semanticsResult = f"{result}"
        return semanticsResult

def booleanAnalyzer(thisLexeme, isInfinite):
    # print(thisLexeme)
    boolean_index = 0
    boolean_list = []
    boolean_operands = []
    while boolean_index < len(thisLexeme):
        # print(boolean_index, thisLexeme[boolean_index][0])
        if thisLexeme[boolean_index][0] in ['BOTH OF', 'EITHER OF', 'WON OF']:
            boolean_list.append(thisLexeme[boolean_index][0])
            if thisLexeme[boolean_index+1][1] == 'TROOF Literal':
                if thisLexeme[boolean_index+1][0] == 'WIN':
                    boolean_operands.append(f'WIN')
                elif thisLexeme[boolean_index+1][0] == 'FAIL':
                    boolean_operands.append(f'FAIL')
                elif varidents[thisLexeme[boolean_index+1][0]] != 'NOOB' or f'{int(float(thisLexeme[boolean_index+1][0]))}' != '0':
                    boolean_operands.append('WIN')
                else:
                    boolean_operands.append('FAIL')
            elif thisLexeme[boolean_index+1][1] == 'Identifier':
                if varidents[thisLexeme[boolean_index+1][0]] == 'WIN':
                    boolean_operands.append(f'WIN')
                elif varidents[thisLexeme[boolean_index+1][0]] == 'FAIL':
                    boolean_operands.append(f'FAIL')
                elif varidents[thisLexeme[boolean_index+1][0]] != 'NOOB' or f'{int(float(varidents[thisLexeme[boolean_index+1][0]]))}' != '0':
                    boolean_operands.append('WIN')
                else:
                    boolean_operands.append('FAIL')
            elif thisLexeme[boolean_index+1][0] in booleans:
                boolean_index += 1
                continue

            if thisLexeme[boolean_index+3][1] == 'TROOF Literal':
                if thisLexeme[boolean_index+3][0] == 'WIN':
                    boolean_operands.append(f'WIN')
                elif thisLexeme[boolean_index+3][0] == 'FAIL':
                    boolean_operands.append(f'FAIL')
                elif varidents[thisLexeme[boolean_index+3][0]] != 'NOOB' or f'{int(float(thisLexeme[boolean_index+3][0]))}' != '0':
                    boolean_operands.append('WIN')
                else:
                    boolean_operands.append('FAIL')
            elif thisLexeme[boolean_index+3][1] == 'Identifier':
                if varidents[thisLexeme[boolean_index+3][0]] == 'WIN':
                    boolean_operands.append(f'WIN')
                elif varidents[thisLexeme[boolean_index+3][0]] == 'FAIL':
                    boolean_operands.append(f'FAIL')
                elif varidents[thisLexeme[boolean_index+3][0]] != 'NOOB' or f'{int(float(varidents[thisLexeme[boolean_index+3][0]]))}' != '0':
                    boolean_operands.append('WIN')
                else:
                    boolean_operands.append('FAIL')
            elif thisLexeme[boolean_index+3][0] in booleans:
                boolean_index += 3
                continue
            boolean_index += 5
        elif thisLexeme[boolean_index][0] == 'NOT':
            if thisLexeme[boolean_index+1][1] == 'TROOF Literal':
                if thisLexeme[boolean_index+1][0] == 'WIN':
                    boolean_operands.append(f'FAIL')
                elif thisLexeme[boolean_index+1][0] == 'FAIL':
                    boolean_operands.append(f'WIN')
                elif varidents[thisLexeme[boolean_index+1][0]] != 'NOOB' or f'{int(float(thisLexeme[boolean_index+1][0]))}' != '0':
                    boolean_operands.append('FAIL')
                else:
                    boolean_operands.append('WIN')
            elif thisLexeme[boolean_index+1][1] == 'Identifier':
                if varidents[thisLexeme[boolean_index+1][0]] == 'WIN':
                    boolean_operands.append(f'FAIL')
                elif varidents[thisLexeme[boolean_index+1][0]] == 'FAIL':
                    boolean_operands.append(f'WIN')
                elif varidents[thisLexeme[boolean_index+1][0]] != 'NOOB' or f'{int(float(varidents[thisLexeme[boolean_index+1][0]]))}' != '0':
                    boolean_operands.append('FAIL')
                else:
                    boolean_operands.append('WIN')
            elif thisLexeme[boolean_index+1][0] in ['BOTH OF', 'EITHER OF', 'WON OF']:
                boolean_list.append('NOT')
                boolean_index += 1
                continue
            elif thisLexeme[boolean_index+1][0] == 'NOT':
                boolean_index += 2
                continue
            boolean_index += 3
        else:
            if thisLexeme[boolean_index][1] == 'TROOF Literal':
                if thisLexeme[boolean_index][0] == 'WIN':
                    boolean_operands.append(f'WIN')
                elif thisLexeme[boolean_index][0] == 'FAIL':
                    boolean_operands.append(f'FAIL')
                elif f'{int(float(thisLexeme[boolean_index][0]))}' != '0':
                    boolean_operands.append('WIN')
                else:
                    boolean_operands.append('FAIL')
            elif thisLexeme[boolean_index][1] == 'Identifier':
                if varidents[thisLexeme[boolean_index][0]] == 'WIN':
                    boolean_operands.append(f'WIN')
                elif varidents[thisLexeme[boolean_index][0]] == 'FAIL':
                    boolean_operands.append(f'FAIL')
                elif f'{int(float(varidents[thisLexeme[boolean_index][0]]))}' != '0':
                    boolean_operands.append('WIN')
                else:
                    boolean_operands.append('FAIL')
            boolean_index += 2

    answer = ''
    # print(boolean_list, boolean_operands)
    if len(boolean_list) == 0:
        answer = boolean_operands[0]
    else:
        for i in range(len(boolean_list)-1, -1, -1):
            if boolean_list[i] == 'BOTH OF':
                if boolean_operands[-1] == 'WIN' and boolean_operands[-2] == 'WIN':
                    answer = 'WIN'
                elif boolean_operands[-1] == 'FAIL' and boolean_operands[-2] == 'WIN':
                    answer = 'FAIL'
                elif boolean_operands[-1] == 'WIN' and boolean_operands[-2] == 'FAIL':
                    answer = 'FAIL'
                else:
                    answer = 'FAIL'
                boolean_operands.pop()
                boolean_operands.pop()
                boolean_operands.append(answer)
            elif boolean_list[i] == 'EITHER OF':
                if boolean_operands[-1] == 'WIN' and boolean_operands[-2] == 'WIN':
                    answer = 'WIN'
                elif boolean_operands[-1] == 'FAIL' and boolean_operands[-2] == 'WIN':
                    answer = 'WIN'
                elif boolean_operands[-1] == 'WIN' and boolean_operands[-2] == 'FAIL':
                    answer = 'WIN'
                else:
                    answer = 'FAIL'
                boolean_operands.pop()
                boolean_operands.pop()
                boolean_operands.append(answer)
            elif boolean_list[i] == 'WON OF':
                if boolean_operands[-1] == 'WIN' and boolean_operands[-2] == 'WIN':
                    answer = 'FAIL'
                elif boolean_operands[-1] == 'FAIL' and boolean_operands[-2] == 'WIN':
                    answer = 'WIN'
                elif boolean_operands[-1] == 'WIN' and boolean_operands[-2] == 'FAIL':
                    answer = 'WIN'
                else:
                    answer = 'FAIL'
                boolean_operands.pop()
                boolean_operands.pop()
                boolean_operands.append(answer)
            elif boolean_list[i] == 'NOT' and boolean_list[i+1] != 'NOT':
                if boolean_operands[-1] == 'WIN':
                    answer = 'FAIL'
                else:
                    answer = 'WIN'
                boolean_operands.pop()
                boolean_operands.append(answer)

    return answer

modified_varidents = {}
explicit_typecast = []
booleans = ['BOTH OF', 'EITHER OF', 'WON OF', 'NOT']
literals = ['NUMBR Literal', 'NUMBAR Literal', 'YARN Literal', 'TROOF Literal', 'Type Literal']
varidents = {}

def getExplicitTypecast(text):
    if syntax.syntax(text) == '>> No syntax errors.':
        semantics(text)
        return explicit_typecast

def getVaridents(text):
    if syntax.syntax(text) == '>> No syntax errors.':
        # print("pasok", modified_varidents)
        semantics(text)

        return modified_varidents
    return 0

def semantics(text):
    arithmetic = ['SUM OF','DIFF OF','PRODUKT OF', 'QUOSHUNT OF', 'MOD OF', 'BIGGR OF', 'SMALLR OF']
    semanticsResult = ''
    global varidents
    global explicit_typecast
    explicit_typecast.clear()
    modified_varidents.clear()
    varidents = syntax.getVaridents(text)
    # print(varidents)
    literals = ['NUMBR Literal', 'NUMBAR Literal', 'YARN Literal', 'TROOF Literal', 'Type Literal']
    comparison = ['BOTH SAEM', 'DIFFRINT']
    booleans = ['BOTH OF', 'EITHER OF', 'WON OF', 'NOT']
    # print(varidents)
    
    for h in range(0, len(text.splitlines())):
        lexeme = keywords.lex(text.splitlines()[h].lstrip().rstrip())
        if lexeme is not None:
            # print(f"lexeme: {lexeme}")
            if ['BTW', 'Comment Delimiter'] in lexeme:
                lexeme.pop(lexeme.index(['BTW', 'Comment Delimiter'])+1)
                lexeme.pop(lexeme.index(['BTW', 'Comment Delimiter']))
            
            # print(f"len(lexeme): {len(lexeme)}")
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
                ##INFINITE ARITY BOOLEAN SYNTAX - ALL OF
                elif lexeme[i][0] == 'ALL OF':
                    operands = []
                    parameters = []
                    result = []
                    standby_index = []
                    an_counter = 1
                    boolean_index = 1
                    while boolean_index <= len(lexeme)-2:
                        if lexeme[boolean_index][0] in ['BOTH OF', 'EITHER OF', 'WON OF']:
                            if lexeme[boolean_index+1][0] in ['BOTH OF', 'EITHER OF', 'WON OF']:
                                standby_index.append(boolean_index)
                                an_counter += 1
                                boolean_index += 1
                                continue
                            elif lexeme[boolean_index+1][0] == 'NOT':
                                standby_index.append(boolean_index)
                                boolean_index += 1
                                continue
                            if lexeme[boolean_index+3][0] in ['BOTH OF', 'EITHER OF', 'WON OF']:
                                an_counter += 1
                                boolean_index += 3
                                continue
                            elif lexeme[boolean_index+1][0] == 'NOT':
                                standby_index.append(boolean_index)
                                boolean_index += 1
                                continue
                            if lexeme[boolean_index+4][0] == 'AN' and len(standby_index) != 0:
                                standby_index.pop()
                                if len(standby_index) == 0:
                                    operands.append(an_counter)
                                    an_counter = 1
                            boolean_index += 5
                        elif lexeme[boolean_index][0] == 'NOT':
                            if lexeme[boolean_index+1][0] in ['BOTH OF', 'EITHER OF', 'WON OF']:
                                boolean_index += 1
                                continue
                            if lexeme[boolean_index+2][0] == 'AN' and len(standby_index) != 0:
                                standby_index.pop()
                                if len(standby_index) == 0:
                                    operands.append(an_counter)
                                    an_counter = 1
                            boolean_index += 3
                        elif lexeme[boolean_index][0] in varidents or lexeme[boolean_index][1] in literals:
                            operands.append(an_counter)
                            boolean_index += 2
                    lexeme = lexeme[1:]

                    isEnd = 0
                    for number_of_an in operands:
                        an = 0
                        boolean_index = 0
                        while an != number_of_an:
                            if lexeme[boolean_index][0] == 'AN':
                                an += 1
                            elif lexeme[boolean_index][0] == 'MKAY':
                                isEnd = 1
                                break
                            boolean_index += 1
                        if isEnd != 1:
                            if lexeme[0][0] in booleans:
                                if lexeme[0][0] in ["BOTH OF", "EITHER OF", "WON OF"]:
                                    parameters.append(lexeme[0:boolean_index+1])
                                    lexeme = lexeme[boolean_index+2:]
                                else:
                                    parameters.append(lexeme[0:boolean_index])
                                    lexeme = lexeme[boolean_index+1:]
                            else:
                                parameters.append(lexeme[0:boolean_index-1])
                                lexeme = lexeme[boolean_index:]
                        else:
                            parameters.append(lexeme[0:-1])
                    for operand in parameters:
                        if len(operand) != 1:
                            result.append(booleanAnalyzer(operand, 0))
                        else:
                            if operand[0][0] in varidents:
                                if varidents[operand[0][0]] in ['WIN', 'FAIL']:
                                    result.append(varidents[operand[0][0]])
                                elif f'{int(float(varidents[operand[0][0]]))}' != '0' or varidents[operand[0][0]] != 'NOOB':
                                    result.append('WIN')
                                else:
                                    result.append('FAIL')
                            else:
                                if operand in ['WIN', 'FAIL']:
                                    result.append(operand[0][0])
                                elif f'{int(float(operand[0][0]))}' != '0':
                                    result.append('WIN')
                                else:
                                    result.append('FAIL')
                    # print(result)
                    if 'FAIL' in result:
                        semanticsResult += f'FAIL\n'
                    else:
                        semanticsResult += f'WIN\n'
                    break
                ##INFINITE ARITY BOOLEAN SYNTAX - ANY OF
                elif lexeme[i][0] == 'ANY OF':
                    operands = []
                    parameters = []
                    result = []
                    standby_index = []
                    an_counter = 1
                    boolean_index = 1
                    while boolean_index <= len(lexeme)-2:
                        if lexeme[boolean_index][0] in ['BOTH OF', 'EITHER OF', 'WON OF']:
                            if lexeme[boolean_index+1][0] in ['BOTH OF', 'EITHER OF', 'WON OF']:
                                standby_index.append(boolean_index)
                                an_counter += 1
                                boolean_index += 1
                                continue
                            elif lexeme[boolean_index+1][0] == 'NOT':
                                standby_index.append(boolean_index)
                                boolean_index += 1
                                continue
                            if lexeme[boolean_index+3][0] in ['BOTH OF', 'EITHER OF', 'WON OF']:
                                an_counter += 1
                                boolean_index += 3
                                continue
                            elif lexeme[boolean_index+1][0] == 'NOT':
                                standby_index.append(boolean_index)
                                boolean_index += 1
                                continue
                            if lexeme[boolean_index+4][0] == 'AN' and len(standby_index) != 0:
                                standby_index.pop()
                                if len(standby_index) == 0:
                                    operands.append(an_counter)
                                    an_counter = 1
                            boolean_index += 5
                        elif lexeme[boolean_index][0] == 'NOT':
                            if lexeme[boolean_index+1][0] in ['BOTH OF', 'EITHER OF', 'WON OF']:
                                boolean_index += 1
                                continue
                            if lexeme[boolean_index+2][0] == 'AN' and len(standby_index) != 0:
                                standby_index.pop()
                                if len(standby_index) == 0:
                                    operands.append(an_counter)
                                    an_counter = 1
                            boolean_index += 3
                        elif lexeme[boolean_index][0] in varidents or lexeme[boolean_index][1] in literals:
                            operands.append(an_counter)
                            boolean_index += 2
                    lexeme = lexeme[1:]

                    isEnd = 0
                    for number_of_an in operands:
                        an = 0
                        boolean_index = 0
                        while an != number_of_an:
                            if lexeme[boolean_index][0] == 'AN':
                                an += 1
                            elif lexeme[boolean_index][0] == 'MKAY':
                                isEnd = 1
                                break
                            boolean_index += 1
                        if isEnd != 1:
                            if lexeme[0][0] in booleans:
                                if lexeme[0][0] in ["BOTH OF", "EITHER OF", "WON OF"]:
                                    parameters.append(lexeme[0:boolean_index+1])
                                    lexeme = lexeme[boolean_index+2:]
                                else:
                                    parameters.append(lexeme[0:boolean_index])
                                    lexeme = lexeme[boolean_index+1:]
                            else:
                                parameters.append(lexeme[0:boolean_index-1])
                                lexeme = lexeme[boolean_index:]
                        else:
                            parameters.append(lexeme[0:-1])
                    for operand in parameters:
                        if len(operand) != 1:
                            result.append(booleanAnalyzer(operand, 0))
                        else:
                            if operand[0][0] in varidents:
                                if varidents[operand[0][0]] in ['WIN', 'FAIL']:
                                    result.append(varidents[operand[0][0]])
                                elif f'{int(float(varidents[operand[0][0]]))}' != '0' or varidents[operand[0][0]] != 'NOOB':
                                    result.append('WIN')
                                else:
                                    result.append('FAIL')
                            else:
                                if operand in ['WIN', 'FAIL']:
                                    result.append(operand[0][0])
                                elif f'{int(float(operand[0][0]))}' != '0':
                                    result.append('WIN')
                                else:
                                    result.append('FAIL')
                    # print(result)
                    if 'WIN' in result:
                        semanticsResult += f'WIN\n'
                    else:
                        semanticsResult += f'FAIL\n'
                    break
                    
                elif lexeme[i][0] in booleans:
                    semanticsResult += f'{booleanAnalyzer(lexeme, 0)}\n'
                    break

                #THIS PART IS FOR THE COMPUTATIONS!!
                elif lexeme[i][0] in arithmetic:
                    semanticsResult += str(arithmeticAnalyzer(varidents,arithmetic,lexeme))
                    break #hindi ko alam baket nag break pa pero pag wala siya nag error shadkashdkadhaskhdahdsa
                
                #THIS IS TO CATER GIMMEH - ASKING USER FOR INPUT
                elif lexeme[i][0] == 'GIMMEH':
                    # resolved na :>>
                    input_value = for_input.get_user_input()
                    varidents[lexeme[i+1][0]] = str(input_value)
                    
                    semanticsResult += f"{lexeme[i+1][0]} is: {varidents[lexeme[i+1][0]]}\n"
                    modified_varidents[lexeme[i+1][0]] = str(input_value)
                    break
                    
                #R
                elif lexeme[i][0] == 'R':
                    if len(lexeme) == 3:
                        # print(varidents, lexeme[i-1][0], lexeme[i+1][0])
                        for j in varidents:
                            if lexeme[i-1][0] == j:
                                # print(lexeme[i+1][0])
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
                                    elif lexeme[i+1][0] in varidents:
                                        for k in varidents:
                                            if lexeme[i+1][0] == k:
                                                # print(k, varidents[k], lexeme[i-1][0])
                                                # print(k, varidents[k][0])
                                                varidents[lexeme[i-1][0]] = varidents[k]
                                                modified_varidents[lexeme[i-1][0]] = varidents[k]
                                                break
                                    else:
                                        varidents[j] = lexeme[i+1][0]
                                        # print(varidents)
                                        modified_varidents[lexeme[i-1][0]] = lexeme[i+1][0]
                                        
                                
                    elif len(lexeme) == 5:
                        # print(varidents)
                        for j in varidents:
                            if lexeme[i-1][0] == j:
                                if lexeme[i+1][0] == '"' and lexeme[i+3][0] == '"':
                                    varidents[j] = lexeme[i+2][0]
                                    modified_varidents[lexeme[i-1][0]] = str(lexeme[i+2][0])
                    else:
                        # print(lexeme[i+1][0])
                        if lexeme[i+1][0] == 'BOTH SAEM' or lexeme[i+1][0] == 'DIFFRINT':
                            for j in varidents:
                                if lexeme[i-1][0] == j:
                                    result = comparison_expression(lexeme[i+1:])
                                    if len(result) != 0:
                                        varidents[j] = result
                                        modified_varidents[lexeme[i-1][0]] = str(result)
                                        break
                                    break
                        elif lexeme[i+1][0] in booleans:
                            # fin_boolean_expression(lexeme) booleanAnalyzer(thisLexeme, isInfinite)
                            for j in varidents:
                                if lexeme[i-1][0] == j:
                                    # result = fin_boolean_expression(lexeme[i+1:])
                                    result = booleanAnalyzer(lexeme[i+1:], "no")
                                    # print(result)
                                    if len(result) != 0:
                                        varidents[j] = result
                                        modified_varidents[lexeme[i-1][0]] = str(result)
                                        break
                                    break
                        elif lexeme[i+1][0] == 'ANY OF' or lexeme[i+1][0] == 'ALL OF':
                            for j in varidents:
                                if lexeme[i-1][0] == j:
                                    # result = fin_boolean_expression(lexeme[i+1:])
                                    result = booleanAnalyzer(lexeme[i+1:], "yes")
                                    # print(result)
                                    if len(result) != 0:
                                        varidents[j] = result
                                        modified_varidents[lexeme[i-1][0]] = str(result)
                                        break
                                    break
                        elif lexeme[i+1][0] in arithmetic:
                            for j in varidents:
                                if lexeme[i-1][0] == j:
                                    # result = fin_boolean_expression(lexeme[i+1:])
                                    result = arithmeticAnalyzer(varidents, arithmetic,lexeme[i+1:])
                                    print(result)
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
                    visible_index = i + 1
                    temp_result = ""
                    #result = "uwu"
                    # print(f"i: {i}")
                    # print(f"current lexeme: {lexeme}")
                    # print(f"len(lexeme) sa visible: {len(lexeme)}")
                    # print(f"visible_index: {visible_index}")
                    #print(f"currently pointed to: {lexeme[visible_index]}")
                    while visible_index < len(lexeme):
                        #print(f"visible_index: {visible_index}")
                        #print(f"currently pointed to right now: {lexeme[visible_index]}")
                        if lexeme[visible_index][1] == 'String Delimiter':
                            temp_result += str(lexeme[visible_index+1][0])
                            visible_index +=3
                        elif lexeme[visible_index][1] == 'Output Delimiter':
                            visible_index +=1
                        elif lexeme[visible_index][0] in varidents:
                            temp_result += str(varidents[lexeme[visible_index][0]])
                            visible_index +=1
                        #this is for IT
                        elif lexeme[visible_index][0] == 'IT':
                            temp_result += str(keywords.get_IT())
                            visible_index+=1
                        elif lexeme[visible_index][0] in arithmetic:
                            #kunin ang lexeme until +
                            temp = []
                            temp_index = visible_index
                            # print(f"current lexeme: {lexeme}")
                            # print(f"temp_index: {temp_index}")
                            while temp_index < len(lexeme):
                                if lexeme[temp_index][1] == "Output Delimiter":
                                    break
                                else:
                                    # print(f"temp_index: {temp_index}")
                                    temp.append(lexeme[temp_index])
                                    temp_index+=1
                            # print(f"lexeme na ipapasa:{temp}")
                            temp_result += str(arithmeticAnalyzer(varidents,arithmetic,temp))
                            visible_index = temp_index
                            # print(f"temp result NA SA LOOB: {temp_result}")
                        #COMPARISON
                        elif lexeme[visible_index][0] in comparison:
                            #kunin ang lexeme until +
                            temp = []
                            temp_index = visible_index
                            # print(f"current lexeme sa comparison: {lexeme}")
                            # print(f"temp_index: {temp_index}")
                            while temp_index < len(lexeme):
                                if lexeme[temp_index][1] == "Output Delimiter":
                                    break
                                else:
                                    # print(f"temp_index: {temp_index}")
                                    temp.append(lexeme[temp_index])
                                    temp_index+=1
                            temp_result += str(comparison_expression(temp))
                            visible_index = temp_index

                        #BOOLEANS
                        elif lexeme[visible_index][0] in booleans:
                            #kunin ang lexeme until +
                            temp = []
                            temp_index = visible_index
                            # print(f"current lexeme sa booleans: {lexeme}")
                            # print(f"temp_index: {temp_index}")
                            while temp_index < len(lexeme):
                                if lexeme[temp_index][1] == "Output Delimiter":
                                    break
                                else:
                                    # print(f"temp_index: {temp_index}")
                                    temp.append(lexeme[temp_index])
                                    temp_index+=1
                            temp_result += str(fin_boolean_expression(temp))
                            visible_index = temp_index
                            # print(f"temp in booleans:{temp}")
                    semanticsResult += f"{temp_result}\n"
                    break
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

def convertFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    