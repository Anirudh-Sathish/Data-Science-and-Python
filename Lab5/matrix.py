# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:40:13 2022

@author: anirudh Sathish 

"""

"""
Write a python program to perform matrix operations on an M x N matrix and solve a system of linear equations. Use inbuilt functions to implement the operations.
Get two matrices from the user. The program should support the following Menus,

Matrix Addition
Matrix Subtraction
Scalar Matrix Multiplication
Elementwise Matrix Multiplication
Matrix Multiplication
Matrix Transpose
Trace of a Matrix
Solve System of Linear Equations
Determinant
 Inverse
 Singular Value Decomposition
 Eigen Value
 Search an Element
 Difference of Sum of Upper and Lower Triangular Matrix
 Exit

"""
# Importing the neccesary libraries 
import numpy as np 

class Matrix_here(object):
    def __init__(self,column, row):
        self.columnSize = column
        self.rowSize = row
    def insertValues(self):
        print("Enter inputs for the matrices ")
        tuple_c = (self.columnSize,self.rowSize)
        list_c = []
        i = 0
        while i != self.rowSize:
            j = 0
            while j != self.columnSize:
                try:
                    inp = int(input("Enter "))
                except:
                    print("Error 3 : Error in input")
                list_c.append(inp)
                j+= 1
            i+= 1
        a = np.array(list_c)
        self.array_One = np.reshape(a,tuple_c)
        print(self.array_One)
        return self.array_One
    def addition(self,b):
        try:
            c = self.array_One+b
            return c
        except:
            print("Error 1 : Couldnt add matrices , maybe their dimensions dont match")
    
    def subtaction(self,b):
        try:
            c = self.array_One-b
            return c
        except:
            print("Error 1 : Couldnt subtract matrices , maybe their dimensions dont match")
    
    def scalarMultiplication(self,scalar):
        try:
            c = self.array_One*scalar
            return c
        except: 
            print("Error 2: Maybe the value u sent is not the required type ")
    def elementWiseMatrixMultiplication(self,b):
        try:
            c = self.array_One*b
            return c
        except: 
            print("Error 1: Maybe Dimension Mismatch")
    def MatrixMultiplication(self,b):
        try:
            c = self.array_One.dot(b)
            return c
        except: 
            print("Error 1: Maybe Dimension Mismatch")
    def Transpose(self):
        try:
            c = self.array_One.transpose()
            return c
        except: 
            print("Error 4 ")
    def FindTrace(self):
        try:
            c = self.array_One.trace()
            return c
        except: 
            print("Error 4 ")
    def SolveLinearEquation(self , input , output):
        try:
            solution = np.linalg.solve(input,output)
            return solution
        except: 
            print("Error 6: Either the dimensions are incorrect , or the matrix is singular ")
    def FindDeterminant(self):
        try:
            solution = np.linalg.det(self.array_One)
            return solution
        except: 
            print("Error 4 ")
    def FindInverse(self):
        try:
            solution = np.linalg.inv(self.array_One)
            return solution
        except: 
            print("Error 4 ")
    def FindSVD(self):
        try:
            solution = np.linalg.svd(self.array_One)
            return solution
        except: 
            print("Error 4 ")
    def FindEigenValue(self):
        try:
            solution = np.linalg.eigvals(self.array_One)
            return solution
        except: 
            print("Error 8 : The eigen value computation foes not converge  ")
    def SearchForElement(self,searchElement):
        try:
            c = np.where(self.array_One == searchElement)
            column_no = np.array2string(c[0])
            row_no = np.array2string(c[1])

            t_w = column_no.split("[")
            t_w = t_w[1].split("]")
            column_no = t_w[0]
            print("Corresponding Column no :",column_no)
            t_w = row_no.split("[")
            t_w = t_w[1].split("]")
            row_no = t_w[0]
            print("Corresponding Row no    :",row_no)
            return c
        except:
            print("Error 4")
    def getDiffImSum(self):
        try:
            upper = np.triu(self.array_One)
            sum_Upper = np.sum(upper)
            lower = np.triu(self.array_One)
            sum_lower = np.sum(lower)
            diff = sum_Upper - sum_lower
            return diff
        except:
            print("Error 4")

# Creating the required matrices 
print("Enter the required columns and rows ")
column = int(input("Enter the number of columns"))
row = int(input("Enter the number of rows"))

#Creating the matrices 
Matrix1 = Matrix_here(column,row)
Matrix2 = Matrix_here(column,row)

A = Matrix1.insertValues()
B = Matrix2.insertValues()

exploration_done = False

while exploration_done is False:
    # Writing the menu part 
    print("Welcome to Matrix Operations \n ")
    print("What Operation do u want to perform \n")
    print("Press Key according to need ")
    print("Press 1 To Add the two Matrices  ")
    print("Press 2 For Matrix Subtraction")
    print("Press 3 For Scalar Matrix Multiplication ")
    print("Press 4 For Elementwise Matrix Multiplication  ")
    print("Press 5 For Matrix Multiplication ")
    print("Press 6 For Matrix Transpose")
    print("Press 7 For  Trace of a Matrix ")
    print("Press 8 To Solve System of Linear Equations  ")
    print("Press 9 For Determinant")
    print("Press 10 For Inverse ")
    print("Press 11 For Singular Value Decomposition  ")
    print("Press 12 For Eigen Value")
    print("Press 13 For Search an Element")
    print("Press 14 Difference of Sum of Upper and Lower Triangular Matrix ")
    print("Press 15 For Exiting ")
    option_chosen = int(input("Enter the option you want to chose"))
    if option_chosen == 1:
        #Inserting value into dict
        val =  Matrix1.addition(B)
        print(val)
    elif option_chosen == 2:
        print("Subtraction of matrix 2 from 1")
        val =  Matrix1.subtaction(B)
        print(val)
        print("Subtraction of matrix 1 from 2")
        val =  Matrix2.subtaction(A)
        print(val)
    elif option_chosen == 3:
        scalar = int(input("Enter the scalar "))
        print("The value of the first matrix after scalar multiplication ")
        val = Matrix1.scalarMultiplication(scalar)
        print(val)
        print("The value of the second matrix after scalar multiplication ")
        val = Matrix2.scalarMultiplication(scalar)
        print(val)
    elif option_chosen == 4:
        print("Element wise multiplication ")
        val = Matrix1.elementWiseMatrixMultiplication(B)
        print(val)
    elif option_chosen == 5:
        print("Matrix multiplication of Matrix 1 * Matrix 2  ")
        val = Matrix1.MatrixMultiplication(B)
        print(val)
        print("Matrix multiplication of Matrix 2 * Matrix 1  ")
        val = Matrix2.MatrixMultiplication(A)
        print(val)
    elif option_chosen == 6:
        print("Transpose of matrix 1 ")
        val = Matrix1.Transpose()
        print(val)
        print("Transpose of matrix 2 ")
        val = Matrix2.Transpose()
        print(val)
    elif option_chosen == 7:
        print("Trace of matrix 1 ")
        val = Matrix1.FindTrace()
        print(val)
        print("Trace of matrix 2 ")
        val = Matrix2.FindTrace()
        print(val)
    elif option_chosen == 8:
        print("Solution when Matrix 1 is known input and Matrix 2 is output")
        val = Matrix1.SolveLinearEquation(A,B)
        print(val)
        print("Solution when Matrix 2 is known input and Matrix 1 is output")
        val = Matrix2.SolveLinearEquation(B,A)
        print(val)
    elif option_chosen == 9:
        print("The determinant of matrix 1 is ")
        val = Matrix1.FindDeterminant()
        print(val)
        print("The determinant of matrix 2 is ")
        val = Matrix2.FindDeterminant()
        print(val)
    elif option_chosen == 10:
        print("The Inverse of matrix 1 is ")
        val = Matrix1.FindInverse()
        print(val)
        print("The Inverse of matrix 2 is ")
        val = Matrix2.FindInverse()
        print(val)
    elif option_chosen == 11:
        print("Singular Value decomposition of matrix 1 ")
        val = Matrix1.FindSVD()
        print(val)
        print("Singular Value decomposition of matrix 2")
        val = Matrix2.FindSVD()
        print(val)
    elif option_chosen == 12:
        print("Eigen Value of matrix A ")
        val = Matrix1.FindEigenValue()
        print(val)
        print("Eigen Value of matrix B ")
        val = Matrix1.FindEigenValue()
        print(val)
    elif option_chosen == 13:
        inp = int(input("Enter element to search in matrix 1"))
        print("Serarching for element in matrix 1  ")
        val = Matrix1.SearchForElement(inp)
        print(val)
        inp = int(input("Enter element to search in matrix 1"))
        print("Eigen Value of matrix B ")
        val = Matrix1.SearchForElement(inp)
        print(val)
    elif option_chosen == 14:
        print("Difference for upper and lower Triangular matrix sum of matrix 1 ")
        val = Matrix1.getDiffImSum()
        print(val)
        print("Difference for upper and lower Triangular matrix sum of matrix 2 ")
        val = Matrix2.getDiffImSum()
        print(val)
    elif option_chosen == 15:
        print("Thanks for visiting ")
        print("You are exiting now")
        exploration_done = True
    else:
        print("Maybe you made an input error. We take input values from range 1 to 4")
