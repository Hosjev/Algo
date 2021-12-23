class WordDictionary:

    def __init__(self):
        # We build a PREFIX trie
        self.trie = dict() 

    def addWord(self, word: str) -> None:
        trie = self.trie
        for letter in word:
            if not letter in trie:
                trie[letter] = dict()
            trie = trie[letter]
        trie["*"] = True

    def search(self, word: str) -> bool:
        def explore_trie(word, trie):
            for idx, char in enumerate(word):
                if not char in trie:
                    if char == ".": # unfortunately, a whole set of possible forks
                        for c in trie:
                            if c != "*" and explore_trie(word[idx + 1:], trie[c]):
                                return True
                    return False # a catch after exploring all possible forks
                else:
                    trie = trie[char]
            return "*" in trie # reached an end, or not
        return explore_trie(word, self.trie)
        


if __name__ == "__main__":
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("bod")
    obj.addWord("mad")
    obj.addWord("dad")
    print(obj.search(".ad"))
    print(obj.trie)
