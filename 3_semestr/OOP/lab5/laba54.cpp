#define _CRT_SECURE_NO_WARNINGS
#include<iostream>

using namespace std;


void num4(char* string, char* delim, char* outStr) {
	char** buff = new char* [20];
	int i = 0;
	char* p = strtok(string, delim);
	while (p != NULL) {
		buff[i] = new char[strlen(p)];
		buff[i] = p;
		p = strtok(NULL, delim);
		i++;
	}
	for (int j = i - 1; j >= 0; j--) {
		strcat(outStr, buff[j]);
		strcat(outStr, " \0");
	}
}
int main() {
	setlocale(LC_ALL, "ru");

	char string[] = "qwert// poiuy";
	char newString[100] = "";
	char delim[] = " ,.!?";
	num4(string, delim, newString);
	cout << newString;
	system("pause");
	return 0;
}