import re
import sys

# try to run this python code

keywords = {
    'HAI': 'Code Delimiter', 
    'KTHXBYE': 'Code Delimiter', 
    'WAZZUP': 'Function Block Delimiter', 
    'BUHBYE': 'Function Block Delimiter', 
    'BTW': 'Comment Identifier', 
    'OBTW': 'Multi-line Comment Delimiter', 
    'TLDR': 'Multi-line Comment Delimiter', 
    'I HAS A': 'Variable Declaration',
    'ITZ': 'Variable Assignment', 
    'R': 'Assignment Operator', 
    'AN': 'Identifier Delimiter',
    'SUM OF': 'Arithmetic Keyword', 
    'DIFF OF': 'Arithmetic Keyword', 
    'PRODUKT OF': 'Arithmetic Keyword', 
    'QUOSHUNT OF': 'Arithmetic Keyword', 
    'MOD OF': 'Arithmetic Keyword', 
    'BIGGR OF': 'Arithmetic Keyword', 
    'SMALLR OF': 'Arithmetic Keyword', 
    'BOTH OF': 'Boolean Keyword', 
    'EITHER OF': 'Boolean Keyword', 
    'WON OF': 'Boolean Keyword', 
    'NOT': 'Boolean Keyword',
    'ANY OF': 'Boolean Keyword', 
    'ALL OF': 'Boolean Keyword', 
    'BOTH SAEM': 'Comparison Keyword', 
    'DIFFRINT': 'Comparison Keyword', 
    'SMOOSH': 'Concatenation Delimiter', 
    'MAEK': 'Typecasting Operator', 
    'A': 'Typecasting Declaration', 
    'IS NOW A': 'Re-casting Declaration',
    'VISIBLE': 'Output Keyword', 
    'GIMMEH': 'Input Keyword', 
    'O RLY?': 'Flow-control Delimiter', 
    'YA RLY': 'If Delimiter', 
    'MEBBE': 'Else-if Delimiter', 
    'NO WAI': 'Else Delimiter', 
    'OIC': 'Flow-control Delimiter', 
    'WTF?': 'Flow-control Delimiter', 
    'OMG': 'Switch-case Delimiter',
    'OMGWTF': 'Switch-case Delimiter', 
    'IM IN YR': 'Loop Delimiter', 
    'UPPIN': 'Loop Operator', 
    'NERFIN': 'Loop Operator', 
    'YR': 'Code Delimiter', 
    'TIL': 'Iteration Keyword', 
    'WILE': 'Iteration Keyword', 
    'IM OUTTA YR': 'Loop Delimiter',
    'HOW IZ I': 'Function Delimiter', 
    'IF U SAY SO': 'Function Delimiter', 
    'GTFO': 'Break Keyword', 
    'FOUND YR': 'Function Return Keyword', 
    'I IZ': 'Function Call Keyword', 
    'MKAY': 'Concatenation Delimiter'
}

def connect_UI(TextInputs):
    print(TextInputs)
    # so ipapasa na dito yung values from the text file :>
    symbols = symbol(TextInputs)
    lexemes = lex(TextInputs)
    return [lexemes, symbols]

