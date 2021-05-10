# MinimaxTicTacToeGame

This is a python program that can play Tic-tac-toe based on the minimax algorithm. 
There must be 2 inputs: the first must be a string that encodes the board state, and the second must be a path to an output text file.
The program will use raster scanning to evaluate the provided board state and then print to the terminal the board state resulting from the best possible move. 
The state of all of the nodes visited when traversing the game tree and the minimax value of each visited node will be printed in the output text file. 

When provided with an additional argument 'prune', the program will utilise the Alpha-Beta Pruning algorithm to trim certain branches of the tree and hence have a faster time complexity.

Additionally, for further speed-up of the program, Early Termination is also implemented and will be used when providing an additional input value. This is used to terminal the minimax tree traversal early. 

Example(without Alpha-Beta pruning and Early Termination): 

input: oxxxo-ox- output.txt

output to terminal: oxxxo-oxo

output to output.txt: oxxxooox- 0
                              oxxxoooxx 0
                              oxxxo-oxo -1
