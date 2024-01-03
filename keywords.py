import re
import sys
import semantics

compiled_lex = []
symbol_table = []


class LOLLexer:
    def __init__(self, source_code_file):
        self.source_code = source_code_file
        self.tokens = []
        self.current_position = 0

    #
    def tokenize(self):
        while self.current_position < len(self.source_code):
            # print(f"Current position: {self.current_position}")
            
            # Print the current value at the position
            current_value = self.source_code[self.current_position:self.current_position + 10]
            
            token = self.match_token()

            if token is not None:
                self.tokens.append(token) #appends the token to the tokens list
            else:
                raise SyntaxError(f"Invalid token at position {self.current_position}")
        return self.tokens


    #responsible for the actual checking and matching in regex
    def match_token(self):
        for pattern, token_type in token_patterns.items():
            match = re.match(pattern, self.source_code[self.current_position:]) #checks if it matches any pattern in the token_patters
            if match:
                value = match.group(0)
                self.current_position += len(value)
                # print(value)
                # if token_type == 'YARN Literal':
                    #  print("value" + value)
                    # print(value)S
                    # if value[0] == '"' and value[len(value)-1] == '"':
                    #       print(value)
                    # value = value.replace('"', "")
                        #   print(val)
                    # return Token(token_type, value)

                    # value = value.replace('"',"")
                return Token(token_type, value)     #returns the Token
        return None

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

# Updated LOLCODE token patterns to allow for indentation
token_patterns = {

    # Keywords [<type>, <classification>]
    r'\s*HAI\s+': 'Code Delimiter',
    r'\s*KTHXBYE\s+': 'Code Delimiter',
    r'\s*WAZZUP\s+': 'Variable Declaration Delimiter',
    r'\s*BUHBYE\s+': 'Variable Declaration Delimiter',
    r'((\s*BTW .*)|( BTW .*))': 'Comment Line',
    r'\s*OBTW\s+': 'Comment Delimiter',
    r'\s*TLDR\s+': 'Comment Delimiter',
    r'\s*I HAS A\s+': 'Variable Declaration',
    r'\s*ITZ\s+': 'Variable Assignment',
    r'\s*R\s+': 'Variable Assignment',
    r'\s*AN\s+': 'Parameter Delimiter',                                   
    r'\s*SUM OF\s+': 'Arithmetic Operation',
    r'\s*DIFF OF\s+': 'Arithmetic Operation',
    r'\s*PRODUKT OF\s+': 'Arithmetic Operation',
    r'\s*QUOSHUNT OF\s+': 'Arithmetic Operation',
    r'\s*MOD OF\s+': 'Arithmetic Operation',
    r'\s*BIGGR OF\s+': 'Arithmetic Operation',
    r'\s*SMALLR OF\s+': 'Arithmetic Operation',
    r'\s*BOTH OF\s+': 'Boolean Operation',
    r'\s*EITHER OF\s+': 'Boolean Operation',
    r'\s*WON OF\s+': 'Boolean Operation',
    r'\s*NOT\s+': 'Boolean Operation',
    r'\s*ANY OF\s+': 'Boolean Operation',
    r'\s*ALL OF\s+': 'Boolean Operation',
    r'\s*BOTH SAEM\s+': 'Comparison Operation',
    r'\s*DIFFRINT\s+': 'Comparison Operation',
    r'\s*SMOOSH\s+': 'String Contatenation',
    r'\s*MAEK\s+': 'Typecasting Operation',
    r'\s*A\s+': 'Typecasting Operation',                   
    r'\s*IS NOW A\s+': 'Typecasting Operation',
    r'\s*VISIBLE\s+': 'Output Keyword',
    r'\s*\+\s+': 'Output Delimiter',
    r'\s*GIMMEH\s+': 'Input Keyword',
    r'\s*O\sRLY\?\s+': 'If-then Keyword',
    r'\s*YA RLY\s+': 'If-then Keyword',
    r'\s*MEBBE\s+': 'If-then Keyword',
    r'\s*NO WAI\s+': 'If-then Keyword',
    r'\s*OIC\s+': 'If-then Keyword',
    r'\s*WTF\?\s+': 'Switch-Case Keyword',
    r'\s*OMG\s+': 'Switch-Case Keyword',
    r'\s*OMG WTF\s+': 'Switch-Case Keyword',
    r'\s*IM IN YR\s+': 'Loop Keyword',
    r'\s*UPPIN\s+': 'Loop Operation',
    r'\s*NERFIN\s+': 'Loop Operation',
    r'\s*YR\s+': 'Parameter Delimiter',
    r'\s*TIL\s+': 'Loop Keyword',
    r'\s*WILE\s+': 'Loop Keyword',
    r'\s*IM OUTTA YR\s+': 'Loop Keyword',
    r'\s*HOW IZ I\s+': 'Function Keyword',
    r'\s*IF U SAY SO\s+': 'Function Keyword',
    r'\s*GTFO\s+': 'Return Keyword',
    r'\s*FOUND YR\s+': 'Return keyword',
    r'\s*I IZ\s+': 'Function Call',
    r'\s*MKAY\s+': 'Concatenation Delimiter',                              
    r'\s*NOOB\s+': 'Void Literal',

    # Literals and variable identifiers
    r'\s*(NUMBR|NUMBAR|YARN|TROOF|NOOB)\s?' : 'Type Literal',  
    r'\s*(WIN|FAIL)\s*': 'TROOF Literal',                 
    r'\s*[a-zA-Z][a-zA-Z0-9_]*\s*': 'Identifier',           
    r'\s*-?(0|[1-9][0-9]*)?\.[0-9]+\s*': 'NUMBAR Literal',  
    r'\s*0\s*|^-?[1-9][0-9]*\s*': 'NUMBR Literal',        
    # r'\s*\"[^\"]*\"\+?\s*': 'YARN Literal',    
    r'\s*\"[^\"]*\"\s*': 'YARN Literal',             
}

