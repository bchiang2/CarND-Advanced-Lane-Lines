import cv2
import numpy as np
import matplotlib.pyplot as plt

# prepare object points
nx = 9
ny = 6


# def get_object_points(img):

# Make a list of calibration images
img = cv2.imread('../camera_cal/calibration2.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



objpoints = np.zeros((nx*ny,3), np.float32)
objpoints[:,:2] = np.mgrid[0:nx,0:ny].T.reshape(-1,2)

imgpoints = []


# Find the chessboard corners
ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)
# If found, draw corners
if ret == True:
    # Draw and display the corners
    cv2.drawChessboardCorners(img, (nx, ny), corners, ret)
    plt.imshow(img)
    plt.show()
    imgpoints.append(corners)
    objpoints.append(objpoints)

# ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
