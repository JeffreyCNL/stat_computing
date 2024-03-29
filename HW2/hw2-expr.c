#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

#define STACK_SIZE 1024

double stack[STACK_SIZE];
int stack_height = 0;

void panic(const char *msg) {
    fprintf(stderr, "%s\n", msg);
    exit(EXIT_FAILURE);
}

void push(double value) {
    if (stack_height == STACK_SIZE)
        panic("stack is too high!");
    stack[stack_height] = value;
    ++stack_height;
}

double pop(void) {
    if (stack_height == 0)
        panic("stack is empty!");
    return stack[--stack_height];
}

int main(int argc, char **argv) {
    int i;
    double value;
    
    for (i = 1; i < argc; ++i) {
        switch (argv[i][0]) {
        case '\0':
            panic("empty command line argument");
            break;
        case '0':
        case '1':
        case '2':
        case '3':
        case '4':
        case '5':
        case '6':
        case '7':
        case '8':
        case '9':
            push(atof(argv[i]));
            break;
        case '+':
            push(pop() + pop());
            break;
        case '-':
            value = pop();
            push(pop() - value);
            break;
        case 'a':
            push(pop() * pop());
            break;
        case '/':
            value = pop();
            push(pop() / value);
            break;
        default:
            panic("unknown operator");
            break;
        }
    }

    printf("%g\n", pop());
    return 0;
}