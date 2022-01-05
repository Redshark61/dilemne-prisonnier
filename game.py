import random


class Game:

    @classmethod
    def play(cls, players: tuple, index):
        # Check for the special characters (!,=, r)
        cls.checkSpecialChoice(players, index)
        # Get the choices of the players
        playersChoice = [player.choice for player in players]

        # If they play the same choice (e.g [c,c] or [b,b])
        if playersChoice[0] == playersChoice[1]:
            # If it's [c,c], they both cooperate
            if 'c' in playersChoice:
                cls.points((3, 3), players)
                return
            # Otherwise, they both betrayed, so they both get 1 points
            cls.points((1, 1), players)
            return

        # If they play different choices (e.g [c,b] or [b,c])
        # If the first player played 'c', then the second player played 'b'
        if players[0].choice == 'c':
            cls.points((5, 0), players)
        # Orherwise, the first player played 'b', then the second player played 'c'
        else:
            cls.points((0, 5), players)

    @classmethod
    def checkSpecialChoice(cls, players, index):
        for i, player in enumerate(players):
            # If the current player played either ! or =
            if player.choice in ('=', '!'):
                # if the index is 0, then it's the first turn, so we must define a beginning choice
                if index == 0 and player != players[0] and players[0].choice in ('=', '!', 'r'):
                    player.choice = random.choice(["c", "b"])
                    return
                # Otherwise, if it's = then play the same move as the other player
                if player.choice == '=':
                    player.choice = players[0 if i == 1 else 1].choice
                    return
                # Otherwise, it's ! then play the opposite of the other player
                player.choice = 'c' if players[0 if i == 1 else 1].choice == 'b' else 'b'
                return
            # If the player played r
            if player.choice == 'r':
                player.choice = random.choice(["c", "b"])

    @staticmethod
    def points(points, players):
        for index in range(2):
            players[index].score += points[index]
