# Shift Reduce Parser in Python

def shift_reduce_parser():
    n = int(input("Enter number of productions: "))

    productions = []
    for _ in range(n):
        left = input("Left side: ")
        right = input("Right side: ")
        productions.append((left, right))

    string = input("Enter input string: ")

    stack = ""

    print("\n--- Parsing Steps ---")

    i = 0
    while i < len(string):
        # SHIFT
        stack += string[i]
        print(f"Shift: {stack}")
        i += 1

        # Try REDUCE
        changed = True
        while changed:
            changed = False
            for left, right in productions:
                if right in stack:
                    stack = stack.replace(right, left, 1)
                    print(f"Reduce: {stack}")
                    changed = True

    # Final result
    if stack == productions[0][0]:
        print("\nString is ACCEPTED ✅")
    else:
        print("\nString is REJECTED ❌")


if __name__ == "__main__":
    shift_reduce_parser()