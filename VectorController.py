class Vector2D:
    def __init__(self, vect = [0, 0]):
        self.vect = vect
    
    def __add__(self, vector2):
        tempX = self.vect[0] + vector2.vect[0]
        tempY = self.vect[1] + vector2.vect[1]
        return [tempX, tempY]
