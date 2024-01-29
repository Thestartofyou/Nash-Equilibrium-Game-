import random

def prisoner_dilemma(player1_action, player2_action):
    # Payoffs for the Prisoner's Dilemma
    if player1_action == 'cooperate' and player2_action == 'cooperate':
        return (-1, -1)  # Both players cooperate - mutual cooperation
    elif player1_action == 'cooperate' and player2_action == 'betray':
        return (-3, 0)   # Player 1 cooperates, Player 2 betrays - Player 1 receives a harsher sentence
    elif player1_action == 'betray' and player2_action == 'cooperate':
        return (0, -3)   # Player 1 betrays, Player 2 cooperates - Player 2 receives a harsher sentence
    elif player1_action == 'betray' and player2_action == 'betray':
        return (-2, -2)  # Both players betray - mutual betrayal

def play_game():
    # Players' strategies
    strategies = ['cooperate', 'betray']

    # Randomly choose strategies for both players
    player1_strategy = random.choice(strategies)
    player2_strategy = random.choice(strategies)

    # Get payoffs based on the chosen strategies
    payoffs = prisoner_dilemma(player1_strategy, player2_strategy)

    # Display the results
    print(f"Player 1 chose: {player1_strategy}")
    print(f"Player 2 chose: {player2_strategy}")
    print(f"Payoffs: Player 1 gets {payoffs[0]}, Player 2 gets {payoffs[1]}")

    return payoffs

if __name__ == "__main__":
    play_game()
