# DILEMNE DU PRISONNIER (prisoner's dilemma)

## Rules

2 players will play # times (1000 by default). If both players betrayed each other, they win 1 point. If they both cooperated, they win 3 points. If one betrayed and the other cooperated, the one who betrayed win 5 point and the other doesn't win any point.

The goal is to determine which strategy is the best.

## Strategy file

Write in a file with the extension `.strategy` the strategy you want to use. **You must leave a final line blank.** The language is the following:

- `1: #` the first player strategy
- `2: #` the second player strategy (on a second line)
- `b` for betray
- `c` for cooperate
- `r` for random
- `b*# + c*#` for a strategy where the player betray # times and then cooperate # times
- `b**` for a strategy where the player betray infinitely
- `c**` for a strategy where the player cooperate infinitely
- `=` for a stragey where the player play the same move as the opponent
- `!` for a strategy where the player play the opposite move as the opponent

If the player who begin play a move involving the opponent move, the first move is random (e.g the player cant play the same move as the opponent if he hasn't already played).
