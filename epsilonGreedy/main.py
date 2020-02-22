import numpy as np
import matplotlib.pyplot as plt
import epsilonGreedy
import greedyOptimistic
import greedyUCB

def compareUCB():
    eGreedy = epsilonGreedy.epsilonGreedy(0.1).run()
    gOptim = greedyOptimistic.greedyOptimistic().run()
    gUCB = greedyUCB.greedyUCB().run()

    # log scale plot
    plt.plot(eGreedy, label='ε = 0.1')
    plt.plot(gOptim, label='Greedy Optimistic')
    plt.plot(gUCB, label='Greedy UCB')
    plt.legend()
    plt.title('Payout over Time (Logarithmic)')
    plt.xlabel('Time (in Pulls)')
    plt.ylabel('Payout')
    plt.xscale('log')
    plt.show()

    # linear plot
    plt.plot(eGreedy, label='ε = 0.1')
    plt.plot(gOptim, label='Greedy Optimistic')
    plt.plot(gUCB, label='Greedy UCB')
    plt.legend()
    plt.title('Payout over Time (Linear)')
    plt.xlabel('Time (in Pulls)')
    plt.ylabel('Payout')
    plt.show()

def compareOptimistic():
    eGreedy = epsilonGreedy.epsilonGreedy(0.1).run()
    gOptimistic = greedyOptimistic.greedyOptimistic().run()

    # log scale plot
    plt.plot(eGreedy, label='ε = 0.1')
    plt.plot(gOptimistic, label='Optimistic = 10')
    plt.legend()
    plt.title('Payout over Time (Logarithmic)')
    plt.xlabel('Time (in Pulls)')
    plt.ylabel('Payout')
    plt.xscale('log')
    plt.show()

    # linear plot
    plt.plot(eGreedy, label='ε = 0.1')
    plt.plot(gOptimistic, label='Optimistic = 10')
    plt.legend()
    plt.title('Payout over Time (Linear)')
    plt.xlabel('Time (in Pulls)')
    plt.ylabel('Payout')
    plt.show()

def compareEpsilons():
    c_1 = epsilonGreedy.epsilonGreedy(0.1).run()
    c_05 = epsilonGreedy.epsilonGreedy(0.05).run()
    c_01 = epsilonGreedy.epsilonGreedy(0.01).run()

    # log scale plot
    plt.plot(c_1, label='ε = 0.1')
    plt.plot(c_05, label='ε = 0.05')
    plt.plot(c_01, label='ε = 0.01')
    plt.legend()
    plt.title('Payout over Time (Logarithmic)')
    plt.xlabel('Time (in Pulls)')
    plt.ylabel('Payout')
    plt.xscale('log')
    plt.show()

    # linear plot
    plt.plot(c_1, label='ε = 0.1')
    plt.plot(c_05, label='ε = 0.05')
    plt.plot(c_01, label='ε = 0.01')
    plt.legend()
    plt.title('Payout over Time (Linear)')
    plt.xlabel('Time (in Pulls)')
    plt.ylabel('Payout')
    plt.show()

if __name__ == '__main__':
    #compareEpsilons()
    #compareOptimistic()
    compareUCB()
    
