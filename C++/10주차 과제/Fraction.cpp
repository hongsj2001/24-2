#include <iostream>
using namespace std;
#include <numeric>
#include "Fraction.h"

Fraction::Fraction() :Fraction(1, 1) {}
Fraction::Fraction(int denominator) :Fraction(1, denominator) {}
Fraction::Fraction(int numerator, int denominator) {
	this->numerator = numerator;
	this->denominator = denominator;
}
void Fraction::printFraction() {
	cout << "(" << numerator << "/" << denominator << ")";
}
void Fraction::printResult() {
	
	cout << "(" << ((double)numerator/(double)denominator) << ")" << endl;
}
bool Fraction::operator==(Fraction frac2) {
	if ((numerator* frac2.denominator == frac2.numerator * denominator))
		return true;
	else
		return false;
}
Fraction Fraction::operator+=(Fraction frac2) {
	Fraction tmp;
	tmp.numerator = numerator * frac2.denominator + frac2.numerator * denominator;
	tmp.denominator = denominator * frac2.denominator;
	return tmp;
}

Fraction Fraction::operator+(Fraction frac2) {
	Fraction tmp;
	tmp.numerator = numerator* frac2.denominator + frac2.numerator* denominator;
	tmp.denominator = denominator * frac2.denominator;
	return tmp;
}
Fraction Fraction::operator+(int x) {
	Fraction tmp;
	tmp.numerator = numerator + denominator * x;
	tmp.denominator = denominator;
	return tmp;
}
Fraction operator+(int op1, Fraction frac) {
	Fraction tmp;
	tmp.numerator = frac.numerator + frac.denominator * op1;
	tmp.denominator = frac.denominator;
	return tmp;
}

Fraction Fraction::operator-(Fraction frac2) {
	Fraction tmp;
	tmp.numerator = numerator * frac2.denominator - frac2.numerator * denominator;
	tmp.denominator = denominator * frac2.denominator;
	return tmp;
}
Fraction Fraction::operator-(int x) {
	Fraction tmp;
	tmp.denominator = denominator;
	tmp.numerator = numerator - denominator * x;
	return tmp;
}
Fraction operator-(int op1, Fraction frac) {
	Fraction tmp;
	tmp.numerator = frac.denominator * op1 - frac.numerator;
	tmp.denominator = frac.denominator;
	return tmp;
}

Fraction Fraction::operator*(Fraction frac2) {
	Fraction tmp;
	tmp.numerator = numerator * frac2.numerator;
	tmp.denominator = denominator * frac2.denominator;
	return tmp;
}
Fraction Fraction::operator*(int x) {
	Fraction tmp;
	tmp.numerator = numerator * x;
	tmp.denominator = denominator;
	return tmp;
}
Fraction operator*(int op1, Fraction frac) {
	Fraction tmp;
	tmp.numerator = frac.numerator + frac.denominator * op1;
	tmp.denominator = frac.denominator;
	return tmp;
}

Fraction Fraction::operator/(Fraction frac2) {
	Fraction tmp;
	tmp.numerator = numerator * frac2.denominator;
	tmp.denominator = denominator * frac2.numerator;
	return tmp;
}
Fraction Fraction::operator/(int x) {
	Fraction tmp;
	tmp.numerator = numerator;
	tmp.denominator = denominator * x;
	return tmp;
}
Fraction operator/(int op1, Fraction frac) {
	Fraction tmp;
	tmp.numerator = frac.denominator * op1;
	tmp.denominator = frac.numerator;
	return tmp;
}