from time import sleep
from os import getenv
from playsound import playsound


def follow(file):
    file.seek(0, 2)
    while True:
        line_ = file.readline()
        if not line_:
            sleep(0.1)
            continue
        yield line_


if __name__ == "__main__":
    try:
        logfile = open(getenv("APPDATA")+"/.minecraft/logs/latest.log", "r")
        log_lines = follow(logfile)
        for line in log_lines:
            if '[CHAT]' in line:
                newline = line.split('[CHAT]')[1]
                if '[СПм]' in newline:
                    message_time = line.split('[')[1].split(']')[0]
                    print(f"{message_time}{newline}")
                    if 'детектив' in newline.lower():
                        playsound("notify.mp3")
    except Exception as e:
        print(e)
        sleep(5)
