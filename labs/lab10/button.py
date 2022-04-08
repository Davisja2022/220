from graphics import *

class Button:
    shape = Rectangle(Point(450,50), Point(450,125))
    text = Text(shape.getCenter(), "Exit")

    def __init__(self, shape, label):
        self.shape = shape
        self.label = label

    def get_label(self):
        return self.label

    def set_label(self, label):
        new_label = label
        self.label = new_label

    def draw(self,win):
        self.shape.draw(win)
        self.text.setText(self.label)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self,point):
        corner1, corner2 = self.shape.getP1(), self.shape.getP2()
        if point.getX() >= corner1.getX() and point.getX() <= corner2.getX() and point.getY() >= corner1.getY() and point.getY() <= corner2.getY():
            return True
        else:
            return False


    def color_button(self,color):
        self.shape.setFill(color)