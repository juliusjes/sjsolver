import re
import os
import pandas as pd


DIR = os.path.dirname(os.path.realpath(__file__))

def contains_number(value):
    """ Check if the given value is a string and contains any digit. """
    if isinstance(value, str):
        return bool(re.search(r'\d', value))
    return False

def get_words(file="nykysuomensanalista2024.csv") -> pd.DataFrame:
    '''
    Read the words file and filter.

    Arguments:
        file (str): file to read from.

    Returns:
        data (pd.DataFrame): the resulting list of words.
    '''
    file = DIR + "/" + file
    print(f"Using words from {file}")
    data = pd.read_csv(file, header=0, sep="\t")
    data = preprocess(data)
    return data

def preprocess(data):
    '''
    Filter to all valid words.

    Arguments:
        data (pd.DataFrame): unfiltered list of words.

    Returns:
        data (pd.DataFrame): filtered data.
    '''
    allowed_classes = ["substantiivi", "verbi", "adjektiivi", "pronomini", "konjunktio"]

    if 'Sanaluokka' in data.columns:
        data = data[data["Sanaluokka"].isin(allowed_classes)]
    else:
        print("Column 'Sanaluokka' not found in the DataFrame.")
        return pd.DataFrame() 

    if 'Hakusana' not in data.columns:
        print("Column 'Hakusana' not found in the DataFrame.")
        return pd.DataFrame()

    data = data[data["Hakusana"].str.strip().ne("")]

    mask = data["Hakusana"].apply(contains_number)

    data = data[~mask]
    
    data = data["Hakusana"]
    
    data.reset_index()

    return data 