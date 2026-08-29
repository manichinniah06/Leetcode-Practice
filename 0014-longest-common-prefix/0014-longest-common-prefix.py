class Solution:

    def checkif(strs, index):
        ch = strs[0][index]

        for i in strs:
            if index >= len(i) or i[index] != ch:
                return False

        return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonprefix = ""

        for i in range(len(strs[0])):
            if Solution.checkif(strs, i):
                commonprefix += strs[0][i]
            else:
                break

        return commonprefix