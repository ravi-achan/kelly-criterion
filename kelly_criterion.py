#Interactive Tool Visualising Kelly's Criterion

import matplotlib.pyplot as plt
import numpy as np
import random

print('What are the odds in this scenario? (Decimal Odds): ')
o = input()
odds = float(o)

print('What is the probability in this scenario? (as %): ')
p = input()
probability = int(p)
q = 100 - probability

bankroll_initial = 100.0

print('Stake proportion of bankroll (as %): ')
s = input()
stake = float(s)/100


#Initialising axes
x = np.arange(0, 1000, 1)
y = np.zeros(1000)

bankroll = bankroll_initial
y[0] = bankroll_initial

#Calculating user bankroll array
for i in range(1, 1000):
    outcomes = ['Win'] * probability + ['Lose'] * q
    result = random.choice(outcomes)

    if(result == 'Win'):
        bankroll = bankroll - (stake*bankroll) + (stake*bankroll*odds)
        y[i] = bankroll

    elif(result == 'Lose'):
        bankroll = bankroll - (bankroll*stake)
        y[i] = bankroll

#Calculating Kelly's bankroll array
k = np.zeros(1000)
k[0] = bankroll_initial
k_bankroll = bankroll_initial
kelly_stake = ((probability/100)*(odds-1) - (q/100))/(odds-1)
if(kelly_stake > 0):

    for i in range(1, 1000):
        outcomes = ['Win'] * probability + ['Lose'] * q
        result = random.choice(outcomes)

        if(result == 'Win'):
            k_bankroll = k_bankroll - (kelly_stake*k_bankroll) + (kelly_stake*k_bankroll*odds)
            k[i] = k_bankroll

        elif(result == 'Lose'):
            k_bankroll = k_bankroll - (k_bankroll*kelly_stake)
            k[i] = k_bankroll

#If Kelly's function is negative the optimal outcome is to not stake anything
else:
    for i in range(1, 1000):
        k[i] = k_bankroll



#Graphing
plt.plot(x,y, color="#228B22")
plt.plot(x,k, color="#800080")
plt.title('Kelly Criterion')
plt.xlabel('Number of Trials')
plt.ylabel('Bankroll')
plt.show()
