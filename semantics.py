import keywords
import syntax
import for_input
import math 
# import ui 


undefined_error = 0
noob_error = 0
#this part is for the semantics of the arithmetic operations (SUM OF, DIFF OF, ETC.)
def arithmeticAnalyzer(varidents, arithmetic,lexeme): 
    # print(f'ARITHMETIC ANALYZER LEXEME: {lexeme}')           
    if lexeme[0][0] in arithmetic:
        remover_index = 0
        is_float = False
        valid_checker = 0
        #this is created to remove the literal naming in lexeme and checking if it's a float or not
        while remover_index < len(lexeme):
            
            if lexeme[remover_index][1] == "String Delimiter":
                    lexeme.pop(remover_index)
                    remover_index = remover_index - 1
            elif lexeme[remover_index][1] == 'NUMBAR Literal' or lexeme[remover_index][1] == 'YARN Literal' or lexeme[remover_index][1] == 'Identifier':
                if lexeme[remover_index][1] == 'Identifier':
                    if varidents[lexeme[remover_index][0]] == 'NOOB':
                        valid_checker = 1
                        break
                    #THIS IS CREATED TO ENSURE THAT GIMME WILL NOT BE ACCEPTED HERE! 
                    elif str(varidents[lexeme[remover_index][0]]).isnumeric() == False:
                        try:
                            float_val = float(varidents[lexeme[remover_index][0]])
                            int_value = int(float_val)
                            if float_val != int_value:
                                is_float = True
                        except ValueError:
                            #end na!
                            valid_checker = 1
                            break
                    else:
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
        arithmetic_index = 0
        operation_list = []
        values_list = []
        result = 0
        an_counter = 0
        undefined_checker = 0 

        #if mag 1 ang valid_checker ay di na siya papasok sa while loop!! 
        if valid_checker == 1:
            result = "NOOBERROR"
            return result 


        while arithmetic_index < len(lexeme) and valid_checker == 0:
            #THIS IS FOR CHECKING IF MAY KATABI BA SIYA OR WALA NA OPERATION
            # print(f"current lexeme sa arithemtic: {lexeme}")
            # print(f"currently pointed to: {lexeme[arithmetic_index][0]}")
            # print(f"varidents: {varidents}")
            # OPERATOR OPERAND1 OPERAND2
            if lexeme[arithmetic_index][0] in arithmetic:
                #check 1ST OPERAND POSITION
                if lexeme[arithmetic_index+1][0] not in arithmetic:
                    #check THE 2ND OPERAND POSITION
                    if lexeme[arithmetic_index+3][0] not in arithmetic:
                        if lexeme[arithmetic_index][0] == 'SUM OF':
                            # print(lexeme[arithmetic_index+1][1], lexeme[arithmetic_index+1][0], float(varidents[lexeme[arithmetic_index+1][0]]),float(lexeme[arithmetic_index+3][0]) )
                            #this is created to cater the variables!!!
                            if (lexeme[arithmetic_index+1][1] == 'Identifier' or lexeme[arithmetic_index+1][1] == 'Variable Identifier') and (lexeme[arithmetic_index+3][1] == 'Identifier' or lexeme[arithmetic_index+3][1] == 'Variable Identifier'):                                        
                                result = float(varidents[lexeme[arithmetic_index+1][0]])+float(varidents[lexeme[arithmetic_index+3][0]])
                            elif lexeme[arithmetic_index+1][1] == 'Identifier' or lexeme[arithmetic_index+1][1] == 'Variable Identifier':
                                result = float(varidents[lexeme[arithmetic_index+1][0]])+float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'Identifier' or lexeme[arithmetic_index+3][1] == 'Variable Identifier':
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
                            if (lexeme[arithmetic_index+1][1] == 'Identifier' or lexeme[arithmetic_index+1][1] == 'Variable Identifier') and (lexeme[arithmetic_index+3][1] == 'Identifier' or lexeme[arithmetic_index+3][1] == 'Variable Identifier'):                                        
                                result = float(varidents[lexeme[arithmetic_index+1][0]])-float(varidents[lexeme[arithmetic_index+3][0]])
                            elif lexeme[arithmetic_index+1][1] == 'Identifier' or lexeme[arithmetic_index+1][1] == 'Variable Identifier':
                                result = float(varidents[lexeme[arithmetic_index+1][0]])-float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'Identifier' or lexeme[arithmetic_index+3][1] == 'Variable Identifier':
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
                            if (lexeme[arithmetic_index+1][1] == 'Identifier' or lexeme[arithmetic_index+1][1] == 'Variable Identifier') and (lexeme[arithmetic_index+3][1] == 'Identifier' or lexeme[arithmetic_index+3][1] == 'Variable Identifier'):                                        
                                result = float(varidents[lexeme[arithmetic_index+1][0]])*float(varidents[lexeme[arithmetic_index+3][0]])
                            elif lexeme[arithmetic_index+1][1] == 'Identifier' or lexeme[arithmetic_index+1][1] == 'Variable Identifier':
                                result = float(varidents[lexeme[arithmetic_index+1][0]])*float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'Identifier' or lexeme[arithmetic_index+3][1] == 'Variable Identifier':
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
                            if (lexeme[arithmetic_index+1][1] == 'Identifier' or lexeme[arithmetic_index+1][1] == 'Variable Identifier') and (lexeme[arithmetic_index+3][1] == 'Identifier' or lexeme[arithmetic_index+3][1] == 'Variable Identifier'):
                                if math.ceil(float(varidents[lexeme[arithmetic_index+3][0]])) == 0 or varidents[lexeme[arithmetic_index+3][0]] == '0':
                                    undefined_checker = 1
                                    break
                                else:                                        
                                    result = float(varidents[lexeme[arithmetic_index+1][0]]) / float(varidents[lexeme[arithmetic_index+3][0]])
                            elif lexeme[arithmetic_index+1][1] == 'Identifier' or lexeme[arithmetic_index+1][1] == 'Variable Identifier':
                                result = float(varidents[lexeme[arithmetic_index+1][0]]) / float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'Identifier' or lexeme[arithmetic_index+3][1] == 'Variable Identifier':
                                if math.ceil(float(varidents[lexeme[arithmetic_index+3][0]])) == 0 or varidents[lexeme[arithmetic_index+3][0]] == '0':
                                    undefined_checker = 1
                                    break
                                else:  
                                    result = float(lexeme[arithmetic_index+1][0]) / float(varidents[lexeme[arithmetic_index+3][0]])
                            #THIS ONE IS FOR THE TROOFS
                            elif lexeme[arithmetic_index+1][1] == 'TROOF Literal' and lexeme[arithmetic_index+3][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+1][0] == 'WIN' and lexeme[arithmetic_index+3][0] == 'WIN':
                                    result = float(1)/float(1)
                                elif lexeme[arithmetic_index+1][0] == 'WIN' and lexeme[arithmetic_index+3][0] == 'FAIL':
                                    undefined_checker = 1
                                    break
                                elif lexeme[arithmetic_index+1][0] == 'FAIL' and lexeme[arithmetic_index+3][0] == 'WIN':
                                    result = float(0)/float(1)
                                elif lexeme[arithmetic_index+1][0] == 'FAIL' and lexeme[arithmetic_index+3][0] == 'FAIL':
                                    undefined_checker = 1
                                    break
                            elif lexeme[arithmetic_index+1][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+1][0] == 'WIN':
                                    result = float(1)/float(lexeme[arithmetic_index+3][0])
                                else:
                                    result = float(0)/float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'TROOF Literal':
                                if lexeme[arithmetic_index+3][0] == 'WIN':
                                    result =float(lexeme[arithmetic_index+1][0])/float(1)
                                else:
                                    undefined_checker = 1
                                    break 
                            else:
                                if math.ceil(float(lexeme[arithmetic_index+3][0])) == 0 or lexeme[arithmetic_index+3][0] == "0":
                                    undefined_checker = 1
                                    break 
                                else:
                                    result = float(lexeme[arithmetic_index+1][0]) / float(lexeme[arithmetic_index+3][0])
                        elif lexeme[arithmetic_index][0] == 'MOD OF':
                            #this is created to cater the variables!!!
                            if (lexeme[arithmetic_index+1][1] == 'Identifier' or lexeme[arithmetic_index+1][1] == 'Variable Identifier') and (lexeme[arithmetic_index+3][1] == 'Identifier' or lexeme[arithmetic_index+3][1] == 'Variable Identifier'):                                        
                                result = float(varidents[lexeme[arithmetic_index+1][0]]) % float(varidents[lexeme[arithmetic_index+3][0]])
                            elif lexeme[arithmetic_index+1][1] == 'Identifier' or lexeme[arithmetic_index+1][1] == 'Variable Identifier':
                                result = float(varidents[lexeme[arithmetic_index+1][0]]) % float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'Identifier' or lexeme[arithmetic_index+3][1] == 'Variable Identifier':
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
                            if (lexeme[arithmetic_index+1][1] == 'Identifier' or lexeme[arithmetic_index+1][1] == 'Variable Identifier') and (lexeme[arithmetic_index+3][1] == 'Identifier' or lexeme[arithmetic_index+3][1] == 'Variable Identifier'):
                                if float(varidents[lexeme[arithmetic_index+1][0]]) > float(varidents[lexeme[arithmetic_index+3][0]]):
                                    result = float(varidents[lexeme[arithmetic_index+1][0]])
                                else:
                                    result = float(varidents[lexeme[arithmetic_index+3][0]])
                            elif lexeme[arithmetic_index+1][1] == 'Identifier' or lexeme[arithmetic_index+1][1] == 'Variable Identifier':
                                if float(varidents[lexeme[arithmetic_index+1][0]]) > float(lexeme[arithmetic_index+3][0]):
                                    result = float(varidents[lexeme[arithmetic_index+1][0]])
                                else:
                                    result = float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'Identifier' or lexeme[arithmetic_index+3][1] == 'Variable Identifier':
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
                            if (lexeme[arithmetic_index+1][1] == 'Identifier' or lexeme[arithmetic_index+1][1] == 'Variable Identifier') and (lexeme[arithmetic_index+3][1] == 'Identifier' or lexeme[arithmetic_index+3][1] == 'Variable Identifier'):
                                if float(varidents[lexeme[arithmetic_index+1][0]]) < float(varidents[lexeme[arithmetic_index+3][0]]):
                                    result = float(varidents[lexeme[arithmetic_index+1][0]])
                                else:
                                    result = float(varidents[lexeme[arithmetic_index+3][0]])
                            elif lexeme[arithmetic_index+1][1] == 'Identifier' or lexeme[arithmetic_index+1][1] == 'Variable Identifier':
                                if float(varidents[lexeme[arithmetic_index+1][0]]) < float(lexeme[arithmetic_index+3][0]):
                                    result = float(varidents[lexeme[arithmetic_index+1][0]])
                                else:
                                    result = float(lexeme[arithmetic_index+3][0])
                            elif lexeme[arithmetic_index+3][1] == 'Identifier' or lexeme[arithmetic_index+3][1] == 'Variable Identifier':
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
                        # print(f"lexeme[arithmetic_index+1][0]]: {lexeme[arithmetic_index+1][0]}")
                        # print(f"varidents:{varidents}")
                        if lexeme[arithmetic_index+1][0] in varidents:
                            values_list.append(float(varidents[lexeme[arithmetic_index+1][0]]))
                        else:
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
                        if lexeme[arithmetic_index+1][1] == "Identifier" or lexeme[arithmetic_index+1][1] == "Variable Identifier":
                            result = result + float(varidents[lexeme[arithmetic_index+1][0]])
                        elif lexeme[arithmetic_index+1][1] == "TROOF Literal":
                            if lexeme[arithmetic_index+1][0] == 'WIN':
                                result = result + 1
                            else:
                                result = result + 0
                        else:
                            result = result + float(lexeme[arithmetic_index+1][0])
                    elif operation_list[-1] == 'DIFF OF':
                        if lexeme[arithmetic_index+1][1] == "Identifier" or lexeme[arithmetic_index+1][1] == "Variable Identifier":
                            result = result - float(varidents[lexeme[arithmetic_index+1][0]])
                        elif lexeme[arithmetic_index+1][1] == "TROOF Literal":
                            if lexeme[arithmetic_index+1][0] == 'WIN':
                                result = result - 1
                            else:
                                result = result - 0                        
                        else:
                            result = result - float(lexeme[arithmetic_index+1][0])
                    elif operation_list[-1] == 'PRODUKT OF':
                        if lexeme[arithmetic_index+1][1] == "Identifier" or lexeme[arithmetic_index+1][1] == "Variable Identifier":
                            result = result * float(varidents[lexeme[arithmetic_index+1][0]])
                        elif lexeme[arithmetic_index+1][1] == "TROOF Literal":
                            if lexeme[arithmetic_index+1][0] == 'WIN':
                                result = result * 1
                            else:
                                result = result * 0                        
                        else:
                            result = result * float(lexeme[arithmetic_index+1][0])
                    elif operation_list[-1] == 'QUOSHUNT OF':
                        if lexeme[arithmetic_index+1][1] == "Identifier" or lexeme[arithmetic_index+1][1] == "Variable Identifier":
                            #check if 0 ba siya 
                            if math.ceil(float(varidents[arithmetic_index+1][0])) == 0 or varidents[arithmetic_index+1][0] == "0":
                                undefined_checker = 1
                                break
                            else:
                                result = result / float(varidents[lexeme[arithmetic_index+1][0]])
                        elif lexeme[arithmetic_index+1][1] == "TROOF Literal":
                            if lexeme[arithmetic_index+1][0] == 'WIN':
                                result = result / 1
                            else:
                                undefined_checker = 1
                                break 
                        else:
                            result = result / float(lexeme[arithmetic_index+1][0])
                    elif operation_list[-1] == 'MOD OF':
                        if lexeme[arithmetic_index+1][1] == "Identifier" or lexeme[arithmetic_index+1][1] == "Variable Identifier":
                            result = result % float(varidents[lexeme[arithmetic_index+1][0]])
                        elif lexeme[arithmetic_index+1][1] == "TROOF Literal":
                            if lexeme[arithmetic_index+1][0] == 'WIN':
                                result = result % 1
                            else:
                                result = result % 0
                        else:
                            result = result % float(lexeme[arithmetic_index+1][0])
                    elif operation_list[-1] == 'BIGGR OF':
                        if lexeme[arithmetic_index+1][1] == "Identifier" or lexeme[arithmetic_index+1][1] == "Variable Identifier":
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
                        if lexeme[arithmetic_index+1][1] == "Identifier" or lexeme[arithmetic_index+1][1] == "Variable Identifier":
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
                if math.ceil(float(values_list[-(1+i)])) == 0:
                    undefined_checker = 1
                    break
                else:
                    result = values_list[-(1+i)] / result                  
            elif operation_list[-(1+i)] == 'MOD OF':
                result = values_list[-(1+i)] % result                      
            elif operation_list[-(1+i)] == 'BIGGR OF':
                if values_list[-(1+i)] > result:
                    result = values_list[-(1+i)]                       
            elif operation_list[-(1+i)] == 'SMALLR OF':
                if values_list[-(1+i)] < result:
                    result = values_list[-(1+i)]
            if is_onelement == 1:
                break

        #check if may undefined result
        if undefined_checker == 1:
            result = "UNDEFINEDERROR"
            return result
        #proceed to checking if float or int
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

