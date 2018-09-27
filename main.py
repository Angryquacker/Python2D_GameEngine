from VectorController import Vector2D
from DrawMap import Draw
import threading

man1 = Vector2D([1, 2])
man2 = Vector2D([3, 4])

field = Draw()

def setUpdateInterval(obj, time):
        e = threading.Event()
        while not e.wait(time):
            obj.update()

#setUpdateInterval(field, 0.5)
