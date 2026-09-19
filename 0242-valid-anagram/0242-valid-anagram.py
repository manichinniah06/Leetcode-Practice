class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_t = {}
        dict_s = {}

        for i in range(len(s)):
            if s[i] in dict_s:
                dict_s[s[i]] += 1
            else:
                dict_s[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] in dict_t:
                dict_t[t[i]] += 1
            else:
                dict_t[t[i]] = 1

        count = 0
        
        for i,j in dict_t.items():
            if i in dict_s:
                if j == dict_s[i]:
                    count += 1
        
        if count == len(dict_t):
            return True
        
        return False