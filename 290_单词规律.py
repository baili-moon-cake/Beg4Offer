class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_list = s.split(' ')
        if len(pattern) != len(word_list):
            return False
        hashmap = {}
        for char, word in zip(pattern, word_list):
            if hashmap.setdefault(word, char) != char:
                return False
        if len(set(hashmap.values())) != len(hashmap.values()):
            return False
        else:
            return True