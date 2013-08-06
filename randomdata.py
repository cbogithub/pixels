import redis
import random
import time
import cPickle

from pixelpusher import pixel, build_strip, send_strip

MAX = 32
MID = 128
OFF = 0

FRAME_KEY = 'frame'

def rand_pixel():
    return pixel(
        random.randint(-MAX, MAX),
        random.randint(-MAX, MAX),
        random.randint(-MAX, MAX))

def rand_frame():
    return [rand_pixel() for i in range(120 * 8)]

def main():
    client = redis.Redis()

    while True:
        time.sleep(0.1)
        frame = rand_frame()
        client.rpush(FRAME_KEY, cPickle.dumps(frame))

if __name__ == "__main__":
    main()
