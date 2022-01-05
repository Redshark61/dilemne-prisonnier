from game import Game
from players import Player1, Player2


def main():
    with open("./strategy/test1.strategy", "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith("1:"):
            player1 = Player1(line[3:-1])
        elif line.startswith("2:"):
            player2 = Player2(line[3:-1])

    for i in range(1000):
        Game.play((player1, player2), i)

    print(f"{player1.score=}")
    print(f"{player2.score=}")


if __name__ == "__main__":
    main()
