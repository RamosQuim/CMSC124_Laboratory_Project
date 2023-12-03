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

def lex(string):
    var_ident = []
    loop_ident = []
    function_ident = []
    it = []
    symbol_table = []

    ##### FOR IDENTIFIER
    pattern = r'^([^\n"]*)\b(?![A-Z]+\b)([A-Za-z][A-Z|a-z|0-9|\_]*|[A-Za-z])\b(.*[^"\n]*)' #regex to catch the preceding words before the match word and also the match word
    
    # pattern = r'(.*)\b(?![A-Z]+\b)([A-Za-z][A-Z|a-z|0-9|\_]*|[A-Za-z])\b(.*)'

    
    #(.*): This is a capturing group that matches any character (.) zero or more times (*). The .* part captures everything on the line (greedily).
    # \b capture the whole word
    # (?![A-Z]+\b) exclude all uppercase word (.*)?
    # ([A-Za-z][A-Z|a-z|0-9|\_]*) para sa identifier
    # pattern =r'^([^\n"]*)\b(?![A-Z]+\b)([A-Za-z][A-Z|a-z|0-9|\_]*|[A-Za-z])\b([^"\n]*)$'



    # matches = re.findall(pattern, string, re.MULTILINE) #find all that matches the pattern in the string
    # pattern = r'^([^\n"]*)\b(?![A-Z]+\b)([A-Za-z][A-Z|a-z|0-9|\_]*|[A-Za-z])\b([^"\n]*)$'
    matches = re.findall(pattern, string, re.MULTILINE)

    print(matches)
    for match in matches:
        
        preceding_words = match[0].strip()
        
        word = match[1]
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
       
        #kinacatch niya is 'yung preceding words sa line kung saan andon 'yung identifier, so sa matches ganito siya (<preceding>, <match word>)
        check = 0 #check kung 'yung word is nasa keywords since dapat is hindi
                
        for keyword in keywords:
            if keyword == word:
                matches.remove(word)
                check = 1
                break

        if check == 0: #if wala siya sa keywords, check 'yung preceding phrase in the same line of the word to identify what identifier the word is
            if preceding_words == "HOW IZ I" or preceding_words == "YR AN": 
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
                    temp.append(word.replace('"', ''))
                # if len(preceding_words) > 8:
                #     w = preceding_words[7:].strip()
                #     temp.append(w)
                
                # it.append(temp)

                while 1:
                    pre = preceding_words
                    x = re.findall(pattern, pre)
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
                                    print(j[1])

                            if c == 0:
                                temp.append(word.replace('"', ''))
                    if x == []:
                        it.append(temp)
                        break

           
            # check for identifiers na nasa preceding words pa
            while 1:
                pre = preceding_words
                x = re.findall(pattern, pre)
                for a in x:
                    preceding_words = a[0].strip()
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

                    if preceding_words.strip() == "HOW IZ I" or preceding_words.strip() == "YR AN": 
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
                            y = re.findall(pattern, pr)
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
    
    
    for i in it:
        j = ""
        for k in range(len(i)):
            j += i[k]
            j += " "
            
        print(f"identifier: IT \t value: {j}")
                

    

    

        
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

main()