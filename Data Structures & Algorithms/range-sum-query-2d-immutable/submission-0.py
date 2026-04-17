class NumMatrix:
    prefixes = [[]]
    og = [[]]
    def __init__(self, matrix: List[List[int]]):
        self.og = matrix
        self.prefixes = [[0 for _ in range(len(matrix[0])+1)] for __ in range(len(matrix)+1)]
        for i in range(1, len(self.prefixes)):
            for j in range(1, len(self.prefixes[i])):
                self.prefixes[i][j] = self.prefixes[i][j-1] + matrix[i-1][j-1]
        
        for j in range(1, len(self.prefixes[0])):
            for i in range(1, len(self.prefixes)):
                self.prefixes[i][j] += self.prefixes[i-1][j]
        print(self.prefixes)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixes[row2+1][col2+1] + self.prefixes[row1][col1] - self.prefixes[row1][col2+1] - self.prefixes[row2+1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)