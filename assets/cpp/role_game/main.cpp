#include <iostream>
#include "main.h"

using namespace std;

string choose_option(string question, string choice1, string choice2, bool returnBack) {
	string choice;
	bool goodChoice;
	do {
		cout << question << endl;
		if (returnBack) {
			cout << "0: Return back" << endl;
		}
		cout << "1: " << choice1 << endl;
		cout << "2: " << choice2 << endl;
		cout << "Your choice? ";
		
		cin >> choice;
		
		goodChoice = (choice == "1") || (choice == "2") || (returnBack && choice == "0");
		
		if (!goodChoice) {
			cout << "Wrong choice!" << endl;
		}
	} while(!goodChoice);
	
	return choice;
}

int max(int a, int b) {
	return (a > b) ? a : b;
}

string center(string s, int width) {
	int mxwidth = max(s.length(), width);
	string ns(mxwidth, ' ');
	int pos = (mxwidth - s.length()) / 2;
	for (int i = 0; i < s.length(); i++) {
		ns[pos + i] = s[i];
	}
	return ns;
}

void game_over(string message) {
	cout << endl;
	cout << "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" << endl;
	cout << "|                G A M E   O V E R                 |" << endl;
	cout << "|" << center(message, 50) << "|" << endl;
	cout << "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" << endl;
	cout << endl;
}

void show_title(string room) {
	cout << endl;
	cout << "----------------------------------------------" << endl;
	cout << "---      D I A M O N D   H U N T E R       ---" << endl;
	cout << "---" << center(room, 40) << "---" << endl;
	cout << "----------------------------------------------" << endl;
	cout << endl;
}

void winner() {
	show_title("Congratulations, you won the game!");
}

void lobby_room() {
	show_title("Lobby Room");
	
	cout << "You entered the castle, you're in the lobby." << endl;
	cout << "You see two doors in front of you." << endl;
	
	string choice = choose_option("Which door do you want to select?",
                           "Right door", 
                           "Left door");
    
    if (choice == "0") {
    	game_over("You choose to escape you are a coward.");
	} else if (choice == "1") {
		bear_room();
	} else {
		monster_room();
	}
}

void bear_room() {
	show_title("Bear Room");
	
	cout << "You're in the Bear room." << endl;
	cout << "You see a huge bear in front of you." << endl;
	
	string choice = choose_option("What you want to do?",
                           "Beat the bear", 
                           "Escape from the left door");
    
    if (choice == "0" || choice == "2") {
    	lobby_room();
	} else if (choice == "1") {
		game_over("You fight the bear and you died!");
	}
}

void monster_room() {
	show_title("Monster Room");
	
	cout << "You're in the Monster room." << endl;
	cout << "You see a tiny monster in front of you." << endl;
	
	string choice = choose_option("What you want to do?",
                           "Beat the monster to access the right door", 
                           "Escape from the left door");
    
    if (choice == "0") {
    	lobby_room();
	} else if (choice == "1") {
		diamond_room();
	} else {
		game_over("You died of terror in the next room!");
	}
}

void diamond_room() {
	show_title("Diamond Room");
	
	cout << "You're in the Diamond room." << endl;
	cout << "You see a diamond in your left." << endl;
	cout << "And a closed chest in your right." << endl;
	
	string choice = choose_option("What you want to do?",
                           "Take the diamond and leave the castle!", 
                           "Force the chest to win more diamonds.");
    
    if (choice == "0") {
    	monster_room();
	} else if (choice == "1") {
		winner();
	} else {
		game_over("The chest is full of vipers and scorpions!");
	}
}

int main() {
	string choice;
	do {
		lobby_room();
		choice = choose_option("What do you want to do ?", "Replay the game", "Quit", false);
	} while(choice != "2");
	
	return 0;
}

