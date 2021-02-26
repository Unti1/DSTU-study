#include <iostream>
#include <iomanip>
using namespace std;

int main() 
{
	setlocale(LC_ALL, "Russian");
	int x;
	float y;
	cout << "¬ведите значение переменных x и y\n";
	cin >> x >> y;
	cout.unsetf(ios::dec);
	cout.setf(ios::oct);
	cout.setf(ios::scientific);
	cout << "x^8 => " << x << endl;
	cout.unsetf(ios::oct);
	cout.setf(ios::hex);
	cout << "x^16 => " << x << endl;
	cout << "y => " << y << endl;
	cout << "y => " << fixed << setprecision(3) << y << endl;
	cout << "y => " << fixed << setprecision(2) << y << endl;
	cout << "y => " << fixed << setprecision(1) << y << endl;
	return 0;
}