import pandas as pd
import re

def natural_sort(x): 
    if x == 'Total':
        return ('!',0,0) #push the total row to the first row
    prefix, n1, n2 = '', 0, 0

    if x[0].isnumeric():
        prefix = '@'
    else:
        prefix = x[0]
        
    numbers = re.findall(r'\d+', x)
    if len(numbers) == 1:
        n1 = int(numbers[0])
    if len(numbers) == 2:
        n1, n2 = int(numbers[0]), int(numbers[1])
        
    return (prefix,n1,n2)
        

def make_tactical_df(dict_list,idx):
    df = pd.DataFrame(dict_list)
    df.set_index(pd.Index(idx), inplace=True)
    df.loc['Total'] = df.sum()
    
    sorted_index = sorted(df.index, key = natural_sort)
    df = df.reindex(sorted_index)
    
    cols_to_drop = df.loc[:, df.loc['Total'] == 0]
    df.drop(columns=cols_to_drop, inplace=True)
    
    return df