from random import sample

class Logic:
    @staticmethod
    def rows_count(matrix):
        length = len(matrix)
        rows = 0
        for i in range(length):
            first = matrix[0][i]
            for j in range(1, length):
                if matrix[j][i] != first:
                    break
            else:
                rows += 1
        return rows

    @staticmethod
    def matrix_shuffle(matrix):
        return list(map(lambda x: sample(x, len(x)), matrix))

    @staticmethod
    def turnR(r, c, matrix):
        length = len(matrix)
        if (0 < r < length-1 and 0 < c < length-1):
            temp = matrix[r-1][c-1]
            matrix[r-1][c-1] = matrix[r+1][c-1]
            matrix[r+1][c-1] = matrix[r+1][c+1]
            matrix[r+1][c+1] = matrix[r-1][c+1]
            matrix[r-1][c+1] = temp

            temp = matrix[r-1][c]
            matrix[r-1][c] = matrix[r][c-1]
            matrix[r][c-1] = matrix[r+1][c]
            matrix[r+1][c] = matrix[r][c+1]
            matrix[r][c+1] = temp
        return matrix   

    @staticmethod
    def turnL(r, c, matrix):
        length = len(matrix)
        if (0 < r < length-1 and 0 < c < length-1):
            temp = matrix[r-1][c-1]
            matrix[r-1][c-1] = matrix[r-1][c+1]
            matrix[r-1][c+1] = matrix[r+1][c+1]
            matrix[r+1][c+1] = matrix[r+1][c-1]
            matrix[r+1][c-1] = temp

            temp = matrix[r-1][c]
            matrix[r-1][c] = matrix[r][c+1]
            matrix[r][c+1] = matrix[r+1][c]
            matrix[r+1][c] = matrix[r][c-1]
            matrix[r][c-1] = temp
        return matrix 

    @staticmethod
    def generate_level(level, length):
        row = []
        for i in range(level+1):
            for j in range(length // (level+1)):
                row.append(i)
        for k in range(length % (level+1)):
            row.append(level)
        return [row for i in range(length)]