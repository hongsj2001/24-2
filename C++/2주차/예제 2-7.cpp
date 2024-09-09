#include <iostream>
#include <string>
using namespace std;

int main() {
	string song("Falling in love with you");
	string elvis("Elvis Presley");
	string singer;

	cout << song + "를 부른 가수는 ";
	cout << "(힌트 : 첫 글자는 " << elvis[0] << ")? :\n";

	getline(cin, singer);
	if (singer == elvis)
		cout << "정답입니다. ";
	else
		cout << "오답입니다. 정답은 " + elvis + "입니다. \n";
}