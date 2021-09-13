#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
using namespace std;
double f(double x)
{
    return (x-2) * cos(x);
}
double fun(double x)
{
    return -(x-2) * cos(x);
}
int main()
{
    setlocale(LC_CTYPE, "Russian");
    int j, k, n, sign, * Fib;
    int j1, k1, n1, sign1, * Fib1;
    double a, b, x, x1, x2, f1, f2, eps;
    double a1, b1, x3, x4, f3, f4, x5;
    cout << " Исходные данные: " << endl;
    cout << "введите a = ";
    cin >> a;
    a1 = a;
    cout << "введите b = ";
    cin >> b;
    b1 = b;
    cout << "введите n = ";
    cin >> n;
    n1 = n;
    cout << "введите Epsilone = ";
    cin >> eps;
    Fib = (int*)malloc((n + 1) * sizeof(int));
    Fib[0] = 1;
    Fib[1] = 1;
    for (k = 2; k <= n; ++k)
        Fib[k] = Fib[k - 1] + Fib[k - 2];
    //cout << Fib[n] << endl;
    if (n % 2 == 0) sign = 1;
    else sign = -1;
    x1 = a + (Fib[n - 2] * (b - a) - sign * eps) / Fib[n];
    x2 = a + (Fib[n - 1] * (b - a) + sign * eps) / Fib[n];
    f1 = f(x1);
    f2 = f(x2);
    j = 1;
    while (j <= (n - 1))
    {
        if ((n - j + 1) % 2 == 0) sign = 1;
        else sign = -1;
        if (f1 <= f2)
        {
            b = x2;
            x2 = x1;
            f2 = f1;
            x1 = a + (Fib[n - j - 1] * (b - a) - sign * eps) /
                Fib[n - j + 1];
            f1 = f(x1);
            x = x2;
        }
        else
        {
            a = x1;
            x1 = x2;
            f1 = f2;
            x2 = a + (Fib[n - j] * (b - a) + sign * eps) /
                Fib[n - j + 1];
            f2 = f(x2);
            x = x1;
        }
        ++j;

    }
    Fib1 = (int*)malloc((n1 + 1) * sizeof(int));
    Fib1[0] = 1;
    Fib1[1] = 1;
    for (k1 = 2; k1 <= n1; ++k1)
        Fib1[k1] = Fib1[k1 - 1] + Fib1[k1 - 2];
    //cout << Fib1[n1] << endl;
    if (n1 % 2 == 0) sign1 = 1;
    else sign1 = -1;
    x3 = a1 + (Fib1[n1 - 2] * (b1 - a1) - sign1 * eps) /
        Fib1[n1];
    x4 = a1 + (Fib1[n1 - 1] * (b1 - a1) + sign1 * eps) /
        Fib1[n1];
    f3 = fun(x3);
    f4 = fun(x4);
    j1 = 1;
    while (j1 <= (n1 - 1))
    {
        if ((n1 - j1 + 1) % 2 == 0) sign1 = 1;
        else sign1 = -1;
        if (f3 <= f4)
        {
            b1 = x4;
            x4 = x3;
            f4 = f3;
            x3 = a1 + (Fib1[n1 - j1 - 1] * (b1 - a1) - sign1 *
                eps) / Fib1[n1 - j1 + 1];
            f3 = fun(x3);
            x5 = x4;
        }
        else
        {
            a1 = x3;
            x3 = x4;
            f3 = f4;
            x4 = a1 + (Fib1[n1 - j1] * (b1 - a1) + sign1 * eps) /
                Fib1[n1 - j1 + 1];
            f4 = fun(x4);
            x5 = x3;
        }
        ++j1;
    }
    cout << "Результаты оптимизации" << endl;
    cout << fixed;
    cout.precision(10);
    cout << "min = " << x << endl;
    cout << "max = " << x5 << endl;
    cout << "f(min) = " << f(x) << endl;
    cout << "f(max) = " << f(x5) << endl;
    free(Fib);
    fflush(stdin);
    getchar();
    system("pause");
    return 0;
}