import re
import sys

compiled_lex = []

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
    r'\s*BIGGER OF\s+': 'Arithmetic Operation',
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
    r'\s*(NUMBR|NUMBAR|YARN|TROOF|NOOB)\s' : 'Type Literal',  
    r'\s*(WIN|FAIL)\s*': 'TROOF Literal',                 
    r'\s*[a-zA-Z][a-zA-Z0-9_]*\s*': 'Identifier',           
    r'\s*-?(0|[1-9][0-9]*)?\.[0-9]+\s*': 'NUMBAR Literal',  
    r'\s*0\s*|^-?[1-9][0-9]*\s*': 'NUMBR Literal',        
    r'\s*\"[^\"]*\"\s*': 'YARN Literal',                  
}

def lex(str):
    code = str
    if code.strip() != "":  # to avoid error when there is no input
        lexer = LOLLexer(code)
        tokens = lexer.tokenize()
        
        for i in range(0, len(tokens)):
            
            temp = tokens[i].value.rstrip()  # remove leading and trailing space characters 
            val = temp.lstrip()

            if len(val) > 1 and val[0] == '"' and val[-1] == '"':   # when token is a string literal separate the string delimiter
                new = Token('String Delimiter', '"')
                tokens[i].value = val[1:-1]
                tokens.insert(i, new)
                tokens.insert(i+2, new)
            elif 'BTW' in val:
                tokens[i].value = val[4:]
                comment = Token('Comment Delimiter', 'BTW')
                tokens.insert(i, comment)
            
            if tokens[i].type == 'Identifier':
                if tokens[i-1].value.rstrip().lstrip() == 'I HAS A':
                    tokens[i].type = 'Variable Identifier'
                elif tokens[i-1].value.rstrip().lstrip() == 'IM IN YR':
                    tokens[i].type = 'Loop Identifier'
                elif tokens[i-1].value.rstrip().lstrip() == 'HOW IZ I' or tokens[i-1].value == 'I IZ':
                    tokens[i].type = 'Function Identifier'
            
                

        # print('\n\nTokens:')
        for token in tokens:
            compiled_lex.append([token.value.rstrip().lstrip(), token.type])

        return compiled_lex

def connect_UI(str):
    return lex(str)

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

    return str
    # for string in lex(str):
    #     print(f'{string[0]} is a {string[1]}')
#main()