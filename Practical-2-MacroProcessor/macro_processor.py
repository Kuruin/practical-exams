# Macro Processor (Pass 1 + Expansion)

class MDTEntry:
    def __init__(self, label, opcode, operand):
        self.label = label
        self.opcode = opcode
        self.operand = operand


def read_line(line):
    parts = line.strip().split()
    if len(parts) == 3:
        return parts[0], parts[1], parts[2]
    elif len(parts) == 2:
        return "", parts[0], parts[1]
    elif len(parts) == 1:
        return "", parts[0], ""
    return "", "", ""


def macro_processor():
    MDT = []   # Macro Definition Table
    macroname = ""

    f1 = open("MACIN.txt", "r")
    f2 = open("MACOUT.txt", "w")

    lines = f1.readlines()
    i = 0

    while i < len(lines):
        label, opcode, operand = read_line(lines[i])

        # 🔴 Macro Definition Start
        if opcode == "MACRO":
            macroname = label
            i += 1

            while True:
                label, opcode, operand = read_line(lines[i])

                if opcode == "MEND":
                    break

                MDT.append(MDTEntry(label, opcode, operand))
                i += 1

        # 🔵 Macro Call → Expand
        elif opcode == macroname:
            for entry in MDT:
                f2.write(f"{entry.label}\t{entry.opcode}\t{entry.operand}\n")

        # ⚪ Normal Instruction
        else:
            f2.write(f"{label}\t{opcode}\t{operand}\n")

        i += 1

    f1.close()
    f2.close()

    print("Macro Processing Completed ✅")
    print("Check MACOUT.txt for output")


if __name__ == "__main__":
    macro_processor()