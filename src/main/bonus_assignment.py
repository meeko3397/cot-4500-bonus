import numpy as np

print("Question 1 \n")

guess = np.array([0, 0, 0])
tolerance = 1e-6

matrix = np.array([[3, 1, 1], [1, 4, 1], [2, 3, 7]])
b_vector = np.array([1, 3, 0])

print("Question 2 \n")

guess = np.array([0, 0, 0])
tolerance = 1e-6

matrix = np.array([[3, 1, 1], [1, 4, 1], [2, 3, 7]])
b_vector = np.array([1, 3, 0])

print("Question 3 \n")

tolerance = 1e-6
guess = 0.5

print("Question 4 \n")

def hermite(num, x, f, fp):
    h = np.zeros((num * 2, num * 2))

    for i in range(num):
        h[i * 2][0] = x[i]
        h[i * 2 + 1][0] = x[i]
        h[i * 2][1] = f[i]
        h[i * 2 + 1][1] = f[i]
        h[i * 2 + 1][2] = fp[i]

        for j in range(2, num * 2):
            for k in range(j-1, num * 2):
                if(h[k][j] == 0 and h[k][j-1] != 0 and h[k-1][j-1] != 0):
                    h[k][j] = (h[k][j-1]-h[k-1][j-1]) / (h[k][0] - h[k-j+1][0])
        return h

# Given info
num = 3
x = [0, 1, 2]
f = [1, 2, 4]
fp = [1.06, 1.23, 1.55]

print(hermite(num, x, f, fp), "\n")

print("Question 5 \n")

def function(y,t):
    return (y - t**3)

def eulers_method(y, t, iterations, x):
     h = (x - y) / iterations

     for unused_variable in range(iterations):
         t = t + (h * function(y,t))
         y = y + h

     print("%.5f \n" % t)

# Given info
y_0 = 0
t_0 = 0.5
iterations = 100
x = 3
eulers_method(y_0, t_0, iterations, x)
