import numpy as np
import cv2
from lane_detections.image_processing.perspective_transform import M_INV
import matplotlib.pyplot as plt


def overly_lanes(undist, ploty, left_fitx, right_fitx, avg_curverad, offset):
    # Create an image to draw the lines on
    warp_zero = np.zeros_like(undist[:, :, 0]).astype(np.uint8)
    color_warp = np.dstack((warp_zero, warp_zero, warp_zero))

    # Recast the x and y points into usable format for cv2.fillPoly()
    pts_left = np.array([np.transpose(np.vstack([left_fitx, ploty]))])
    pts_right = np.array([np.flipud(np.transpose(np.vstack([right_fitx, ploty])))])
    pts = np.hstack((pts_left, pts_right))

    # Draw the lane onto the warped blank image
    cv2.fillPoly(color_warp, np.int_([pts]), (0, 255, 0))

    # Warp the blank back to original image space using inverse perspective matrix (Minv)
    newwarp = cv2.warpPerspective(color_warp, M_INV, (undist.shape[1], undist.shape[0]))
    # Combine the result with the original image
    result = cv2.addWeighted(undist, 1, newwarp, 0.3, 0)

    cv2.putText(result, 'Radius of Curvature = ' + str(round((avg_curverad / 1000), 2)) + 'km', (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
    cv2.putText(result, 'Vehicle Offset from Center = ' + str(round(offset, 2)) + 'm', (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
    return result
