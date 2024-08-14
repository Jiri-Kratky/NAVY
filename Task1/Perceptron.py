import numpy as np
import matplotlib.pyplot as plt
import Functions as fn

class Perceptron:
    def __init__(self,w:float,b:float,learning_rate:float):
        self.w=w
        self.b=b
        self.learning_rate=learning_rate
        
    def Run(self,x:float,y:float,results):
        changed=True
        epoches = 0
        # Training loop - while there is change in weights and bias continue training
        while changed==True:
            changed=False
            for i in range(len(x)):
                guess = np.sign(x[i] * self.w[0] + y[i] * self.w[1] + self.b)
                if guess != results[i]:          # Update weights and bias based on prediction error
                    error = results[i] - guess
                    self.w[0] = self.w[0] + x[i] * error * self.learning_rate 
                    self.w[1] = self.w[1] + y[i] * error * self.learning_rate
                    self.b = self.b + error * self.learning_rate
                    changed=True
            epoches += 1
        print("Epoches: ", epoches)
        print(f"w = {self.w} | b = {self.b}")

    def Run_Epoches(self,x:float,y:float,results,epoches):
        print("Epoches: ", epoches)
        while epoches!=0:
            for i in range(len(x)):
                guess = np.sign(x[i] * self.w[0] + y[i] * self.w[1] + self.b)
                if guess != results[i]:          # Update weights and bias based on prediction error
                    error = results[i] - guess
                    self.w[0] = self.w[0] + x[i] * error * self.learning_rate 
                    self.w[1] = self.w[1] + y[i] * error * self.learning_rate
                    self.b = self.b + error * self.learning_rate
            epoches -= 1
        print(f"w = {self.w} | b = {self.b}")
    
    def Predict(self,x:float,y:float):
        return np.sign(x * self.w[0] + y * self.w[1] + self.b)