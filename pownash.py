"""Finds Nash equilibria for proof-of-work cryptocurrency."""

import argparse

parser = argparse.ArgumentParser(description='Finds Nash equilibria for proof-of-work cryptocurrency.')
parser.add_argument('--players', type=int, default=2, help='Number of players')
parser.add_argument('--reward', type=int, default=100, help='Block reward')
args = parser.parse_args()

PLAYERS = args.players
REWARD = args.reward

def profit_for_player(state, player):
    pow_power = sum(state)
    player_revenue = state[player] / pow_power * REWARD
    profit = player_revenue - state[player]
    return profit

def player_moves(state, player):
    if state[player] > 0 and sum(state) > 1:
        yield state[:player] + [state[player] - 1] + state[player + 1:]
    yield state[:player] + [state[player] + 1] + state[player + 1:]

def evolve_state(state):
    for player in range(PLAYERS):
        current_profit = profit_for_player(state, player)
        for new_state in player_moves(state, player):
            if profit_for_player(new_state, player) > current_profit:
                return new_state
    return state

state = [0] * PLAYERS
state[0]  = 1
old_state = None

while state != old_state:
    print(state, sum(state))
    old_state = state
    state = evolve_state(state)
