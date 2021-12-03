#Interactive Tool Visualising Kelly's Criterion
import matplotlib.pyplot as plt
import numpy as np
import random

def outcome_user_stake(bank_init, stake, odds, probability, trials):
    y = np.zeros(trials)
    bankroll = bank_init
    y[0] = bank_init
    outcomes = ['Win'] * int(probability*100) + ['Lose']*int((1-probability)*100)
    for i in range(1,trials):
        result = random.choice(outcomes)

        if(result == 'Win'):
            bankroll = bankroll + (stake*bankroll*odds) - (stake*bankroll)
            y[i] = bankroll

        elif(result == 'Lose'):
            bankroll = bankroll - (stake*bankroll)
            y[i] = bankroll
    return y

def outcome_kelly_stake(bank_init, odds, probability, trials):

    kelly_stake = probability - ((1-probability)/(odds-1))
    if kelly_stake > 0:
        return outcome_user_stake(bank_init, kelly_stake, odds, probability, trials)
    else:
        y = np.zeros(trials)
        y.fill(bank_init)
        return y

def averaged_outcome_n_repeats(n, bank_init, stake, odds, probability, trials):
    y = np.zeros(trials)
    k = np.zeros(trials)

    for i in range(n):
        y += outcome_user_stake(bank_init, stake, odds, probability, trials)
        k += outcome_kelly_stake(bank_init, odds, probability, trials)

    return y/n, k/n

def plotting(n, bank_init, stake, odds, probability, trials):
    x = np.arange(0,trials,1)
    y, k = averaged_outcome_n_repeats(n, bank_init, stake, odds, probability, trials)

    plt.plot(x,y, color="#228B22") #user plots in green
    plt.plot(x,k, color="#800080") #kelly plots in purple
    plt.title('Kelly Criterion')
    plt.xlabel('Number of Trials')
    plt.ylabel('Bankroll')
    plt.show()

print(outcome_user_stake(100, 0.20, 1.58, 0.7, 100))
print(outcome_kelly_stake(100, 1.58, 0.7, 100))

plotting(1000, 100, 0.20, 1.58, 0.7, 100)
