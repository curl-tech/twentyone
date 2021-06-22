import pandas as pd

def util():
    """
    This method is performing the following operations on the metrics.py which we are getting form pycaret "pull()"
        Removed the blank rows
        Renamed "Prec." to "Precision"
        Dropped the column with Model code 
        Added Index column
    """
    df = pd.read_csv("metrics.csv")
    df = df.rename({'Prec.': 'Precision'}, axis='columns')
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df.to_csv('metrics_without_blank_rows.csv', index=True,index_label ="Sno")
    
