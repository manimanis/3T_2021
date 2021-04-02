#ifndef __MAIN_H__
#define __MAIN_H__
using namespace std;
string choose_option(string question, string choice1, string choice2, bool returnBack = true);
int max(int a, int b);
string center(string s, int width);
void game_over(string message);
void show_title(string room);
void winner();
void lobby_room();
void bear_room();
void monster_room();
void diamond_room();
#endif
