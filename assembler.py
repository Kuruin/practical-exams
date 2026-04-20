# 2 Pass Assembler in Python

class Symbol:
    def __init__(self, name, value, length, reloc):
        self.name = name
        self.value = value
        self.length = length
        self.reloc = reloc

class Base:
    def __init__(self, name, content, indicator):
        self.name = name
        self.content = content
        self.indicator = indicator


def read_input():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    print("Contents of input file:")
    for line in lines:
        print("\t" + line.strip())
    return lines


def pass1(lines):
    print("\nPASS 1")
    loc = 0
    base = "15"
    base_table = []

    for line in lines:
        tokens = line.strip().replace(",", " ").split()
        if not tokens:
            continue

        if tokens[0] == "USING":
            base_table.append(Base(base, 0, 'Y'))

        elif tokens[0] not in ["START", "END"]:
            print(f"{loc}\t{tokens[0]}\t", end="")

            if len(tokens) > 1 and tokens[1] in ["DC", "DS"]:
                print(tokens[1])
            else:
                print(f"{tokens[1]}, {base}")

            loc += 4

    return base_table


def build_symbol_table(lines):
    symtab = []
    loc = 0

    for line in lines:
        tokens = line.strip().replace(",", " ").split()
        if not tokens:
            continue

        if tokens[0] in ["USING", "START"]:
            continue

        if tokens[0] in ["L", "ST", "A"]:
            loc += 4
            continue

        symtab.append(Symbol(tokens[0], loc, 4, 'R'))
        loc += 4

    return symtab


def print_tables(symtab, base_table):
    print("\nSymbol Table:")
    print("Symbol\tValue\tLength\tReloc")
    for sym in symtab:
        print(f"{sym.name}\t{sym.value}\t{sym.length}\t{sym.reloc}")

    print("\nBase Table:")
    print("Base\tIndicator\tContent")
    for b in base_table:
        print(f"{b.name}\t{b.indicator}\t\t{b.content}")


def pass2(lines, symtab):
    print("\nPASS 2")
    loc = 0
    base = "15"

    for line in lines:
        tokens = line.strip().replace(",", " ").split()
        if not tokens:
            continue

        if tokens[0] in ["USING", "START", "END"]:
            continue

        print(f"{loc}\t{tokens[0]}\t", end="")

        if len(tokens) > 1 and tokens[1] in ["DC", "DS"]:
            print(tokens[1])
        else:
            print(f"{tokens[1]},", end="")

            symbol_name = tokens[2]
            for sym in symtab:
                if sym.name == symbol_name:
                    print(f"{sym.value}(0,{base})")
                    break

        loc += 4


def main():
    lines = read_input()

    base_table = pass1(lines)
    symtab = build_symbol_table(lines)

    print_tables(symtab, base_table)
    pass2(lines, symtab)


if __name__ == "__main__":
    main()