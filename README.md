# GameStats
A quick and easy way to search your game library

## libraries
Put your game lists (theyre quite easy to get from Steam, Epic Games Store, and GOG) as files with their platform name and no extension (so a file just named `steam` or `epic`) in ~/.gamestats/games/
### Getting Steam Games
In a browser (not the Steam desktop client) go to `Steam > account details > licenses & subscriptions`. From there, you can highlight the whole game table and copy.

### Getting Epic Games Store Games
In a browser, go to the epic games website, then go to `Account > Transactions > Purchase`. Scroll down and keep selecting 'Show more' until no more games show up, then copy the whole table.

### Getting GOG Games
For once, its easy. Go to your GOG.com games page. Open your browsers console and run:
```js
var games = Array.from(document.getElementsByClassName("product-title__text"));
var text = '';
games.forEach(a => text += ("\n" + a.innerHTML));
console.log(text);
```
Then, copy the list.

### Cleaning up Steam and EGS game lists
Before you can use the Steam and EGS game data, you need to get the information you copied into a much easier format. Open up some form of spreadsheet program (Google Sheets, Excel, etc) and paste the list into them. They should auto format back into a table. From there, copy just the games and paste into your library file


## Commands
### find
Searches through all your libraries for games names containg the string. All strings are assessed as lowercase, so no case snesitve searching will work

### number
Finds the number of games in a given library. No argumens will find the number of games in each library. All will combine the number from each library into one list. Any other string will be used to find a library name to search

### help
Shows the help page
