#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)
int main()
{
	//#1
	int a, b, c;
	scanf("%d %lf %lf", &a, &b, &c);
	printf("%lf \n", a + b + c);

	//#2
	/*int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	char st1[10], st2[10], st3[10];
	scanf("%10s %10s %10s", st1, st2, st3);
	printf("%-5s.......%5d\n", st1, a);
	printf("%-5s.......%5d\n", st2, b);
	printf("%-5s.......%5d\n", st3, c);*/

	//#3
	/*int x;
	double y;
	scanf_s("%d %f", &x, &y);
	printf("%o - 8  %x - 16\n", x, x);
	printf("%.1e %.2e %.3e\n", y, y, y);*/

	//#4
	/*double x = 1.3456;
	printf("%20.0f\n%20.1f\n%20.2f\n%20.3f\n%20.4f\n", x, x, x, x, x);*/

	//#6
	/*int x0, y0, x1, y1;
	scanf("(%d,%d) (%d,%d)", &x0, &y0, &x1, &y1);
	printf("(%d;%d)\n(%d;%d)\n", x0, y0, x1, y1);*/

	//#7
	/*char str[9];
	scanf("%8s\n", str);
	str[7] = 'g';
	str[8] = '\0';
	printf("%s\n", str);
	//free(str);*/

	//#8
	/*char a, b;
	char *str = (char*)malloc(40);
	gets(str);
	a = str[0];
	b = str[1];
	str++;
	str++;
	printf("%c\n%c\n", a, b);
	printf("%s\n", str);*/

	//#9
	/*char* ask1 = "what would you like to learn?\n";
	char *ask2 = "what would you like to learn?\n";
	char *ask3 = "what would you like to learn?\n";
	char *ask4 = "what would you like to learn?\n";
	char *ask5 = "what would you like to learn?\n";
	char* q1 = malloc(40);
	char *q2 = malloc(40);
	char *q3 = malloc(40);
	char *q4 = malloc(40);
	char *q5 = malloc(40);
	printf(ask1);
	gets(q1);
	printf(ask2);
	gets(q2);
	printf(ask3);
	gets(q3);
	printf(ask4);
	gets(q4);
	printf(ask5);
	gets(q5);
	system("cls");
	printf("|.................................................................|\n");
	printf("1. %s\n", ask1);
	printf("%67s\n", q1);
	printf("2. %s\n", ask2);
	printf("%67s\n", q2);
	printf("3. %s\n", ask3);
	printf("%67s\n", q3);
	printf("4. %s\n", ask4);
	printf("%67s\n", q4);
	printf("5. %s\n", ask5);
	printf("%67s\n", q5);
	printf("|.................................................................|\n");*/

	//#10
	/*char c = 'A';
	wchar_t w = L'W';
	printf("%c  %c\n", c, w);
	printf("%d  %d\n", sizeof(c), sizeof(w));*/
	

}