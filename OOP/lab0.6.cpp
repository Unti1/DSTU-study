#include <iostream>
#include <stdio.h> 
 
main()
{
    setlocale(LC_ALL,"Russian");
    int x,y,x1,y1;
    printf("Введите начало координат ");
    scanf("%d,%d",&x,&y);
    printf("Введите конец координат ");
    scanf("%d,%d",&x1,&y1);
    printf("Координаты начала %d,%d\n",x,y);
    printf("Координаты конца %d,%d\n",x1,y1);
    system("pause");
 }