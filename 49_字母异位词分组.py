class Solution:
    def groupAnagrams(self, strs: List[str]):
        ret = {}
        for string in strs:
            ret.setdefault(self.get_sorted_str(string),[]).append(string)
        return list(ret.values())
    def get_sorted_str(self, string):
        return ''.join(sorted(string))