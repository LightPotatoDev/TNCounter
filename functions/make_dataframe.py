import pandas as pd
import re
from .item_dictionary import item_value_dict

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
        

def make_tactical_df(dict_list,room_idx):
    df = pd.DataFrame(dict_list)
    df.set_index(pd.Index(room_idx), inplace=True)
    df.loc['Total'] = df.sum()
    
    sorted_index = sorted(df.index, key = natural_sort)
    df = df.reindex(sorted_index)
    
    cols_to_drop = df.loc[:, df.loc['Total'] == 0]
    df.drop(columns=cols_to_drop, inplace=True)
    
    return df

def make_extra_df(main_df:pd.DataFrame):
    extra_stats = {'Atk':0, 'Def':0, 'Hp':0, 'Mattock':0}
    for name, value in item_value_dict.items():
        if name in main_df.columns:
            number_of_obj = main_df.loc['Total',name]
            for stat, amount in value.items():
                extra_stats[stat] += amount*number_of_obj
        
    extra_df = pd.Series(extra_stats)
    return extra_df