import matplotlib.pyplot as plt
import random

n = 1
prob = []
flip = []
mu = []
while n < 201:
    head = 0
    tail = 0

    for i in range(n):
        if random.randint(0, 1) == 0:
            head += 1
        else:
            tail += 1
    k = head / (head + tail)
    mu.append(0.5)
    prob.append(k)
    flip.append(n)
    n = n + 1
small_size = 12
plt.rc('font', size=small_size)
plt.rc('axes', titlesize=small_size)
plt.subplot(2, 1, 1)
plt.hist(prob, 100, label='Counts')
plt.legend()


plt.subplot(2, 1, 2)
plt.plot(flip, prob, flip, mu)
plt.xlabel('Number of Flips')
plt.ylabel('Probability of Heads')
plt.grid(True)

plt.show()