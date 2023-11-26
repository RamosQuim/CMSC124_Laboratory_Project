import re

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



def is_keyword(word):
    if word in keywords:
        return 1
    else:
        return 0

string = '''
HAIS
    I HAS A var ITZ 12
    VISIBLE "noot noot" var
KTHXBYE
'''

spans = []
storage = []

for keyword in keywords:
    x = re.search(f" ?{keyword} ?", string)
    if x:
        spans.append(x.span())
        spans = sorted(spans, key=lambda a: (a[0], a[1]))
for span in spans:
    for keyword in keywords:
        x = re.search(f" ?{keyword} ?", string)
        if x:
            if span == x.span():
                storage.append(keyword)

for i in storage:
    print(i, '------>', keywords[i])