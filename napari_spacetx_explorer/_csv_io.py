import numpy as np
import pandas as pd


class CSVIO:
    """Read data from csv file

    Parameters
    ----------
    file_path : str
        Path to the csv file

    """
    def __init__(self, file_path):
        self.file_path = file_path

    def is_compatible(self):
        if self.file_path.endswith('.csv'):
            return True
        return False

    def read(self):
        df = pd.read_csv(self.file_path)
        df = df.fillna('None')
        #df_gene = df[df['target'] != np.nan]
        #self.data = np.column_stack([df_gene['yc'], df_gene['xc']])
        self.total_data = (np.column_stack([df['yc'], df['xc']]), df['target'])
