from lane_detections.image_processing.helpers.calibration import get_undistorted_image
from lane_detections.image_processing.helpers.perspective_transform import first_person_to_birds_eye_view, \
    birds_eye_to_first_person_view
from lane_detections.image_processing.helpers.color_space import get_white_binary, get_yellow_binary
import matplotlib.pyplot as plt


class Image(object):
    @classmethod
    def from_image_path(cls, image_path):
        return cls.__init__(plt.imread(image_path))

    def __init__(self, raw_image, raw=True, birds_eye=False):
        self.birds_eye = None
        self.fpv = None

        if birds_eye:
            self.birds_eye = raw_image
            self.fpv = birds_eye_to_first_person_view(self.birds_eye)
        else:
            if raw:
                self.fpv = get_undistorted_image(raw_image)
                self.birds_eye = first_person_to_birds_eye_view(self.fpv)

    def get_image(self, birds_eye=False):
        return self.birds_eye if birds_eye else self.fpv

    def plot_image(self, birds_eye=False):
        plt.imshow(self.get_image(birds_eye=birds_eye))
        plt.show()

    def get_white_binary(self, birds_eye=False):
        return get_white_binary(self.get_image(birds_eye=birds_eye))

    def get_yellow_binary(self, birds_eye=False):
        return get_yellow_binary(self.get_image(birds_eye=birds_eye))
