class CustomHashMap:

    def __init__(self):
        self.data = {}

    def put(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def contains(self, key):
        return key in self.data

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()


class TrieNode:

    def __init__(self):
        self.children = {}
        self.product_ids = []
        self.end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, product_id):

        node = self.root

        for ch in word.lower():

            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

            if product_id not in node.product_ids:
                node.product_ids.append(product_id)

        node.end = True

    def get_suggestions(self, prefix):

        node = self.root

        for ch in prefix.lower():

            if ch not in node.children:
                return []

            node = node.children[ch]

        return node.product_ids