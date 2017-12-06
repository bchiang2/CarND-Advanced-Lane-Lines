import matplotlib.pyplot as plt
import numpy as np
import cv2
import copy


def plot_images(images):
    image_count = len(images)
    fig = plt.figure()
    for i, image in enumerate(images):
        tmp = fig.add_subplot(1, image_count, i + 1)
        tmp.imshow(image)
    return fig


def plot_image(image):
    plt.imshow(image)
    plt.show()


def over_lay_binary_to_rgb(rgb, binary, alpha=1, beta=1, weights=(200, 0, 0)):
    src2 = np.dstack((np.dot(binary, weights[0]), np.dot(binary, weights[1]), np.dot(binary, weights[2])))
    return cv2.addWeighted(
        src1=rgb,
        alpha=alpha,
        src2=src2,
        beta=beta,
        gamma=0,
        dtype=8
    )
