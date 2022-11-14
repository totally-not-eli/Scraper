import pandas as pd
class Helper:
    def __init__(self):
        pass

    def create_df(self,**kwargs):
        print(kwargs)
        return pd.DataFrame(kwargs)

    