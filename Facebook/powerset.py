class Powerset:
    """ O(2 base len(input)) b/c output appears as a BinTree """
    def _recur(self, master, idx = None) -> list:
        if idx is None: idx = len(master) - 1
        if idx < 0: return [ [] ]

        current = master[idx]
        subsets = self._recur(master, idx - 1)
        for sub_idx in range(len(subsets)):
            local_subset = subsets[sub_idx] + [current]
            # Specific feature for non-distinctness
            if local_subset not in subsets:
                subsets.append(local_subset)

        return subsets

    def evaluate(self, master_set):
        return self._recur(master_set)


if __name__ == "__main__":
    m = 'abcde'
    print(Powerset().evaluate(m))
