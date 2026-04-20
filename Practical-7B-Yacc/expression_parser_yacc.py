# Practical 7B: YACC-like Expression Evaluator

def evaluate_expression(expr):
    try:
        result = eval(expr)
        print(f"\nResult = {result}")
        print("Expression is VALID ✅")
    except:
        print("Expression is INVALID ❌")


if __name__ == "__main__":
    expression = input("Enter arithmetic expression: ")
    evaluate_expression(expression)