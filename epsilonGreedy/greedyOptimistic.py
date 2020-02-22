import numpy as np
import matplotlib.pyplot as plt
import bandit

class greedyOptimistic:
    def __init__(self):
        self.payoutModifier1 = 1.0
        self.payoutModifier2 = 2.0
        self.payoutModifier3 = 3.0
        self.iterations = 10000

        self.means = [10, 10, 10]

        self.bandits = [bandit.Bandit(self.payoutModifier1), bandit.Bandit(self.payoutModifier2), bandit.Bandit(self.payoutModifier3)]
        self.data = np.empty(self.iterations)
        

    def run(self):
        for i in range(self.iterations):
            selectedMachine = np.argmax(self.means)

            result = self.bandits[selectedMachine].pull()
            n = i + 1
            self.means[selectedMachine] = (1 - 1.0/n)*self.bandits[selectedMachine].payoutModifier + 1.0/n*result

            # for the plot
            self.data[i] = result

        cumulative_average = np.cumsum(self.data) / (np.arange(self.iterations) + 1)

        # plot moving average ctr
        plt.plot(cumulative_average)
        plt.plot(np.ones(self.iterations) * 1)
        plt.plot(np.ones(self.iterations) * 2)
        plt.plot(np.ones(self.iterations) * 3)
        plt.xscale('log')
        plt.xlabel('Iteration')
        plt.ylabel('Cumulative Average')
        plt.show()

        for result in self.means:
            print(result)

        return cumulative_average