import numpy as np
import cv2


def get_edges(image, threshold=100):
    sobel = cv2.Sobel(image, cv2.CV_64F, 1, 0)
    scaled_sobel = np.uint8(255 * sobel / np.max(sobel))

    thresh_min = 50
    thresh_max = 100
    sxbinary = np.zeros_like(scaled_sobel)
    sxbinary[(scaled_sobel >= thresh_min) & (scaled_sobel <= thresh_max)] = 1
    return sxbinary

