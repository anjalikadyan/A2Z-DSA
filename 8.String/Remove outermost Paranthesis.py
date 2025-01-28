s="((()))(())"
def removeOuterParentheses(self, s: str) -> str:
    d=[]
    ans=0
    for i in s:
        if i=="(":
            if ans>0:
                d.append(i)
            ans+=1
        if i==")":
            ans-=1
            if ans>0:
                d.append(i)
    return "".join(d)
print(removeOuterParentheses(s))