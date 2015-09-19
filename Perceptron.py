import random as rand;
import os, subprocess

class Perceptron:

    #Constructor
    def __init__(self, inputLength, learningConstant):
        self.learningConstant = learningConstant;
        self.inputLength = inputLength;
        #weights is a 3d vector.
        self.weights = {};
        n = 0;
        while n < inputLength:
            #randomly assigning weights here, value of -1 to 1
            self.weights[n] = rand.uniform(-1, 1);
            n += 1;

    #Feed, input "inputs", output 1 or -1 (true or false)
    #Test of network
    def feedForward(self, inputs):
        sum = 0;
        #dot product of inputs and weights vectors
        for idx, i in enumerate(inputs):
            sum += i*self.weights.get(idx);
        print("Sum of feedForward is " + str(sum));
        print("Result of activation is " + str(self.activate(sum)));
        return self.activate(sum);

    #Simply determines if sum is above or below 0
    def activate(self, sum):
        return (1 if sum > 0 else -1);

    #Runs data through feedForward and adjusts weights according to results
    def train(self, inputs, desired):
        guess = self.feedForward(inputs);
        error = desired - guess;
        for i in range(0, self.inputLength):
            self.weights[i] += self.learningConstant * error * inputs[i];
        print(self.weights);

#trainer class, just inputs, bias, ans
class Trainer:
    def __init__(self, x, y, answer):
        self.inputs = [x, y, 1];
        self.ans = answer;
