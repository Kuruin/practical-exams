#include <stdio.h>

int main() {
    char exp[20];
    int i;

    printf("Enter expression: ");
    scanf("%s", exp);

    printf("\nTarget Code:\n");

    for (i = 0; exp[i] != '\0'; i++) {
        if (exp[i] == '+' || exp[i] == '-' || exp[i] == '*' || exp[i] == '/') {

            printf("MOV R0, %c\n", exp[i - 1]);

            if (exp[i] == '+')
                printf("ADD R0, %c\n", exp[i + 1]);
            else if (exp[i] == '-')
                printf("SUB R0, %c\n", exp[i + 1]);
            else if (exp[i] == '*')
                printf("MUL R0, %c\n", exp[i + 1]);
            else if (exp[i] == '/')
                printf("DIV R0, %c\n", exp[i + 1]);
        }
    }

    return 0;
}
