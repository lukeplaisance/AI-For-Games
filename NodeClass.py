#pylint: disable = E1101
#pylint: disable = C0330
from vector2 import Vector2

class Node(object):
    '''class that creates the nodes and its properties'''
    def __init__(self, pos):
        '''constructor'''
        self.position = pos
        self.parent = None
        self.h_score = 0
        self.g_score = 0
        self.f_score = 0
        self.is_traversable = True
        self.is_goal = False
        self.is_start = False

    def set_parent(self, other):
        '''sets the parent of a node to another'''
        self.parent = other
        return self.parent

    def calc_g(self, other):
        '''returns the G score of the node'''
        if self.parent is None:
            if ((self.position.x_position is other.position.x_position and
                self.position.y_position is not other.position.y_position)
            or (self.position.x_position is not other.position.x_position and
                self.position.y_position is other.position.y_position)):
                self.g_score = other.g_score + 10
            else:
                self.g_score = other.g_score + 14
        elif self.parent is not None:
            tent_g = self.g_score
            if ((self.position.x_position is other.position.x_position and
                self.position.y_position is not other.position.y_position)
            or (self.position.x_position is not other.position.x_position and
                self.position.y_position is other.position.y_position)):
                tent_g = other.g_score + 10
            else:
                tent_g = other.g_score + 14
            if tent_g < self.g_score:
                self.g_score = tent_g
                self.set_parent(other)

    def calc_h(self, other):
        '''returns the H score of the node'''
        x_distance = abs(other.position.x_position - self.position.x_position)
        y_distance = abs(other.position.y_position - self.position.y_position)
        total = x_distance + y_distance
        self.h_score = total * 10
        return self.h_score

    def calc_f(self):
        '''returns the F score of the node'''
        self.f_score = self.g_score + self.h_score
        return self.f_score

    def set_non_trav(self):
        '''sets a node to be non traversable'''
        self.is_traversable = False



