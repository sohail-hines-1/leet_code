# LeetCode #211 — Design Add and Search Words Data Structure
#
# Implement a WordDictionary that supports addWord and search. The search method
# supports '.' as a wildcard that can match any single letter.
#
# Example:
#   wd = WordDictionary()
#   wd.addWord("bad")
#   wd.addWord("dad")
#   wd.search("bad")  → True
#   wd.search(".ad")  → True
#   wd.search("b..")  → True


class WordDictionary:
    def __init__(self):
        pass

    def addWord(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass


if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    assert wd.search("bad") == True
    assert wd.search(".ad") == True
    assert wd.search("b..") == True
    print("All tests passed!")
