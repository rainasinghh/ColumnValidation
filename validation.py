from typing import List
import pandas as pd
import yaml
import gzip
import os


def readYaml(filename):
    with open(filename) as f:
        try:
            return yaml.safe_load(f)
        except:
            print("ERROR: failed to load yaml")
            exit(1)

def writeAndZip(df, config):
    sep = config["write-delimiter"]
    out = config["output-path"]
    out_temp = out + '-temp'
    df.to_csv(out_temp, sep=sep)
    f_in = open(out_temp)
    content = f_in.read()
    f_out = gzip.open(out, 'wt')
    f_out.write(content)
    f_out.close()
    f_in.close()

    os.remove(out_temp)


def colVal(df: pd.DataFrame, col_list: List[str]):
    is_equal = list(df.columns) == col_list
    if is_equal:
        print(f"Dataframe matches column list: {col_list}")
    else:
        not_in_col_list = []
        missing_cols = []
        df_cols = list(df.columns) 
        for col in df_cols:
            if col not in col_list:
                not_in_col_list.append(col)
        print(f"The following dataframe columns were unexpected: {not_in_col_list}")
        print()

        for col in col_list:
            if col not in df_cols:
                missing_cols.append(col)
        print(f"The following expected columns are not in the dataframe: {missing_cols}")
    
    return is_equal