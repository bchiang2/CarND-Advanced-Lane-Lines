import numpy as np
import cv2


def get_lane_color(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    H, S, V = [hsv[:, :, i] for i in range(3)]
    binary = np.zeros_like(V)
    # White & Yellow
    # binary[((V > 190) & (S <= 30)) & ((H > 80))] = 1
    # binary[((H > 70) & (H < 130) & (S > 70) & (V > 160))] = 1
    binary[((H > 70) & (H < 130) & (S > 70) & (V > 160)) | ((V > 220) & (S <= 30)) & ((H > 80))] = 1
    return binary
