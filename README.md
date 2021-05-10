# MinimaxTicTacToeGame

This is a python program that can play Tic-tac-toe based on the minimax algorithm. 
There must be 2 inputs: the first must be a string that encodes the board state, and the second must be a path to an output text file.
The program will use raster scanning to evaluate the provided board state and the print to the terminal the board state resulting from the best possible move. 
The state of all of the nodes visited when traversing the game tree and the minimax value of each visited node will be printed in the output text file. 

Example: 
input: oxxxo-ox-
output to terminal: oxxxo-oxo
output to external text file: oxxxooox- 0
                              oxxxoooxx 0
                              oxxxo-oxo -1
