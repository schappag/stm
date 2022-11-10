import numpy as np
import matplotlib.pyplot as plt

import random

def play_round(doors, switch):
    
    car = random.randint(1, doors)
    initial_choice = random.randint(1, doors)

    if initial_choice != car:
        leaves = car 
    else:
        while True:
            leaves = random.randint(1, doors)
            if leaves != initial_choice:
                break
    if switch:
        final_choice = leaves
    else:
        final_choice = initial_choice
        
    victory = 1*(final_choice == car)
    
    return victory, initial_choice, final_choice, car

ac = []
nc = []
N = []
doors = 3
for M in range(1,1000): 
    score = []
    scorenc = []
    runs = 0
    for K in range(1,M): 
        won_game, intial_choice, final_choice, car = play_round(doors, False)
        scorenc.append(won_game) 
        won_game, intial_choice, final_choice, car = play_round(doors, True)
        score.append(won_game) 

    ac.append(np.mean(score))
    nc.append(np.mean(scorenc))
    N.append(M)

plt.plot(N,ac,'b',N,nc,'r')
plt.legend(['change','no change'])
plt.show()


ac = []
nc = []
N = []
doors = 100
for M in range(1,1000): 
    score = []
    scorenc = []
    runs = 0
    for K in range(1,M): 
        won_game, intial_choice, final_choice, car = play_round(doors, False)
        scorenc.append(won_game) 
        won_game, intial_choice, final_choice, car = play_round(doors, True)
        score.append(won_game) 

    ac.append(np.mean(score))
    nc.append(np.mean(scorenc))
    N.append(M)


plt.plot(N,ac,'b',N,nc,'r')
plt.legend(['change','no change'])
plt.show()