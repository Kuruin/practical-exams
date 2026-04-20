#include <stdio.h>

int main()
{
    char str[10];
    scanf("%s", str);

    if (str[0] == 'a' && str[1] == '+')
        printf("Valid Expression\n");
    else
        printf("Invalid\n");

    return 0;
}