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
    spans = []
    storage = []
    var_ident = []
    loop_ident = []
    function_ident = []

    
    for keyword in keywords:
        x = re.search(f" ?{keyword} ?", string) # regex for keywords
        if x:   # if x is not None
            spans.append(x.span())
            spans = sorted(spans, key=lambda a: (a[0], a[1]))
    

    ##### FOR IDENTIFIER ##### kulang pa kapag more than 2 identifiers
    pattern = '[^A-Z ]([A-Z]|[a-z])([A-Z]|[a-z]|[0-9]|\_)*'
    res = re.search(pattern, string)
    index = res.span()
    identifier = string[index[0]:index[1]] #mismong identifier
    # print("identifier: ",identifier)

    #check 'yung before nung identifier kung I HAS A ba or etc
    check = 0
    identifier = string[index[0]:index[1]]

    for keyword in keywords:
        if keyword == identifier:
            check = 1
            break

    if check == 0:
        #check first kung ano 'yung phrase before the identifier to distinguish what kinf of identifier it is
        if string[index[0]-8:index[0]-1].strip(' ') == "I HAS A":
            var_ident.append(identifier.strip('\n'))

        elif string[index[0]-9:index[0]-1].strip(' ') == "IM IN YR":
            loop_ident.append(identifier.strip('\n'))

        elif string[index[0]-5:index[0]-1].strip(' ') == "IZ I":
            function_ident.append(identifier.strip('\n'))
    ##### FOR IDENTIFIER #####

    ### FOR ARRANGEMENT (kulang pa 'yung sa identifier sa pag-arrange) ###
    for span in spans:  # this is for arranging the found keywords based on string input
        for keyword in keywords:
            x = re.search(f" ?{keyword} ?", string)
            if x:
                if span == x.span():
                    storage.append(keyword)
     ### FOR ARRANGEMENT (kulang pa 'yung sa identifier sa pag-arrange) ###

    ### FOR PRINTING ###
    print("\nLexical Analyzer:\n")
    for i in storage:
        print(i, 'is a', keywords[i])

    
    for j in loop_ident:
        print(j, " is a LOOP IDENTIFIER")
    
    for j in var_ident:
        print(j, " is a VARIABLE IDENTIFIER")
  
    for j in function_ident:
        print(j, " is a FUNCTION IDENTIFIER")
    
     ### FOR PRINTING ###



#for accepting many input lines from user

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