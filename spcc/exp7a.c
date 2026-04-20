#include <stdio.h>
#include <ctype.h>

int main()
{
    char ch;
    scanf("%c", &ch);

    if (isalpha(ch))
        printf("Identifier\n");
    else if (isdigit(ch))
        printf("Number\n");
    else
        printf("Operator\n");

    return 0;
}