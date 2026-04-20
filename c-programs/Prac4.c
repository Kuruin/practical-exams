#include <stdio.h> #include <string.h>

char s[20] = "$E", in[20], *p; int t = 1, i = 0;

void push(char *m) {
for (int l = strlen(m) - 1; l >= 0; l--) s[++t] = m[l];
}

int main() {
printf("Enter input: "); scanf("%s", in);
strcat(in, "$");

printf("\nStack\tInput\tAction\n"); while (t >= 0) {
printf("%s\t%s\t", s, in + i); char c = s[t--], c_in = in[i]; s[t + 1] = 0;

if (c == c_in) { printf("match\n"); i++; }
else if (c == 'E') { printf("E->TE'\n"); push("TX"); } else if (c == 'X') {
if (c_in == '+') { printf("E'->+TE'\n"); push("+TX"); } else printf("E'->ε\n");
}
else if (c == 'T' && c_in == 'i') { printf("T->i\n"); push("i"); } else return printf("Rejected\n"), 0;
}
printf(in[i] == 0 ? "Accepted\n" : "Rejected\n");
