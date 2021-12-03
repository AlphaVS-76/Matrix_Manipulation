import numpy as np                         # importing numpy library

a = np.array([[1, 2, 3, 4, 5],             # A matrix of order 6x5
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30]])

print(a[2:4, : 2])                         # for printing basics cubes within a given matrix

print(a[[0, 1, 2, 3], [1, 2, 3, 4]])       # for printing diagonal elements

print(a[[0, -2, -1], 3:])                  # for printing random pairs in the matrix
