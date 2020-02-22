import bandit

class banditFactory:

    @staticmethod
    def create():
        return [bandit.Bandit(1.0), bandit.Bandit(2.0), bandit.Bandit(3.0)]