#include <iostream>
using namespace std;
#include "Fraction.h"

int main() {
	cout << "분수1 (분자 , 분모) 입력 : ";
	int n1, n2, d1, d2, x;
	cin >> n1;
	cin >> d1;
	cout << "분수2 (분자 , 분모) 입력 : ";
	cin >> n2;
	cin >> d2;
	cout << "정수 입력 : ";
	cin >> x;
	Fraction a(n1, d1);
	Fraction b(n2, d2);
	Fraction c;
	cout << "=================================================" << endl;
	cout << "객체	연산자	객체	=	연산수행 (실행 결과)" << endl;
	a.printFraction(); cout << " + "; b.printFraction(); c = a + b; cout << "= "; c.printFraction(); c.printResult();
	a.printFraction(); cout << " - "; b.printFraction(); c = a - b; cout << "= "; c.printFraction(); c.printResult();
	a.printFraction(); cout << " * "; b.printFraction(); c = a * b; cout << "= "; c.printFraction(); c.printResult();
	a.printFraction(); cout << " / "; b.printFraction(); c = a / b; cout << "= "; c.printFraction(); c.printResult();
	cout << "=================================================" << endl;
	cout << "객체	연산자	정수	=	연산수행 (실행 결과)" << endl;
	a.printFraction(); cout << " + "; cout << x; c = a + x; cout << "= "; c.printFraction(); c.printResult();
	a.printFraction(); cout << " - "; cout << x; c = a - x; cout << "= "; c.printFraction(); c.printResult();
	a.printFraction(); cout << " * "; cout << x; c = a * x; cout << "= "; c.printFraction(); c.printResult();
	a.printFraction(); cout << " / "; cout << x; c = a / x; cout << "= "; c.printFraction(); c.printResult();
	cout << "=================================================" << endl;
	cout << "정수	연산자	객체	=	연산수행 (실행 결과)" << endl;
	cout << x << " + "; b.printFraction(); c = x + b; cout << "= "; c.printFraction(); c.printResult();
	cout << x << " - "; b.printFraction(); c = x - b; cout << "= "; c.printFraction(); c.printResult();
	cout << x << " * "; b.printFraction(); c = x * b; cout << "= "; c.printFraction(); c.printResult();
	cout << x << " / "; b.printFraction(); c = x / b; cout << "= "; c.printFraction(); c.printResult();
	cout << "=================================================" << endl;
	cout << "객체	연산자	객체	=	연산수행 (실행 결과)" << endl;
	a.printFraction(); cout << " == "; b.printFraction(); a + b; cout << "= "; c.printFraction(); cout << endl;
	a.printFraction(); cout << " += "; b.printFraction(); c = a += b; cout << "= "; c.printFraction(); c.printResult();
}