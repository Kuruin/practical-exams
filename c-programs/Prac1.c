#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct SymTab {
    char label[10];
    int addr;
} st[10];

int main() {
    // Input format: {Label, Opcode, Operand}
    char *input[6][3] = {
        {"START", "100", ""},
        {"L1", "MOVER", "AREG,B"},
        {"", "ADD", "AREG,C"},
        {"B", "DS", "1"},
        {"C", "DS", "1"},
        {"", "END", ""}
    };

    int lc, i, sym_count = 0;

    // --- PASS 1: SYMBOL TABLE GENERATION ---
    if (strcmp(input[0][0], "START") == 0) {
        lc = atoi(input[0][1]);
    }

    printf("PASS 1: Assigning Addresses\n");
    for (i = 1; strcmp(input[i][1], "END") != 0; i++) {
        if (strcmp(input[i][0], "") != 0) {
            strcpy(st[sym_count].label, input[i][0]);
            st[sym_count].addr = lc;
            sym_count++;
        }
        printf("LC: %d | Instruction: %s\n", lc, input[i][1]);
        lc++;
    }

    // --- PASS 2: OBJECT CODE GENERATION ---
    printf("\nPASS 2: Generating Machine Code\n");
    for (i = 1; i < 3; i++) { // Only processing the instructions
        char *opcode = input[i][1];
        char *mnemonic = (strcmp(opcode, "MOVER") == 0) ? "04" : "01";
        
        // Simulating a symbol lookup for the 'B' and 'C' addresses
        int addr = (strcmp(opcode, "MOVER") == 0) ? st[0].addr : st[1].addr;
        
        printf("Opcode: %s | Operand Addr: %d\n", mnemonic, addr);
    }

    return 0;
}
