#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
using namespace std;


int main() {
	srand((unsigned)time(0)); //���� �õ� ����
	vector<int>v;
	for (int i = 0; i < 10; i++) {
		int n = rand();
		v.push_back(n);
	}
	vector<int>::iterator it;

	while (true) {
		char select;
		cout << "��� (a), �˻� (b), ����(c), ����(d) : ";
		cin >> select;
		if (select == 'a') {
			for (int i = 0; i < v.size(); i++) {
				cout << v[i] << ' ';
			}
			cout << endl;
		}
		else if (select == 'b') {
			int fnum;
			int n = 0;
			cout << "�˻��� ���� �Է� : ";
			cin >> fnum;
			for (int i = 0; i < v.size(); i++) {
				if (fnum == v[i])
					n += 1;
			}
			cout << n << "�� �ֽ��ϴ�." << endl;
		}
		else if (select == 'c') {
			int dnum;
			int n = 0;
			cout << "������ ���� �Է� : ";
			cin >> dnum;
			it = v.begin();
			for (it = v.begin(); it != v.end(); it++) {
				if (*it == dnum) {
					it = v.erase(it);
					n += 1;
				}
			}
			cout << n << "�� �ֽ��ϴ�." << endl;
		}
		else if (select == 'd') {
			int size = v.size(); //erase�� v.size���� v.size�� �ǽð����� ���ϹǷ� �ʱ� size�� ����
			it = v.begin();
			for (int i = 0; i < size; i++) {
				it = v.begin();
				v.erase(it);
			}
			cout << "���α׷��� �����մϴ�. " << endl;
			break;
		}
		else
			cout << "�ùٸ� ���ڸ� �Է����ֽʽÿ�" << endl;
	}
}