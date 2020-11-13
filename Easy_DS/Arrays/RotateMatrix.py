'''
You are given an n x n 2D self.matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D self.matrix directly. DO NOT allocate another 2D self.matrix and do the rotation.

Example 1:

Given input self.matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input self.matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input self.matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input self.matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''

class RotateMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        return

    
    def rotate_right(self):
        '''
        Matr = [[ 5, 1, 9,11],
                [ 2, 4, 8,10],
                [13, 3, 6, 7],
                [15,14,12,16]]

        rotated_matr = [[15, 13, 2, 5], 
                        [14, 3, 4, 1], 
                        [12, 6, 8, 9], 
                        [16, 7, 10, 11]]
        '''

        N = len(self.matrix)
        for i in range(N//2):
            for j in range(i, N-1-i):
                temp = self.matrix[i][j]
                self.matrix[i][j] = self.matrix[N-1-j][i]
                self.matrix[N-1-j][i] = self.matrix[N-1-i][N-1-j]
                self.matrix[N-1-i][N-1-j] = self.matrix[j][N-1-i]
                self.matrix[j][N-1-i] = temp
        return self.matrix

    def rotate_left(self):
        '''
        Matr = [[ 5, 1, 9,11],
                [ 2, 4, 8,10],
                [13, 3, 6, 7],
                [15,14,12,16]]

        rotated_matr = [[11, 10, 7, 16], 
                        [9, 8, 6, 12], 
                        [1, 4, 3, 14], 
                        [5, 2, 13, 15]]
        '''

        N = len(self.matrix)
        for i in range(N//2):
            for j in range(i, N-1-i):
                temp = self.matrix[i][j]
                self.matrix[i][j] = self.matrix[j][N-1-i]
                self.matrix[j][N-1-i] = self.matrix[N-1-i][N-1-j]
                self.matrix[N-1-i][N-1-j] = self.matrix[N-1-j][i]
                self.matrix[N-1-j][i] = temp
        return self.matrix



mat = [[ 5, 1, 9,11],
        [ 2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]]

print("matrix rotated right", RotateMatrix(mat).rotate_right())
print("matrix rotated left", RotateMatrix(mat).rotate_left())