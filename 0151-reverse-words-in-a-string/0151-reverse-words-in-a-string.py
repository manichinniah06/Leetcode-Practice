class Solution:
    def reverseWords(self, s: str) -> str:
        temp = ""
        wordlist = []

        for i in s:
            if i != " ":
                temp += i
            else:
                if temp != "":
                    wordlist.append(temp)
                    temp = ""

        if temp != "":
            wordlist.append(temp)

        returnstring = ""

        for i in wordlist[::-1]:
            returnstring += i + " "

        return returnstring.strip()