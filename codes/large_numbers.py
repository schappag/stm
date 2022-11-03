import numpy as np
import matplotlib.pyplot as plt

n_rs1 = 10

# Underlying true fraction of failure: 2%
s = 0.02
defect = 0
def_rs1 = []
N = 20001
x_axis = np.linspace(1, N+1, 1)

i: int
for i in range(1, N):
    x = np.random.uniform(0, 1, 1)
    if x <= s:
        defect = defect + 1
    d_proz = defect / i
    def_rs1.append([d_proz])

plt.plot(def_rs1)
plt.ylabel('Relative frequency')
plt.xlabel('Number of experiments')
plt.show()    