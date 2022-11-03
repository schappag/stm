import matplotlib.pyplot as plt
import numpy as np

n = 1
prob = []
flip = []
mu = []
while n < 1001:
    head = 0
    tail = 0

    for i in range(n):
        if np.random.uniform(0, 1, 1) >= 0.3:
            head += 1
        else:
            tail += 1
    k = head / (head + tail)
    mu.append(0.5)
    prob.append(k)
    flip.append(n)
    n = n + 1

plt.subplot(2, 1, 1)
plt.hist(prob, 100, label='Counts')
plt.legend()


plt.subplot(2, 1, 2)
plt.plot(flip, prob, flip, mu)
plt.xlabel('Number of Flips')
plt.ylabel('Probability of Heads')
plt.grid(True)

plt.show()
