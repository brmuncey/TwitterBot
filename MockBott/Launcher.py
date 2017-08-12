import time

from MockBott.Bot import Bot

print("Program Launch")


def launch():
    Bot()

    start = time.time()
    while True:
        current = time.time()
        if current - start > 60 * 20:
            break

    launch()


launch()
