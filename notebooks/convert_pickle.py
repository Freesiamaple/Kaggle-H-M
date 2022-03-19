import pandas as pd
import numpy as np

DIR = "H_M/data/original/"


def convert_csv_to_pkl(filename):
    df = pd.read_csv(f'{DIR}{filename}.csv')
    df.to_pickle(f'{DIR}{filename}.pkl')

#convert_csv_to_pkl("articles")
#convert_csv_to_pkl("customers")
#convert_csv_to_pkl("sample_submission")
#convert_csv_to_pkl("transactions_train")
convert_csv_to_pkl("color_kusunoki")