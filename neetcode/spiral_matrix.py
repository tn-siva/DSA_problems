class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out_list = []
        first_row = 0
        first_col = 0
        last_row = len(matrix)
        last_col = len(matrix[0])
        matrix_size = last_row * last_col
        last_row -= 1
        last_col -= 1
        
        def traverse_right():
            cc = first_col
            nonlocal first_row
            while cc<=last_col:
                out_list.append(matrix[first_row][cc])
                cc += 1
            first_row += 1

        def traverse_down():
            rr = first_row
            nonlocal last_col
            while rr<=last_row:
                out_list.append(matrix[rr][last_col])
                rr += 1
            last_col -= 1

        def traverse_left():
            cc = last_col
            nonlocal last_row
            while cc>=first_col:
                out_list.append(matrix[last_row][cc])
                cc -= 1
            last_row -= 1

        def traverse_up():
            rr = last_row
            nonlocal first_col
            while rr>=first_row:
                out_list.append(matrix[rr][first_col])
                rr -= 1
            first_col += 1

        # while first_row<= last_row and first_col<= last_col:
        while True:
            traverse_right()
            if len(out_list) == matrix_size:
                break
            traverse_down()
            if len(out_list) == matrix_size:
                break
            traverse_left()
            if len(out_list) == matrix_size:
                break
            traverse_up()
            if len(out_list) == matrix_size:
                break

        return out_list
