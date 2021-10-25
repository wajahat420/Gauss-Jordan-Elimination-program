

class ForwardElimination:
    
    def __init__(self, matrix):
        self.matrix = matrix
        self.matrixLength = len(self.matrix)
        self.modifiedMatrix = []

    def elementsToIterate(self, matrixLength, index):
        elements = matrixLength - 1 - index
        return matrixLength -  elements

    def checkingSuitableRow(self, row, elemIndex, element):
        iterateFrom = self.elementsToIterate(self.matrixLength, row)
        print("row", row)

        a = []
        # for elemIndex in range(iterateFrom, self.matrixLength):
        elemValue = self.matrix[elemIndex][row]
        a.append(elemValue)
        print(elemValue)
        print("end\n")


    def calculate(self):
        print(self.matrix)

        for column in range(0, self.matrixLength-1):
            # iterateFrom = self.elementsToIterate(self.matrixLength, rowIndex)
            # iterateFrom = self.elementsToIterate(self.matrixLength, rowIndex)
            temp = []
            element = self.matrix[column]
            print("FISRT")
            for row in range(column+1, self.matrixLength):
                indexElem = self.matrix[column][row] 
                print("elemIndex", row, column)
                # if element != 0:
                suitableRow = self.checkingSuitableRow(column, row, element)


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
    