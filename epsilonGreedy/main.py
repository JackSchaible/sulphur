import numpy as np
import matplotlib.pyplot as plt
import epsilonGreedy
import greedyOptimistic
import greedyUCB

class line:
    def __init__(self, value, label):
        self.value = value
        self.label = label

def drawGraphs(axes):
    # log scale plot
    for axis in axes:
        plt.plot(axis.value, label=axis.label)

    plt.legend()
    plt.title('Payout over Time (Logarithmic)')
    plt.xlabel('Time (in Pulls)')
    plt.ylabel('Payout')
    plt.xscale('log')
    plt.show()

    # linear plot
    for axis in axes:
        plt.plot(axis.value, label=axis.label)

    plt.legend()
    plt.title('Payout over Time (Linear)')
    plt.xlabel('Time (in Pulls)')
    plt.ylabel('Payout')
    plt.show()

def compareUCB():
    eGreedy = epsilonGreedy.epsilonGreedy(0.1).run()
    gOptim = greedyOptimistic.greedyOptimistic().run()
    gUCB = greedyUCB.greedyUCB().run()

    drawGraphs([line(eGreedy, 'ε = 0.1'), line(gOptim, 'Greedy Optimistic'), line(gUCB, 'Greedy UCB')])

def compareOptimistic():
    eGreedy = epsilonGreedy.epsilonGreedy(0.1).run()
    gOptimistic = greedyOptimistic.greedyOptimistic().run()

    drawGraphs([line(eGreedy, 'ε = 0.1'), line(gOptimistic, 'Optimistic = 10')])

def compareEpsilons():
    c_1 = epsilonGreedy.epsilonGreedy(0.1).run()
    c_05 = epsilonGreedy.epsilonGreedy(0.05).run()
    c_01 = epsilonGreedy.epsilonGreedy(0.01).run()

    drawGraphs([line(c_1, 'ε = 0.1'), line(c_05, 'ε = 0.05'), line(c_01, 'ε = 0.01')])

if __name__ == '__main__':
    #compareEpsilons()
    #compareOptimistic()
    compareUCB()
    
