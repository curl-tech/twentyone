import pandas as pd
from pandas_profiling import ProfileReport


def plot(config):
    df = pd.read_csv(config.raw_data_address)
    if (df.shape[1] <= 15):
        profile = ProfileReport(df,title="Project-21 Report")
        profile.to_file("plot.html")
    else:
        profile = ProfileReport(df,title="Project-21 Report",minimal=True)
        profile.to_file("plot.html")
    
    