"""
Write a function that takes in an array of strings and groups anagrams together.

Anagrams are strings made up of exactly the same letters, where order doesn't matter. For ex--"cinema" and "iceman" are anagrams; like "foo" and "ofo".

Your function shoudl return a list of anagram groups in no particular order.

Input:
    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

Output:
    [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]


O(w*n*log(n))T | O(wn)S
"""
import time



def groupAnagrams(words):
    matches = []
    copy_of_words = [x for x in words]

    for word_idx in range(len(words)):
        print("Processing idx:", word_idx)
        idx_list = []
        for match in copy_of_words:
            print("evaling match:", match)
            if sorted(words[word_idx]) == sorted(match):
                idx_list.append(match)
        if idx_list:
            for x in idx_list:
                copy_of_words.remove(x)
            matches.append(idx_list)


    return matches


if __name__ == "__main__":

    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    #words = ["abc", "dabd", "bca", "cab", "ddba"]


    print(groupAnagrams(words))
