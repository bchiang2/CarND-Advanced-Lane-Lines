**Advanced Lane Finding Project**

The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

[//]: # (Image References)

[image1a]: ./my_examples/calibration_sample.png "Undistorted"
[image1b]: ./my_examples/calibration_result.png "Undistorted"
[image2]: ./my_examples/undist.png "Road Transformed"
[image3]: ./my_examples/edges.png "Binary Example"
[image4]: ./my_examples/topdown.png "Warp Example"
[image5]: ./examples/color_fit_lines.jpg "Fit Visual"
[image6]: ./my_examples/demo.png "Output"
[video1]: ./project_video_out.mp4 "Video"

## [Rubric](https://review.udacity.com/#!/rubrics/571/view) Points

### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---

### Writeup / README

#### 1. Provide a Writeup / README that includes all the rubric points and how you addressed each one.  You can submit your writeup as markdown or pdf.  [Here](https://github.com/udacity/CarND-Advanced-Lane-Lines/blob/master/writeup_template.md) is a template writeup for this project you can use as a guide and a starting point.  

You're reading it!

### Camera Calibration

#### 1. Briefly state how you computed the camera matrix and distortion coefficients. Provide an example of a distortion corrected calibration image.

The code for this step is contained in the first code cell of the IPython notebook located in 
`lane_detections/image_processing/utils/calibration.py`

I start by preparing "object points", which will be the (x, y, z) coordinates of the chessboard corners in the world. 
Here I am assuming the chessboard is fixed on the (x, y) plane at z=0, such that the object points are the same for each calibration image.  
Thus, `objp` is just a replicated array of coordinates, and `objpoints` will be appended with a copy of it every time I successfully detect all chessboard corners in a test image.  `imgpoints` will be appended with the (x, y) pixel position of each of the corners in the image plane with each successful chessboard detection.  

I then used the output `objpoints` and `imgpoints` to compute the camera calibration and distortion coefficients using the `cv2.calibrateCamera` function.  
I applied this distortion correction to the test image using the `cv2.undistort` function and obtained this result: 

![alt text][image1a]
![alt text][image1b]

### Pipeline (single images)

#### 1. Provide an example of a distortion-corrected image.

To demonstrate this step, I will describe how I apply the distortion correction to one of the test images like this one:
![alt text][image2]

#### 2. Describe how (and identify where in your code) you used color transforms, gradients or other methods to create a thresholded binary image.  Provide an example of a binary image result.

I used of color thresholds to generate a binary image.
The code can be found in `lane_detections/image_processing/utils/color_space.py` 

Here's an example of my output for this step. 

![alt text][image3]

#### 3. Describe how (and identify where in your code) you performed a perspective transform and provide an example of a transformed image.

The code for my perspective transform includes a function called `first_person_to_birds_eye_view`, which appears in `lane_detections/image_processing/utils/perspective_transform.py`

This resulted in the following source and destination points:

| Source        | Destination   | 
|:-------------:|:-------------:| 
| 265, 690      | 315, 690        | 
| 1050, 690      | 900, 690      |
| 555, 480     | 315, 480      |
| 730, 480      | 900, 480        |

I verified that my perspective transform was working as expected by drawing the `src` and `dst` points onto a test image and its warped counterpart to verify that the lines appear parallel in the warped image.

![alt text][image2]
![alt text][image4]

#### 4. Describe how (and identify where in your code) you identified lane-line pixels and fit their positions with a polynomial?

I fitted my lane lines with a 2nd order polynomial kinda like this:

![alt text][image5]

Using the code provided in the lecture, the implementation can be found in `fit_lines.py` 

#### 5. Describe how (and identify where in your code) you calculated the radius of curvature of the lane and the position of the vehicle with respect to center.

I did this in the `curvature` and `offset` methods in `LanePolynomial` class located in `lanes_polynomial.py`

The curvature is extracted from the polynomial fit, and the offset is extracted from the camera position and the lane positioning.

#### 6. Provide an example image of your result plotted back down onto the road such that the lane area is identified clearly.

I implemented this step in `main.py` in the method `process_image`.  

Here is an example of my result on a test image:

![alt text][image6]

---

### Pipeline (video)

#### 1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (wobbly lines are ok but no catastrophic failures that would cause the car to drive off the road!).

Here's a [link to my video result](./project_video_out.mp4)

---

### Discussion

#### 1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

The main problem I faced with reliably detecting the lane in the video without jitter.
To solve this by trying out different color space to get the best lane marking detection.

If the width between two lane are different significantly. i.e. at least on of the lane is incorrect. I will reuse the last good detection.

This resolve the jitter issue a little bit, but there are still a lot of room for improvement.
Here are two low hanging fruit that I think can improve the results

1. Better use of color space to extract lane. Use both HSV and HLS. 
2. Better smoothing, i.e. averaging across multiple frame. 
