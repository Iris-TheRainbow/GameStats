# GameStats
A quick and easy way to search your game library

## libraries
Put your game lists (theyre quite easy to get from Steam, Epic Games Store, and GOG) as files with their platform name and no extension (so a file just named `steam` or `epic`) in ~/.gamestats/games/

## Commands

### find
Searches through all your libraries for games names containg the string. All strings are assessed as lowercase, so no case snesitve searching will work

### number
Finds the number of games in a given library. No argumens will find the number of games in each library. All will combine the number from each library into one list. Any other string will be used to find a library name to search

### libraries
Libraries are lists of your games put in ~/.gamestats/games
Libraries are just text list of games, stored in extnsionless files with the name of their launcher

### help
Shows the help page
