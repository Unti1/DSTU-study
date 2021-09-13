
#include<iostream>


using namespace std;


int** create(int rows, int cols) {
	int** matr;
	matr = new int* [rows];
	for (int i = 0; i < rows; i++) {
		matr[i] = new int[cols];
	}
	return matr;
}

void fill_matr(int** matr, int rows, int cols) {
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			matr[i][j] = rand() % 10 - 5;
			cout << matr[i][j] << "  ";
		}
		cout << endl;
	}
}
double geometric_mean(int** matr, int rows, int cols) {
	double mul = 1;
	int count = 0;
	double x = 0;
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			if (matr[i][j] < 0) {
				count++;

				mul *= matr[i][j];
			}
		}
	}
	if (mul > 0) {
		double step = 1.0 / count;
		x = pow(mul, step);
	}
	else {
		mul *= (-1);
		double step = 1.0 / count;
		x = pow(mul, step);
		x *= (-1);
	}
	return x;
}
int main() {
	setlocale(LC_ALL, "ru");
	int** matr;
	int rows = 0; int cols = 0;
	cout << " Введите количество строк : ";
	cin >> rows;
	cout << " Введите количество столбцов : ";
	cin >> cols;
	matr = create(rows, cols);
	fill_matr(matr, rows, cols);
	int sr_geom = geometric_mean(matr, rows, cols);
	cout << " Среднее геометрическое = " << sr_geom << endl;
	for (int i = 0; i < rows; i++) {
		delete[]matr[i];
	}
	delete[] matr;
	system("pause");
	return 0;
}
