import numpy as np
import cv2


def get_lane_color(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    H, S, V = [hsv[:, :, i] for i in range(3)]
    binary = np.zeros_like(V)
    # White & Yellow
    binary[((V > 200) & (S <= 30)) | ((H > 80) & (H < 105) & (S > 70))] = 1
    return binary
