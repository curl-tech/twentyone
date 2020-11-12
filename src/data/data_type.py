from enum import Enum

class DataType(Enum):
    # When you add a new data type, modify from_string method accordingly
    Image = 0
    Text = 1
    Tabular = 2
    Audio = 3
    Single_TS = 4    
    Multi_TS = 5   
    Location = 6
    Graph = 7

    @staticmethod
    def from_str(dt_str):
        l_dt_str = dt_str.lower()

        if l_dt_str == "image":
            return DataType.Image
        elif l_dt_str == "text":
            return DataType.Text
        elif l_dt_str == "audio":
            return DataType.Audio
        elif l_dt_str == "tabular":
            return DataType.Tabular
        elif l_dt_str == "single_ts":
            return DataType.Single_TS
        elif l_dt_str == "multi_ts":
            return DataType.Multi_TS
        elif l_dt_str == "location":
            return DataType.Location
        elif l_dt_str == "graph":
            return DataType.Graph
        else:
            return None