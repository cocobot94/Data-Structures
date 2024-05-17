from TrieNode import TrieNode


class Trie:
    def __init__(self, root: TrieNode) -> None:
        self.root = root
        self.lista = []

    def insert(self, word: str):
        if not isinstance(word, str):
            return TypeError
        w = word.lower()
        currentNode = self.root
        for c in w:
            node = currentNode.adjacents.get(c)
            if node is None:
                node = TrieNode()
                node.value = c
                currentNode.adjacents[node.value] = node
                self.lista.append(currentNode.value)
            currentNode = node
        currentNode.isEndofWord = True
        return

    def search_prefix(self, word: str):
        if not isinstance(word, str):
            return TypeError
        lowerCaseWord = word.lower()
        currentNode = self.root
        for c in lowerCaseWord:
            currentNode = currentNode.adjacents.get(c)
            if currentNode is None:
                return False
        return currentNode

    def _collect_words(self, prefix_node: TrieNode, prefix: str, words: list):
        if prefix_node.isEndofWord:
            words.append(prefix)
        for adj_value, adj_node in prefix_node.adjacents.items():
            self._collect_words(adj_node, prefix + adj_value, words)

    def get_words(self, prefix: str):
        words = []
        prefix_node = self.search_prefix(prefix)
        if prefix_node:
            self._collect_words(prefix_node, prefix, words)
        return words


trieNode = TrieNode()
t = Trie(trieNode)
t.insert("agua")
t.insert("aguacate")
t.insert("baguacero")
t.insert("acua")
t.insert("Albacete")
t.insert("agupuntura")
t.insert("agoalete")

print(t.get_words("agua"))
print(t.get_words("a"))
print(t.lista)
