# Trie is data structure which is used for the information retreival.
# search through the strings to see the words are present or not.


class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_end_of_word = False

        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _character_index(self, char):
        if char.isupper():
            return ord(char) - ord('A')
        else:
            return ord(char) - ord('a')

    def insert(self, string):
        pointer = self.root
        for character in string:
            index = self._character_index(character)
            if not pointer.children[index]:
                pointer.children[index] = TrieNode()
            pointer = pointer.children[index]
        pointer.is_end_of_word = True
        return

    def search(self, string):
        pointer = self.root
        for character in string:
            index = self._character_index(character)
            if not pointer.children[index]:
                return False
            pointer = pointer.children[index]
        return pointer and pointer.is_end_of_word


my_trie = Trie()
my_trie.insert('Data')
my_trie.insert("Structures")
my_trie.insert("and")
my_trie.insert("Algorithms")
print(my_trie.search("and"))
# True
print(my_trie.search("Data"))
# True
print(my_trie.search("woohoo"))
# False
print(my_trie.search("STructures"))
# True

