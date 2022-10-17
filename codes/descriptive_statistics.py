import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/semicond.csv',
                   encoding='utf-8', encoding_errors='ignore', sep=';')
print(data)


abs_frequ = data.value_counts().sort_index()               # sort index: otherwise first come / first presented
rel_frequ = data.value_counts(normalize=True).sort_index()
cumabs_frequ = abs_frequ.cumsum() # cummulative sum
cumrel_frequ = rel_frequ.cumsum()

print('Absolute frequency: '+str(abs_frequ)+', Sum: '+str(sum(abs_frequ)))
print('Relative frequency: '+str(rel_frequ)+', Sum: '+str(sum(rel_frequ)))
print('Cummulative absolute frequency: '+str(cumabs_frequ))
print('Cummulative relative frequency: '+str(cumrel_frequ))


stats_data = data.groupby('NumberOfErrors')['NumberOfErrors'].agg('count')\
            .pipe(pd.DataFrame).rename(columns={'NumberOfErrors': 'frequency'})
print(stats_data)

stats_data['rel_freq'] = stats_data['frequency']/sum(stats_data['frequency'])
stats_data['cum_freq'] = stats_data['rel_freq'].cumsum()
stats_data = stats_data.reset_index()
stats_data

stats_data.plot.bar(x='NumberOfErrors', y=['rel_freq','cum_freq'], grid=True, figsize=(5,3))

randomInput = pd.Series(np.random.normal(loc = 3, scale = 0.1, size=1000), name = 'values')
data_con = pd.DataFrame(randomInput)
stats_data = data_con.groupby('values')['values'].agg('count')\
            .pipe(pd.DataFrame)\
            .rename(columns={'values': 'frequency'})

stats_data['rel_freq'] = stats_data['frequency']/sum(stats_data['frequency'])
stats_data['cum_freq'] = stats_data['rel_freq'].cumsum()
stats_data = stats_data.reset_index()
stats_data

stats_data.plot(x='values', y='cum_freq', grid=True, figsize=[5,3])

n, bins, patches = plt.hist(x=data, bins='auto', color='#00afcb',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Number or errors')
plt.ylabel('Frequency')

plt.ylim(ymax=np.ceil(n.max() / 10) * 10 if n.max() < 10 else n.max() + 10)

s =  np.random.normal(loc=15, scale=3, size=500)
s =  np.random.uniform(low=0, high=10, size=500)
s =  np.random.beta(a=2, b=10, size=500)
n, bins, patches = plt.hist(x=s, bins='auto', color='#00afcb',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Results')
plt.ylabel('Frequency')

plt.ylim(ymax=np.ceil(n.max() / 10) * 10 if n.max() < 10 else n.max() + 10)

print(data.describe())

print(data.quantile(q=0.75, interpolation='midpoint'))

ax = data.plot.box()
plt.show()

IQR = data['NumberOfErrors'].quantile(q=0.75, interpolation='midpoint')-data['NumberOfErrors'].quantile(q=0.25, interpolation='midpoint')
lowerBound = data['NumberOfErrors'].quantile(q=0.25, interpolation='midpoint')-IQR
upperBound = data['NumberOfErrors'].quantile(q=0.75, interpolation='midpoint')+IQR
data_no_outlier = data[(data['NumberOfErrors']>=lowerBound) & (data['NumberOfErrors']<=upperBound)]
data_outlier = data[(data['NumberOfErrors']<lowerBound) | (data['NumberOfErrors']>upperBound)]

fig, ax = plt.subplots()
boxes = [
    {
        'label' : "Number of errors",
        'whislo': data_no_outlier.min(),    # Bottom whisker position
        'q1'    : data.quantile(q=0.25, interpolation='midpoint'),    # First quartile (25th percentile)
        'med'   : data.quantile(q=0.5, interpolation='midpoint'),    # Median         (50th percentile)
        'q3'    : data.quantile(q=0.75, interpolation='midpoint'),    # Third quartile (75th percentile)
        'whishi': data_no_outlier.max(),    # Top whisker position
        'fliers': data_outlier       # Outliers
    }
]
ax.bxp(boxes, showfliers=True)