def lex(string):
    spans = []
    storage = []
    var_ident = []
    loop_ident = []
    function_ident = []
    comment = []
    literal = []
    allMatches = []
    dupes = []
    
    ##### FOR IDENTIFIER ##### kulang pa kapag more than 2 identifiers
    pattern = r'(.*)\b(?![A-Z]+\b)([A-Za-z][A-Z|a-z|0-9|\_]*)\b' #regex to catch the preceding words before the match word and also the match word
    commentPattern = r'BTW.*'
    #(.*): This is a capturing group that matches any character (.) zero or more times (*). The .* part captures everything on the line (greedily).
    # \b capture the whole word
    # (?![A-Z]+\b) exclude all uppercase word
    # ([A-Za-z][A-Z|a-z|0-9|\_]*) para sa identifier
    literalPattern = r'(\".*\")|\b(0(\.[0-9]+|-0.[0-9]*[1-9]+[0-9]*)?|-?[1-9][0-9]*(\.[0-9]+)?)\b|\b(WIN|LOSE|NUMBR|NUMBAR|YARN|TROOF)\b'
    compiled_lexs = []

    
    for keyword in keywords:
        x = re.compile(r'\b'+keyword+r'\b') # regex for keywords

        for found in x.finditer(string):
            spans.append(found.span())
            spans = sorted(spans, key=lambda a: (a[0], a[1]))

    matches = re.compile(pattern) #find all that matches the pattern in the string
    for found in matches.finditer(string):
        if found.group()[0:3] != 'BTW':
            allMatches.append(found.groups())
            spans.append(found.span())
            spans = sorted(spans, key=lambda a: (a[1]))

    commentMatch = re.compile(commentPattern)
    for found in commentMatch.finditer(string):
        allMatches.append((found.group()[0:3], found.group()[4:len(found.group())]))
        spans.append(found.span())
        spans = sorted(spans, key=lambda a: (a[1]))
        

    literalMatch = re.compile(literalPattern)
    for found in literalMatch.finditer(string):
        literal.append(found.group())
        spans.append(found.span())
        spans = sorted(spans, key=lambda a: (a[1]))
          

    for i in range(0, len(spans)):
        if i != (len(spans)-2) and len(spans)>2:
            if spans[i][1] == spans[i+1][1]:
                dupes.append(spans[i+1])
        else:
            break

    for dupe in dupes:
        spans.remove(dupe)

    for span in spans:  # this is for arranging the found keywords based on string input
        for keyword in keywords:
            x = re.compile(r'\b'+keyword+r'\b') # regex for keywords
            for found in x.finditer(string):
                if span == found.span():
                    storage.append(keyword)
            
        for found in matches.finditer(string):
            if span == found.span():
                storage.append(found.groups()[1])
        
        for found in commentMatch.finditer(string):
            if span == found.span():
                storage.append(found.group()[4:len(found.group())])
        
        for found in literalMatch.finditer(string):
            if span == found.span():
                storage.append(found.group())
    
    for match in allMatches:
        preceding_words, word = match #unpack or hinihiwalay niya 'yung nacatch ng regex since ang regex
        #kinacatch niya is 'yung preceding words sa line kung saan andon 'yung identifier, so sa matches ganito siya (<preceding>, <match word>)
        check =0 #check kung 'yung word is nasa keywords since dapat is hindi
        for keyword in keywords:
            if keyword == word:
                matches.remove(word)
                check = 1
                break

        if check == 0: #if wala siya sa keywords, check 'yung preceding phrase in the same line of the word to identify what identifier the word is
            if preceding_words.strip() == "HOW IZ I" or preceding_words.strip() == "I IZ": 
                function_ident.append(word)
            elif preceding_words.strip() == "IM IN YR":
                loop_ident.append(word)
            elif preceding_words.strip() == "I HAS A":
                var_ident.append(word)
            elif preceding_words == "BTW":
                comment.append(word)
    
    ### FOR PRINTING ###
    print("\nLexical Analyzer:\n")
    for i in storage:
        if i in keywords:
            print(i, 'is a', keywords[i])
            compiled_lexs.append([f"{i}",f"{keywords[i]}"])
        else:
            if i in loop_ident:
                print(i, "is a Loop Identifier")
                compiled_lexs.append([f"{i}","Loop Identifier"])
            elif i in var_ident:
                print(i, "is a Variable Identifier")
                compiled_lexs.append([f"{i}","Variable Identifier"])
            elif i in function_ident:
                print(i, "is a Function Identifier") 
                compiled_lexs.append([f"{i}","Function Identifier"])
            elif i in literal:
                if i[0] == '"':
                    print(i[0], "is a String Delimiter")
                    compiled_lexs.append([f"{i[0]}","String Delimiter"])
                    if i[-1] == '"':
                        print(i[1:-1], "is a Literal")
                        print(i[-1], "is a String Delimiter")
                        compiled_lexs.append([f"{i[1:-1]}","Literal"])
                        compiled_lexs.append([f"{i[-1]}","String Delimiter"])
                else:
                    print(i, "is a Literal")
                    compiled_lexs.append([f"{i}","Literal"])
            elif i in comment:
                print(i, "is a Comment")
                compiled_lexs.append([f"{i}","Comment"])

    return compiled_lexs



