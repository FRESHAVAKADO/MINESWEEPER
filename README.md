# MINESWEEPER
This project was made with the game minesweeper in mind. In Minesweeper, mines are scattered throughout a board, which is divided into cells. Cells have three states: uncovered, covered and flagged. A covered cell is blank and selectable, while an uncovered cell is exposed. Flagged cells are those marked by the player to indicate a potential mine location.
A player gives the row and column number of a cell to uncover it. If a player uncovers a mined cell, the game ends, as there is only 1 life per game. Otherwise, the uncovered cells displays either a number, indicating the number of mines diagonally and/or adjacent to it, or a blank tile (or "0"), and all adjacent non-mined cells will automatically be uncovered. After inputting  the row ad column number an option will be given to flag the selected cell, if selected option ‘y’ causing ‘F’ to appear on it. Flagged cells are still considered covered, and a player can input the row and column number them to uncover them.
The first square selected in any game will never be a mine.
To win the game, players must uncover all non-mine cells, at which point. Flagging all the mined cells is not required.

# OPTIONS
The first option given after starting the game is ‘Enter Row Number:’ this is used to select the row number.
The second option is ‘Enter Column Number:’ this is used to select the column number.
The 3rd option given after selecting the row and column number is ’Place Flag(y/n)’ this is used to select whether we want to place a flag on the square selected by imputing the row and column number or not.
