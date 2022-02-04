class FatFinger:
    """ TYPEAHEAD """

    def __init__(self, word):
        self.candidates = self.neighbor_helper(word)

    def permute_helper(self, placeholder, parent_idx, words):
        # Recursive
        # O(N) => candidates ^ characters in word O(3^4) [xxxx]
        # TODO: turn into on-demand generator
        if parent_idx == len(self.candidates):
            if self.word_helper(placeholder):
                words.append(placeholder)
            return words

        for c_idx in range(len(self.candidates[parent_idx])):
            local_placeholder = placeholder + self.candidates[parent_idx][c_idx] # just me, char index
            self.permute_helper(local_placeholder, parent_idx + 1, words)

        # Up the stack
        return words

    def word_helper(self, word):
        return True

    def neighbor_helper(self, word):
        candidates = []
        for letter in word:
            if letter == "b":
                candidates.append(["v", "b", "n"])
            if letter == "y":
                candidates.append(["t", "y", "u"])
            if letter == "e":
                candidates.append(["w", "e", "r"])
        return candidates


if __name__ == "__main__":
    # Q: the word helper is enormous amt of code given code is grammar agnostic
    #    the NH--does it return single chars or valid words?
    #    the NH--does it return the word or char typed?
    #    does the logic watch each char input or spaces/qualifiers?
    #    which chars are considered "nearby"? hex pattern? same line?
    #    do we ask user "did you mean..." and retrieve a new string?
    string = "gi"
    # We return permutations of "g" to "i" => starter to neighbor
    # ghf -> iok = gi, go, gk 
    #              hi, ho, hk
    #              fo, fi, fk
    # ALWAYS ALWAYS consider edge cases 2nd
    # Ask them ?s about the job and their take on an average day?
    f_obj = FatFinger("byeb")
    results = f_obj.permute_helper("", 0, [])
    print(results, len(results))
