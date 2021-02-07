"""
Write a ContMedianHandler.
    -continuous insertion of numbers with the insert method.
    -the instant O(1) time retrieval of the median of the numbers that have been inserted thus far w/getMedian method.

The getMedian method has already been written for you.

The median of a set of numbers is the "middle" number WHEN the numbers are ordered from smallest to largest. If there's an odd number of numbers in the set, as in {1, 3, 7}, the median is the number in the middle (3 prior); if there's an even number of numbers in the set, as in {1, 3, 7, 8}, the median is the average of the 2 middle numbers ( (3+7) / 2 == 5 ).

Input:
    ContinuousMedianHandler()

Output:
    insert(5): -
    insert(10): -
    getMedian(): 7.5
    insert(100): -
    getMedian(): 10

answer - O(WS + NM 8^S)T -- W=words in our trie; N/M is our 2D matrix and the most 8 times S levels we recursively search
       - O(WS + NM)S
"""
import time


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def add_word(self, string):
        node = self.root
        for char in string:
            if char not in node: # if our char not in 'this level' dict
                node[char] = {} # initiate the dict with it as key
            node = node[char] # set node to THIS char we just created
        node[self.endSymbol] = string # at the end of this suffix creation, tail the dict w/end


def boggleBoard(board, words):
    trie = Trie()
    for x in words:
        trie.add_word(x)

    final_words = {}
    visited = [ [False for letter in row] for row in board ]

    # Rows
    for row in range(len(board)):
        # Cols
        for col in range(len(board[row])):
            solve(row, col, board, trie.root, visited, final_words)

    return list(final_words.keys())


def solve(row, col, board, trie_node, visited, final_words):
    if visited[row][col]:
        return
    letter = board[row][col]
    if letter not in trie_node:
        return

    visited[row][col] = True
    trie_node = trie_node[letter]
    # Reached end of word search?
    if "*" in trie_node:
        final_words[trie_node["*"]] = True

    # DFS on neighbors
    for neighbor in get_adjacencies(row, col, board):
        solve(neighbor[0], neighbor[1], board, trie_node, visited, final_words)

    # Undo each as we have to traverse the next letter and possible answers
    visited[row][col] = False

	
def get_adjacencies(i, j, board):
    # 8 possible
    adjacencies = []
    # Diagonal upper left
    if i > 0 and j > 0:
        adjacencies.append([i - 1, j - 1])
    # Diagonal upper right
    if i > 0 and j < len(board[0])-1:
        adjacencies.append([i - 1, j + 1])
    # Diagonal lower right
    if i < len(board)-1 and j < len(board[0])-1:
        adjacencies.append([i + 1, j + 1])
    # Diagonal lower left
    if i < len(board)-1 and j > 0:
        adjacencies.append([i + 1, j - 1])
    # Upper center
    if i > 0:
        adjacencies.append([i - 1, j])
    # Lower center
    if i < len(board)-1:
        adjacencies.append([i + 1, j])
    # Left
    if j > 0:
        adjacencies.append([i, j - 1])
    # Right
    if j < len(board[0])-1:
        adjacencies.append([i, j + 1])

    return adjacencies




if __name__ == "__main__":

    board = [
        ["t", "h", "i", "s", "i", "s", "a"],
        ["s", "i", "m", "p", "l", "e", "x"],
        ["b", "x", "x", "x", "x", "e", "b"],
        ["x", "o", "g", "g", "l", "x", "o"],
        ["x", "x", "x", "D", "T", "r", "a"],
        ["R", "E", "P", "E", "A", "d", "x"],
        ["x", "x", "x", "x", "x", "x", "x"],
        ["N", "O", "T", "R", "E", "-", "P"],
        ["x", "x", "D", "E", "T", "A", "E"]
      ]
    words = ["t", "this", "is", "not", "a", "simple", "boggle", "board", "test", "REPEATED", "NOTRE-REPEATED"]

    # Build my Trie object
    trie = Trie()
    for word in range(len(words)):
        trie.add_word(words[word])
    print(trie.root)

    print(boggleBoard(board, words))
