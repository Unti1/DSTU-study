#include <iostream>
#include <typeinfo>
#include <string>
#include <iomanip>
using namespace std;

int main()
{
    // задание 1
    double a, b, c;
    cin >> a >> b >> c;
    cout << a + b + c << endl;


    // задание 2
    /*int x, y, z;
    cin >> x >> y >> z;
    string st1, st2, st3;
    cin >> st1 >> st2 >> st3;
    cout.fill('.');
    cout << setw(20) << left << st1 << setw(20) << right << x << endl;
    cout << setw(20) << left << st2 << setw(20) << right << y << endl;
    cout << setw(20) << left << st3 << setw(20) << right << z << endl;*/

    // задание 3
    /////////
    /*setlocale(LC_ALL, "Russian");
	int x;
	float y;
	cout << "Введите значение  x и y(float)\n";
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
	return 0;*/



    // задание 4
    /*double x = 1.2345;
    cout.precision(1);
    cout << setw(20) << x << endl;
    cout.precision(2);
    cout << setw(20) << x << endl;
    cout.precision(3);
    cout << setw(20) << x << endl;
    cout.precision(4);
    cout << setw(20) << x << endl;*/

    // задание 6
    /*int x1, y1, x2, y2;
    char t;
    cin >> t >>  x1 >> t >> y1 >> t;
    cout << '(' << x1 << ',' << y1 << ')' << endl;
    cin >> t >> x2 >> t >> y2 >> t;
    cout << '(' << x2 << ',' << y2 << ')' << endl;*/

    // задание 7
    /*char str[9];
    cin.getline(str, sizeof(str), 'g');
    cout << str << 'g' << endl;*/

    // задание 8
    //////////
    /*string st;
    cin >> st;
    char ch1, ch2;
    ch1 = st[0];
    ch2 = st[1];
    st = st[2, sizeof(st)/sizeof(st[0])];*/

    // задание 9
   /* string q1, q2, q3, q4, q5, o1, o2, o3, o4, o5;
    q1 = "how are you?\n";
    cout << "1. " << q1;
    cout << "- ";
    cin >> o1;
    cout << endl;
    q2 = "who are you ?\n";
    cout << "2. " << q2;
    cout << "- ";
    cin >> o2;
    cout << endl;
    q3 = "what about you?\n";
    cout << "3. " << q3;
    cout << "- ";
    cin >> o3;
    cout << endl;
    q4 = "why mercedes better bmw?\n";
    cout << "4. " << q4;
    cout << "- ";
    cin >> o4;
    cout << endl;
    q5 = "why trump loss?\n";
    cout << "5. " << q5;
    cout << "- ";
    cin >> o5;
    system("cls");
    cout.fill('-');
    cout << '|' << setw(40) << '|' << endl;
    cout << "1. " << q1 << endl;
    cout.fill(' ');
    cout << setw(40) << o1 << endl;
    cout << "2. " << q2 << endl;
    cout << setw(40) << o2 << endl;
    cout << "3. " << q3 << endl;
    cout << setw(40) << o3 << endl;
    cout << "4. " << q4 << endl;
    cout << setw(40) << o4 << endl;
    cout << "5. " << q5 << endl;
    cout << setw(40) << o5 << endl;
    cout.fill('-');
    cout << '|' << setw(40) << '|' << endl;*/


    // задание 10
    /*char c1;
    cin >> c1;
    wchar_t c2;
    wcin >> c2;
    cout << sizeof(c1) << ' ' << c1 << endl << sizeof(c2) << ' ' << c2;
    wcout......*/
}