import random as rand;
import os, subprocess

class Perceptron:
    def __init__(self, inputLength, learningConstant):
        super(Perceptron, self).__init__();
        self.learningConstant = learningConstant;
        self.inputLength = inputLength;
        self.weights = {};
        n = 0;
        while n < inputLength:
            self.weights[n] = rand.uniform(-1, 1);
            n += 1;

    def feedForward(self, inputs):
        sum = 0;
        for i in range(0, self.inputLength):
            sum += i*self.weights.get(i);
        print("Sum of feedForward is " + str(sum));
        print("Result of activation is " + str(self.activate(sum)));

    def activate(self, sum):
        return (1 if sum > 0 else -1);

    def train(self, inputs, desired):
        guess = feedForward(inputs);
        error = desired - guess;
        for i in range(0, self.inputLength):
            self.weights[i] += self.learningConstant * error * inputs[i];
            print(self.weights);

class Trainer:
    def __init__(self, x, y, bias, answer):
        self.inputs = [x, y, bias];
        self.bias = bias;
