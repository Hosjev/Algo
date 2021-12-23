from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # TC O(n * len of word) len of word can vary
        # Edge Case(s)
        if not bool(words): return False

        # Prime
        alpha = {c:i for i,c in enumerate(order)}

        # Logic (compare every word and char)
        for left_word, right_word in zip(words, words[1:]):
            positive = False # set this at word level?
            for l_c, r_c in zip(left_word, right_word):
                if l_c != r_c:
                    if alpha[l_c] > alpha[r_c]: return False
                    positive = True
                    break
            # We didn't break or return False
            if not positive and len(right_word) < len(left_word):
                return False
        return True



if __name__ == "__main__":
    words = ["appge", "applex", "app"]
    #words = ["apap", "app"]
    o = "abcdefghijklmnopqrstuvwxyz"
    print(Solution().isAlienSorted(words, o))
