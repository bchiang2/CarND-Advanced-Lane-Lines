import glob
import matplotlib.pyplot as plt
from image_processing.calibration import get_undistorted_image
from image_processing.perspective_transform import get_top_down_view
from image_processing.edge_detection import get_edges
from image_processing.color_space import get_white_line
from image_processing.line_filter import get_sliding_windows, get_curvature, get_offset
from image_processing.overlay import overly_lanes
from smoother import smooth
from moviepy.editor import VideoFileClip
from helpers import plot_images


def get_rgb_top_down(image):
    return get_top_down_view(image=image)


def get_line_edges(image):
    binary_white_line = get_white_line(image=image)
    return get_edges(binary_white_line)


def detect_lanes(edges):
    ploty, leftx, rightx = get_sliding_windows(binary_warped=edges)
    left_curverad, right_curverad = get_curvature(ploty=ploty, leftx=leftx, rightx=rightx)
    offset = get_offset(leftx=leftx[0], rightx=rightx[0], image_width=edges.shape[1])
    return ploty, leftx, rightx, left_curverad, right_curverad, offset


def apply_lane_overlay(image):
    undist = get_undistorted_image(image=image)
    top_down_view = get_rgb_top_down(image=undist)
    line_edges = get_line_edges(image=top_down_view)
    ploty, leftx_base, rightx_base, left_curverad, right_curverad, offset = detect_lanes(edges=line_edges)
    ploty, leftx_base, rightx_base, left_curverad, right_curverad, offset = smooth(ploty, leftx_base, rightx_base, left_curverad, right_curverad, offset)
    overlied = overly_lanes(
        undist=undist,
        ploty=ploty,
        left_fitx=leftx_base,
        right_fitx=rightx_base,
        avg_curverad=(left_curverad + right_curverad) / 2,
        offset=offset
    )
    return overlied



def test():
    for image_path in glob.glob('../test_images/test*.jpg'):
        image = plt.imread(image_path)
        plt.imshow(apply_lane_overlay(image))
        plt.show()


def main():
    white_output = '../challenge_video_out.mp4'
    clip2 = VideoFileClip('../challenge_video.mp4')
    yellow_clip = clip2.fl_image(apply_lane_overlay)
    yellow_clip.write_videofile(white_output, audio=False)


if __name__ == "__main__":
    main()
