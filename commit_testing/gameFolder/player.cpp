#include <string>
#include <iostream>
#include <fstream>
#include "player.h"

using namespace std;

string Player::getName() {
	return Player::playerName;
}

void Player::setName() {
	cout << "Enter your name: ";
	cin >> Player::playerName;
	
	ofstream f_stream("playerNames.txt");
	f_stream << Player::playerName << endl;
	f_stream.close();
}
