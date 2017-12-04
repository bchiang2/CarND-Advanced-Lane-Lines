import numpy as np
import cv2


def get_satruated_pixels(image):
    hls = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)
    S = hls[:, :, 2]
    thresh = (90, 255)
    binary = np.zeros_like(S)
    binary[(S > thresh[0]) & (S <= thresh[1])] = 1
    return binary

def get_satruated_pixels(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    H = hsv[:, :, 0]
    thresh = (10,100)
    binary = np.zeros_like(H)
    binary[(H > thresh[0]) & (H <= thresh[1])] = 1
    return binary

def get_white_line(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    V = hsv[:, :, 2]
    thresh = (220,255)
    binary = np.zeros_like(V)
    binary[(V > thresh[0]) & (V <= thresh[1])] = 1
    return binary