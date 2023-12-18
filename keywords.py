import re
import sys




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
    r'\s*\"[^\"]*\"\s*': 'YARN Literal',                  
}

def lex(str):
    # global compiled_lex
    compiled_lex = []
    code = str
    if code.strip() != "":  # to avoid error when there is no input
        lexer = LOLLexer(code)
        tokens = lexer.tokenize()
        
        for i in range(0, len(tokens)):
            
            temp = tokens[i].value.rstrip()  # remove leading and trailing space characters 
            val = temp.lstrip()

            # print(tokens[i+1].value)
            
            # print(temp)

            if len(val) > 1 and val[0] == '"' and val[-1] == '"':   # when token is a string literal separate the string delimiter
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
                        tokens[i+1].type = 'Variable Identifier'
                elif tokens[i].type == 'Loop Keyword':
                    if tokens[i+1].type == 'Identifier':
                        tokens[i+1].type = 'Loop Identifier'
                elif tokens[i].type == 'Function Keyword' or tokens[i].type == 'Function Call':
                    if tokens[i+1].type == 'Identifier':
                        tokens[i+1].type = 'Function Identifier'

        # print('\n\nTokens:')
        for token in tokens:
            compiled_lex.append([token.value.rstrip().lstrip(), token.type])
    
        return compiled_lex
    
def symbolTable(str):
    it = []
    symbol_table = []
    # print(lex(str))

    for token in lex(str):
        if token[1].rstrip().lstrip() == 'Variable Identifier':
            arr = []
            matches = re.finditer(r'I HAS A \b'+token[0]+r'\b', str)
            last_occurrence_startIndex = -1
            end_index = -1
            for match in matches:
                last_occurrence_startIndex = match.start()
                end_index = match.end()

            if str[end_index+1:end_index+4].rstrip().lstrip() == "ITZ":
                whole = str[end_index+5:]
                value = re.match(r'(.*)[^\n]*',whole)[0]
                if len(symbol_table) == 0:
                    arr.append(token[0])
                    arr.append(value)
                    symbol_table.append(arr)
                else:
                    for i in symbol_table:
                        if i[0] != token[0]:

                            arr.append(token[0])
                            arr.append(value)
                            symbol_table.append(arr)
                        else:
                            break

        elif token[0].rstrip().lstrip() == 'VISIBLE':
            if len(it) == 0:

                matches = re.finditer(r'\b'+token[0]+r'\b', str)
                for match in matches:
                    last_occurrence_startIndex = match.start()
                    end_index = match.end()
                    whole = str[end_index+1:]
                    value = (re.match(r'(.*)[^ \n]*',whole)[0]).split()
                    temp = []
                    for v in value:
                        c = 0
                        if v[0] == '"' and v[len(v)-1] == '"':
                            temp.append(v)
                        else:
                            for j in symbol_table:
                                if j[0].split() == v.split():
                                    c = 1
                                    temp.append(j[1])
                                    break
                    it.append(temp)
                    temp.clear()

    j = ""   
    for k in it[len(it)-1:len(it)]:
        for i in range(0, len(k)):
            j += k[i]
            j += " "
    
    if len(it) != 0:
        symbol_table.insert(0, ['IT', j])

    
    # print("\nSymbol table:")
    # for j in symbol_table:
    #     print(f"identifier: {j[0]}          value: {j[1]}")
    it.clear()
    return symbol_table


def connect_UI(str):
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