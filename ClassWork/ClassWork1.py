import os
from datetime import datetime, timedelta


def get_files(temp):
    os.makedirs(temp, exist_ok=True)
    now_time = datetime.now()

    for i in range(10):
        name = now_time.strftime('%Y-%m-%d-%H-%M-%S.log')
        with open(os.path.join(temp, name), 'w') as f:
            if now_time.second % 2 == 0:
                f.write('Status: Fail')
            else:
                f.write('Status: Pass')

        now_time += timedelta(seconds=1)


def main():
    temp = 'tests'
    get_files(temp)


if __name__ == '__main__':
    main()
