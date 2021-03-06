import random
import numpy as np
import time
def CreateMatrix(rows,columns):
    Matrix=[]
    for i in range(rows):
        Matrix.append([])
        for j in range(columns):
             Matrix[i].append(random.randint(0, 10))                
    return Matrix

rows=int(input("rows="))
columns=int(input("columns="))
Matrix1 = CreateMatrix(rows,columns)
Matrix2 = CreateMatrix(rows,columns)
Matrix1NumPy = np.array(Matrix1)
Matrix2NumPy = np.array(Matrix2)

def MulMatrix(Matrix1,Matrix2):
    Result=np.zeros((rows,columns))
    for i in range(rows):
        for j in range(columns):
            for k in range(rows):
                Result[i][j] += Matrix1[i][k] * Matrix2[k][j]
    return Result
startTime = time.time()
MulMatrix(Matrix1,Matrix2)
timeMult=time.time() - startTime
print("MulMatrix: {:.7f}s" .format(timeMult))

startTimeNumPy = time.time()
NumPyMulMatrix= np.dot(Matrix1NumPy,Matrix2NumPy)
timeNumPy=time.time() - startTimeNumPy
print("NumPyMulM: {:.7f}s" .format(timeNumPy))


################# if rows=200 and columns=200, result is MulMatrix: 11.3646371s and NumPyMulM: 0.0050006s
