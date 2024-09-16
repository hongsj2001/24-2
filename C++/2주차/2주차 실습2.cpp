//정수를 입력받아 별을 출력하는 함수 만들기

#include <iostream>
#include <string>
using namespace std;


void printStar(int n, int c);
int main() {
	int c, n;
	cout << "정수 입력 : " << "\n";
	cin >> n;
	cout << "별출력 (1~4) : " << "\n";
	cin >> c;
	printStar(n,c);
}

void printStar(int n, int c) {
	switch (c) {
	case 1:
		for (int i = 1; i <= n; i++) {
			for (int j = 0; j < i; j++) {
				cout << "*";
			}
			cout << "\n";
		}
		break;
	case 2:
		for (int i = 1; i <= n; i++) {
			for (int h = n; h > i; h--) {
				cout << ' ';
			}
			for (int k = 0; k < i; k++) {
				cout << '*';
			}
			cout << "\n";
		}
		break;

	case 3:
		for (int i = 1; i <= n; i++) {
			for (int j = 0; j < i; j++) {
				cout << "*";
			}
			cout << "\n";
		}
		for (int i = n - 1; i >= 0; i--) {
			for (int j = 0; j < i; j++) {
				cout << "*";
			}
			cout << "\n";
		}
		break;

	case 4:
		for (int i = 1; i <= n; i++) {
			for (int h = n; h > i; h--) {
				cout << ' ';
			}
			for (int k = 0; k < i; k++) {
				cout << '*';
			}
			cout << "\n";
		}
		for (int i = n-1; i >= 0; i--) {
			for (int h = n; h > i; h--) {
				cout << ' ';
			}
			for (int k = 0; k < i; k++) {
				cout << '*';
			}
			cout << "\n";
		}
		break;
	}
}
