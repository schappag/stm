import math

# Number of pairs: ordering matters, repetition not allowed
N = 23
d = 2
pairs = math.factorial(N)/(math.factorial(d)*math.factorial(N-d))
print(pairs)

# Probability of 2 people having different birthdays:
p_different_day = 364/365

# 253 comparisons
p_all_different_days = p_different_day**pairs
p_same_day = 1-p_all_different_days
print(p_same_day)

%matplotlib inline
import matplotlib.pyplot as plt

N = list(range(10,100))
p = []
for i in N:
    pairs = i*(i-1)/2
    p.append(1-p_different_day**pairs)
    
my_list = [0.5 for _ in N]
plt.plot(N,p,'b-',23,p_same_day,'ro',N,my_list,'k-') 
plt.show()