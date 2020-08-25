import time
import os

if __name__ == "__main__":

    print('test list file')
    files = os.listdir('/dataset')
    print(files)

    print('test env datasetinput = ')
    print(os.getenv('DATASET_INPUT'))

    cnt = 0
    total = 1000
    while cnt <= total:
        time.sleep(0.25)

        print(f'current cnt = {cnt}, {total-cnt} to go')
        cnt += 1

    print('count finished')
