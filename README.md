# formal-tic-tac-toe
Implements Formal Methods based Never-Losing Robot Player for Tic-Tac-Toe.

# How to Play the Game
- Clone or Download the ZIP. 
- Run the playgame.py file. 
- At each iteration the game will display current board state and request the human player to enter (row, col) for next move. 
- Human Player must provide (row, col) in strict format --> comma separated integers without any spaces. Eg. "0,0" for top-most left corner, "1,0" for middle cell in left-most column and so on. 

# How computer player thinks...
The computer agent builds a complete game-graph and generates a policy such that it should "never-lose". This is a typical safety game. Equivalently stated, it solves the reachability game for the opponent. 

Note that, computer player is supposed to be defensive and is not programmed to win. So at times it may make funny random decisions as well. But it can be proved that computer will never-lose!
