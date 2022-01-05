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
        if strategy == "r":
            return "r"
        if '+' in strategy:
            if '*' in strategy:
                if [i for i in strategy].count('*') == 2:
                    # strategy like "b*5 + c*8"
                    firstSplittedStrategy = strategy.split('+')[0]
                    firstChoice = firstSplittedStrategy.split('*')[0].strip()
                    numberFirstChoice = firstSplittedStrategy.split('*')[1].strip()

                    secondSplittedStrategy = strategy.split('+')[1]
                    secondChoice = secondSplittedStrategy.split('*')[0].strip()
                    numberSecondChoice = secondSplittedStrategy.split('*')[1].strip()
                    return [(firstChoice, int(numberFirstChoice)), (secondChoice, int(numberSecondChoice))]


class Player1(Strategy):

    def __init__(self, strategy) -> None:
        self.score = 0
        self.wichChoice = 0
        self.howManyTimeChoice = 0
        self.choice = self.strategy = self.checkStrategy(strategy)


class Player2(Strategy):

    def __init__(self, strategy) -> None:
        self.score = 0
        self.wichChoice = 0
        self.howManyTimeChoice = 0
        self.choice = self.strategy = self.checkStrategy(strategy)
