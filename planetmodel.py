from math import sin, cos, pi


class Planet:
    """ Creating a math model of a planet, return a list of points, in which
    should be a planet circle draw in every each tick of time.
    the closer planets has smaller amount of points(theirs round cycle
    is smaller) that planets, which are more far away from the "sun"

    """

    def __init__(self, center_x, center_y, orbit_radius, resolution, orbit_direction):
        """center_x, center_y -- center of a sun
        radius -- planet orbit radius
        resolution -- amount of points in which planet will be draw
        """
        self.center_x = center_x
        self.center_y = center_y
        self.orbit_radius = orbit_radius
        self.resolution = resolution
        self.points = []
        self.orbit_direction = orbit_direction
        self.calculate_points()

    def choose_direction(self):
        if self.orbit_direction == "forward":
            return 0, self.resolution, 1
        else:
            return self.resolution - 1, -1, -1

    def calculate_points(self):
        start, stop, step = self.choose_direction()
        for i in range(start, stop, step):
            ang = 2*pi*i / self.resolution
            pos_x = cos(ang)*self.orbit_radius + self.center_y
            pos_y = sin(ang)*self.orbit_radius + self.center_x
            self.points.append((pos_x, pos_y))
