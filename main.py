import numpy as np
import pandas as pd
import time
import os
import random

if __name__ == "__main__":
    print('check env vars:')
    input_file = os.getenv('INPUT_FILE')
    input_folder = os.getenv('INPUT_FOLDER')
    output_file = os.getenv('OUTPUT_FILE')
    output_folder = os.getenv('OUTPUT_FOLDER')

    print(f'''
    input file = {input_file}
    output file = {output_file}
    input folder = {input_folder}
    output folder = {output_folder}
    ''')

    df = pd.read_csv(input_file)
    print('show part of input file data')
    print(df.head())

    df['preditions'] = np.random.randint(1, 6, df.shape[0])
    df.to_csv(output_file)

    print('check output file whether data write successfully')

    df_out = pd.read_csv(output_file)
    print('show part of ouptput file data')
    print(df_out.head())

    time.sleep(5)
