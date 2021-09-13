
#include<iostream>

using namespace std;

void num2(int* x, int* y) {
	int tmp = 0;
	tmp = *x;
	*x = *y;
	*y = tmp;
}
int main() {
	setlocale(LC_ALL, "ru");
	int x, y;
	cout << " Введите значения x, y:" << endl;
	cin >> x >> y;
	num2(&x, &y);
	cout << " x = " << x << " y = " << y;
	system("pause");
	return 0;
}