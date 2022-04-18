import datetime, sys, os, time


def check_time(get) -> bool:
    while 1:
        time_all = datetime.datetime.now().time()
        minute = time_all.minute
        if minute < 10:
            minute = f"0{minute}"

        if f"{time_all.hour}:{minute}" == get[0]:
            return True
        print(minute)
        time.sleep(60)


def start():
    get = sys.argv[1:]
    print(get)
    if check_time(get):
        os.system("python3 main.py")

if __name__ == "__main__":
    start()