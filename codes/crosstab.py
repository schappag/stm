import pandas as pd
import numpy as np

data = pd.read_csv('C:/Users/s61i46/Dokumente/GitHub/mathematical_methods_stm/jupyter_notebook/Chips_CrossTab.csv',
                   encoding='utf-8', encoding_errors='ignore', sep=';')
data.info()
data.head()

pd.crosstab(index=[data.Batch], columns=[data.Errors],
           rownames=["Randomly chosen Batch"],
            colnames=["Occurence of errors"],
            normalize=False,
            margins=True, 
            margins_name="Totals") 

prob_cond_O = cross_tab.loc["A"].loc["yes"]/cross_tab.loc["A"].loc["Totals"]
print(prob_cond_O)
prob_O = cross_tab.loc["Totals"].loc["yes"]/cross_tab.loc["Totals"].loc["Totals"]
print(prob_O)


d = {'Expected Batch': ['A','B'],
     'NoErrors': [cross_tab.loc["Totals"].loc["no"]*cross_tab.loc["A"].loc["Totals"]/cross_tab.loc["Totals"].loc["Totals"],
                cross_tab.loc["Totals"].loc["no"]*cross_tab.loc["B"].loc["Totals"]/cross_tab.loc["Totals"].loc["Totals"]],
     'YesErrors': [cross_tab.loc["Totals"].loc["yes"]*cross_tab.loc["A"].loc["Totals"]/cross_tab.loc["Totals"].loc["Totals"],
                cross_tab.loc["Totals"].loc["yes"]*cross_tab.loc["B"].loc["Totals"]/cross_tab.loc["Totals"].loc["Totals"]]
    }
data_expected = pd.DataFrame(data=d)
print(data_expected)
print(cross_tab)