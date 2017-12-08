import numpy as np

ym_per_pix = 30 / 720  # meters per pixel in y dimension
xm_per_pix = 3.7 / 700  # meters per pixel in x dimension

IMAGE_WIDTH = 1280


class LanePolynomial(object):
    def __init__(self, ploty, leftx, rightx):
        self.ploty = ploty
        self.leftx = leftx
        self.rightx = rightx

    def curvature(self):
        # Define conversions in x and y from pixels space to meters

        y_eval = np.max(self.ploty)
        # Fit new polynomials to x,y in world space
        left_fit_cr = np.polyfit(self.ploty * ym_per_pix, self.leftx * xm_per_pix, 2)
        right_fit_cr = np.polyfit(self.ploty * ym_per_pix, self.rightx * xm_per_pix, 2)
        # Calculate the new radii of curvature
        left_curverad = ((1 + (2 * left_fit_cr[0] * y_eval * ym_per_pix + left_fit_cr[1]) ** 2) ** 1.5) / np.absolute(
            2 * left_fit_cr[0])
        right_curverad = ((1 + (
                2 * right_fit_cr[0] * y_eval * ym_per_pix + right_fit_cr[1]) ** 2) ** 1.5) / np.absolute(
            2 * right_fit_cr[0])

        # Now our radius of curvature is in meters
        avg_curverad = (left_curverad + right_curverad) / 2.0

        return round((avg_curverad / 1000), 2)

    def offset(self):
        vehicle_x = self.leftx[-1] + (self.rightx[-1] - self.leftx[-1]) / 2.0
        return (IMAGE_WIDTH / 2.0 - vehicle_x) * xm_per_pix

    def get_texts(self):
        return [
            'Radius of Curvature: {} km'.format(round(self.curvature(),2)),
            'Vehicle Offset from Center: {} m'.format(round(self.offset(),2))
        ]
