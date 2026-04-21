#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
    char s[100];
    int i = 0;

    printf("Enter code: ");
    fgets(s, sizeof(s), stdin);

    while (s[i] != '\0') {

        // Skip spaces
        if (isspace(s[i])) {
            i++;
            continue;
        }

        // Identifier / Keyword
        if (isalpha(s[i])) {
            char word[20];
            int j = 0;

            while (isalpha(s[i])) {
                word[j++] = s[i++];
            }
            word[j] = '\0';

            if (strcmp(word, "int") == 0 ||
                strcmp(word, "float") == 0 ||
                strcmp(word, "if") == 0 ||
                strcmp(word, "else") == 0 ||
                strcmp(word, "while") == 0 ||
                strcmp(word, "return") == 0) {
                printf("%s : Keyword\n", word);
            } else {
                printf("%s : Identifier\n", word);
            }
        }

        // Number
        else if (isdigit(s[i])) {
            char num[20];
            int j = 0;

            while (isdigit(s[i])) {
                num[j++] = s[i++];
            }
            num[j] = '\0';

            printf("%s : Number\n", num);
        }

        // Operator
        else if (strchr("+-*/=", s[i])) {
            printf("%c : Operator\n", s[i]);
            i++;
        }

        else {
            i++;
        }
    }

    return 0;
}
