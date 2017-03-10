import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r}, {!r})'.format(
            self.x,
            self.y
        )
    def __eq__(self, other_entry):
        """

        :param other_entry:
        :return:
        >>> (5, -1) == (0, -1)
        False
        >>> (5, 5) == (5, 5)
        True
        """
        return(
            self.x == other_entry.x and
            self.y == other_entry.y
        )

    def find_distance_between_pts(self, point_b_x, point_b_y):
        """

        :param point_a:
        :param point_b:
        :return:
         >>> Point(5, 5).find_distance_between_pts(7, 7)
         2.8284271247461903
        """
        distance = math.sqrt((self.x - point_b_x)**2 + (self.y - point_b_y)**2)
        return distance

    def move_point(self, distance, angle):


