class Permutations:
    
    def count_matches(self, source, pattern):
        # Edge Case(s)
        if (len(pattern) > len(source)) or \
            not len(pattern):
            return 0

        # Build a cache of key/val where key = char / val = list of indices
        cache = dict()
        for idx, val in enumerate(source):
            try:
                cache[val].append(idx)
            except KeyError:
                cache[val] = [idx]
        
        # Build nested list of indices
        temp = [cache[i] for i in pattern if cache[i]]
        # Early exit if our nested list of indices doesn't match
        #   => each character isn't present
        if len(temp) != len(pattern): return 0

        indices = list()
        for i in temp: # unpack them
            for j in i: indices.append(j)

        # Main logic
        count = 0
        p_sorted = sorted(pattern)
        for i in indices:
            if sorted(source[i:i+len(pattern)]) == p_sorted:
                count += 1
        return count
    
    
if __name__ == "__main__":
    obj = Permutations()
    c = obj.count_matches("foobarbfoobararfoo", "bar")
    print(c)
