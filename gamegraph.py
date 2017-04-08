#!/usr/bin/env python
"""
This file generates a complete game-graph for Tic-Tac-Toe game.

Author: Abhishek N. Kulkarni (abhibp1993)
Date Modified: 7 April 2017
"""

from networkx import DiGraph
from tictacutils import *


def build_game_graph(state, G=DiGraph()):
    free_cells = free_positions(state)
    states = set()

    if len(free_cells) == 0 or label_state(state) in [XWINS, OWINS, DRAW]:
        return G

    for cell in free_cells:
        tmp_state = mark(state, cell, turn_of(state))
        G.add_node(tmp_state)
        G.add_edge(state, tmp_state, action=cell)

        is_over = label_state(tmp_state)
        if is_over != UNDECIDED:
            continue

        G = build_game_graph(tmp_state, G)
        print G.number_of_nodes()
    return G


if __name__ == '__main__':

    print 'Building Game Graph...'
    init_state = ((None, None, None), (None, None, None), (None, None, None))
    G = build_game_graph(init_state)
    print G.number_of_nodes(), G.number_of_edges()

    # Pickle it up
    pickle_graph(G)