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
    allMatches = []
    dupes = []
    tempStorage = []

    ##### FOR IDENTIFIER
    pattern = r'(.*)\b(?![A-Z]+\b)([A-Za-z][A-Z|a-z|0-9|\_]*)\b[^.*]' #regex to catch the preceding words before the match word and also the match word
    #(.*): This is a capturing group that matches any character (.) zero or more times (*). The .* part captures everything on the line (greedily).
    # \b capture the whole word
    # (?![A-Z]+\b) exclude all uppercase word
    # ([A-Za-z][A-Z|a-z|0-9|\_]*) para sa identifier
    compiled_lexs = []

    matches = re.findall(pattern, string) #find all that matches the pattern in the string

    for match in matches:
        # print(match)
            
    
        preceding_words, word = match #unpack or hinihiwalay niya 'yung nacatch ng regex since ang regex

       
        #kinacatch niya is 'yung preceding words sa line kung saan andon 'yung identifier, so sa matches ganito siya (<preceding>, <match word>)
        check = 0 #check kung 'yung word is nasa keywords since dapat is hindi
                
        for keyword in keywords:
            if keyword == word:
                matches.remove(word)
                check = 1
                break

        if check == 0: #if wala siya sa keywords, check 'yung preceding phrase in the same line of the word to identify what identifier the word is
            if preceding_words.strip() == "HOW IZ I": 
                function_ident.append(word)
            elif preceding_words.strip() == "IM IN YR" or "UPPIN YR":
                loop_ident.append(word)
            elif preceding_words.strip() == "I HAS A":
                var_ident.append(word)
           
            # check for identifiers na nasa preceding words pa
            while 1:
                pre = preceding_words
                x = re.findall(pattern, pre)
                for a in x:
                    preceding_words, word =a
                    if preceding_words.strip() == "HOW IZ I" or "YR AN": 
                        function_ident.append(word)
                    elif preceding_words.strip() == "IM IN YR" or "UPPIN YR":
                        loop_ident.append(word)
                    elif preceding_words.strip() == "I HAS A":
                        var_ident.append(word)
                if x == []:
                    break
                print(x)  

           

    for i in function_ident:
        print(f"{i} is a function identifier")
    
    for i in loop_ident:
        print(f"{i} is a loop identifier")
    
    for i in var_ident:
        print(f"{i} is a var identifier")

        
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