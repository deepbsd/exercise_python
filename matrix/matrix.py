class Matrix(object):
    def __init__(self, matrix_string):
        self.row_of_strings = matrix_strings.split("\n")
        self.rows = [ elem.split(" ") for elem in rows_of_strings ]
        for arr in self.rows: 
            for index, char in enumerate(arr):
                arr[index] = int(char)
        self.cols = []
        for row in self.rows:
            col = []
            for val in row:
                col.append(val)
            self.cols.append(col)

    def row(self, index):
        pass

    def column(self, index):
        pass




