import numpy as np
import matplotlib.pyplot as plt
import bandit
import banditFactory as bf

class result:
    def __init__(self):
        self.mean = 10
        self.n = 0

    def update(self, mean):
        self.n += 1
        self.mean = (1 - 1.0/self.n)*self.mean + 1.0/self.n*mean

class greedyUCB:
    def __init__(self):
        self.iterations = 10000

        self.results = [result(), result(), result()]
        self.bandits = bf.banditFactory.create()
        self.data = np.empty(self.iterations)

    def ucb(self, mean, n, nj):
        if nj == 0:
            return float('inf')
        else:
            return mean + np.sqrt(2*np.log(n) / nj)

    def run(self):
        for i in range(self.iterations):
            n = i + 1

            selectedMachine = np.argmax([self.ucb(r.mean, n, r.n) for r in self.results])

            result = self.bandits[selectedMachine].pull()
            self.results[selectedMachine].update(result)

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

        for result in self.results:
            print(result.mean)

        return cumulative_average
