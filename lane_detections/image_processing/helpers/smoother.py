import numpy as np
queue = []

class LastMeasurment(object):
    def __init__(self, data):
        self.data = data
        self.count = 0

    def get_last_measurment(self):
        self.count += 1
        print("Using last measurment")
        return self.data

    def update_measurment(self,data):
        self.count = 0
        self.data = data

last_measurment = LastMeasurment(None)

def smooth(ploty, leftx_base, rightx_base, left_curverad, right_curverad, offset):
    print(left_curverad, right_curverad)
    print(offset)
    line_width = rightx_base - leftx_base
    medium_width = np.median(line_width)
    anomaly_count = (len([w for w in np.subtract(line_width, medium_width) if w>150]))

    if anomaly_count > 100 and last_measurment.data:
        return last_measurment.get_last_measurment()
    else:
        last_measurment.update_measurment((ploty, leftx_base, rightx_base, left_curverad, right_curverad, offset))
        return ploty, leftx_base, rightx_base, left_curverad, right_curverad, offset