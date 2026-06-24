class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        structs = {}
        for string in strs:
            m = [0]*26
            for c in string:
                m[ord(c) - ord('a')] += 1
            if tuple(m) in structs:
                structs[tuple(m)].append(string)
            else:
                structs[tuple(m)] = [string]
        ans = []
        for val in structs.values():
            ans.append(val)
        return ans
         
                
            
            
        