import time

if __name__ == "__main__":
    cnt = 0
    total = 100
    while cnt <= total:
        time.sleep(0.25)

        print(f'current cnt = {cnt}, {total-cnt} to go')
        cnt += 1

    print('count finished')
