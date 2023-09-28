# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > 2:
        guess = opponent_history[-2]

    return guess

# Solution to defeat opponent

def player(prev_play, opponent_history=[]):
  """Returns a move that is more likely to counter the opponent's previous move."""

  moves = ["R", "P", "S"]

  # If the opponent has played rock twice in a row, play paper.
  if len(opponent_history) >= 2 and opponent_history[-2] == opponent_history[-1] == "R":
    return "P"

  # Otherwise, return a random move.
  return random.choice(moves)
