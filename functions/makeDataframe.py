import pandas as pd
import re

def natural_sort(x): 
    if x == 'Total':
        return ('!',0) #push the total row to the first row
    prefix, num = 0,0
    if x[0].isnumeric():
        prefix, num = '@', int(x[0:-1])
    else:
        prefix, num = x[0], int(x[1:-1])
    return (prefix,num)
        

def make_tactical_df(dict_list,idx):
    df = pd.DataFrame(dict_list)
    df.set_index(pd.Index(idx), inplace=True)
    df.loc['Total'] = df.sum()
    sorted_index = sorted(df.index, key = natural_sort)
    df = df.reindex(sorted_index)
    
    return df
    
""" #add a total row
sum_row = pd.DataFrame(df.sum()).T
df = pd.concat([df, sum_row], ignore_index=True)
df.insert(0, 'Floor', list(floors.keys()) + ['Total'])

#drop columns where its sum is 0
total_row = df.loc[df['Floor'] == 'Total']
cols_to_drop = total_row[total_row == 0].index
print(cols_to_drop)
df.drop(columns=cols_to_drop, inplace=True)

df.to_excel('TNCount.xlsx', index=False) """