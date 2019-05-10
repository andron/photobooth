#!/usr/bin/env python

import imageio
import configparser
import pytumblr
import time
import uuid


import sys, termios, tty, os


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

button_delay = 0.2


def create_filename():
    return str(uuid.uuid4())


def create_gif(filenames):
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    out_filename = 'output/' + create_filename() + '.gif'
    imageio.mimsave(out_filename, images)
    return out_filename


def upload_photo(config, image_paths):
    # Authenticate via OAuth
    client = pytumblr.TumblrRestClient(
        config["Keys"]["consumer_key"],
        config["Keys"]["consumer_secret"],
        config["Keys"]["token_key"],
        config["Keys"]["token_secret"]
    )

    # Make the request
    # print(client.info())

    client.create_photo(
        config["Photobooth"]["blog"],
        state="published",
        tags=["party", "on"],
        data=image_path)


def take_pictures(num_images):
    return []


def print_stage(freq, totaltime):
    for i in range(freq*totaltime):
        print("#")
        time.sleep(1.0/freq)


def do_countdown():
    # 3 2 1...
    print_stage(2, 1)
    print_stage(4, 1)
    print_stage(8, 1)


def poll_gpio(config):
    not_quit = True
    while not_quit:
        if False:
            # turn off if key is pressed?
            not_quit = False
            break
        if True:
            char = getch()
            if char == "q":
                return
            if char != "a":
                continue
            # Check if gpio-pin is set
            do_countdown()
            num_images = 3
            print("IMAGE")
            continue
            images = take_pictures(num_images)
            image = None
            if moving:
                image = create_gif(images)
                upload_photo(config, image)
            else:
                upload_photo(config, images[0])

        time.sleep(0.005)


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("photobooth.cfg")
    image_path = "chance.jpg"
    poll_gpio(config)
    upload_photo(config, image_path)