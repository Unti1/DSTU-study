#include <cmath>
#include <iostream>
#include <bitset>

using namespace std;

void task8()
{
	char flag = 0;
	bool s;
	int i = 0;
	cout << "state card " << bitset<8>(flag) << endl;
	int mask;
	cout << "1 - install block | 0 - not install block " << endl;

	cout << "block 1: ";
	cin >> s;
	i = 0;
	if (s)
	{
		flag = flag + pow(2, i);
		s = 1;
	}
	cout << "block 2: ";
	cin >> s;
	i = 1;
	if (s)
	{
		flag = flag + pow(2, i);
		s = 1;

	}
	cout << "block 3: ";
	cin >> s;
	i = 2;
	if (s)
	{
		flag = flag + pow(2, i);
		s = 1;

	}
	cout << "block 4: ";
	cin >> s;
	i = 3;
	if (s)
	{
		flag = flag + pow(2, i);
		s = 1;

	}
	cout << "block 5: ";
	cin >> s;
	i = 4;
	if (s)
	{
		flag = flag + pow(2, i);
		s = 1;
	}
	cout << "block 6: ";
	cin >> s;
	i = 5;
	if (s)
	{
		flag = flag + pow(2, i);
		s = 1;

	}
	cout << "block 7: ";
	cin >> s;
	i = 6;
	if (s)
	{
		flag = flag + pow(2, i);
		s = 1;

	}
	cout << "block 8: ";
	cin >> s;
	i = 7;
	if (s)
	{
		flag = flag + (1 << i);
		s = 1;

	}
	cout << "state card " << bitset<8>(flag) << endl;

	cout << "1 - exempt block | 0 - not exempt block " << endl;

	cout << "block 1: ";
	cin >> s;
	if ((s) && (flag & 1))
		flag &= ~1;
	cout << "block 2: ";
	cin >> s;
	if ((s) && (flag & 2))
		flag = flag & ~2;
	cout << "block 3: ";
	cin >> s;
	if ((s) && (flag & 4))
		flag &= ~4;
	cout << "block 4: ";
	cin >> s;
	if ((s) && (flag & 8))
		flag &= ~8;
	cout << "block 5: ";
	cin >> s;
	if ((s) && (flag & 16))
		flag &= ~16;
	cout << "block 6: ";
	cin >> s;
	if ((s) && (flag & 32))
		flag &= ~32;
	cout << "block 7: ";
	cin >> s;
	if ((s) && (flag & 64))
		flag &= ~64;
	cout << "block 8: ";
	cin >> s;
	if ((s) && (flag & 128))
		flag &= ~128;
	cout << endl << "state card " << bitset<8>(flag) << endl;
	system("pause");
}

int main()
{
	setlocale(LC_ALL, "ru");
	/*
	task2();
	task3();
	task4();
	task5();*/
	/*task6();*/
	/*task7();*/
	task8();
}