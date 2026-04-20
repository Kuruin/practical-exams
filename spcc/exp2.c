#include <stdio.h>
#include <string.h>

int main()
{
    char line[20];

    printf("Enter code (END to stop):\n");

    while (1)
    {
        scanf("%s", line);
        if (strcmp(line, "END") == 0)
            break;

        if (strcmp(line, "INCR") == 0)
            printf("ADD 1\n");
        else
            printf("%s\n", line);
    }

    return 0;
}