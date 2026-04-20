#include <stdio.h>
#include <ctype.h>

int main()
{
    char str[50];
    scanf("%s", str);

    for (int i = 0; str[i]; i++)
    {
        if (isalpha(str[i]))
            printf("%c : Identifier\n", str[i]);
        else if (isdigit(str[i]))
            printf("%c : Number\n", str[i]);
        else
            printf("%c : Operator\n", str[i]);
    }

    return 0;
}