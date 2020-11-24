import numpy as np
import pandas as pd
import time
import os

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

    time.sleep(30)
