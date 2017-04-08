#!/usr/bin/env python
"""
This file plays an instance of Tic-Tac-Toe game with computer
using Formal Methods based strategy against a human player.
The computer's objective is to NEVER-LOSE the game. Therefore,
the computer may or may not win, but it's guaranteed that human
will NOT win it!

Author: Abhishek N. Kulkarni (abhibp1993)
Date Modified: 7 April 2017
"""

from networkx import DiGraph
from random import choice
from tictacutils import *


def random_bot(st):
    free_cells = free_positions(state=st)
    return choice(free_cells)


def formal_bot(st):
    """ Makes use of G, policy_x as global variables """
    my_st = tuple(tuple(item) for item in st)

    nbrs = G.neighbors(my_st)
    safe_nbrs = [nbr for nbr in nbrs if nbr in policy_x]

    actions = [G[my_st][nbr]['action'] for nbr in safe_nbrs]

    if len(actions) == 0:
        print 'Oh Almighty... I give up... '

    return choice(actions)


def play_game():
    game_state = [[None, None, None], [None, None, None], [None, None, None]]

    def mark(player, cell):
        if game_state[i][j] is None:
            game_state[i][j] = player
        else:
            raise ValueError('Cannot mark already marked cell.')

    def show_game():
        for row in range(3):
            print game_state[row]
        print '\n'

    # Show Game State
    print "New Game Starting..."

    # Repeat (for 9 steps maximum) until game is won OR player wants to exit
    free_cells = [(i, j) for i in range(3) for j in range(3)]
    for turn in range(5):

        # Random Bot makes a move
        # (i, j) = random_bot(game_state)
        (i, j) = formal_bot(game_state)
        mark(X, (i, j))
        free_cells.remove((i, j))

        # Check if game is won/draw/still on!
        if label_state(game_state) in [XWINS, OWINS, DRAW]:
            break

        # Show Current State
        show_game()

        # Repeat until Human makes a valid move
        while True:
            try:
                val = raw_input('Enter position (i, j) as comma separated values without space: ')
                if val == 'exit':
                    exit()

                i, j = [int(val[0]), int(val[2])]

                if (i, j) in free_cells:
                    mark(O, (i, j))
                    free_cells.remove((i, j))
                    break
            except IndexError:
                pass

        # Check if game is won/draw/still on!
        if label_state(game_state) in [XWINS, OWINS, DRAW]:
            break

    show_game()
    if label_state(game_state) == XWINS: print 'X-Wins'
    if label_state(game_state) == OWINS: print 'O-Wins'
    if label_state(game_state) == DRAW: print 'Draw'
    print 'Game is DONE'


if __name__ == '__main__':
    # Load the Game Graph
    try:
        G = unpickle_graph()
        assert isinstance(G, DiGraph), 'Loaded Game-Graph is not a DiGraph instance.'
        print 'Loaded the Game Graph Successfully...'
    except:
        print "Couldn't load the Game-Graph. Application Terminating..."
        exit()

    # Load the Policy for FM Player
    try:
        policy_x = unpickle_policy()
        print 'Loaded the Policy for Computer Successfully...'
    except:
        print "Couldn't load the Policy for Computer. Application Terminating..."
        exit()


    # PLAY GAME...
    play_game()