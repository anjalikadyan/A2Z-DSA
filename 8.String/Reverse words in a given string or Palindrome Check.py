s="i am a student in collage"
def reverseWords(self, s: str) -> str:
    f=s.split()
    d=f[::-1]
    return ' '.join(d)
print(reverseWords(s))