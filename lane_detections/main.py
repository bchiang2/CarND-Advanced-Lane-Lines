import glob
import cv2
import matplotlib.pyplot as plt
from moviepy.editor import VideoFileClip
import helpers
from lane_detections.image_processing.models.Image import Image


def test():
    for image_path in glob.glob('../test_images/test*.jpg'):
        image = plt.imread(image_path)

def play_video():
    cap = cv2.VideoCapture('../project_video.mp4')
    while (cap.isOpened()):
        ret, frame = cap.read()
        img = Image(raw_image=frame)
        new_image = helpers.over_lay_binary_to_rgb(binary=img.get_yellow_binary(birds_eye=True), rgb=img.get_image(birds_eye=True))
        cv2.imshow('frame', new_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    white_output = '../project_video_out1.mp4'
    clip2 = VideoFileClip('../project_video.mp4')
    # yellow_clip = clip2.fl_image(apply_lane_overlay)
    # yellow_clip.write_videofile(white_output, audio=False)


if __name__ == "__main__":
    play_video()