def lex(str):
    compiled_lex.clear()
    # global compiled_lex
    # compiled_lex = []
    varidents = []
    code = str
    if code.strip() != "":  # to avoid error when there is no input
        lexer = LOLLexer(code)
        tokens = lexer.tokenize()
        # print(tokens)
        
        for i in range(0, len(tokens)):
            # print(tokens[i].value, tokens[i].type)
            temp = tokens[i].value.rstrip()  # remove leading and trailing space characters 
            val = temp.lstrip()
            # print(val, val[0], val[len(val)-1], len(val))

            # print(tokens[i+1].value)
            
            # print(temp)

            # if len(val) > 1 and val[0] == '"' and val[-1] == '"':   # when token is a string literal separate the string delimiter
            if tokens[i].type == 'YARN Literal':
                    
                # print(tokens[i].value)
                if val[0] == '"' and val[-1] == '"':
                    # print(tokens[i].value)
                    new = Token('String Delimiter', '"')
                    tokens[i].value = val[1:-1]
                    tokens.insert(i, new)
                    tokens.insert(i+2, new)
            elif 'BTW' in val:
                tokens[i].value = val[4:]
                comment = Token('Comment Delimiter', 'BTW')
                tokens.insert(i, comment)
            
            if i != len(tokens):
                if tokens[i].type == 'Variable Declaration':
                    if tokens[i+1].type == 'Identifier':
                        varidents.append(tokens[i+1].value.lstrip().rstrip())
                        tokens[i+1].type = 'Variable Identifier'
                elif tokens[i].type == 'Loop Keyword':
                    if tokens[i+1].type == 'Identifier':
                        tokens[i+1].type = 'Loop Identifier'
                elif tokens[i].type == 'Function Keyword' or tokens[i].type == 'Function Call':
                    if tokens[i+1].type == 'Identifier':
                        tokens[i+1].type = 'Function Identifier'
                elif tokens[i].type == 'Identifier' and tokens[i].value.lstrip().rstrip() in varidents:
                        tokens[i].type = 'Variable Identifier'

        # print('\n\nTokens:')
        for token in tokens:
            compiled_lex.append([token.value.rstrip().lstrip(), token.type])
        
        # print(compiled_lex)
        # print(compiled_lex)
        return compiled_lex

def nmbar(tk):  
                # print(tk)
                check = 0
                for j in symbol_table:
                    # print('haha')
                    if j[0] == tk:
                        # print('meron')
                        # print(token[0])
                        check = 1
                        for k in compiled_lex:
                            # print(k[0])
                            if k[0] == j[1]:
                                print(k[0])
                                # print(k[0])
                                t = k[1]
                                if t == 'NUMBAR Literal':
                                    j[1] = j[1]
                                    break
                                elif t == 'NUMBR Literal':
                                    # print('numbr')
                                    j[1] = float(j[1])
                                    break
                                elif t == 'TROOF Literal':
                                    if j[1] == 'WIN':
                                        # print('win')
                                        j[1] = 1.0
                                        break
                                    elif j[1] == 'FAIL':
                                        # print('fail')
                                        j[1] = 0.0
                                        break
                                elif t == 'YARN Literal':
                                    if re.search(r'^\d+$', j[1]):
                                       j[1] = float(j[1])
                                       break
                        break
                #for noob variables or uninitialized
                if check == 0: 
                    # print('noob')
                    temp_arr = [] 
                    for a in compiled_lex:
                        if a[0] == tk:
                            # print('noob')
                            #check if the variable is declared uninitialized
                            temp_arr.append(tk)
                            temp_arr.append(0.0)
                            symbol_table.append(temp_arr)
                            break
                

