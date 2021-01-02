# Class for storing the meta information about the RawData
# Use this for storing all the extra information 

class DataMeta:
    def __init__(self) -> None:
        self.num_obs = None
        self.num_features = None
        self.size = None

        self.default_target = None

        self.features_names = None
        self.target_names = None

        self.target_type = None
