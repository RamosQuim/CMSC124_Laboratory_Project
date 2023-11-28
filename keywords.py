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

#this part will be responsible for sending content to the UI

def connect_UI(TextInputs):
    print(TextInputs)
    # so ipapasa na dito yung values from the text file :>
    results = lex(TextInputs)
    print(f"results:{results}")
    return results


def lex(string):
    spans = []
    storage = []
    var_ident = []
    loop_ident = []
    function_ident = []
    allMatches = []
    dupes = []
    
    ##### FOR IDENTIFIER ##### kulang pa kapag more than 2 identifiers
    pattern = r'(.*)\b(?![A-Z]+\b)([A-Za-z][A-Z|a-z|0-9|\_]*)\b' #regex to catch the preceding words before the match word and also the match word
    #(.*): This is a capturing group that matches any character (.) zero or more times (*). The .* part captures everything on the line (greedily).
    # \b capture the whole word
    # (?![A-Z]+\b) exclude all uppercase word
    # ([A-Za-z][A-Z|a-z|0-9|\_]*) para sa identifier
    compiled_lexs = []

    
    for keyword in keywords:
        x = re.compile(r'\b'+keyword+r'\b') # regex for keywords

        for found in x.finditer(string):
            spans.append(found.span())
            spans = sorted(spans, key=lambda a: (a[0], a[1]))

    matches = re.compile(pattern) #find all that matches the pattern in the string
    for found in matches.finditer(string):
            allMatches.append(found.groups())
            spans.append(found.span())
            spans = sorted(spans, key=lambda a: (a[1]))

    for i in range(0, len(spans)):
        if i != (len(spans)-2):
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
            if preceding_words.strip() == "HOW IZ I": 
                function_ident.append(word)
            elif preceding_words.strip() == "IM IN YR":
                loop_ident.append(word)
            elif preceding_words.strip() == "I HAS A":
                var_ident.append(word)

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

    return compiled_lexs


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