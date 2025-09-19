class Solution:
    def searchMatrix1(self, matrix: list[list[int]], target: int) -> bool:
        """
        Approach 1: Brute-force linear scan over all cells.

        Idea:
        - Iterate every row i and every column j; return True as soon as you find `target`.

        Assumptions:
        - Works for any matrix shape/content (no ordering assumptions).
        - This implementation assumes `matrix` and `matrix[0]` are non-empty.

        Complexity:
        - Time:  O(m * n) in the worst case (scan every element).
        - Space: O(1) auxiliary space.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False

    def searchMatrix2(self, matrix: list[list[int]], target: int) -> bool:
        """
        Approach 2: Staircase search from top-right.

        Idea:
        - Start at top-right (i=0, j=n-1).
        - If current > target, move left (j--), eliminating a column.
        - If current < target, move down (i++), eliminating a row.
        - In a matrix where each row is sorted L→R and each column is sorted T→B,
          this walks at most m+n steps.

        Assumptions:
        - Each row is sorted in nondecreasing order.
        - Each column is sorted in nondecreasing order.
        - `matrix` and `matrix[0]` are non-empty.

        Complexity:
        - Time:  O(m + n) in the worst case.
        - Space: O(1) auxiliary space.
        """
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1

        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1  # Eliminate current column (all below are >= current)
            else:
                i += 1  # Eliminate current row (all left are <= current)
        return False

    def searchMatrix3(self, matrix: list[list[int]], target: int) -> bool:
        """
        Approach 3: Binary search in each row.

        Idea:
        - For every row, run a standard binary search.
        - Early exit if found in any row.

        Assumptions:
        - Each row is individually sorted in nondecreasing order.
        - No requirement on column ordering.
        - `matrix` is non-empty; rows are non-empty.

        Complexity:
        - Time:  O(m * log n) in the worst case (binary search on each of m rows).
        - Space: O(1) auxiliary space.
        """

        def binary_search(array: list[int], target: int) -> bool:
            left, right = 0, len(array) - 1
            while left <= right:
                mid = (left + right) // 2
                if array[mid] == target:
                    return True
                elif array[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False

        for row in matrix:
            if binary_search(row, target):
                return True
        return False

    def searchMatrix4(self, matrix: list[list[int]], target: int) -> bool:
        """
        Approach 4: Flatten then binary search (explicit flattening).

        Idea:
        - Copy all m*n elements into a 1D array `arr` in row-major order,
          then binary search on `arr`.

        Assumptions:
        - For the binary search to be correct, the matrix must be "globally sorted"
          in row-major order: rows are sorted L→R and the first element of each row
          is >= the last element of the previous row.
        - `matrix` and `matrix[0]` are non-empty.

        Notes:
        - This implementation does a full O(m*n) flattening; one can avoid extra
          space by mapping a 1D index back to 2D coordinates during binary search.

        Complexity:
        - Time:  O(m * n) to build `arr` + O(log(m*n)) to search ⇒ overall O(m * n).
        - Space: O(m * n) for the flattened array.
        """
        m, n = len(matrix), len(matrix[0])
        arr = [0] * (m * n)
        k = 0

        for i in range(m):
            for j in range(n):
                arr[k] = matrix[i][j]
                k += 1

        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