def infiniteBooleanAnalyzer(lexeme, keyword):
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

    if keyword == 'ANY OF':
        if 'WIN' in result:
            return f'WIN'
        else:
            return f'FAIL'
    else:
        if 'FAIL' in result:
            return f'FAIL'
        else:
            return f'WIN'

def concatenationAnalyzer(lexeme):
    concat = []
    result = ''
    start_index = 1
    while start_index <= len(lexeme)-1:
        if lexeme[start_index][1] in literals or lexeme[start_index][1] == 'String Delimiter':
            if lexeme[start_index][1] in literals:
                concat.append(lexeme[start_index][0])
                start_index += 1
            else:
                concat.append(lexeme[start_index][0])
                start_index += 3
        elif lexeme[start_index][0] in varidents:
            concat.append(varidents[lexeme[start_index][0]])
            start_index += 1
        
        if start_index <= len(lexeme)-1:
            if lexeme[start_index][0] == 'AN':
                start_index += 1
        
    for operand in concat:
        result += str(operand)
    
    return result

isInCondition = -1      # -1 means unused
conditionFlag = -1
omgwtfFlag = -1
gtfoFlag = -1
nowaiFlag = -1
isInFunction = -1
isLoops = -1
loopOut = -1
functionBody = ''
currentFunction = ''
functions = {}
modified_varidents = {}
loopDone = -1
loops = {}
loopsLabel = ''
loopsOperation = ''
loopsVar = ''
loopsCondition = ''
loopsExpression = ''
loopsBody = []
loopStatement = ''
# loopsCodeBlock = []

temp_res = []
explicit_typecast = []
booleans = ['BOTH OF', 'EITHER OF', 'WON OF', 'NOT']
literals = ['NUMBR Literal', 'NUMBAR Literal', 'YARN Literal', 'TROOF Literal', 'Type Literal']
varidents = {}


# def getExplicitTypecast(text):
#     if syntax.syntax(text) == '>> No syntax errors.':
#         semantics(text)
#         print('>>>>', modified_varidents, explicit_typecast)
#         return explicit_typecast

# def getVaridents(text):
#     if syntax.syntax(text) == '>> No syntax errors.':
#         # print("pasok", modified_varidents)
#         semantics(text)
#         print(modified_varidents)
#         return modified_varidents
#     return 0

# def getVisibleValue(text):
#     if syntax.syntax(text) == '>> No syntax errors.':
#         # print("pasok", modified_varidents)
#         semantics(text)
#         print('>>>:', temp_res)
#         return temp_res
#     return 0

