import numpy as np

a = float(input("Enter the coefficent - a : "))
b = float(input("Enter the coefficent - b : "))
c = float(input("Enter the coefficent - c : "))
d = float(input("Enter the coefficent - d : "))

x = np.random.rand()

learning_rate = .01
epochs =100

for epoch in range(epochs):
  value = a*x**3 + b*x**2 + d*x +c
  #Calculate the gradient of the equation with respect to x
  gradient  = 3*a *x**2 + 2*b*x+c
  #Apply ReLU to the gradient (if it's negative)
  if gradient < -1:
    gradient =0
    #Updating x using SGD
    x -=  learning_rate *gradient

print(f"The solution for x is approximately : {x}")