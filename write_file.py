
from cProfile import label
from re import M
import pandas as pd

def write_file(test_outputs,test_targets):
    pred = pd.Series(test_outputs)
    label = pd.Series(test_targets)
    data = {'label':label,
       'pred':pred}
    df = pd.DataFrame(data)
    df.to_csv('test_result_del_none_entity0819.txt',index=None,sep='\t')