

class ForwardElimination:
    
    def __init__(self, matrix):
        self.matrix = matrix
        self.matrixLength = len(self.matrix)
        self.modifiedMatrix = []
        self.same = -1 # 0 index = row, 1 index = operation, 2  index = multiply / divide by X
        self.inverse = -1 # 0 index = row, 1 index = operation, 2  index = multiply / divide by X
        self.multiple = [] # 0 index = row, 1 index = operation, 2 index = multiply / divide by X, 3 multiply own row = True
        self.leastMultiple = None
        # self.perform = ""  # +, -, *, / 
        # self.multiplyBy = ""

    def elementsToIterate(self, matrixLength, index):
        elements = matrixLength - 1 - index
        return matrixLength -  elements

    def setLeastMultiple(self, elemValue, element):
        setLeastMultiple = False

        if self.leastMultiple == None:
            setLeastMultiple = True

        else:
            if elemValue // element < self.leastMultiple or (element // elemValue < self.leastMultiple and element // elemValue != 0):
                setLeastMultiple = True

        if setLeastMultiple:
            if elemValue % element == 0:
                self.leastMultiple = elemValue // element
            else:
                self.leastMultiple = element // elemValue
                
        if self.leastMultiple < 0 :
            self.leastMultiple *= -1
        
        if setLeastMultiple:
            return True
        else:
            return False

    def checkingSuitableRow(self, column, row, element):
        iterateFrom = self.elementsToIterate(self.matrixLength, column)
        # print("checkingSuitablecolumn", row, column, element)
        elemValue = self.matrix[row][column]

        if elemValue % element == 0 or element % elemValue == 0:

            if elemValue == element:
                # print("equal", element, elemValue, row, column)
                self.same = row
            elif elemValue + element == 0:
                self.inverse = row
                # print("inversec", element, elemValue, row, column)

            else:

                leastMultiple = self.setLeastMultiple(elemValue, element)
                # print("multiple", element, elemValue, row, column, self.leastMultiple)


                if leastMultiple:
                    self.multiple.append(row)
                    self.multiple.append("+")
                    self.multiple.append(True)

                    if elemValue % element == 0:
                        self.multiple.append(elemValue // element)
                    else:
                        self.multiple.append(element // elemValue)
                        self.multiple[2] = False


                    if elemValue * element > 0:
                        self.multiple[1] = "-"


        # print(elemValue)


    def calculate(self):
        # print(self.matrix)

        for column in range(0, self.matrixLength-1):
            # iterateFrom = self.elementsToIterate(self.matrixLength, rowIndex)
            element = self.matrix[column][column]
            if element != 0:
            # print("\nFISRT")
                for row in range(column+1, self.matrixLength):
                    # indexElem = self.matrix[column][row] 
                    # print("row = ", row, column)

                    # if element != 0:
                    suitableRow = self.checkingSuitableRow(column, row, element)
                print("multiple", self.multiple)
                print("same", self.same)
                print("inverse", self.inverse)

matrix = [
            [1, 3, 0],
            [2, 1, 3],
            [4, 2, 3]
        ]
matrix2 = [
            [1, 3, 0, 8],
            [2, 1, 3, 7],
            [4, 2, 3, 5],
            [0, 4, 10, 15]
        ]
ans = [1, 6, 3]
forward_obj  = ForwardElimination(matrix)
forward_obj.calculate()
