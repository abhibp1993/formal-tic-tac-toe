#!/usr/bin/env python
"""
This file generates a never-losing strategy
for computer player Tic-Tac-Toe game.

Author: Abhishek N. Kulkarni (abhibp1993)
Date Modified: 7 April 2017
"""

from networkx import DiGraph
from tictacutils import *


def force_next(aut, player, attr):
    """
    Computes next step of addition to attractor.
    """
    # assert isinstance(aut, Automata), 'fcn: force_next:: aut must be Automata instance'
    # assert isinstance(attr, set), 'fcn: force_next:: attr must be a set.'

    # Define new addition to attractor
    new_attr = set()

    # For all states in attractor till now: do
    for dest_state in attr:

        # For all in_edge neighbors of dest_state do
        for from_state in [in_nbr[0] for in_nbr in aut.in_edges(dest_state)]:
            if from_state in attr:
                continue

            # If from state is "our" player, then we just need one transition
            # taking us from from_state to inside attractor. This is true by
            # construction of this code! Hence, directly add.
            if turn_of(from_state) == player:
                new_attr.add(from_state)

            # Else (player is not "our" player). This requires ALL transitions
            # out from from_state should lead inside attractor. i.e, all
            # neighbors are inside attractor.
            else:
                if set(aut.neighbors(from_state)).issubset(attr):
                    new_attr.add(from_state)

    # Return
    return new_attr


def attractor(prod_game, final_states, player, attr=dict()):
    # Initialize local variables
    if len(attr.keys()) == 0:
        next_level = 1
        attr[0] = final_states
        curr_attr = set(final_states)
    else:
        next_level = max(attr.keys()) + 1
        curr_attr = reduce(set.union, attr.values())

    # Compute next step attractor
    next_attr = force_next(prod_game, player, curr_attr)

    # Update Attractor
    if next_attr == curr_attr or len(next_attr) == 0:  # len(next_attr) == 0:
        return attr
    else:
        attr[next_level] = next_attr
        return attractor(prod_game=prod_game, final_states=final_states, player=player, attr=attr)


if __name__ == '__main__':
    # Load the Game Graph
    try:
        G = unpickle_graph()
        assert isinstance(G, DiGraph), 'Loaded Game-Graph is not a DiGraph instance.'
        print 'Loaded the Game Graph Successfully...'
    except:
        print "Couldn't load the Game-Graph. Application Terminating..."
        exit()

    # Because the game is a simple reachability game,
    # the corresponding automaton has exactly 2 states.
    # Therefore, the product game will also have exactly same
    # number of states as that in the game graph, with the goal
    # states being the final states.

    # Construct Final State Set: Solving Reachability Game for player-O
    final_states = set()
    for st in G.nodes():
        if is_winning(state=st, player=O):
            final_states.add(st)

    print len(final_states)

    # Construct Attractor
    attr = attractor(prod_game=G, final_states=final_states, player=O, attr=dict())

    # Pickle Policy
    safe_st = set(G.nodes()) - reduce(set.union, attr.values())
    pickle_policy(safe_st)

