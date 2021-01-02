from .data import Data

class ImageData(Data):
    def __init__(self, config) -> None:
        super().__init__(config)

    def load_data(self, data=None, data_config=None):
        self.create_train_test()
    
    def create_train_test(self):
        pass