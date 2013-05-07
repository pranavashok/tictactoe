tictactoe
=========

Simple Tic Tac Toe game using heuristics.

The heuristic used here is the count of number of wins the opponent can 
have in the current state.

The computer decides the next move as follows:
- Try out all the possible moves and compute the heuristics of the new 
states
- Take the moves with the least value for the heuristic
- Check whether any of these moves are critical - i.e. if the move isn't 
chosen, the player gets a definite win.
- If such a move exists, choose it. Else choose any other move with the 
least heuristic.
