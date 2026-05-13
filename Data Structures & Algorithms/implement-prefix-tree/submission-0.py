class PrefixTree:

    def __init__(self):
        self.arr = []

    def insert(self, word: str) -> None:
        self.arr.append(word)

    def search(self, word: str) -> bool:
        for words in self.arr:
            if words == word:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:

        for word in self.arr:
            if word[:len(prefix)] == prefix:
                return True
        return False
        
        