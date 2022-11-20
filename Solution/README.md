_NOTE_: This repository is an adaptation of Michael Hein's code at https://github.com/michaelhein39/Dicebot.

## The Dice Game

Each player starts with the same number of dice.

The game proceeds in rounds, with everyone rolling and immediately hiding their dice at the start of each round (so that a player may only see their own dice).

Players have the option to make a *claim* or *call bluff* on the previous claim.

A claim is given by stating a quantity and a die value (1-6). If a player chooses to claim, they must give a quantity that is greater than or equal to the previous quantity given. If the current player claims and gives the same quantity as the previous player, the current player must give a die value that is greater than the previously given die value. (If the current player claims and gives a quantity that is strictly greater than the previous quantity given, then they may give *any* die value.)

For example, if I call 2 "4"s and you are next to move, you can call 3, 4, 5, (etc.) of *any* die value, or you can call 2 "5"s or  2 "6"s.

Or, if you do not think that there are 2 "4s" among all the dice in play, then you can *call bluff*. In that case, everyone in the game shows their rolls. If there are 2 or more "4"s as previously called, then the player who called bluff is wrong and they lose one die. If there are less than 2 "4"s, then the player who made the previous claim is wrong and they lose one die.

In this game, 6s are wild and thus can count as any die value. So if players have to show their "4"s after a bluff call, they must show all of their "4"s AND "6"s. Note though that if players must show their "6"s, they only show "6"s.

## Setup

Run the program with the following:
```
$ python3 run.py <path-to-config-file>
```
A configuration file looks like the following:
```
# of games
# of starting dice per player
verbose? (True/False)
FirstPlayerName
SecondPlayerName
...
LastPlayerName
```
An example configuration file looks like the following:
```
1
3
False
Anthony
Michael
```
