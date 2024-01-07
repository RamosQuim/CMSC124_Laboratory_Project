import keywords
import semantics
import re

#note: 
#VARIABLE ASSIGNMENT USING R = wala pang syntax para sa expression
varidents = {}
exp_lexeme = 0 #this is for the expression checker
prev_checker = 0 #checker for exp_lexeme 
func_parameters = [] 
labelWord = ''

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def getVaridents(text):
    syntax(text)
    # print(varidents, "syntax")
    return varidents

#this part will be repsonsible for analyzing the operations 
def arithmeticSyntax(h,arithmetic, lexeme):
    # print(f"ARITHMETIC SYNTAX LEXEME SA LOOB: {lexeme}")
    # print(varidents)
    tempResult = ''
    success = 1
    result = []
    global func_parameters
    #arithmetic counter  for indexing
    an_counter = 0
    operation_counter = 0
    arithmetic_index = 0
    if lexeme[0][0] in arithmetic: 
        if len(lexeme) < 4:
            success = 0
            tempResult+= (f'\n>> SyntaxError in line {h+1} near <{lexeme[0][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\t{lexeme[0][0]} <x> AN <y>')
            #break
        else:
            #loop para macater yung more than 1 operations
            # print(f"lexeme: {lexeme}")
            while arithmetic_index < len(lexeme):
                # print(f"arithmetic index : {arithmetic_index}")
                # print(f"len(lexeme)-1 = {len(lexeme)} ")
                #this is for hahving another 
                if lexeme[arithmetic_index][1] == 'Arithmetic Operation':
                    #mag add lang siya ng index 
                    arithmetic_index += 1
                    operation_counter += 1
                # this one if may AN !!
                elif lexeme[arithmetic_index][1] == "Parameter Delimiter":
                    #before ng "AN"
                    an_counter += 1
                    if lexeme[arithmetic_index-1][1] != "NUMBR Literal":
                        if lexeme[arithmetic_index-1][1] != "NUMBAR Literal":
                            if lexeme[arithmetic_index-1][1] != "TROOF Literal":
                                if lexeme[arithmetic_index-1][1] == "Identifier":
                                    # print(f"varidents: {varidents}")
                                    if lexeme[arithmetic_index-1][0] not in func_parameters:
                                        if lexeme[arithmetic_index-1][0] not in varidents:
                                            tempResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[arithmetic_index][0]}>: \n\t Variable is not existing')
                                            success = 0
                                            break
                                        else:
                                            #converted to string muna para macheck if ang laman ay numeric or not ba :> Since ang function na ito ay limited to strings only
                                            #GIVING CONSIDERATION TO NOOB
                                            if varidents[lexeme[arithmetic_index-1][0]] != "NOOB":
                                                if str(varidents[lexeme[arithmetic_index-1][0]]).isnumeric() == False:
                                                    # print(f"varidents[lexeme[arithmetic_index-1][0]]: {varidents[lexeme[arithmetic_index-1][0]]}")
                                                    try:
                                                        float_val = float(varidents[lexeme[arithmetic_index-1][0]])
                                                    except ValueError:
                                                        tempResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[arithmetic_index][0]}>: \n\t Variable value should be numeric only')
                                                        success = 0
                                                        break                                                         
                                elif lexeme[arithmetic_index-1][1] != "String Delimiter":
                                    tempResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[arithmetic_index][0]}>: \n\tIncorrect syntax, see correct syntax. \n\t{lexeme[0][0]} <x> AN <y> where <x> and <y> are either NUMBR, NUMBAR,YARN, TROOF, and Variables only')
                                    success = 0
                                    break
                    #after ng "AN"
                    if lexeme[arithmetic_index+1][1] != "NUMBR Literal":
                        if lexeme[arithmetic_index+1][1] != "NUMBAR Literal":
                            if lexeme[arithmetic_index+1][1] != "TROOF Literal":
                                if lexeme[arithmetic_index+1][1] == "Identifier":
                                    # print(f"varidents: {varidents}")
                                    if lexeme[arithmetic_index+1][0] not in func_parameters:
                                        if lexeme[arithmetic_index+1][0] not in varidents:
                                            tempResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[arithmetic_index][0]}>: \n\t Variable is not existing')
                                            success = 0
                                            break
                                        else:
                                            #converted to string muna para macheck if ang laman ay numeric or not ba :> Since ang function na ito ay limited to strings only
                                            #considering noob
                                            if varidents[lexeme[arithmetic_index+1][0]] != "NOOB":
                                                if str(varidents[lexeme[arithmetic_index+1][0]]).isnumeric() == False:
                                                    # print(f"varidents[lexeme[arithmetic_index+1][0]]: {varidents[lexeme[arithmetic_index+1][0]]}")
                                                    try:
                                                        float_val = float(varidents[lexeme[arithmetic_index+1][0]])
                                                    except ValueError:
                                                        tempResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[arithmetic_index][0]}>: \n\t Variable value should be numeric only')
                                                        success = 0
                                                        break  
                                elif lexeme[arithmetic_index+1][1] != 'String Delimiter':
                                    if lexeme[arithmetic_index+1][1] != 'Arithmetic Operation':
                                        tempResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[arithmetic_index][0]}>: \n\tIncorrect syntax, see correct syntax. \n\t{lexeme[0][0]} <x> AN <y> where <x> and <y> are either NUMBR, NUMBAR, YARN, and Variables only')
                                        success = 0
                                        break                                    
                    arithmetic_index +=1
                
                #this is for catering the operands!!
                else:
                    #proceed to if else ganern!!  
                    if lexeme[arithmetic_index][1] != "NUMBR Literal":
                        if lexeme[arithmetic_index][1] != "NUMBAR Literal":
                            if lexeme[arithmetic_index][1] != "TROOF Literal":
                                if lexeme[arithmetic_index][1] == "Identifier":
                                    # print(f"varidents: {varidents}")
                                    if lexeme[arithmetic_index][0] not in func_parameters:
                                        if lexeme[arithmetic_index][0] not in varidents:
                                            tempResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[arithmetic_index][0]}>: \n\t Variable is not existing')
                                            success = 0
                                            break
                                        else:
                                            #converted to string muna para macheck if ang laman ay numeric or not ba :> Since ang function na ito ay limited to strings only
                                            #considering noob
                                            if varidents[lexeme[arithmetic_index][0]] != "NOOB":
                                                if str(varidents[lexeme[arithmetic_index][0]]).isnumeric() == False:
                                                    # print(f"varid/ents[lexeme[arithmetic_index][0]]: {varidents[lexeme[arithmetic_index][0]]}")
                                                    try:
                                                        float_val = float(varidents[lexeme[arithmetic_index][0]])
                                                        arithmetic_index +=1  #added this para di magkaroon ng inifnity loop
                                                    except ValueError:
                                                        tempResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[arithmetic_index][0]}>: \n\t Variable value should be numeric only')
                                                        success = 0
                                                        break
                                                else:
                                                    arithmetic_index +=1  
                                            else:
                                                arithmetic_index+=1
                                    else:
                                        arithmetic_index+=1                                                 
                                elif lexeme[arithmetic_index][1] != "String Delimiter":
                                    tempResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[arithmetic_index][0]}>: \n\t{lexeme[0][0]} only accepts NUMBR, NUMBAR,TROOF, YARN and Variables!')
                                    success = 0
                                    break
                                #if yarn nga siya
                                else:
                                    if lexeme[arithmetic_index+1][0].isnumeric() == False:
                                        tempResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[arithmetic_index][0]}>: \n\tYARN is not a NUMBR or NUMBAR!')
                                        success = 0
                                        break
                                    if lexeme[arithmetic_index+2][1] != "String Delimiter":
                                        tempResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[arithmetic_index][0]}>: \n\tYARN should start and end with " "')
                                        success = 0
                                        break                                                                                                        
                                    arithmetic_index += 3
                            else:
                                arithmetic_index+=1
                        else:
                            arithmetic_index +=1
                    else:
                        arithmetic_index +=1
            if an_counter != operation_counter and success != 0:
                # print(f"arithmetic_index: {arithmetic_index}")
                tempResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[0][0]}>: \n\tTotal no. of {lexeme[0][0]} should be equal to AN')
                success = 0
                
        result.append(success)
        result.append(tempResult)
        return result
    
