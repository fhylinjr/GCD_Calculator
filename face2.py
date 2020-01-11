from graphics import *
def main():
    win=GraphWin('Angry Face',500,500)
    head=Circle(Point(win.getWidth()/2,win.getHeight()/2),100)
    head.draw(win)
    leftEye=Circle(Point(210,210),15)
    leftEye.draw(win)
    rightEye=leftEye.clone()
    rghtEye.move(80,0)
    rightEye.draw(win)
    mouth=Line(Point(230,300),Point(270,300))
    mouth.draw(win)
    nose=Polygon(Point(250,240),Point(240,260),Point(260,260))
    nose.draw(win)

main()
