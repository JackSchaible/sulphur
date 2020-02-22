import numpy as np

class Bandit:
    def __init__(self, payoutModifier):
        self.payoutModifier = payoutModifier

    def pull(self):
        return np.random.randn() + self.payoutModifier
