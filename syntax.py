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

def arithmeticOperands(lexeme):
    arithmetic = ['SUM OF','DIFF OF','PRODUKT OF', 'QUOSHUNT OF', 'MOD OF', 'BIGGR OF', 'SMALLR OF']
    result = 0
    arithmetic_index = 0
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
            result = float(varidents[lexeme[arithmetic_index+1][0]]) / float(varidents[lexeme[arithmetic_index+3][0]])
        elif lexeme[arithmetic_index+1][1] == 'Identifier' or lexeme[arithmetic_index+1][1] == 'Variable Identifier':
            result = float(varidents[lexeme[arithmetic_index+1][0]]) / float(lexeme[arithmetic_index+3][0])
        elif lexeme[arithmetic_index+3][1] == 'Identifier' or lexeme[arithmetic_index+3][1] == 'Variable Identifier':
            result = float(lexeme[arithmetic_index+1][0]) / float(varidents[lexeme[arithmetic_index+3][0]])
        #THIS ONE IS FOR THE TROOFS
        elif lexeme[arithmetic_index+1][1] == 'TROOF Literal' and lexeme[arithmetic_index+3][1] == 'TROOF Literal':
            if lexeme[arithmetic_index+1][0] == 'WIN' and lexeme[arithmetic_index+3][0] == 'WIN':
                result = float(1)/float(1)
            elif lexeme[arithmetic_index+1][0] == 'FAIL' and lexeme[arithmetic_index+3][0] == 'WIN':
                result = float(0)/float(1)
        elif lexeme[arithmetic_index+1][1] == 'TROOF Literal':
            if lexeme[arithmetic_index+1][0] == 'WIN':
                result = float(1)/float(lexeme[arithmetic_index+3][0])
            else:
                result = float(0)/float(lexeme[arithmetic_index+3][0])
        elif lexeme[arithmetic_index+3][1] == 'TROOF Literal':
            if lexeme[arithmetic_index+3][0] == 'WIN':
                result =float(lexeme[arithmetic_index+1][0])/float(1)
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


modified_varidents = {}
explicit_typecast = []
booleans = ['BOTH OF', 'EITHER OF', 'WON OF', 'NOT']
literals = ['NUMBR Literal', 'NUMBAR Literal', 'YARN Literal', 'TROOF Literal', 'Type Literal']
varidents = {}

def getExplicitTypecast(text):
    if syntax.syntax(text) == '>> No syntax errors.':
        semantics(text)
        print('>>>>', modified_varidents, explicit_typecast)
        return explicit_typecast

def getVaridents(text):
    if syntax.syntax(text) == '>> No syntax errors.':
        # print("pasok", modified_varidents)
        # semantics(text)

        return modified_varidents
    return 0

