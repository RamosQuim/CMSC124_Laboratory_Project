import keywords
import semantics

#note: 
#VARIABLE ASSIGNMENT USING R = wala pang syntax para sa expression
varidents = {}
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
    # print(varidents)
    tempResult = ''
    success = 1
    result = []
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

#parameters: lexeme - ang ipapasa here is from the lexeme with index kung saan nagstart 'yung both saem of diffrint up 
    #hanggang sa end ng format lang ng both saem or diffrint so either lexeme[i:i+4] or lexeme[i:i+7] kapag may biggr of | smallr of
def comparisonSyntax(lexeme, h, i):
        # comparison = ["BOTH SAEM", "DIFFRINT"]
        comparison_index = 0
        check = 0
        # print(lexeme[comparison_index][0])
        # print(len(lexeme))
    # while comparison_index < len(lexeme):
    #     print(varidents)
        if isfloat(lexeme[comparison_index+1][0]) == False:
            if lexeme[comparison_index+1][0] not in varidents:
                success =0
                check = 1
                return(f'\n>> SyntaxError in line {h+1} near <{lexeme[comparison_index][0]}>: \n\t{lexeme[comparison_index][0]} only accepts NUMBR or NUMBAR type')
            else:
                # print(isfloat(varidents[lexeme[comparison_index+1][0]]))
                if isfloat(varidents[lexeme[comparison_index+1][0]]) == False:
                    success =0
                    check = 1
                    return(f'\n>> SyntaxError in line {h+1} near <{lexeme[comparison_index][0]}>: \n\t{lexeme[comparison_index][0]} only accepts NUMBR or NUMBAR type variable')

        if len(lexeme) == 4:
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
                    if isfloat(varidents[lexeme[comparison_index+3][0]]) == False:
                        success =0
                        check = 1
                        return(f'\n>> SyntaxError in line {h+1} near <{lexeme[comparison_index][0]}>: \n\t{lexeme[comparison_index][0]} only accepts NUMBR or NUMBAR type variable')
        elif len(lexeme) == 7:
            if lexeme[comparison_index+2][0] != 'AN':
                success =0
                check = 1
                return(f"\n>> SyntaxError in line {h+1} near <{lexeme[comparison_index][0]}>: \n\t{lexeme[comparison_index+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
            elif lexeme[comparison_index+3][0] != 'SMALLR OF' and lexeme[comparison_index+3][0] != 'BIGGR OF':
                success =0
                check = 1
                return(f"\n>> SyntaxError in line {h+1} near <{lexeme[comparison_index+2][0]}>: \n\t{lexeme[comparison_index+3][0]} is recognized incorrectly. Perhaps you need a 'SMALLR OF' or 'BIGGR OF' keyword?")
            elif isfloat(lexeme[comparison_index+4][0]) == False and lexeme[comparison_index+4][0] != lexeme[comparison_index+1][0]:
                success =0
                check = 1
                return(f'\n>> SyntaxError in line {h+1} near <{lexeme[comparison_index][0]}>: \n\t{lexeme[comparison_index][0]} SMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
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
                    if isfloat(varidents[lexeme[comparison_index+6][0]]) == False:
                        success =0
                        check = 1
                        return(f'\n>> SyntaxError in line {h+1} near <{lexeme[comparison_index][0]}>: \n\t{lexeme[comparison_index][0]} only accepts NUMBR or NUMBAR type variable')
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
            
    

modif_var = {}

def getModifVaridents(text):
    #  if syntax.syntax(text) == '>> No syntax errors.':
    #     # print("pasok", modified_varidents)
        syntax(text)
        # print(modif_var, "anye")
        return modif_var
    # return 0

def syntax(text):
    global varidents
    global modif_var
    modif_var.clear()
    varidents.clear()
    syntaxResult = ''
    success = 1
    comparison = ['BOTH SAEM', 'DIFFRINT']
    arithmetic = ['SUM OF','DIFF OF','PRODUKT OF', 'QUOSHUNT OF', 'MOD OF', 'BIGGR OF', 'SMALLR OF']
    literals = ['NUMBR Literal', 'NUMBAR Literal', 'YARN Literal', 'TROOF Literal', 'Type Literal']
    varAssignment_literals = ['NUMBR Literal', 'NUMBAR Literal', 'YARN Literal', 'TROOF Literal', 'Type Literal']
    booleans = ['BOTH OF', 'EITHER OF', 'WON OF', 'NOT']
    booleans_checker = ['BOTH OF', 'EITHER OF', 'WON OF', 'NOT', 'ALL OF', 'ANY OF']
    keyUsingExp = ['YR', 'FOUND YR', 'ITZ', 'R', 'MEBBE', 'TIL', 'WILE', 'VISIBLE']
    hasHai = -1
    hasKthxbye = -1
    hasWazzup = -1
    hasBuhbye = -1
    hasVarDec = 0
    wtfchecker = -1
    omgchecker = -1
    omgwtfchecker = -1
    for h in range(0, len(text.splitlines())):
        lexeme = keywords.lex(text.splitlines()[h].lstrip().rstrip())
        if lexeme is not None:
            if ['BTW', 'Comment Delimiter'] in lexeme:
                lexeme.pop(lexeme.index(['BTW', 'Comment Delimiter'])+1)
                lexeme.pop(lexeme.index(['BTW', 'Comment Delimiter']))
                
            for i in range(0, len(lexeme)):
                
                ## PROGRAM BLOCK SYNTAX - HAI
                if lexeme[i][0] == 'HAI' and hasHai == -1 and hasKthxbye == -1:
                    hasHai = 0
                    break
                else:
                        if lexeme[i][0] == 'HAI' and hasHai > -1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <HAI>: \n\tAlready has HAI; it must be declared once')
                            success = 0
                            break
                        elif lexeme[i][0] == 'HAI' and hasKthxbye > -1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <HAI>: \n\HAI must be declared before KTHXBYE')
                            success = 0
                            break
                if hasHai == 0:
                    ## VARIABLE BLOCK SYNTAX - WAZZUP
                    if lexeme[i][0] == 'WAZZUP' and hasWazzup == -1 and hasBuhbye == -1:
                        hasWazzup = 0
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
                    ## VARIABLE DECLARATION SYNTAX
                    if lexeme[i][0] == 'I HAS A' and hasWazzup == 0:
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
                                    syntaxResult += (f"\n>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'ITZ' keyword?")
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
                                            varidents[lexeme[i+1][0]] = semantics.comparison_expression(lexeme[i+3:])
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
                                print(lexeme[i+3][0])
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
                    #     # if less than
                        # print(f"lexeme in visible start: {lexeme}")
                        if len(lexeme) < 2:
                            syntaxResult +=(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tVISIBLE must have a Variable Identifier, Literal, or an Expression')
                            success = 0
                            break
                        else:
                            visible_indexcounter = 1
                            while visible_indexcounter < len(lexeme):
                                # check muna yung "+"
                                if lexeme[visible_indexcounter][1] == "Output Delimiter":
                                    #check yung before "+"
                                    if lexeme[visible_indexcounter-1][0] not in varidents:
                                        if lexeme[visible_indexcounter-1][1] != 'NUMBR Literal':
                                            if lexeme[visible_indexcounter-1][1] != 'NUMBAR Literal':
                                                if lexeme[visible_indexcounter-1][1] != 'TROOF Literal':
                                                    if lexeme[visible_indexcounter-1][1] != 'String Delimiter':
                                                        if lexeme[visible_indexcounter-1][0] != "IT":
                                                            # print(f"lexeme[visible_indexcounter-1][0]:{lexeme[visible_indexcounter-1][0]}")
                                                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[visible_indexcounter][0]}>: \n\tIncorrect syntax, see correct syntax. \n\t{lexeme[visible_indexcounter][0]} VISIBLE <x> + <y> where <x> and <y> are either Variable Identifiers, Expressions, String, or IT only1')
                                                            success = 0
                                                            break
                                    
                                    #check yung after naman "+"
                                    if lexeme[visible_indexcounter+1][0] not in varidents:
                                        if lexeme[visible_indexcounter+1][0] not in arithmetic:
                                            if lexeme[visible_indexcounter+1][0] not in comparison:
                                                if lexeme[visible_indexcounter+1][0] not in booleans_checker:
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
                                            if lexeme[visible_indexcounter][0] not in varidents: #check if varidents
                                                if lexeme[visible_indexcounter][0] not in arithmetic: #check if expressions
                                                    if lexeme[visible_indexcounter][0] not in comparison: #check if comparison
                                                        if lexeme[visible_indexcounter][0] != "IT":
                                                            if lexeme [visible_indexcounter][0] not in booleans_checker: #check if boolean
                                                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[visible_indexcounter][0]}>: \n\tIncorrect syntax, see correct syntax. \n\t{lexeme[visible_indexcounter][0]} VISIBLE <x> + <y> where <x> and <y> are either Variable Identifiers, Expressions, String, or IT only3')
                                                                success = 0
                                                                break
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
                                                visible_indexcounter += 1
                                        else:
                                            visible_indexcounter +=1
                                    else:
                                        if lexeme[visible_indexcounter+2][1] != 'String Delimiter':
                                            syntaxResult += (f'>> SyntaxError in line {h+1} near <{lexeme[visible_indexcounter+2][1]}>: \n\tVariable Identifier ')
                                            success = 0
                                            break
                                        else:
                                            #move forward 
                                            visible_indexcounter +=3
                            # print("UMABOT SA END NG SYNTAX HUHU")
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
                        print(lexeme[i][0])
                        result = comparisonSyntax(lexeme, h, i)
                        if result is not None:
                            success = 0
                            syntaxResult += result
                            
                        break

                    #SWITCH CASES STATEMENTS
                    wtfchecker = -1
                    if lexeme[i][0] == 'WTF?':
                        #omgcounter=i
                        wtfchecker = 1
                        omgchecker = -1
                        omgwtfchecker = -1
                        #while lexeme[omgcounter][0] != "OMGWTF":
                    #OMG STATEMENTS 
                    if lexeme[i][0] == "OMG":
                        if wtfchecker == 1: 
                            if lexeme[i+1][1] != "String Delimeter": #check the sting
                                syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t OMG Should be followed by Value Literal')
                                success = 0
                                break
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
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Switch Statements required WTF?, OMG, and OMGWTF?')
                            success = 0
                            break                                    

                    if lexeme[i][0] == "OMGWTF?":
                        if omgchecker == 1:
                            omgwtfchecker = 1
                        else:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Switch Statements required WTF?, OMG, and OMGWTF?')
                            success = 0
                            break   

                    if lexeme[i][0] == 'OIC':
                        if omgwtfchecker != 1 and omgchecker != 1 and wtfchecker != 1:
                            syntaxResult += (f'\n>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Switch Statements required WTF?, OMG, and OMGWTF?')
                            success = 0
                            break     

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