#include <iostream>
using namespace std;
#include <numeric>
#include "Complex.h"

Complex::Complex() :Complex(0, 0) {}
Complex::Complex(int real, int imag) {
	this->real = real;
	this->imag = imag;
}
void Complex::complexPrint() {
	if (real != 0)
		cout << real;
	if (imag != 0)
		cout << imag << "j";
	if (real == 0 and imag == 0)
		cout << "0j";
}

Complex Complex::operator+(Complex cmp2) {
	Complex tmp;
	tmp.real = real + cmp2.real;
	tmp.imag = imag + cmp2.imag;
	return tmp;
}
Complex Complex::operator+(int x) {
	Complex tmp;
	tmp.real = real + x;
	tmp.imag = imag;
	return tmp;
}
Complex operator+(int x, Complex cmp) {
	Complex tmp;
	tmp.real = cmp.real + x;
	tmp.imag = cmp.imag;
	return tmp;
}

Complex Complex::operator+=(Complex cmp2) {
	Complex tmp;
	tmp.real = real + cmp2.real;
	tmp.imag = imag + cmp2.imag;
	return tmp;
}
Complex Complex::operator+=(int x) {
	Complex tmp;
	tmp.real = real + x;
	tmp.imag = imag;
	return tmp;
}
Complex operator+=(int x, Complex cmp) {
	Complex tmp;
	tmp.real = cmp.real + x;
	tmp.imag = cmp.imag;
	return tmp;
}

Complex Complex::operator-(Complex cmp2) {
	Complex tmp;
	tmp.real = real - cmp2.real;
	tmp.imag = imag - cmp2.imag;
	return tmp;
}
Complex Complex::operator-(int x) {
	Complex tmp;
	tmp.real = real - x;
	tmp.imag = imag;
	return tmp;
}
Complex operator-(int x, Complex cmp) {
	Complex tmp;
	tmp.real = cmp.real - x;
	tmp.imag = cmp.imag;
	return tmp;
}

Complex Complex::operator-=(Complex cmp2) {
	Complex tmp;
	tmp.real = real - cmp2.real;
	tmp.imag = imag - cmp2.imag;
	return tmp;
}
Complex Complex::operator-=(int x) {
	Complex tmp;
	tmp.real = real - x;
	tmp.imag = imag;
	return tmp;
}
Complex operator-=(int x, Complex cmp) {
	Complex tmp;
	tmp.real = cmp.real - x;
	tmp.imag = cmp.imag;
	return tmp;
}

Complex Complex::operator*(Complex cmp2) {
	Complex tmp;
	tmp.real = real * cmp2.real - imag*cmp2.imag;
	tmp.imag = real * cmp2.imag + cmp2.real*imag;
	return tmp;
}
Complex Complex::operator*(int x) {
	Complex tmp;
	tmp.real = real*x;
	tmp.imag = imag*x;
	return tmp;
}
Complex operator*(int x, Complex cmp) {
	Complex tmp;
	tmp.real = cmp.real * x;
	tmp.imag = cmp.imag * x;
	return tmp;
}

Complex Complex::operator*=(Complex cmp2) {
	Complex tmp;
	tmp.real = real * cmp2.real - imag * cmp2.imag;
	tmp.imag = real * cmp2.imag + cmp2.real * imag;
	return tmp;
}
Complex Complex::operator*=(int x) {
	Complex tmp;
	tmp.real = real * x;
	tmp.imag = imag * x;
	return tmp;
}
Complex operator*=(int x, Complex cmp) {
	Complex tmp;
	tmp.real = cmp.real * x;
	tmp.imag = cmp.imag * x;
	return tmp;
}

Complex Complex::operator*(Complex cmp2) {
	Complex tmp;
	tmp.real = real * cmp2.real - imag * cmp2.imag;
	tmp.imag = real * cmp2.imag + cmp2.real * imag;
	return tmp;
}
Complex Complex::operator*(int x) {
	Complex tmp;
	tmp.real = real * x;
	tmp.imag = imag * x;
	return tmp;
}
Complex operator*(int x, Complex cmp) {
	Complex tmp;
	tmp.real = cmp.real * x;
	tmp.imag = cmp.imag * x;
	return tmp;
}