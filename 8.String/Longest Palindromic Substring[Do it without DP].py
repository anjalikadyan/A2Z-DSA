s = "babad"

def expandAroundCenter(self,s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  

        if not s or len(s) == 1:
            return s
        
def longestPalindrome(self, s):
        longest = ""
        
        for i in range(len(s)):
            odd_pal = self.expandAroundCenter(s, i, i)
            even_pal = self.expandAroundCenter(s, i, i + 1)
            
            if len(odd_pal) > len(longest):
                longest = odd_pal
            if len(even_pal) > len(longest):
                longest = even_pal
        
        return longest
print(longestPalindrome(s))