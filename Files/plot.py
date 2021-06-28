import os
import yaml
from yaml.loader import SafeLoader
import pandas as pd
from pandas_profiling import ProfileReport


def plot(config):
    config=yaml.load(open(config),Loader=SafeLoader)
    df = pd.read_csv(config["raw_data_address"])
    plotFileLocation=os.path.join(config["location"],"plot.html")
    if (df.shape[1] <= 15):
        profile = ProfileReport(df,title="Project-21 Report")
        profile.to_file(plotFileLocation)
    else:
        profile = ProfileReport(df,title="Project-21 Report",minimal=True)
        profile.to_file(plotFileLocation)
    return plotFileLocation
    
    