# Practical 6: Code Generation (TAC → Assembly)

def generate_code():
    try:
        with open("input.txt", "r") as f1, open("output.txt", "w") as f2:
            
            for line in f1:
                parts = line.strip().split()

                if len(parts) != 4:
                    continue

                op, arg1, arg2, result = parts

                if op == '+':
                    f2.write(f"MOV R0, {arg1}\n")
                    f2.write(f"ADD R0, {arg2}\n")
                    f2.write(f"MOV {result}, R0\n")

                elif op == '*':
                    f2.write(f"MOV R0, {arg1}\n")
                    f2.write(f"MUL R0, {arg2}\n")
                    f2.write(f"MOV {result}, R0\n")

                elif op == '-':
                    f2.write(f"MOV R0, {arg1}\n")
                    f2.write(f"SUB R0, {arg2}\n")
                    f2.write(f"MOV {result}, R0\n")

                elif op == '/':
                    f2.write(f"MOV R0, {arg1}\n")
                    f2.write(f"DIV R0, {arg2}\n")
                    f2.write(f"MOV {result}, R0\n")

                elif op == '=':
                    f2.write(f"MOV R0, {arg1}\n")
                    f2.write(f"MOV {result}, R0\n")

        print("Code Generation Completed ✅")
        print("Check output.txt")

    except FileNotFoundError:
        print("input.txt not found ❌")


if __name__ == "__main__":
    generate_code()