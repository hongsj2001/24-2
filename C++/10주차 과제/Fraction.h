#ifndef FRACTION_H
#define FRACTION_H

class Fraction {
private:
	int numerator, denominator;
public:
	Fraction();
	Fraction(int denominator);
	Fraction(int numerator, int denominator);
	void printFraction();
	void printResult();
	bool operator==(Fraction op2);
	Fraction operator+=(Fraction op2);

	Fraction operator+(Fraction op2);
	Fraction operator+(int op2);
	friend Fraction operator+(int x, Fraction op2);
	Fraction operator-(Fraction op2);
	Fraction operator-(int op2);
	friend Fraction operator-(int x, Fraction op2);
	Fraction operator*(Fraction op2);
	Fraction operator*(int op2);
	friend Fraction operator*(int x, Fraction op2);
	Fraction operator/(Fraction op2);
	Fraction operator/(int op2);
	friend Fraction operator/(int x, Fraction op2);

};

#endif
