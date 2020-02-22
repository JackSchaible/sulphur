import numpy as np
import matplotlib.pyplot as plt
import epsilonGreedy

if __name__ == '__main__':
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

