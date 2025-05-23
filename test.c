#include <stdio.h>

int main()
{
    int a;
    printf("Enter a Number: ");
    scanf("%d", &a);

    for (int i = 0; i <= a; i += 2)
    {
        printf("%d\n", i);
    }
    return 0;
}