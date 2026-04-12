# LeetCode #208 — Implement Trie (Prefix Tree)
#
# Implement a Trie data structure with insert, search, and startsWith methods.
# search returns True if the word exists; startsWith returns True if any word
# has the given prefix.
#
# Example:
#   trie = Trie()
#   trie.insert("apple")
#   trie.search("apple")    → True
#   trie.search("app")      → False
#   trie.startsWith("app")  → True

from collections import defaultdict


class Trie:
    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.startsWith("app") == True
    print("All tests passed!")
