from pygame import draw


class Planet:
    """Drawing a planet moving around "sun"

    """

    def __init__(self, radius, color, surface, points, current_point_index=0):
        """radius -- radius of a planet
        points -- points from planetmodel module which are simulating planet
        movement

        """
        self.radius = radius
        self.color = color
        self.surface = surface
        self.points = points
        self.current_point_index = current_point_index

    def draw(self):
        """drawing next planet position

        """
        print("radius", self.radius, "len(self.points)", len(self.points))
        if self.current_point_index == len(self.points) - 1:
            self.current_point_index = 0
        else:
            self.current_point_index += 1
        draw.circle(self.surface, self.color,
                    self.points[self.current_point_index], self.radius)
        
