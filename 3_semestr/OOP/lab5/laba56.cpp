
#include<iostream>
#include <iomanip>

using namespace std;

double func(double x)
{
	return x * x;
}

void print_graph(double xMin, double xMax, double(*fun)(double h))

{
	double yScrMin = 1, yScrMax = 90; // масштаб по у
	double x_len, step;
	int h = 0;
	double yScr;
	double yMin, yMax;//min и max значения

	x_len = xMax - xMin; //длина графика по у
	step = x_len / 30; //шаг точек графика
	yMin = yMax = fun(xMin);
	double x = xMin;

	while (x <= xMax) //расчёт yMin и yMax пока мы не дойдем до конца границы по иксу
	{
		double fx = fun(x);//вычисление коорднаты по иксу
		x += step;//увеличиваем шаг
		if (fx < yMin) yMin = fx;
		if (fx > yMax) yMax = fx;
	}

	x = xMin;
	//сама печать графика
	while (x <= xMax)
	{
		yScr = yScrMin + (fun(x) - yMin) / (yMax - yMin) * (yScrMax - yScrMin);//масштабирование
		cout << "|" << setfill(' ') << setw(yScr) << "-" << endl;

		x += step;
	}
}
int main() {
	setlocale(LC_ALL, "ru");
	double  xMin, xМах;
	xMin = 0;//масштаб по х
	xМах = 2;
	print_graph(xMin, xМах, &func);
	system("pause");
	return 0;
}