def symbol(string):
    var_ident = []
    loop_ident = []
    function_ident = []
    it = []
    symbol_table = []

    ##### FOR IDENTIFIER
    
    pattern = r'^([^\n]*[^"])\b(?![A-Z]+\b)([A-Za-z][A-Z|a-z|0-9|\_]*|[A-Za-z])\b([^\n]*)'
    matches = re.findall(pattern, string, re.MULTILINE)

    # print(matches)
    for match in matches:
        
        preceding_words = match[0].strip()
        
        word = match[1]
         #kinacatch niya is 'yung preceding words sa line kung saan andon 'yung identifier, so sa matches ganito siya (<preceding>, <match word>)
        check = 0 #check kung 'yung word is nasa keywords since dapat is hindi
                
        for keyword in keywords:
            if keyword == word:
                # matches.remove(word)
                check = 1
                break

        if check == 0: #if wala siya sa keywords, check 'yung preceding phrase in the same line of the word to identify what identifier the word is
            next_words = match[2].strip()
        # print(word)
        # print(preceding_words)
            if next_words != " ":
                if next_words[0:3] == "ITZ":
                    var_value = []
                    possible_val = next_words[3:].strip()
                    var_value.append(word)
                    var_value.append(possible_val.replace('"', ''))
                    symbol_table.append(var_value)
            
            
            if preceding_words.strip() == "HOW IZ I" or preceding_words[len(preceding_words)-5:].strip() == "YR AN": 
                function_ident.append(word)
            elif (preceding_words == "IM IN YR" or preceding_words == "UPPIN YR") or (preceding_words[len(preceding_words)-9:].strip() == "UPPIN YR" or preceding_words[len(preceding_words)-9:].strip() == "IM IN YR"):
                loop_ident.append(word)
            elif preceding_words == "I HAS A":
                var_ident.append(word)
            elif preceding_words == "VISIBLE" or preceding_words[0:7].strip() == "VISIBLE":
                temp = []
                c = 0
                for j in symbol_table:
                    if j[0] == word:
                        c = 1
                        temp.append(j[1])

                        # print(j[1])

                if c == 0:
                    # print(word)
                    temp.append(word.replace('"', ''))
                # if len(preceding_words) > 8:
                #     w = preceding_words[7:].strip()
                #     temp.append(w)
                
                # it.append(temp)

                while 1:
                    pre = preceding_words
                    # print(pre)
                    pt = r'^([^\n]*)\b(?![A-Z]+\b)([A-Za-z][A-Z|a-z|0-9|\_]*|[A-Za-z])\b([^\n]*)'
                    x = re.findall(pt, pre)
                    # print(x)
                    for a in x:
                        preceding_words = a[0]
                        word = a[1]
                        next_words = a[2]
                        
                        if preceding_words == "VISIBLE" or preceding_words[0:7].strip() == "VISIBLE":
                            
                            c = 0
                            for j in symbol_table:
                                if j[0] == word:
                                    c = 1
                                    temp.append(j[1])
                                    # print(j[1])

                            if c == 0:
                                # print(word)
                                temp.append(word.replace('"', ''))
                    if x == []:
                        it.append(temp)
                        break

           
            # check for identifiers na nasa preceding words pa
            while 1:
                pre = preceding_words
                x = re.findall(pattern, pre)
                # print(x)
                for a in x:
                    preceding_words = a[0].strip()
                    # print(preceding_words[len(preceding_words)-5:])
                    word = a[1]
                    next_words = a[2].strip()
                    if next_words != " ":
                        if next_words[0:3] == "ITZ":
                            var_value = []
                            possible_val = next_words[3:].strip()

                            var_value.append(word)
                            var_value.append(possible_val.replace('"', ''))
                            # print(f"value for {word} is {possible_val}")
                            symbol_table.append(var_value)

                    if preceding_words.strip() == "HOW IZ I" or preceding_words[len(preceding_words)-5:].strip() == "YR AN": 
                        function_ident.append(word)
                    elif (preceding_words.strip() == "IM IN YR" or preceding_words.strip() == "UPPIN YR") or (preceding_words[len(preceding_words)-9:].strip() == "UPPIN YR" or preceding_words[len(preceding_words)-9:].strip() == "IM IN YR"):
                        loop_ident.append(word)
                    elif preceding_words.strip() == "I HAS A":
                        var_ident.append(word)
                    elif preceding_words == "VISIBLE" or preceding_words[0:7].strip() == "VISIBLE":
                        temp = []
                        c = 0
                        for j in symbol_table:
                            if j[0] == word:
                                c = 1
                                temp.append(j[1])
                                # print(j[1])

                        if c == 0:
                            temp.append(word.replace('"', ''))
                        

                        while 1:
                            pr = preceding_words
                            pt = r'^([^\n]*)\b(?![A-Z]+\b)([A-Za-z][A-Z|a-z|0-9|\_]*|[A-Za-z])\b([^\n]*)'
                            y = re.findall(pt, pr)
                            for b in y:
                                preceding_words = b[0]
                                wd = b[1]
                                nw = b[2]
                        
                                if preceding_words == "VISIBLE" or preceding_words[0:7].strip() == "VISIBLE":
                                    c = 0
                                    for j in symbol_table:
                                        if j[0] == wd:
                                            c = 1
                                            temp(j[1])
                                    # print(j[1])

                                    if c == 0:
                                        temp.append(wd.replace('"', ''))
                            if y == []:
                                it.append(temp)
                                break
                if x == []:
                    break
                
                # print(x)  
    ### FOR PRINTING ###
    print("\nLexical Analyzer:\n")
           
    print("\nIDENTIFIERS:")
    for i in function_ident:
        print(f"{i} is a function identifier")
    
    for i in loop_ident:
        print(f"{i} is a loop identifier")
    
    for i in var_ident:
        print(f"{i} is a var identifier")

    print("\nSYMBOL TABLE:")
    for j in symbol_table:
        print(f"identifier: {j[0]} \t value: {j[1]}")
    
    print(it)
    for i in it:
        j = ""
        for k in range(len(i)-1, -1, -1):
            # print(k)
            j += i[k]
            j += " "
 
        print(f"identifier: IT \t\t value: {j}")
        symbol_table.insert(0, ['IT', j])
    return symbol_table

    

    

        
