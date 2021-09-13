
#include<iostream>

using namespace std;

int* num3_f1(int size) {
	int* mas = new int[size];
	cout << " Массив : ";
	for (int i = 0; i < size; i++) {
		mas[i] = rand() % 20;
		cout << mas[i] << "  ";
	}
	return mas;
}

void num3_f2(int** array, int size) {
	*array = new int[size];
	cout << endl << " Массив : ";
	for (int i = 0; i < size; i++) {
		(*array)[i] = rand() % 20;
		cout << (*array)[i] << "  ";
	}
	cout << endl;
}
int main() {
	setlocale(LC_ALL, "ru");
	int size = 15;
	int* mas;
	mas = num3_f1(size);
	delete[] mas;
	

	num3_f2(&mas, size);
	delete[] mas;
	system("pause");
	return 0;
}