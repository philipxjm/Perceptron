#TODO
#Draw Graphs, and training dataset initialization
from Perceptron import *;
from graphics import *;
from numpy import *;
import matplotlib.pyplot as plt

p = Perceptron(inputLength = 2, learningConstant = 0.01);
training = [];

def fLine(x):
    return 2*x + 5;

def setup():
    for i in range(0, 2000):
        x = rand.uniform(-50, 50);
        y = rand.uniform(-30, 30);
        ans = 1;
        if (y < fLine(x)):
            ans = -1;
        training[i] = Trainer(x, y, ans);

def drawGraph():
    win = GraphWin("Perceptron", 1000, 600);

    xAxis = Line(Point(0, 300), Point(1000, 300));
    yAxis = Line(Point(500, 0), Point(500, 600));
    xAxis.draw(win);
    yAxis.draw(win);

print(p.weights);
drawGraph();
k = raw_input("press close to exit");
