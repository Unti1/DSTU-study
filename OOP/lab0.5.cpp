#include <iostream>
using namespace std;

int main( )
{
setlocale(LC_ALL,"Russian");
char str1[5];
char str2[3];
cin.getline(str1,5);
cin.clear();
cin.getline(str2,3);
cout<<endl<<"str1 = "<<str1;
cout<<endl<<"str2 = "<<str2<<endl;;
system("pause");
return 0;
}
