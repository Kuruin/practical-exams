#include <stdio.h>
#include <string.h>

int main()
{
    char str[20];
    int a = 0, b = 0;

    scanf("%s", str);

    for (int i = 0; str[i]; i++)
    {
        if (str[i] == 'a')
            a++;
        if (str[i] == 'b')
            b++;
    }

    if (a == b)
        printf("Accepted\n");
    else
        printf("Rejected\n");

    return 0;
}