#include <stdio.h>
main(void)
{
    char op;
    int a, b;

    printf("===���� ���α׷�=== \n");
    printf("������ �Է��ϼ���.(��: 3+3) \n");
    scanf("%d %c %d", &a, &op, &b);

    if(op=='+') printf("\n%d", a+b);
    else if(op=='-') printf("\n%d", a-b);
    else if(op=='*') printf("\n%d", a*b);
    else if(op=='/') printf("\n%d", a/b);
    else printf("\n�߸��Է��ϼ̽��ϴ�.");

    return 0;
}