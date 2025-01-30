
strs = ["flower","flow","flight"]
def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        pre = strs[0]
        for string in strs[1:]:
            while string[:len(pre)] != pre:
                pre = pre[:-1]
                if not pre:
                    return ""
        return pre
print(longestCommonPrefix(strs))