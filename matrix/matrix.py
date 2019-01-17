class Matrix(object):
    def __init__(self, matrix_string):
        #self.rows_of_strings = matrix_string.split("\n")
        #self.rows = [ elem.split(" ") for elem in self.rows_of_strings ]
        #for arr in self.rows: 
        #    for index, char in enumerate(arr):
        #        arr[index] = int(char)
        #self.cols = []
        #for col in self.rows[0]:
        #    self.cols.append([])

        #for col_num in range(len(self.cols)):
        #    for arr in self.rows:
        #        self.cols[col_num].append(arr[col_num])



        self.rows = [[element.split(" ") for element in string_element] for string_element in matrix_string.split("\n")]
        self.cols = [ list(tuple) for tuple in zip(*self.rows) ]


    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.cols[index-1]




