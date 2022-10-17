import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/semicond.csv',
                   encoding='utf-8', encoding_errors='ignore', sep=';')

stats_data = data.groupby('NumberOfErrors')['NumberOfErrors'].agg('count') \
    .pipe(pd.DataFrame).rename(columns={'NumberOfErrors': 'frequency'})
print(stats_data)

stats_data['rel_freq'] = stats_data['frequency'] / sum(stats_data['frequency'])
stats_data['cum_freq'] = stats_data['rel_freq'].cumsum()
stats_data = stats_data.reset_index()
stats_data

n, bins, patches = plt.hist(x=data, bins='auto', color='#00afcb',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Number or errors')
plt.ylabel('Frequency')

plt.ylim(ymax=np.ceil(n.max() / 10) * 10 if n.max() < 10 else n.max() + 10)
plt.show()

s = np.random.normal(loc=15, scale=3, size=500)
s = np.random.uniform(low=0, high=10, size=500)
s = np.random.beta(a=2, b=10, size=500)
n, bins, patches = plt.hist(x=s, bins='auto', color='#00afcb',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Results')
plt.ylabel('Frequency')

plt.ylim(ymax=np.ceil(n.max() / 10) * 10 if n.max() < 10 else n.max() + 10)
plt.show()