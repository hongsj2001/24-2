//2주차 실습 : 입/출력을 이용한 구구단 출력

#include <iostream>
#include <string>
using namespace std;


int mul(int x, int y) {
	return x * y;
}

int main() {

	int a, b;
	cout << "정수 2개 입력 (2~9): \n";
	cin >> a;
	cin >> b;

	string matrix;
	cout << "방향 입력 (가로, 세로): ";
	cin >> matrix;
	if ((a > 9) or (b > 9) or (a<2) or (b<2)) {
		cout << "2와 9 사이의 정수를 입력하세요. ";
	}
	else {
		if (a > b) {
			int tmp;
			tmp = a;
			a = b;
			b = tmp;
		}

		if (matrix == "가로") {
			for (int i = a; i < b + 1; i++) {
				for (int j = 1; j < 10; j++) {
					cout << i << "*" << j << "=" << mul(i, j);
					if (j < 9)
						cout << ",";
					cout << "\t";
				}
				cout << "\n";
			}
		}
		else if (matrix == "세로") {
			for (int i = 1; i < 10; i++) {
				for (int j = a; j < b + 1; j++) {
					cout << j << "*" << i << "=" << mul(i, j);
					if (j < b)
						cout << ",";
					cout << "\t";
				}
				cout << "\n";
			}
		}
		else
			cout << "올바른 방향을 입력하세요";
	}
}
