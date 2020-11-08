#!/usr/bin/env python3
MAX_SPEED = 256

import sys


def how_long(size, speed=MAX_SPEED):
    time = ((float(size) * 1048576) / float(speed)) / 60
    hour = int(time // 60)
    minute = int(time % 60)
    minute = round(minute)
    if time > 1440:
        day = hour // 24
        hour %= 24
        print(f"При скорости {speed}, файл размером {size} гигов будет качаться {day} день {hour}:{minute}")
    elif time > 60:
        print(f"При скорости {speed}, файл размером {size} гигов будет качаться {hour}:{minute}")
    else:
        print(f"При скорости {speed}, файл размером {size} гигов будет качаться {minute} минут")


def main():
    how_long(*sys.argv[1:])


if __name__ == '__main__':
    main()
