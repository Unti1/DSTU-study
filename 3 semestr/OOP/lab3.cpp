#include <iostream>
#include <bitset>

using namespace std;

int main()
{
    // Задание 2
	
	int i = 5;
	int j = 12;
	int k = 7;
 
	k = (--i + 2 * j - k++, j-- + i - k);

	cout << i << endl << j << endl << k;
	

	/*
	// Задание 3
	int i, j, k, l;
	cin >> i >> j >> k >> l;
	float m;
	cout<<"m= "<<(i > j + k<<1 ? (i >> 4) + (j << 7) - 17 + (k << 1) - (l >> 5) : (i >> 4) + (j << 7) - 17 + (k << 1) + (l >> 5))<< endl;
	
	//каждый сдвиг слева умножаем на 2 ; каждый сдвиг вправо делим на 2 ;
	cout << m;
	*/

	/*
	// Задание 4
	setlocale(LC_ALL, "Russian");
	int x, y;
	cin >> x >> y;
	cout << "В 16-ой системе :" << hex << x << "," << y << endl;
	double m = x | y;
	double k = x & y;
	long g = x << y;
	long h = x >> y;

	cout << hex << m << endl << k << endl << g << endl << h;
	*/

	/*
	// Задание 5
	setlocale(LC_ALL, "Russian");
	int x = 0x41424344;
	cout << "До шифрования" << endl;
	cout << (x >> 24) << endl << ((x & 0xffffff) >> 16) << endl <<((x & 0xffff) >> 8)<<endl << (x & 0xff)<< endl;
	int y = 0x26473829;
	x = (x ^ y);
	cout << "После шифрования" << endl;
	cout << (x >> 24) << endl << ((x & 0xffffff) >> 16) << endl <<((x & 0xffff) >> 8) << endl << (x & 0xff) << endl;
	x = (x ^ y);
	cout << "После расшифровки" << endl;
	cout <<(x >> 24) << endl << ((x & 0xffffff) >> 16) << endl << ((x & 0xffff) >> 8) << endl << (x & 0xff) << endl;
	*/

	/*
	// Задание 6
	int i = 0, r = 0, t = 0;
	cin >> hex >> i;
	i = (i & ~0xFFFF) | ((i & 0xFF) << 8) | ((i >> 8) & 0xFF);
	cout << endl << hex << i << endl;
	*/

	/*
	//Задание 7
	int r = 0, i = 0;

	char c;
	cin >> c;
	

	for (i = 128; i > 0; i /= 2)
	{

		if (c & i)
		{
			cout << c << endl;
			r = r + 1;
		}
	}
	cout << r << endl;
	*/
}
