#include <stdio.h>
#include <string.h>

// Tables needed for Macro Processor
struct MNT { char name[10]; int mdt_ptr; } mnt[5];
char mdt[50][20]; // Macro Definition Table (stores the actual lines)
int mntc = 0, mdtc = 0;

int main() {
    // PASS 1: Store the Definition
    // Let's say we have a macro 'INCR' that does: ADD AREG, B
    strcpy(mnt[mntc].name, "INCR");
    mnt[mntc].mdt_ptr = mdtc;
    mntc++;

    strcpy(mdt[mdtc++], "ADD AREG, B");
    strcpy(mdt[mdtc++], "MEND"); // End of macro

    // PASS 2: Expansion
    char call[10] = "INCR"; // Simulating a macro call in the main program
    printf("Program Code Calling Macro: %s\n", call);
    printf("--- EXPANED CODE ---\n");

    for (int i = 0; i < mntc; i++) {
        if (strcmp(call, mnt[i].name) == 0) {
            int ptr = mnt[i].mdt_ptr;
            while (strcmp(mdt[ptr], "MEND") != 0) {
                printf("+ %s\n", mdt[ptr]); // The '+' sign indicates expanded code
                ptr++;
            }
        }
    }

    return 0;
}

