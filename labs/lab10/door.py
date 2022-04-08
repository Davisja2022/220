from graphics import *
class Door:
    shape = Rectangle(Point(120, 185), Point(530, 585))
    text = Text(shape.getCenter(), "Exit")
    secret = False

    def __init__(self, shape, label):
        self.shape = shape



    def get_label(self):
        return self.label

    def set_label(self, label):
        new_label = label
        self.label = new_label

    def draw(self, win):
        self.shape.draw(win)


    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        corner1, corner2 = self.shape.getP1(), self.shape.getP2()
        if point.getX() >= corner1.getX() and point.getX() <= corner2.getX() and point.getY() >= corner1.getY() and point.getY() <= corner2.getY():
            return True
        else:
            return False

    def open(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def close(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def color_door(self, color,):
        self.shape.setFill(color)

    def is_secret(self):
        if self.secret == False:
            return False
        else:
            return True

    def set_secret(self, secret):
        self.secret = secret


