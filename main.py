

class ForwardElimination:
    
    def __init__(self, matrix):
        self.matrix = matrix
        self.matrixLength = len(self.matrix)
        self.modifiedMatrix = []
        self.same = -1 
        self.inverse = -1 
        self.multiple = [] # 0 index = row, 1 index = operation, 2 multiply own row = True, 3 index = multiply / divide by X
        self.leastMultiple = None
        self.noMultiple = False

    def elementsToIterate(self, matrixLength, index):
        elements = matrixLength - 1 - index
        return matrixLength -  elements

    def setLeastMultiple(self, elemValue, element):
        setLeastMultiple = False

        if self.leastMultiple == None:
            setLeastMultiple = True

        else:
            if (elemValue // element < self.leastMultiple and element // elemValue != 0) or (element // elemValue < self.leastMultiple and element // elemValue != 0):
                setLeastMultiple = True

        if setLeastMultiple:
            if elemValue % element == 0:
                self.leastMultiple = elemValue // element
            else:
                self.leastMultiple = element // elemValue
                
        if self.leastMultiple < 0 :
            self.leastMultiple *= -1
        
        # print(setLeastMultiple, "\n")
        if setLeastMultiple:
            return True
        else:
            return False

    def checkingSuitableRow(self, column, row, element):

        multiple = False
        for i in range(column,len(self.matrix)):
            elemValue = self.matrix[i][column]

            if self.noMultiple:
                elemValue = int(self.matrix[i][column] * element / self.matrix[i][column])
                multipliedRow = self.onlyMultiply(self.matrix[i], element / self.matrix[i][column])
                self.matrix[i] = multipliedRow
                self.noMultiple = False

            if (elemValue % element == 0 or element % elemValue == 0) and i != row and elemValue != 0:
                # print("==", i)
                # print("elemValue", elemValue)
                multiple = True
                if elemValue == element:
                    # print("equal", element, elemValue, row, column)
                    self.same = i
                elif elemValue + element == 0:
                    self.inverse = i
                    # print("inversec", element, elemValue, row, column)

                else:

                    leastMultiple = self.setLeastMultiple(elemValue, element)
                    # print("multiple", element, elemValue, row, column, self.leastMultiple)


                    if leastMultiple:
                        # self.multiple = []
                        self.multiple.append(i)
                        self.multiple.append("+")
                        self.multiple.append(True)

                        if elemValue % element == 0:
                            self.multiple.append(elemValue // element)
                        else:
                            self.multiple.append(element // elemValue)
                            self.multiple[2] = False

                        if elemValue * element > 0:
                            self.multiple[1] = "-"

                        if self.multiple[3] < 0:
                            self.multiple[3] *= -1

        if not multiple:
            self.noMultiple = True
            self.checkingSuitableRow(column, row, element)

    def addRows(self,row1, row2):
        matrix = self.matrix
        return [matrix[row1][i] + matrix[row2][i] for i in range(len(self.matrix))]

    def subtractRows(self, row1, row2):
        matrix = self.matrix
        return [matrix[row1][i] - matrix[row2][i] for i in range(len(self.matrix))]

    def multiply(self, row, matrix):
        if matrix[2]:
            index = row
            otherIndex = matrix[0]
        else:
            index = matrix[0]
            otherIndex = row

        if matrix[1] == "+":
            array = [
                self.matrix[index][i] * matrix[3] + self.matrix[otherIndex][i]
                for i in range(len(self.matrix))
            ]
        else:
            array = [
                self.matrix[index][i] * matrix[3] - self.matrix[otherIndex][i]
                for i in range(len(self.matrix))
            ]
        # print("array", array, self.matrix[index],matrix[3],self.matrix[otherIndex])
        return array

    def onlyMultiply(self, row, number):
        return [i * number for i in row]

    def calculate(self):
        for column in range(0, self.matrixLength-1):
            # iterateFrom = self.elementsToIterate(self.matrixLength, rowIndex)
            diagonalElem = self.matrix[column][column]
            if diagonalElem != 0:
                for row in range(column+1, self.matrixLength):
                    element = self.matrix[row][column]
                    # print("element = ", element)

                    # print("row = ", row, column)
                    print("\nelem", element, row, column)
                    suitableRow = self.checkingSuitableRow(column, row, element)

                    if self.inverse != -1:
                        print("adding")
                        self.matrix[row] = self.addRows(row, self.inverse)
                    elif self.same != -1:
                        print("subtracting")
                        self.matrix[row] = self.subtractRows(row, self.same)
                    elif len(self.multiple) != 0:
                        print("multiply",self.matrix[row])
                        self.matrix[row] = self.multiply(row, self.multiple[:4])

                    print("matrix", self.matrix)
                    # print("same", self.same)
                    # print("inverse", self.inverse)

                    self.multiple = []
                    self.leastMultiple = None
                    self.same = -1
                    self.inverse = -1

matrix = [
            [1, 3, 0],
            [2, 1, 3],
            [4, 2, 3]
        ]
matrix2 = [
            [1, 1, 1],
            [2, 3, 7],
            [1, 3, -2]
        ]

ans = [1, 6, 3]
forward_obj  = ForwardElimination(matrix2)
forward_obj.calculate()

# matrix2 = [
#             [1, 3, 0, 8],
#             [2, 1, 3, 7],
#             [4, 2, 3, 5],
#             [0, 4, 10, 15]
#         ]

# matrix = [
#             [1, 3, 0],
#             [2, 1, 3],
#             [4, 2, 3]
#         ]
