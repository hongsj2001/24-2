#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
using namespace std;


int main() {
	srand((unsigned)time(0)); //랜덤 시드 생성
	vector<int>v;
	vector<int>::iterator it;
	for (int i = 0; i < 10; i++) {
		int n = rand();
		v.push_back(n);
	}

	while (true) {
		char select;
		cout << "출력 (a), 검색 (b), 삭제(c), 종료(d) : ";
		cin >> select;
		if (select == 'a') {
			for (int i = 0; i < v.size(); i++) {
				cout << v[i] << ' ';
			}
			cout << endl;
		}
		else if (select == 'b') {
			int fnum;
			int n=0;
			cout << "검색할 숫자 입력 : ";
			cin >> fnum;
			cout << endl;
			for (int i = 0; i < v.size(); i++) {
				if (fnum == v[i])
					n += 1;
			}
			cout << n << "개 있습니다." << endl;
		}
		else if (select == 'c') {
			int dnum;
			int n = 0;
			cout << "삭제할 숫자 입력 : ";
			cin >> dnum;
			cout << endl;
			it = v.begin();
			for (it = v.begin(); it != v.end(); it++) {
				if (*it == dnum) {
					it = v.erase(it);
					n += 1;
				}
			}
			cout << n << "개 있습니다." << endl;

		}
		else if (select == 'd') {
			for (it = v.begin(); it != v.end(); it++) {
				cout << *it << endl;
				it = v.erase(it);
			}


			cout << "프로그램을 종료합니다. " << endl;
			//break;
		}
		else
			cout << "올바른 문자를 입력해주십시오" << endl;
	}
}