import numpy as np
import cv2
import matplotlib.pyplot as plt


def find_histogram_peak(line):
    histogram = np.sum(line, axis=0)
    midpoint = np.int(histogram.shape[0] / 2)
    leftx_base = np.argmax(histogram[:midpoint])
    rightx_base = np.argmax(histogram[midpoint:]) + midpoint
    return leftx_base, rightx_base


def filter(image):
    for row in image:
        return find_histogram_peak()
