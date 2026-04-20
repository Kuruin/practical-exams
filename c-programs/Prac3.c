#include <stdio.h> #include <ctype.h> #include <string.h>

int main() {
char s[100], b[20]; printf("Enter code: "); fgets(s, 100, stdin);

for (int i = 0, n; s[i]; i += n) { n = 1; // Default jump
if (isspace(s[i])) continue;

if (sscanf(s + i, "%[a-zA-Z]%n", b, &n)) {
char *k[] = {"int", "float", "if", "else", "while", "return", NULL}; char *type = "Identifier";
 
for (int j = 0; k[j]; j++)
if (strcmp(b, k[j]) == 0) type = "Keyword";

printf("%s : %s\n", b, type);
}

else if (sscanf(s + i, "%[0-9]%n", b, &n)) { printf("%s : Number\n", b);
}
else if (strchr("+-*/=", s[i])) {
printf("%c : Operator\n", s[i]);
}
}
return 0;
}