def comparisonSyntax(lexeme, h, i):
        inf_bool = ['ANY OF', 'ALL OF']
        booleans = ['BOTH OF', 'EITHER OF', 'WON OF', 'NOT']
        arithmetic = ['SUM OF','DIFF OF','PRODUKT OF', 'QUOSHUNT OF', 'MOD OF', 'BIGGR OF', 'SMALLR OF']
        # print(varidents)
        # comparison = ["BOTH SAEM", "DIFFRINT"]
        comparison_index = 0
        check = 0
        # print(lexeme[comparison_index][0])
        # print(len(lexeme))
    # while comparison_index < len(lexeme):
    #     print(varidents)
        print('comparison', lexeme)
        

        if len(lexeme) == 4:
            if isfloat(lexeme[comparison_index+1][0]) == False:
                if lexeme[comparison_index+1][0] not in varidents:
                    success =0
                    check = 1
                    return(f'\n>> SyntaxError in line {h+1} near <{lexeme[comparison_index][0]}>: \n\t{lexeme[comparison_index][0]} only accepts NUMBR or NUMBAR type')
                else:
                # print(isfloat(varidents[lexeme[comparison_index+1][0]]))
                    if isfloat(varidents[lexeme[comparison_index+1][0]]) == False and varidents[lexeme[comparison_index+1][0]] != 'NOOB':
                        success =0
                        check = 1
                        return(f'\n>> SyntaxError in line {h+1} near <{lexeme[comparison_index][0]}>: \n\t{lexeme[comparison_index][0]} only accepts NUMBR or NUMBAR type variable')
            if lexeme[comparison_index+2][0] != 'AN':
                success =0
                check = 1
                return(f"\n>> SyntaxError in line {h+1} near <{lexeme[comparison_index][0]}>: \n\t{lexeme[comparison_index+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
            elif isfloat(lexeme[comparison_index+3][0]) == False:
                if lexeme[comparison_index+3][0] not in varidents:
                    success =0
                    check = 1
                    return(f'\n>> SyntaxError in line {h+1} near <{lexeme[comparison_index][0]}>: \n\t{lexeme[comparison_index][0]} only accepts NUMBR or NUMBAR type')
                else:
                # print(isfloat(varidents[lexeme[comparison_index+1][0]]))
                    if isfloat(varidents[lexeme[comparison_index+3][0]]) == False and varidents[lexeme[comparison_index+3][0]] != 'NOOB':
                        success =0
                        check = 1
                        return(f'\n>> SyntaxError in line {h+1} near <{lexeme[comparison_index][0]}>: \n\t{lexeme[comparison_index][0]} only accepts NUMBR or NUMBAR type variable')
        elif len(lexeme) >4:
            if lexeme[comparison_index+1][0] in arithmetic:
                index = comparison_index+1
                num_operations = 1
                for i in range(2, len(lexeme)):
                    if lexeme[i][0] in arithmetic:
                        num_operations += 1
                        index = i
                num_AN = num_operations * 2 + 3
                result = arithmeticSyntax(h,arithmetic, lexeme[comparison_index+1:num_AN])
                if result[0] == 0:
                    success = result[0]
                    return result[1]
                
                
            elif isfloat(lexeme[comparison_index+1][0]) == False:
                if lexeme[comparison_index+1][0] not in varidents:
                    success =0
                    check = 1
                    return(f'\n>> SyntaxError in line {h+1} near <{lexeme[comparison_index][0]}>: \n\t{lexeme[comparison_index][0]} only accepts NUMBR or NUMBAR type')
                else:
                # print(isfloat(varidents[lexeme[comparison_index+1][0]]))
                    if isfloat(varidents[lexeme[comparison_index+1][0]]) == False and varidents[lexeme[comparison_index+1][0]] != 'NOOB':
                        success =0
                        check = 1
                        return(f'\n>> SyntaxError in line {h+1} near <{lexeme[comparison_index][0]}>: \n\t{lexeme[comparison_index][0]} only accepts NUMBR or NUMBAR type variable')
            elif lexeme[comparison_index+2][0] != 'AN':
                success =0
                check = 1
                return(f"\n>> SyntaxError in line {h+1} near <{lexeme[comparison_index][0]}>: \n\t{lexeme[comparison_index+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
            elif lexeme[comparison_index+3][0] in arithmetic and lexeme[comparison_index+3][0] !='BIGGR OF' and lexeme[comparison_index+3][0] != 'SMALLR OF':
                           
                            index = comparison_index+1
                            num_operations = 1
                            for i in range(2, len(lexeme)):
                                if lexeme[i][0] in arithmetic:
                                    num_operations += 1
                                    index = i
                            num_AN = num_operations * 2 + 3
                            # print(lexeme[comparison_index+3:index+4])
                            result = arithmeticSyntax(h,arithmetic, lexeme[comparison_index+3:num_AN])
                            if result[0] ==0:
                    
                                success = result[0]
                                return result[1]
                    
            elif lexeme[comparison_index+3][0] != 'SMALLR OF' and lexeme[comparison_index+3][0] != 'BIGGR OF':
                success =0
                check = 1
                return(f"\n>> SyntaxError in line {h+1} near <{lexeme[comparison_index+2][0]}>: \n\t{lexeme[comparison_index+3][0]} is recognized incorrectly. Perhaps you need a 'SMALLR OF' or 'BIGGR OF' keyword?")
            elif lexeme[comparison_index+3][0] == 'SMALLR OF' and lexeme[comparison_index+3][0] == 'BIGGR OF':
                if isfloat(lexeme[comparison_index+4][0]) == False: 
                        if lexeme[comparison_index+4][0] != lexeme[comparison_index+1][0]:
                            success =0
                            check = 1
                            return(f"\n>> SyntaxError in line {h+1} near <{lexeme[comparison_index+4][0]}>: \n\t{lexeme[comparison_index+4][0]} and {lexeme[comparison_index+4][0]} should be same")
                elif lexeme[comparison_index+5][0] != 'AN':
                        success =0
                        check = 1
                        return(f"\n>> SyntaxError in line {h+1} near <{lexeme[comparison_index+4][0]}>: \n\t{lexeme[i+5][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                elif isfloat(lexeme[comparison_index+6][0]) == False:
                        if lexeme[comparison_index+6][0] not in varidents:
                            success =0
                            check = 1
                            return(f'\n>> SyntaxError in line {h+1} near <{lexeme[comparison_index][0]}>: \n\t{lexeme[comparison_index][0]} only accepts NUMBR or NUMBAR type')
                        else:
                # print(isfloat(varidents[lexeme[comparison_index+1][0]]))
                            if isfloat(varidents[lexeme[comparison_index+6][0]]) == False and varidents[lexeme[comparison_index+6][0]] != 'NOOB':
                                success =0
                                check = 1
                                return(f'\n>> SyntaxError in line {h+1} near <{lexeme[comparison_index][0]}>: \n\t{lexeme[comparison_index][0]} only accepts NUMBR or NUMBAR type variable')
            # elif lexeme[comparison_index+3][0] in arithmetic:
            #     index = comparison_index+1
            #     num_operations = 1
            #     for i in range(2, len(lexeme)):
            #         if lexeme[i][0] in arithmetic:
            #             num_operations += 1
            #             index = i
            #     num_AN = num_operations + 4
            #     result = arithmeticSyntax(h,arithmetic, lexeme[comparison_index+1:index+4])
            #     if result:
                    
            #         success = result[0]
            #         return result[1]
        else:
            success =   0
            check = 1
            return(f'\n>> SyntaxError in line {h+1} near <{lexeme[comparison_index][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\t{lexeme[comparison_index][0]}<value> [[AN BIGGR OF|SMALLR OF] <value>] AN <value>')

        if check == 0:
            return None
        



def booleanSyntax(lexeme, h, i):
    booleans = ['BOTH OF', 'EITHER OF', 'WON OF', 'NOT']
    literals = ['NUMBR Literal', 'NUMBAR Literal', 'YARN Literal', 'TROOF Literal', 'Type Literal']
    boolean_index = 0
    standby_index = []   # para malaman kung may keyword na need pa ng AN na keyword pag nagnesting
    isComplete = 0 # para malaman if complete na yung operands ng finite boolean, para marestrict na 2 operands lang kahit may nesting
    remaining_keywords = len(lexeme)
    while True:
        if boolean_index < len(lexeme):
            if lexeme[boolean_index][0] not in booleans and lexeme[boolean_index][0] not in varidents and lexeme[boolean_index][1] not in literals:
                return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index][0]} is not a finite boolean keyword.')
            else:
                if lexeme[boolean_index][0] in ["BOTH OF", "EITHER OF", "WON OF"] and isComplete == 0:
                    if remaining_keywords >= 4:
                        if lexeme[boolean_index+1][0] not in booleans:
                            if lexeme[boolean_index+1][0] != 'WIN':
                                if lexeme[boolean_index+1][0] != 'FAIL':
                                    if lexeme[boolean_index+1][1] not in literals and lexeme[boolean_index+1][0] not in varidents:
                                        return (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of {lexeme[boolean_index][0]} must be either WIN OR FAIL.')
                                        
                            elif lexeme[boolean_index+1][0] != 'FAIL':
                                if lexeme[boolean_index+1][0] != 'WIN':
                                    if lexeme[boolean_index+1][1] not in literals and lexeme[boolean_index+1][0] not in varidents:
                                        return (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of {lexeme[boolean_index][0]} must be either WIN OR FAIL.')
                                        

                        else:
                            standby_index.append(boolean_index)
                            standby_index.append(boolean_index+1)
                            boolean_index += 1
                            remaining_keywords -= 1
                            continue

                        if lexeme[boolean_index+2][0] != 'AN':
                            
                            return (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tThere is a need for AN to indicate "and".')
                            

                        if lexeme[boolean_index+3][0] not in booleans:
                            if lexeme[boolean_index+3][0] != 'WIN':
                                if lexeme[boolean_index+3][0] != 'FAIL':
                                    if lexeme[boolean_index+3][1] not in literals and ((standby_index == -1 and lexeme[boolean_index+3][0] == 'AN') or lexeme[boolean_index+3][0] not in varidents):
                                        return (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of {lexeme[boolean_index][0]} must be either WIN OR FAIL.')
                                        
                            elif lexeme[boolean_index+3][0] != 'FAIL':
                                if lexeme[boolean_index+3][0] != 'WIN':
                                    if lexeme[boolean_index+3][1] not in literals and ((standby_index == -1 and lexeme[boolean_index+3][0] == 'AN') or lexeme[boolean_index+3][0] not in varidents):
                                        return (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of {lexeme[boolean_index][0]} must be either WIN OR FAIL.')
                                        
                        else:
                            boolean_index += 3
                            remaining_keywords -= 3
                            continue

                        if ((boolean_index+4) < len(lexeme)):
                            if len(standby_index) != 0 and lexeme[boolean_index+4][0] == 'AN':
                                temp = standby_index.pop()
                                if temp == 0:
                                    isComplete = 1
                            if lexeme[boolean_index+4][0] != 'AN' and boolean_index+4 != len(lexeme)-1:
                                
                                return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+4][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                
                            elif boolean_index+4 == len(lexeme)-1:
                                
                                return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>:\n\tIncorrect number of parameters, see correct syntax. \n\t{lexeme[boolean_index][0]} [WIN|FAIL] AN [WIN|FAIL]')
                        
                        if len(standby_index) == 0:
                            isComplete = 1       
                        boolean_index += 5
                        remaining_keywords -= 5
                    else:
                        
                        return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>\n\tIncorrect number of parameters, see correct syntax. \n\t{lexeme[boolean_index][0]} [WIN|FAIL] AN [WIN|FAIL]')
                        
                elif lexeme[boolean_index][0] == "NOT" and isComplete == 0:
                    if remaining_keywords >= 2:
                        if lexeme[boolean_index+1][0] not in booleans:
                            if lexeme[boolean_index+1][0] != 'WIN':
                                if lexeme[boolean_index+1][0] != 'FAIL':
                                    if lexeme[boolean_index+1][1] not in literals and (lexeme[boolean_index+1][0] not in varidents):
                                        
                                        return (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of NOT must be either WIN OR FAIL.')
                                        
                            elif lexeme[boolean_index+1][0] != 'FAIL':
                                if lexeme[boolean_index+1][0] != 'WIN':
                                    if lexeme[boolean_index+1][1] not in literals and (lexeme[boolean_index+1][0] not in varidents):
                                        
                                        return (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of NOT must be either WIN OR FAIL.')
                                        
                        else:
                            boolean_index += 1
                            remaining_keywords -= 1
                            continue

                        if isComplete == 0:
                            if len(standby_index) != 0:
                                standby_index.pop()
                            if len(standby_index) == 0:
                                isComplete = 1

                        if ((boolean_index+2) < len(lexeme)):
                            if lexeme[boolean_index+2][0] != 'AN' and boolean_index+2 != len(lexeme)-1:
                                
                                return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+2][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                                
                            elif boolean_index+2 == len(lexeme)-1:
                                
                                return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>:\n\tIncorrect number of parameters, see correct syntax. \n\t{lexeme[boolean_index][0]} [WIN|FAIL] AN [WIN|FAIL]')
                                
                        boolean_index += 3
                        remaining_keywords -= 3
                    else:
                        
                        return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>\n\tIncorrect number of parameters, see correct syntax. \n\t{lexeme[boolean_index][0]} [WIN|FAIL] AN [WIN|FAIL]')
                        
                elif (lexeme[boolean_index][0] in varidents or lexeme[boolean_index][1] in literals) and len(standby_index) != 0:
                    if lexeme[boolean_index][0] in varidents or lexeme[boolean_index][1] in literals:
                        boolean_index += 1
                        temp = standby_index.pop()
                        if temp == 0:
                            isComplete = 1
                    else:
                        return (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\t{lexeme[boolean_index][0]} [WIN|FAIL] AN [WIN|FAIL]')
                else:
                    # print(lexeme[boolean_index][0])
                    return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>\n\tIncorrect format, see correct syntax. \n\t{lexeme[i][0]} [WIN|FAIL] AN [WIN|FAIL]')
        else:
            if len(standby_index) != 0:
                return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>\n\tIncorrect format, see correct syntax. \n\t{lexeme[i][0]} [WIN|FAIL] AN [WIN|FAIL]')
            return None        

def infiniteBooleanSyntax(lexeme, h, i):
    boolean_index = 1
    literals = ['NUMBR Literal', 'NUMBAR Literal', 'YARN Literal', 'TROOF Literal', 'Type Literal']
    booleans = ['BOTH OF', 'EITHER OF', 'WON OF', 'NOT']
    standby_index = []   # para malaman kung may keyword na need pa ng AN na keyword pag nagnesting
    if len(lexeme) < 5:
        
        return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\t{lexeme[boolean_index][0]} <finite_bool_expr> AN <finite_bool_expr> [[AN <finite_bool_expr>...] MKAY')
    while boolean_index <= len(lexeme)-2:
        if lexeme[boolean_index][0] not in booleans and lexeme[boolean_index][0] not in varidents and lexeme[boolean_index][1] not in literals:
            if lexeme[boolean_index][0] not in varidents:
                return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index][0]} is not a declared variable.')
            else:
                return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index][0]} is not a finite boolean keyword.')
            
        else:
            if lexeme[boolean_index][0] in ["BOTH OF", "EITHER OF", "WON OF"]:
                if lexeme[boolean_index+1][0] not in booleans:
                    if lexeme[boolean_index+1][0] != 'WIN':
                        if lexeme[boolean_index+1][0] != 'FAIL':
                            if lexeme[boolean_index+1][1] not in literals and lexeme[boolean_index+1][0] not in varidents:
                                
                                return (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of {lexeme[boolean_index][0]} must be either WIN OR FAIL.')
                                
                    elif lexeme[boolean_index+1][0] != 'FAIL':
                        if lexeme[boolean_index+1][0] != 'WIN':
                            if lexeme[boolean_index+1][1] not in literals and lexeme[boolean_index+1][0] not in varidents:
                                
                                return (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of {lexeme[boolean_index][0]} must be either WIN OR FAIL.')
                                
                else:
                    standby_index.append(boolean_index)
                    standby_index.append(boolean_index+1)
                    boolean_index += 1
                    continue

                if lexeme[boolean_index+2][0] != 'AN':
                    
                    return (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tThere is a need for AN to indicate "and".')
                    
                if lexeme[boolean_index+3][0] not in booleans:
                    if lexeme[boolean_index+3][0] != 'WIN':
                        if lexeme[boolean_index+3][0] != 'FAIL':
                            if lexeme[boolean_index+3][1] not in literals and ((standby_index == 0 and lexeme[boolean_index+3][0] == 'AN') or lexeme[boolean_index+3][0] not in varidents):
                                
                                return (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of {lexeme[boolean_index][0]} must be either WIN OR FAIL.')
                                
                    elif lexeme[boolean_index+3][0] != 'FAIL':
                        if lexeme[boolean_index+3][0] != 'WIN':
                            if lexeme[boolean_index+3][1] not in literals and ((standby_index == 0 and lexeme[boolean_index+3][0] == 'AN') or lexeme[boolean_index+3][0] not in varidents):
                                
                                return (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\t Operands of {lexeme[boolean_index][0]} must be either WIN OR FAIL.')
                                
                else:
                    boolean_index += 3
                    continue

                if ((boolean_index+4) < len(lexeme)):
                    if len(standby_index) != 0 and lexeme[boolean_index+4][0] == 'AN':
                        standby_index.pop()
                    if lexeme[boolean_index+4][0] != 'AN' and (lexeme[boolean_index+4][0] != 'MKAY' and boolean_index+4 != len(lexeme)-1):
                        
                        return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+4][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                        
                    elif lexeme[boolean_index+4][0] == 'AN' and lexeme[boolean_index+5][0] == 'MKAY':
                        
                        return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>:\n\tIncorrect number of parameters, see correct syntax. \n\t {lexeme[boolean_index][0]} [WIN|FAIL] AN [WIN|FAIL]')
                        
                boolean_index += 5
            elif lexeme[boolean_index][0] == "NOT":
                if lexeme[boolean_index+1][0] not in booleans:
                    if lexeme[boolean_index+1][0] != 'WIN':
                        if lexeme[boolean_index+1][0] != 'FAIL':
                            if lexeme[boolean_index+1][1] not in literals and lexeme[boolean_index+1][0] not in varidents:
                                
                                return (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of NOT must be either WIN OR FAIL.')
                                
                    elif lexeme[boolean_index+1][0] != 'FAIL':
                        if lexeme[boolean_index+1][0] != 'WIN':
                            if lexeme[boolean_index+1][1] not in literals and lexeme[boolean_index+1][0] not in varidents:
                                
                                return (f'\n>> SyntaxError in line {h+1} near <{lexeme[boolean_index][0]}>: \n\tOperands of NOT must be either WIN OR FAIL.')
                                
                else:
                    boolean_index += 1
                    continue

                if len(standby_index) != 0:
                    standby_index.pop()

                if ((boolean_index+2) < len(lexeme)):
                    if lexeme[boolean_index+2][0] != 'AN' and (lexeme[boolean_index+2][0] != 'MKAY' and boolean_index+2 != len(lexeme)-1):
                        
                        return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+2][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                        
                    elif lexeme[boolean_index+2][0] == 'AN' and lexeme[boolean_index+3][0] == 'MKAY':
                        
                        return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>:\n\tIncorrect number of parameters, see correct syntax. \n\t{lexeme[boolean_index][0]} [WIN|FAIL] AN [WIN|FAIL]')
                        
                boolean_index += 3
            elif lexeme[boolean_index][0] in varidents:
                if ((boolean_index+1) < len(lexeme)):
                    if lexeme[boolean_index+1][0] != 'AN' and (lexeme[boolean_index+1][0] != 'MKAY' and boolean_index+1 != len(lexeme)-1):
                        
                        return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+1][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                        
                    elif lexeme[boolean_index+1][0] == 'AN' and lexeme[boolean_index+2][0] == 'MKAY':
                        
                        return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>:\n\tIncorrect number of parameters, see correct syntax. \n\t{lexeme[boolean_index][0]} [WIN|FAIL] AN [WIN|FAIL]')
                        
                if len(standby_index) != 0:
                    standby_index.pop()
                boolean_index += 2
            elif lexeme[boolean_index][1] in literals:
                if ((boolean_index+1) < len(lexeme)):
                    if lexeme[boolean_index+1][0] != 'AN' and (lexeme[boolean_index+1][0] != 'MKAY' and boolean_index+1 != len(lexeme)-1):
                        
                        return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[boolean_index+1][0]} is recognized incorrectly. Perhaps you need an "AN" keyword?')
                        
                    elif lexeme[boolean_index+1][0] == 'AN' and lexeme[boolean_index+2][0] == 'MKAY':
                        
                        return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>:\n\tIncorrect number of parameters, see correct syntax. \n\t{lexeme[boolean_index][0]} [WIN|FAIL] AN [WIN|FAIL]')
                        
                if len(standby_index) != 0:
                    standby_index.pop()
                boolean_index += 2
            else:
                
                return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>:\n\tIncorrect number of parameters, see correct syntax. \n\t{lexeme[i][0]} [WIN|FAIL] AN [WIN|FAIL]')
                
    else:
        if len(standby_index) != 0:
            
            return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>:\n\tIncorrect number of parameters, see correct syntax. \n\t{lexeme[i][0]} [WIN|FAIL] AN [WIN|FAIL]')
            
        if lexeme[len(lexeme)-1][0] != 'MKAY':
            
            return (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tMKAY must be the end, see correct syntax. \n\t{lexeme[boolean_index][0]} <finite_bool_expr> AN <finite_bool_expr> [[AN <finite_bool_expr>...] MKAY')
            
    
def concatenationSyntax(lexeme, h, i):
    comparison = ['BOTH SAEM', 'DIFFRINT']
    arithmetic = ['SUM OF','DIFF OF','PRODUKT OF', 'QUOSHUNT OF', 'MOD OF', 'BIGGR OF', 'SMALLR OF']
    literals = ['NUMBR Literal', 'NUMBAR Literal', 'YARN Literal', 'TROOF Literal', 'Type Literal']
    varAssignment_literals = ['NUMBR Literal', 'NUMBAR Literal', 'YARN Literal', 'TROOF Literal', 'Type Literal']
    booleans = ['BOTH OF', 'EITHER OF', 'WON OF', 'NOT']
    inifinitebooleans = ['ALL OF', 'ANY OF']
    print(f"lexeme sa smoosh: {lexeme}")
#     # if less than
    # print(f"lexeme in visible start: {lexeme}")
    if len(lexeme) < 2:
        return (f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMOOSH must have a Variable Identifier, Literal, or an Expression')
    else:
        visible_indexcounter = 1
        while visible_indexcounter < len(lexeme):
            # check muna yung "+"
            if lexeme[visible_indexcounter][0] == "AN":
                #check yung before "+"
                if lexeme[visible_indexcounter-1][0] not in varidents:
                    if lexeme[visible_indexcounter-1][1] != 'NUMBR Literal':
                        if lexeme[visible_indexcounter-1][1] != 'NUMBAR Literal':
                            if lexeme[visible_indexcounter-1][1] != 'TROOF Literal':
                                if lexeme[visible_indexcounter-1][1] != 'String Delimiter':
                                    if lexeme[visible_indexcounter-1][1] != 'Concatenation Delimiter':
                                        if lexeme[visible_indexcounter-1][0] != "IT":
                                            return (f'\n>> SyntaxError in line {h+1} near <{lexeme[visible_indexcounter][0]}>: \n\tIncorrect syntax, see correct syntax. \n\t{lexeme[visible_indexcounter][0]} VISIBLE <x> + <y> where <x> and <y> are either Variable Identifiers, Expressions, String, or IT only1')
                                            
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
                                                        return (f'\n>> SyntaxError in line {h+1} near <{lexeme[visible_indexcounter][0]}>: \n\tIncorrect syntax, see correct syntax. \n\t{lexeme[visible_indexcounter][0]} SMOOSH <x> + <y> where <x> and <y> are either Variable Identifiers, Expressions, String, or IT only2')
                                                        
                visible_indexcounter+=1
            else:
                #CHECK MUNA IF STRING SIYA 
                if lexeme[visible_indexcounter][1] != 'String Delimiter':
                    if lexeme[visible_indexcounter][1] != 'TROOF Literal':
                        if lexeme[visible_indexcounter][1] != 'NUMBR Literal':
                            if lexeme[visible_indexcounter][1] != 'NUMBAR Literal':
                                if lexeme[visible_indexcounter][1] != 'TROOF Literal':
                                    if lexeme[visible_indexcounter][0] not in varidents: #check if varidents
                                        if lexeme[visible_indexcounter][0] not in arithmetic: #check if expressions
                                            if lexeme[visible_indexcounter][0] not in comparison: #check if comparison
                                                if lexeme[visible_indexcounter][0] != "IT":
                                                    if lexeme [visible_indexcounter][0] not in booleans: #check if boolean
                                                        if lexeme [visible_indexcounter][0] not in inifinitebooleans:
                                                            return (f'\n>> SyntaxError in line {h+1} near <{lexeme[visible_indexcounter][0]}>: \n\tIncorrect syntax, see correct syntax. \n\t{lexeme[visible_indexcounter][0]} SMOOSH <x> + <y> where <x> and <y> are either Variable Identifiers, Expressions, String, or IT only3')
                                                            
                                                        else:
                                                            #THIS IF THE INIFNITE BOOLEANS (ANY OF AND ALL OF)
                                                            temp = []
                                                            tempcounter = visible_indexcounter
                                                            while tempcounter < len(lexeme):
                                                                if lexeme[tempcounter][0] == "SMOOSH":
                                                                    break
                                                                else:
                                                                    temp.append(lexeme[tempcounter])
                                                                    tempcounter+=1
                                                            result = infiniteBooleanSyntax(temp,h,i)
                                                            #check kung ano yung irereturn
                                                            if result is not None:                                                            
                                                                return result
                                                                
                                                            #means walang error
                                                            visible_indexcounter = tempcounter 
                                                    else:
                                                        #THIS IS THE BOOLEANS
                                                        temp = []
                                                        tempcounter = visible_indexcounter
                                                        while tempcounter < len(lexeme):
                                                            if lexeme[tempcounter][0] == "SMOOSH":
                                                                break
                                                            else:
                                                                temp.append(lexeme[tempcounter])
                                                                tempcounter+=1
                                                        result = booleanSyntax(temp, h, i)
                                                        #check kung ano yung irereturn
                                                        if result is not None:  
                                                            return result
                                                            
                                                        #move forward!
                                                        visible_indexcounter = tempcounter
                                                else:
                                                    visible_indexcounter+=1
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
                                                    
                                                    return result
                                                    
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
                                                return result[1]
                                                
                                            visible_indexcounter = tempcounter
                                    else:
                                        visible_indexcounter += 1
                                else:
                                        visible_indexcounter +=1
                            else:
                                    visible_indexcounter +=1
                        else:
                                visible_indexcounter +=1
                    else:
                        visible_indexcounter +=1
                else:
                    if lexeme[visible_indexcounter+2][1] != 'String Delimiter':
                        return (f'>> SyntaxError in line {h+1} near <{lexeme[visible_indexcounter+2][1]}>: \n\tVariable Identifier ')
                    else:
                        #move forward 
                        visible_indexcounter +=3
        # print("UMABOT SA END NG SYNTAX HUHU")
modif_var = {}

def getModifVaridents(text):
    #  if syntax.syntax(text) == '>> No syntax errors.':
    #     # print("pasok", modified_varidents)
        syntax(text)
        # print(modif_var, "anye")
        return modif_var
    # return 0

def syntax(text):
    # print("in syntax", text)
    global varidents
    global modif_var
    global exp_lexeme
    global prev_checker
    global func_parameters
    # global labelWord

    modif_var.clear()
    varidents.clear()
    syntaxResult = ''
    labelWord = ''
    success = 1
    inyrcount = 0
    outtayrcount = 0
    comparison = ['BOTH SAEM', 'DIFFRINT']
    arithmetic = ['SUM OF','DIFF OF','PRODUKT OF', 'QUOSHUNT OF', 'MOD OF', 'BIGGR OF', 'SMALLR OF']
    literals = ['NUMBR Literal', 'NUMBAR Literal', 'YARN Literal', 'TROOF Literal', 'Type Literal']
    varAssignment_literals = ['NUMBR Literal', 'NUMBAR Literal', 'YARN Literal', 'TROOF Literal', 'Type Literal']
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
    orlychecker = -1
    yarlychecker = -1
    nowaichecker = -1
    functionchecker = -1
    hasobtw = -1
    hastldr = -1
    hasinyr = -1
    hasoutta = -1
    # labelWord = []
    # not_accepted = ['!','-','_','0','1','2','2','3','4','5','6','7','8','9','0','?','~','+','*','&','^','$','#','@','[',']','|',':']
    
    for h in range(0, len(text.splitlines())):
        lexeme = keywords.lex(text.splitlines()[h].lstrip().rstrip())
        if lexeme is not None:
            #this is for the if else 
            print(f"lexeme sa pagstart ng loop: {lexeme}")
            print(f"exp_lexeme sa start: {exp_lexeme}")
            print(f"prev_checker sa start: {prev_checker}")
            if exp_lexeme == 1:
                prev_checker = 1
            #elif exp_lexeme < 1:
            #    exp_lexeme -= 1


            if ['BTW', 'Comment Delimiter'] in lexeme:
                lexeme.pop(lexeme.index(['BTW', 'Comment Delimiter'])+1)
                lexeme.pop(lexeme.index(['BTW', 'Comment Delimiter']))
            
            # if ['OBTW', 'Comment Delimiter'] in lexeme:
            #     lexeme.pop(lexeme.index(['OBTW', 'Comment Delimiter'])+1)
                
            for i in range(0, len(lexeme)):
                # print(f"starting lexeme sa while:{lexeme}")
                # if lexeme[i][0] == 'IM IN YR' :
                #     hasIminyr = 0
                #     checker = 0
                #     # print('im in yr like',hasIminyr)
                #     check = 0
                #     for c in range(i+1, len(lexeme)):
                #         if lexeme[c][0] == 'OBTW':
                #             count = c
                #             checker = 1
                #             break
                                    
                #     if checker == 1:
                #         check = 1
                #         syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                #         success = 0
                #         break
                #     else:
                #         if len(lexeme) >= 7:
                #             if lexeme[i+1][0]in varidents:
                #                 syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n<label> should be in variable format and also unique.')
                #                 success = 0
                #                 break
                #             else:
                #                 matches = re.match(r'\s*[a-zA-Z][a-zA-Z0-9_]*\s*', lexeme[i+1][0])
                #         # label = matches.group(0)
                       
                #                 if matches is None:
                #             # labelWord = ''
                #                     syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n{lexeme[i][0]} <label> must be in a variable format.')
                #                     success = 0
                #                     break
                #                 else:
                #                     labelWord = lexeme[i+1][0]
                #         # else:
                #         #     label = matches.group(0)
                #         #     break
                    
                #             if lexeme[i+2][0] != "UPPIN" and lexeme[i+2][0] != "NERFIN":
                #                 syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n{lexeme[i][0]} <operation> must be either UPPIN or NERFIN.')
                #                 success = 0
                #                 break
                #             elif lexeme[i+3][0] != 'YR':
                #                 syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n{lexeme[i][0]} <operation> must be followed by YR.')
                #                 success = 0
                #                 break
                #             elif lexeme[i+4][0] not in varidents:
                #                 syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n{lexeme[i][0]} <variable> must be declared and initialized.')
                #                 success = 0
                #                 break
                #             elif lexeme[i+4][0] in varidents:
                #                 if isfloat(varidents[lexeme[i+4][0]]) == False: #if hindi number or numbar
                #                     if varidents[lexeme[i+4][0]].isnumeric() == False and varidents[lexeme[i+4][0]]!= 'WIN' and varidents[lexeme[i+4][0]] != 'FAIL': #if hindi "123"
                #                         if varidents[lexeme[i+4][0]] != 'WIN' and 'FAIL':
                #                             syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n{lexeme[i][0]} <variable> must have a value that can be converted to numerical.')
                #                             success = 0
                #                             break
                #             elif lexeme[i+5][0] != "TIL" and lexeme[i+5][0] != 'WILE':
                #                 syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n{lexeme[i][0]} condition teller should be either TIL or WILE.')
                #                 success = 0
                #                 break
                #             else:
                #                 if lexeme[i+6][0] not in booleans:
                #                     if lexeme[i+6][0] not in inifinitebooleans:
                #                         if lexeme[i+6][0] not in comparison:
                #                             syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n{lexeme[i][0]} condition expression should result to WIN or FAIL.')
                #                             success = 0
                #                             break
                #                         else:
                #                             result = comparisonSyntax(lexeme[i+1:], h, i)
                #                             if result is not None:
                #                                 success = 0
                #                                 syntaxResult += result
                #                                 break
                #                     else:
                #                         result = infiniteBooleanSyntax(lexeme[i+1:], h, i)
                #                         if result is not None:
                #                             success = 0
                #                             syntaxResult += result
                #                             break
                #                 else:
                #                     result = booleanSyntax(lexeme[i+1:], h, i)
                #                     if result is not None:
                #                         success = 0
                #                         syntaxResult += result
                #                         break

                        




                ## PROGRAM BLOCK SYNTAX - HAI
                if lexeme[i][0] == 'HAI' and hasHai == -1 and hasKthxbye == -1:
                    # print('HAHA',lexeme)
                    count = 0
                    checker = 0
                    for c in range(i+1, len(lexeme)):
                        if lexeme[c][0] == 'OBTW':
                            count = c
                            checker = 1
                            break

                    if checker == 0:
                        hasHai = 0
                        break
                    else:

                        hasHai = 0
                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <HAI>: \nOBTW must have its own line!!!')
                        success = 0
                        break
                else:
                        if lexeme[i][0] == 'HAI' and hasHai > -1 and hasobtw == -1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <HAI>: \n\tAlready has HAI; it must be declared once')
                            success = 0
                            break
                        elif lexeme[i][0] == 'HAI' and hasKthxbye > -1 and hasobtw == -1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <HAI>: \n\HAI must be declared before KTHXBYE')
                            success = 0
                            break
                if hasHai == 0:
                    ## VARIABLE BLOCK SYNTAX - WAZZUP
                    if lexeme[i][0] == 'WAZZUP' and hasWazzup == -1 and hasBuhbye == -1 and hasobtw == -1:
                        count = 0
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break

                        if checker == 0:
                            hasWazzup = 0
                           
                            break
                        else:

                            hasWazzup = 0
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                    else:
                        if lexeme[i][0] == 'WAZZUP' and hasWazzup > -1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <WAZZUP>: \n\tAlready has WAZZUP; it must be declared once')
                            success = 0
                            break
                        elif lexeme[i][0] == 'WAZZUP' and hasBuhbye > -1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <WAZZUP>: \n\tWAZZUP must be declared before BUHBYE')
                            success = 0
                            break
                    # print("has",hasWazzup)
                    # print(lexeme[i][0], lexeme[i][1])
                    ## VARIABLE DECLARATION SYNTAX
                    if lexeme[i][0] == 'I HAS A' and hasWazzup == 0 and hasobtw == -1:
                        print(len(lexeme))
                        count = 0
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break
                                    
                        if checker == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
                            if len(lexeme) < 2 or lexeme[i+1][1] != 'Variable Identifier':
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tI HAS A must have a variable identifier')
                                success = 0
                                break
                            elif len(lexeme) > 2:
                           
                            
                                if len(lexeme) < 4:
                                    if (lexeme[i+3][1] not in varAssignment_literals and lexeme[i+3][1] != 'Variable Identifier'):
                                        if lexeme[i+3][1] not in literals and lexeme[i+3][1] != 'NOOB': 
                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\tITZ must have a literal or variable identifier')
                                            success = 0
                                            break
                                else:
                                    if lexeme[i+2][0] != 'ITZ':
                                        count = 0
                                        checker = 0
                                        for c in range(i+3, len(lexeme)):
                                            if lexeme[c][0] == 'OBTW':
                                                count = c
                                                checker = 1
                                                break
                                    
                                        if checker == 1:
                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i+3][0]}>: \nOBTW must have its own line!!!')
                                            success = 0
                                            break
                                        else:
                                            syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'ITZ' keyword?")
                                            success = 0
                                            break
                                    else: #if ITZ
                                        count = 0
                                        checker = 0
                                        for c in range(i+3, len(lexeme)):
                                            if lexeme[c][0] == 'OBTW':
                                                count = c
                                                checker = 1
                                                break
                                    # print("itz", checker)
                                        if checker == 1:
                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i+3][0]}>: \nOBTW must have its own line!!!')
                                            success = 0
                                            break
                                        else:
                                            if lexeme[i+3][0] in booleans:#
                                        # print('pasok')
                                                result = booleanSyntax(lexeme[i+3:], h, i)
                                                if result is not None:
                                                    success = 0
                                                    syntaxResult += result
                                                    break
                                                else:
                                                    success = 1
                                                    result = semantics.booleanAnalyzer(lexeme[i+3:], 'no')
                                                    varidents[lexeme[i+1][0]] = result
                                                    modif_var[lexeme[i+1][0]] = result
                                            # print(modif_var)
                                        # break
                                            elif lexeme[i+3][0] == 'ANY OF': 
                                                result = infiniteBooleanSyntax(lexeme[i+3:], h, i)
                                                if result is not None:
                                                    success = 0
                                                    syntaxResult += result
                                                    break
                                                else:
                                                    success = 1
                                                    result = semantics.infiniteBooleanAnalyzer(lexeme[i+3:], 'ANY OF')
                                                    varidents[lexeme[i+1][0]] = result
                                                    modif_var[lexeme[i+1][0]] = result
                                                    break
                                            elif lexeme[i+3][0] == 'ALL OF':
                                                result = infiniteBooleanSyntax(lexeme[i+3:], h, i)
                                                if result is not None:
                                                    success = 0
                                                    syntaxResult += result
                                                    break
                                                else:
                                                    success = 1
                                                    result = semantics.infiniteBooleanAnalyzer(lexeme[i+3:], 'ALL OF')
                                                    varidents[lexeme[i+1][0]] = result
                                                    modif_var[lexeme[i+1][0]] = result
                                                    break
                                            elif lexeme[i+3][0] in arithmetic:
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
                        elif lexeme[i][0] == 'I HAS A' and hasobtw == -1:
                                    count = 0
                                    checker = 0
                                    for c in range(i+1, len(lexeme)):
                                        if lexeme[c][0] == 'OBTW':
                                            count = c
                                            checker = 1
                                            break
                                    # print("itz", checker)
                                    if checker == 1:
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \nOBTW must have its own line!!!')
                                        success = 0
                                        break
                                    else:
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <I HAS A>: \n\tI HAS A statements must be inside WAZZUP and BUHBYE')
                                        success = 0
                                        break
                    ## VARIABLE BLOCK SYNTAX - BUHBYE
                    if lexeme[i][0] == 'BUHBYE' and hasWazzup == 0 and hasobtw == -1:
                                    count = 0
                                    checker = 0
                                    for c in range(i+1, len(lexeme)):
                                        if lexeme[c][0] == 'OBTW':
                                            count = c
                                            checker = 1
                                            break
                                    # print("itz", checker)
                                    if checker == 1:
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                                        success = 0
                                        break
                                    else:
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
                    if lexeme[i][0] == 'VISIBLE' and hasobtw == -1:
                        # print(f"lexeme sa visible: {lexeme}")
                        # print(f"func_parameters: {func_parameters}")
                        # print(f"previous lexeme3:{prev_lexeme}")
                    #     # if less than
                        # print(f"lexeme in visible start: {lexeme}")
                        if len(lexeme) < 2:
                                    count = 0
                                    checker = 0
                                    for c in range(i+1, len(lexeme)):
                                        if lexeme[c][0] == 'OBTW':
                                            count = c
                                            checker = 1
                                            break
                                    # print("itz", checker)
                                    if checker == 1:
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                                        success = 0
                                        break
                                    else:
                                        syntaxResult +=(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tVISIBLE must have a Variable Identifier, Literal, or an Expression')
                                        success = 0
                                        break
                        else:
                            count = 0
                            checker = 0
                            for c in range(i+1, len(lexeme)):
                                if lexeme[c][0] == 'OBTW':
                                    count = c
                                    checker = 1
                                    break
                                    # print("itz", checker)
                            if checker == 1:
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                                success = 0
                                break
                            else:
                                visible_indexcounter = 1
                                while visible_indexcounter < len(lexeme):
                                    # print(f"visible_indexcounter:{visible_indexcounter}")
                                    # print(f"len(lexeme): {len(lexeme)}")
                                    # check muna yung "+"
                                    if lexeme[visible_indexcounter][1] == "Output Delimiter":
                                    #check yung before "+"
                                        if lexeme[visible_indexcounter-1][0] not in varidents:
                                            if lexeme[visible_indexcounter-1][0] not in func_parameters:
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
                                            if lexeme[visible_indexcounter+1][0] not in func_parameters:
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
                                                            if lexeme[visible_indexcounter][0] not in func_parameters:
                                                                if lexeme[visible_indexcounter][0] not in varidents: #check if varidents
                                                                    if lexeme[visible_indexcounter][0] != "IT":
                                                                        if lexeme[visible_indexcounter][0] not in arithmetic: #check if expressions
                                                                            if lexeme[visible_indexcounter][0] not in comparison: #check if comparison
                                                                            
                                                                                if lexeme [visible_indexcounter][0] not in booleans: #check if boolean
                                                                                    if lexeme [visible_indexcounter][0] not in inifinitebooleans:
                                                                                        if lexeme[visible_indexcounter][0] != 'SMOOSH':
                                                                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[visible_indexcounter][0]}>: \n\tIncorrect syntax, see correct syntax. \n\t{lexeme[visible_indexcounter][0]} VISIBLE <x> + <y> where <x> and <y> are either Variable Identifiers, Expressions, String, or IT only3')
                                                                                            success = 0
                                                                                            break
                                                                                        else:
                                                                                        #THIS IF THE SMOOSH
                                                                                            temp = []
                                                                                            tempcounter = visible_indexcounter
                                                                                            while tempcounter < len(lexeme):
                                                                                                if lexeme[tempcounter][1] == "Output Delimiter":
                                                                                                    break
                                                                                                else:
                                                                                                    temp.append(lexeme[tempcounter])
                                                                                                    tempcounter+=1
                                                                                            result = concatenationSyntax(temp,h,i)
                                                                                        #check kung ano yung irereturn
                                                                                            if result is not None:
                                                                                                success = 0
                                                                                                syntaxResult += result
                                                                                                break
                                                                                        #means walang error
                                                                                            visible_indexcounter = tempcounter
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
                    
                    
                    #RETURN WITH SOMETHING
                    if lexeme[i][0]=='FOUND YR' and hasobtw == -1:
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break
                                    
                        if checker == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
                            if lexeme[i+1][0] not in arithmetic:
                                if lexeme[i+1][0] not in comparison:
                                    if lexeme[i+1][0] not in booleans:
                                        if lexeme[i+1][0] not in inifinitebooleans:
                                            if lexeme[i+1][1] != 'Identifier':
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>:  \n\tFOUND YR only accepts expressions!')
                                                success = 0
                                                break
                                            else:
                                                break
                                        else:
                                            result = infiniteBooleanSyntax(lexeme[i+1:], h, i)
                                            if result is not None:
                                                success = 0
                                                syntaxResult += result
                                                break
                                    else:
                                        result = booleanSyntax(lexeme[i+1:], h, i)
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
                            # print(f"MAG END SI FOUND YR")
                            break
                    
                    #THIS IS FOR CALLING
                    if lexeme[i][0] == 'I IZ' and hasobtw == -1:
                        if len(lexeme) < 4:
                            success = 0
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tI IZ <function name> [YR <expression1> [AN YR <expression2> AN YR <expression2>]] MKAY1')
                            break
                        else:
                            #check yung sa harap
                            if lexeme[i+1][1] != "Function Identifier":
                                success = 0
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tI IZ <function name> [YR <expression1> [AN YR <expression2> AN YR <expression2>]] MKAY2')
                                break
                            #check yung dulo
                            elif lexeme[-1][0] != "MKAY":
                                success = 0
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tI IZ <function name> [YR <expression1> [AN YR <expression2> AN YR <expression2>]] MKAY3')
                                break
                            #check yung between
                            else:
                                # print(f"lexeme[i+3][0]:{lexeme[i+3][0]}")
                                #check na yung mga parameters po 
                                if lexeme[i+2][0] != 'YR':
                                    success = 0
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect syntax. \n\t function name should be followed by YR')
                                    break
                                elif lexeme[i+3][0] not in arithmetic:
                                    if lexeme[i+3][0] not in comparison:
                                        if lexeme[i+3][0] not in booleans:
                                            if lexeme[i+3][0] not in inifinitebooleans:
                                                if lexeme[i+3][0] not in varidents:         #DELETE THIS IF HINDI MAG ACCEPT NG VARIDENTS
                                                    success = 0
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tInvalid expression.')
                                                    break
                                else:
                                    #while loop na para sa infinite
                                    calling_index = i+3
                                    # print(f"lexeme before pumasok ng loop: {lexeme[calling_index][0]}")
                                    while calling_index != (len(lexeme)-2): #minus 2 kasi zero indexing + hindi isasama yung dulo 
                                        # print(f"while {calling_index} != {(len(lexeme)-1)}")
                                        # print(f"calling_index:{calling_index}")
                                        if lexeme[calling_index][0] == 'AN':
                                            #check yung before AN
                                            if lexeme[calling_index-1][0] not in arithmetic:
                                                if lexeme[calling_index-1][0] not in comparison:
                                                    if lexeme[calling_index-1][0] not in booleans:
                                                        if lexeme[calling_index-1][0] not in inifinitebooleans:
                                                            success = 0
                                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t There should be a valid expression before AN.')
                                                            break
                                            #check yung after AN
                                            if lexeme[calling_index+1][0] != "YR":
                                                success = 0
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t YR should exist right after AN.')
                                                break
                                            calling_index+=1
                                        elif lexeme[calling_index][0] == 'YR':
                                            #check yung before ni YR
                                            if lexeme[calling_index-1][0] != 'AN':
                                                success = 0
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t There should be an AN before YR.')
                                                break
                                            #check yung after ni YR
                                            if lexeme[calling_index+1][0] not in arithmetic:
                                                if lexeme[calling_index+1][0] not in comparison:
                                                    if lexeme[calling_index+1][0] not in booleans:
                                                        if lexeme[calling_index+1][0] not in inifinitebooleans:
                                                            success = 0
                                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t There should be a valid expression after YR.')
                                                            break
                                            calling_index+=1
                                        else:
                                            #IBIG SABIHIN AY EXPRESSION SIYA!
                                            # print(f"lexeme[calling_index][0]:{lexeme[calling_index][0]}")
                                            # print(f"lexeme[calling_index-1][0]: {lexeme[calling_index-1][0]}")
                                            if lexeme[calling_index-1][0] != 'YR':
                                                success = 0
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t There should be a YR before the expression.')
                                                break
                                            else:
                                                if lexeme[calling_index][0] not in arithmetic:
                                                    if lexeme[calling_index][0] not in comparison:
                                                        if lexeme[calling_index][0] not in booleans:
                                                            if lexeme[calling_index][0] not in inifinitebooleans:
                                                                if lexeme[calling_index][0] not in varidents:   #DELETE THIS IF HINDI TATANGGAPIN SI VARIDENTS
                                                                    success = 0
                                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tInvalid expression.')
                                                                    break
                                                                else:
                                                                    calling_index += 1
                                                            else:
                                                                temp = []
                                                                temp_index = calling_index
                                                                while True:
                                                                    if lexeme[temp_index+1][0] == 'MKAY':
                                                                        temp.append(lexeme[temp_index]) #nag add pa rin dito para ma add yung pinakadulo bago mag MKAY 
                                                                        temp_index +=1
                                                                        break
                                                                    elif lexeme[temp_index+1][0] == 'AN' and lexeme[temp_index+2][0] == 'YR':
                                                                        temp.append(lexeme[temp_index]) #nag append pa rin dito para masama yung pinakadulo bago mag AN or YR
                                                                        temp_index +=1
                                                                        break
                                                                    else:
                                                                        temp.append(lexeme[temp_index])
                                                                        temp_index +=1

                                                                result = infiniteBooleanSyntax(temp, h, i)
                                                                if result is not None:
                                                                    success = 0
                                                                    syntaxResult += result
                                                                    break
                                                                calling_index = temp_index
                                                        else:
                                                            temp = []
                                                            temp_index = calling_index
                                                            while True:
                                                                if lexeme[temp_index+1][0] == 'MKAY':
                                                                        temp.append(lexeme[temp_index]) #nag append para masama yung dulo
                                                                        temp_index +=1
                                                                        break
                                                                elif lexeme[temp_index+1][0] == 'AN' and lexeme[temp_index+2][0] == 'YR':
                                                                    temp.append(lexeme[temp_index]) #nag append para masama yung dulo
                                                                    temp_index +=1
                                                                    break
                                                                else:
                                                                    temp.append(lexeme[temp_index])
                                                                    temp_index +=1
                                                            result = booleanSyntax(temp, h, i)
                                                            if result is not None:
                                                                success = 0
                                                                syntaxResult += result
                                                                break
                                                            calling_index = temp_index
                                                    else:
                                                        temp = []
                                                        temp_index = calling_index
                                                        while True:
                                                            if lexeme[temp_index+1][0] == 'MKAY':
                                                                    temp.append(lexeme[temp_index]) #nag append para masama yung dulo
                                                                    temp_index +=1
                                                                    break
                                                            elif lexeme[temp_index+1][0] == 'AN' and lexeme[temp_index+2][0] == 'YR':
                                                                temp.append(lexeme[temp_index]) #nag append para masama yung dulo
                                                                temp_index +=1
                                                                break
                                                            else:
                                                                temp.append(lexeme[temp_index])
                                                                temp_index +=1
                                                        result = comparisonSyntax(temp, h, i)
                                                        if result is not None:
                                                            success = 0
                                                            syntaxResult += result
                                                            break
                                                        calling_index = temp_index
                                                else:
                                                    temp = []
                                                    temp_index = calling_index
                                                    while True:
                                                        if lexeme[temp_index+1][0] == 'MKAY':
                                                                temp.append(lexeme[temp_index]) #nag append para masama yung dulo
                                                                break
                                                        elif lexeme[temp_index+1][0] == 'AN' and lexeme[temp_index+2][0] == 'YR':
                                                            temp.append(lexeme[temp_index]) #nag append para masama yung dulo
                                                            temp_index +=1
                                                            break
                                                        else:
                                                            temp.append(lexeme[temp_index])
                                                            temp_index +=1
                                                    result = arithmeticSyntax(h,arithmetic, temp)
                                                    if result[0] == 0:
                                                        success = result[0]
                                                        syntaxResult += result[1]
                                                        break 
                                                    calling_index = temp_index
                                    break
                        break
                            

                                
                    ##INFINITE ARITY BOOLEAN SYNTAX - ANY OF and ALL OF
                    if lexeme[i][0] == 'ANY OF' or lexeme[i][0] == 'ALL OF' and hasobtw == -1:
                        count = 0
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break
                                    # print("itz", checker)
                        if checker == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
                            result = infiniteBooleanSyntax(lexeme, h, i)
                            if result is not None:
                                success = 0
                                syntaxResult += result
                                break
                            exp_lexeme = 1 
                            break
                        

                    if lexeme[i][0] in booleans and hasobtw == -1:
                        count = 0
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break
                                    # print("itz", checker)
                        if checker == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
                            result = booleanSyntax(lexeme, h, i)
                            if result is not None:
                                success = 0
                                syntaxResult += result
                                break
                            exp_lexeme = 1 #for if else 
                            break

                   

                    ## CONCATENATION BLOCK SYNTAX - SMOOSH
                    if lexeme[i][0] == 'SMOOSH' and hasobtw == -1:
                        count = 0
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break
                                    # print("itz", checker)
                        if checker == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
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
                    if lexeme[i][0] == 'R' and hasobtw == -1:
                        count = 0
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break
                                    # print("itz", checker)
                        if checker == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
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
                            elif lexeme[i+1][0] == "SMOOSH":
                            # print(lexeme[i+1:])
                                if concatenationSyntax(lexeme[i+1:], h, i):
                                    success = 0
                                    syntaxResult += concatenationSyntax(lexeme[i+1:], h, i)
                                    break
                                break
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
                            elif len(lexeme) == 5:
                                if lexeme[i+1][0] != '"' and lexeme[i+3][0] != '"':

                                    if lexeme[i-1][0] not in varidents:
                                        success = 0
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t{lexeme[i-1][0]} is not a variable identifier or is an uninitialized variable.')
                                        break
                                    if lexeme[i+1][1] not in varAssignment_literals and lexeme[i+1][0] not in varidents:
                                        if lexeme[i+1][0] != 'MAEK':
                                            success = 0
                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near  <{lexeme[i][0]}>: \n\t{lexeme[i+1][0]} is not a [MAEK | Variable identifier | NUMBAR Literal | NUMBR Literal | TROOF Literal | YARN Literal].')
                                            break 
                                    if lexeme[i+2][0] != lexeme[i-1][0]:
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
                    if lexeme[i][0] == 'MAEK' and hasobtw == -1:
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break
                                    
                        if checker == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
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
                    if lexeme[i][0] == 'IS NOW A' and hasobtw == -1:
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break
                                    
                        if checker == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
                        # print(lexeme)
                            if len(lexeme) == 3:
                            # print(lexeme[i-1][0])
                                if lexeme[i-1][0] not in varidents:
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
                    if lexeme[i][0] in arithmetic and hasobtw == -1: # 'SUM OF','DIFF OF','PRODUKT OF', 'QUOSHUNT OF', 'MOD OF', 'BIGGR OF', 'SMALLR OF'
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break
                                    
                        if checker == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
                            # print(f"lexeme sa arithmeticsyntax:{lexeme}")
                            result = arithmeticSyntax(h,arithmetic,lexeme)
                        #this is to add pag may error po
                        # print(f"result: {result}")
                            if result is not None:
                                if result[0] == 0:
                                    syntaxResult += result[1]
                                    success = result[0]
                            exp_lexeme = 1
                            break    
                            
                    
                    if lexeme[i][0] in comparison and hasobtw == -1:
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break
                                    
                        if checker == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
                            #pwede pa ito mamooooove                            
                            exp_lexeme = 1
                            print(f"pumasok sa comparison kaya ang exp_lexeme: {exp_lexeme}")
                            if lexeme[i-1][0] == "":
                                result = comparisonSyntax(lexeme, h, i)
                                if result is not None:
                                    success = 0
                                    syntaxResult += result

                                break



                    #SWITCH CASES STATEMENTS
                    #temporary tinanggal muna yung ? WTF
                    if lexeme[i][0] == 'WTF' and hasobtw == -1:
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break
                                    
                        if checker == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
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
                    if lexeme[i][0] == "OMG" and hasobtw == -1:
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break
                                    
                        if checker == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
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

                    if lexeme[i][0] == "OMGWTF" and hasobtw == -1:
                        print("omgwtf",len(lexeme), lexeme)
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break
                                    
                        if checker == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
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

                    if lexeme[i][0] == 'OIC' and hasobtw == -1:
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break
                                    
                        if checker == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
                            if len(lexeme) != 1:
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t OIC should not be followed by anything.')
                                success = 0
                                break 


                            elif wtfchecker != 1 and orlychecker != 1:
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t OIC can only be used in If-Then and Switch Statements.')
                                success = 0
                                break  
                            elif wtfchecker == 1:
                                print(f"omgwtfchecker sa wtf: {omgwtfchecker}")
                                print(f"omgchecker sa wtf: {omgchecker}")
                                if omgchecker !=1 and wtfchecker !=1:
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Switch Statements required WTF?, OMG, and OMGWTF?3')
                                    success = 0
                                    break
                                else:
                                    if omgchecker == 1:
                                        if omgwtfchecker != 1:
                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Switch Statements required WTF?, OMG, and OMGWTF?8')
                                            success = 0
                                            break
                                        else:
                                            wtfchecker = -1
                                            omgchecker = -1
                                            omgwtfchecker = -1
                                    else:
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Switch Statements required WTF?, OMG, and OMGWTF?1')
                                        success = 0
                                        break
                                    
                            elif orlychecker == 1:
                                if yarlychecker != 1 and nowaichecker !=1:
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t If-Then Statements required O RLY?, YA RLY, and NO WAI')
                                    success = 0
                                    break
                                else:
                                    if yarlychecker == 1 and nowaichecker != 1: #if lang ang nagamit 
                                        orlychecker = -1
                                        yarlychecker = -1
                                        nowaichecker = -1  
                                    else: #means lahat ay gamit 
                                        orlychecker = -1
                                        yarlychecker = -1
                                        nowaichecker = -1 



                    #THIS ONE IS CREATED FOR THE GIMMEH INPUT!!
                    if lexeme[i][0] == 'GIMMEH' and hasobtw == -1:
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break
                                    
                        if checker == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
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

                    #IF THEN SYNTAX
                    #O RLY
                    if lexeme[i][0] == 'O' and hasobtw == -1:
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break
                                    
                        if checker == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
                            # print(f"previous lexeme1: {prev_lexeme}")
                            if len(lexeme) != 2:
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <O RLY?>: \n\t O RLY? should not have other characters in the same line.')
                                success = 0
                                break                 
                            else:
                                if lexeme[i+1][0] != 'RLY':
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <O RLY?>: \n\t Incorrect Syntax.')
                                    success = 0
                                    break 
                            #COMMENT OUT KO MUNA KASI AYAW GUMANA NETO HUHU
                            #check yung previous line expression
                            print(f"prev checker sa o rly: {prev_checker}")
                            if prev_checker != 1:
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <O RLY?>: \n\t Previous Expression is not valid.')
                                success = 0
                                break 
                        print(f"ya rly: {yarlychecker}")
                        print(f"no wai: {nowaichecker}")
                        orlychecker = 1
                    #YA RLY
                    if lexeme[i][0] == 'YA' and hasobtw == -1:
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break
                                    
                        if checker == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
                            if len(lexeme)!= 2:  
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <YA RLY>: \n\t YA RLY should not have other characters in the same line.')
                                success = 0
                                break
                            else:
                                if lexeme[i+1][0] != 'RLY':
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <YA RLY>: \n\t Incorrect Syntax.')
                                    success = 0
                                    break 
                                elif orlychecker != 1:
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <YA RLY>: \n\t YA RLY should have O RLY? in the previous lines.')
                                    success = 0
                                    break 
                                else:
                                    yarlychecker =1
                    #NO WAI
                    if lexeme[i][0] == 'NO' and hasobtw == -1:
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break
                                    
                        if checker == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
                            if len(lexeme)!= 2:  
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <NO WAI>: \n\t NO WAI should not have other characters in the same line.')
                                success = 0
                                break
                            else:
                                if lexeme[i+1][0] != 'WAI':
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <NO WAI>: \n\t Incorrect Syntax.')
                                    success = 0
                                    break
                                elif yarlychecker != 1:
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <NO WAI>: \n\t YA RLY should be existing before NO WAI.')
                                    success = 0
                                    break 
                                else:
                                    nowaichecker = 1                                
                    
                    #FUNCTION SYNTAX
                    #note: hindi pa nacoconsider dito if valid ba yung parameters (???) not sure if need pa ba yon 
                    if lexeme[i][0] == 'HOW IZ I' and hasobtw == -1:
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break
                                    
                        if checker == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
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
                                # print(f"lexeme before while loop: {lexeme}")

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
                                                #PARAMETER SIYA IBIG SABIHIN
                                                if len(lexeme) != (function_index+1):
                                                    if lexeme[function_index+1][1] == 'Identifier' and lexeme[function_index+1][0] != 'AN':
                                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[function_index][0]}>: \n\tIncorrect syntax, see correct syntax: \n\t{lexeme[i][0]} [YR <param1> [AN YR <param2> ...]]3')
                                                        success = 0
                                                        break
                                                
                                                if lexeme[function_index-1][0] != 'YR':
                                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[function_index][0]}>: \n\tIncorrect syntax, see correct syntax: \n\t{lexeme[i][0]} [YR <param1> [AN YR <param2> ...]]4')
                                                    success = 0
                                                    break
                                                func_parameters.append(lexeme[function_index][0])
                                                print(f"function parameters: {func_parameters}")
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
                        
                    #THIS IS THE RETURN OF EMPTY (USED IN FUNCTIONS AND SWITCH CASE)
                    if lexeme[i][0] == 'GTFO' and hasobtw == -1:
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break
                                    
                        if checker == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
                            if functionchecker == -1 and omgchecker == -1:
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: GTFO should only be used in a Function or Switch-Case!')
                                success = 0
                                break
                            elif len(lexeme)<1:
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>:  \n\tIncorrect syntax, see correct syntax: \n\t GTFO')
                                success = 0
                                break
                            break

                    if lexeme[i][0] == 'OBTW':
                        hasobtw = 0
                    
                    if lexeme[i][0] == 'TLDR':
                        hastldr = 0
                        if hasobtw == -1:
                            hastldr = -1
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>:  \n\tthere should be an OBTW before TLDR')
                            success = 0
                            break
                        else: hasobtw = -1

                    #THIS IS THE END OF THE FUNCTION 
                    if lexeme[i][0] == 'IF U SAY SO' and hasobtw == -1:
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break
                                    
                        if checker == 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
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

                    if lexeme[i][0] == 'IM IN YR' and hasobtw == -1 :
                        hasinyr = 0
                        checker = 0
                        inyrcount += 1
                        # print('im in yr like',hasIminyr)
                        check = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break

                        if checker == 1:
                            check = 1
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
                            if len(lexeme) >= 7:
                                if lexeme[i+1][0]in varidents:
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n<label> should be in variable format and also unique.')
                                    success = 0
                                    break
                                else:
                                    matches = re.match(r'\s*[a-zA-Z][a-zA-Z0-9_]*\s*', lexeme[i+1][0])
                            # label = matches.group(0)
                       
                                    if matches is None:
                                # labelWord = ''
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n{lexeme[i][0]} <label> must be in a variable format.')
                                        success = 0
                                        break
                                    else:
                                        labelWord = lexeme[i+1][0]
                            # else:
                            #     label = matches.group(0)
                            #     break
                    
                                if lexeme[i+2][0] != "UPPIN" and lexeme[i+2][0] != "NERFIN":
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n{lexeme[i][0]} <operation> must be either UPPIN or NERFIN.')
                                    success = 0
                                    break
                                elif lexeme[i+3][0] != 'YR':
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n{lexeme[i][0]} <operation> must be followed by YR.')
                                    success = 0
                                    break
                                elif lexeme[i+4][0] not in varidents:
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n{lexeme[i][0]} <variable> must be declared and initialized.')
                                    success = 0
                                    break
                                elif lexeme[i+4][0] in varidents:
                                    if isfloat(varidents[lexeme[i+4][0]]) == False: #if hindi number or numbar
                                        if varidents[lexeme[i+4][0]].isnumeric() == False and varidents[lexeme[i+4][0]]!= 'WIN' and varidents[lexeme[i+4][0]] != 'FAIL' and varidents[lexeme[i+4][0]] != 'NOOB': #if hindi "123"
                                            # if varidents[lexeme[i+4][0]] != 'WIN' and 'FAIL':
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n{lexeme[i][0]} <{lexeme[i+4][0]}> must have a value that can be converted to numerical.')
                                                success = 0
                                                break
                                elif lexeme[i+5][0] != "TIL" and lexeme[i+5][0] != 'WILE':
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n{lexeme[i][0]} condition teller should be either TIL or WILE.')
                                    success = 0
                                    break
                                else:
                                    if lexeme[i+6][0] not in booleans:
                                        if lexeme[i+6][0] not in inifinitebooleans:
                                            if lexeme[i+6][0] not in comparison:
                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n{lexeme[i][0]} condition expression should result to WIN or FAIL.')
                                                success = 0
                                                break
                                            else:
                                                    result = comparisonSyntax(lexeme[i+6:], h, i)
                                                    if result is not None:
                                                        success = 0
                                                        syntaxResult += result
                                                        break
                                                    break
                                        else:
                                            result = infiniteBooleanSyntax(lexeme[i+6:], h, i)
                                            if result is not None:
                                                success = 0
                                                syntaxResult += result
                                                break
                                            break
                                    else:
                                        print("ipinapasa",lexeme[i+6:])
                                        result = booleanSyntax(lexeme[i+6:], h, i)
                                        if result is not None:
                                            success = 0
                                            syntaxResult += result
                                            break
                                        break
                        
                        # if check == 0:
                        #     hasIminyr = 0
                        #     break
                    # print('im in yr2',hasIminyr)

                    if lexeme[i][0] == 'IM OUTTA YR' and hasobtw == -1:
                        hasoutta = 0
                        outtayrcount +=1
                        c = 0
                        checker = 0
                        for c in range(i+1, len(lexeme)):
                            if lexeme[c][0] == 'OBTW':
                                count = c
                                checker = 1
                                break
                                    
                        if checker == 1:
                            check = 1
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \nOBTW must have its own line!!!')
                            success = 0
                            break
                        else:
                            hasoutta = 0
                            if len(lexeme) == 2:
                                if hasinyr == 0:
                                    if lexeme[i+1][0] != labelWord:
                                        # print("is this check?:", labelWord, "and", lexeme[i+1][0])
                                        c = 1
                                        syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: <label> must be the same as you used to IM IN YR')
                                        success = 0
                                        break
                                    # hasoutta = -1
                                    # hasIminyr = -1
                                else:
                                    
                                    c = 1
                                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: there must be IM IN YR before this!')
                                    success = 0
                                    hasOutta = -1
                                    break
                            else:
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: Wrong syntax! It should be IM OUTTA YR <label>')
                                success = 0
                                break
                    
                    # print("anona" , hasIminyr)
                    
                    # if hasIminyr == 0 and hasOutta == -1:
                        
                    #     syntaxResult += (f'\n>> SyntaxError in line {h+1} near <IM IN YR>: IM IN YR should stop with OUTTA YR')
                    #     success = 0
                    #     hasIminyr = -1
                    #     hasOutta == -1
                    #     break

                    # print("hasIm", hasIminyr, " hasOUt", hasOutta, "hasHai", hasHai)
                    



                    
                    

                    
                    # break
                    # break
                    
                    
                else:
                    syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tStatements must be inside HAI and KTHXBYE')
                    success = 0
                    break

                ## PROGRAM BLOCK SYNTAX - KTHXBYE
                if lexeme[i][0] == 'KTHXBYE' and hasHai == 0 and hasobtw == -1:
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
            #sa dulo pag both ay naging 
            print(f"prev_checker sa end: {prev_checker}")
            print(f"exp_lexeme sa end: {exp_lexeme}")
            if prev_checker == 1 and exp_lexeme == 1:
                prev_checker = 0
                exp_lexeme = 0
            lexeme.clear()

    if outtayrcount != inyrcount:
        success = 0
        syntaxResult += (f'\n>> SyntaxError in line {h+1} in <IM IN YR> & <IM OUTTA YR>: \n\tNumber of IM IN YR and IM OUTTA YR is not equal so there is a for loop that do not have end clause of begging clause! ')
    else:
        outtayrcount = 0
        inyrcount = 0
    if hasinyr == 0 and hasoutta == -1:
        success = 0
        syntaxResult += (f'\n>> SyntaxError in line {h+1} in <IM IN YR>: \n\tIM IN YR must be enclosed with IM OUTTA <label>')
    else:
        hasinyr = -1
        hasoutta = -1

    if hasobtw == 0 and hastldr == -1:
        success = 0
        syntaxResult += (f'\n>> SyntaxError in line {h+1} in <OBTW>: \n\tOBTW must be enclosed with TLDR')
    else:
        hasobtw = -1
        hastldr = -1

    if hasHai == 0 and hasKthxbye == -1:
        syntaxResult += (f'\n>> SyntaxError in line {h+1} in <HAI>: \n\tHAI must be enclosed with KTHXBYE')

    if hasWazzup == 0 and hasBuhbye == -1:
        syntaxResult += (f'\n>> SyntaxError in line {h+1} in <WAZZUP>: \n\tWAZZUP must be enclosed with BUHBYE')

    if success == 1:
        syntaxResult += ('>> No syntax errors.')
            
    return syntaxResult