def functionExecute(text, parameters):
    global varidents
    comparison = ['BOTH SAEM', 'DIFFRINT']
    booleans = ['BOTH OF', 'EITHER OF', 'WON OF', 'NOT']
    arithmetic = ['SUM OF','DIFF OF','PRODUKT OF', 'QUOSHUNT OF', 'MOD OF', 'BIGGR OF', 'SMALLR OF']
    infinitebooleans = ['ANY OF', "ALL OF"]
    IT = []
    for h in range(0, len(text.splitlines())):
        lexeme = keywords.lex(text.splitlines()[h].lstrip().rstrip())
        if lexeme is not None:
            for i in range(0, len(lexeme)):    
                if lexeme[i][0] == 'VISIBLE':
                    # print(f"lexeme:{lexeme}")
                    visible_index = i + 1
                    temp_result = ""
                    while visible_index < len(lexeme):
                        #print(f"visible_index: {visible_index}")
                        #print(f"currently pointed to right now: {lexeme[visible_index]}")
                        print(lexeme[visible_index][0], parameters, '<<<<<<<<<<<<<<<<>>>>>>>>>>')
                        if lexeme[visible_index][1] == 'String Delimiter':
                            temp_result += str(lexeme[visible_index+1][0])
                            visible_index +=3
                        elif lexeme[visible_index][1] == 'Output Delimiter':
                            visible_index +=1
                        elif lexeme[visible_index][0] in parameters:
                            temp_result += str(parameters[lexeme[visible_index][0]])
                            visible_index +=1
                        #this is for IT
                        elif lexeme[visible_index][0] == 'IT':
                            temp_result += str(keywords.get_IT())
                            visible_index+=1
                        #THIS IS FOR THE TROOF LITERAL
                        elif lexeme[visible_index][1] == 'TROOF Literal':
                            temp_result += str(lexeme[visible_index][0])
                            visible_index+=1
                        #THIS IS FOR GETTING THE NUMBR
                        elif lexeme[visible_index][1] == 'NUMBAR Literal':
                            temp_result += str(lexeme[visible_index][0])
                            visible_index+=1
                        #FOR GETTING THE NUMBAR
                        elif lexeme[visible_index][1] == 'NUMBR Literal':
                            temp_result += str(lexeme[visible_index][0])
                            visible_index+=1
                        elif lexeme[visible_index][0] in arithmetic:
                            #kunin ang lexeme until +
                            temp = []
                            temp_index = visible_index
                            while temp_index < len(lexeme):
                                if lexeme[temp_index][1] == "Output Delimiter":
                                    break
                                else:
                                    temp.append(lexeme[temp_index])
                                    temp_index+=1
                            arithmeticresult = str(arithmeticAnalyzer(parameters,arithmetic,temp)) 
                            temp_result += arithmeticresult
                            visible_index = temp_index
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
                            while temp_index < len(lexeme):
                                if lexeme[temp_index][1] == "Output Delimiter":
                                    break
                                else:
                                    temp.append(lexeme[temp_index])
                                    temp_index+=1
                            temp_result += str(booleanAnalyzer(temp, 0))
                            visible_index = temp_index
                        #INFINITE BOOLEANS
                        elif lexeme[visible_index][0] in infinitebooleans:
                            #kunin ang lexeme until +
                            temp = []
                            temp_index = visible_index
                            while temp_index < len(lexeme):
                                if lexeme[temp_index][1] == "Output Delimiter":
                                    break
                                else:
                                    temp.append(lexeme[temp_index])
                                    temp_index+=1
                            temp_result += str(infiniteBooleanAnalyzer(temp, lexeme[visible_index][0]))
                            visible_index = temp_index
                        elif lexeme[visible_index][0] == 'SMOOSH':
                            #kunin ang lexeme until +
                            temp = []
                            temp_index = visible_index
                            while temp_index < len(lexeme):
                                if lexeme[temp_index][1] == "Output Delimiter":
                                    break
                                else:
                                    temp.append(lexeme[temp_index])
                                    temp_index+=1
                            temp_result += str(concatenationAnalyzer(lexeme[i+1:]))
                            visible_index = temp_index
                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ "{temp_result}"', 1)
                    # temp_res.append(temp_result)
                    # print("temp_res:", temp_res)
                    print('ito ang current result', temp_result)
                    print('ito ang current result',varidents)
                    varidents['IT'] = temp_result
                    print('ito ang current ipapasa',varidents)
                    IT.append(temp_result)
                    break
                elif lexeme[i][0] == 'FOUND YR':
                    #-- BOTH SAEM AND DIFFRINT WITH VARIDENTS
                    if lexeme[i][0] == 'BOTH SAEM' or lexeme[i][0] == 'DIFFRINT':
                        result = comparison_expression(lexeme[i+1:])
                        varidents['IT'] = result
                    
                    ##INFINITE ARITY BOOLEAN SYNTAX - ANY OF
                    elif lexeme[i][0] == 'ANY OF' or lexeme[i][0] == 'ALL OF':
                        result = infiniteBooleanAnalyzer(lexeme[i+2:], "ALL OF")
                        varidents['IT'] = result
                        
                    elif lexeme[i][0] in booleans:
                        result = infiniteBooleanAnalyzer(lexeme[i+2:], "ANY OF")
                        varidents['IT'] = result

                    #THIS PART IS FOR THE COMPUTATIONS!!
                    elif lexeme[i][0] in arithmetic:
                        arithmeticresult = str(arithmeticAnalyzer(parameters,arithmetic,lexeme[i+1:]))
                        varidents['IT'] = result
                    return IT
                elif lexeme[i][0] == 'GTFO':
                    return IT

