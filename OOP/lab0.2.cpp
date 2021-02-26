#include <iostream>
#include <iomanip>
#include <string>

using namespace std;
int main() 
{
	setlocale(LC_ALL, "Russian");
	string st1,st2,st3;
	double x, y, z;
	cout << "Введите значения x,y,z \n";
	cin >> x >> y >> z;
	cout << "Введите значения st1,st2,st3\n";
	cin >> st1 >> st2 >> st3;
	cout << st1 << setfill('.') << setw(40) << x << endl;
	cout << st2 << setfill('.') << setw(40) << y << endl;
	cout << st3 << setfill('.') << setw(40) << z << endl;
	return 0;
}