def nmbr(tk):
                check = 0
                for j in symbol_table:
                    if j[0] == tk:
                        # print(token[0])
                        check = 1
                        for k in compiled_lex:
                            # print(k[0])
                            if k[0] == j[1]:
                                # print(k[0])
                                t = k[1]
                                # print(t, j[0], j[1])
                                if t == 'NUMBR Literal':
                                    j[1] = int(j[1])
                                elif t == 'NUMBAR Literal':
                                    # print('numbr')
                                    j[1] = int(float(j[1]))
                                    break
                                elif t == 'TROOF Literal':
                                    # print('yey')
                                    if j[1] == 'WIN':
                                        # print('win')
                                        j[1] = 1
                                        break
                                    elif j[1] == 'FAIL':
                                        # print('fail')
                                        j[1] = 0
                                        break
                                elif t == 'YARN Literal':
                                    if re.search(r'^\d+$', j[1]):
                                       j[1] = int(j[1])
                                       break
                        break
               

def trf(tk):
                check = 0
                for j in symbol_table:
                    if j[0] == tk:
                        # print(token[0])
                        check = 1
                        for k in compiled_lex:
                            # print(k[0])
                            if k[0] == j[1]:
                                # print(k[0])
                                t = k[1]
                                if t == 'NUMBAR Literal':
                                    if j[1] == 0.0:
                                    # print('numbr')
                                        j[1] = "FAIL"
                                    else:
                                        j[1] = "WIN"
                                    break
                                elif t == 'NUMBR Literal':
                                    if j[1] == 0:
                                    # print('numbr')
                                        j[1] = "FAIL"
                                    else:
                                        j[1] = "WIN"
                                    break
                                elif t == 'YARN Literal':
                                    if j[1] == "" or j[1] == " ":
                                        j[1] = "FAIL"
                                    else:
                                        j[1] = "WIN"
                                    break
                        break
                #for noob variables or uninitialized
                # if check == 0: 
                #     temp_arr = [] 
                #     for a in compiled_lex:
                #         if a[0] == tk:
                #             # print('noob')
                #             #check if the variable is declared uninitialized
                #             temp_arr.append(tk)
                #             temp_arr.append("FAIL")
                #             symbol_table.append(temp_arr)
                #             break

def yrn(tk):
                check = 0
                for j in symbol_table:
                    if j[0] == tk:
                        # print(token[0])
                        check = 1
                        for k in compiled_lex:
                            if k[0] == j[1]:
                                t = k[1]
                                if t == 'NUMBAR Literal':
                                    j[1] = str(round(float(j[1]),2))
                                    break
                                elif t == 'NUMBR Literal':
                                    new = str(j[1])
                                    j[1] = new
                                    break
                        break
                

