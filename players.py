class Strategy:

    @staticmethod
    def checkStrategy(strategy) -> str:
        if strategy == "c**":
            return "c"
        if strategy == "b**":
            return "b"
        if strategy == "=":
            return "="
        if strategy == "!":
            return "!"


class Player1(Strategy):

    def __init__(self, strategy) -> None:
        self.score = 0
        self.choice = self.checkStrategy(strategy)


class Player2(Strategy):

    def __init__(self, strategy) -> None:
        self.score = 0
        self.choice = self.checkStrategy(strategy)
