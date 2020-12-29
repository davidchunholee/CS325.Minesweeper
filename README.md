# CS325.Minesweeper

David Chunho Lee
CS325 Portfolio Project

URL: 
https://repl.it/@davidchunholee/DavidMinesweeper#main.py


DESCRIPTION:
- Minesweeper is a game played on a m * n grid where the goal is to uncover the entire field without revealing a mine.
- Initially, the mines are randomly generated, hidden, and spread throughout the board. 
- The user starts off by seeing an empty board and has to uncover a cell. 
- If the cell contains a mine, the game is over and the player loses. 
- If it does not contain a mine, the user uncovers a number in that cell. 
- The number displays how many mines are in its vicinity (adjacent, neighboring cell by 1 square).

Table Example:
[x  -  -]
[-  3  -]
[x  -  x]

- In the table above, we can visualize a 3x3 grid. 
- The user uncovers the center number ‘3’ represents how many mines are within its 3x3 square. 
- A mine is represented as a ‘x’ (seen in top-left cell, bottom-left cell, bottom-right cell). 
- In an actual game environment, the mines, ‘x’, will be hidden from the player and the empty cells will be populated with numbers as     well (when the player uncovers it), representing its own number depending on how many mines there are.


RULES:
* A 9x9 board is populated with randomly generated mines and calculated numbers that represent each cell and its surrounding mines. 
* The user can enter their input by entering a row number and a column number, separated by a comma. 
* The following inputs are valid:
      Input: ‘5, 6’
      Input: ‘    7,       4       ‘
      Input: ‘9,1’
	* The following inputs are invalid:
      Input: ‘0, 5’		(number needs to be between 1-9) 
      Input: ‘5 3’		(no comma)
	* If the user uncovers a cell that is not a mine and is not next to a mine, that cell and its neighboring cells are also uncovered for the user. 
	* Once all cells are revealed (without the ones containing mines), the user wins. 


How to Play:
1. Open up the URL to Repl.it (https://repl.it/@davidchunholee/DavidMinesweeper#main.py)
2. Click the 'Run' button when the page loads
3. The board will print onto the terminal on the right half of the window.
4. Enter a row number and column number as requested under the 'Rules' section of this ReadMe.
5. Upon completion of the game, input as directed in the terminal:
	Input: 'y' to play again
	Input: 'b' to print the board
	Input: anything else to quit
