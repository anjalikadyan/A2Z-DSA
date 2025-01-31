s = "(1+(2*3)+((8)/4))+1"

def maxDepth(self, s):
        sum=0
        maxi=0
        for i in range(len(s)):
            if s[i]=='(':
                sum+=1
            if s[i]==")":
                sum-=1
            maxi=max(maxi,sum)
        return maxi
print(maxDepth(s))