#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	float x = 1.42564;
	cout << fixed << setprecision(1) << setw(10) << x << endl;
	cout << fixed << setprecision(2) << setw(10) << x << endl;
	cout << fixed << setprecision(3) << setw(10) << x << endl;
	cout << fixed << setprecision(4) << setw(10) << x << endl;
	cout << fixed << setprecision(5) << setw(10) << x << endl;
	return 0;
}