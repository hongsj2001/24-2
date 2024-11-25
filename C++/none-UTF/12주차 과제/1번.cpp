#include <iostream>
#include <vector>
using namespace std;

int sum(vector<int>v) {
	int sum = 0;
	for (int i = 0; i < v.size(); i++) {
		sum += v[i];
	}
	return sum;
}

float average(vector<int>v) {
	float average;
	average = (float)sum(v) / (float)v.size();
	return average;
}

int main() {
	vector<int>v;
	vector<int>::iterator it;

	while (true) {
		int input;
		cout << "정수를 입력하세요 (-1000을 입력하면 종료) >> ";
		cin >> input;
		if (input == -1000) {
			int size = v.size();
			it = v.begin();
			for (int i = 0; i < size; i++) {
				it = v.begin();
				v.erase(it);
			}
			break;
		}
		else
			v.push_back(input);
		cout << "합계 : " << sum(v) << ", 평균 : " << average(v) << endl;

	}
}