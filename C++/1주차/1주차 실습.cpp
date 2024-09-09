//1주차 실습 : 구구단 출력

#include <iostream>
using namespace std;

int mul(int x, int y) {
	return x * y;
}

int main() {
	for (int i = 2; i < 10; i++) {
		for (int j = 1; j < 10; j++) {
			cout << i << "*" << j << "=" << mul(i, j) ;
			if(j<9)
				cout << ",";
			cout << "\t";
		}
		cout << "\n";
	}
	cout << "\n";

	for (int i = 1; i < 10; i++) {
		for (int j = 2; j < 10; j++) {
			cout << j << "*" << i << "=" << mul(i, j);
			if (j < 9)
				cout << ",";
			cout << "\t";
		}
		cout << "\n";
	}
}