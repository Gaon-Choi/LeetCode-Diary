class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i = 0
        j = 0

        dxs = [0, 1, 0, -1]
        dys = [1, 0, -1, 0]

        d = 0

        size_h = len(matrix)
        size_w = len(matrix[0])

        max_num = size_h * size_w
        curr_num = 0

        result = []

        MARKER = -1000

        while True:
            if curr_num == max_num:
                break
            
            result.append(matrix[i][j])
            matrix[i][j] = MARKER
            curr_num += 1

            if not (0 <= i + dxs[d] < size_h and 0 <= j + dys[d] < size_w and matrix[i+dxs[d]][j+dys[d]] != MARKER):
                d = (d + 1) % 4

            i += dxs[d]
            j += dys[d]

        return result