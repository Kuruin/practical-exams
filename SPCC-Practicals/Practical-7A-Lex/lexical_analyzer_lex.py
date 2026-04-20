# Practical 7A: LEX-like Tokenizer

import re

keywords = {"class", "static", "int", "float", "double", "long", "void", "String"}
conditional = {"if", "else", "switch", "case"}
iterative = {"for", "while", "do"}

def classify_token(token):
    if token in keywords:
        return "KEYWORD"
    elif token in conditional:
        return "CONDITIONAL"
    elif token in iterative:
        return "ITERATIVE"
    elif re.match(r'^[0-9]+$', token):
        return "INTEGER"
    elif re.match(r'^[0-9]+\.[0-9]+$', token):
        return "REAL"
    elif re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token):
        return "IDENTIFIER"
    elif token in ['+', '-', '*', '/', '%']:
        return "ARITHMETIC OPERATOR"
    elif token in ['&&', '||', '!']:
        return "LOGICAL OPERATOR"
    elif token in ['<', '>', '<=', '>=', '==']:
        return "RELATIONAL OPERATOR"
    elif token == '=':
        return "ASSIGNMENT OP"
    elif token in ['{', '}']:
        return "BLOCK"
    elif token in ['(', ')']:
        return "PARENTHESIS"
    elif token == ';':
        return "DELIMITER"
    else:
        return "UNKNOWN"


def lexer(input_code):
    tokens = re.findall(r'\w+|==|!=|<=|>=|[{}();+\-*/%]', input_code)

    for token in tokens:
        print(f"{token} ==> {classify_token(token)}")


if __name__ == "__main__":
    code = input("Enter code:\n")
    lexer(code)