def semantics(text):
    arithmetic = ['SUM OF','DIFF OF','PRODUKT OF', 'QUOSHUNT OF', 'MOD OF', 'BIGGR OF', 'SMALLR OF']
    semanticsResult = ''
    global varidents
    global explicit_typecast
    global undefined_error
    global noob_error
    explicit_typecast.clear()
    modified_varidents.clear()
    varidents = syntax.getVaridents(text)
    # print(varidents)
    literals = ['NUMBR Literal', 'NUMBAR Literal', 'YARN Literal', 'TROOF Literal', 'Type Literal']
    comparison = ['BOTH SAEM', 'DIFFRINT']
    booleans = ['BOTH OF', 'EITHER OF', 'WON OF', 'NOT']
    inifinitebooleans = ['ALL OF', 'ANY OF']
    keyUsingExp = ['YR', 'FOUND YR', 'ITZ', 'R', 'MEBBE', 'TIL', 'WILE', 'VISIBLE']
    hasHai = -1
    hasKthxbye = -1
    hasWazzup = -1
    hasBuhbye = -1
    hasVarDec = 0
    wtfchecker = -1
    omgchecker = -1
    omgwtfchecker = -1
    functionchecker = -1
    
    for h in range(0, len(text.splitlines())):
        lexeme = keywords.lex(text.splitlines()[h].lstrip().rstrip())
        
        if undefined_error == 1 or noob_error:
            undefined_error = 0
            noob_error = 0
            return [None,'']
        
        if lexeme is not None:
            # print(f"lexeme: {lexeme}")
            if ['BTW', 'Comment Delimiter'] in lexeme:
                lexeme.pop(lexeme.index(['BTW', 'Comment Delimiter'])+1)
                lexeme.pop(lexeme.index(['BTW', 'Comment Delimiter']))
            
            # print(f"len(lexeme): {len(lexeme)}")
            for i in range(0, len(lexeme)):
                print(f"starting lexeme sa while:{lexeme}")
                
                ## PROGRAM BLOCK SYNTAX - HAI
                if lexeme[i][0] == 'HAI' and hasHai == -1 and hasKthxbye == -1:
                    hasHai = 0
                    break
                if lexeme[i][0] == 'I HAS A':
                    if outsideWazzup == 1:
                        varidents[lexeme[i+1][0]] = lexeme[i+3][0]
                    break
                #-- BOTH SAEM AND DIFFRINT WITH VARIDENTS
                if lexeme[i][0] in comparison:
                    
                    text = text.replace(f'{text.splitlines()[h]}', '', 1)
                    return [f'{comparison_expression(lexeme)}\n', text]
                ##INFINITE ARITY BOOLEAN SYNTAX - ANY OF
                elif lexeme[i][0] == 'ANY OF' or lexeme[i][0] == 'ALL OF':
                    text = text.replace(f'{text.splitlines()[h]}', '', 1)
                    return [f'{infiniteBooleanAnalyzer(lexeme, lexeme[i][0])}\n', text]
                    
                elif lexeme[i][0] in booleans:
                    text = text.replace(f'{text.splitlines()[h]}', '', 1)
                    return [f'{booleanAnalyzer(lexeme, 0)}\n', text]

                #THIS PART IS FOR THE COMPUTATIONS!!
                elif lexeme[i][0] in arithmetic:
                    text = text.replace(f'{text.splitlines()[h]}', '', 1)
                    arithmeticresult = str(arithmeticAnalyzer(varidents,arithmetic,lexeme))
                    print(f"arithmetic result:{arithmeticresult}")
                    if arithmeticresult == "NOOBERROR":
                        temp_result += noob_error_prompt
                        noob_error = 1
                        break 
                    if arithmeticresult == "UNDEFINEDERROR":
                        temp_result += undefined_error_prompt
                        undefined_error = 1
                        print("UNDEFINEDERROR1")
                        break
                    else:
                        return [arithmeticresult, text]
                        break #hindi ko alam baket nag break pa pero pag wala siya nag error shadkashdkadhaskhdahdsa
                
                #THIS IS TO CATER GIMMEH - ASKING USER FOR INPUT
                elif lexeme[i][0] == 'GIMMEH':
                    # resolved na :>>
                    input_value = for_input.get_user_input()
                    varidents[lexeme[i+1][0]] = str(input_value)
                    modified_varidents[lexeme[i+1][0]] = str(input_value)
                    text = text.replace(f'{text.splitlines()[h]}', f'I HAS A {lexeme[i+1][0]} ITZ {input_value}', 1)
                    return [f'{input_value}\n', text]
                    
                #R
                elif lexeme[i][0] == 'R':
                    print('pasok dito')
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
                                        result = arithmeticSyntax(h,arithmetic,lexeme[i+3:])
                                        if result[0] == 0:
                                            syntaxResult += result[1]
                                            success = result[0]
                                            break   
                                        else:
                                           
                                            success = 1
                                            result = semantics.arithmeticAnalyzer(varidents, arithmetic,lexeme[i+3:])
                                            # print(result[0])
                                            varidents[lexeme[i+1][0]] = result
                                            modif_var[lexeme[i+1][0]] = result
                                            break
                                    elif lexeme[i+3][0] in comparison:
                                        if comparisonSyntax(lexeme[i+3:], h, i):
                                            success = 0
                                            syntaxResult += comparisonSyntax(lexeme[i+1:], h, i)
                                            break 
                                        else:
                                            # print(lexeme[i+3:])
                                            result = semantics.comparison_expression(lexeme[i+3:])
                                            # success = 1
                                            varidents[lexeme[i+1][0]] = result
                                            modif_var[lexeme[i+1][0]] = result
                                            # break
                                    # elif lexeme[i+3][0]!= '"' and lexeme[i+5][0] != '"': #if string shoudl be enclosed by ""
                                    #     syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+4][0]} should be enclosed by quotation marks if it is a yarn or string")
                                    #     success = 0
                                    #     break

                            
                        hasVarDec = 1
                        if len(lexeme) == 2:
                            varidents[lexeme[i+1][0]] = 'NOOB'
                        elif len(lexeme) == 4 or len(lexeme) == 6:
                            if isfloat(lexeme[i+3][0]) != False and '.' in lexeme[i+3][0]:
                                # print(lexeme[i+3][0])
                                varidents[lexeme[i+1][0]] = float(lexeme[i+3][0])       # if NUMBAR
                            elif isfloat(lexeme[i+3][0]) != False and '.' not in lexeme[i+3][0]:
                                varidents[lexeme[i+1][0]] = int(lexeme[i+3][0])         # if NUMBR
                            else:
                                if lexeme[i+3][0] != '"':
                                    varidents[lexeme[i+1][0]] = lexeme[i+3][0]              # if TROOF
                                else:
                                    varidents[lexeme[i+1][0]] = lexeme[i+4][0] 
                            
                        break
                    else:
                        if lexeme[i][0] != 'I HAS A' and lexeme[i][0] != 'BUHBYE' and lexeme[i][0] != 'KTHXBYE' and hasWazzup == 0 and hasBuhbye == -1: 
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} in <WAZZUP> block: \n\tonly I HAS A statements can be inside WAZZUP and BUHBYE')
                            success = 0
                            break
                        elif lexeme[i][0] == 'I HAS A':
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <I HAS A>: \n\tI HAS A statements must be inside WAZZUP and BUHBYE')
                            success = 0
                            break
                    ## VARIABLE BLOCK SYNTAX - BUHBYE
                    if lexeme[i][0] == 'BUHBYE' and hasWazzup == 0:
                        hasBuhbye = 0
                        hasWazzup = 1
                        break
                    else:
                        if lexeme[i][0] == 'BUHBYE' and hasWazzup == -1 and hasBuhbye == -1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <BUHBYE>: \n\tBUHBYE must be declared after WAZZUP')
                            success = 0
                            break
                        elif lexeme[i][0] == 'BUHBYE' and hasWazzup == 0 and hasBuhbye == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <BUHBYE>: \n\tAlready has BUHBYE; it must be declared once')
                            success = 0
                            break

                    #PRINTING
                    if lexeme[i][0] == 'VISIBLE':
                        print(f"lexeme sa visible: {lexeme}")
                    #     # if less than
                        # print(f"lexeme in visible start: {lexeme}")
                        if len(lexeme) < 2:
                            syntaxResult +=(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tVISIBLE must have a Variable Identifier, Literal, or an Expression')
                            success = 0
                            break
                        else:
                            visible_indexcounter = 1
                            while visible_indexcounter < len(lexeme):
                                print(f"visible_indexcounter:{visible_indexcounter}")
                                print(f"len(lexeme): {len(lexeme)}")
                                # check muna yung "+"
                                if lexeme[visible_indexcounter][1] == "Output Delimiter":
                                    #check yung before "+"
                                    if lexeme[visible_indexcounter-1][0] not in varidents:
                                        if lexeme[visible_indexcounter-1][1] != 'NUMBR Literal':
                                            if lexeme[visible_indexcounter-1][1] != 'NUMBAR Literal':
                                                if lexeme[visible_indexcounter-1][1] != 'TROOF Literal':
                                                    if lexeme[visible_indexcounter-1][1] != 'String Delimiter':
                                                        if lexeme[visible_indexcounter-1][1] != 'Concatenation Delimiter':
                                                            if lexeme[visible_indexcounter-1][0] != "IT":
                                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[visible_indexcounter][0]}>: \n\tIncorrect syntax, see correct syntax. \n\t{lexeme[visible_indexcounter][0]} VISIBLE <x> + <y> where <x> and <y> are either Variable Identifiers, Expressions, String, or IT only1')
                                                                success = 0
                                                                break
                                    #check yung after naman "+"
                                    if lexeme[visible_indexcounter+1][0] not in varidents:
                                        if lexeme[visible_indexcounter+1][0] not in arithmetic:
                                            if lexeme[visible_indexcounter+1][0] not in comparison:
                                                if lexeme[visible_indexcounter+1][0] not in booleans:
                                                    if lexeme[visible_indexcounter+1][1] != 'NUMBR Literal':
                                                        if lexeme[visible_indexcounter+1][1] != 'NUMBAR Literal':
                                                            if lexeme[visible_indexcounter+1][1] != 'TROOF Literal':
                                                                if lexeme[visible_indexcounter+1][0] not in inifinitebooleans:
                                                                    if lexeme[visible_indexcounter+1][1] != 'String Delimiter':
                                                                        if lexeme[visible_indexcounter+1][0] != "IT":
                                                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[visible_indexcounter][0]}>: \n\tIncorrect syntax, see correct syntax. \n\t{lexeme[visible_indexcounter][0]} VISIBLE <x> + <y> where <x> and <y> are either Variable Identifiers, Expressions, String, or IT only2')
                                                                            success = 0
                                                                            break
                                    visible_indexcounter+=1
                                else:
                                    #CHECK MUNA IF STRING SIYA 
                                    if lexeme[visible_indexcounter][1] != 'String Delimiter':
                                        if lexeme[visible_indexcounter][1] != 'TROOF Literal':
                                            if lexeme[visible_indexcounter][1] != 'NUMBR Literal':
                                                if lexeme[visible_indexcounter][1] != 'NUMBAR Literal':
                                                    if lexeme[visible_indexcounter][1] != 'TROOF Literal':
                                                        if lexeme[visible_indexcounter][0] not in varidents: #check if varidents
                                                            if lexeme[visible_indexcounter][0] != "IT":
                                                                if lexeme[visible_indexcounter][0] not in arithmetic: #check if expressions
                                                                    if lexeme[visible_indexcounter][0] not in comparison: #check if comparison
                                                                        
                                                                        if lexeme [visible_indexcounter][0] not in booleans: #check if boolean
                                                                            if lexeme [visible_indexcounter][0] not in inifinitebooleans:
                                                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[visible_indexcounter][0]}>: \n\tIncorrect syntax, see correct syntax. \n\t{lexeme[visible_indexcounter][0]} VISIBLE <x> + <y> where <x> and <y> are either Variable Identifiers, Expressions, String, or IT only3')
                                                                                success = 0
                                                                                break
                                                                            else:
                                                                                #THIS IF THE INIFNITE BOOLEANS (ANY OF AND ALL OF)
                                                                                temp = []
                                                                                tempcounter = visible_indexcounter
                                                                                while tempcounter < len(lexeme):
                                                                                    if lexeme[tempcounter][1] == "Output Delimiter":
                                                                                        break
                                                                                    else:
                                                                                        temp.append(lexeme[tempcounter])
                                                                                        tempcounter+=1
                                                                                result = infiniteBooleanSyntax(temp,h,i)
                                                                                #check kung ano yung irereturn
                                                                                if result is not None:
                                                                                    success = 0
                                                                                    syntaxResult += result
                                                                                    break
                                                                                #means walang error
                                                                                visible_indexcounter = tempcounter 
                                                                        else:
                                                                            #THIS IS THE BOOLEANS
                                                                            temp = []
                                                                            tempcounter = visible_indexcounter
                                                                            while tempcounter < len(lexeme):
                                                                                if lexeme[tempcounter][1] == "Output Delimiter":
                                                                                    break
                                                                                else:
                                                                                    temp.append(lexeme[tempcounter])
                                                                                    tempcounter+=1
                                                                            result = booleanSyntax(temp, h, i)
                                                                            #check kung ano yung irereturn
                                                                            if result is not None:
                                                                                success = 0
                                                                                syntaxResult += result
                                                                                break
                                                                            #move forward!
                                                                            visible_indexcounter = tempcounter
                                                                    else:
                                                                        #THIS IS THE COMPARISONS 
                                                                        temp = []
                                                                        tempcounter = visible_indexcounter
                                                                        while tempcounter < len(lexeme):
                                                                            if lexeme[tempcounter][1] == "Output Delimiter":
                                                                                break
                                                                            else:
                                                                                temp.append(lexeme[tempcounter])
                                                                                tempcounter+=1
                                                                        result = comparisonSyntax(temp, h, i)
                                                                        #check kung ano yung irereturn
                                                                        if result is not None:
                                                                            success = 0
                                                                            syntaxResult += result
                                                                            break
                                                                        #move forward!
                                                                        visible_indexcounter = tempcounter
                                                                else:
                                                                    #get muna yung mga lexeme na pasok sa operation na ito 
                                                                    temp = []
                                                                    tempcounter = visible_indexcounter
                                                                    while tempcounter < len(lexeme):
                                                                        if lexeme[tempcounter][1] == "Output Delimiter":
                                                                            break
                                                                        else:
                                                                            temp.append(lexeme[tempcounter])
                                                                            tempcounter+=1
                                                                    result = arithmeticSyntax(h,arithmetic,temp)
                                                                    #this is to add pag may error po
                                                                    if result[0] == 0:
                                                                        syntaxResult += result[1]
                                                                        success = result[0]
                                                                    visible_indexcounter = tempcounter
                                                            else:
                                                                # +1 since naka zero indexing
                                                                if len(lexeme) != (visible_indexcounter+1):
                                                                    if lexeme[visible_indexcounter+1][1] != "Output Delimiter":
                                                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[visible_indexcounter][0]}>: \n\tIncorrect syntax. Operand should be followed by + ')
                                                                        success = 0
                                                                        break
                                                                    else:
                                                                        visible_indexcounter+=1
                                                                else:
                                                                    visible_indexcounter+=1
                                                        else:
                                                            # +1 since naka zero indexing
                                                            if len(lexeme) != (visible_indexcounter+1):
                                                                if lexeme[visible_indexcounter+1][1] != "Output Delimiter":
                                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[visible_indexcounter][0]}>: \n\tIncorrect syntax. Operand should be followed by + ')
                                                                    success = 0
                                                                    break
                                                                else:
                                                                    visible_indexcounter+=1
                                                            else:
                                                                visible_indexcounter+=1
                                                    else:
                                                        # +1 since naka zero indexing
                                                        if len(lexeme) != (visible_indexcounter+1):
                                                            if lexeme[visible_indexcounter+1][1] != "Output Delimiter":
                                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[visible_indexcounter][0]}>: \n\tIncorrect syntax. Operand should be followed by + ')
                                                                success = 0
                                                                break
                                                            else:
                                                                visible_indexcounter+=1
                                                        else:
                                                            visible_indexcounter+=1
                                                else:
                                                    # +1 since naka zero indexing
                                                    if len(lexeme) != (visible_indexcounter+1):
                                                        if lexeme[visible_indexcounter+1][1] != "Output Delimiter":
                                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[visible_indexcounter][0]}>: \n\tIncorrect syntax. Operand should be followed by + ')
                                                            success = 0
                                                            break
                                                        else:
                                                            visible_indexcounter+=1
                                                    else:
                                                        visible_indexcounter+=1
                                            else:
                                                if len(lexeme) != (visible_indexcounter+1):
                                                    if lexeme[visible_indexcounter+1][1] != "Output Delimiter":
                                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[visible_indexcounter][0]}>: \n\tIncorrect syntax. Operand should be followed by + ')
                                                        success = 0
                                                        break
                                                    else:
                                                        visible_indexcounter+=1
                                                else:
                                                    visible_indexcounter+=1
                                        else:
                                            if len(lexeme) != (visible_indexcounter+1):
                                                if lexeme[visible_indexcounter+1][1] != "Output Delimiter":
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[visible_indexcounter][0]}>: \n\tIncorrect syntax. Operand should be followed by + ')
                                                    success = 0
                                                    break
                                                else:
                                                    visible_indexcounter+=1
                                            else:
                                                visible_indexcounter+=1
                                    else:
                                        if lexeme[visible_indexcounter+2][1] != 'String Delimiter':
                                            syntaxResult += (f'>> SyntaxError in line {h+1} near <{lexeme[visible_indexcounter+2][1]}>: \n\tVariable Identifier ')
                                            success = 0
                                            break
                                        else:
                                            #move forward 
                                            visible_indexcounter +=3
                            break
                    ## COMPARISON SYNTAX - BOTH SAEM
                    # print(lexeme[i][0])
                    # if lexeme[i][0] == 'BOTH SAEM':
                    #     # print(lexeme[i-1][0])
                    #     if isfloat(lexeme[i+1][0]) == False:
                    #         # print("pasok")
                    #         if lexeme[i+1][0] not in varidents:
                    #             syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tBOTH SAEM only accepts NUMBR or NUMBAR type')
                    #             success = 0
                    #             break
                    #         else:
                    #             if isfloat(varidents[lexeme[i+1][0]]) == False:
                    #                 syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tBOTH SAEM only accepts NUMBR or NUMBAR type variable')
                    #                 success = 0
                    #                 break
                        
                    #     if lexeme[i-1][0] not in keyUsingExp:
                    #         # check format of comparison
                    #         if len(lexeme) == 4:
                    #             if lexeme[i+2][0] != 'AN':
                    #                 syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                    #                 success = 0
                    #                 break
                            
                    #             elif isfloat(lexeme[i+3][0]) == False:
                    #                 if lexeme[i+3][0] not in varidents:
                    #                     syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tBOTH SAEM only accepts NUMBR or NUMBAR type')
                    #                     success = 0
                    #                     break
                    #                 else:
                    #                     if isfloat(varidents[lexeme[i+3][0]]) == False:
                    #                         syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tBOTH SAEM only accepts NUMBR or NUMBAR type variable')
                    #                         success = 0
                    #                         break
                                
                    #         elif len(lexeme) == 7 : #or (len(lexeme) == 9 and lexeme[i-1][0] == 'R')
                    #             if lexeme[i+2][0] != 'AN':
                    #                 syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                    #                 success = 0
                    #                 break
                    #             elif lexeme[i+3][0] != 'SMALLR OF' and lexeme[i+3][0] != 'BIGGR OF':
                    #                 syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+2][0]}>: \n\t{lexeme[i+3][0]} is recognized incorrectly. Perhaps you need a 'SMALLR OF' or 'BIGGR OF' keyword?")
                    #                 success = 0
                    #                 break
                    #             elif isfloat(lexeme[i+4][0]) == False and  lexeme[i+4][0] != lexeme[i+1][0]:
                    #                 syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                    #                 success = 0
                    #                 break
                    #             elif lexeme[i+5][0] != 'AN':
                    #                 syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+4][0]}>: \n\t{lexeme[i+5][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                    #                 success = 0
                    #                 break
                    #             elif isfloat(lexeme[i+6][0]) == False:
                    #                 if lexeme[i+6][0] not in varidents:
                    #                     syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                    #                     success = 0
                    #                     break
                    #                 else:
                    #                     if isfloat(varidents[lexeme[i+6][0]]) == False:
                    #                         syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                    #                         success = 0
                    #                         break
                    #         else:
                    #             syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tBOTH SAEM <value> [[AN BIGGR OF|SMALLR OF] <value>] AN <value>')
                    #             success = 0
                    #             break  
                    #     else:
                    #         # print('yey')
                    #         if lexeme[i-1][0] == "VISIBLE":
                    #             # print(lexeme)
                    #             if len(lexeme) == 5:
                    #                 if lexeme[i+2][0] != 'AN':
                    #                     syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                    #                     success = 0
                    #                     break
                            
                    #                 elif isfloat(lexeme[i+3][0]) == False:
                    #                     if lexeme[i+3][0] not in varidents:
                    #                         syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tBOTH SAEM only accepts NUMBR or NUMBAR type')
                    #                         success = 0
                    #                         break
                    #                     else:
                    #                         if isfloat(varidents[lexeme[i+3][0]]) == False:
                    #                             syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tBOTH SAEM only accepts NUMBR or NUMBAR type variable')
                    #                             success = 0
                    #                             break
                    #             elif len(lexeme) == 8:
                    #                 if lexeme[i+2][0] != 'AN':
                    #                     syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                    #                     success = 0
                    #                     break
                    #                 elif lexeme[i+3][0] != 'SMALLR OF' and lexeme[i+3][0] != 'BIGGR OF':
                    #                     syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+2][0]}>: \n\t{lexeme[i+3][0]} is recognized incorrectly. Perhaps you need a 'SMALLR OF' or 'BIGGR OF' keyword?")
                    #                     success = 0
                    #                     break
                    #                 elif isfloat(lexeme[i+4][0]) == False and  lexeme[i+4][0] != lexeme[i+1][0]:
                    #                     syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                    #                     success = 0
                    #                     break
                    #                 elif lexeme[i+5][0] != 'AN':
                    #                     syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+4][0]}>: \n\t{lexeme[i+5][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                    #                     success = 0
                    #                     break
                    #                 elif isfloat(lexeme[i+6][0]) == False:
                    #                     if lexeme[i+6][0] not in varidents:
                    #                         syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                    #                         success = 0
                    #                         break
                    #                     else:
                    #                         if isfloat(varidents[lexeme[i+6][0]]) == False:
                    #                             syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                    #                             success = 0
                    #                             break  
                    #             else:
                    #                 if len(lexeme) == 9 or len(lexeme) == 6:
                    #                     if lexeme[i+7][0] == 'R' or lexeme[i+4][0] == 'R':
                    #                         syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i-1][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\t"+" should be followed by any expression.')
                    #                         success = 0
                    #                         break 
                                
                    # ## COMPARISON SYNTAX - DIFFRINT
                    # if lexeme[i][0] == 'DIFFRINT':
                            
                    #     if isfloat(lexeme[i+1][0]) == False or isfloat(lexeme[i+1][0]) == False:
                    #         syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tDIFFRINT only accepts NUMBR or NUMBAR type')
                    #         success = 0
                    #         break
                        
                    #     if lexeme[i-1][0] not in keyUsingExp:
                    #         if len(lexeme) == 4:
                    #             if lexeme[i+2][0] != 'AN':
                    #                 syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                    #                 success = 0
                    #                 break
                    #             elif isfloat(lexeme[i+3][0]) == False or isfloat(lexeme[i+3][0]) == False:
                    #                 syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tDIFFRINT only accepts NUMBR or NUMBAR type')
                    #                 success = 0
                    #                 break
                    #         elif len(lexeme) == 7:
                    #             if lexeme[i+2][0] != 'AN':
                    #                 syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                    #                 success = 0
                    #                 break
                    #             elif lexeme[i+3][0] != 'SMALLR OF' and lexeme[i+3][0] != 'BIGGR OF':
                    #                 syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+2][0]}>: \n\t{lexeme[i+3][0]} is recognized incorrectly. Perhaps you need a 'SMALLR OF' or 'BIGGR OF' keyword?")
                    #                 success = 0
                    #                 break
                    #             elif isfloat(lexeme[i+4][0]) == False or isfloat(lexeme[i+4][0]) == False:
                    #                 syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                    #                 success = 0
                    #                 break
                    #             elif lexeme[i+5][0] != 'AN':
                    #                 syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+4][0]}>: \n\t{lexeme[i+5][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                    #                 success = 0
                    #                 break
                    #             elif isfloat(lexeme[i+6][0]) == False or isfloat(lexeme[i+6][0]) == False:
                    #                 syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                    #                 success = 0
                    #                 break
                    #         else:
                    #             syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tBOTH SAEM <value> [[AN BIGGR OF|SMALLR OF] <value>] AN <value>')
                    #             success = 0
                    #             break

                    #     else:
                    #         if lexeme[i-1][0] == 'VISIBLE':
                    #             if len(lexeme) == 4:
                    #                 if lexeme[i+2][0] != 'AN':
                    #                     syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                    #                     success = 0
                    #                     break
                    #                 elif isfloat(lexeme[i+3][0]) == False or isfloat(lexeme[i+3][0]) == False:
                    #                     syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tDIFFRINT only accepts NUMBR or NUMBAR type')
                    #                     success = 0
                    #                     break
                    #             elif len(lexeme) == 7:
                    #                 if lexeme[i+2][0] != 'AN':
                    #                     syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                    #                     success = 0
                    #                     break
                    #                 elif lexeme[i+3][0] != 'SMALLR OF' and lexeme[i+3][0] != 'BIGGR OF':
                    #                     syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+2][0]}>: \n\t{lexeme[i+3][0]} is recognized incorrectly. Perhaps you need a 'SMALLR OF' or 'BIGGR OF' keyword?")
                    #                     success = 0
                    #                     break
                    #                 elif isfloat(lexeme[i+4][0]) == False or isfloat(lexeme[i+4][0]) == False:
                    #                     syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                    #                     success = 0
                    #                     break
                    #                 elif lexeme[i+5][0] != 'AN':
                    #                     syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+4][0]}>: \n\t{lexeme[i+5][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                    #                     success = 0
                    #                     break
                    #                 elif isfloat(lexeme[i+6][0]) == False or isfloat(lexeme[i+6][0]) == False:
                    #                     syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                    #                     success = 0
                    #                     break
                    # #             # else:
                                    #check 'yung may +

                    ##INFINITE ARITY BOOLEAN SYNTAX - ANY OF and ALL OF
                    if lexeme[i][0] == 'ANY OF' or lexeme[i][0] == 'ALL OF':
                        result = infiniteBooleanSyntax(lexeme, h, i)
                        if result is not None:
                            success = 0
                            syntaxResult += result
                            break
                        break

                    if lexeme[i][0] in booleans:
                        result = booleanSyntax(lexeme, h, i)
                        if result is not None:
                            success = 0
                            syntaxResult += result
                            break
                        break

                   

                    ## CONCATENATION BLOCK SYNTAX - SMOOSH
                    if lexeme[i][0] == 'SMOOSH':
                        if len(lexeme) <= 2 or len(lexeme)%2 == 1:
                            success = 0
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tSMOOSH <value> AN <value> [[AN <value>]...]')
                            break
                        elif lexeme[i+1][1] not in literals:
                            if lexeme[i+1][1] not in varidents and lexeme[i+1][0] != '"':
                                success = 0
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i+1][0]} is not declared.')
                                break
                        else:
                            for j in range(0, int((len(lexeme)-2)/2)):
                                if lexeme[(j+1)*2][0] != 'AN' and lexeme[(j+1)*2][0] != '"':
                                    success = 0
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[(j+1)*2][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                    break
                                elif lexeme[((j+1)*2)+1][1] not in literals:
                                    if lexeme[((j+1)*2)+1][1] not in varidents and lexeme[((j+1)*2)+1][0] != '"':
                                        success = 0
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[((j+1)*2)+1][0]} is not declared.')
                                        break
                        
                    #  #FOR VARIABLE ASSIGNMENT USING R AND R WITH MAEK
                    # wala pang ano para sa expression
                    if lexeme[i][0] == 'R':
                        if lexeme[i+1][0] == "BOTH SAEM" or lexeme[i+1][0] == "DIFFRINT":
                                # print(lexeme[i+1:])
                                if comparisonSyntax(lexeme[i+1:], h, i):
                                    success = 0
                                    syntaxResult += comparisonSyntax(lexeme[i+1:], h, i)
                                    break
                                break
                        elif lexeme[i+1][0] in booleans:
                            result = booleanSyntax(lexeme[i+1:], h, i)
                            if result is not None:
                                success = 0
                                syntaxResult += result
                                
                            break
                            # continue //
                        elif lexeme[i+1][0] in arithmetic:
                            result = arithmeticSyntax(h,arithmetic,lexeme[i+1:])
                            if result[0] == 0:
                                syntaxResult += result[1]
                                success = result[0]
                                break
                            break
                        
                        if len(lexeme) == 3:
                            if lexeme[i-1][0] not in varidents:
                                # print('hello', lexeme[i-1][0])
                                success = 0
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i-1][0]} is not a variable identifier.')
                                break
                            
                            if lexeme[i+1][1] not in varAssignment_literals and lexeme[i+1][0] not in varidents:
                                    success = 0
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near  <{lexeme[i][0]}>: \n\t{lexeme[i+1][0]} is not a [Variable identifier | NUMBAR Literal | NUMBR Literal | TROOF Literal | YARN Literal].')
                                    break
                            
                            # varidents[lexeme[i-1][0]] = lexeme[i+1]
                        elif len(lexeme) == 5:
                            if lexeme[i+1][0] != '"' and lexeme[i+3][0] != '"':

                                if lexeme[i-1][0] not in varidents or varidents[lexeme[i-1][0]] == 'NOOB':
                                    success = 0
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i-1][0]} is not a variable identifier or is an uninitialized variable.')
                                    break
                                if lexeme[i+1][1] not in varAssignment_literals and lexeme[i+1][0] not in varidents:
                                    if lexeme[i+1][0] != 'MAEK':
                                        success = 0
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near  <{lexeme[i][0]}>: \n\t{lexeme[i+1][0]} is not a [MAEK | Variable identifier | NUMBAR Literal | NUMBR Literal | TROOF Literal | YARN Literal].')
                                        break 
                                if lexeme[i+2][0] != lexeme[i-1][0] or varidents[lexeme[i+2][0]] == 'NOOB':
                                    success = 0
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i+2][0]} and {lexeme[i-1][0]} should be same variable when recasting and must be initialized.')
                                    break
                                if lexeme[i+3][1] != 'Type Literal':
                                    success = 0
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i+3][0]} should be a type literal.')
                                    break
                            break
                        else:
                                success = 0
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tincorrect number of parameters.')
                                break

                        
                    
                    #MAEK TYPECASTING
                    if lexeme[i][0] == 'MAEK':
                        if len(lexeme) >= 6 or len(lexeme) <=2:
                            success = 0
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tincorrect number of parameters.')
                            break
                        else:
                            if lexeme[i+1][0] not in varidents :
                                success = 0
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i+1][0]} should be a variable identifier and must be initialized.')
                                break

                            if lexeme[i-1][0] == 'R' and len(lexeme) == 4:
                                success = 0
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tincorrect number of parameters.')
                                break
                            elif lexeme[i-1][0] == 'R' and len(lexeme) == 5:
                                if lexeme[i-2][0] != lexeme[i+1][0]:
                                    success = 0
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i-2][0]} and {lexeme[i+1][0]} should be same variable for recasting.')
                                    break

                                if lexeme[i+2][1] != 'Type Literal':
                                    success = 0
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i+2][0]} should be a type literal.')
                                    break
                            else:
                                if lexeme[i+2][0] != 'A' and lexeme[i+2][1] != 'Type Literal':
                                    success = 0
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i+2][0]} should be a type literal or an A.')
                                    break
                                elif lexeme[i+2][0] == 'A':
                                    if len(lexeme) == 3:
                                        success = 0
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tincorrect number of parameters.')
                                        break
                                    else:
                                        if lexeme[i+3][1] != 'Type Literal' or len(lexeme) == 3:
                                            success = 0
                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i+2][0]} should be a type literal.')
                                            break

                    #IS NOW A
                    if lexeme[i][0] == 'IS NOW A':
                        # print(lexeme)
                        if len(lexeme) == 3:
                            # print(lexeme[i-1][0])
                            if lexeme[i-1][0] not in varidents or varidents[lexeme[i-1][0]] == 'NOOB':
                                success = 0
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i-1][0]} should be a variable identifier.')
                                break
                            # elif lexeme[i-1][0] not in varidents and varidents[lexeme[i-1][0]] == 'NOOB':
                            #     if lexeme[i+1][0] != "TROOF":
                            #         success = 0
                            #         syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i-1][0]} that is a NOOB can only be implicit typecast to TROOF.')
                            #         break
                            if lexeme[i+1][1] != 'Type Literal':
                                success = 0
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i+1][0]} should be a type literal.')
                                break
                        else:
                            success = 0
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tincorrect number of parameters.')
                            break
                        
                    # #ARITHMETIC OPERATIONS SYNTAX - FOR ALL ARITHMETIC OPERATIONS!
                    if lexeme[i][0] in arithmetic: # 'SUM OF','DIFF OF','PRODUKT OF', 'QUOSHUNT OF', 'MOD OF', 'BIGGR OF', 'SMALLR OF'
                        result = arithmeticSyntax(h,arithmetic,lexeme)
                        #this is to add pag may error po
                        # print(f"result: {result}")
                        if result[0] == 0:
                            syntaxResult += result[1]
                            success = result[0]
                        break    
                    
                    if lexeme[i][0] in comparison:
                        # print(lexeme[i][0])
                        result = comparisonSyntax(lexeme, h, i)
                        if result is not None:
                            success = 0
                            syntaxResult += result
                            
                        break



                    #SWITCH CASES STATEMENTS
                    #temporary tinanggal muna yung ? WTF
                    if lexeme[i][0] == 'WTF':
                        if wtfchecker == 1 or omgchecker !=-1 or omgwtfchecker !=-1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t WTF? is not properly used previously.')
                            success = 0
                            break
                        elif len(lexeme) != 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t WTF? should not be followed by any characters.')
                            success = 0
                            break
                        else:
                            wtfchecker = 1
                        

                    #OMG STATEMENTS 
                    if lexeme[i][0] == "OMG":
                        if wtfchecker == 1: 
                            #to ensure na walang sobra na makukuha
                            if len (lexeme) == 4:
                                if lexeme[i+1][1] != 'String Delimeter':
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Invalid Value Literal')
                                    success = 0
                                    break
                            #to ensure na 2 lang ang pwedeng tanggapin niya 
                            elif len(lexeme) == 2:
                                if lexeme[i+1][1] != "String Delimeter": #check the sting
                                    if lexeme[i+1][1] != 'NUMBR Literal':
                                        if lexeme[i+1][1] != 'NUMBER Literal':
                                            if lexeme[i+1][1] != 'TROOF Literal':
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t OMG Should be followed by Value Literal (NUMBRs, NUMBARs, YARNs, and TROOFs)')
                                                success = 0
                                                break
                                            else:
                                                omgchecker = 1 
                                        else:
                                            omgchecker = 1
                                    else: 
                                        omgchecker = 1
                                else: #check the actual value
                                    if lexeme[i+2][1] != "YARN Literal":
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Invalid Value Literal')
                                        success = 0
                                        break
                                    else:
                                        if lexeme[i+3][1] != "String Delimeter": #check the closing string
                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t OMG Should be followed by Value Literal')
                                            success = 0
                                            break
                                        else:
                                            #check yung next!!    
                                            omgchecker = 1
                            else:
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t OMG Should be followed by 1 Value Literal (NUMBRs, NUMBARs, YARNs, and TROOFs) only!')
                                success = 0
                                break
                        else:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Switch Statements required WTF?, OMG, and OMGWTF?1')
                            success = 0
                            break                                    

                    if lexeme[i][0] == "OMGWTF?":
                        if len(lexeme) != 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t OMGWTF? should not be followed by anything.')
                            success = 0
                            break 
                        elif omgchecker == 1:
                            omgwtfchecker = 1
                        else:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Switch Statements required WTF?, OMG, and OMGWTF?2')
                            success = 0
                            break   

                    if lexeme[i][0] == 'OIC':
                        if len(lexeme) != 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t OIC should not be followed by anything.')
                            success = 0
                            break 
                        elif omgwtfchecker != 1 and omgchecker != 1 and wtfchecker != 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Switch Statements required WTF?, OMG, and OMGWTF?3')
                            success = 0
                            break   
                        else:
                            #we will now reset it 
                            wtfchecker = -1
                            omgchecker = -1
                            omgwtfchecker = -1  


                    #THIS ONE IS CREATED FOR THE GIMMEH INPUT!!
                    if lexeme[i][0] == 'GIMMEH':
                        # print(f"varidents:{varidents}")
                        if len(lexeme[i])<2:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t GIMMEH should be followed by a Variable')
                            success = 0
                            break
                        elif lexeme[i+1][0] not in varidents:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t GIMMEH should be followed by a Variable')
                            success = 0
                            break
                        elif len(lexeme[i])>2:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t GIMMEH should only have a Variable')
                            success = 0
                            break                         
                    
                    #FUNCTION SYNTAX
                    #note: hindi pa nacoconsider dito if valid ba yung parameters (???) not sure if need pa ba yon 
                    if lexeme[i][0] == 'HOW IZ I':
                        if len(lexeme)<2:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t HOW IZ I should have a function name!')
                            success = 0
                            break
                        elif len(lexeme)==2: #no parameters
                            if lexeme[i+1][1] != "Function Identifier":
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t HOW IZ I should be followed by a function name!')
                                success = 0
                                break
                        else: #with parameters
                            if lexeme[i+1][1] != "Function Identifier":
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t HOW IZ I should be followed by a function name!')
                                success = 0
                                break

                            #checking the parameters
                            function_index = 2
                            print(f"lexeme before while loop: {lexeme}")

                            while function_index < len(lexeme):
                                #print(f"function index: {function_index}")
                                if lexeme[function_index][1] != "Parameter Delimiter":
                                    if lexeme[function_index][1] != "Identifier":
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[function_index][0]}>: \n\tIncorrect syntax, see correct syntax: \n\t{lexeme[i][0]} [YR <param1> [AN YR <param2> ...]]1')
                                        success = 0
                                        break
                                    else:
                                        #mag add lang if siya ay Identifer OR AN PARAMETER DELIMITER (AN)
                                        if lexeme[function_index][0] == 'AN':
                                            #check muna yung before ni AN
                                            print("pumasok sa AN")
                                            if len(lexeme) == function_index+1:
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[function_index][0]}>: \n\tIncorrect syntax, see correct syntax: {lexeme[function_index][0]} should only have a precedent of Function Name or AN.1')
                                                    success = 0
                                                    break
                                            if lexeme[function_index-1][1] != 'Identifier' and lexeme[function_index-1][0]!='AN':
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[function_index][0]}>: \n\tIncorrect syntax, see correct syntax: {lexeme[function_index][0]} should only have a precedent of Function Name or AN.2')
                                                    success = 0
                                                    break
                                            #check yung after ni AN
                                            if lexeme[function_index+1][0] != 'YR':
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[function_index][0]}>: \n\tIncorrect syntax, see correct syntax: \n\t{lexeme[i][0]} [YR <param1> [AN YR <param2> ...]]2')
                                                    success = 0
                                                    break
                                            function_index+=1
                                        else:
                                            if len(lexeme) != (function_index+1):
                                                if lexeme[function_index+1][1] == 'Identifier' and lexeme[function_index+1][0] != 'AN':
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[function_index][0]}>: \n\tIncorrect syntax, see correct syntax: \n\t{lexeme[i][0]} [YR <param1> [AN YR <param2> ...]]3')
                                                    success = 0
                                                    break
                                                
                                            if lexeme[function_index-1][0] != 'YR':
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[function_index][0]}>: \n\tIncorrect syntax, see correct syntax: \n\t{lexeme[i][0]} [YR <param1> [AN YR <param2> ...]]4')
                                                success = 0
                                                break
                                            function_index += 1
                                else:
                                    #POSSIBLE PARAMETER DELIMITER IS YR ONLY or AN 
                                    if lexeme[function_index][0] == 'YR':
                                        print("nasa YR ako")
                                        if len(lexeme) == function_index+1:
                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[function_index][0]}>: \n\tIncorrect syntax, see correct syntax: {lexeme[function_index][0]} should only have a precedent of Function Name or AN.3')
                                            success = 0
                                            break
                                        #check before YR 
                                        if lexeme[function_index-1][1] != 'Function Identifier':
                                            if lexeme[function_index-1][1] != 'Parameter Delimiter':
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[function_index][0]}>: \n\tIncorrect syntax, see correct syntax: {lexeme[function_index][0]} should only have a precedent of Function Name or AN.4')
                                                success = 0
                                                break
                                        #check after YR
                                        if lexeme[function_index+1][1] != 'Identifier':
                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[function_index][0]}>: \n\tIncorrect syntax, see correct syntax: {lexeme[function_index][0]} should only have a precedent of Function Name or AN.5')
                                            success = 0
                                            break                                        
                                        function_index+=1
                                        
                                    #checking the AN
                                    elif lexeme[function_index][0] == 'AN':
                                        #check muna yung before ni AN
                                        print("pumasok sa AN")
                                        if len(lexeme) == function_index+1:
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[function_index][0]}>: \n\tIncorrect syntax, see correct syntax: {lexeme[function_index][0]} should only have a precedent of Function Name or AN.6')
                                                success = 0
                                                break
                                        if lexeme[function_index-1][1] != 'Identifier' and lexeme[function_index-1][0]!='AN':
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[function_index][0]}>: \n\tIncorrect syntax, see correct syntax: {lexeme[function_index][0]} should only have a precedent of Function Name or AN.')
                                                success = 0
                                                break
                                        #check yung after ni AN
                                        if lexeme[function_index+1][0] != 'YR':
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[function_index][0]}>: \n\tIncorrect syntax, see correct syntax: \n\t{lexeme[i][0]} [YR <param1> [AN YR <param2> ...]]5')
                                                success = 0
                                                break
                                        function_index+=1
                        functionchecker = 1
                        break
                    
                    #RETURN WITH SOMETHING
                    if lexeme[i][0]=='FOUND YR':
                        if lexeme[i+1][0] not in arithmetic:
                            if lexeme[i+1][0] not in comparison:
                                if lexeme[i+1][0] not in booleans:
                                    if lexeme[i+1][0] not in inifinitebooleans:
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>:  \n\tFOUND YR only accepts expressions!')
                                        success = 0
                                        break
                                    else:
                                        result = booleanSyntax(lexeme[i+1:], h, i)
                                        if result is not None:
                                            success = 0
                                            syntaxResult += result
                                            break
                                else:
                                    result = infiniteBooleanSyntax(lexeme[i+1:], h, i)
                                    if result is not None:
                                        success = 0
                                        syntaxResult += result
                                        break
                            else:
                                result = comparisonSyntax(lexeme[i+1:], h, i)
                                if result is not None:
                                    success = 0
                                    syntaxResult += result
                                    break
                        else:
                            result = arithmeticSyntax(h,arithmetic, lexeme[i+1:])
                            if result[0] == 0:
                                success = result[0]
                                syntaxResult += result[1]
                                break                        
                        break
                    #THIS IS THE RETURN OF EMPTY (USED IN FUNCTIONS AND SWITCH CASE)
                    if lexeme[i][0] == 'GTFO':
                        if functionchecker == -1 and omgchecker == -1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: GTFO should only be used in a Function or Switch-Case!')
                            success = 0
                            break
                        elif len(lexeme)<1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>:  \n\tIncorrect syntax, see correct syntax: \n\t GTFO')
                            success = 0
                            break
                        break

                    #THIS IS THE END OF THE FUNCTION 
                    if lexeme[i][0] == 'IF U SAY SO':
                        if functionchecker == -1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: IF U SAY SO should only be used in a Function!')
                            success = 0
                            break
                        elif len(lexeme)!=1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect syntax, see correct syntax: \n\t IF U SAY SO')
                            success = 0
                            break
                        #reset the checker
                        functionchecker = -1
                else:
                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tStatements must be inside HAI and KTHXBYE')
                    success = 0
                    break

                ## PROGRAM BLOCK SYNTAX - KTHXBYE
                if lexeme[i][0] == 'KTHXBYE' and hasHai == 0:
                        hasKthxbye = 0
                        hasHai = 1
                        break
                else:
                    if lexeme[i][0] == 'KTHXBYE' and hasHai == -1 and hasKthxbye == -1:
                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <KTHXBYE>: \n\tKTHXBYE must be declared after HAI')
                        success = 0
                        break
                    elif lexeme[i][0] == 'KTHXBYE' and hasHai == 0 and hasKthxbye == 1:
                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <KTHXBYE>: \n\tAlready has KTHXBYE; it must be declared once')
                        success = 0
                        break
            lexeme.clear()

    if hasHai == 0 and hasKthxbye == -1:
        syntaxResult += (f'\n>> SyntaxError in line {h+1} in <HAI>: \n\tHAI must be enclosed with KTHXBYE')

    if hasWazzup == 0 and hasBuhbye == -1:
        syntaxResult += (f'\n>> SyntaxError in line {h+1} in <WAZZUP>: \n\tWAZZUP must be enclosed with BUHBYE')

    if success == 1:
        syntaxResult += ('>> No syntax errors.')
            
    return syntaxResult
    