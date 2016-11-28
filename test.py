#!/usr/bin/env python3

import time
import motion_detector


if __name__ == "__main__":
    while True:
        if motion_detector.motion_detect():
            print("Somebody is closing")
        else:
            print("Nobody")
        time.sleep(1)
