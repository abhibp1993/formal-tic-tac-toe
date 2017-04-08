#!/usr/bin/env python
"""
This file provides common functions needed for the Tic-Tac-Toe game.

Author: Abhishek N. Kulkarni (abhibp1993)
Date Modified: 7 April 2017
"""

import pickle
from copy import deepcopy

O = 'O'
X = 'X'

XWINS = 0
OWINS = 1
DRAW = 2
UNDECIDED = 3

WINNING_CONDITION = [
                        [(0, 0), (0, 1), (0, 2)],
                        [(1, 0), (1, 1), (1, 2)],
                        [(2, 0), (2, 1), (2, 2)],
                        [(0, 0), (1, 0), (2, 0)],
                        [(0, 1), (1, 1), (2, 1)],
                        [(0, 2), (1, 2), (2, 2)],
                        [(0, 0), (1, 1), (2, 2)],
                        [(0, 2), (1, 1), (2, 0)],
                    ]


def unpickle_graph():
    with open('tic-tac-toe-game-graph.pkl', 'r') as pkl:
        grf = pickle.load(file=pkl)
        pkl.close()
    return grf


def unpickle_policy():
    with open('tic-tac-toe-safe-policy-X.pkl', 'r') as pkl:
        safe_st = pickle.load(file=pkl)
        pkl.close()
    return safe_st


def free_positions(state):
    return [(i, j) for i in range(3) for j in range(3) if state[i][j] is None]


def label_state(state):
    """
    Returns label of "X-Wins", "O-Wins", "Draw", "No Decision" for given state.
    """
    for element in WINNING_CONDITION:
        # Decouple indices of winning positions
        (i1, j1), (i2, j2), (i3, j3) = element

        # Check for Winner
        if state[i1][j1] == state[i2][j2] == state[i3][j3]:
            if state[i1][j1] == X:
                return XWINS

            if state[i1][j1] == O:
                return OWINS

    # If no ones winning the game, then check for a draw
    if len(free_positions(state)) == 0:
        return DRAW

    return UNDECIDED


def pickle_policy(safe_st):
    with open('tic-tac-toe-safe-policy-X.pkl', 'w') as pkl:
        pickle.dump(obj=safe_st, file=pkl)
        pkl.close()


def is_winning(state, player):
    if player == X:
        return label_state(state) == XWINS
    else:   # player == O:
        return label_state(state) == OWINS


def is_draw(state):
    return label_state(state) == DRAW


def x_positions(state):
    return [(i, j) for i in range(3) for j in range(3) if state[i][j] == X]


def o_positions(state):
    return [(i, j) for i in range(3) for j in range(3) if state[i][j] == O]


def turn_of(state):
    if len(free_positions(state)) == 0 or len(x_positions(state)) == len(o_positions(state)):
        return X
    elif len(x_positions(state)) > len(o_positions(state)):
        return O


def pickle_graph(G):
    with open('tic-tac-toe-game-graph.pkl', 'w') as pkl:
        pickle.dump(obj=G, file=pkl)
        pkl.close()


def show_game(state):
    print
    for row in range(3):
        print state[row]
    print


def mark(state, cell, player):
    """
    Does not mutate state.
    """
    # Uncouple row, col
    m, n = cell

    # Copy and Convert to list
    state_copy = [list(deepcopy(i)) for i in state]

    # Update the mark the state
    if state_copy[m][n] is not None:
        raise ValueError('Cannot set value of occupied cell.')

    state_copy[m][n] = player

    return tuple(tuple(i) for i in state_copy)