def symbolTable(str1):
    symbol_table.clear()
    it = []

    for token in lex(str1):
        # print(token[0], token[1])

        if token[1].rstrip().lstrip() == 'Variable Identifier':
            
            matches = re.finditer(r'I HAS A \b'+token[0]+r'\b', str1)
            last_occurrence_startIndex = -1
            end_index = -1
            for match in matches:
                last_occurrence_startIndex = match.start()
                end_index = match.end()

            if str1[end_index+1:end_index+4].rstrip().lstrip() == "ITZ":
                whole = str1[end_index+5:]
                value = re.match(r'.*[^\n]*',whole)[0]
                new = value.replace('"', '')
                # value = value.strip()
                if len(symbol_table) == 0:
                    arr = []
                    arr.append(token[0])
                    arr.append(new)
                    symbol_table.append(arr)
                else:
                    checker = 0
                    for i in symbol_table:
                        if i[0] == token[0]:
                            checker = 1
                            break
                    if checker == 0:
                        arr = []
                        arr.append(token[0])
                        arr.append(new)
                        symbol_table.append(arr)
            
            #for recasting IS NOW A
            recasting = re.finditer(r'\b'+token[0]+r'\b IS NOW A', str1)
            last_occurrence_startIndex = -1
            end_index = -1
            for match in recasting:
                last_occurrence_startIndex = match.start()
                end_index = match.end()
            
            # print(str1[end_index+1:end_index+5])
            
            if str1[end_index+1:end_index+7].rstrip().lstrip() == 'NUMBAR': #convert to float 
                nmbar(token[0])
                
            elif str1[end_index+1:end_index+6].rstrip().lstrip() == 'NUMBR': #convert to int 
                nmbr(token[0])
                
            elif str1[end_index+1:end_index+6].rstrip().lstrip() == 'TROOF': #convert to bool 
                trf(token[0])
                
            elif str1[end_index+1:end_index+5].rstrip().lstrip() == 'YARN': #convert to string 
                yrn(token[0])
                

            #for R MAEK RECASTING r'\b'+token[0]+r'\b IS NOW A'
            m = re.finditer(r'\b'+token[0]+r'\b R MAEK', str1)
            last_occurrence_startIndex = -1
            e = -1
            for match in m:
                last_occurrence_startIndex = match.start()
                e = match.end()
            
            length = len(token[0]) + 1

            if str1[e+length:e+length+7].rstrip().lstrip() == 'NUMBAR':
                       nmbar(token[0])
                        
            elif str1[e+length:e+length+6].rstrip().lstrip() == 'NUMBR':
                       nmbr(token[0])
            elif str1[e+length:e+length+5].rstrip().lstrip() == 'YARN':
                       yrn(token[0])
            elif str1[e+length:e+length+6].rstrip().lstrip() == 'TROOF':
                       trf(token[0])
            

        elif token[0] == 'VISIBLE':
            if len(it) == 0:

                matches = re.finditer(r'\b'+token[0]+r'\b', str1)
                for match in matches:
                    last_occurrence_startIndex = match.start()
                    end_index = match.end()
                    whole = str1[end_index+1:]
                    value = (re.match(r'\"?.*\"?[^\n]*',whole)[0]).split(' + ')
                    # value = re.match(r'\"?\w+\s*\w*[^ ]\"?[ ^\n]', whole)[0](.*)? r'\s*\"[^\"]*\"\+?\s*'

                    # print(value)
                    temp = []
                    for v in value:
                        c = 0
                        if v[0] == '"' and v[len(v)-1] == '"':
                            # print(v)
                            temp.append(v.replace('"', ''))
                        elif v.replace(".", "").isnumeric() or v == 'WIN' or v == 'FAIL' or v == '+':
                            # print(v)
                            temp.append(v)
                        else:
                            for j in symbol_table:
                                if j[0].split() == v.split():
                                    c = 1
                                    temp.append(j[1])
                                    break
                    # print(temp)
                    it.append(temp)
                    # temp.clear()

        elif token[0] == 'MAEK':
            ex_typecast = semantics.getExplicitTypecast(str1)
            if len(ex_typecast) != 0:
                for i in ex_typecast:
                    it.append(str(i))
    
    if len(it) != 0:
        # it[0] = [str(item) for item in str(it[0]) if item != '+'] # removing all '+'

        j = ""  
        for k in it[len(it)-1:len(it)]:
            # print
            for i in range(0, len(k)):
                if k[i] != '+':
                     
                    j += k[i]
                    j += " "
        symbol_table.insert(0, ['IT', j])
        it.clear()

    #need ayusin syntax for expression
    semantics_varidents = semantics.getVaridents(str1) #get modified varidents using R operation in semantics part
    if semantics_varidents != 0:
        sem_keys = semantics_varidents.keys()                
        matchkeys = [key for key in sem_keys if any(key == sublist[0] for sublist in symbol_table)]

        for k in symbol_table:
            if k[0] in matchkeys:
                if k[1] != semantics_varidents[k[0]]:
                    k[1] = semantics_varidents[k[0]]
                    semantics_varidents.pop(k[0])

    # print(semantics_varidents)

        if len(semantics_varidents) != 0:
            for k in semantics_varidents:
                arr = []
                arr.append(k)
                arr.append(semantics_varidents[k])
                symbol_table.append(arr)
            
    # return symbol_table
    return symbol_table


def connect_UI(str):
    compiled_lex.clear()
    return lex(str)
    

# # for accepting many input lines from user
# def main():
#     # array_words = []
#     con = True
#     str = ""
#     while con:
#         line = sys.stdin.readline()
    
#         if line == "KTHXBYE\n": #if eto na-encounter mag stop sa pag-accept
#             con = False
#             str += line
#             # array_words.append(str.strip('\n'))
#             break
#         str += line
#         # array_words.append(str.strip('\n'))

#     return str
#     # for string in lex(str):
#     #     print(f'{string[0]} is a {string[1]}')
#     symbolTable(str)
# # main()