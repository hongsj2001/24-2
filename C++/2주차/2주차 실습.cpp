//2���� �ǽ� : ��/����� �̿��� ������ ���

#include <iostream>
#include <string>
using namespace std;


int mul(int x, int y) {
	return x * y;
}

int main() {

	int a, b;
	cout << "���� 2�� �Է� (2~9): \n";
	cin >> a;
	cin >> b;

	string matrix;
	cout << "���� �Է� (����, ����): ";
	cin >> matrix;
	if ((a > 9) or (b > 9) or (a<2) or (b<2)) {
		cout << "2�� 9 ������ ������ �Է��ϼ���. ";
	}
	else {
		if (a > b) {
			int tmp;
			tmp = a;
			a = b;
			b = tmp;
		}

		if (matrix == "����") {
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
		else if (matrix == "����") {
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
			cout << "�ùٸ� ������ �Է��ϼ���";
	}
}
