#include <stdio.h>
main(void)
{
    printf("for �ݺ��� ����1 : ");

    int i;
    for (i=0; i<10; ++i)
    {
        printf("%d", i);
    }
    printf("\n");

    printf("for �ݺ��� ����2 : ");

    for(int j=0; j<5; ++j)
    {
        printf("%d", j);
    }

    return 0;
}