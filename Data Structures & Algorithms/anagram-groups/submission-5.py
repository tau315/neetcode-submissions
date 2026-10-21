class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            letters = [0] * 26
            for char in string:
                letters[ord(char) - ord('a')] += 1
            
            group = anagrams.get(tuple(letters), [])
            group.append(string)
            anagrams[tuple(letters)] = group
        ans = []
        for key, value in anagrams.items():
            ans.append(value)
        return ans
         
                
            
            
        