import time
import os
import pandas as pd

if __name__ == "__main__":

    cnt = 0
    total = 100
    while cnt <= total:
        time.sleep(0.25)
        print('check env DATASET_INPUT = ')
        print(os.getenv('DATASET_INPUT'))
        print('check env DATASET_OUTPUT = ')
        print(os.getenv('DATASET_OUTPUT'))

        print('list file in dataset path')
        files = os.listdir('/shared/dataset/')
        print(files)

        df = pd.read_json(os.getenv('DATASET_INPUT'))
        print(df)
        print(f'current cnt = {cnt}, {total-cnt} to go')
        cnt += 1

    print('count finished')
