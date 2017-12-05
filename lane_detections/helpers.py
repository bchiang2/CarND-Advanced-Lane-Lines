import matplotlib.pyplot as plt
import numpy as np
import cv2
import copy
def plot_images(images):
    image_count = len(images)
    fig = plt.figure()
    for i, image in enumerate(images):
        tmp = fig.add_subplot(1, image_count, i+1)
        tmp.imshow(image)
    return fig


def plot_image(image):
    plt.imshow(image)
    plt.show()

def fill_color(rgb, binary):
    new_rgb = copy.deepcopy(rgb)
    for y in range(len(rgb)):
        for x in range(len(rgb[0])):
            if binary[y][x] == 1:
                new_rgb[y][x] = (255, 0, 0)
    return new_rgb

def over_lay_binary_to_rgb(binary, rgb):
    return fill_color(rgb,binary)
