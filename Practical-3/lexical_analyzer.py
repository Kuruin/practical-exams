# Lexical Analyzer in Python

import string

# Keywords list
keywords = ["int", "float", "if", "else", "while"]

def is_keyword(word):
    return word in keywords


def lexical_analyzer(input_string):
    i = 0
    n = len(input_string)

    while i < n:
        
        # IDENTIFIER or KEYWORD
        if input_string[i].isalpha():
            token = ""
            while i < n and input_string[i].isalnum():
                token += input_string[i]
                i += 1

            if is_keyword(token):
                print(f"{token} : KEYWORD")
            else:
                print(f"{token} : IDENTIFIER")

        # NUMBER
        elif input_string[i].isdigit():
            token = ""
            while i < n and input_string[i].isdigit():
                token += input_string[i]
                i += 1

            print(f"{token} : NUMBER")

        # OPERATOR
        elif input_string[i] in ['+', '-', '*', '/', '=']:
            print(f"{input_string[i]} : OPERATOR")
            i += 1

        # SEPARATOR
        elif input_string[i] in [';', ',', '(', ')', '{', '}']:
            print(f"{input_string[i]} : SEPARATOR")
            i += 1

        # IGNORE SPACES
        elif input_string[i] in [' ', '\n', '\t']:
            i += 1

        # INVALID
        else:
            print(f"{input_string[i]} : INVALID CHARACTER")
            i += 1


# MAIN
if __name__ == "__main__":
    user_input = input("Enter a C statement: ")
    lexical_analyzer(user_input)