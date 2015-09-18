#TODO
#Draw Graphs, and training dataset initialization
from Perceptron import *;
from graphics import *

p = Perceptron(inputLength = 2, learningConstant = 0.01);
training = [];

def fLine(x):
    return -0.5*x + 2;

def setup():
    for i in range(0, 2000):
        x = rand.uniform(-5, 5);
        y = rand.uniform(-3, 3);
        ans = 1;
        if (y < fLine(x)):
            ans = -1;
        training.append(Trainer(x, y, ans));
        print("Trainer " + str(i + 1) + " :[x = " + str(x) + ", y = " + str(y) + ", ans = " + str(ans) + "]");

def drawGraph():
    win = GraphWin("Perceptron", 1000, 600);

    xAxis = Line(Point(0, 300), Point(1000, 300));
    yAxis = Line(Point(500, 0), Point(500, 600));
    xAxis.setWidth(2);
    yAxis.setWidth(2);
    xAxis.draw(win);
    yAxis.draw(win);

    targetLine = Line(Point(300, 0), Point(1000, 350));
    targetLine.setWidth(2);
    targetLine.setFill('green');
    targetLine.draw(win);

    for t in training:
        pointT = Point(t.inputs[0]*100 + 500,-t.inputs[1]*100 + 300);
        if t.ans == 1:
            pointT.setFill("red");
        else:
            pointT.setFill("blue");
        pointT.draw(win);


if __name__ == '__main__':
    print(p.weights);
    setup();
    drawGraph();
    k = raw_input("press close to exit");
