#!/usr/bin/env python3

__author__ = "Matej"
__version__ = "0.1.0"
__license__ = "MIT"
__status__ = "Prototype"

from yeelight import *
import datetime

BULB_IP = "192.168.1.100"
TRANSITION_DURATION = 1000
SCHEDULE = [
    {"color": "0,255,0", "day": 4},
    {"color": "0,0,255", "day": 5}
]  # monday is 0, sunday is 6
REPEAT_TIMES = 6  # number of times to repeat the notification pulse

bulb = None


def main():
    print("Starting trashlight!")

    global bulb
    bulb = Bulb(BULB_IP)

    current_day = datetime.datetime.today().weekday()  # get index of today

    for elem in SCHEDULE:  # go over our schedule
        if elem["day"] == current_day:  # check if today is in our schedule
            notify_me(elem["color"])


def notify_me(color):
    rgb = color.split(",")
    rgb = [int(x) for x in rgb]  # cast elements to integers

    transitions = [
        RGBTransition(rgb[0], rgb[1], rgb[2], duration=TRANSITION_DURATION),
        SleepTransition(duration=TRANSITION_DURATION),
        RGBTransition(255, 255, 255, duration=TRANSITION_DURATION)
    ]

    flow = Flow(
        count=REPEAT_TIMES,
        transitions=transitions
    )

    bulb.start_flow(flow)
    bulb.turn_on()


if __name__ == "__main__":
    main()