#for accepting many input lines from user
def main():
    # array_words = []
    con = True
    str = ""
    while con:
        line = sys.stdin.readline()
    
        if line == "KTHXBYE\n": #if eto na-encounter mag stop sa pag-accept
            con = False
            str += line
            # array_words.append(str.strip('\n'))
            break
        str += line
        # array_words.append(str.strip('\n'))

    # print(arr)

    lex(str)

# main()

# if token[1].rstrip().lstrip() == 'Variable Identifier':
#             arr = []
#             matches =re.finditer(r'\b'+token[0]+r'\b', str)

#             last_occurrence_startIndex = -1
#             end_index = -1
#             for match in matches:
#                 last_occurrence_startIndex = match.start()
#                 end_index = match.end()

#             if str[end_index+1:end_index+4].rstrip().lstrip() == "ITZ":
#                 print("yey")
#                 whole = str[end_index+5:]
#                 value = re.match(r'(.*)[^\n]*',whole)[0]
#                 if len(symbol_table) == 0:
#                     arr.append(token[0])
#                     arr.append(value)
#                     symbol_table.append(arr)
#                 else:
#                     for i in symbol_table:
#                         if i[0] != token[0]:

#                             arr.append(token[0])
#                             arr.append(value)
#                             symbol_table.append(arr)
#                         else:
#                             break

'''
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
'''