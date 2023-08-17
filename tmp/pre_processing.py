# -*- coding: utf-8 -*-
import re
import pandas as pd

def remove_HTML(raw):
    CLEANER = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleanText = re.sub(CLEANER, '', raw)
    return cleanText.strip()

def remove_new_line(raw):
    cleanText = re.sub(r"[\r\n\t]+", ' ', raw)
    return cleanText.strip()

# Remove empty description
def remove_empty(column_name: str, df: pd.DataFrame) -> pd.DataFrame:
    indices = []
    for index, row in df.iterrows():
        if row[column_name] == '':
            indices.append(index)
    df = df.drop(df.index[indices])
    df.reset_index(drop=True, inplace=True)
    return df