def semantics(text):
    print(text, 'ito ang text anu baaaaa')
    # print("<<<<,>>>>>>>")
    # print(text, "\n\n\n")
    arithmetic = ['SUM OF','DIFF OF','PRODUKT OF', 'QUOSHUNT OF', 'MOD OF', 'BIGGR OF', 'SMALLR OF']
    semanticsResult = ''
    # global modified_varidents
    global varidents
    global explicit_typecast
    global undefined_error
    global noob_error
    global temp_res
    global isInCondition
    global conditionFlag
    global omgwtfFlag
    global gtfoFlag
    global nowaiFlag
    global isInFunction
    global isLoops
    global functionBody
    global functions
    global currentFunction
    global loops
    global loopsBody
    global loopsCondition
    global loopsExpression
    global loopsLabel
    global loopsOperation
    global loopsVar
    global loopDone
    global loopStatement
    # global loops
   

    varidents = {'IT': 'NOOB'}
    # temp_res.clear()
    # temp_res = ""
    temp_list = []

    temp_varident = syntax.getVaridents(text)
    for key in temp_varident:
        varidents[key] = temp_varident[key]
    # print(varidents)
    literals = ['NUMBR Literal', 'NUMBAR Literal', 'YARN Literal', 'TROOF Literal', 'Type Literal']
    comparison = ['BOTH SAEM', 'DIFFRINT']
    booleans = ['BOTH OF', 'EITHER OF', 'WON OF', 'NOT']
    infinitebooleans = ['ANY OF', "ALL OF"]
    outsideWazzup = 0
    # print(varidents)
    undefined_error_prompt =  "\n>> ZeroDivisionError: Result will have an undefined due to 0.\n"
    noob_error_prompt = "\n>> SyntaxError near line <{h}>: \n\tVariable Identifier to be used in arithmetic operations should not be empty and should be numeric only!"
    #undefined_error = 0
    parameter_list = {}
    for h in range(0, len(text.splitlines())):
        lexeme = keywords.lex(text.splitlines()[h].lstrip().rstrip())
        if undefined_error == 1 or noob_error:
            undefined_error = 0
            noob_error = 0
            return [None,'', varidents]
        
        if lexeme is not None:
            # print(f"lexeme: {lexeme}")
            if ['BTW', 'Comment Delimiter'] in lexeme:
                lexeme.pop(lexeme.index(['BTW', 'Comment Delimiter'])+1)
                lexeme.pop(lexeme.index(['BTW', 'Comment Delimiter']))
            if conditionFlag == 0 and omgwtfFlag == 1 and lexeme[0][0] != 'OMGWTF':     # para sa mga statements na hindi ieexecute sa if else at switch case
                continue
            elif conditionFlag == 1 and gtfoFlag == 1 and lexeme[0][0] != 'OIC':
                continue
            elif conditionFlag == 0 and nowaiFlag == 1:
                if len(lexeme) != 2 or lexeme[0][0] != 'NO' or lexeme[1][0] != 'WAI':
                    continue
            elif conditionFlag == 1 and nowaiFlag == 0 and lexeme[0][0] != 'OIC':
                continue 
            # print('><><><><><', lexeme, "loop: ",isLoops)
            if isInFunction == 1:
                if lexeme[0][0] != 'IF' or lexeme[1][0] != 'U' or lexeme[2][0] != 'SAY' or lexeme[3][0] != 'SO':
                    functionBody += f'{text.splitlines()[h]}\n'
                    print('CURRENT FUNCTION BODY ><><><><', functionBody)
                    continue

            # print(lexeme, '<<<<<<<<<<<<<<<<<')
            # print(f"len(lexeme): {len(lexeme)}")
            for i in range(0, len(lexeme)):   
                # print("\nkeyword:",lexeme[i][0], "\n")  
                # if lexeme[i][1] == "Loop Keyword":
                #     print(f"\n\nLOOP KEYWORD: {lexeme[i][0]}\n\n")   
                # if isLoops == 0 and lexeme[i][1] != 'Loop Keyword':
                #     print(lexeme[i])
                    # loopsBody.append(lexeme[i:])        
                if lexeme[i][0] == 'BUHBYE':
                    outsideWazzup = 1
                    break
                if lexeme[i][0] == 'I HAS A':
                    if outsideWazzup == 1:
                        if len(lexeme) == 4:
                            varidents[lexeme[i+1][0]] = lexeme[i+3][0]
                        elif len(lexeme) > 4:
                            varidents[lexeme[i+1][0]] = lexeme[i+4][0]
                    break
                #-- BOTH SAEM AND DIFFRINT WITH VARIDENTS
                if lexeme[i][0] == 'BOTH SAEM' or lexeme[i][0] == 'DIFFRINT':
                    result = comparison_expression(lexeme)
                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {result}', 1)
                    return ['', text, varidents]
                
                ##INFINITE ARITY BOOLEAN SYNTAX - ANY OF
                elif lexeme[i][0] == 'ANY OF' or lexeme[i][0] == 'ALL OF':
                    result = infiniteBooleanAnalyzer(lexeme[i+1:], "ALL OF")
                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {result}', 1)
                    return ['', text, varidents]
                    
                elif lexeme[i][0] in booleans:
                    result = infiniteBooleanAnalyzer(lexeme[i+1:], "ANY OF")
                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {result}', 1)
                    return ['', text, varidents]

                #THIS PART IS FOR THE COMPUTATIONS!!
                elif lexeme[i][0] in arithmetic:
                    arithmeticresult = str(arithmeticAnalyzer(varidents,arithmetic,lexeme))
                    # print(f"arithmetic result:{arithmeticresult}")
                    if arithmeticresult == "NOOBERROR":
                        temp_result += noob_error_prompt
                        noob_error = 1
                        break 
                    if arithmeticresult == "UNDEFINEDERROR":
                        temp_result += undefined_error_prompt
                        undefined_error = 1
                        # print("UNDEFINEDERROR1")
                        break
                    else:
                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {arithmeticresult}', 1)
                        return [arithmeticresult, text, varidents]
                        break #hindi ko alam baket nag break pa pero pag wala siya nag error shadkashdkadhaskhdahdsa
                
                #THIS IS TO CATER GIMMEH - ASKING USER FOR INPUT
                elif lexeme[i][0] == 'GIMMEH':
                    # resolved na :>>
                    input_value = for_input.get_user_input()
                    varidents[lexeme[i+1][0]] = str(input_value)
                    modified_varidents[lexeme[i+1][0]] = str(input_value)
                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i+1][0]} ITZ {input_value}', 1)
                    return [f'{input_value}\n', text, varidents]
                    
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
                                                text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {varidents[k]}', 1)
                                                return [f'', text, varidents]     
                                    else:
                                        varidents[j] = lexeme[i+1][0]
                                        # print(varidents)
                                        modified_varidents[lexeme[i-1][0]] = lexeme[i+1][0]  
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {varidents[j]}', 1)
                                        return [f'', text, varidents]              
                                
                    elif len(lexeme) == 5 and lexeme[i+1][0] != 'MAEK':
                        # print(varidents)
                        for j in varidents:
                            if lexeme[i-1][0] == j:
                                if lexeme[i+1][0] == '"' and lexeme[i+3][0] == '"':
                                    varidents[j] = lexeme[i+2][0]
                                    modified_varidents[lexeme[i-1][0]] = str(lexeme[i+2][0])
                                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {j} ITZ {lexeme[i+2][0]}', 1)
                                    return [f'', text, varidents]  
                    else:
                        if lexeme[i+1][0] == 'BOTH SAEM' or lexeme[i+1][0] == 'DIFFRINT':
                            for j in varidents:
                                if lexeme[i-1][0] == j:
                                    result = comparison_expression(lexeme[i+1:])
                                    if len(result) != 0:
                                        varidents[j] = result
                                        modified_varidents[lexeme[i-1][0]] = str(result)
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {j} ITZ {result}', 1)
                                        return [f'', text, varidents] 
                                        
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
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {j} ITZ {result}', 1)
                                        return [f'', text, varidents] 
                                        
                        elif lexeme[i+1][0] == 'ANY OF':
                            for j in varidents:
                                if lexeme[i-1][0] == j:
                                    # result = fin_boolean_expression(lexeme[i+1:])
                                    result = infiniteBooleanAnalyzer(lexeme[i+1:], "ANY OF")
                                    # print(result)
                                    if len(result) != 0:
                                        varidents[j] = result
                                        modified_varidents[lexeme[i-1][0]] = str(result)
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {j} ITZ {result}', 1)
                                        return [f'', text, varidents] 
                                        
                        elif lexeme[i+1][0] == 'SMOOSH':
                            for j in varidents:
                                if lexeme[i-1][0] == j:
                                    # result = fin_boolean_expression(lexeme[i+1:])
                                    # print(lexeme[i+1:])
                                    result = concatenationAnalyzer(lexeme[i+1:])
                                    # print(result)
                                    if len(result) != 0:
                                        varidents[j] = result
                                        modified_varidents[lexeme[i-1][0]] = str(result)
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {j} ITZ {result}', 1)
                                        return [f'', text, varidents] 
                                        

                        elif lexeme[i+1][0] == 'ALL OF':
                            for j in varidents:
                                if lexeme[i-1][0] == j:
                                    # result = fin_boolean_expression(lexeme[i+1:])
                                    result = infiniteBooleanAnalyzer(lexeme[i+1:], lexeme[i+1][0])
                                    # print(result)
                                    if len(result) != 0:
                                        varidents[j] = result
                                        modified_varidents[lexeme[i-1][0]] = str(result)
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {j} ITZ {result}', 1)
                                        return [f'', text, varidents] 
                                        
                        elif lexeme[i+1][0] in arithmetic:
                            for j in varidents:
                                if lexeme[i-1][0] == j:
                                    # result = fin_boolean_expression(lexeme[i+1:])
                                    result = arithmeticAnalyzer(varidents, arithmetic,lexeme[i+1:])
                                    # print(f"result in arithmetic:{result}")
                                    if result == "NOOBERROR":
                                        temp_result += noob_error_prompt
                                        noob_error = 1
                                    elif result == 'UNDEFINEDERROR':
                                        temp_result += undefined_error_prompt
                                        undefined_error = 1
                                        # print("UNDEFINEDERROR2")
                                        
                                    else:
                                        if len(result) != 0:
                                            varidents[j] = result
                                            modified_varidents[lexeme[i-1][0]] = str(result)
                                            text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {j} ITZ {result}', 1)
                                            return [f'', text, varidents] 
                        elif lexeme[i+1][0] == 'MAEK':
                            i += 1
                            if len(lexeme[i:]) == 3 or len(lexeme[i:]) == 4 :
                                for j in varidents:
                                    if j == lexeme[i+1][0]:
                                        if varidents[j] == 'NOOB':
                                            if lexeme[i+2][0] == 'YARN' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'YARN'):
                                                text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-2][0]} ITZ {""}', 1)
                                                return [f'', text, varidents] 
                                            elif lexeme[i+2][0] == 'NUMBAR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBAR'):
                                                text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-2][0]} ITZ {"0.0"}', 1)
                                                return [f'', text, varidents] 
                                            elif lexeme[i+2][0] == 'NUMBR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBR'):
                                                text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-2][0]} ITZ {"0"}', 1)
                                                return [f'', text, varidents]
                                            elif lexeme[i+2][0] == 'TROOF' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'TROOF'):
                                                text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-2][0]} ITZ {"FAIL"}', 1)
                                                return [f'', text, varidents]
                                            elif lexeme[i+2][0] == 'NOOB' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NOOB'):
                                                text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-2][0]} ITZ {"NOOB"}', 1)
                                                return [f'', text, varidents]
                                        else:
                                            if convertFloat(varidents[j]):
                                                if lexeme[i+2][0] == 'YARN' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'YARN'):
                                                    print('pasok diosidnkfkjsbdf')
                                                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-2][0]} ITZ {str(varidents[j])}', 1)
                                                    return [f'', text, varidents]
                                                elif lexeme[i+2][0] == 'NUMBAR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBAR'):
                                                    if '.' in str(varidents[j]):
                                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-2][0]} ITZ {varidents[j]}', 1)
                                                        return [f'', text, varidents]
                                                    else:
                                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-2][0]} ITZ {varidents[j]}.0', 1)
                                                        print(text)
                                                        return [f'', text, varidents]
                                                elif lexeme[i+2][0] == 'NUMBR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBR'):
                                                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-2][0]} ITZ {int(float(varidents[j]))}', 1)
                                                    return [f'', text, varidents]
                                                elif lexeme[i+2][0] == 'NOOB' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NOOB'):
                                                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-2][0]} ITZ {"NOOB"}', 1)
                                                    return [f'', text, varidents]
                                                elif lexeme[i+2][0] == 'TROOF' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'TROOF'):
                                                    if varidents[j] == 0.0:
                                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-2][0]} ITZ {"FAIL"}', 1)
                                                        return [f'', text, varidents]
                                                    else:
                                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-2][0]} ITZ {"WIN"}', 1)
                                                        return [f'', text, varidents]
                                            elif varidents[j] == 'WIN':
                                                if lexeme[i+2][0] == 'YARN' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'YARN'):
                                                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-2][0]} ITZ {str(varidents[j])}', 1)
                                                    return [f'', text, varidents]
                                                elif lexeme[i+2][0] == 'NUMBAR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBAR'):
                                                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-2][0]} ITZ {"1.0"}', 1)
                                                    return [f'', text, varidents] 
                                                elif lexeme[i+2][0] == 'NUMBR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBR'):
                                                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-2][0]} ITZ {"1"}', 1)
                                                    return [f'', text, varidents] 
                                                elif lexeme[i+2][0] == 'TROOF' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'TROOF'):
                                                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-2][0]} ITZ {varidents[j]}', 1)
                                                    return [f'', text, varidents]
                                                elif lexeme[i+2][0] == 'NOOB' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NOOB'):
                                                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-2][0]} ITZ {"NOOB"}', 1)
                                                    return [f'', text, varidents]
                                            elif varidents[j] == 'FAIL':
                                                if lexeme[i+2][0] == 'YARN' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'YARN'):
                                                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-2][0]} ITZ {str(varidents[j])}', 1)
                                                    return [f'', text, varidents]
                                                elif lexeme[i+2][0] == 'NUMBAR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBAR'):
                                                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-2][0]} ITZ {"0.0"}', 1)
                                                    return [f'', text, varidents] 
                                                elif lexeme[i+2][0] == 'NUMBR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBR'):
                                                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-2][0]} ITZ {"0"}', 1)
                                                    return [f'', text, varidents] 
                                                elif lexeme[i+2][0] == 'TROOF' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'TROOF'):
                                                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-2][0]} ITZ {varidents[j]}', 1)
                                                    return [f'', text, varidents]
                                                elif lexeme[i+2][0] == 'NOOB' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NOOB'):
                                                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-2][0]} ITZ {"NOOB"}', 1)
                                                    return [f'', text, varidents]                    
                    print(modified_varidents)

                elif lexeme[i][0] == 'IS NOW A':
                    for j in varidents:
                        if j == lexeme[i-1][0]:
                            if varidents[j] == 'NOOB':
                                if lexeme[i+1][0] == 'YARN':
                                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {""}', 1)
                                    return [f'', text, varidents] 
                                elif lexeme[i+1][0] == 'NUMBAR':
                                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {"0.0"}', 1)
                                    return [f'', text, varidents] 
                                elif lexeme[i+1][0] == 'NUMBR':
                                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {"0"}', 1)
                                    return [f'', text, varidents]
                                elif lexeme[i+1][0] == 'TROOF':
                                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {"FAIL"}', 1)
                                    return [f'', text, varidents]
                                elif lexeme[i+1][0] == 'NOOB':
                                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {"NOOB"}', 1)
                                    return [f'', text, varidents]
                            else:
                                if convertFloat(varidents[j]):
                                    if lexeme[i+1][0] == 'YARN':
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {str(varidents[j])}', 1)
                                        return [f'', text, varidents]
                                    elif lexeme[i+1][0] == 'NUMBAR':
                                        if '.' in str(varidents[j]):
                                            text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {varidents[j]}', 1)
                                            return [f'', text, varidents]
                                        else:
                                            text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {varidents[j]}.0', 1)
                                            print(text)
                                            return [f'', text, varidents]
                                    elif lexeme[i+1][0] == 'NUMBR':
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {int(float(varidents[j]))}', 1)
                                        return [f'', text, varidents]
                                    elif lexeme[i+1][0] == 'NOOB':
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {"NOOB"}', 1)
                                        return [f'', text, varidents]
                                    elif lexeme[i+1][0] == 'TROOF':
                                        if varidents[j] == 0.0:
                                            text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {"FAIL"}', 1)
                                            return [f'', text, varidents]
                                        else:
                                            text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {"WIN"}', 1)
                                            return [f'', text, varidents]
                                elif varidents[j] == 'WIN':
                                    if lexeme[i+1][0] == 'YARN':
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {str(varidents[j])}', 1)
                                        return [f'', text, varidents]
                                    elif lexeme[i+1][0] == 'NUMBAR':
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {"1.0"}', 1)
                                        return [f'', text, varidents] 
                                    elif lexeme[i+1][0] == 'NUMBR':
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {"1"}', 1)
                                        return [f'', text, varidents] 
                                    elif lexeme[i+1][0] == 'TROOF':
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {varidents[j]}', 1)
                                        return [f'', text, varidents]
                                    elif lexeme[i+1][0] == 'NOOB':
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {"NOOB"}', 1)
                                        return [f'', text, varidents]
                                elif varidents[j] == 'FAIL':
                                    if lexeme[i+1][0] == 'YARN':
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {str(varidents[j])}', 1)
                                        return [f'', text, varidents]
                                    elif lexeme[i+1][0] == 'NUMBAR':
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {"0.0"}', 1)
                                        return [f'', text, varidents] 
                                    elif lexeme[i+1][0] == 'NUMBR':
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {"0"}', 1)
                                        return [f'', text, varidents] 
                                    elif lexeme[i+1][0] == 'TROOF':
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {varidents[j]}', 1)
                                        return [f'', text, varidents]
                                    elif lexeme[i+1][0] == 'NOOB':
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i-1][0]} ITZ {"NOOB"}', 1)
                                        return [f'', text, varidents]
                #MAEK    
                elif lexeme[i][0] == 'MAEK':
                    if len(lexeme) == 3 or len(lexeme) == 4 :
                        for j in varidents:
                            if j == lexeme[i+1][0]:
                                if varidents[j] == 'NOOB':
                                    if lexeme[i+2][0] == 'YARN' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'YARN'):
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {""}', 1)
                                        return [f'', text, varidents] 
                                    elif lexeme[i+2][0] == 'NUMBAR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBAR'):
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {"0.0"}', 1)
                                        return [f'', text, varidents] 
                                    elif lexeme[i+2][0] == 'NUMBR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBR'):
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {"0"}', 1)
                                        return [f'', text, varidents]
                                    elif lexeme[i+2][0] == 'TROOF' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'TROOF'):
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {"FAIL"}', 1)
                                        return [f'', text, varidents]
                                    elif lexeme[i+2][0] == 'NOOB' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NOOB'):
                                        text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {"NOOB"}', 1)
                                        return [f'', text, varidents]
                                else:
                                    if convertFloat(varidents[j]):
                                        if lexeme[i+2][0] == 'YARN' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'YARN'):
                                            print('pasok diosidnkfkjsbdf')
                                            text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {str(varidents[j])}', 1)
                                            return [f'', text, varidents]
                                        elif lexeme[i+2][0] == 'NUMBAR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBAR'):
                                            if '.' in str(varidents[j]):
                                                text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {varidents[j]}', 1)
                                                return [f'', text, varidents]
                                            else:
                                                text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {varidents[j]}.0', 1)
                                                print(text)
                                                return [f'', text, varidents]
                                        elif lexeme[i+2][0] == 'NUMBR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBR'):
                                            text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {int(float(varidents[j]))}', 1)
                                            return [f'', text, varidents]
                                        elif lexeme[i+2][0] == 'NOOB' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NOOB'):
                                            text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {"NOOB"}', 1)
                                            return [f'', text, varidents]
                                        elif lexeme[i+2][0] == 'TROOF' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'TROOF'):
                                            if varidents[j] == 0.0:
                                                text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {"FAIL"}', 1)
                                                return [f'', text, varidents]
                                            else:
                                                text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {"WIN"}', 1)
                                                return [f'', text, varidents]
                                    elif varidents[j] == 'WIN':
                                        if lexeme[i+2][0] == 'YARN' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'YARN'):
                                            text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {str(varidents[j])}', 1)
                                            return [f'', text, varidents]
                                        elif lexeme[i+2][0] == 'NUMBAR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBAR'):
                                            text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {"1.0"}', 1)
                                            return [f'', text, varidents] 
                                        elif lexeme[i+2][0] == 'NUMBR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBR'):
                                            text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {"1"}', 1)
                                            return [f'', text, varidents] 
                                        elif lexeme[i+2][0] == 'TROOF' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'TROOF'):
                                            text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {varidents[j]}', 1)
                                            return [f'', text, varidents]
                                        elif lexeme[i+2][0] == 'NOOB' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NOOB'):
                                            text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {"NOOB"}', 1)
                                            return [f'', text, varidents]
                                    elif varidents[j] == 'FAIL':
                                        if lexeme[i+2][0] == 'YARN' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'YARN'):
                                            text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {str(varidents[j])}', 1)
                                            return [f'', text, varidents]
                                        elif lexeme[i+2][0] == 'NUMBAR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBAR'):
                                            text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {"0.0"}', 1)
                                            return [f'', text, varidents] 
                                        elif lexeme[i+2][0] == 'NUMBR' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NUMBR'):
                                            text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {"0"}', 1)
                                            return [f'', text, varidents] 
                                        elif lexeme[i+2][0] == 'TROOF' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'TROOF'):
                                            text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {varidents[j]}', 1)
                                            return [f'', text, varidents]
                                        elif lexeme[i+2][0] == 'NOOB' or (lexeme[i+2][0] == 'A' and lexeme[i+3][0] == 'NOOB'):
                                            text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {"NOOB"}', 1)
                                            return [f'', text, varidents]
                
                elif lexeme[i][0] in varidents and len(lexeme) == 1:
                    print('>>>>><><><>< dito napprinted', lexeme[i][0])
                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ {varidents[lexeme[i][0]]}', 1)
                    return [f'', text, varidents]

                elif len(lexeme) == 2 and lexeme[i][0] == 'O' and lexeme[i+1][0] == 'RLY':
                    isInCondition = 1

                elif len(lexeme) == 2 and lexeme[i][0] == 'YA' and lexeme[i+1][0] == 'RLY':
                    if varidents['IT'] == 'WIN':
                        conditionFlag = 1
                    elif varidents['IT'] == 'FAIL':
                        conditionFlag = 0
                        nowaiFlag = 1
                    else:
                        if f'{int(float(varidents["IT"]))}' != '0' or varidents["IT"] != 'NOOB':
                            conditionFlag = 1
                        else:
                            conditionFlag = 0
                            nowaiFlag = 1
                
                elif len(lexeme) == 2 and lexeme[i][0] == 'NO' and lexeme[i+1][0] == 'WAI':
                    nowaiFlag = 0

                elif lexeme[i][0] == 'WTF':
                    isInCondition = 1
                
                elif lexeme[i][0] == 'OMG' and isInCondition == 1:
                    if len(lexeme) > 2:     # pag string ang condition
                        if lexeme[i+2][0] == varidents['IT']:
                            conditionFlag = 1
                        else:
                            omgwtfFlag = 1
                    else:                   # pag other literals
                        if lexeme[i+1][0] == varidents['IT']:
                            conditionFlag = 1
                        else:
                            conditionFlag = 0
                            omgwtfFlag = 1
                
                elif lexeme[i][0] == 'GTFO' and isInCondition == 1:
                    gtfoFlag = 1

                elif lexeme[i][0] == 'OMGWTF' and isInCondition == 1:
                    omgwtfFlag = -1

                elif lexeme[i][0] == 'OIC' and isInCondition == 1:  # reset all flags
                    if gtfoFlag != -1:
                        gtfoFlag = -1
                    isInCondition == -1
                    conditionFlag = -1
                    nowaiFlag = -1
                
                # elif lexeme[i][0] == 'IM IN YR':
                #     isLoops = 1

                elif lexeme[i][0] == 'HOW IZ I':
                    currentFunction = lexeme[i+1][0]
                    if len(lexeme) == 4:
                        parameter_list[lexeme[i+1][0]] = lexeme[i+3][0]
                    isInFunction = 1
                
                elif lexeme[i][0] == 'I IZ':
                    if len(lexeme) == 5:
                        if lexeme[i+3][0] in varidents:
                            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',functions[lexeme[i+1][0]])
                            it = functionExecute(functions[lexeme[i+1][0]], {parameter_list[lexeme[i+1][0]]: varidents[lexeme[i+3][0]]})
                            
                            if len(it) != 0:
                                to_print = ''
                                for value in it:
                                    to_print += f'{value}\n'
                                text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ "{it[-1]}"', 1)
                                # temp_res.append(temp_result)
                                # print("temp_res:", temp_res)
                                varidents['IT'] = it[-1]
                                return [f"{to_print}", text, varidents]
                            return [f'', text, varidents]
                                

                elif lexeme[i][0] == 'IF' and lexeme[i+1][0] == 'U' and lexeme[i+2][0] == 'SAY' and lexeme[i+3][0] == 'SO':
                    print('PAPASOK DITOOOO <<<,')
                    functions[currentFunction] = functionBody
                    functionBody = ''
                    isInFunction = -1
                    print('ito ang functions', functions)
                
                
                elif lexeme[i][0] == 'IM IN YR':
                    loopStatement = text.splitlines()[h]
                    print(loopStatement, ',,,,,,,,,,,,,,,,,,,,,,,,,,,, ITO LOOP')
                    isLoops = 0
                    loopsLabel = lexeme[i+1][0] #label
                    loopsOperation = lexeme[i+2][0]
                    loopsVar = lexeme[i+4][0]
                    loopsCondition = lexeme[i+5][0]
                    if lexeme[i+6][0] == 'BOTH SAEM' or lexeme[i+6][0] == 'DIFFRINT':
                        print(loopsCondition, '<<<<<<<<<<<<<<<PASOOOOOOOK')
                        if lexeme[i+6][0] == 'BOTH SAEM' and loopsCondition == 'TIL':
                            result = comparison_expression(lexeme[i+6:])
                            if result == 'FAIL':
                                loopDone = 0
                                # if loopsOperation != 'NERFIN':
                            else:
                                loopDone = 1

                        elif lexeme[i+6][0] == 'BOTH SAEM' and loopsCondition == 'WILE':
                            result = comparison_expression(lexeme[i+6:])
                            if result == 'WIN':
                                loopsExpression = result
                                loopDone = 0
                            else:
                                loopDone = 1
                    break
                
                
                    

                elif lexeme[i][0] == 'IM OUTTA YR':
                    
                    text = text.replace(f'{text.splitlines()[h]}', f'', 1)
                    return ['', text, varidents]
                    # arr = []
                    # arr.append(loopsOperation)
                    # arr.append(loopsVar)
                    # arr.append(loopsCondition)
                    # arr.append(loopsExpression)
                    # arr.append(loopsBody)

                    # loops[loopsLabel] = arr
                    # print("loopsie hoops:",loops)
                    # loopsLabel = ''
                    # loopsOperation = ''
                    # loopsVar = ''
                    # loopsCondition = ''
                    # loopsExpression = ''
                    # loopsBody = []
                    # isLoops = -1
                    #     # loopOut = 1
                    #     # loopsBody
                    #     # loopsCodeBlock[currentLoops] = loopsBody
                    #     # loopsBody = ''
                    #     # isInForLoops = 0
                    #     # print('ito ang loop body', loops)

                elif lexeme[i][0] == 'VISIBLE':
                    print('ito na ung current >>>>>>>>>>><<<<<<<', text, loopDone)
                    # print(f"lexeme:{lexeme}")
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
                        #THIS IS FOR THE TROOF LITERAL
                        elif lexeme[visible_index][1] == 'TROOF Literal':
                            temp_result += str(lexeme[visible_index][0])
                            visible_index+=1
                        #THIS IS FOR GETTING THE NUMBR
                        elif lexeme[visible_index][1] == 'NUMBAR Literal':
                            temp_result += str(lexeme[visible_index][0])
                            visible_index+=1
                        #FOR GETTING THE NUMBAR
                        elif lexeme[visible_index][1] == 'NUMBR Literal':
                            temp_result += str(lexeme[visible_index][0])
                            visible_index+=1
                        elif lexeme[visible_index][0] in arithmetic:
                            #kunin ang lexeme until +
                            temp = []
                            temp_index = visible_index
                            while temp_index < len(lexeme):
                                if lexeme[temp_index][1] == "Output Delimiter":
                                    break
                                else:
                                    temp.append(lexeme[temp_index])
                                    temp_index+=1
                            arithmeticresult = str(arithmeticAnalyzer(varidents,arithmetic,temp)) 
                            if arithmeticresult == "NOOBERROR":
                                temp_result += noob_error_prompt
                                break 
                            elif arithmeticresult == "UNDEFINEDERROR":
                                temp_result += undefined_error_prompt
                                undefined_error = 1
                                # print("UNDEFINEDERROR3")
                                break
                            else:
                                temp_result += arithmeticresult
                                visible_index = temp_index
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
                            while temp_index < len(lexeme):
                                if lexeme[temp_index][1] == "Output Delimiter":
                                    break
                                else:
                                    temp.append(lexeme[temp_index])
                                    temp_index+=1
                            temp_result += str(booleanAnalyzer(temp, 0))
                            visible_index = temp_index
                        #INFINITE BOOLEANS
                        elif lexeme[visible_index][0] in infinitebooleans:
                            #kunin ang lexeme until +
                            temp = []
                            temp_index = visible_index
                            while temp_index < len(lexeme):
                                if lexeme[temp_index][1] == "Output Delimiter":
                                    break
                                else:
                                    temp.append(lexeme[temp_index])
                                    temp_index+=1
                            temp_result += str(infiniteBooleanAnalyzer(temp, lexeme[visible_index][0]))
                            visible_index = temp_index
                        elif lexeme[visible_index][0] == 'SMOOSH':
                            #kunin ang lexeme until +
                            temp = []
                            temp_index = visible_index
                            while temp_index < len(lexeme):
                                if lexeme[temp_index][1] == "Output Delimiter":
                                    break
                                else:
                                    temp.append(lexeme[temp_index])
                                    temp_index+=1
                            temp_result += str(concatenationAnalyzer(lexeme[i+1:]))
                            visible_index = temp_index
                    if loopDone == 0:
                        print(varidents, loopsVar,loopStatement,loopsOperation, 'PASOK <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>')
                        if loopsOperation != 'NERFIN':
                            text = text.replace(f'{loopStatement}', f'I HAS A {loopsVar} ITZ {int(varidents[loopsVar])+1}\n{loopStatement}', 1)
                        else:
                            print()
                            text = text.replace(f'{loopStatement}', f'I HAS A {loopsVar} ITZ {int(varidents[loopsVar])-1}\n{loopStatement}', 1)
                            print('pasooooooooooook',text)
                        return [f"{temp_result}\n", text, varidents]
                    print('dapat dito naaaa >>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<')
                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A IT ITZ "{temp_result}"', 1)
                    # temp_res.append(temp_result)
                    # print("temp_res:", temp_res)
                    # print('ito ang current result', temp_result)
                    # print('ito ang current result',varidents)
                    varidents['IT'] = temp_result
                    # print('ito ang current ipapasa',varidents)
                    return [f"{temp_result}\n", text, varidents]
                    # break
            lexeme.clear()
    text = text.replace(f'{text.splitlines()[h]}', '', 1)
    temp_res = temp_list
    # print('hey:', varidents)
    return [None, text, varidents]



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
                            result += f'FAIL\n'
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
    print(lexeme, '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    arithmetic = ['SUM OF','DIFF OF','PRODUKT OF', 'QUOSHUNT OF', 'MOD OF', 'BIGGR OF', 'SMALLR OF']
    result = []
    for i in range(0, len(lexeme)):
                if lexeme[i][0] == 'BOTH SAEM':
                    if len(lexeme) == 4:
                        one = convertFloat(lexeme[i+1][0])
                        three = convertFloat(lexeme[i+3][0])
                        if one == True and three == True:
                            if float(lexeme[i+1][0]) == float(lexeme[i+3][0]):
                                result = 'WIN'
                                
                            else:
                                result = 'FAIL'
                        elif one == False and three == True:
                            value = ""
                            for j in varidents:
                                if j == lexeme[i+1][0]:
                                    value = varidents[j]
                            if convertFloat(value) == True:
                                if float(value) == float(lexeme[i+3][0]):
                                    result = 'WIN'
                                else:
                                    result = 'FAIL'
                        elif one == True and three == False:
                            value = ""
                            for j in varidents:
                                if j == lexeme[i+3][0]:
                                    value = varidents[j]
                            if convertFloat(value) == True:
                                if float(lexeme[i+1][0]) == float(value):
                                    result = 'WIN'
                                else:
                                    result = 'FAIL'
                        elif one == False and three == False:
                            # value = []
                            # for j in varidents:
                            #     if j == lexeme[i+3][0] or j == lexeme[i+1][0]:
                            #         value.append(varidents[j])
                            # if len(value) == 2:
                                if convertFloat(varidents[lexeme[i+1][0]]) == True and  convertFloat(varidents[lexeme[i+3][0]]) == True:
                                    if float(varidents[lexeme[i+1][0]]) == float(varidents[lexeme[i+3][0]]):
                                        result = 'WIN'
                                    else:
                                        result = 'FAIL'
                    else: #for SMALLR OF and BIGGR OF
                        #BOTH SAEM/DIFFRINT x AN y

                        #assuming x is in arithmetic
                        
                        if lexeme[i+1][0] in arithmetic:
                            num_operations = 1
            
                            index =i+1
                            # num_operations += 1
                            for j in range(2, len(lexeme)):
                                if lexeme[j][0] in arithmetic:
                                    num_operations += 1
                                    index = j
                            num_AN = num_operations * 2 + 3

                            temp = arithmeticAnalyzer(varidents, arithmetic,lexeme[i+1:num_AN])
                            # print(lexeme[index+4+1])
                            # print(temp)
                            one = convertFloat(temp)
                            three = convertFloat(lexeme[index+4+1][0])
                            last_operand = lexeme[index+4+1][0]
                            if one == True and three == True:
                                if float(temp) == float(last_operand):
                                    result = 'WIN'
                                else:
                                    result = 'FAIL'
                           
                            elif one == True and three == False:
                                value = ""
                                for j in varidents:
                                    if j == last_operand:
                                        value = varidents[j]
                                if convertFloat(value) == True:
                                    if float(temp) == float(value):
                                       result = 'WIN'
                                    else:
                                        result = 'FAIL'
                            break
                        #assuming y is in arithmetic
                        # elif lexeme[i+3][0] in arithmetic:
                        #     num_operations = 1
            
                        #     index =i+3
                        #     for j in range(index, len(lexeme)):
                        #         if lexeme[j][0] in arithmetic:
                        #             num_operations += 1
                        #             index = j
                        #             num_AN = num_operations + 4

                        #     temp = arithmeticAnalyzer(varidents, arithmetic,lexeme[i+3:index+4])
                        #     # print(lexeme[index+4+1])
                        #     one = convertFloat(temp)
                        #     three = convertFloat(lexeme[index+3][0])
                        #     # last_operand = lexeme[index+4+1][0]
                        #     if one == True and three == True:
                        #         if float(lexeme[i+1][0]) == float(temp):
                        #             result = 'WIN'
                        #         else:
                        #             result = 'FAIL'
                           
                        #     elif one == False and three == True:
                        #         value = ""
                        #         for j in varidents:
                        #             if j == lexeme[i+1][0]:
                        #                 value = varidents[j]
                        #         if convertFloat(value) == True:
                        #             if float(value) == float(temp):
                        #                result = 'WIN'
                        #             else:
                        #                 result = 'FAIL'
                        #     print(result)
                
                        elif lexeme[i+3][0] == 'SMALLR OF':
                            
                            one = convertFloat(lexeme[i+1][0])
                            three = convertFloat(lexeme[i+6][0])
                            if one == True and three == True:
                                print('comparisoooon >>>>>>>>>>', one, three)
                                if float(lexeme[i+1][0]) <= float(lexeme[i+6][0]):
                                    result = 'WIN'
                                else:
                                    result = 'FAIL'
                            elif one == False and three == True:
                                value = ""
                                for j in varidents:
                                    if j == lexeme[i+1][0]:
                                        value = varidents[j]
                                if convertFloat(value) == True:
                                    if float(value) <= float(lexeme[i+6][0]):
                                        result = 'WIN'
                                    else:
                                       result = 'FAIL'
                            elif one == True and three == False:
                                value = ""
                                for j in varidents:
                                    if j == lexeme[i+6][0]:
                                        value = varidents[j]
                                if convertFloat(value) == True:
                                    if float(lexeme[i+1][0]) <= float(value):
                                       result = 'WIN'
                                    else:
                                        result = 'FAIL'
                            elif one == False and three == False:
                                # value = []
                                # for j in varidents:
                                #     if j == lexeme[i+6][0] or j == lexeme[i+1][0]:
                                #         value.append(varidents[j])
                                # if len(value) == 2:
                                    if convertFloat(varidents[lexeme[i+1][0]]) == True and  convertFloat(varidents[lexeme[i+6][0]]) == True:
                                        if float(varidents[lexeme[i+1][0]]) <= float(varidents[lexeme[i+6][0]]):
                                            result = 'WIN'
                                        else:
                                            result = 'FAIL'
                                    # print(convertFloat(value[0]),convertFloat(value[1]), '<<<<<<<<<<<<<<<<<')
                                    # if convertFloat(value[0]) == True and convertFloat(value[1]) == True:
                                    #     if float(value[0]) >= float(value[1]):
                                    #         result = 'WIN'
                                    #     else:
                                    #        result = 'FAIL'
                        elif lexeme[i+3][0] == 'BIGGR OF':
                            one = convertFloat(lexeme[i+1][0])
                            three = convertFloat(lexeme[i+6][0])
                            if one == True and three == True:
                                if float(lexeme[i+1][0]) >= float(lexeme[i+6][0]):
                                   result = 'WIN'
                                else:
                                    result = 'FAIL'
                            elif one == False and three == True:
                                value = ""
                                for j in varidents:
                                    if j == lexeme[i+1][0]:
                                        value = varidents[j]
                                if convertFloat(value) == True:
                                    if float(value) >= float(lexeme[i+6][0]):
                                        result = 'WIN'
                                    else:
                                        result = 'FAIL'
                            elif one == True and three == False:
                                value = ""
                                for j in varidents:
                                    if j == lexeme[i+6][0]:
                                        value = varidents[j]
                                if convertFloat(value) == True:
                                    if float(lexeme[i+1][0]) >= float(value):
                                        result = 'WIN'
                                    else:
                                       result = 'FAIL'
                            elif one == False and three == False:
                                if convertFloat(varidents[lexeme[i+1][0]]) == True and  convertFloat(varidents[lexeme[i+6][0]]) == True:
                                        if float(varidents[lexeme[i+1][0]]) >= float(varidents[lexeme[i+6][0]]):
                                            result = 'WIN'
                                        else:
                                            result = 'FAIL'
                                # value = []
                                # for j in varidents:
                                #     if j == lexeme[i+6][0] or j == lexeme[i+1][0]:
                                #         value.append(varidents[j])
                                
                                # if len(value) == 2:
                                #     if convertFloat(value[0]) == True and  convertFloat(value[1]) == True:
                                #         if float(value[0]) <= float(value[1]):
                                #             result = 'WIN'
                                #         else:
                                #             result = 'FAIL'
                        #assuming y is in arithmetic
                        elif lexeme[i+3][0] in arithmetic:
                            num_operations = 1
            
                            index =i+3
                            for j in range(index, len(lexeme)):
                                if lexeme[j][0] in arithmetic:
                                    num_operations += 1
                                    index = j
                            num_AN = num_operations * 2 + 3

                            temp = arithmeticAnalyzer(varidents, arithmetic,lexeme[i+3:num_AN])
                            # print(lexeme[index+4+1])
                            one = convertFloat(temp)
                            three = convertFloat(lexeme[index+3][0])
                            # last_operand = lexeme[index+4+1][0]
                            if one == True and three == True:
                                if float(lexeme[i+1][0]) == float(temp):
                                    result = 'WIN'
                                else:
                                    result = 'FAIL'
                           
                            elif one == False and three == True:
                                value = ""
                                for j in varidents:
                                    if j == lexeme[i+1][0]:
                                        value = varidents[j]
                                if convertFloat(value) == True:
                                    if float(value) == float(temp):
                                       result = 'WIN'
                                    else:
                                        result = 'FAIL'
                            # print(result)
                #for diffrint
                elif lexeme[i][0] == 'DIFFRINT':
                    if len(lexeme) == 4:
                        one = convertFloat(lexeme[i+1][0])
                        three = convertFloat(lexeme[i+3][0])
                        if one == True and three == True:
                            if float(lexeme[i+1][0]) != float(lexeme[i+3][0]):
                               result = 'WIN'
                            else:
                                result = 'FAIL'
                        elif one == False and three == True:
                            value = ""
                            for j in varidents:
                                if j == lexeme[i+1][0]:
                                    value = varidents[j]
                            if convertFloat(value) == True:
                                if float(value) != float(lexeme[i+3][0]):
                                   result = 'WIN'
                                else:
                                   result = 'FAIL'
                        elif one == True and three == False:
                            value = ""
                            for j in varidents:
                                if j == lexeme[i+3][0]:
                                    value = varidents[j]
                            if convertFloat(value) == True:
                                if float(lexeme[i+1][0]) != float(value):
                                   result = 'WIN'
                                else:
                                    result = 'FAIL'
                        elif one == False and three == False:
                            if convertFloat(varidents[lexeme[i+1][0]]) == True and  convertFloat(varidents[lexeme[i+3][0]]) == True:
                                        if float(varidents[lexeme[i+1][0]]) != float(varidents[lexeme[i+3][0]]):
                                            result = 'WIN'
                                        else:
                                            result = 'FAIL'
                            # value = []
                            # for j in varidents:
                            #     if j == lexeme[i+3][0] or j == lexeme[i+1][0]:
                            #         value.append(varidents[j])
                            # if len(value) == 2:
                            #     if convertFloat(value[0]) == True and  convertFloat(value[1]) == True:
                            #         if float(value[0]) != float(value[1]):
                            #             result = 'WIN'
                            #         else:
                            #            result = 'FAIL'
                    else: #for SMALLR OF and BIGGR OF
                        # print(lexeme[i+1][0])
                        if lexeme[i+1][0] in arithmetic:
                            num_operations = 1
            
                            index =i+1
                            # num_operations += 1
                            for j in range(index, len(lexeme)):
                                if lexeme[j][0] in arithmetic:
                                    num_operations += 1
                                    index = j
                            num_AN =num_operations * 2 + 3

                            temp = arithmeticAnalyzer(varidents, arithmetic,lexeme[i+1:index+4])
                            # print(temp)
                            # print(lexeme[index+4+1])
                            one = convertFloat(temp)
                            three = convertFloat(lexeme[index+4+1][0])
                            last_operand = lexeme[index+4+1][0]
                            if one == True and three == True:
                                if float(temp) != float(last_operand):
                                    result = 'WIN'
                                else:
                                    result = 'FAIL'
                           
                            elif one == True and three == False:
                                value = ""
                                for j in varidents:
                                    if j == last_operand:
                                        value = varidents[j]
                                if convertFloat(value) == True:
                                    if float(temp) != float(value):
                                       result = 'WIN'
                                    else:
                                        result = 'FAIL'
                        # elif lexeme[i+3][0] in arithmetic:
                        #     num_operations = 1
            
                        #     index =i+3
                        #     for j in range(index, len(lexeme)):
                        #         if lexeme[j][0] in arithmetic:
                        #             num_operations += 1
                        #             index = j
                        #             num_AN = num_operations + 4

                        #     temp = arithmeticAnalyzer(varidents, arithmetic,lexeme[i+3:index+4])
                        #     # print(lexeme[index+4+1])
                        #     one = convertFloat(temp)
                        #     three = convertFloat(lexeme[index+3][0])
                        #     # last_operand = lexeme[index+4+1][0]
                        #     if one == True and three == True:
                        #         if float(lexeme[i+1][0]) != float(temp):
                        #             result = 'WIN'
                        #         else:
                        #             result = 'FAIL'
                           
                        #     elif one == False and three == True:
                        #         value = ""
                        #         for j in varidents:
                        #             if j == lexeme[i+1][0]:
                        #                 value = varidents[j]
                        #         if convertFloat(value) == True:
                        #             if float(value) != float(temp):
                        #                result = 'WIN'
                        #             else:
                        #                 result = 'FAIL'
                        if lexeme[i+3][0] == 'SMALLR OF':
                            one = convertFloat(lexeme[i+1][0])
                            three = convertFloat(lexeme[i+6][0])
                            if one == True and three == True:
                                if float(lexeme[i+1][0]) > float(lexeme[i+6][0]):
                                    result = 'WIN'
                                else:
                                    result = 'FAIL'
                            elif one == False and three == True:
                                value = ""
                                for j in varidents:
                                    if j == lexeme[i+1][0]:
                                        value = varidents[j]
                                if convertFloat(value) == True:
                                    if float(value) > float(lexeme[i+6][0]):
                                        result = 'WIN'
                                    else:
                                       result = 'FAIL'
                            elif one == True and three == False:
                                value = ""
                                for j in varidents:
                                    if j == lexeme[i+6][0]:
                                        value = varidents[j]
                                if convertFloat(value) == True:
                                    if float(lexeme[i+1][0]) > float(value):
                                        result = 'WIN'
                                    else:
                                        result = 'FAIL'
                            elif one == False and three == False:
                                if convertFloat(varidents[lexeme[i+1][0]]) == True and  convertFloat(varidents[lexeme[i+6][0]]) == True:
                                        if float(varidents[lexeme[i+1][0]]) > float(varidents[lexeme[i+6][0]]):
                                            result = 'WIN'
                                        else:
                                            result = 'FAIL'
                                # value = []
                                # for j in varidents:
                                #     if j == lexeme[i+6][0] or j == lexeme[i+1][0]:
                                #         value.append(varidents[j])
                                # if len(value) == 2:
                                #     if convertFloat(value[0]) == True and  convertFloat(value[1]) == True:
                                #         if float(value[0]) > float(value[1]):
                                #            result = 'WIN'
                                #         else:
                                #             result = 'FAIL'
                        elif lexeme[i+3][0] == 'BIGGR OF':
                            one = convertFloat(lexeme[i+1][0])
                            three = convertFloat(lexeme[i+6][0])
                            if one == True and three == True:
                                if float(lexeme[i+1][0]) < float(lexeme[i+6][0]):
                                    result = 'WIN'
                                else:
                                    result = 'FAIL'
                            elif one == False and three == True:
                                value = ""
                                for j in varidents:
                                    if j == lexeme[i+1][0]:
                                        value = varidents[j]
                                if convertFloat(value) == True:
                                    if float(value) < float(lexeme[i+6][0]):
                                       result = 'WIN'
                                    else:
                                       result = 'FAIL'
                            elif one == True and three == False:
                                value = ""
                                for j in varidents:
                                    if j == lexeme[i+6][0]:
                                        value = varidents[j]
                                if convertFloat(value) == True:
                                    if float(lexeme[i+1][0]) < float(value):
                                        result = 'WIN'
                                    else:
                                        result = 'FAIL'
                            elif one == False and three == False:
                                if convertFloat(varidents[lexeme[i+1][0]]) == True and  convertFloat(varidents[lexeme[i+6][0]]) == True:
                                        if float(varidents[lexeme[i+1][0]]) < float(varidents[lexeme[i+6][0]]):
                                            result = 'WIN'
                                        else:
                                            result = 'FAIL'
                                # value = []
                                # for j in varidents:
                                #     if j == lexeme[i+6][0] or j == lexeme[i+1][0]:
                                #         value.append(varidents[j])
                                # if len(value) == 2:
                                #     if convertFloat(value[0]) == True and  convertFloat(value[1]) == True:
                                #         if float(value[0]) < float(value[1]):
                                #             result = 'WIN'
                                #         else:
                                #             result = 'FAIL'
                        #assuming y is in arithmetic
                        elif lexeme[i+3][0] in arithmetic:
                            num_operations = 1
            
                            index =i+3
                            for j in range(index, len(lexeme)):
                                if lexeme[j][0] in arithmetic:
                                    num_operations += 1
                                    index = j
                            num_AN = num_operations * 2 + 3

                            temp = arithmeticAnalyzer(varidents, arithmetic,lexeme[i+3:num_AN])
                            # print(lexeme[index+4+1])
                            one = convertFloat(temp)
                            three = convertFloat(lexeme[index+3][0])
                            # last_operand = lexeme[index+4+1][0]
                            if one == True and three == True:
                                if float(lexeme[i+1][0]) != float(temp):
                                    result = 'WIN'
                                else:
                                    result = 'FAIL'
                           
                            elif one == False and three == True:
                                value = ""
                                for j in varidents:
                                    if j == lexeme[i+1][0]:
                                        value = varidents[j]
                                if convertFloat(value) == True:
                                    if float(value) != float(temp):
                                       result = 'WIN'
                                    else:
                                        result = 'FAIL'
        # print(result)
    return result

def convertFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    