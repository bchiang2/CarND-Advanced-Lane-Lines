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


def over_lay_binary_to_rgb(rgb, binary):
    warp_zero = np.zeros_like(binary)
    color_warp = np.dstack((warp_zero, np.dot(binary, 255), warp_zero))
    return cv2.addWeighted(
        src1=rgb,
        alpha=1,
        src2=color_warp.astype(np.uint8),
        beta=0.5,
        gamma=0,
        dtype=8
    )
