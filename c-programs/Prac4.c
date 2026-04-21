#include <stdio.h>
#include <string.h>

int main() {
    char input[20];
    int i;

    printf("Enter input: ");
    scanf("%s", input);

    // Check pattern: i+i+i...
    if (input[0] != 'i') {
        printf("Rejected\n");
        return 0;
    }

    for (i = 1; input[i] != '\0'; i += 2) {
        if (input[i] != '+' || input[i + 1] != 'i') {
            printf("Rejected\n");
            return 0;
        }
    }

    printf("Accepted\n");
    return 0;
}
