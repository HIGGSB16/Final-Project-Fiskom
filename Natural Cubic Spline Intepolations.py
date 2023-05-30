import numpy as np

# Use the natural cubic spline to determine y at x = 1.25, data points \n
# are as follows: (2,1), (1,0), (5,0), (3,0), (4,1)


# First, rearrange the values to ease the process
# (1,0), (2,0), (3,0), (4,0), (5,0)

x = [1, 2, 3, 4, 5]
y = [0, 1, 0, 1, 0]
n = len(x)

# Knots, k[i-1](x[i-1]-x[i]) + 2k[i](x[i-1]-x[i+1]) + k[i+1](x[i]-x[i+1]) = \n
# 6((y[i-1]-y[i]/x[i-1]-x[i]) - (y[i]-y[i+1]/x[i]-x[i+1]))
# for i = 2, 3, ..., n-1

## When k1 and k5 = 0, we get:
## -4k2 - k3 = ...
## -k2 - 4k3 - k4 = ...
## -k3 - 4k4 = ...

p = []
for i in range(2, n):
    j = int(6*(((y[i-2] - y[i-1])/(x[i-2] - x[i-1])) - ((y[i-1] - y[i])/(x[i-1] - x[i]))))
    p.append(j)

## then, the matrix is

t = np.array([[-4, -1, 0], [-1, -4, -1], [0, -1, -4]])
r = np.array([[p[0]], [p[1]], [p[2]]])

# Using Gauss Elimination, we have:

k2 = -(30/7)
k3 = k2
k4 = (36/7)

# For the interpolant for a segment:
# f[i, i+1](x) = k[i]/6 (((x - x[i+1])^3 / (x[i] - x[i+1])) - (x - x[i+1])(x[i] - x[i+1]))
#                - k[i+1]/6 (((x - x[i])^3 / (x[i] - x[i+1])) - (x - x[i])(x[i] - x[i+1]))
#                + ((y[i](x - x[i+1]) - y[i+1](x - x[i])) / (x[i] - x[i+1]))

## then

f = ((k2)*(-1/6) * ((((1.25 - x[0])**3) / (x[0] - x[1])) - ((1.25 - x[0])*(x[0] - x[1])))) + (((y[0]*(1.25 - x[1])) - (y[1]*(1.25 - x[0]))) / (x[0] - x[1]))

print("y(1.25) = ", round(f, 4))

