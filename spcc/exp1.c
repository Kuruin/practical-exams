#include <stdio.h>
#include <string.h>

int main()
{
    char label[10][10], opcode[10][10];
    int loc[10], i = 0, lc = 0;

    printf("Enter instructions (END to stop):\n");

    while (1)
    {
        scanf("%s", opcode[i]);
        if (strcmp(opcode[i], "END") == 0)
            break;

        scanf("%s", label[i]);
        loc[i] = lc;
        lc += 3;
        i++;
    }

    printf("\nSymbol Table:\n");
    for (int j = 0; j < i; j++)
        printf("%s -> %d\n", label[j], loc[j]);

    return 0;
}