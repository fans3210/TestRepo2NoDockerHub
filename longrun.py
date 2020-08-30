import time
import os
import pandas as pd

if __name__ == "__main__":

    print('test env datasetinput = ')
    print(os.getenv('DATASET_INPUT'))

    print('test list file')
    files = os.listdir('/shared/dataset/')
    print(files)

    df = pd.read_json(os.getenv('DATASET_INPUT'))
    print(df)

    cnt = 0
    total = 100
    while cnt <= total:
        time.sleep(0.25)

        print(f'current cnt = {cnt}, {total-cnt} to go')
        cnt += 1

    print('count finished')
