import pandas as pd
import numpy as np


def cut_behavior():
    array = [1,2,3,4,5,6]
    seq_scalars = pd.cut(x=array, bins=[1,4,6], include_lowest=True)
    single_int = pd.cut(x=array, bins=2, include_lowest=True)
    return seq_scalars, single_int

def test_cut_behavior():
