#TODO
#Draw Graphs, and training dataset initialization
from Perceptron import *;
from graphics import *

p = Perceptron(inputLength = 3, learningConstant = 0.0005);
training = [];

def fLine(x):
    return -0.5*x + 1;

def setup():
    for i in range(0, 3000):
        x = rand.uniform(-5, 5);
        y = rand.uniform(-3, 3);
        ans = 1;
        if (y < fLine(x)):
            ans = -1;
        training.append(Trainer(x, y, ans));

def drawGraph():
    win = GraphWin("Perceptron - Training", 1000, 600);

    xAxis = Line(Point(0, 300), Point(1000, 300));
    yAxis = Line(Point(500, 0), Point(500, 600));
    xAxis.setWidth(2);
    yAxis.setWidth(2);
    xAxis.draw(win);
    yAxis.draw(win);

    targetLine = Line(Point(100, 0), Point(1000, 450));
    targetLine.setWidth(2);
    targetLine.setFill('green');
    targetLine.draw(win);

    currectWeightedLine = Line(Point(100, 0), Point(1000, 450));
    currectWeightedLine.setWidth(2);
    currectWeightedLine.setFill('red');
    currectWeightedLine.draw(win);

    for i, t in enumerate(training):
        print("Trainer " + str(i + 1) + " :[x = " + str(t.inputs[0]) + ", y = " + str(t.inputs[1]) + ", ans = " + str(t.ans) + "]");
        p.train(t.inputs, t.ans);

        guess = p.feedForward(t.inputs);
        pointT = Point(t.inputs[0]*100 + 500,-t.inputs[1]*100 + 300);

        if guess > 0:
            pointT.setFill("red");
        else:
            pointT.setFill("blue");
        pointT.draw(win);
        currectWeightedLine.undraw();
        currectWeightedLine = Line(Point(0, (((-5)*(p.weights.get(0)/p.weights.get(1)))-((p.weights.get(2)/p.weights.get(1))))*100 + 100), Point(1000, (((5)*(p.weights.get(0)/p.weights.get(1)))-((p.weights.get(2)/p.weights.get(1))))*100 + 100));
        currectWeightedLine.setWidth(2);
        currectWeightedLine.setFill('red');
        currectWeightedLine.draw(win);

        print("\n");
        time.sleep(0.00005);





    #After training, click on window to run through 2000 more random points to get a sense of correctness.
    win.getMouse();
    win.close();
    win = GraphWin("Perceptron - Trained", 1000, 600);
    xAxis = Line(Point(0, 300), Point(1000, 300));
    yAxis = Line(Point(500, 0), Point(500, 600));
    xAxis.setWidth(2);
    yAxis.setWidth(2);
    xAxis.draw(win);
    yAxis.draw(win);
    targetLine = Line(Point(100, 0), Point(1000, 450));
    targetLine.setWidth(2);
    targetLine.setFill('green');
    targetLine.draw(win);

    correctness = 0.0;
    currectWeightedLine = Line(Point(0, (((-5)*(p.weights.get(0)/p.weights.get(1)))-((p.weights.get(2)/p.weights.get(1))))*100 + 100), Point(1000, (((5)*(p.weights.get(0)/p.weights.get(1)))-((p.weights.get(2)/p.weights.get(1))))*100 + 100));
    currectWeightedLine.setWidth(2);
    currectWeightedLine.setFill('red');
    currectWeightedLine.draw(win);

    for i, t in enumerate(training):
        print("Trainer " + str(i + 1) + " :[x = " + str(t.inputs[0]) + ", y = " + str(t.inputs[1]) + ", ans = " + str(t.ans) + "]");

        guess = p.feedForward(t.inputs);
        print("guess: " + str(guess));
        pointT = Point(t.inputs[0]*100 + 500,-t.inputs[1]*100 + 300);

        if guess > 0:
            pointT.setFill("red");
        else:
            pointT.setFill("blue");
        pointT.draw(win);
        if guess == t.ans:
            correctness += 1;
        targetLine = Line(Point(100, 0), Point(1000, 450));
        time.sleep(0.00005);

    print("Correctness of Training is: " + str((correctness/3000.0)*100.0) + "%");
    print("Final weights: " + str(p.weights));

if __name__ == '__main__':
    print(p.weights);
    setup();
    drawGraph();
    k = raw_input("press close to exit");
