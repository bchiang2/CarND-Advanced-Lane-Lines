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


def over_lay_image_to_rgb(rgb, image, alpha=1, beta=1, weights=(200, 0, 0)):
    if len(image.shape) == 2:
        src2 = np.dstack((np.dot(image, weights[0]), np.dot(image, weights[1]), np.dot(image, weights[2])))
    else:
        src2 = image
    return cv2.addWeighted(
        src1=rgb,
        alpha=alpha,
        src2=src2,
        beta=beta,
        gamma=0,
        dtype=8
    )
