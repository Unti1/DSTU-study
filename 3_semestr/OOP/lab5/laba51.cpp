
#include<iostream>

using namespace std;
int main() {
	int P[] = { 0, 2, 4, 5, 6, 7, 9, 12 };
	cout << " P[3] = " << P[3] << endl;
	cout << " *P = " << *P << endl;
	cout << " *(P + 4) = " << *(P + 4) << endl;//P[4]
	cout << " *(P + P[2]) = " << *(P + P[2]) << endl;
	cout << **((&P)+5) << endl;
	system("pause");
	return 0;
}