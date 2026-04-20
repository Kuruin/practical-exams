#include <stdio.h>
#include <string.h>

int main() { char exp[20];
int i, temp = 1; printf("Enter expression: "); scanf("%s", exp);
printf("\nThree Address Code:\n"); for(i = 0; exp[i] != '\0'; i++) {
if(exp[i] == '+' || exp[i] == '-' || exp[i] == '*' || exp[i] == '/') {
printf("t%d = %c %c %c\n", temp, exp[i-1], exp[i], exp[i+1]); exp[i+1] = 't'; // replace with temp (simplified)
temp++;
}
}

printf("Result stored in t%d\n", temp-1);

return 0;
}
