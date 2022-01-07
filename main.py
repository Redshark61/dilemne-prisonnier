import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from game import Game
from players import Player1, Player2


def main():
    """
    Define the main program
    """

    # Erase the data file
    choice = input("Voulez-vous effacer les données précédentes ? (y/n)")
    if choice == "y":
        eraseData()

        choice = input("Jouer: \n1- Toute les stratégies\n2- Fichier de stratégies\n")

        if choice == "1":
            playAll()

        elif choice == "2":
            playStrategy()

    elif choice == "n":
        choice = input("1- Voir le graphique\n2- Tout jouer\n3- Jouer tous les stratégies\n")
        if choice == "1":
            graph(True)
        elif choice == "2":
            playAll()
        elif choice == "3":
            playStrategy()


def playStrategy():

    # Get the strategies from the file
    with open("./strategy/test1.strategy", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Define the players as not ready yet
    isReady = (False, False)
    for line in lines:

        # If the line start with 1: then it's the first player
        if line.startswith("1:"):
            # Take the strategy, and remove the \n and the 1:
            player1 = Player1(line.split('\n')[0][3:])
            # The first player is ready, but not the second yet
            isReady = (True, False)

        # If the line start with 2: then it's the second player
        elif line.startswith("2:"):
            player2 = Player2(line.split('\n')[0][3:])
            # The second player is ready, and the first is the same
            isReady = (isReady[0], True)

        # The tuple is a len of 2, so if there are 2 True, then both players are ready
        if isReady.count(True) == 2:

            # Play 10 times
            for i in range(10):
                # Play 1000 turns
                for i in range(1000):
                    Game.play((player1, player2), i)
                writeData(player1, player2)

            isReady = (False, False)
    graph()


def playAll():

    # List of all the strategies : play all c, all b, random, the same as the opponent, the oppposite of the opponent
    strategies = ['c**', 'b**', 'r', '=', '!']
    iteration = 0
    begin = time.time()

    for strategy1 in strategies:

        for strategy2 in strategies:
            # Initialize the players with their strategy
            player1 = Player1(strategy1)
            player2 = Player2(strategy2)

            # Play 10 times
            for _ in range(10):
                player1.score, player2.score = 0, 0
                iteration += 1

                # Play 1000 games
                for i in range(1000):
                    Game.play((player1, player2), i)
                    # Print how many games are left
                    print(f"{'#'*int(i/1000*10)} - {iteration}/{len(strategies)*len(strategies)*10}", end="\r")
                print("\n")
                # Write the data in the file
                writeData(player1, player2)

    end = time.time()
    print(f"Temps d'exécution: {round(end-begin, 2)}s")
    graph()


def eraseData():
    # Get all the lines (data)
    with open("./score/data.csv", "r", encoding="utf-8") as f:
        data = f.readlines()

    # The "write" mode erases the file and write the new data
    # We write the first line of the csv file
    with open("./score/data.csv", "w", encoding="utf-8") as f:
        f.write(data[0])


def graph(seeGraph=False):
    if not seeGraph:
        choice = input("Voulez-vous voir un graphique :\n1- Oui\n2- Non\n")
    else:
        choice = "1"

    if choice == "1":
        choice = input("Quel graphique voulez-vous voir: (e.g : '!,r') \n")

        # Get all the lines (data)
        with open("./score/data.csv", "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Get the strategies asked by the user
        choices = [i.strip() for i in choice.split(",")]

        # We must keep the data the player asked for
        # so the line start with the first element of the strategies asked by the user
        # and the line got the 2nd strategy asked by the user
        data = [line for line in lines if line.startswith(choice[0]) and choices[1] in line.split(",")[1:]]

        # Split the line along ,
        # It returns a list (contains the data of the line) of list (the list of lines)
        data = [line.split(",") for line in data]
        # Data it a list of two lists, each one is the result of the player
        data = [[int(result[1]) for i, result in enumerate(data) if i % 2 == 1],
                [int(result[3].split('\n')[0]) for i, result in enumerate(data) if i % 2 == 0]]

        # Convert the list into a np array
        data = np.array(data)
        # Get the mean of the player's score
        mean = np.mean(data, axis=1)
        oldMeans = [number for number in mean]
        # Get the score between 1 and 0 (more clear on the graph)
        mean = [number / np.max(mean) for number in mean]
        print(f"{choices=}")
        print(f"{mean=}")

        # Create a bar graph
        if choices.count(choices[0]) == len(choices):
            choices = (choices[0] + '1', choices[1] + '2')

        oldScore = pd.Series(mean)
        plt.figure(figsize=(10, 5))
        ax = oldScore.plot(kind='bar', color=['#0066ff', '#ff0000'], title=f"{choices[0]} vs {choices[1]}")
        ax.set_xlabel("Strategies")
        ax.set_ylabel("Score")
        ax.set_xticklabels(choices)
        ax.tick_params(axis='x', rotation=0)
        rects = ax.patches

        print(oldMeans)
        labels = [str(round(oldMean, 2)) for oldMean in oldMeans]
        for rect, label in zip(rects, labels):
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2, height + 0.01,
                    label, ha='center', va='bottom')

        # Show the graph
        plt.show()


def writeData(player1, player2):
    with open("./score/data.csv", "a", encoding="utf-8") as f:
        f.write(toCSV(player1, player2))


def toCSV(player1, player2):
    return f"\n{str(player1.strategy).replace(',', ';')}, {player1.score},{str(player2.strategy).replace(',', ';')},{player2.score}\n"


if __name__ == "__main__":
    main()
