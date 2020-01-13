class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        non_empty_cols = self.get_value_cols(A)
        non_empty_rows = self.get_value_rows(B)
        a_rows = len(A)
        a_cols = len(A[0])
        # matrix multiplication: the result columns are the min(a_cols, b_cols)
        cols = min(a_cols, len(B[0]))
        ans = [[0 for _ in range(cols)] for _ in range(a_rows)]
        for r in range(a_rows):
            for c in range(cols):
                non_empty = non_empty_cols[r].union(non_empty_rows[c])
                product = self.calc_product(A, B, r, c, non_empty)
                ans[r][c] = product
        return ans

    def get_value_cols(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        nec = [set() for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    continue
                nec[r].add(c)
        return nec

    def get_value_rows(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        ner = [set() for _ in range(cols)]
        for c in range(cols):
            for r in range(rows):
                if matrix[r][c] == 0:
                    continue
                ner[c].add(r)
        return ner

    def calc_product(self, A, B, r, c, commons):
        product = 0
        for i in commons:
            product += A[r][i] * B[i][c]
        return product



