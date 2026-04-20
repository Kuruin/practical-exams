#include <stdio.h>

int main()
{
    char exp[20];
    scanf("%s", exp);

    for (int i = 0; exp[i]; i++)
    {
        if (exp[i] == '+')
        {
            printf("MOV R0, %c\n", exp[i - 1]);
            printf("ADD R0, %c\n", exp[i + 1]);
        }
        if (exp[i] == '*')
        {
            printf("MOV R0, %c\n", exp[i - 1]);
            printf("MUL R0, %c\n", exp[i + 1]);
        }
    }

    return 0;
}