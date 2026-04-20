#include <stdio.h>

int main()
{
    char exp[20];
    int t = 1;

    scanf("%s", exp);

    for (int i = 0; exp[i]; i++)
    {
        if (exp[i] == '+' || exp[i] == '*')
        {
            printf("t%d = %c %c %c\n", t, exp[i - 1], exp[i], exp[i + 1]);
            t++;
        }
    }

    return 0;
}