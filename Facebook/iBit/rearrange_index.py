class Solution:
    def rarray(self, A):
        """
        In this problem, we (in-place) adjust an array to reflect
        the # stored in the index indicated.
        This problem is solved in 2 steps:
        Changed each value in array to a corrupted version of the future pure #.
        1) a) future i * len(A) == the pure # to corrupt
           b) corrupt this # by adding i 
        2) a) remove len(A) from corrupted pure #
           b) subtract corruption from pure corrupted #
           c) remove len(A) from pure #
        ** note this works b/c the VALUES are of 0 -> len(A) -1 (indices)
        """
        # Establish a # we can properly corrupt
        for idx in range(len(A)):
            #          1st part of equation
            # The "i" that we're reviewing is the pure # we want to preserve
            #          2nd part of equation
            # The "i" we add is our own corruption
            val_of_idx = A[idx] % len(A)
            preserve = A[val_of_idx] % len(A)
            A[idx] = (preserve * len(A)) + val_of_idx
        print(A)

        # Change our values to the uncorrupted original #
        for idx in range(len(A)):
            # The pure # - len(A) - is removed from our corrupted pure #
            amt_corruption = A[idx] % len(A)
            # We remove that corruption from the corrupted pure
            # Now we can compare pure and pure
            A[idx] = int((A[idx] - amt_corruption) / len(A))

        return A

n = [4, 0, 2, 1, 3]
print(Solution().rarray(n))
