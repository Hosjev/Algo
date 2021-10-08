"""
Write a SuffixTrie class for that data structure. The class should have root properly set to the root node of the trie and support:
    Creating the trie from a string; by calling populateSuffixTrieFrom method upon instantiation, which should then populate the root of the class.
    Search for strings in the trie.

Note that every string added to the trie should end with the special endSymbol character "*".

Input:
   "babc" 

Output:
    {
      "c": { "*": True},
      "b": {
          "c": { "*": True},
          "a": { "b": {"c": {"*": True}}},
      }
      "a": { "b": {"c": {"*": True}}},
    }

Input (search):
    string = "abc"

Output:
    True

O(n^2)T | O(n)S
"""
import time


class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        # Write your code here.
        # Process one character/item at a time from string
        for item in range(len(string)):
            self.inner_populate(item, string)

    def inner_populate(self, item, string):
        # Set first node to root (empty dict to start) starts w/top level suffix
        node = self.root
        # Iterate from item (our suffix) to end of string
        for suffix in range(item, len(string)):
            char = string[suffix] # set the character
            if char not in node: # if our char not in 'this level' dict
                node[char] = {} # initiate the dict with it as key
            node = node[char] # set node to THIS char we just created
        node[self.endSymbol] = True # at the end of this suffix creation, tail the dict w/end

    def contains(self, string):
        # Write your code here.
        node = self.root
        for item in string:
            if item in node:
                node = node[item] 
        # This allows the Trie to respond w/True or False
        return self.endSymbol in node



if __name__ == "__main__":

    string = "babc"

    trie = SuffixTrie(string)

    print(trie.root)
    #print(trie.contains("abc"))
    #print(trie.contains("abs"))
