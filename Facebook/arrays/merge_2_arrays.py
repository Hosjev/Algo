class MergeArrays:
    """ O(N) """
    def sort(self, A, B):
        if not bool(A): return B
        if not bool(B): return A

        flex = len(A) - 1
        Pb = len(B) - 1
        try:
            Pa = max([i for i,e in enumerate(A) if e])
        except ValueError: # If A full of None
            return B
        while Pa >= 0 and Pb >= 0:
            if A[Pa] > B[Pb]:
                A[flex] = A[Pa]
                Pa -= 1
                while A[Pa] is None:
                    Pa -= 1
            else:
                A[flex] = B[Pb]
                Pb -= 1
            flex -= 1
        # Last check
        if Pa < 0: A[0] = B[0]
        return A


if __name__ == "__main__":
    A = [1, 3, 5, None, None, None]
    B = [2, 4, 6]
    print(MergeArrays().sort(A, B))
