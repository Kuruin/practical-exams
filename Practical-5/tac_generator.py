# Practical 5: Intermediate Code Generation (Three Address Code)

def generate_TAC(expression):
    operators = ['+', '-', '*', '/', '%']
    temp_count = 0
    temp_vars = []

    tokens = list(expression.replace(" ", ""))

    print("\nOp\tArg1\tArg2\tResult")

    i = 0
    while i < len(tokens):
        if tokens[i] in operators:
            op = tokens[i]
            arg1 = tokens[i - 1]
            arg2 = tokens[i + 1]

            temp = f"t{temp_count}"
            temp_count += 1

            print(f"{op}\t{arg1}\t{arg2}\t{temp}")

            # Replace in tokens
            tokens[i - 1:i + 2] = [temp]
            i = 0  # restart scan
        else:
            i += 1


if __name__ == "__main__":
    expr = input("Enter arithmetic expression: ")
    generate_TAC(expr)