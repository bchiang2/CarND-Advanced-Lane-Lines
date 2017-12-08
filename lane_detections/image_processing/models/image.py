from lane_detections.image_processing.utils.calibration import get_undistorted_image
from lane_detections.image_processing.utils.perspective_transform import first_person_to_birds_eye_view, \
    birds_eye_to_first_person_view
from lane_detections.image_processing.utils.color_space import get_lane_color
from lane_detections.image_processing.utils.edge_detection import get_edges
import matplotlib.pyplot as plt

class CameraView(object):
    def __init__(self, image):
        self.image = image

    def front(self):
        return birds_eye_to_first_person_view(self.image)

    def birds_eye(self):
        return first_person_to_birds_eye_view(self.image)

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

    def get_lane_binary(self, birds_eye=False):
        return get_lane_color(self.get_image(birds_eye=birds_eye))

    def get_edges(self, birds_eye=False):
        return get_edges(self.get_image(birds_eye=birds_eye))
