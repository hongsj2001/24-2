#ifndef COMPLEX_H
#define COMPLEX_H

class Complex {
private:
	int real, imag;
public:
	Complex();
	Complex(int real, int imag);
	void complexPrint();

	Complex operator+(Complex cmp2);
	Complex operator+(int op2);
	friend Complex operator+(int x, Complex cmp2);

	Complex operator-(Complex cmp2);
	Complex operator-(int op2);
	friend Complex operator-(int x, Complex cmp2);

	Complex operator*(Complex cmp2);
	Complex operator*(int op2);
	friend Complex operator*(int x, Complex cmp2);

	Complex operator/(Complex cmp2);
	Complex operator/(int op2);
	friend Complex operator/(int x, Complex cmp2);

	Complex operator+=(Complex cmp2);
	Complex operator+=(int op2);
	friend Complex operator+=(int x, Complex cmp2);

	Complex operator-=(Complex cmp2);
	Complex operator-=(int op2);
	friend Complex operator-=(int x, Complex cmp2);

	Complex operator*=(Complex cmp2);
	Complex operator*=(int op2);
	friend Complex operator*=(int x, Complex cmp2);

	Complex operator/=(Complex cmp2);
	Complex operator/=(int op2);
	friend Complex operator/=(int x, Complex cmp2);

};
#endif

